"""Profile loading from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


_TRUE_VALUES = {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True)
class ReservationProfile:
    """User profile values for form input assistance."""

    last_name: str = ""
    first_name: str = ""
    last_name_kana: str = ""
    first_name_kana: str = ""
    email: str = ""
    email_confirm: str = ""
    phone: str = ""
    postal_code: str = ""
    prefecture: str = ""
    city: str = ""
    address1: str = ""
    address2: str = ""
    birth_year: str = ""
    birth_month: str = ""
    birth_day: str = ""
    visit_date: str = ""
    visit_time: str = ""
    message: str = ""
    agree_business_notice: bool = False

    @property
    def full_name(self) -> str:
        return " ".join(part for part in [self.last_name, self.first_name] if part).strip()

    @property
    def full_name_kana(self) -> str:
        return " ".join(part for part in [self.last_name_kana, self.first_name_kana] if part).strip()


def load_profile(env_file: str | None = None) -> ReservationProfile:
    """Load profile from .env and process environment."""

    load_dotenv(env_file)
    email = os.getenv("RESERVATION_EMAIL", "")
    email_confirm = os.getenv("RESERVATION_EMAIL_CONFIRM", email)
    return ReservationProfile(
        last_name=os.getenv("RESERVATION_LAST_NAME", ""),
        first_name=os.getenv("RESERVATION_FIRST_NAME", ""),
        last_name_kana=os.getenv("RESERVATION_LAST_NAME_KANA", ""),
        first_name_kana=os.getenv("RESERVATION_FIRST_NAME_KANA", ""),
        email=email,
        email_confirm=email_confirm,
        phone=os.getenv("RESERVATION_PHONE", ""),
        postal_code=os.getenv("RESERVATION_POSTAL_CODE", ""),
        prefecture=os.getenv("RESERVATION_PREFECTURE", ""),
        city=os.getenv("RESERVATION_CITY", ""),
        address1=os.getenv("RESERVATION_ADDRESS1", ""),
        address2=os.getenv("RESERVATION_ADDRESS2", ""),
        birth_year=os.getenv("RESERVATION_BIRTH_YEAR", ""),
        birth_month=os.getenv("RESERVATION_BIRTH_MONTH", ""),
        birth_day=os.getenv("RESERVATION_BIRTH_DAY", ""),
        visit_date=os.getenv("RESERVATION_VISIT_DATE", ""),
        visit_time=os.getenv("RESERVATION_VISIT_TIME", ""),
        message=os.getenv("RESERVATION_MESSAGE", ""),
        agree_business_notice=os.getenv("RESERVATION_AGREE_BUSINESS_NOTICE", "").lower() in _TRUE_VALUES,
    )
