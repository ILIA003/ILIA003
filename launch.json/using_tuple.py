zoo = ("питон", "слон", "пингвин")
print("количество животных в зоопарке -", len(zoo)) # len указывает кол-во

new_zoo = "обезьянка", "верблюд", zoo
print("Количество клеток в зоопарке -", len(new_zoo))
print("Все животные в новом зоопарке:", new_zoo)
print("Животные, привезённые из старого зоопарка -", new_zoo[2]) # [2] указывает на кол-во животных, отсчёт 0, 1, 2
print("Последнее животное, привезённое из старого зоопарка -", new_zoo[2][2]) # [2] вторая подтверждает что только нужен 3 это пингвин
print("Количество животных в новом зоопарке -", len(new_zoo))-1 + \
        len(new_zoo[2])