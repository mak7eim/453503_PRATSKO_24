'''
Description: Computes ln(1+x) using the Taylor series expansion
            and compares the result with math.log.
'''

import math
from utils import get_float, timing_decorator


MAX_ITERATIONS = 500


@timing_decorator
def compute_series(x: float, eps: float) -> tuple[float, int]:
    """
    Compute ln(1+x) via the alternating Taylor
    
    Iteration stops when |term| < eps or MAX_ITERATIONS is reached.

    Args:
        x:   The argument; must satisfy |x| < 1.
        eps: Desired precision (stopping criterion).

    Returns:
        A tuple (approximation, iterations_used).

    Raises:
        ValueError: If |x| >= 1 (series does not converge).
    """
    if abs(x) >= 1:
        raise ValueError("The series converges only when |x| < 1.")

    total = 0.0
    term = x
    n = 1

    while n <= MAX_ITERATIONS:
        total += term
        if abs(term) < eps:
            break
        n += 1
        term = ((-1) ** (n - 1)) * (x ** n) / n

    return total, n


def print_series_result(x: float, eps: float,
                        approx: float, exact: float, iters: int) -> None:
    """
    Display a formatted comparison table for the series result.

    Args:
        x:      Input value.
        eps:    Precision used.
        approx: Series approximation of ln(1+x).
        exact:  Exact value from math.log.
        iters:  Number of iterations performed.
    """
    header = f"{'x':>10}  {'n':>6}  {'F(x)':>20}  {'math.log(1+x)':>20}  {'eps':>12}"
    separator = "-" * len(header)
    row = (f"{x:>10.6f}  {iters:>6}  "
            f"{approx:>20.10f}  {exact:>20.10f}  {eps:>12.2e}")

    print("\n  Results:")
    print("  " + header)
    print("  " + separator)
    print("  " + row)

    if iters >= MAX_ITERATIONS:
        print(f"\n  Warning: reached the maximum of {MAX_ITERATIONS} iterations.")
        print("  The required precision may not have been achieved.")


def task1() -> None:
    """
    Business function for Task 1.

    Prompts the user for x and eps, computes ln(1+x) via power series,
    and prints a comparison table with the exact math.log value.
    """
    print("  TASK 1 — Compute ln(1+x) via Taylor series")

    x = get_float("  Enter x (|x| < 1): ", min_val=-0.9999999, max_val=0.9999999)
    eps = get_float("  Enter precision eps (e.g. 1e-6): ", min_val=1e-15, max_val=1.0)

    try:
        approx, iters = compute_series(x, eps)
    except ValueError as exc:
        print(f"  Computation error: {exc}")
        return

    exact = math.log(1 + x)
    print_series_result(x, eps, approx, exact, iters)