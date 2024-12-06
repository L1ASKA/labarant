import time
import itertools
#IT-предприятие набирает сотрудников: 2 тимлида, 2 проджек-менеджера, 3 синьера, 3 мидла, 4 юниора.
# Сформировать все возможные варианты заполнения вакантных мест, если имеются 16 претендентов.
# Стоимости кандидатов
candidate_costs = [7, 6, 1, 7, 7, 7, 10, 1, 5, 6, 8, 2, 3, 6, 7, 7]
positions = {
    'team_lead': 2,
    'project_manager': 2,
    'senior': 3,
    'middle': 3,
    'junior': 4
}
candidates = list(range(1, 17))  # Кандидаты: 1 до 16


def compute_team_cost(team):
    """Вычисляет общую стоимость команды."""
    return sum(candidate_costs[candidate - 1] for candidate in team)


def functional_method(candidates, positions):
    """Ищет оптимальную команду с использованием ограничений."""
    best_team = None
    best_cost = float('inf')

    # Генерируем кандидатов для каждой позиции
    position_counts = []
    for pos, count in positions.items():
        position_counts.extend([pos] * count)

    # Генерируем все возможные комбинации кандидатов
    for team in itertools.combinations(candidates, len(candidate_costs)):
        cost = compute_team_cost(team)
        if cost < best_cost:
            best_cost = cost
            best_team = team

    return best_team, best_cost


def greedy_method(candidates, positions):
    """Алгоритмический метод для минимизации стоимости."""
    selected = []
    total_cost = 0

    # Сортируем кандидатов по стоимости
    sorted_candidates = sorted(candidates, key=lambda x: candidate_costs[x - 1])

    for pos, count in positions.items():
        for _ in range(count):
            candidate = sorted_candidates.pop(0)  # Берем кандидата с наименьшей стоимостью
            selected.append(candidate)
            total_cost += candidate_costs[candidate - 1]

    return selected, total_cost


# ===============================================================
# Функциональный метод
print("\n--- Функциональный метод ---")
start_time = time.time()
best_team_functional, best_cost_functional = functional_method(candidates, positions)
end_time = time.time()

print(f"Оптимальная команда: {best_team_functional}")
print(f"Минимальная стоимость команды (функциональный метод): {best_cost_functional}")
print(f"Время выполнения: {end_time - start_time:.4f} секунд.")


# ===============================================================
# Алгоритмический метод
print("\n--- Алгоритмический метод ---")
start_time = time.time()
greedy_team, greedy_cost = greedy_method(candidates, positions)
end_time = time.time()

print(f"Команда с минимальной стоимостью (алгоритмический метод): {greedy_team}")
print(f"Общая стоимость команды: {greedy_cost}")
print(f"Время выполнения: {end_time - start_time:.4f} секунд.")

# ===============================================================
# Сравнение результатов
print("\n--- Сравнение результатов ---")
print(f"Минимальная стоимость команды (функциональный метод): {best_cost_functional}")
print(f"Общая стоимость команды (алгоритмический метод): {greedy_cost}")

if best_cost_functional < greedy_cost:
    print("Функциональный метод дает лучший результат.")
elif best_cost_functional > greedy_cost:
    print("Алгоритмический метод дает лучший результат.")
else:
    print("Оба метода дают одинаковые результаты.")
