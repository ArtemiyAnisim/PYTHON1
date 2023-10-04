# задача первое и последнее вхождения

s = input()
a = s.find('f')
b = s.rfind('f')
if a == -1 and b == -1:
    print("ничего")
elif a >= 0 and b >= 0:
    print(a, b)
elif a >= 0 and b == -1:
    print(a)
elif a == -1 and b >= 0:
    print(b)