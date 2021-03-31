i = int(input())
A = input()
A = A.split()
A = list(map(int, A))
A.sort()
if len(A) == 2:
    print(int(A[0]) * int(A[1]))
elif len(A) == 3:
    if int(A[0]) * int(A[1]) < int(A[1]) * int(A[2]):
        if int(A[1]) * int(A[2]) > int(A[0]) * int(A[2]):
            print(int(A[1]) * int(A[2]))
        else:
            print(int(A[0]) * int(A[2]))
    elif int(A[0]) * int(A[1]) > int(A[1]) * int(A[2]):
        if int(A[0]) * int(A[1]) > int(A[0]) * int(A[2]):
            print(int(A[0]) * int(A[1]))
        else:
            print(int(A[0]) * int(A[2]))
    else:
        if int(A[0]) * int(A[1]) > int(A[0]) * int(A[2]):
            print(int(A[0]) * int(A[1]))
        else:
            print(int(A[0]) * int(A[2]))
elif len(A) > 3:
    if int(A[len(A) - 1]) * int(A[len(A) - 2]) > int(A[0]) * int(A[1]):
        print(int(A[len(A) - 1]) * int(A[len(A) - 2]))
    else:
        print((int(A[0]) * int(A[1])))