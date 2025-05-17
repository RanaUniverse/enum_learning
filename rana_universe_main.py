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
    fruits[i : i + items_per_row] for i in range(0, len(fruits), items_per_row)
]

print(fruits_rows)
