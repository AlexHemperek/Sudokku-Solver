from collections import deque


class Box:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = []
        self.count_of_number = {}
        self.queue = deque([])
        self.little_box = deque([] for _ in range(dimension))
        self.column = deque([[] for _ in range(dimension)])

    def add(self, row):
        self.matrix.append(row)
        counter = 0
        if len(self.little_box[counter]) == 4:
            check_witch_box = 2
        else:
            check_witch_box = 0
        while counter < self.dimension:
            self.column[counter].append(row[counter])
            self.little_box[check_witch_box].append(row[counter])
            if counter == 1:
                check_witch_box += 1
            counter += 1

    def draw(self):
        for row in self.matrix:
            print(f'{row}')
        print('\n')

    def count_in_box(self):
        number = 0
        while number <= self.dimension:
            counter = 0
            for row in self.matrix:
                counter += row.count(number)
            self.count_of_number[number] = counter
            number += 1

    def create_queue(self):
        self.queue.clear()
        number = 1
        comparison_counter = 1
        while number <= self.dimension:
            while comparison_counter <= number:
                if number == 1:
                    self.queue.append(number)
                    break
                elif comparison_counter == number:
                    self.queue.append(number)
                elif self.count_of_number[number] > self.count_of_number[number-comparison_counter]:
                    self.queue.insert(self.queue.index(
                        number-comparison_counter), number)
                    break
                comparison_counter += 1
            comparison_counter = 1
            number += 1

    def update_little_box(self, number, witch_row, witch_column):
        witch_little_box = 0
        place_in_little_box = 0
        if witch_row < 2 and witch_column < 2:
            witch_little_box = 0
        elif witch_row < 2 and witch_column >= 2:
            witch_little_box = 1
        elif witch_row >= 2 and witch_column < 2:
            witch_little_box = 2
        elif witch_row >= 2 and witch_column >= 2:
            witch_little_box = 3
        if witch_row % 2 != 0 and witch_column < 2:
            place_in_little_box = witch_column + 2
        elif witch_row % 2 == 0 and witch_column >= 2:
            place_in_little_box = witch_column - 2
        else:
            place_in_little_box = witch_column
        self.little_box[witch_little_box][place_in_little_box] = number

    def solve_row(self, row, witch_row):
        number = 1
        while number <= self.dimension:
            if number not in row:
                self.column[row.index(0)][witch_row] = number
                self.update_little_box(number, witch_row, row.index(0))
                row[row.index(0)] = number
                break
            number += 1
        return row

    def solve_column(self, row, witch_column):
        number = 1
        while number <= self.dimension:
            if number not in self.column[witch_column]:
                row[witch_column] = number
                self.update_little_box(
                    number, self.column[witch_column].index(0), witch_column)
                self.column[witch_column][self.column[witch_column].index(
                    0)] = number
                break
            number += 1
        return row

    def solve_little_box(self, row, witch_row, witch_box):
        number = 1
        while number <= self.dimension:
            if number not in self.little_box[witch_box]:
                if witch_row % 2 == 0 and witch_box % 2 != 0:
                    row[self.little_box[witch_box].index(0) + 2] = number
                    self.column[self.little_box[witch_box].index(
                        0) + 2][witch_row] = number
                elif witch_row % 2 != 0 and witch_box % 2 == 0:
                    row[self.little_box[witch_box].index(0) - 2] = number
                    self.column[self.little_box[witch_box].index(
                        0) - 2][witch_row] = number
                else:
                    row[self.little_box[witch_box].index(0)] = number
                    self.column[self.little_box[witch_box].index(
                        0)][witch_row] = number
                self.little_box[witch_box][self.little_box[witch_box].index(
                    0)] = number
            number += 1
        return row

    def solve(self):
        self.count_in_box()
        while self.count_of_number[0] > 0:
            column_counter = 0
            row_counter = 0
            row_with_zero = 0
            little_box_counter = 0
            little_box_row_with_zero = 0
            queue_counter = 0
            possibilities_list = []
            while row_counter < self.dimension:
                if self.matrix[row_counter].count(0) == 1:
                    self.matrix[row_counter] = self.solve_row(
                        self.matrix[row_counter], row_counter)
                row_counter += 1
            while column_counter < self.dimension:
                if self.column[column_counter].count(0) == 1:
                    row_with_zero = self.column[column_counter].index(0)
                    self.matrix[row_with_zero] = self.solve_column(
                        self.matrix[self.column[column_counter].index(0)], column_counter)
                column_counter += 1
            while little_box_counter < self.dimension:
                if self.little_box[little_box_counter].count(0) == 1:
                    if little_box_counter < 2 and self.little_box[little_box_counter].index(0) < 2:
                        little_box_row_with_zero = 0
                    elif little_box_counter < 2 and self.little_box[little_box_counter].index(0) >= 2:
                        little_box_row_with_zero = 1
                    elif little_box_counter >= 2 and self.little_box[little_box_counter].index(0) < 2:
                        little_box_row_with_zero = 2
                    elif little_box_counter >= 2 and self.little_box[little_box_counter].index(0) >= 2:
                        little_box_row_with_zero = 3
                    self.matrix[little_box_row_with_zero] = self.solve_little_box(
                        self.matrix[little_box_row_with_zero], little_box_row_with_zero, little_box_counter)
                little_box_counter += 1
            self.count_in_box()
            self.create_queue()
            column_counter = 0
            row_counter = 0
            little_box_counter = 0
            while row_counter < self.dimension:
                while column_counter < self.dimension:
                    if row_counter < 2 and column_counter < 2:
                        little_box_counter = 0
                    elif row_counter < 2 and column_counter >= 2:
                        little_box_counter = 1
                    elif row_counter >= 2 and column_counter < 2:
                        little_box_counter = 2
                    elif row_counter >= 2 and column_counter >= 2:
                        little_box_counter = 3
                    possibilities_list.clear()
                    while queue_counter < self.dimension:
                        if self.matrix[row_counter][column_counter] == 0:
                            if not self.queue[queue_counter] in self.matrix[row_counter] and not self.queue[queue_counter] in self.column[column_counter] and not self.queue[queue_counter] in self.little_box[little_box_counter]:
                                possibilities_list.append(
                                    self.queue[queue_counter])
                        else:
                            break
                        queue_counter += 1
                    if len(possibilities_list) == 1:
                        self.matrix[row_counter][column_counter] = possibilities_list[0]
                        self.column[column_counter][row_counter] = possibilities_list[0]
                        self.update_little_box(
                            possibilities_list[0], row_counter, column_counter)
                    queue_counter = 0
                    column_counter += 1
                column_counter = 0
                row_counter += 1
            self.count_in_box()


box = Box(4)
box.add([3, 4, 1, 0])
box.add([0, 2, 0, 0])
box.add([0, 0, 2, 0])
box.add([0, 1, 4, 3])
box.draw()
box.solve()
box.draw()
