import pytest

from reservation_input_helper.stores import STORES, get_store


def test_get_store_known():
    assert get_store("ginza").url.startswith("https://reservation.rolexboutique-lexia.jp")


def test_all_store_urls_are_https():
    assert all(store.url.startswith("https://") for store in STORES.values())


def test_get_store_unknown():
    with pytest.raises(ValueError):
        get_store("unknown")
