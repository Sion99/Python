a, b = map(int, input().split())
while True:
    n = int(input())
    if n == -999:
        break
    if a <= n <= b:
        print("Nothing to report")
    else:
        print("Alert!")
        break