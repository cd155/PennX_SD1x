from random import randrange

class WhackAMole:
    def __init__(self, nums_attempts, grid_dimension):
        self.score = 0
        self.moles_left = 0
        self.attempts_left = nums_attempts
        self.grid_dimension = grid_dimension
        self.mole_grid = []
        for i in range(grid_dimension):
            row = []
            for j in range (grid_dimension):
                row.append("*")
            self.mole_grid.append(row)

    def place(self, x, y):
        if x >= self.grid_dimension or y >= self.grid_dimension:
            return False

        if self.mole_grid[x][y] == "M":
            return False
        else:
            self.moles_left += 1
            self.mole_grid[x][y] = "M"
            return True

    def whack(self, x, y):
        if x >= self.grid_dimension or y >= self.grid_dimension:
            print("x or y are out of bound")
            return

        if x == -1 and y ==-1:
            print("Give up")
            self.print_grid()
            self.attempts_left = 0
            return

        self.attempts_left -= 1
        if self.mole_grid[x][y] == "M":
            self.score += 1
            self.moles_left -= 1
            self.mole_grid[x][y] = "W"
            print("You caught a mole, " + str(self.moles_left) + " left")
            print(str(self.attempts_left) + " time(s) left")
        else:
            print("No mole in this spot.")
            print(str(self.attempts_left) + " time(s) left")

        if self.attempts_left <= 0:
            print("Attempts ran out")
            self.print_grid_to_user()
            return

        if self.moles_left <= 0:
            print("All moles were caught")
            self.attempts_left = 0
            return

    def print_grid_to_user(self):
        for row in self.mole_grid:
            for box in row:
                if box == "M":
                    print("*", end =" ")
                else:
                    print(box, end =" ")
            print()

    def print_grid(self):
        for row in self.mole_grid:
            for box in row:
                print(box, end =" "),
            print()

# Start a game
is_running = True
while is_running:
    try:
        grid_dimension = int(input("Enter the grid_dimension: "))
        nums_attempts = int(input("Enter the nums_attempts: "))
        nums_place = int(input("Enter the nums_place: "))

    except:
        print("grid_dimension is not an integer or "
        "nums_attempts is not an integer or "
        "nums_place is not an integer.")
        continue

    whack_a_mole = WhackAMole(nums_attempts, grid_dimension)
    is_placing = True
    nums_try_placing = 0
    while is_placing:
        x = randrange(grid_dimension)
        y = randrange(grid_dimension)
        if whack_a_mole.place(x, y):
            nums_try_placing += 1
        if nums_try_placing == nums_place:
            is_placing = False

    while whack_a_mole.attempts_left > 0:
        try:
            x = int(input("Enter the x: "))
            y = int(input("Enter the y: "))
        except:
            print("x is not an integer or y is not an integer.")
            continue
        
        whack_a_mole.whack(x, y)
    is_running = False