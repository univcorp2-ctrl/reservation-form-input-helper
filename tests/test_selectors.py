from reservation_input_helper.selectors import CHECKBOX_LABELS, CONFIRM_BUTTON_NAMES, FIELD_SELECTORS


def test_core_fields_have_selectors():
    for field in ["last_name", "first_name", "email", "phone"]:
        assert field in FIELD_SELECTORS
        assert FIELD_SELECTORS[field]


def test_privacy_label_present():
    assert CHECKBOX_LABELS["privacy"]


def test_confirm_names_present():
    assert "入力内容確認" in CONFIRM_BUTTON_NAMES
