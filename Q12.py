if __name__ == '__main__':
    N = int(input())
    
lst = []

for i in range(N):
    fun , *value = input().split()
    l = list(map(int, value))
    if(fun == "insert"):
        
        lst.insert(l[0], l[1])
    elif(fun == "remove"):
        lst.remove(l[0])
    elif(fun == "append"):
        lst.append(l[0])
    elif(fun == "sort"):
        lst.sort()
    elif(fun == "pop"):
        lst.pop()
    elif(fun == "reverse"):
        lst.reverse()
    elif(fun == "print"):
        print(lst)