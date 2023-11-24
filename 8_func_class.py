# *** Функция ***

# создание функции
# не обладает параметрами и ничего не возвращает
def func_1():
    print("hello alisa")

# обладает параметрами и ничего не возвращает
def func_2(par_0, par_1, par_2=5):
    res = par_0 + par_1 + par_2
    print(res)

# обладает параметрами и возвращает что-то
def func_3(par_1):
    res = par_1 ** 2
    return res

# вызов функции
# func_2(10, 20, 30)
# result = func_3(10)

# print(result)


# *** Классы ***

# создание класса
class Cat:
    # метод-конструктор
    def __init__(self, name, a):
        # атрибуты
        self.name = name
        self.age = a

    # метод экземпляра - функция объекта
    def kis(self):
        res = f"kis-kis! My name is {self.name}! Age = {self.age}."
        print(res)

# создание экземпляров (объектов) класса Cat
c_0 = Cat("Kitty", 5)
c_1 = Cat("Mary", 3)
c_2 = Cat("Missy", 1)

# вызов метода
# c_0.kis()
# c_1.kis()

# работа с атрибутами
# c_2.name = "Missy"
# print(c_2.name)

# c_2.kis()
