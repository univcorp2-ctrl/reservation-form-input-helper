"""Flexible selector candidates for Japanese reservation forms.

The helper uses multiple conservative candidates because the production form may
change names, IDs, labels, and placeholders. Missing selectors are ignored.
"""

from __future__ import annotations

FIELD_SELECTORS: dict[str, list[str]] = {
    "last_name": [
        "input[name='last_name']",
        "input[name='family_name']",
        "input[name='sei']",
        "input[id*='last'][type='text']",
        "input[placeholder*='姓']",
        "input[aria-label*='姓']",
    ],
    "first_name": [
        "input[name='first_name']",
        "input[name='given_name']",
        "input[name='mei']",
        "input[id*='first'][type='text']",
        "input[placeholder*='名']",
        "input[aria-label*='名']",
    ],
    "full_name": [
        "input[name='name']",
        "input[id='name']",
        "input[placeholder*='お名前']",
        "input[aria-label*='お名前']",
    ],
    "last_name_kana": [
        "input[name='last_name_kana']",
        "input[name='family_name_kana']",
        "input[name='sei_kana']",
        "input[placeholder*='セイ']",
        "input[aria-label*='セイ']",
    ],
    "first_name_kana": [
        "input[name='first_name_kana']",
        "input[name='given_name_kana']",
        "input[name='mei_kana']",
        "input[placeholder*='メイ']",
        "input[aria-label*='メイ']",
    ],
    "full_name_kana": [
        "input[name='kana']",
        "input[name='name_kana']",
        "input[placeholder*='フリガナ']",
        "input[aria-label*='フリガナ']",
    ],
    "email": [
        "input[name='email']",
        "input[type='email']",
        "input[placeholder*='メール']",
        "input[aria-label*='メール']",
    ],
    "email_confirm": [
        "input[name='email_confirmation']",
        "input[name='email_confirm']",
        "input[name='confirm_email']",
        "input[placeholder*='確認'][placeholder*='メール']",
        "input[aria-label*='確認'][aria-label*='メール']",
    ],
    "phone": [
        "input[name='phone']",
        "input[name='tel']",
        "input[type='tel']",
        "input[placeholder*='電話']",
        "input[aria-label*='電話']",
    ],
    "postal_code": [
        "input[name='postal_code']",
        "input[name='zip']",
        "input[name='zipcode']",
        "input[placeholder*='郵便']",
        "input[aria-label*='郵便']",
    ],
    "prefecture": [
        "select[name='prefecture']",
        "input[name='prefecture']",
        "select[aria-label*='都道府県']",
        "input[placeholder*='都道府県']",
    ],
    "city": [
        "input[name='city']",
        "input[placeholder*='市区町村']",
        "input[aria-label*='市区町村']",
    ],
    "address1": [
        "input[name='address1']",
        "input[name='address']",
        "input[placeholder*='住所']",
        "input[aria-label*='住所']",
    ],
    "address2": [
        "input[name='address2']",
        "input[placeholder*='建物']",
        "input[aria-label*='建物']",
    ],
    "birth_year": [
        "select[name='birth_year']",
        "input[name='birth_year']",
        "select[aria-label*='年']",
        "input[placeholder*='年']",
    ],
    "birth_month": [
        "select[name='birth_month']",
        "input[name='birth_month']",
        "select[aria-label*='月']",
        "input[placeholder*='月']",
    ],
    "birth_day": [
        "select[name='birth_day']",
        "input[name='birth_day']",
        "select[aria-label*='日']",
        "input[placeholder*='日']",
    ],
    "visit_date": [
        "input[name='date']",
        "input[name='visit_date']",
        "select[name='visit_date']",
        "input[type='date']",
    ],
    "visit_time": [
        "select[name='time']",
        "select[name='visit_time']",
        "input[name='visit_time']",
    ],
    "message": [
        "textarea[name='message']",
        "textarea[name='note']",
        "textarea[placeholder*='備考']",
        "textarea[aria-label*='備考']",
    ],
}

CHECKBOX_LABELS: dict[str, list[str]] = {
    "privacy": [
        "個人情報取り扱いに同意する",
        "個人情報取扱いに同意する",
        "個人情報保護ポリシー",
        "handling of personal information",
    ],
    "business_notice": [
        "営業についてのお知らせに同意する",
        "営業についてはこちら",
        "business notice",
    ],
}

CONFIRM_BUTTON_NAMES = [
    "入力内容確認",
    "Input content confirmation",
    "確認",
    "Confirm",
]
