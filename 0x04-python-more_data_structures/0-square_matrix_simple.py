#!/usr/bin/python3
def square_matri_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = ls(map(lambda x: x**2, matrix[i]))

    return (new_matrix)