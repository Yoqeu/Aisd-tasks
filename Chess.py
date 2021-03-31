i = input()
i = i.split()
n = int(i[0])
m = int(i[1])
x_1 = int(i[2])
y_1 = int(i[3])
x_2 = int(i[4])
y_2 = int(i[5])
sub_x = abs(x_1 - x_2)
sub_y = abs(y_1 - y_2)
if sub_x != sub_y:
    print("YES")
else:
    print("NO")
