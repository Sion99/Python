def simple_interest(p, r, t):
    return p * r * t


def simple_interest_amount(p, r, t):
    return p * (1 + r * t)


p, r, t = map(float, input().split())
print(simple_interest(p, r, t))
print(simple_interest_amount(p, r, t))