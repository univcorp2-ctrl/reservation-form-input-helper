"""Command line entrypoint."""

from __future__ import annotations

import argparse
import asyncio

from reservation_input_helper.fill import open_and_fill
from reservation_input_helper.profile import load_profile
from reservation_input_helper.stores import STORES, get_store


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Open a reservation page and fill user-provided profile fields. Stops before CAPTCHA/final submit."
    )
    parser.add_argument("--store", required=True, choices=sorted(STORES), help="Store key to open")
    parser.add_argument("--env-file", default=".env", help="Path to env file")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode. Not recommended for manual CAPTCHA.")
    parser.add_argument("--slow-mo-ms", type=int, default=80, help="Playwright slow_mo in milliseconds")
    parser.add_argument(
        "--click-confirm",
        action="store_true",
        help="Click the input confirmation button after filling. CAPTCHA/final submission are still manual.",
    )
    parser.add_argument("--stay-open-seconds", type=int, default=600, help="Seconds to keep browser open after filling")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    store = get_store(args.store)
    profile = load_profile(args.env_file)
    asyncio.run(
        open_and_fill(
            store,
            profile,
            headless=args.headless,
            slow_mo_ms=args.slow_mo_ms,
            click_confirm=args.click_confirm,
            stay_open_seconds=args.stay_open_seconds,
        )
    )


if __name__ == "__main__":
    main()
