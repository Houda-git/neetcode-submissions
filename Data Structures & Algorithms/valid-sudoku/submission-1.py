class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we try to verify the rows and columns
        for i in range(9):
            seen_h = set()
            seen_v = set()
            for j in range(9):
                candidat_h = board[i][j]
                candidat_v = board[j][i]
                if candidat_h != ".":
                    if candidat_h in seen_h:
                        return False
                    seen_h.add(candidat_h)
                if candidat_v != ".":
                    if candidat_v in seen_v:
                        return False
                    seen_v.add(candidat_v)
        # We verify the 3*3 box
        # we do the corners
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        candidate = board[row+i][col+j]
                        if candidate != ".":
                            if candidate in seen:
                                return False
                            seen.add(candidate)
        return True

            
        