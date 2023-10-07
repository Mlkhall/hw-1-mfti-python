from random import randint
from dataclasses import dataclass, asdict
from typing import Sequence

import rich
from rich.console import Console


@dataclass(frozen=True, slots=True, kw_only=True)
class BinarySearchResponse:
    """Ответ бинарного поиска."""
    count_attempts: int
    index: int
    found_value: int | None


def binary_search(array: Sequence[int], value: int) -> BinarySearchResponse:
    """Бинарный поиск.

    Args:
        array: Отсортированный массив.
        value: Искомое значение.

    Returns:
        Количество попыток и индекс найденного значения + само значение.
    """
    left = 0
    right = len(array) - 1
    count_attempts = 0

    while left <= right:
        count_attempts += 1
        middle = (left + right) // 2

        if array[middle] == value:
            return BinarySearchResponse(
                count_attempts=count_attempts,
                index=middle,
                found_value=value,
            )

        if array[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    return BinarySearchResponse(
        count_attempts=count_attempts,
        index=-1,
        found_value=None,
    )


def main() -> None:
    """Точка входа."""

    console = Console()

    rand_size = 100
    random_value = randint(0, rand_size - 1)
    target_array = tuple(range(rand_size))

    response = binary_search(target_array, random_value)

    console.rule("[bold red] Домашнее задание №1")
    console.print(f"Массив: {target_array}", justify="center")
    console.rule()
    console.print(f"Искомое значение: {random_value}", style="bold red", justify="center")
    console.rule()

    console.print(f"Индекс искомого значения: {response.index}", justify="center")
    console.print(f"Количество попыток: {response.count_attempts}", justify="center")
    console.print(f"Найденное значение: {response.found_value}", justify="center")



if __name__ == "__main__":
    main()
