i = input().strip()
temp = 1
j = 0
k = len(i) - 1
# проверка на то, состоит ли строка из одной и той же буквы
while j < k + 1:
    if i[j] != i[0] or i[k] != i[0]:
        temp = 0
    j += 1
    k -= 1
# если строка состоит из одной и той же буквы, то выводим -1
if temp == 1:
    print("-1")
    exit()
temp = 1
j = 0
k = len(i) - 1
# проверка на то, палиндром ли наша строка: если да, то выводим длина - 1, если нет, то всю длину
while j < k:
    if i[j] != i[k]:
        temp = 0
    j += 1
    k -= 1
if temp == 1:
    print(len(i) - 1)
else:
    print(len(i))
