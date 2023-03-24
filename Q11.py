if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

lst= []    
for i in student_marks:
    if(i == query_name):
        lst.append(student_marks[i])
ans = 0.0
for i in lst[0]:
    ans = ans + i
    
final = ans/3
print('%.2f'%final)
