import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    #file_path = os.path.join(cwd_path, file_name)

    with open(file_name, "r") as file:
        subor = csv.reader(file, delimiter="\t")

        for line in subor:
            row = [int(number) for number in line]

    return row


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    with open(file_name, "r") as file:
        subor = csv.reader(file)


        for idx, line in enumerate(subor):
            if idx == row_number:
                row = [int(number) for number in line]

    return row

def selection_sort(number_array, direction="ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """

    for i in range(len(number_array)): #najlepsia aj najhorisa zlozitost su m^2
        min = i
        for j in range(i+1, len(number_array)):
            if direction == "ascending":
                if number_array[min] > number_array[j]:
                    min = j
            elif direction == "descending":
                if number_array[min] < number_array[j]:
                    min = j
        number_array[i], number_array[min] = number_array[min], number_array[i]

    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    # najlepsie aj najhorsia zlozitost je n^2
    change = False
    for i in range(len(number_array) - 1):
        for j in range(len(number_array) - i - 1):
            if number_array[j] > number_array[j+1]:
                number_array[j], number_array[j+1] = number_array[j+1], number_array[j]
                change = True
        if not change:
            break

    return number_array


def main():

    hodnoty = read_row("numbers_one.csv")
    print("Hodnoty z read_row:", hodnoty)

    # Ukol: Selection Sort
    selection = selection_sort(hodnoty)
    print("Hodnoty z selection:", selection)


    # Ukol: Selection Sort - se smerem razeni
    selection = selection_sort(hodnoty, "descending")
    print("Hodnoty z selection + smer:", selection)

    dalsie_hodnoty = read_rows("numbers_two.csv", 2)
    print("Hodnoty z read_rows:", dalsie_hodnoty)

    # Ukol: Bubble Sort
    bubble = bubble_sort(dalsie_hodnoty)
    print("Hodnoty z bubble:", bubble)



    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

