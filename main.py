from ItemToPurchase import ItemToPurchase

def main():
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print('Item1:')
    item1.item_name = input('Enter the item name: ')
    
    while True:
        try:
            item1.item_price = float(input('Enter the item price: '))
            if item1.item_price < 0:
                raise ValueError
        except ValueError:
            print('Please enter a number greater then 0')
        break
    
    while True:
        try:
            item1.item_quantity = int(input('Enter the item quantity: '))
            if item1.item_quantity < 0:
                raise ValueError
        except ValueError:
            print('Please enter a number greater than 0')
        break

    print('Item2:')
    item2.item_name = input('Enter the item name: ')

    while True:
        try:
            item2.item_price = float(input('Enter the item price: '))
            if item2.item_price < 0:
                raise ValueError
        except ValueError:
            print('Please enter a number greater then 0')
        break
    
    while True:
        try:
            item2.item_quantity = int(input('Enter the item quantity: '))
            if item2.item_quantity < 0:
                raise ValueError
        except ValueError:
            print('Please enter a number greater than 0')
        break

    print('Total Cost:')
    item1.print_item_cost()
    item2.print_item_cost()
    print('Total: ${}'.format(item1.total_cost() + item2.total_cost()))



if __name__ == '__main__':main()