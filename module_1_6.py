print("Работа со словарями:")
my_dict = {'Danil': 2002, 'Ivan': 1999, 'Yura' : 2003 }
print(my_dict)
print(my_dict['Danil'])
print(my_dict.get('Alex'))
my_dict.update({'Igor' : 1995, 'Nikolay': 2007})
del my_dict['Danil']
print(my_dict)

print("Работа со множествами:")
my_set = {9, 9, 1, 3 ,3, 1, 'urban', True}
print(my_set)
my_set.update({(1,2,3,4,5), 'Tolya'})
my_set.discard('urban')
print(my_set)

