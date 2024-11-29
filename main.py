# Відкриваємо файл input_text.txt для зчитування
with open("input_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Використання функції .lower(), щоб зробити всі літери в рядку малими.
lower_text = text.lower()
print("Текст з малими літерами:")
print(lower_text)
print("\n")

# Використання функції .replace(), щоб замінити слово "рефаунд" на "REFUND".
modified_text = lower_text.replace("рефаунд", "REFUND")
print("Текст після заміни 'рефаунд' на 'REFUND':")
print(modified_text)
print("\n")

# Використання функцї .split(), щоб розділити текст на окремі слова.
words = modified_text.split()
print("Список слів з тексту:")
print(words)
print("\n")

# Підрахунок кількрсты слів у тексті
word_count = len(words)
print("Кількість слів у тексті:", word_count)