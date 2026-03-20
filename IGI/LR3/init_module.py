'''
Description: Provides two strategies for populating a list —
            via a random-number generator and via manual user input.
            Both functions receive the target list and fill it in-place.
'''


import random
from utils import get_int


def init_from_generator(sequence: list, n: int,
                        low: int = -100, high: int = 100) -> None:
    """
    Fill *sequence* with *n* random integers in the range [low, high].

    Args:
        sequence: The list to be populated (modified in-place).
        n:        Number of elements to generate.
        low:      Lower bound for random values (inclusive).
        high:     Upper bound for random values (inclusive).

    Raises:
        ValueError: If n <= 0 or low > high.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if low > high:
        raise ValueError("low must be <= high.")

    sequence.clear()
    sequence.extend(random.randint(low, high) for _ in range(n))
    print(f"  List of {n} elements generated randomly in [{low}, {high}].")


def init_from_user(sequence: list, n: int) -> None:
    """
    Fill *sequence* with *n* integers entered interactively by the user.

    Args:
        sequence: The list to be populated (modified in-place).
        n:        Number of elements to read from the user.

    Raises:
        ValueError: If n <= 0.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    sequence.clear()
    print(f"  Enter {n} integers:")
    for i in range(n):
        value = get_int(f"    Element [{i + 1}]: ")
        sequence.append(value)
    print("  List successfully filled from user input.")


def choose_init_method(sequence: list, n: int) -> None:
    """
    Interactively ask the user which initialization method to use,
    then delegate to the appropriate function.

    Args:
        sequence: The list to be populated (modified in-place).
        n:        Number of elements required.
    """
    print("\nChoose initialization method:\n")
    print("1 — Random generator")
    print("2 — Manual user input")

    choice = get_int("\nYour choice (1 or 2): ", min_val=1, max_val=2)

    if choice == 1:
        init_from_generator(sequence, n)
    else:
        init_from_user(sequence, n)