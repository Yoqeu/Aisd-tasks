i = input().strip()
last = len(i)
first = int(i.index(i[0]))
temp_temp = [1]
temp = []
steps = 0
for x in temp_temp:
    if first == len(i):
        break
    elif first == last:
        first += 1
        last = len(i)
        temp_temp.append(1)
        continue
    elif i[first:last] in temp:
        last -= 1
        temp_temp.append(1)
        continue
    else:
        temp.append(i[first:last])
        steps += 1
        last -= 1
        temp_temp.append(1)
        continue
print(steps)
