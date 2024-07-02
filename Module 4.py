#Step 1: Build the ItemToPurchase class
class ItemToPurchase:
    name = ''
    price = 0.0
    quantity = 0
    def print_item_cost(self):
        total_cost = self.quantity * self.price
        print(f'{self.name} {self.quantity} @ ${self.price} = ${self.quantity * self.price}')
        return total_cost

#Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
items = [] 
for i in range(2):
    print(f'Item {i + 1}')
    item = ItemToPurchase()
    item.name = input('Enter the item name:\n')
    item.price = float(input('Enter the item price:\n'))
    item.quantity = int(input('Enter the item quantity:\n'))
    items.append(item)
    item_cost = item.print_item_cost()
    i = i + 1

#Step 3: Add the costs of the two items together and output the total cost.
print('TOTAL COST')
total_cost = 0 
for item in items:
    total_cost += item.print_item_cost()
    print(f'Total: ${total_cost}')


