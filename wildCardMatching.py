class Solution(object):
    def isMatch(self, s, p):
        m=len(s)
        n=len(p)
        
        if (n==0):
            return (m==0)
        
        table = []

#table = np.zeros((m+1,n+1), dtype=bool)

        for i in range (0, m+1):
            new = []
            for j in range (0, n+1):
                new.append(False)
            table.append(new)

        table[0][0]=True
        for j in range(1,n+1):
            if (p[j-1]=='*'):
                table[0][j] = table[0][j-1]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (s[i-1] == p[j-1] or p[j-1]=='?'):
                    table[i][j] = table[i-1][j-1]
                elif (p[j-1]=='*'):
                    table[i][j] = table[i][j-1] or table[i-1][j]
                else:
                    table[i][j] = False
      
        return table[m][n]