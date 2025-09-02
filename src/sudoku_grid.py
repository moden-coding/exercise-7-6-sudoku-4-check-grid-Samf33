def sudoku_grid_correct(sudoku: list):
    curr = True
    curr1 = True
    count3 = 0
    count4 = 0
    for i in range(9):
        curr = row_correct(sudoku, i)
        curr1=column_correct(sudoku,i)
        if(curr is False or curr1 is False):
            return False
    for row in sudoku:
        count4=0
        for inte in row:
            if count3 % 3 == 0 and count4 % 3 == 0:
                curr = block_correct(sudoku,count3,count4)
            if curr is False:
                return False
            count4+=1
        count3+=1
    return True
def block_correct(sudoku: list, row_no: int, column_no: int):
    count1=0
    count2=0
    column=[]
    for val in sudoku:
        count2=0
        for valu in val:
            if(count1 >= row_no and count1 < row_no +3 and count2 >= column_no and count2<column_no+3):
                column.append(valu)
            count2+=1
        count1+=1

    count1 = 0
    count2 = 0
    for num in column:
        count1 += 1
        for nom in column:
            count2+=1
            if nom == num and nom != 0 and num != 0 and count1 != count2:
                return False
        count2 = 0
    return True

def column_correct(list : list, column_num : int):
    column = []
    count1 = 0
    for row in list:
        count1 = 0
        for value in row:
            if count1 == column_num:
                column.append(value)
            count1 +=1
    count1 = 0
    count2 = 0
    for num in column:
        count1 += 1
        for nom in column:
            count2+=1
            if nom == num and nom != 0 and num != 0 and count1 != count2:
                return False
        count2 = 0
    return True

def row_correct(sudoku : list, row_index : int):
    count1 = 0
    count2 = 0
    for num in sudoku[row_index]:
        count1 += 1
        for nom in sudoku[row_index]:
            count2+=1
            if nom == num and nom != 0 and num != 0 and count1 != count2:
                return False
        count2 = 0
    return True
if __name__ == "__main__":

    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]

    print(sudoku_grid_correct(sudoku2))

    sudoku = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
        ]
    print(sudoku_grid_correct(sudoku))