'''
Description: Works with an integer list to:
    1) Count negative odd elements.
    2) Find the sum of elements before the last zero.
'''

from utils import get_int
from init_module import choose_init_method


def display_list(lst: list[int]) -> None:
    """
    Print all elements of *lst* in a readable format.

    Args:
        lst: The list to display.
    """
    if not lst:
        print("  (the list is empty)")
        return
    print("  Elements:", ", ".join(str(e) for e in lst))


def validate_list(lst: list[int]) -> bool:
    """
    Verify that *lst* is non-empty and contains only integers.

    Args:
        lst: The list to validate.

    Returns:
        True if valid, False otherwise.

    Raises:
        TypeError: If *lst* is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("Expected a list.")
    if not lst:
        return False
    return all(isinstance(x, int) for x in lst)


def count_negative_odd(lst: list[int]) -> int:
    """
    Count elements that are both negative and odd.

    Args:
        lst: List of integers.

    Returns:
        Number of negative odd elements.
    """
    return sum(1 for x in lst if x < 0 and x % 2 != 0)


def sum_before_last_zero(lst: list[int]) -> int | None:
    """
    Return the sum of all elements that appear before the last zero.

    Args:
        lst: List of integers.

    Returns:
        Sum of elements before the last zero element, or None if no zero exists.
        Returns 0 if the last zero is the first element.
    """
    last_zero_idx = None
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == 0:
            last_zero_idx = i
            break

    if last_zero_idx is None:
        return None

    return sum(lst[:last_zero_idx])


def task5() -> None:
    """
    Business function for Task 5.

    Lets the user choose the list size and initialization method,
    then computes and prints:
        1) The count of negative odd elements.
        2) The sum of elements before the last zero.
    """
    print("  TASK 5 — Integer list processing")

    n = get_int("  Enter the number of list elements: ", min_val=1, max_val=10_000)

    my_list: list[int] = []
    choose_init_method(my_list, n)

    print("\n  Entered list:")
    display_list(my_list)

    try:
        if not validate_list(my_list):
            print("  Error: the list is empty or contains invalid data.")
            return
    except TypeError as exc:
        print(f"  Validation error: {exc}")
        return

    # --- Result 1 ---
    neg_odd = count_negative_odd(my_list)
    print(f"\n  1) Negative odd elements: {neg_odd}")

    # --- Result 2 ---
    s = sum_before_last_zero(my_list)
    if s is None:
        print("  2) The list contains no zeros — sum cannot be computed.")
    else:
        print(f"  2) Sum of elements before the last zero: {s}")