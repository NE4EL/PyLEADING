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

while string := input():
    if string[-3:] != '@@@':
        if string[0:2] == '##':
            string = string[2:]
        print(string)