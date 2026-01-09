daily_sales = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sale in daily_sales:
    if sale == -1:
        print("Corrupted data found. Stopping.")
        break
    elif sale == 0:
        continue
    else:
        total_sales += sale
        print("Running Total:", total_sales)

print("Final Total Sales:", total_sales)