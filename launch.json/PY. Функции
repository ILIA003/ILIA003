def sayHello():
    print("Hello world!") # блок принадлежащий функции
# Конец функции

sayHello()
sayHello()

def printMax(a, b):
    if a > b:
        print(a, "максимально")
    elif a == b:
        print(a, "равно", b)
    else:
        print(b, "минимально")

printMax(3, 4)

x = 10
y = 7

printMax(x, y)

def func(x):
    print("x равен", x)
    x = 2
    print("Замена локального x на", x)

func(x)
print("х по прежнему")

x = 50

def func():
    global x

    print("х равно", x)
    x = 2
    print("Заменяем глобальное значение х на", x)

func()
print("Значение х составляет", x) # я глобально зарезервирововал слово, но пока хз что это значит

def func_outher():
    z = 2
    print("z равно", z)
    def func_inner():
        nonlocal z
        z = 5
    func_inner()
    print("Локальное z сменилось на", z)

func_outher()

def say(message, times = 1):
    print(message * times)

say("Привет")
say("Мир", 5)

def func(a, b=5, c=10):
    print("a равно", a, ", b равно", b, ", a c равно", c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

def total(a=5, *numbers, **phonebook):
    print("a", a)

    for single_item in numbers:
        print("single_item", single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)

total(10, 1,  2,  3, extra_number=50)

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "Числа равны."
    else:
        return y

print(maximum(2, 3))

def printmax(x, y):
    ''' Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами.'''
    x = int(x)
    y = int(y)

if x > y:
    print(x, "наибольшее")
else:
    print(y, "наибольшее")

printmax(3, 5)
print(printMax.__doc__)
