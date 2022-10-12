from PIL import Image
import numpy


class Game:

    def __init__(self, rows, columns, file_path):
        self.rows = rows
        self.columns = columns
        self.file_path = file_path
        self.board_to_play = self.convert_image_from_file()
        self.hints_array = self.create_hints()
        self.isDone = False

    def create_hints(self):
        rows = len(self.board_to_play)
        columns = len(self.board_to_play[0])
        hints = numpy.empty([rows, columns, 2], dtype=int)

        for i in range(len(hints)):
            for j in range(len(hints[0])):
                hints[i][j][0] = self.count_value(i, j)
                if self.board_to_play[i][j] == 1:
                    hints[i][j][1] = -1
                else:
                    hints[i][j][1] = 0

        for i in range(len(hints)):
            for j in range(len(hints[0])):
                if hints[i][j][0] == 9:
                    for k in range(-1, 2):
                        for m in range(-1, 2):
                            if k == 0 and m == 0:
                                continue
                            else:
                                hints[i + k][j + m][0] = -2

        return hints

    def count_value(self, i, j):
        hints_sum = 0
        for k in range(max(0, i - 1), i + 2 if i + 2 <= len(self.board_to_play) else len(self.board_to_play)):
            if j - 1 >= 0:
                for m in range(j - 1 if j - 1 >= 0 else j,
                               j + 2 if j + 2 <= len(self.board_to_play[0]) else len(self.board_to_play[0])):
                    hints_sum += self.board_to_play[k][m]
            else:
                for m in range(j, j + 2 if j + 2 <= len(self.board_to_play[0]) else len(self.board_to_play[0])):
                    hints_sum += self.board_to_play[k][m]

        return hints_sum

    def check_answer(self, row, column):
        if self.board_to_play[row][column] == 1:
            self.hints_array[row][column][1] = 1
            if not self.hints_array.__contains__(-1):
                self.isDone = True
            return True
        return False

    def convert_image_from_file(self):
        img = Image.open(self.file_path, 'r')

        # parametr 'L' konwertuje obraz do skali szarości
        img = img.resize((self.columns, self.rows)) \
            .convert('L') \
            .point(lambda color: 0 if color > 150 else 1)

        image_data = list(img.getdata())
        converted_image = numpy.empty([self.rows, self.columns])
        for i in range(self.rows):
            for j in range(self.columns):
                converted_image[i][j] = int(image_data[i * self.columns + j])

        return converted_image
