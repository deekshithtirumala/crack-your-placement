from collections import Counter

class Solution:
    def validIndex(self, row, col, m, n):
        if (row<0 or row>=m) or (col<0 or col>=n):
            return False
        return True
    def check(self, row, col, word, index, m, n):
        if index>=len(word):
            return True
        if not self.validIndex(row, col, m, n):
            return False
        adj = [[row, col-1],[row-1, col], [row, col+1], [row+1, col]]
        if self.board[row][col]!=word[index] or ((row, col) in self.visited):
            return False
        
        self.visited.append((row, col))
        for i in range(4):
            new_row, new_col = adj[i][0],adj[i][1]
            if self.check(new_row, new_col, word, index+1, m, n):
                return True
        self.visited.pop()
        return False
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.board = board
        self.visited = []
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]]+=1
        counter = Counter(word)
        for i in counter:
            if i not in boardDic or boardDic[i]<counter[i]:
                return False
            
        for row in range(m):
            for col in range(n):
                if self.check(row, col, word, 0, m, n):
                    return True
        return False

    
