from numpy import dot, transpose, flip, fliplr, flipud, linalg


class Matrix:
    def __init__(self, dimensions, values):
        self.rows = int(dimensions.split()[0])
        self.cols = int(dimensions.split()[1])
        self.values = values

    def print(self):
        for x in self.values:
            print(*x, sep=' ')
        print()

    def flip(self):
        self.values = flip(self.values)
        return self

    def fliplr(self):
        self.values = fliplr(self.values)
        return self

    def flipud(self):
        self.values = flipud(self.values)
        return self

    def transpose(self):
        self.values = transpose(self.values)
        return self

    def dot_product(self, other):
        self.values = dot(self.values, other.values)
        return self

    def multiply_by(self, const):
        self.values = [[self.values[i][j] * const for j in range(self.cols)] for i in range(self.rows)]
        return self

    def add_matrix(self, other):
        self.values = [[self.values[i][j] + other.values[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return self

    def determinant(self):
        return linalg.det(self.values)

    def inverse(self):
        self.values = linalg.inv(self.values)
        return self


while True:
    print("1. Add matrices\n"
          "2. Multiply matrix by a constant\n"
          "3. Multiply matrices\n"
          "4. Transpose matrix\n"
          "5. Calculate a determinant\n"
          "6. Inverse matrix\n"
          "0. Exit")
    num = int(input("Your choice: "))
    if num == 0:
        exit()
    elif num == 1:
        d1 = input("Enter size of first matrix: ")
        print("Enter first matrix:")
        v1 = [list(map(float, input().split())) for i in range(int(d1.split()[0]))]
        d2 = input("Enter size of second matrix: ")
        print("Enter second matrix:")
        v2 = [list(map(float, input().split())) for i in range(int(d2.split()[0]))]
        print("The result is:")
        Matrix(d1, v1).add_matrix(Matrix(d2, v2)).print()
    elif num == 2:
        d = input("Enter size of matrix: ")
        print("Enter matrix:")
        v = [list(map(float, input().split())) for i in range(int(d.split()[0]))]
        c = int(input("Enter constant: "))
        print("The result is:")
        Matrix(d, v).multiply_by(c).print()
    elif num == 3:
        d1 = input("Enter size of first matrix: ")
        print("Enter first matrix:")
        v1 = [list(map(float, input().split())) for i in range(int(d1.split()[0]))]
        d2 = input("Enter size of second matrix: ")
        print("Enter second matrix:")
        v2 = [list(map(float, input().split())) for i in range(int(d2.split()[0]))]
        print("The result is:")
        Matrix(d1, v1).dot_product(Matrix(d2, v2)).print()
    elif num == 4:
        print("1. Main diagonal\n"
              "2. Side diagonal\n"
              "3. Vertical line\n"
              "4. Horizontal line")
        num2 = int(input("Your choice: "))
        dimensions = input("Enter matrix size: ")
        print("Enter matrix:")
        values = [list(map(float, input().split())) for i in range(int(dimensions.split()[0]))]
        print("The result is:")
        if num2 == 1:
            Matrix(dimensions, values).transpose().print()
        elif num2 == 2:
            Matrix(dimensions, values).flip().transpose().print()
        elif num2 == 3:
            Matrix(dimensions, values).fliplr().print()
        elif num2 == 4:
            Matrix(dimensions, values).flipud().print()
    elif num == 5:
        d = input("Enter matrix size: ")
        print("Enter matrix:")
        v = [list(map(float, input().split())) for i in range(int(d.split()[0]))]
        print("The result is:")
        print(Matrix(d, v).determinant())
    elif num == 6:
        d = input("Enter matrix size: ")
        print("Enter matrix:")
        v = [list(map(float, input().split())) for i in range(int(d.split()[0]))]
        print("The result is:")
        if Matrix(d, v).determinant() == 0:
            print("This matrix doesn't have an inverse.")
        else:
            Matrix(d, v).inverse().print()
