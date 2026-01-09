categories = ["Stationery", "Electronics", "Fashion", "Electronics"]
categories_set = set(categories)

categories_set.add("Groceries")
categories_set.add("Electronics")

print(categories_set)
print("Electronics" in categories_set)
print("Total unique categories:", len(categories_set))