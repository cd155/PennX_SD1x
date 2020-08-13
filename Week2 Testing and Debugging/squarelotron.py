class Squarelotron:
    def __init__(self, size=1):
        self.size = size
        self.number_of_rings = size/2 + size%2

        self.squarelotron = []
        for i in range(size):
            arrays = []
            for j in range (1, size + 1):
                 arrays.append(i*size + j)
            self.squarelotron.append(arrays)

    def upside_down_flip(self, ring):
        # check ring size
        if ring > self.number_of_rings or ring < 1:
            print("Ring input must with 1<=ring<=" + self.number_of_rings)
            return

        # copy a matrix to edit
        matrix = self.squarelotron.copy()

        # set bound
        top_bound = 0
        bottom_bound = self.size
        out_number_of_rings = ring -1
        if out_number_of_rings > 0:
            top_bound = out_number_of_rings
            bottom_bound = self.size - out_number_of_rings

        half_row = (top_bound + bottom_bound)/2
        for i in range(top_bound, int(half_row)):
            for j in range(top_bound, bottom_bound):
                if i == top_bound:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[self.size - 1 - i][j]
                    matrix[self.size - 1 - i][j] = temp
                else:
                    if j == top_bound or j == bottom_bound - 1:
                        temp = matrix[i][j]
                        matrix[i][j] = matrix[self.size - 1 - i][j]
                        matrix[self.size - 1 - i][j] = temp
        return matrix

    def main_diagonal_flip(self, ring):
        # check ring size
        if ring > self.number_of_rings or ring < 1:
            print("Ring input must with 1<=ring<=" + self.number_of_rings)
            return

        # copy a matrix to edit
        matrix = self.squarelotron.copy()

        # set bound
        top_bound = 0
        bottom_bound = self.size
        out_number_of_rings = ring -1
        if out_number_of_rings > 0:
            top_bound = out_number_of_rings
            bottom_bound = self.size - out_number_of_rings

        for i in range(top_bound, bottom_bound):
            if i == bottom_bound -1:
                for j in range(top_bound, bottom_bound):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
            else:
                temp = matrix[i][out_number_of_rings]
                matrix[i][out_number_of_rings] = matrix[out_number_of_rings][i]
                matrix[out_number_of_rings][i] = temp
        return matrix

    def rotate_right(self, number_of_turns):

        def clock_wise(number_of_turns):
            for _ in range(number_of_turns):
                top_bound = 0
                bottom_bound = self.size
                for i in range(int(self.size/2)):
                    # Example: 5 by 5 matrix
                    # order: row 0 > colum 4> row 4 > colum 0
                    # part1: row 0
                    # part2: colum 4
                    # part3: row 4
                    # part4: colum 0
                    for j in range(top_bound, bottom_bound - 1):
                        # replace part2 with part1
                        temp1 = self.squarelotron[j][self.size - 1 - i]
                        self.squarelotron[j][self.size - 1 - i] = self.squarelotron[i][j]
                        # replace part3 with part2
                        temp2 = self.squarelotron[self.size - 1 - i][self.size - 1 - j]
                        self.squarelotron[self.size - 1 - i][self.size - 1 - j] = temp1
                        # replace part4 with part3
                        temp1 = self.squarelotron[self.size - 1 - j][i]
                        self.squarelotron[self.size - 1 - j][i] = temp2
                        # replace part1 with part4
                        self.squarelotron[i][j] = temp1

                    # adjust top bottom bound
                    top_bound += 1
                    bottom_bound -= 1

        def counter_clock_wise(number_of_turns):
            for _ in range(abs(number_of_turns)):
                top_bound = 0
                bottom_bound = self.size
                for i in range(int(self.size/2)):
                    # Example: 5 by 5 matrix
                    # order: row 0 > colum 0> row 4 > colum 4
                    # part1: row 0
                    # part2: colum 4
                    # part3: row 4
                    # part4: colum 0
                    for j in range(top_bound, bottom_bound - 1):
                        # replace part4 with part1
                        temp1 = self.squarelotron[self.size - 1 - j][i]
                        self.squarelotron[self.size - 1 - j][i] = self.squarelotron[i][j]
                        # replace part3 with part4
                        temp2 = self.squarelotron[self.size - 1 - i][self.size - 1 - j]
                        self.squarelotron[self.size - 1 - i][self.size - 1 - j] = temp1
                        # replace part2 with part3
                        temp1 = self.squarelotron[j][self.size - 1 - i]
                        self.squarelotron[j][self.size - 1 - i] = temp2
                        # replace part1 with part2
                        self.squarelotron[i][j] = temp1

                    # adjust top bottom bound
                    top_bound += 1
                    bottom_bound -= 1

        if self.size == 1:
            return self.squarelotron

        if number_of_turns > 0:
            clock_wise(number_of_turns)
        else:
            counter_clock_wise(number_of_turns)