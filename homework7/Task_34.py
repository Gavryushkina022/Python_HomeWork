vowels = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
phrase = input('Введите фразу: ').split(" ")

# Функция подсчёта кол-ва гласных в слове
def count_vowels(word):
    value = 0
    for i in range(len(word)):
        if word[i] in vowels:
            value = value + 1
    return value

def check(phrase):
    # Определяем кол-во гласных в первом слове (выступает как ориентир для сравнения для последующих слов)
    quantity_vowels_in_first_word = count_vowels(list(phrase[0]))
    for i in range(len(phrase) - 1):
        var = count_vowels(list(phrase[i + 1])) == quantity_vowels_in_first_word
        if not var:
            return 'Пам парам'
    return 'Парам пам-пам'


print(check(phrase))



