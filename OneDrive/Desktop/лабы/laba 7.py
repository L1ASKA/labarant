import tkinter as tk
from tkinter import scrolledtext
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
    best_team = None
    best_cost = float('inf')

    for team in itertools.combinations(candidates, len(candidate_costs)):
        cost = compute_team_cost(team)
        if cost < best_cost:
            best_cost = cost
            best_team = team

    return best_team, best_cost

def greedy_method(candidates, positions):
    selected = []
    total_cost = 0
    sorted_candidates = sorted(candidates, key=lambda x: candidate_costs[x - 1])

    for pos, count in positions.items():
        for _ in range(count):
            candidate = sorted_candidates.pop(0)
            selected.append(candidate)
            total_cost += candidate_costs[candidate - 1]

    return selected, total_cost

def run_analysis():
    output_text.delete(1.0, tk.END)

    start_time = time.time()
    best_team_functional, best_cost_functional = functional_method(candidates, positions)
    end_time = time.time()

    output_text.insert(tk.END, f"--- Функциональный метод ---\n")
    output_text.insert(tk.END, f"Оптимальная команда: {best_team_functional}\n")

    output_text.insert(tk.END, f"Минимальная стоимость команды: {best_cost_functional}\n")
    output_text.insert(tk.END, f"Время выполнения: {end_time - start_time:.4f} секунд.\n\n")

    start_time = time.time()
    greedy_team, greedy_cost = greedy_method(candidates, positions)
    end_time = time.time()

    output_text.insert(tk.END, f"--- Алгоритмический метод ---\n")
    output_text.insert(tk.END, f"Команда с минимальной стоимостью: {greedy_team}\n")
    output_text.insert(tk.END, f"Общая стоимость команды: {greedy_cost}\n")
    output_text.insert(tk.END, f"Время выполнения: {end_time - start_time:.4f} секунд.\n\n")

    output_text.insert(tk.END, f"--- Сравнение результатов ---\n")
    output_text.insert(tk.END, f"Минимальная стоимость команды: {best_cost_functional}\n")
    output_text.insert(tk.END, f"Общая стоимость команды: {greedy_cost}\n")

    if best_cost_functional < greedy_cost:
        output_text.insert(tk.END, "Функциональный метод дает лучший результат.\n")
    elif best_cost_functional > greedy_cost:
        output_text.insert(tk.END, "Алгоритмический метод дает лучший результат.\n")
    else:
        output_text.insert(tk.END, "Оба метода дают одинаковые результаты.\n")

root = tk.Tk()
root.title("Анализ команды")

btn_run = tk.Button(root, text="Запустить анализ", command=run_analysis)
btn_run.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack(padx=10, pady=10)

root.mainloop()
