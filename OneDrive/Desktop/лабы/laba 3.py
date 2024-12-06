# Словарь для преобразования цифр в текст
#Вещественные числа, заключенные в кавычки (все виды). Кавычки не выводятся. Целая часть числа
#выводится словами.
digit_to_word = {
    "0": "Ноль",
    "1": "Один",
    "2": "Два",
    "3": "Три",
    "4": "Четыре",
    "5": "Пять",
    "6": "Шесть",
    "7": "Семь",
    "8": "Восемь",
    "9": "Девять",
}


def number_to_words(number):
    """Преобразует целое число в слова."""
    words = []
    for digit in str(number):
        words.append(digit_to_word[digit])
    return ' '.join(words)


def is_valid_float(value):
    """Проверяет, является ли строка корректным вещественным числом."""
    try:
        # Check if the value can be converted to float
        float_value = float(value)
        # Убедимся, что есть только одна десятичная точка
        return value.count('.') <= 1 and ('.' in value or 'e' in value or 'E' in value)
    except ValueError:
        return False


def process_file(filename):
    with open(filename, 'r') as file:
        char = file.read()
        numbers = char.split()  # Разделяем входные данные по пробелам

        for number in numbers:
            # Проверка на наличие кавычек
            if (number.startswith('"') and number.endswith('"')) or (number.startswith("'") and number.endswith("'")):
                value = number[1:-1]  # Удаляем кавычки

                if is_valid_float(value):
                    float_value = float(value)  # Преобразуем в вещественное число
                    int_part = int(float_value)  # Целая часть
                    des_part = str(abs(float_value - int_part)).split(".")[1]  # Десятичная часть

                    # Преобразуем целую часть в слова
                    int_part_words = number_to_words(abs(int_part))  # Используем абсолютное значение для слов
                    sign_prefix = "Минус " if int_part < 0 else ""

                    # Выводим результат
                    print(f"Это вещественное число: {sign_prefix}{int_part_words}.{des_part}")
                else:
                    print("Это не вещественное число:", value)
            else:
                print("Значение не находится в кавычках:", number)


# Вызов функции с названием файла
process_file('laba 3.txt')
