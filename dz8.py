#1
bread = ['хлеб', 1]
cake = ['торт', 1]
#2
household_chemicals = [['стиральный порошок', 1],['средство для мытья посуды', 1]]
#3
Names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

names_and_dogs_names = zip(Names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
#4
orders = ['маргаритки', 'васильки']
print(orders)

orders.append('тюльпаны')
orders.append('розы')
print(orders)
#5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

new_orders = orders + ['сирень', 'ирис']

broken_prices = [5, 3, 4, 5, 4] + [4]