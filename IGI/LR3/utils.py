'''
Description: Reusable helpers — input validation, repeat-loop, and decorators.
'''

import time
import functools


def timing_decorator(func):
    """
    Decorator that measures and prints the execution time of a function.

    Args:
        func: The function to wrap.

    Returns:
        wrapper: The wrapped function with timing output.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[Timer] '{func.__name__}' finished in {elapsed:.6f} seconds.")
        return result
    return wrapper


def get_int(prompt: str, *, min_val: int = None, max_val: int = None) -> int:
    """
    Prompt the user for an integer, repeating on bad input.

    Args:
        prompt:  Text shown to the user.
        min_val: Optional minimum accepted value (inclusive).
        max_val: Optional maximum accepted value (inclusive).

    Returns:
        A validated integer entered by the user.

    Raises:
        KeyboardInterrupt: If the user presses Ctrl+C (propagated).
    """
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                print("  Error: input cannot be empty. Please try again.")
                continue
            value = int(raw)
            if min_val is not None and value < min_val:
                print(f"  Error: value must be >= {min_val}. Please try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Error: value must be <= {max_val}. Please try again.")
                continue
            return value
        except ValueError:
            print("  Error: please enter a valid integer.")


def get_float(prompt: str, *, min_val: float = None, max_val: float = None) -> float:
    """
    Prompt the user for a float, repeating on bad input.

    Args:
        prompt:  Text shown to the user.
        min_val: Optional minimum accepted value (inclusive).
        max_val: Optional maximum accepted value (inclusive).

    Returns:
        A validated float entered by the user.
    """
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                print("  Error: input cannot be empty. Please try again.")
                continue
            value = float(raw)
            if min_val is not None and value < min_val:
                print(f"  Error: value must be >= {min_val}. Please try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"  Error: value must be <= {max_val}. Please try again.")
                continue
            return value
        except ValueError:
            print("  Error: please enter a valid number (e.g. 0.001 or 1e-6).")


def ask_repeat() -> bool:
    """
    Ask the user whether they want to run the task again.

    Returns:
        True if the user wants to repeat, False otherwise.
    """
    while True:
        answer = input("\nRun again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("  Please enter 'yes' or 'no'.")


def run_with_repeat(task_func):
    """
    Run *task_func* in a loop, asking the user to repeat after each run.

    Args:
        task_func: A callable (no arguments) representing a single task run.
    """
    while True:
        task_func()
        if not ask_repeat():
            break