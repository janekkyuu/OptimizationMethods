import numpy as np

 # flow = np.array([
#    [0, 9, 7, 1, 10],
#    [9, 0, 10, 3, 7],
#    [7, 10, 0, 4, 10],
#    [1, 3, 4, 0, 4],
#    [10, 7, 10, 4, 0]
# ])
#
# dist = np.array([
#    [0, 147, 511, 266, 405],
#    [147, 0, 429, 285, 547],
#    [511, 429, 0, 353, 772],
#    [266, 285, 353, 0, 425],
#    [405, 547, 772, 425, 0]
# ])

# flow = np.array([
#     [ 0, 64, 89, 80, 63, 65, 26, 81, 36, 73, 66, 28,  5, 67, 37],
#     [64,  0, 68,  9, 44, 18, 78, 67, 49, 98, 31, 66, 84, 36, 78],
#     [89, 68,  0, 21, 49, 99, 32, 44, 72, 92, 75, 45, 97, 14, 21],
#     [80,  9, 21,  0, 47, 24, 32, 67,  8, 31, 59, 39, 53, 74, 72],
#     [63, 44, 49, 47,  0, 69, 94, 31, 89, 49,  3, 43, 88, 50, 31],
#     [65, 18, 99, 24, 69,  0, 42, 78, 55, 60, 90,  8, 51, 28, 45],
#     [26, 78, 32, 32, 94, 42,  0, 78, 12, 86, 50, 66, 18, 70, 30],
#     [81, 67, 44, 67, 31, 78, 78,  0, 21, 15, 85, 28, 31, 65, 22],
#     [36, 49, 72,  8, 89, 55, 12, 21,  0,  4, 50, 66, 49, 19, 28],
#     [73, 98, 92, 31, 49, 60, 86, 15,  4,  0, 57,  8, 79, 37, 40],
#     [66, 31, 75, 59,  3, 90, 50, 85, 50, 57,  0, 43, 52, 75, 19],
#     [28, 66, 45, 39, 43,  8, 66, 28, 66,  8, 43,  0, 55,  7,  5],
#     [ 5, 84, 97, 53, 88, 51, 18, 31, 49, 79, 52, 55,  0, 60, 86],
#     [67, 36, 14, 74, 50, 28, 70, 65, 19, 37, 75,  7, 60,  0, 15],
#     [37, 78, 21, 72, 31, 45, 30, 22, 28, 40, 19,  5, 86, 15,  0]])
#
# dist = np.array(
# [[ 0, 19, 96, 59, 89, 46, 44, 66, 84, 36,  7, 42, 12, 58, 67],
#  [19,  0, 47,  9, 91, 50, 98, 35, 83, 81, 40, 61, 21, 78, 27],
#  [96, 47,  0, 90, 25, 97, 46, 31, 30, 73, 68, 71, 31, 45, 93],
#  [59,  9, 90,  0, 29, 31, 92, 46, 14, 28, 29,  2, 75, 35, 96],
#  [89, 91, 25, 29,  0, 97,  9, 93, 15, 28, 65, 23, 98, 14, 73],
#  [46, 50, 97, 31, 97,  0, 51, 98, 75, 96, 88, 48, 10, 51,  9],
#  [44, 98, 46, 92,  9, 51,  0, 91, 28, 65, 75, 47, 91, 86, 26],
#  [66, 35, 31, 46, 93, 98, 91,  0, 30, 25, 56,  7, 27, 11, 13],
#  [84, 83, 30, 14, 15, 75, 28, 30,  0, 46, 64, 83, 14, 11, 10],
#  [36, 81, 73, 28, 28, 96, 65, 25, 46,  0, 13,  8, 90, 48, 25],
#  [ 7, 40, 68, 29, 65, 88, 75, 56, 64, 13,  0, 90, 97,  4, 56],
#  [42, 61, 71,  2, 23, 48, 47,  7, 83,  8, 90,  0,  8, 92, 42],
#  [12, 21, 31, 75, 98, 10, 91, 27, 14, 90, 97,  8,  0, 62, 42],
#  [58, 78, 45, 35, 14, 51, 86, 11, 11, 48,  4, 92, 62,  0,  8],
#  [67, 27, 93, 96, 73,  9, 26, 13, 10, 25, 56, 42, 42,  8,  0]
#  ])
# 14x14:
flow = np.array(
    [[ 0, 64, 89, 80, 63, 65, 26, 81, 36, 73, 66, 28,  5, 67],
    [64,  0, 68,  9, 44, 18, 78, 67, 49, 98, 31, 66, 84, 36],
    [89, 68,  0, 21, 49, 99, 32, 44, 72, 92, 75, 45, 97, 14],
    [80,  9, 21,  0, 47, 24, 32, 67,  8, 31, 59, 39, 53, 74],
    [63, 44, 49, 47,  0, 69, 94, 31, 89, 49,  3, 43, 88, 50],
    [65, 18, 99, 24, 69,  0, 42, 78, 55, 60, 90,  8, 51, 28],
    [26, 78, 32, 32, 94, 42,  0, 78, 12, 86, 50, 66, 18, 70],
    [81, 67, 44, 67, 31, 78, 78,  0, 21, 15, 85, 28, 31, 65],
    [36, 49, 72,  8, 89, 55, 12, 21,  0,  4, 50, 66, 49, 19],
    [73, 98, 92, 31, 49, 60, 86, 15,  4,  0, 57,  8, 79, 37],
    [66, 31, 75, 59,  3, 90, 50, 85, 50, 57,  0, 43, 52, 75],
    [28, 66, 45, 39, 43,  8, 66, 28, 66,  8, 43,  0, 55,  7],
    [ 5, 84, 97, 53, 88, 51, 18, 31, 49, 79, 52, 55,  0, 60],
    [67, 36, 14, 74, 50, 28, 70, 65, 19, 37, 75,  7, 60,  0]
    ])

dist = np.array(
[[ 0, 19, 96, 59, 89, 46, 44, 66, 84, 36,  7, 42, 12, 58],
 [19,  0, 47,  9, 91, 50, 98, 35, 83, 81, 40, 61, 21, 78],
 [96, 47,  0, 90, 25, 97, 46, 31, 30, 73, 68, 71, 31, 45],
 [59,  9, 90,  0, 29, 31, 92, 46, 14, 28, 29,  2, 75, 35],
 [89, 91, 25, 29,  0, 97,  9, 93, 15, 28, 65, 23, 98, 14],
 [46, 50, 97, 31, 97,  0, 51, 98, 75, 96, 88, 48, 10, 51],
 [44, 98, 46, 92,  9, 51,  0, 91, 28, 65, 75, 47, 91, 86],
 [66, 35, 31, 46, 93, 98, 91,  0, 30, 25, 56,  7, 27, 11],
 [84, 83, 30, 14, 15, 75, 28, 30,  0, 46, 64, 83, 14, 11],
 [36, 81, 73, 28, 28, 96, 65, 25, 46,  0, 13,  8, 90, 48],
 [ 7, 40, 68, 29, 65, 88, 75, 56, 64, 13,  0, 90, 97,  4],
 [42, 61, 71,  2, 23, 48, 47,  7, 83,  8, 90,  0,  8, 92],
 [12, 21, 31, 75, 98, 10, 91, 27, 14, 90, 97,  8,  0, 62],
 [58, 78, 45, 35, 14, 51, 86, 11, 11, 48,  4, 92, 62,  0]
 ])


# flow = np.array([
#    [0, 12,15],
#    [12, 0, 4],
#     [15, 4, 0]
# ])
#
# dist = np.array([
#     [0, 1, 2],
#     [1, 0, 4],
#     [2, 4, 0]
# ])

def cost(flow):
    global dist
    cost = flow*dist
    return np.sum(cost[np.triu_indices(flow.shape[0],1)])*2

# Greedy Approach:
# Find the respective largest range of the rows in the two matrix
# match the smallest value with the largest value, second smallest to second largest
# and so on..
def idxMax(mat):
    maxrow = mat.max(axis=0)  # find max value in each rows
    np.fill_diagonal(mat, 999)
    minrow = mat.min(axis=0)  # find min value in each rows
    np.fill_diagonal(mat, 0)
    max_range = maxrow - minrow  # find the largest range
    return np.where(max_range == np.amax(max_range))[0][0]  # get index of the largest range


def idxSort(A, B):
    list_A = A[idxMax(A), 0:]  # get the row with largest range
    list_B = B[idxMax(B), 0:]

    zero_idx = np.where(list_A == 0)[0][0]  # store index of zero in matrix A
    list_A = np.trim_zeros(list_A)  # remove zeros
    list_B = np.trim_zeros(list_B)
    list_B = np.sort(list_B)[::-1]  # sort list B in desc order
    sorted_list = [list_B for _, list_B in sorted(zip(list_A, list_B))]  # sort min in A match max in B
    sorted_list = np.insert(sorted_list, zero_idx, 0)

    res = []
    for i in sorted_list:
        b = B[idxMax(B), 0:]
        res.append(np.where(b == i)[0][0])  # get the indices of sorted matrix
    return res


def greedHeu(matA, matB):
    global idx
    idx = idxSort(matA, matB)
    return matA[np.ix_(idx, idx)], idx


greedy = greedHeu(flow, dist)
print("Greddy Heuristic solution: " + str(greedy[1]))
print("Greedy Heuristic solution's cost: " + str(cost(greedy[0])))
