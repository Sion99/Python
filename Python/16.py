def korean_number(n):
    if n == 1:
        print("일")
    elif n == 2:
        print("이")
    elif n == 3:
        print("삼")
    elif n == 4:
        print("사")
    elif n ==5:
        print("오")
    elif n ==6:
        print("육")
    elif n == 7:
        print("칠")
    elif n == 8:
        print("팔")
    elif n == 9:
        print("구")
    else:
        print("십")

n = int(input())
korean_number(n)