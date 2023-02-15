import os

import pytest
import pytest_mock

from hypermodern_python.wikipedia.language import Language


def test_init() -> None:
    _ = Language.FRENCH
    _ = Language.ENGLISH
    _ = Language.OTHER


def test_from_preferences_os_posix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(os, "name", "posix")
    monkeypatch.setattr(Language, "_from_preferences_posix", lambda: Language.FRENCH)
    assert Language.from_preferences() == Language.FRENCH


def test_from_preferences_os_windows(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(os, "name", "windows")
    monkeypatch.setattr(Language, "_from_preferences_windows", lambda: Language.FRENCH)
    assert Language.from_preferences() == Language.FRENCH


def test_from_preferences_posix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(os, "environ", {"LANG": "fr"})
    monkeypatch.setattr(Language, "from_str", lambda: Language.FRENCH)


def test_from_preferences_windows(mocker: pytest_mock.MockerFixture) -> None:
    mock_windll = mocker.patch("ctypes.windll", create=True)
    mock_windll.kernel32.GetUserDefaultUILanguage.return_value = 42
    mocker.patch("locale.windows_locale", new={42: "english"})
    result = Language._from_preferences_windows()
    assert result == Language.ENGLISH


def test_from_str() -> None:
    for detected_french in ("french", "fr", "FRENCH", "Fr", "fr031"):
        assert Language.from_str(detected_french) == Language.FRENCH

    for detected_english in ("english", "en", "ENGLISH", "En", "En131"):
        assert Language.from_str(detected_english) == Language.ENGLISH

    for detected_other in ("other", "OTHER", "polish", "fancy", "es"):
        assert Language.from_str(detected_other) == Language.OTHER
