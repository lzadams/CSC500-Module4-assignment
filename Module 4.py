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

item1 = ItemToPurchase()
item1.name ='Chocolate Chips'
item1.price = 3.0
item1.quantity = 1
item1_cost = item1.print_item_cost()

item2 = ItemToPurchase()
item2.name = 'Bottled Water'
item2.price = 1.0
item2.quantity = 10
item2_cost = item2.print_item_cost()

#Step 3: Add the costs of the two items together and output the total cost.
total_cost = item1_cost + item2_cost
print(f'Total: ${total_cost}')

