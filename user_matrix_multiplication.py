m = int(input("enter number of row of matrix: "))
n = int(input("enter nymber of column of matrix: "))

A = []
for i in range(m):
    A.append([])
print("Enter the element of matrix 1: ")
for i in range(m):
    for j in range(n):
        x = int(input())
        A[i].append(x)

print("number of row of matrix 2 must be equal to number of column in matrix 1.")
p = int(input("Enter number of row in matrix 2: "))
q = int(input("Enter number of column in matrix 2: "))

if n == p:
    B = []
    for i in range(p):
        B.append([])
    print("Enter the number of element in matrix 2: ")
    for i in range(p):
        for j in range(q):
            x = int(input())
            B[i].append(x)

    result = []
    for i in range(m):
        result.append([])
    for i in range(n):
        for j in range(q):
            result[i].append(j)
            result[i][j] = 0
    for i in range(m):
        for j in range(q):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    print(result)
else:
    print("matrix cant multiply")