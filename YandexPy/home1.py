# A Задание
# n = int(input())
# arr = []
#
# for i in range(n):
#     string = input()
#     if string[0] in "абв":
#         arr.append(string)
#
# if len(arr) == n:
#     print("YES")
# else:
#     print("NO")

# B Задание
# text = input()
# for i in text:
#     print(i)

# C Задание
# l = int(input())
# val = int(input())
# arr = []
#
# for i in range(val):
#     string = input()
#     arr.append(string)
#
#
# for i in arr:
#     if len(i) > l:
#         print(i[:l] + "...")
#     else:
#         print(i)

# D Задание
# while string := input():
#     if string[-3:] != '@@@':
#         if string[0:2] == '##':
#             string = string[2:]
#         print(string)

# E Задание
# text = input()
#
# if text == text[::-1]:
#     print("YES")
# else:
#     print("NO")

# F Задание
# num = int(input())
# mas = []
#
# for i in range(num):
#     mas.append(input())
# text = " ".join(mas)
# print(text.count("зайка"))

# G Задание
# text = input()
# text = text.split()
# num = 0
# for i in text:
#     num += int(i)
# print(num)

# H Задание
# mas = []
#
# for i in range(int(input())):
#     text = input()
#     mas.append(text)
#
# for text in mas:
#     val = text.find("зайка")
#     if val != -1:
#         print(val + 1)
#     else:
#         print("Заек нет =(")

# I Задание
while string := input(): # моржовой оператор, присваиваются значения прям в конструкции
    if not (pos := string.find('#')) + 1:
        print(string)
    elif string[:pos]:
        print(string[:pos])