class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(len(board)):
            row = board[x]
            left_to_right = [0] * 9
            top_to_bottom = [0] * 9
            three_by_three = [0] * 9
            for y in range(len(row)):
                if row[y] != ".":
                    left_to_right[int(row[y]) - 1] += 1
                    if left_to_right[int(row[y]) - 1] > 1:
                        return False
                if board[y][x] != ".":
                    top_to_bottom[int(board[y][x]) - 1] += 1
                    if top_to_bottom[int(board[y][x]) - 1] > 1:
                        return False
                if board[int(y / 3) + (int(x / 3) * 3)][(y % 3) + (3 * (x % 3))] != ".":
                    three_by_three[int(board[int(y / 3) + (int(x / 3) * 3)][(y % 3) + (3 * (x % 3))]) - 1] += 1
                    if three_by_three[int(board[int(y / 3) + (int(x / 3) * 3)][(y % 3) + (3 * (x % 3))]) - 1] > 1:
                        return False
        return True


