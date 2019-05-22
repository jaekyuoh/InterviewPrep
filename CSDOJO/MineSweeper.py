# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for bomb in bombs:
        field[bomb[0]][bomb[1]] = -1
        up = bomb[0]-1
        down = bomb[0]+1
        left = bomb[1]-1
        right = bomb[1]+1
        if down < num_rows:
            if field[down][bomb[1]] != -1:
                field[down][bomb[1]] += 1 
            if right < num_cols and field[down][right] != -1:
                field[down][right] += 1
            if left >= 0 and field[down][left] != -1:
                field[down][left] += 1

        if up >= 0: 
            if field[up][bomb[1]] != -1:
                field[up][bomb[1]] += 1
            if right < num_cols and field[up][right] != -1:
                field[up][right] += 1
            if left >= 0 and field[up][left] != -1:
                field[up][left] += 1

        if right < num_cols and field[bomb[0]][right] != -1:
            field[bomb[0]][right] += 1

        if left >= 0 and field[bomb[0]][left] != -1:
            field[bomb[0]][left] += 1
    return field

def mine_sweeper_dojo(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for bomb in bombs:
        (row_i, col_i) = bomb
        field[row_i][col_i] = -1
        for i in range(row_i - 1, row_i + 2):
            for j in range(col_i - 1, col_i + 2):
                if (0 <= i < num_rows and 0 <= j < num_cols
                        and field[i][j] != -1):
                    field[i][j] += 1
    return field

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# # NOTE: The following input values will be used for testing your solution.
# print(mine_sweeper([[0, 2], [2, 0]], 3, 3)) # should return:
# # [[0, 1, -1],
# #  [1, 2, 1],
# #  [-1, 1, 0]]

# print(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)) # should return:
# # [[-1, -1, 2, 1],
# #  [2, 3, -1, 1],
# #  [0, 1, 1, 1]]

print(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)) # should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]