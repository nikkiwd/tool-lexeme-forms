"""Module to convert between different kinds of language codes.

There are three kinds of language codes relevant for this tool:
- MediaWiki language codes
- HTML language codes (aka BCP47 language tags)
- Babel language codes

Additionally, MediaWiki language codes differ by usage between:
- lexicographical data language codes
- user interface language codes

Templates specify lexicographical data MediaWiki language codes;
translations are given for user interface language codes.

These language codes cannot be converted to one another losslessly,
and this module does not provide functions for all possible
conversions; rather, it only implements conversions to less specific
codes, which may lose some information."""


def lang_lex2int(code):
    """Convert a MediaWiki language code from lexicographical data usage
    to user interface usage."""

    return {
        # Manbhumi reuses the standard Bengali messages
        'bn-x-Q6747180': 'bn',
    }.get(code, code)


def lang_int2html(code):
    """Convert a MediaWiki user interface language code to an HTML one."""

    # no changes needed so far
    return code


def lang_int2babel(code):
    """Convert a MediaWiki user interface language code to a Babel one."""

    # remove everything after -, interpreted differently by Babel
    code, separator, rest = code.partition('-')
    return {
        # Latin is not in CLDR, English is similar for our purposes
        'la': 'en',
    }.get(code, code)
