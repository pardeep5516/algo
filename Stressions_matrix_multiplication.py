a = [[1,2], [2,1]]
b = [[3,4], [4,2]]
c = [[0,0], [0,0]]

m = []

#P 0
m.append((a[0][0] + a[1][1]) * (b[0][0] + b[1][1]))

#Q 1
m.append(b[0][0] * (a[1][0] + a[1][1]))

#R 2
m.append(a[0][0] * (b[0][1] - b[1][1]))

#S 3
m.append(a[1][1] * (b[1][0] - b[0][0]))

#T 4
m.append(b[1][1] * (a[0][0] + a[0][1]))

#U 5
m.append((a[1][0] - a[0][0]) * (b[0][0] + b[0][1]))

#V 6
m.append((b[1][0] + b[1][1]) * a[0][1] - a[1][1])

print(m)

c[0][0] = m[0] + m[3] - m[4] + m[6]

c[0][1] = m[2] + m[4]

c[1][0] = m[1] + m[3]

c[1][1] = m[0] + m[2] - m[1] + m[5]

print(a)
print(b)
print("result")
print(c)