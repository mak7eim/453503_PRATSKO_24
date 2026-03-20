'''
Description: Analyses a fixed text passage to find:
    1) Words consisting entirely of capital letters.
    2) The longest word starting with the letter 'l'.
    3) All words that appear more than once (with their frequencies).
'''

_SOURCE_TEXT = (
    "So she was considering in her own mind, as well as she could, "
    "for the hot day made her feel very sleepy and stupid, whether the pleasure of "
    "making a daisy-chain would be worth the trouble of getting up and picking the "
    "daisies, when suddenly a White Rabbit with pink eyes ran close by her."
)


def clean_word(word: str) -> str:
    """
    Strip leading/trailing punctuation from *word* and convert to lower case.

    Args:
        word: A raw token from the text.

    Returns:
        The cleaned, lower-cased word.
    """
    return word.strip('.,!?;:()"-').lower()


def tokenize(text: str) -> list[str]:
    """
    Split *text* into a list of raw word tokens.

    Args:
        text: The full source string.

    Returns:
        List of non-empty whitespace-separated tokens.
    """
    return [w for w in text.split() if w]


def find_all_caps_words(raw_tokens: list[str]) -> list[str]:
    """
    Return tokens that consist solely of uppercase alphabetic characters.

    Args:
        raw_tokens: Whitespace-split tokens (punctuation still attached).

    Returns:
        List of fully-uppercase words.
    """
    return [w for w in raw_tokens if w.isupper() and w.isalpha()]


def find_longest_l_word(cleaned_tokens: list[str]) -> str | None:
    """
    Return the longest word (cleaned, lowercase) that starts with 'l'.

    Args:
        cleaned_tokens: Tokens already stripped of punctuation and lower-cased.

    Returns:
        The longest 'l'-word, or None if no such word exists.
    """
    l_words = [w for w in cleaned_tokens if w.startswith('l')]
    return max(l_words, key=len) if l_words else None


def find_repeated_words(cleaned_tokens: list[str]) -> dict[str, int]:
    """
    Build a frequency map of words that appear more than once.

    Args:
        cleaned_tokens: Tokens already stripped of punctuation and lower-cased.

    Returns:
        Dictionary mapping each repeated word to its occurrence count,
        sorted by frequency in descending order.
    """
    freq: dict[str, int] = {}
    for word in cleaned_tokens:
        if word:
            freq[word] = freq.get(word, 0) + 1

    repeated = {w: c for w, c in freq.items() if c > 1}
    return dict(sorted(repeated.items(), key=lambda kv: kv[1], reverse=True))


def task4() -> None:
    """
    Business function for Task 4.

    Analyses the built-in text passage and prints:
        • count of all-caps words,
        • longest word starting with 'l',
        • all repeated words with their frequencies.
    """
    print("  TASK 4 — Text analysis")
    print("\n  Source text:")
    print(f"  {_SOURCE_TEXT}\n")

    raw_tokens = tokenize(_SOURCE_TEXT)
    cleaned_tokens = [clean_word(w) for w in raw_tokens]

    # --- 1) All-caps words ---
    caps_words = find_all_caps_words(raw_tokens)
    print(f"  1) Words in ALL CAPS: {len(caps_words)}  → {caps_words}")

    # --- 2) Longest word starting with 'l' ---
    longest_l = find_longest_l_word(cleaned_tokens)
    if longest_l:
        print(f"  2) Longest word starting with 'l': '{longest_l}'")
    else:
        print("  2) No words starting with 'l' were found.")

    # --- 3) Repeated words ---
    repeated = find_repeated_words(cleaned_tokens)
    print("  3) Repeated words:")
    if repeated:
        for word, count in repeated.items():
            print(f"       '{word}' — {count} times")
    else:
        print("       No repeated words found.")