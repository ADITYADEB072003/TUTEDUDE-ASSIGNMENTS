price_dict = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500,
    "Bottle": 200,
    "Shoes": 1200,
    "Watch": 1500
}

price_dict["Laptop"] = 45000
price_dict["Pen"] = 12
price_dict.pop("Bottle", None)

avg_price = sum(price_dict.values()) / len(price_dict)
print("Average Price:", avg_price)

print("Max Price:", max(price_dict, key=price_dict.get))
print("Min Price:", min(price_dict, key=price_dict.get))