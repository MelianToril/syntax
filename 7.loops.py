# *** Циклы ***

# Оператор while 

# бесконечный цикл
# while True: 
#     print("alisa!")

# цикл с условием
val_1 = 0

# while val_1 <= 10:
#     print(f"Значение: {val_1}")
#     # инкремент
#     # val_1 = val_1 + 1
#     val_1 += 1

# прерывание цикла по дополнительному условию

# while True:
#     val = input("Введите имя: ")
#     if val == "stop":
#         print("Bye-bye!")
#         break
#     print(f"Привет, {val}!")

# пропуск части кода тела цикла

val = 0

# while val < 20:
#     # 1 кусок кода
#     print(val_1)
#     val += 1 

#     if val > 10:
#         continue
#     # 2 кусок кода
#     print("alisa")

#     if val < 10:
#         continue

#     # 2 кусок кода
#     break


# Оператор for

# 1 шаг. "чтение" значения итерируемого объекта с последовательностью по порядку
# 2 шаг. каждое считанное значение присваивает в собственную переменную
# 3 шаг. выполняет код тела

list_0 = [50, 40, 30, 20, 10, 5]

# for var in list_0:
#     var *= 10
#     print(var)

my_dict = dict(a=100, b=200, c=300)

# print(my_dict)

# for item in my_dict.items():
#     print(item)

# for key, val in my_dict.items():
#     print(f"Ключ: {key}, Значение: {val}")

# for char in "hello, alisa!":
#     print(char)

# класс range()

r = range(0, 10)
r = range(0, 20, 2)

# print(tuple(r))

# for num in range(10):
#     print(num)

# безыменная переменная
for _ in range(5):
    print("alisa")

# дз генератор списка
# дз генератор словаря