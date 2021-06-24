n = int(input())

if n%4 != 0:
    print("평년")
else:
    if n % 100 != 0:
        print("윤년")
    else:
        if n % 400 != 0:
            print("평년")
        else:
            print("윤년")
