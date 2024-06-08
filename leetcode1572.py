mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
diagonal = 0
n = len(mat)
for i in range(n):
    diagonal += mat[i][i]
    diagonal += mat[i][n - 1 - i]  
if n % 2 == 1:
    diagonal -= mat[n // 2][n // 2]

print(diagonal)