'''
Laboratory Work 3
Topic: Standard data types, collections, functions, modules
Version: 1.0
Developer: Pratsko Maksim Dmitrievich
Date: 19-03-2026
Description: Imports all task modules and provides an interactive menu
            that lets the user choose and repeatedly run any task.
'''


from utils import get_int, run_with_repeat
from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5


_TASKS: dict[int, tuple[str, callable]] = {
    1: ("Task 1", task1),
    2: ("Task 2", task2),
    3: ("Task 3", task3),
    4: ("Task 4", task4),
    5: ("Task 5", task5),
}


def print_menu() -> None:
    """
    Print the main task-selection menu to the console.
    """
    print("MAIN MENU\n")
    for key, (title, _) in _TASKS.items():
        print(f"{key}. {title}")
    print("0. Exit")


def choose_task() -> int:
    """
    Ask the user to select a task number from the menu.

    Returns:
        The chosen task number (0 = exit).
    """
    return get_int("\nSelect task (0 to exit): ", min_val=0, max_val=len(_TASKS))


def main() -> None:
    """
    Main entry point.

    Displays the menu, dispatches the selected task (with repeat support),
    and exits cleanly when the user chooses 0.
    """
    while True:
        print_menu()
        choice = choose_task()

        if choice == 0:
            break

        _, task_func = _TASKS[choice]
        run_with_repeat(task_func)


if __name__ == "__main__":
    main()