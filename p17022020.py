#Strassen's Matrix Multiplication
a=[[1,2],[2,1]]
b=[[3,4],[4,2]]
c=[[0,0],[0,0]]
m=[]
m.append((a[0][0]+a[1][1]) * (b[0][0]+b[1][1]))
m.append((a[0][1]-a[1][1]) * (b[1][0]+b[1][1]))
m.append((a[0][0]-a[1][0]) * (b[0][0]+b[0][1]))
m.append((a[0][0]+a[0][1]) * b[1][1])
m.append(a[0][0] * (b[0][1]-b[1][1]))
m.append(a[1][1] * (b[1][0]-b[0][0]))
m.append((a[1][0]+a[1][1]) * b[0][0])
c[0][0]=m[0]+m[1]-m[3]+m[5]
c[0][1]=m[3]+m[4]
c[1][0]=m[5]+m[6]
c[1][1]=m[0]-m[2]+m[4]-m[6]
print(a)
print(b)
print("Product Matrix")
print(c)
