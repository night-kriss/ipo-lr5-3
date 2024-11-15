#Напишите программу, которая считывает текст из файла (text.txt) и выводит количество слов в этом файле.
# Открытие файла в режиме чтения
with open("text.txt", "r", encoding="utf-8") as file:
    # Чтение содержимого файла
    text = file.read()

# Вывод содержимого файла на экран
print(text)
# Подсчёт количества слов
word_count = len(text.split())

# Вывод количества слов на экран
print("Количество слов в файле:", word_count)
