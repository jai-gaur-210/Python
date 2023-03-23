N = int(input())

list = []
for x in range(N):
    p = input()
    
    q= float(input())
    lst = [p,q]
    list.append(lst)
    
    
final = []    
min = list[0][1]
num = 999999999999
for x in list:
    if(min>x[1]):
        min = x[1]
for x in list:
    if(x[1]>min):
        if(num>x[1]):
            num = x[1]

            
for x in list:
    if(x[1]==num):
        final.append(x[0])
            
final.sort()