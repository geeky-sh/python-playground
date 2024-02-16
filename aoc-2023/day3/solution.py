from typing import List
from dataclasses import dataclass

@dataclass
class Matrix:
    items: List[List[str]]

    @property
    def row_size(self) -> int:
        return len(self.items)

    @property
    def column_size(self) -> int:
        return len(self.items[0])

    def get_number(self, row: int, column: int):
        point = self.items[row][column]

        left = ""
        i = column - 1
        while i >= 0 and self.items[row][i].isdigit():
            left = self.items[row][i] + left
            i -= 1

        right = ""
        i = column + 1
        while i < self.column_size and self.items[row][i].isdigit():
            right = right + self.items[row][i]
            i += 1

        return "{}{}{}".format(left, point, right)

    def get_nearby_numbers(self, row, column):
        nearby_numbers = []
        if row > 0 and self.items[row-1][column].isdigit():
            nearby_numbers.append(self.get_number(row-1, column))
        if row < self.row_size-1 and self.items[row+1][column].isdigit():
            nearby_numbers.append(self.get_number(row+1, column))
        if column > 0 and self.items[row][column-1].isdigit():
            nearby_numbers.append(self.get_number(row, column-1))
        if column < self.column_size-1 and self.items[row][column+1].isdigit():
            nearby_numbers.append(self.get_number(row, column+1))
        if row > 0 and column > 0 and self.items[row-1][column-1].isdigit():
            nearby_numbers.append(self.get_number(row-1, column-1))
        if row < self.row_size-1 and column < self.column_size-1 and self.items[row+1][column+1].isdigit():
            nearby_numbers.append(self.get_number(row+1, column+1))

        return nearby_numbers

    @classmethod
    def build(cls, file_path: str):
        rows = []
        with open(file_path) as f:
            lines = f.readlines()
            for line in lines:
                rows.append(list(line.strip()))
        return cls(rows)
