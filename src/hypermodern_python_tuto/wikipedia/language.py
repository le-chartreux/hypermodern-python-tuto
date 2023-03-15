"""Language enum declaration."""
import ctypes
import enum
import locale
import os


class Language(str, enum.Enum):
    """Supported languages for the pages on the Wikipedia API (non-exhaustive)."""

    FRENCH = "french"
    ENGLISH = "english"
    OTHER = "other"

    @classmethod
    def from_preferences(cls) -> "Language":
        """Search for the preferred language in the computer's settings.

        Since the computer settings vary a lot depending on the operating system,
        this function works on posix and Windows only.

        Returns:
            The preferred language.

        Raises:
            RuntimeError: If the os name is not posix or Windows.

        Examples:
            >>> language = Language.from_preferences()
            >>> isinstance(language, Language)
            True
        """
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
        """Convert a language name to its equivalent Enum.

        Args:
            language: The name of the language.

        Returns:
            The equivalent of the language in Enum.

        Warnings:
            Inaccurate because it works by looking for the beginning of the name,
            e.g. "fresh" will be detected as FRENCH.

        Examples:
            >>> Language.from_str("french") is Language.FRENCH
            True
            >>> Language.from_str("en") is Language.ENGLISH
            True
            >>> Language.from_str("unrecognized") is Language.OTHER
            True
        """
        language = language.lower()
        if language.startswith("fr"):
            return cls.FRENCH
        elif language.startswith("en"):
            return cls.ENGLISH
        else:
            return cls.OTHER
