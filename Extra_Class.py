l = [1,2,3,4,]
cl =[]

for i in range(len(l)):
    c = l[i]
    d = l[-1]
    x = c * d
    if x%2 ==0:
        cl.append(x)

print(cl)
