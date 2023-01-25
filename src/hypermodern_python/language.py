import enum
import locale
import ctypes
import os


class Language(str, enum.Enum):
    FRENCH = "french"
    ENGLISH = "english"
    OTHER = "other"

    @classmethod
    def from_preferences(cls) -> "Language":
        if os.name == "posix":
            return cls._from_preferences_posix()
        else:
            return cls._from_preferences_windows()

    @classmethod
    def _from_preferences_posix(cls) -> "Language":
        language = os.environ['LANG']
        return cls.from_str(language)

    @classmethod
    def _from_preferences_windows(cls) -> "Language":
        windll = ctypes.windll.kernel32
        windll.GetUserDefaultUILanguage()
        language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        return cls.from_str(language)

    @classmethod
    def from_str(cls, language: str) -> "Language":
        language = language.lower()
        if "fr" in language:
            return cls.FRENCH
        elif "en" in language:
            return cls.ENGLISH
        else:
            return cls.OTHER
