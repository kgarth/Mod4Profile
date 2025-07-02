class ItemToPurchase:
	item_name = ''
	item_price = 0.0
	item_quantity = 0

	def __init__(self, name='', price=0.0, quantity=0):
		self.item_name = name
		self.item_price = price
		self.item_quantity = quantity

	def total_cost(self):
		return self.item_price * self.item_quantity

	def print_item_cost(self):
		print('{} {} @ ${:.2f} = ${}'.format(
			self.item_name, 
			self.item_quantity, 
			self.item_price, 
			self.item_quantity * self.item_price))