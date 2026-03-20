'''
Description: Reads integers from the user until the sentinel value 15
            is entered, then counts how many numbers exceed 23.
'''

from utils import get_int


SENTINEL = 15
THRESHOLD = 23


def collect_numbers() -> list[int]:
    """
    Collect integers from the user until the sentinel value (15) is entered.

    Returns:
        A list of all integers entered before the sentinel.
    """
    numbers: list[int] = []
    print(f"  Enter integers (enter {SENTINEL} to finish):")

    while True:
        value = get_int("  Number: ")
        
        numbers.append(value)
        
        if value == SENTINEL:
            break
    return numbers


def count_above_threshold(numbers: list[int], threshold: int) -> int:
    """
    Count how many values in *numbers* are strictly greater than *threshold*.

    Args:
        numbers:   List of integers to examine.
        threshold: The comparison boundary.

    Returns:
        The count of elements where element > threshold.
    """
    return sum(1 for n in numbers if n > threshold)


def task2() -> None:
    """
    Business function for Task 2.

    Collects integers from the user (stopping at sentinel 15),
    then reports how many of them are greater than 23.
    """
    print("  TASK 2 — Count numbers greater than 23")

    numbers = collect_numbers()

    if not numbers:
        print("  No numbers were entered (only the sentinel was received).")
        return

    result = count_above_threshold(numbers, THRESHOLD)
    print(f"\n  Numbers entered: {numbers}")
    print(f"  Count of numbers greater than {THRESHOLD}: {result}")