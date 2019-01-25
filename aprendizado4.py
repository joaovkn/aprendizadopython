heights = [61, 70, 67, 64, 65]
broken_heights = [65, 71, 59, 62]

#---------------------------------------------------

ints_and_strings = [1, 2, 3, 'four', 'five', 'banana']
sam_height = ['Sam', 67]

#--------------------------------------------------

heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

ages = [['Aaron', 15], ['Dhruti', 16]] 

#-----------------------------------------------------

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
print(names_and_dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

#----------------------------------------------------

my_empty_list = []

#----------------------------------------------------

orders = ['daisies', 'periwinkle']
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)

#------------------------------------------------------
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
new_orders = orders + ['lilac','iris']
print(new_orders)
# Create new orders here:
broken_prices = [5, 3, 4, 5, 4] + [4]

#------------------------------------------------------
list1 = range(0,9)
range1 = range(0,8)
#------------------------------------------------------
list1 = range(5, 15, 3)
list2 = range(0, 40, 5)
#-----------------------------------------------------
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip(first_names, all_ages)
ids = range(4)
