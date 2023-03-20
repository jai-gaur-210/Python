if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    
i=0 
j=0
k=0
list = []

for p in range(x+1):
    for q in range(y+1):
        for r in range(z+1):
            if(p+q+r != n):
                lst = [p,q,r]
                list.append(lst)
   
print(list)
