products = ["Pen", "Notebook", "Bag", "Bottle", "Shoes", "Watch"]
sample_product = ("Pen", 10, "Stationery")

print(products[1])
print(products[-1])

products.append("Laptop")
products.append("Mouse")
print(products)

temp = list(sample_product)
temp[1] = 15
sample_product = tuple(temp)
print(sample_product)