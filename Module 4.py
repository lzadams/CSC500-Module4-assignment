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

print('Item 1')
item1 = ItemToPurchase()
item1.name = input('Enter the item name:\n')
item1.price = float(input('Enter the item price:\n'))
item1.quantity = int(input('Enter the item quantity:\n'))
item1_cost = item1.print_item_cost()

print('Item 2')
item2 = ItemToPurchase()
item2.name = input('Enter the item name:\n')
item2.price = float(input('Enter the item price:\n'))
item2.quantity = int(input('Enter the item quantity:\n'))
item2_cost = item2.print_item_cost()

#Step 3: Add the costs of the two items together and output the total cost.
print('TOTAL COST')
print(f'{item1.name} {item1.quantity} @ ${item1.price} = ${item1_cost}')
print(f'{item2.name} {item2.quantity} @ ${item2.price} = ${item2_cost}')
total_cost = item1_cost + item2_cost
print(f'Total: ${total_cost}')

