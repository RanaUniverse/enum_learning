fruits = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Elderberry",
    "Fig",
    "Grape",
    "Honeydew",
    "Kiwi",
    "Lemon",
]

items_per_row = 3

fruits_rows = [
    fruits[i : i + items_per_row]
    for i in range(
        0,
        len(fruits),
        items_per_row,
    )
]


def split_list(input_list: list[str], items_count: int) -> list[list[str]]:

    return [
        input_list[i : i + items_count] for i in range(0, len(input_list), items_count)
    ]


if __name__ == "__main__":
    fruit_rows = split_list(fruits, 3)
    print(fruit_rows)
