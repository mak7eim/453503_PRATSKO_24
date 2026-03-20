'''
Description: Determines whether a user-supplied string represents
            a valid hexadecimal number.
'''


_HEX_CHARS = frozenset('0123456789ABCDEFabcdef')


def is_hex_string(s: str) -> bool:
    """
    Check whether *s* is a non-empty string containing only hexadecimal digits.

    Valid hex digits are: 0-9, A-F, a-f (case-insensitive).

    Args:
        s: The string to validate.

    Returns:
        True if *s* is a valid hexadecimal string, False otherwise.

    Raises:
        TypeError: If *s* is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}.")
    if not s:
        return False
    return all(ch in _HEX_CHARS for ch in s)


def get_nonempty_string(prompt: str) -> str:
    """
    Prompt the user for a non-empty string, repeating until one is provided.

    Args:
        prompt: Text displayed to the user.

    Returns:
        A non-empty string entered by the user.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Error: input cannot be empty. Please try again.")


def task3() -> None:
    """
    Business function for Task 3.

    Reads a string from the user and reports whether it is a valid
    hexadecimal number.
    """
    print("  TASK 3 — Check whether a string is hexadecimal")

    text = get_nonempty_string("  Enter a string: ")

    try:
        if is_hex_string(text):
            print(f"  Result: '{text}' IS a valid hexadecimal number.")
        else:
            print(f"  Result: '{text}' is NOT a valid hexadecimal number.")
    except TypeError as exc:
        print(f"  Type error: {exc}")