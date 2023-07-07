products = []
while True:
	name = input('plese enter the product name:')
	if name == 'q':
		break
	price = input('plese enter the product price:')
	products.append([name, price])
print(products)