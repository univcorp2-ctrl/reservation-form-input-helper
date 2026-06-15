from reservation_input_helper.profile import load_profile


def test_load_profile_defaults_email_confirm(monkeypatch):
    monkeypatch.setenv("RESERVATION_EMAIL", "user@example.com")
    monkeypatch.delenv("RESERVATION_EMAIL_CONFIRM", raising=False)

    profile = load_profile(env_file=None)

    assert profile.email == "user@example.com"
    assert profile.email_confirm == "user@example.com"


def test_load_profile_business_notice_bool(monkeypatch):
    monkeypatch.setenv("RESERVATION_AGREE_BUSINESS_NOTICE", "true")

    profile = load_profile(env_file=None)

    assert profile.agree_business_notice is True
