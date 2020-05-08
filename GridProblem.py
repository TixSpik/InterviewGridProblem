# ``Starting at the top left corner of an N x M grid and facing towards the right, you keep walking one square at a time in the direction you are facing. If you reach the boundary of the grid or if the next square you are about to visit has already been visited, you turn right. You stop when all the squares in the grid have been visited. What direction will you be facing when you stop? For example: Consider the case with N = 3, M = 3. The path followed will be(0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2) -> (2, 1) -> (2, 0) -> (1, 0) -> (1, 1). At this point, all squares have been visited, and you are facing right.
# Input specification The first line contains T the number of test cases. Each of the next T lines contain two integers N and M, denoting the number of rows and columns respectively.
# Output specification Output T lines, one for each test case, containing the required direction you will be facing at the end. Output L for left, R for right, U for up, and D for down. 1 <= T <= 5000, 1 <= N, M <= 10 ^ 9``


class Grid:
    def __init__(self, inputCases):
        self.input = inputCases
        self.rows = 0
        self.columns = 0

    def iterateGridPosition(self):
        try:
            for position in range(0, self.input):
                self.rows = int(input('row: '))
                self.columns = int(input('columns: '))

                if self.rows == self.columns and self.rows > 1:
                    if (self.rows % 2 == 0):
                        print('L')
                    else:
                        print('R')
                elif (self.rows > self.columns and self.columns > 1):
                    if (self.columns % 2 == 0):
                        print('U')
                    else:
                        print('D')
                elif (self.columns > self.rows):
                    if (self.rows % 2 == 0):
                        print('L')
                    else:
                        print('R')
                elif(self.columns == 1):
                    if (self.rows == 1):
                        print('R')
                    else:
                        print('D')
        except:
            print('error')


print('Type Cases: ')
cases = int(input())

obj = Grid(cases)
obj.iterateGridPosition()
