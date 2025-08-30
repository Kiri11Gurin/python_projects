import copy
from collections import Counter
class Solution:
    main_board = []

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        boxes = {i: set() for i in range(9)}
        rowes = {i: set() for i in range(9)}
        columns = {i: set() for i in range(9)}
        counter = 0
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rowes[r].add(board[r][c])
                    columns[c].add(board[r][c])
                    boxes[r // 3 * 3 + c // 3].add(board[r][c])
                else:
                    counter += 1

        def rec(boxes, rowes, columns, board, counter):
            while counter > 0:
                prev_counter = counter
                for r in range(9):
                    row_nums = Counter()
                    column_nums = Counter()
                    box_nums = Counter()
                    for c in range(9):
                        if board[r][c] == '.':
                            row_taken_vals = rowes[r] | columns[c] | boxes[r // 3 * 3 + c // 3]
                            if len(row_taken_vals) == 9:
                                return
                            row_nums.update(set('123456789') - row_taken_vals)
                        if board[c][r] == '.':
                            column_taken_vals = rowes[c] | columns[r] | boxes[c // 3 * 3 + r // 3]
                            if len(column_taken_vals) == 9:
                                return
                            column_nums.update(set('123456789') - column_taken_vals)
                        if board[r // 3 * 3 + c // 3][r % 3 * 3 + c % 3] == '.':
                            box_taken_vals = rowes[r // 3 * 3 + c // 3] | columns[r % 3 * 3 + c % 3] | boxes[r]
                            if len(box_taken_vals) == 9:
                                return
                            box_nums.update(set('123456789') - box_taken_vals)
                    for num, count in row_nums.items():
                        if count != 1:
                            continue
                        for c in range(9):
                            if board[r][c] != '.':
                                continue
                            if num in (set('123456789') - (rowes[r] | columns[c] | boxes[r // 3 * 3 + c // 3])):
                                board[r][c] = num
                                rowes[r].add(num)
                                columns[c].add(num)
                                boxes[r // 3 * 3 + c // 3].add(num)
                                counter -= 1
                                break
                    for num, count in column_nums.items():
                        if count != 1:
                            continue
                        for c in range(9):
                            if board[c][r] != '.':
                                continue
                            if num in (set('123456789') - (rowes[c] | columns[r] | boxes[c // 3 * 3 + r // 3])):
                                board[c][r] = num
                                rowes[c].add(num)
                                columns[r].add(num)
                                boxes[c // 3 * 3 + r // 3].add(num)
                                counter -= 1
                                break
                    for num, count in box_nums.items():
                        if count != 1:
                            continue
                        for c in range(9):
                            if board[r // 3 * 3 + c // 3][r % 3 * 3 + c % 3] != '.':
                                continue
                            if num in (set('123456789') - (rowes[r // 3 * 3 + c // 3] | columns[r % 3 * 3 + c % 3] | boxes[r])):
                                board[r // 3 * 3 + c // 3][r % 3 * 3 + c % 3] = num
                                rowes[r // 3 * 3 + c // 3].add(num)
                                columns[r % 3 * 3 + c % 3].add(num)
                                boxes[r].add(num)
                                counter -= 1
                                break

                # посмотреть какие числа могут быть в ячейках:
                # if prev_counter == counter:
                #     for r in range(9):
                #         for c in range(9):
                #             if board[r][c] == '.':
                #                 val = set('123456789') - (rowes[r] | columns[c] | boxes[r // 3 * 3 + c // 3])
                #                 val = ''.join(str(e) for e in sorted(val))
                #                 print(val.ljust(7), end=' ')
                #             else:
                #                 print(str(board[r][c]).ljust(7), end=' ')
                #         print()
                # return

                if prev_counter == counter:
                    for r in range(9):
                        for c in range(9):
                            if board[r][c] == '.':
                                val = rowes[r] | columns[c] | boxes[r // 3 * 3 + c // 3]
                                if len(val) < 9:
                                    for num in set('123456789') - val:
                                        copy_board = copy.deepcopy(board)
                                        copy_board[r][c] = num
                                        copy_rowes = copy.deepcopy(rowes)
                                        copy_rowes[r].add(copy_board[r][c])
                                        copy_columns = copy.deepcopy(columns)
                                        copy_columns[c].add(copy_board[r][c])
                                        copy_boxes = copy.deepcopy(boxes)
                                        copy_boxes[r // 3 * 3 + c // 3].add(copy_board[r][c])
                                        rec(copy_boxes, copy_rowes, copy_columns, copy_board, counter - 1)
                                    return
                                else:
                                    return

            self.main_board[:] = copy.deepcopy(board)
            return

        rec(boxes, rowes, columns, board, counter)
        board[:] = copy.deepcopy(self.main_board)
        return


board = [["8",".",".",".",".",".",".",".","."],
         [".",".","3","6",".",".",".",".","."],
         [".","7",".",".","9",".","2",".","."],
         [".","5",".",".",".","7",".",".","."],
         [".",".",".",".","4","5","7",".","."],
         [".",".",".","1",".",".",".","3","."],
         [".",".","1",".",".",".",".","6","8"],
         [".",".","8","5",".",".",".","1","."],
         [".","9",".",".",".",".","4",".","."]]


res = Solution()
res.solveSudoku(board)
for row in board:
    print(*row)
