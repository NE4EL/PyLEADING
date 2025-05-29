# Строки

text = input("Enter your text: ")
for i, letter in enumerate(text):
    print(i, letter)

print(text.capitalize()) # Заглавная буква первая
print(text.find("f")) # Возвращает индекс

a = ["1", "2", "3"]
text = "; ".join(a)

print(text)

s = "one, two, three"
text = s.split(",")

print(text)

# Кортежи


