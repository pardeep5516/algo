A = [12,10,5,15,18,4,16]
hi = 0
mid = 0
cnt = 0
for i in range(0,len(A)):
    cnt += 1
    if A[i] > hi:
        mid = hi
        hi = A[i]
    else:
        cnt += 2
        if A[i] < hi and A[i] > mid:
            mid = A[i]
print("Large element: ", hi)
print("second large: ", mid)
print("comparision", cnt)