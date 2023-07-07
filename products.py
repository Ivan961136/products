import os #operation system

#read file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'name,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#user input
def user_input(products):
	while True:
		name = input('plese enter the product name:')
		if name == 'q':
			break
		price = input('plese enter the product price:')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#print record
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#write file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('name,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	#check file exist or not
	if os.path.isfile(filename):
		print('Find the file.')
		products = read_file(filename)
	else:
		print('Not find the file.')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()