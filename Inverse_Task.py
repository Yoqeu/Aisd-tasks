s = input()
q = int(input())
arr = []
s = list(''.join(s))
while q != 0:
    LR = input()
    LR = LR.split()
    LR = list(map(int, LR))
    arr.append(int(LR[0]) - 1)
    arr.append(int(LR[1]) - 1)
    q -= 1
if int(arr[0]) != int(arr[1]):
    if int(arr[0]) > int(arr[1]):
        temp = int(arr[0])
        arr[0] = int(arr[1])
        arr[1] = int(temp)
    while True:
        if int(arr[1]) >= int(arr[0]):
            if s[int(arr[1])].isupper():
                s[arr[1]] = s[int(arr[1])].lower()
            elif s[int(arr[1])].islower():
                s[arr[1]] = s[int(arr[1])].upper()
            arr[1] -= 1
            continue
        else:
            del arr[1]
            del arr[0]
            if not arr:
                break
            else:
                continue
else:
    if s[int(arr[1])].isupper():
        s[arr[1]] = s[int(arr[1])].lower()
    elif s[int(arr[1])].islower():
        s[arr[1]] = s[int(arr[1])].upper()
result = str("".join(map(str, s)))
print(result)