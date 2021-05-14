ab = {"Swaroop" : "swaroop@swaroopch.com",
            "Larry" : "larry@wall.org",
            "Matsumoto" : "matz@ruby-lang.org",
            "Spammer" : "spammer@hotmail.com"
        }
print("Адрес Swaroop'a:", ab["Swaroop"])

del ab["Spammer"]

print("\nВ адресной строке {0} контакта\n".format(len(ab)))

for name, addres in ab.items():
    print("Контакт {0} с адресом {1}".format(name, addres))

ab["Guido"] = "guido@python.org"

if "Guido" in ab:
    print("\nАдрес Guido:", ab["Guido"])
    