import math
import time
#4.	F(x<2) = 3; F(n) = (-1)n*(F(n-1)/n! + F(n-5) /(2n)!)

# Рекурсивная функция
def F_recursive(n):
    if n < 2:
        return 3
    else:
        recursive_part = F_recursive(n - 1) / math.factorial(n)
        second_part = F_recursive(n - 5) / math.factorial(2 * n) if n >= 5 else 0
        return (-1) ** n * (recursive_part + second_part)


# Итеративная функция
def F_iterative(n):
    if n < 2:
        return 3

    f_values = [0] * (n + 1)
    f_values[0] = f_values[1] = 3

    for i in range(2, n + 1):
        term1 = f_values[i - 1] / math.factorial(i)
        term2 = f_values[i - 5] / math.factorial(2 * i) if i >= 5 else 0
        f_values[i] = (-1) ** i * (term1 + term2)

    return f_values[n]


# Функция для измерения времени и возврата результата
def measure_function_time(func, n):
    start_time = time.time()
    result = func(n)
    elapsed_time = time.time() - start_time
    return elapsed_time, result


# Запустим тестирование
results = []
n_values = range(1, 26)  # выбираем n от 1 до 25

# Заголовки таблицы
print(
    f"{'n':<5} {'Recursive Time (s)':<20} {'Iterative Time (s)':<20} {'Recursive Result':<20} {'Iterative Result':<20}")

for n in n_values:
    # Измеряем время выполнения рекурсивной функции
    recursive_time, recursive_result = measure_function_time(F_recursive, n)

    # Измеряем время выполнения итеративной функции
    iterative_time, iterative_result = measure_function_time(F_iterative, n)

    # Записываем результаты
    results.append((n, recursive_time, iterative_time, recursive_result, iterative_result))

    # Выводим результаты
    print(f"{n:<5} {recursive_time:<20.6f} {iterative_time:<20.6f} {recursive_result:<20.6f} {iterative_result:<20.6f}")

# Определяем границы применимости
print("\nГраницы применимости:")
print("Рекурсивный подход: для n < 20 (из-за глубокой рекурсии и использования памяти).")
print("Итеративный подход: для n больше 25 (предполагается, что он более эффективен по времени).")
