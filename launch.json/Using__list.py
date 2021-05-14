shoplist = ["яблоки", "манго", "морковь", "бананы"]

print("Я должен сделать", len(shoplist), "покупки") # указываю свой список покупок и функция len показывает кол-во моих покупок в списке

print("Покупки:", end="  ")
for item in shoplist:
    print(item, end="  ")

print("\nТакже нужно купить риса.")
shoplist.append("рис") # добавляю в свой список покупок рис т. е. этот код отвечает за добавление в список
print("Теперь мой список покупок таков:", shoplist)

print("Отсортирую-ка я свой список")
shoplist.sort() # команда отвечающая за сортировку
print("Отсортированный список покупок выглядит так:", shoplist)

print("Первое, что мне нужно купить, это", shoplist)
olditem = shoplist[0]
del shoplist[0] # нумерация идёт с 0 поэтому первый в списке это бананы
print("Я купил", olditem)
print("Теперь мой список покупок:", shoplist)