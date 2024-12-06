import re
#Вещественные числа, заключенные в кавычки (все виды). Кавычки не выводятся. Целая часть числа выводится словами.

# Функция для преобразования целого числа в слова
def number_to_words(n):
    if n < 0:
        return 'минус ' + number_to_words(-n)

    units = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
             'десять', 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
             'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят',
            'восемьдесят', 'девяносто']
    hundreds = ['ноль', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот',
                'семьсот', 'восемьсот', 'девятьсот']

    if 0 <= n < 20:
        return units[n]
    elif 20 <= n < 100:
        return tens[n // 10 - 1] + ('' if n % 10 == 0 else ' ' + units[n % 10])
    elif 100 <= n < 1000:
        return hundreds[n // 100] + ('' if n % 100 == 0 else ' ' + number_to_words(n % 100))
    else:
        return str(n)  # Для чисел более 999 просто возвращаем строку


# Функция для извлечения вещественных чисел и целых чисел из строки
def extract_numbers_and_convert(text):
    # Регулярное выражение для поиска чисел
    pattern = r'[-+]?\d*\.\d+|[-+]?\d+'
    matches = re.findall(pattern, text)

    result = []
    for match in matches:
        number = float(match)  # Полное число с плавающей запятой
        whole_part = int(number)  # Целая часть
        fractional_part = number - whole_part  # Дробная часть (как десятичное число)

        # Преобразуют целую часть в слова
        words = number_to_words(whole_part)

        # Получаем дробную часть как строку
        fractional_string = f"{abs(int(fractional_part * 10 ** len(str(fractional_part).split('.')[1])))}" if fractional_part > 0 else '0'

        # Сохраняем как текст, так и числовое значение
        result.append((words, whole_part, fractional_string, number))

    return result


# Чтение строк из файла
with open('laba 4.txt', 'r', encoding='utf-8') as file:
    input_string = file.read()

# Обработка строки
output_words = extract_numbers_and_convert(input_string)

# Вывод результата
for words, whole_number, fractional_number, original_number in output_words:
    print(f"{words} ({whole_number}.{fractional_number}) = {original_number}")
