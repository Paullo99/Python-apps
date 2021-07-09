from PIL import Image
from os import system
import numpy
import random
from colorama import Back, Style, Fore


def create_hints(input_array):
    rows = len(input_array)
    columns = len(input_array[0])
    hints = numpy.empty([rows, columns, 2])

    for i in range(len(hints)):
        for j in range(len(hints[0])):
            hints[i][j][0] = count_value(i, j, input_array)
            if input_array[i][j] == 1:
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


def count_value(i, j, input_array):
    hints_sum = 0
    for k in range(max(0, i - 1), i + 2 if i + 2 <= len(input_array) else len(input_array)):
        if j - 1 >= 0:
            for m in range(j - 1 if j - 1 >= 0 else j, j + 2 if j + 2 <= len(input_array[0]) else len(input_array[0])):
                hints_sum += input_array[k][m]
        else:
            for m in range(j, j + 2 if j + 2 <= len(input_array[0]) else len(input_array[0])):
                hints_sum += input_array[k][m]

    return hints_sum


def main():
    try:
        system('clear')
        images = ['./images/heart.jpg', './images/house.jpg']
        filename = random.choice(images)  # input("Wprowadz bezwgledna sciezke do obrazka: ")
        rows = input("Wprowadz liczbe wierszy do gry: ")
        columns = input("Wprowadz liczbe kolumn do gry: ")
        board_to_play = convert_image_from_file(filename, int(rows), int(columns))
        hints_array = create_hints(board_to_play)
        # display_solution(board_to_play)
        while -1 in hints_array:
            system('clear')
            display_actual_solution(board_to_play, hints_array)
            try:
                [row, column] = input("Podaj wiersz i kolumne (spacja przerwy): ").split(' ')
                if row == '' or column == '' or int(row) >= len(hints_array) or int(column) >= len(hints_array[0]):
                    continue
                check_answer(int(row), int(column), board_to_play, hints_array)
            except ValueError:
                pass

        system('clear')
        print('BRAWO! Oto Twoj rozwiazany obrazek:')
        display_solution(board_to_play)
    except KeyboardInterrupt:
        print("Zakonczono gre")


def display_hints(hints_array):
    for i in range(len(hints_array)):
        for j in range(len(hints_array[0])):
            if hints_array[i][j][0] == -1:
                print('   ', end="")
            else:
                print(int(hints_array[i][j][0]), ' ', end="")
        print("")


def check_answer(row, column, board_to_play, hints_array):
    if board_to_play[row][column] == 1:
        hints_array[row][column][1] = 1
    else:
        print("Niepoprawna odpowiedz! Sprobuj ponownie.")
        input()


def convert_image_from_file(file_path, rows=20, columns=20):
    img = Image.open(file_path, 'r')

    # parametr 'L' konwertuje obraz do skali szarości
    img = img.resize((columns, rows)) \
        .convert('L') \
        .point(lambda color: 0 if color > 150 else 1)

    image_data = list(img.getdata())
    converted_image = numpy.empty([rows, columns])
    for i in range(rows):
        for j in range(columns):
            converted_image[i][j] = int(image_data[i * columns + j])

    return converted_image


def display_actual_solution(board_to_play, hints_array):
    print('   ', end="")
    for i in range(len(board_to_play[0])):
        if i <= 9:
            print('', int(i), '', end="")
        else:
            print('', int(i), end="")
    print('\n   ', end="")
    for x in range(len(board_to_play[0])):
        print('---', end="")
    print("   ")

    for i in range(len(board_to_play)):
        # wyświetlanie bocznych indeksów
        if i <= 9:
            print(i, '|', end="")
        else:
            print(str(i) + '|', end="")

        for j in range(len(board_to_play[0])):
            if hints_array[i][j][1] == 1 and hints_array[i][j][0] != -2:
                text = ' ' + str(int(hints_array[i][j][0])) + ' '
                print((Back.LIGHTBLACK_EX + text + Style.RESET_ALL), end="")
            elif hints_array[i][j][0] != -2:
                print('', int(hints_array[i][j][0]), '', end="")
            elif hints_array[i][j][1] == 1 and hints_array[i][j][0] == -2:
                print((Back.LIGHTBLACK_EX + '   ' + Style.RESET_ALL), end="")
            else:
                print('   ', end="")
        print("")
    pass


def display_solution(input_array):
    black_pixel = (Back.LIGHTBLACK_EX + '   ' + Style.RESET_ALL)
    white_pixel = (Back.LIGHTWHITE_EX + Fore.BLACK + '   ' + Style.RESET_ALL)

    for i in range(len(input_array)):
        for j in range(len(input_array[0])):
            if input_array[i][j] == 1:
                print(black_pixel, end='')
            elif input_array[i][j] == 0:
                print(white_pixel, end='')
            else:
                print('  ', end='')
        print('')


if __name__ == '__main__':
    main()
