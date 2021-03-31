i = int(input())
str(i)
# переводим значения в список
res = [int(x) for x in str(i)]
# проверка на то, состоит ли список из 1 элемента и меньше
if len(res) < 2:
    print("-1")
    exit()
first_num = len(res) - 1
second_num = len(res) - 2
# проверка на то является ли в второй элемент больше первого(если всего 2 числа)
if len(res) == 2 and res[first_num] <= res[second_num]:
    print("-1")
    exit()
# создание переменной для прохода по циклу
# длина - 1 создаётся именно так, потому что для прохода по циклу нужно будет уменьшать переменную
x = len(res) - 1

while x >= -1:
    x -= 1
    # проверка на выход за пределы списка
    if x == -1:
        print("-1")
        exit()
    # находим первое меньшее число, которое будет переставлено
    if res[x] >= res[x + 1]:
        continue
    elif res[x] < res[x] + 1:
        first_num = x
        break
# здесь уже отсчёт идёт от первого числа
x = len(res) - 1
while x > -1:
    # находим первое число с которым поменяем местами
    if res[x] <= res[first_num]:
        x -= 1
        continue
    else:
        second_num = x
        temp = res[second_num]
        res[second_num] = res[first_num]
        res[first_num] = temp
        break
# в цикле меняем местами оставшуются часть, чтобы получилось от меньшего к большему
second_num = len(res) - 1
x = first_num + 1
while x < second_num:
    temp = res[x]
    res[x] = res[second_num]
    res[second_num] = temp
    second_num -= 1
    x += 1
# вносим список в одну переменную и выводим
result = int("".join(map(str, res)))
print(result)
