import ctypes
import enum
import locale
import os


class Language(str, enum.Enum):
    FRENCH = "french"
    ENGLISH = "english"
    OTHER = "other"

    @classmethod
    def from_preferences(cls) -> "Language":
        if os.name == "posix":
            return cls._from_preferences_posix()
        elif os.name == "nt":
            return cls._from_preferences_windows()
        else:
            raise RuntimeError(f"Unsupported operating system: {os.name}.")

    @classmethod
    def _from_preferences_posix(cls) -> "Language":
        language = os.environ["LANG"]
        return cls.from_str(language)

    @classmethod
    def _from_preferences_windows(cls) -> "Language":
        windll = ctypes.windll.kernel32  # type: ignore
        language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        return cls.from_str(language)

    @classmethod
    def from_str(cls, language: str) -> "Language":
        language = language.lower()
        if language.startswith("fr"):
            return cls.FRENCH
        elif language.startswith("en"):
            return cls.ENGLISH
        else:
            return cls.OTHER
