# все делители числа 1 087 388 483 это 1, 1021, 1031, 1033, 1052651, 1054693, 1065023, 1087388483,
# а 1 021, 1 031, 1 033 являются простыми, при этом 1087388483 = 1 052 651 * 1033,
# 1087388483 = 1 054 693 * 1031 , 1087388483 = 1 065 023 * 1021, и при этом
# 1052651 = 1021 * 1031, 1054693 = 1021 * 1033, 1065023 = 1031 * 1033
i = int(input())
arr = []
while i > 0:
    arr_num = int(input())
    arr.append(arr_num)
    i -= 1
if 1021 in arr and 1031 in arr and 1033 in arr:
    print("YES")
elif 1052651 in arr and 1033 in arr:
    print("YES")
elif 1054693 in arr and 1031 in arr:
    print("YES")
elif 1065023 in arr and 1021 in arr:
    print("YES")
elif 1087388483 in arr:
    print("YES")
else:
    print("NO")


