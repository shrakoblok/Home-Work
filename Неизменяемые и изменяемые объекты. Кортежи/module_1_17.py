immutable_var = 1, 2, 'Привет', False
print(immutable_var)
#immutable_var[0] = 2
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
mutable_list = [1, 2, 'Hello', True]
mutable_list[0:5] = [10, 20, 'Привет', False]
print(mutable_list)
mutable_list[2] = 30
mutable_list[3] = 40
print(mutable_list)