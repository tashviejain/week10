#Reflection Questions:
#1. The most suprising thing about how lists work in Python is that they can be changed after they are created by using methods like append () and remove (). I thought you would have to completely go back and edit the entire list.
#2. In geology, I could have used a python list to organize ages of rock layers when learning about realtive dating. 

#Exercise 1: Build the list
print("---Exercise 1:")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Exercise 2: Index Practice
print("--- Exercise 2: Index Practice ---")
print(inventory [0])
print(inventory [-1])

middle = len(inventory) // 2
print(inventory[middle]) 

#Exercise 3: Last Slicing
print ("---Exercise 3: List Slicing ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Exercise 4: List Methods
print("---Exercise 4: List Methods ---")

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.remove("stapler")
print(inventory)

#Exercise 5
print("--- Exercise 5: Tuple Compaision ---")
coords = (40.7128, -74.0060)

coords [0] = 99
try:
    coords [0]
except TypeError as error:
    print(f"TypeError caught: {error}")
print("Tuples protect coordiantes from being changed by accidentally.")

#Exercise 6
print("---Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Numbeer of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales [0]
worst = sales [0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

#Exercise 7
print("---Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9,2))
print(prices)
print(discounted)

#Exercise 8
print("---Exercise 8: Filter above threshold ---")
slaes = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print (high_sales)
print("Count:", len(high_sales))
print("Avg:", sum(high_sales) / len(high_sales))
