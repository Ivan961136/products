import os #operation system

products = []

#read file
if os.path.isfile('products.csv'):
	print('There is the file.')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'name,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('There is not that file.')

#user input
while True:
	name = input('plese enter the product name:')
	if name == 'q':
		break
	price = input('plese enter the product price:')
	price = int(price)
	products.append([name, price])
print(products)

#print record
for p in products:
	print(p[0], '的價格是', p[1])

#write file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('name,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')