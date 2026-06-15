"""Store URL registry."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Store:
    """Reservation store definition."""

    key: str
    name: str
    url: str


STORES: dict[str, Store] = {
    "osaka": Store(
        key="osaka",
        name="大阪",
        url="https://reservation.rolexboutique-hiltonplaza-osaka.jp/osaka-umeda/reservation",
    ),
    "ginza": Store(
        key="ginza",
        name="銀座",
        url="https://reservation.rolexboutique-lexia.jp/ginza/reservation",
    ),
    "omotesando": Store(
        key="omotesando",
        name="表参道",
        url="https://reservation.rolexboutique-omotesando-tokyo.jp/omotesando/reservation?func_distinction=1",
    ),
    "shinjuku": Store(
        key="shinjuku",
        name="新宿",
        url="https://reservation.rolexboutique-lexia.jp/shinjuku/reservation",
    ),
    "nagoya-sakae": Store(
        key="nagoya-sakae",
        name="名古屋栄",
        url="https://reservation.rolexboutique-lexia.jp/nagoya-sakae/reservation",
    ),
}


def get_store(key: str) -> Store:
    """Return a store by key."""

    normalized = key.strip().lower()
    try:
        return STORES[normalized]
    except KeyError as exc:
        choices = ", ".join(sorted(STORES))
        raise ValueError(f"Unknown store '{key}'. Choose one of: {choices}") from exc
