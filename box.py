from collections import deque


def count(row, symbol):
    return row.count(symbol)


def check_row(row, symbol):
    return symbol in row


def check_column(object, symbol, column):
    for line in object:
        if symbol == line[column]:
            return True
    return False


class Box:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = []
        self.count_of_number = {}
        self.queue = deque([0])*dimension

    def add(self, row):
        self.matrix.append(row)

    def draw(self):
        for row in self.matrix:
            print(f'{row}')

    def count_in_box(self):
        self.count_of_number[0] = 0
        number = 1
        while number <= self.dimension:
            counter = 0
            for row in self.matrix:
                counter += count(row, number)
            self.count_of_number[number] = counter
            number += 1

    def sort_queue(self):
        number = 1
        while number <= self.dimension:
            if self.count_of_number[number] >= self.count_of_number[number-1]:
                if self.queue[0] == 0:
                    self.queue[0] = number
                else:
                    self.queue[number-2], self.queue[number -
                                                     1] = number, self.queue[number-2]
            elif self.count_of_number[number] > self.count_of_number[self.queue[number-2]]:
                self.queue[number-2], self.queue[number -
                                                 1] = number, self.queue[number-2]
            number += 1

    def solve(self):
        column = 0
        row = 0
        queue = 0
        while queue < self.dimension:
            while row < self.dimension:
                while column < self.dimension:
                    if not check_row(self.matrix[row], self.queue[queue]) and not check_column(self.matrix, self.queue[queue], column) and self.matrix[row][column] == 0:
                        self.matrix[row][column] = self.queue[queue]
                        self.count_of_number[self.queue[queue]] += 1
                    column += 1
                column = 0
                row += 1
            row = 0
            queue += 1


box = Box(3)
box.add([0, 2, 0])
box.add([0, 3, 2])
box.add([0, 0, 0])
box.draw()
box.count_in_box()
box.sort_queue()
box.solve()
box.draw()
