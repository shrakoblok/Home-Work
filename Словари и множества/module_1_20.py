# Словари
my_dict = {'Денис': 1997, 'Инна': 1998, 'Андрей': 1994}
print(my_dict)
print(my_dict['Денис'])
print(my_dict.get('Маша'))
my_dict.update({'Кирилл': 1995,
                'Лиза': 2000})
print(my_dict)
a = my_dict.pop('Кирилл')
print(a)
print(my_dict)

# Множества
my_set = {1, 2, 3, 4, 2, 55, 34, 22, 34, True, 'Hi', 'Hello'}
print(my_set)
my_set.add(11)
my_set.add(66)
print(my_set)
my_set.remove(11)
print(my_set)