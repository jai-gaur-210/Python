if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split()))[:n]
max = lst[0]

for i in lst:
    if(max<i):
        max = i
num = -9999999
for i in lst:
    if(i<max):
        if(num<i):
            num=i 
print(num)
