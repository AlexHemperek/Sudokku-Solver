from collections import deque


def count(line, symbol):
    return line.count(symbol)


def check_line(line, symbol):
    return symbol in line


def check_row(object, symbol, row):
    for line in object:
        if symbol == line[row]:
            return True
    return False


class Box:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = []
        self.count_of_number = {}
        self.queue = deque([0])*dimension

    def add(self, line):
        self.matrix.append(line)

    def draw(self):
        for line in self.matrix:
            print(f'{line}')

    def count_in_box(self):
        self.count_of_number[0] = 0
        number = 1
        while number <= self.dimension:
            counter = 0
            for line in self.matrix:
                counter += count(line, number)
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
        row = 0
        line = 0
        queue = 0
        while queue < self.dimension:
            while line < self.dimension:
                while row < self.dimension:
                    if not check_line(self.matrix[line], self.queue[queue]) and not check_row(self.matrix, self.queue[queue], row) and self.matrix[line][row] == 0:
                        self.matrix[line][row] = self.queue[queue]
                        self.count_of_number[self.queue[queue]] += 1
                    row += 1
                row = 0
                line += 1
            line = 0
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
# box = [[0, 2, 0], [0, 3, 2], [0, 0, 0]]
# print(check_row(box, 2, 2))
