#Словарь. Условия задачи:

my_list = [42, 43]

my_dict = {'foo': {'a': 12, 'b': (1, 2, 3, 4, my_list)},
'bar': {'c': 12, 'd': {5, 6, 7, 8}},
'moo': {'e': 12, 'f': {'Lol': ['L', 'o', 'l']}}}

# 7 Вывести множество

print(my_dict['bar']['d'])

# 8 Удалить из списка элемент 'о'

my_dict['moo']['f']['Lol'].remove('o')
print(my_dict['moo']['f']['Lol'])

# 9 Добавьте в словарь, который является значением ключа 'f' ключ 'K' со значением ['K', 'e', 'k']

my_dict['moo']['f']['K'] = ['K', 'e', 'k']
print(my_dict['moo'])

# 10 Очистите словарь my_dict

my_dict.clear()
print(my_dict)