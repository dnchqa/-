a1, a2, x = int(input()), int(input()), input()
if x == '+':
    print(a1 + a2)
elif x == '-':
    print(a1 - a2)
elif x == '*':
    print(a1 * a2)
elif x == '/':
    if a2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(a1 / a2)
else:
    print("Неверная операция")