"""
Suppose i want to get 2nd value of the tupe as a list of list

"""

from my_module import MathOperation


all_objs = MathOperation


def split_list(input_list: list[str], items_count: int) -> list[list[str]]:

    return [
        input_list[i : i + items_count] for i in range(0, len(input_list), items_count)
    ]


if __name__ == "__main__":

    names_list = [_.name for _ in MathOperation]
    print(names_list)

    new_list = split_list(names_list, 6)
    print(new_list)
