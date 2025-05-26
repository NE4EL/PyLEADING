# СПИСОК

empty = []  # пустой список
numbers = [1, 2, 3, 4]
words = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(numbers[0])
print(words[0])

print(words[1:3])  # ['banana', 'cherry']
print(words[:2])   # ['apple', 'banana']
print(words[::2])  # ['apple', 'cherry'] — каждый второй элемент

# ОСНОВНЫЕ МЕТОДЫ

my_list = [3, 1, 4]

my_list.append(5)        # Добавить элемент в конец
my_list.remove(1)        # Удалить первый найденный элемент
my_list.pop()            # Удалить и вернуть последний элемент
my_list.sort()           # Сортировать по возрастанию
my_list.reverse()        # Развернуть список
print(len(my_list))      # Длина списка

# ПЕРЕБОР СПИСКА

for item in my_list:
    print(item)