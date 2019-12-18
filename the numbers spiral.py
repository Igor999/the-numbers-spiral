n = int(input())
matrix = [[0]*n for i in range(n)]
st, m = 1, 0
result_matrix = ""
matrix[n//2][n//2]=n*n
for v in range(n//2):
    for i in range(n-m):
        matrix[v][i+v] = st
        st+=1
    for i in range(v+1, n-v):
        matrix[i][-v-1] = st
        st+=1
    for i in range(v+1, n-v):
        matrix[-v-1][-i-1] =st
        st+=1
    for i in range(v+1, n-(v+1)):
        matrix[-i-1][v]=st
        st+=1
    m+=2
for i in matrix:
    for h in i:
        result_matrix += str(h)+" "
    result_matrix += "\n"
print(result_matrix)