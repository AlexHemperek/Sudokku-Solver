class Box:
    def __init__(self):
        self.dimension = 9
        self.box = []
        self.column = [[] for _ in range(self.dimension)]
        self.little_box = [[] for _ in range(self.dimension)]
        self.possibilities_in_box = [
            [[] for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.possibilities_in_column = [
            [[] for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.possibilities_in_little_box = [
            [[] for _ in range(self.dimension)] for _ in range(self.dimension)]

    def add(self, row):
        self.box.append(row)
        counter = 0
        witch_little_box = 0
        if len(self.little_box[witch_little_box + 3]) == 9:
            witch_little_box = 6
        elif len(self.little_box[witch_little_box]) == 9:
            witch_little_box = 3
        while counter < self.dimension:
            self.column[counter].append(row[counter])
            self.little_box[witch_little_box].append(row[counter])
            counter += 1
            if counter % 3 == 0:
                witch_little_box += 1

    def draw(self):
        for row in self.box:
            print(f'{row}')
        print('\n')

    def count_zero(self):
        zero_counter = 0
        row_counter = 0
        column_counter = 0
        while row_counter < self.dimension:
            while column_counter < self.dimension:
                if self.box[row_counter][column_counter] == 0:
                    zero_counter += 1
                column_counter += 1
            column_counter = 0
            row_counter += 1
        return zero_counter

    def update_matrix(self):
        row_counter = 0
        column_counter = 0
        witch_little_box = 0
        step_counter = 0
        while witch_little_box < self.dimension:
            self.box[row_counter][column_counter] = self.little_box[witch_little_box][step_counter % 9]
            column_counter += 1
            step_counter += 1
            if step_counter % 9 == 0:
                witch_little_box += 1
                if step_counter % 27 == 0:
                    row_counter += 1
                    column_counter = 0
                else:
                    row_counter -= 2
            elif step_counter % 3 == 0:
                column_counter -= 3
                row_counter += 1

    def update_column(self):
        row_counter = 0
        column_counter = 0
        clear_counter = 0
        while clear_counter < self.dimension:
            self.column[clear_counter].clear()
            clear_counter += 1
        while row_counter < self.dimension:
            while column_counter < self.dimension:
                self.column[column_counter].append(
                    self.box[row_counter][column_counter])
                column_counter += 1
            column_counter = 0
            row_counter += 1

    def update_little_box(self):
        row_counter = 0
        column_counter = 0
        step_counter = 0
        witch_little_box = 0
        clear_counter = 0
        while clear_counter < self.dimension:
            self.little_box[clear_counter].clear()
            clear_counter += 1
        while witch_little_box < self.dimension:
            self.little_box[witch_little_box].append(
                self.box[row_counter][column_counter])
            column_counter += 1
            step_counter += 1
            if step_counter % 9 == 0:
                row_counter += 1
                column_counter = 0
                if step_counter % 27 == 0:
                    witch_little_box += 1
                else:
                    witch_little_box -= 2
            elif step_counter % 3 == 0:
                witch_little_box += 1

    def update_possibilities(self):
        row_counter = 0
        column_counter = 0
        number = 1
        step_counter = 0
        witch_little_box = 0
        first_clear_counter = 0
        second_clear_counter = 0
        while first_clear_counter < self.dimension:
            while second_clear_counter < self.dimension:
                self.possibilities_in_box[first_clear_counter][second_clear_counter].clear(
                )
                self.possibilities_in_column[first_clear_counter][second_clear_counter].clear(
                )
                self.possibilities_in_little_box[first_clear_counter][second_clear_counter].clear(
                )
                second_clear_counter += 1
            second_clear_counter = 0
            first_clear_counter += 1
        while witch_little_box < self.dimension:
            while number <= self.dimension:
                if self.box[row_counter][column_counter] == 0:
                    if not number in self.box[row_counter] and not number in self.column[column_counter] and not number in self.little_box[witch_little_box]:
                        self.possibilities_in_box[row_counter][column_counter].append(
                            number)
                        self.possibilities_in_column[column_counter][row_counter].append(
                            number)
                        self.possibilities_in_little_box[witch_little_box][step_counter % 9].append(
                            number)

                else:
                    self.possibilities_in_box[row_counter][column_counter].append(
                        0)
                    self.possibilities_in_column[column_counter][row_counter].append(
                        0)
                    self.possibilities_in_little_box[witch_little_box][step_counter % 9].append(
                        0)
                    break
                number += 1
            number = 1
            column_counter += 1
            step_counter += 1
            if step_counter % 9 == 0:
                witch_little_box += 1
                if step_counter % 27 == 0:
                    row_counter += 1
                    column_counter = 0
                else:
                    row_counter -= 2
            elif step_counter % 3 == 0:
                column_counter -= 3
                row_counter += 1
        self.update_double_in_row_possibilities()
        self.update_double_in_column_possibilities()
        self.update_double_in_little_box_possibilities()

    def update_double_in_row_possibilities(self):
        row_counter = 0
        colum_counter = 0
        start_counter = 0
        end_counter = 0
        clear_counter = 0
        place_in_row = 0
        counter = 0
        number = 1
        possible_place_for_number = [[] for _ in range(self.dimension)]
        possible_double = []
        while row_counter < self.dimension:
            while number <= self.dimension:
                while colum_counter < self.dimension:
                    if 0 not in self.possibilities_in_box[row_counter][colum_counter] and number in self.possibilities_in_box[row_counter][colum_counter]:
                        possible_place_for_number[number -
                                                  1].append(colum_counter)
                    colum_counter += 1
                if len(possible_place_for_number[number - 1]) == 2:
                    possible_double.append(number)
                colum_counter = 0
                number += 1
            if len(possible_double) > 1:
                start_counter = 0
                end_counter = len(possible_double) - 1
                while start_counter < end_counter:
                    while start_counter < end_counter:
                        if possible_place_for_number[possible_double[start_counter] - 1] == possible_place_for_number[possible_double[end_counter] - 1]:
                            while counter < 2:
                                place_in_row = possible_place_for_number[
                                    possible_double[start_counter] - 1][counter]
                                self.possibilities_in_box[row_counter][place_in_row].clear(
                                )
                                self.possibilities_in_box[row_counter][place_in_row].append(
                                    possible_double[start_counter])
                                self.possibilities_in_box[row_counter][place_in_row].append(
                                    possible_double[end_counter])
                                counter += 1
                        end_counter -= 1
                    end_counter = len(possible_double) - 1
                    start_counter += 1
            clear_counter = 0
            while clear_counter < self.dimension:
                possible_place_for_number[clear_counter].clear()
                clear_counter += 1
            possible_double.clear()
            number = 1
            row_counter += 1

    def update_double_in_column_possibilities(self):
        column_counter = 0
        step_counter = 0
        start_counter = 0
        end_counter = 0
        clear_counter = 0
        place_in_column = 0
        counter = 0
        number = 1
        possible_place_for_number = [[] for _ in range(self.dimension)]
        possible_double = []
        while column_counter < self.dimension:
            while number <= self.dimension:
                while step_counter < self.dimension:
                    if 0 not in self.possibilities_in_column[column_counter][step_counter] and number in self.possibilities_in_column[column_counter][step_counter]:
                        possible_place_for_number[number -
                                                  1].append(step_counter)
                    step_counter += 1
                if len(possible_place_for_number[number - 1]) == 2:
                    possible_double.append(number)
                step_counter = 0
                number += 1
            if len(possible_double) > 1:
                start_counter = 0
                end_counter = len(possible_double) - 1
                while start_counter < end_counter:
                    while start_counter < end_counter:
                        if possible_place_for_number[possible_double[start_counter] - 1] == possible_place_for_number[possible_double[end_counter] - 1]:
                            while counter < 2:
                                place_in_column = possible_place_for_number[
                                    possible_double[start_counter] - 1][counter]
                                self.possibilities_in_column[column_counter][place_in_column].clear(
                                )
                                self.possibilities_in_column[column_counter][place_in_column].append(
                                    possible_double[start_counter])
                                self.possibilities_in_column[column_counter][place_in_column].append(
                                    possible_double[end_counter])
                                counter += 1
                        end_counter -= 1
                    end_counter = len(possible_double) - 1
                    start_counter += 1
            clear_counter = 0
            while clear_counter < self.dimension:
                possible_place_for_number[clear_counter].clear()
                clear_counter += 1
            possible_double.clear()
            number = 1
            column_counter += 1

    def update_double_in_little_box_possibilities(self):
        step_counter = 0
        start_counter = 0
        end_counter = 0
        clear_counter = 0
        place_in_little_box = 0
        counter = 0
        number = 1
        possible_place_for_number = [[] for _ in range(self.dimension)]
        possible_double = []
        witch_little_box = 0
        while witch_little_box < self.dimension:
            while number <= self.dimension:
                while step_counter < self.dimension:
                    if 0 not in self.possibilities_in_little_box[witch_little_box][step_counter] and number in self.possibilities_in_little_box[witch_little_box][step_counter]:
                        possible_place_for_number[number -
                                                  1].append(step_counter)
                    step_counter += 1
                if len(possible_place_for_number[number - 1]) == 2:
                    possible_double.append(number)
                step_counter = 0
                number += 1
            if len(possible_double) > 1:
                start_counter = 0
                end_counter = len(possible_double) - 1
                while start_counter < end_counter:
                    while start_counter < end_counter:
                        if possible_place_for_number[possible_double[start_counter] - 1] == possible_place_for_number[possible_double[end_counter] - 1]:
                            while counter < 2:
                                place_in_little_box = possible_place_for_number[
                                    possible_double[start_counter] - 1][counter]
                                self.possibilities_in_little_box[witch_little_box][place_in_little_box].clear(
                                )
                                self.possibilities_in_little_box[witch_little_box][place_in_little_box].append(
                                    possible_double[start_counter])
                                self.possibilities_in_little_box[witch_little_box][place_in_little_box].append(
                                    possible_double[end_counter])
                                counter += 1
                        end_counter -= 1
                    end_counter = len(possible_double) - 1
                    start_counter += 1
            clear_counter = 0
            while clear_counter < self.dimension:
                possible_place_for_number[clear_counter].clear()
                clear_counter += 1
            possible_double.clear()
            number = 1
            witch_little_box += 1

    def solve_row_with_one_zero(self):
        row_counter = 0
        number = 1
        while row_counter < self.dimension:
            if self.box[row_counter].count(0) == 1:
                while number <= self.dimension:
                    if number not in self.box[row_counter]:
                        self.box[row_counter][self.box[row_counter].index(
                            0)] = number
                        self.update_little_box()
                        self.update_column()
                        break
                    number += 1
            number = 1
            row_counter += 1

    def solve_column_with_one_zero(self):
        column_counter = 0
        number = 1
        while column_counter < self.dimension:
            if self.column[column_counter].count(0) == 1:
                while number <= self.dimension:
                    if number not in self.column[column_counter]:
                        self.box[self.column[column_counter].index(
                            0)][column_counter] = number
                        self.update_little_box()
                        self.update_column()
                        break
                    number += 1
            number = 1
            column_counter += 1

    def solve_little_box_with_one_zero(self):
        witch_little_box = 0
        number = 1
        while witch_little_box < self.dimension:
            if self.little_box[witch_little_box].count(0) == 1:
                while number <= self.dimension:
                    if number not in self.little_box[witch_little_box]:
                        self.little_box[witch_little_box][self.little_box[witch_little_box].index(
                            0)] = number
                        self.update_matrix()
                        self.update_column()
                        break
                    number += 1
            number = 1
            witch_little_box += 1

    def solve_row(self):
        self.update_possibilities()
        row_counter = 0
        column_counter = 0
        number = 1
        possible_place_for_number = []
        while row_counter < self.dimension:
            while number <= self.dimension:
                while column_counter < self.dimension:
                    if self.possibilities_in_box[row_counter][column_counter].count(number) == 1:
                        possible_place_for_number.append(column_counter)
                    column_counter += 1
                if len(possible_place_for_number) == 1:
                    self.box[row_counter][possible_place_for_number[0]] = number
                    self.update_column()
                    self.update_little_box()
                possible_place_for_number.clear()
                column_counter = 0
                number += 1
            number = 1
            row_counter += 1

    def solve_column(self):
        self.update_possibilities()
        row_counter = 0
        column_counter = 0
        number = 1
        possible_place_for_number = []
        while column_counter < self.dimension:
            while number <= self.dimension:
                while row_counter < self.dimension:
                    if self.possibilities_in_column[column_counter][row_counter].count(number) == 1:
                        possible_place_for_number.append(row_counter)
                    row_counter += 1
                if len(possible_place_for_number) == 1:
                    self.box[possible_place_for_number[0]
                             ][column_counter] = number
                    self.update_column()
                    self.update_little_box()
                possible_place_for_number.clear()
                row_counter = 0
                number += 1
            number = 1
            column_counter += 1

    def solve_little_box(self):
        self.update_possibilities()
        counter = 0
        witch_llittle_box = 0
        number = 1
        possible_place_for_number = []
        while witch_llittle_box < self.dimension:
            while number <= self.dimension:
                while counter < self.dimension:
                    if self.possibilities_in_little_box[witch_llittle_box][counter].count(number) == 1:
                        possible_place_for_number.append(counter)
                    counter += 1
                if len(possible_place_for_number) == 1:
                    self.little_box[witch_llittle_box][possible_place_for_number[0]] = number
                    self.update_matrix()
                    self.update_column()
                possible_place_for_number.clear()
                counter = 0
                number += 1
            number = 1
            witch_llittle_box += 1

    def solve_point(self):
        self.update_possibilities()
        row_counter = 0
        column_counter = 0
        while row_counter < self.dimension:
            while column_counter < self.dimension:
                if self.possibilities_in_box[row_counter][column_counter].count(0) == 0 and len(self.possibilities_in_box[row_counter][column_counter]) == 1:
                    self.box[row_counter][column_counter] = self.possibilities_in_box[row_counter][column_counter][0]
                    self.update_column()
                    self.update_little_box()
                column_counter += 1
            column_counter = 0
            row_counter += 1

    def solve(self):
        while self.count_zero() > 0:
            self.draw()
            self.solve_row_with_one_zero()
            self.solve_column_with_one_zero()
            self.solve_little_box_with_one_zero()
            self.solve_row()
            self.solve_column()
            self.solve_little_box()
            self.solve_point()


box = Box()
box.add([0, 0, 0, 0, 0, 0, 7, 9, 6])
box.add([0, 5, 0, 0, 2, 0, 0, 0, 0])
box.add([0, 0, 0, 9, 0, 4, 0, 0, 0])
box.add([0, 2, 0, 0, 0, 3, 0, 1, 0])
box.add([9, 8, 0, 0, 0, 0, 0, 6, 5])
box.add([0, 3, 0, 4, 0, 0, 0, 7, 0])
box.add([0, 0, 0, 5, 0, 8, 0, 0, 0])
box.add([0, 0, 0, 0, 9, 0, 0, 3, 0])
box.add([1, 6, 7, 0, 0, 0, 0, 0, 0])
box.solve()
box.draw()
