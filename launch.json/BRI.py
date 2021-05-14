bri = set(["Бразилия", "Россия", "Индия"])
"Индия" in bri
True
"США" in bri
False
bric = bri.copy()
bric.add("Китай")
bric.issuperset(bri)
True
bri.remove("Россия")
bri & bric
{"Бразилия", "Индия"}