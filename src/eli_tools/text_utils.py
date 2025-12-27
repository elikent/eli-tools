"""
Utilities for normalizing and cleaning up text.
"""
import logging
import unicodedata
import re

logger = logging.getLogger(__name__)

#----------------------------------------- remove_diacritics() is part of canon()---------------------------------------------
def remove_diacritics(text: str) -> str:
    """Return text without accents/diacritics.

    Example:
        >>> remove_diacritics("Señor Niño")
        'Senor Nino'
    """
    nfkd_form = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in nfkd_form if not unicodedata.combining(ch))

def canon(name: str) -> str:
    """Canonicalize a filename or text string for matching.

    - Remove diacritics
    - Lowercase
    - Normalize dashes/underscores to spaces
    - Collapse multiple spaces
    - Strip leading/trailing spaces

    Example:
        >>> canon(" Recíbo---de_dopaje.PDF ")
        'recibo de dopaje.pdf'
    """
    # remove diacritics
    s = remove_diacritics(name)
    # lowercase
    s = s.lower()
    # normalize dashes/underscores to spaces
    s = re.sub(r"[-_]+", " ", s)
    # collapse multiple spaces
    s = re.sub(r"\s+", " ", s)
    # strip leading/trailing spaces
    s = s.strip()
    return s

def normalize_name(name: str) -> str:
    """
    Normalize names FOR MATCHING

    - canonizes
    - removes .
    """

    #canonize
    s = canon(name)

    # remove dots preceded by a letter (e.g. "jose m." -> "jose m")
    s = re.sub(r'(?<=[A-Za-z])\.', '', s)

    # collapse multiple spaces (dot removal can create double spaces)
    s = re.sub(r"\s+", " ", s).strip()

    return s


def normalize_email(email: str, *, username: bool = False) -> str:
    """
    Normalize emails FOR MATCHING

    - Lowercase
    - Strip surrounding whitespace
    - Remove internal spaces (common data error)
    - if username = True, return only local part (before '@')

    DOES NOT:
    - Remove dots
    - Remove tags
    - Change domains
    - Check for '@'
    """

    if not email:
        return ""

    if not isinstance(email, str):
        logger.debug(
            'normalize_email received a non-string value: %r (%s)',
            email,
            type(email).__name__,
        )
        email = str(email)

    s = email.strip().lower()
    s = s.replace(' ', '')

    if username:
        return s.split('@', 1)[0]
    else:
        return s

def normalize_phone(phone: str) -> str:
    """
    Normalize US phone numbers FOR MATCIHNG

    - Keep digits only
    - Normalize to 10 digits
    - Drop leading 1 if present

    DOES NOT:
    - Validate phone (ensure 10 digits)
    """

    if not phone:
        return ""

    # cast to str if not str
    if isinstance(phone, str):
        logger.debug(
            'normalize_phone received a non-string value: %r, (%s)',
            phone,
            type(phone).__name__
        )
        phone = str(phone)

    # strip to digits only
    digits = re.sub(r'\D', '', phone)

    # drop us country code if present
    if len(digits) == 11 and digits.startswith('1'):
        digits = digits[1:]

    return digits
