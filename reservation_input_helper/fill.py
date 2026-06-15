"""Playwright-based form fill routines."""

from __future__ import annotations

import asyncio
from dataclasses import asdict
from typing import Iterable

from playwright.async_api import Locator, Page, TimeoutError as PlaywrightTimeoutError

from reservation_input_helper.profile import ReservationProfile
from reservation_input_helper.selectors import CHECKBOX_LABELS, CONFIRM_BUTTON_NAMES, FIELD_SELECTORS
from reservation_input_helper.stores import Store


def _value_for_field(profile: ReservationProfile, field: str) -> str:
    if field == "full_name":
        return profile.full_name
    if field == "full_name_kana":
        return profile.full_name_kana
    value = asdict(profile).get(field, "")
    return str(value or "")


async def _first_visible(page: Page, selectors: Iterable[str], timeout_ms: int = 350) -> Locator | None:
    for selector in selectors:
        locator = page.locator(selector).first
        try:
            await locator.wait_for(state="visible", timeout=timeout_ms)
            return locator
        except PlaywrightTimeoutError:
            continue
    return None


async def fill_field(page: Page, selectors: list[str], value: str) -> bool:
    """Fill or select the first visible matching field."""

    if not value:
        return False
    locator = await _first_visible(page, selectors)
    if locator is None:
        return False

    tag_name = (await locator.evaluate("el => el.tagName.toLowerCase()")) or ""
    if tag_name == "select":
        try:
            await locator.select_option(label=value)
            return True
        except Exception:
            await locator.select_option(value=value)
            return True

    await locator.fill(value)
    return True


async def click_checkbox_by_labels(page: Page, labels: list[str]) -> bool:
    """Click first checkbox that appears to be associated with one of labels."""

    for label in labels:
        try:
            checkbox = page.get_by_label(label, exact=False).first
            await checkbox.wait_for(state="visible", timeout=400)
            if not await checkbox.is_checked():
                await checkbox.check()
            return True
        except Exception:
            pass

    # Fallback for custom label layouts where the checkbox itself has no label.
    for label in labels:
        text = page.get_by_text(label, exact=False).first
        try:
            await text.wait_for(state="visible", timeout=400)
            nearest = text.locator("xpath=ancestor::*[self::label or self::div or self::li][1]//input[@type='checkbox']").first
            await nearest.wait_for(state="attached", timeout=250)
            if not await nearest.is_checked():
                await nearest.check(force=True)
            return True
        except Exception:
            continue
    return False


async def click_confirm_button(page: Page) -> bool:
    """Optionally click a visible confirm button."""

    for name in CONFIRM_BUTTON_NAMES:
        try:
            button = page.get_by_role("button", name=name, exact=False).first
            await button.wait_for(state="visible", timeout=400)
            await button.click()
            return True
        except Exception:
            pass
        try:
            link_or_input = page.locator(
                f"input[type='submit'][value*='{name}'], input[type='button'][value*='{name}'], a:has-text('{name}')"
            ).first
            await link_or_input.wait_for(state="visible", timeout=400)
            await link_or_input.click()
            return True
        except Exception:
            continue
    return False


async def fill_reservation_form(
    page: Page,
    profile: ReservationProfile,
    *,
    agree_privacy: bool = True,
    agree_business_notice: bool | None = None,
) -> dict[str, bool]:
    """Fill known fields and consent checkboxes.

    Returns a map of attempted item name to success status.
    """

    results: dict[str, bool] = {}
    for field, selectors in FIELD_SELECTORS.items():
        results[field] = await fill_field(page, selectors, _value_for_field(profile, field))

    if agree_privacy:
        results["privacy_checkbox"] = await click_checkbox_by_labels(page, CHECKBOX_LABELS["privacy"])

    should_agree_business = profile.agree_business_notice if agree_business_notice is None else agree_business_notice
    if should_agree_business:
        results["business_notice_checkbox"] = await click_checkbox_by_labels(page, CHECKBOX_LABELS["business_notice"])

    return results


async def open_and_fill(
    store: Store,
    profile: ReservationProfile,
    *,
    headless: bool = False,
    slow_mo_ms: int = 80,
    click_confirm: bool = False,
    stay_open_seconds: int = 600,
) -> dict[str, bool]:
    """Open reservation page and fill fields, stopping before human-only steps."""

    from playwright.async_api import async_playwright

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless, slow_mo=slow_mo_ms)
        context = await browser.new_context(locale="ja-JP", timezone_id="Asia/Tokyo")
        page = await context.new_page()
        await page.goto(store.url, wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        results = await fill_reservation_form(page, profile)

        if click_confirm:
            results["confirm_button"] = await click_confirm_button(page)

        print("\n入力補助が完了しました。CAPTCHA と最終送信は人が画面を確認して行ってください。")
        print("結果:")
        for name, ok in results.items():
            print(f"- {name}: {'ok' if ok else 'not found/skipped'}")
        print(f"\nブラウザを {stay_open_seconds} 秒開いたままにします。")
        await asyncio.sleep(stay_open_seconds)
        await context.close()
        await browser.close()

    return results
