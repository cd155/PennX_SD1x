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

        def clock_wise(self, number_of_turns):
            pass

        def counter_clock_wise(self, number_of_turns):
            pass

        def clock_wise_conner_adjust(self, number_of_turns):
            pass

        def counter_clock_wise_conner_adjust(self, number_of_turns):
            pass