DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:

    def findWords(self, board, words):
        if board is None or len(board) == 0:
            return []
        
        wordSet = set(words)
        prefixSet = set()
        for word in words:
            for i in range(len(word)):
                prefixSet.add(word[:i + 1])
        
        final = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.findWordsHelper(board,i,j,board[i][j],wordSet,prefixSet,set([(i, j)]),final,)
                
        return list(final)
        
    def findWordsHelper(self, board, x, y, word, wordSet, prefixSet, visited, final):
        if word not in prefixSet:
            return
        
        if word in wordSet:
            final.add(word)
        
        for row, col in DIR:
            x1 = x + row
            y1 = y + col
            
            if not self.check(board, x1, y1):
                continue
            if (x1, y1) in visited:
                continue
            
            visited.add((x1, y1))
            self.findWordsHelper(board,x1,y1,word + board[x1][y1],wordSet,prefixSet,visited,final,)
            visited.remove((x1, y1))
            
    def check(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])