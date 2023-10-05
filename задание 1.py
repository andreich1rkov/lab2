a = int(input("введите число a :  "))
b = int(input("введите число b :  "))
print()

print("сумма чисел a и b =  ", a + b)
print()

print("разность чисел a и b =  ", a - b)
print()

print("произведение чисел a и b =  ", a * b)
print()

print("среднее арифметическое чисел a и b =  ", (a + b)/2)
print()


print("Разность максимального и минимального по модулю =  ", max(abs(a),abs(b)) - min(abs(a),abs(b)) )
print()

c = a/b

print(f"Частное a и b точностью до сотых: {c:.2f}")