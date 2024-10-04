import random
matrix = [[random.randint(1,10)for i in range(3)] for j in range(3)]
for row in matrix:
    for element in row:
        print(element, end='\t') #ставим в конце tab
    print()
print()
print()
count = 1 #сбрасываем счетчик
for row in matrix:
    if count != 2:
        row.reverse() #разворачиваем строки
    for element in row:
        print(element, end='\t') #ставим в конце tab
    print()  #переносим строки
    count += 1  #счётчик