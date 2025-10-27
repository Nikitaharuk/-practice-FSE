import random
import time


n = int(input("Введите количество примеров: "))
correct_answers = 0
total_time = 0
question_times = []
for i in range(1, n + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_result = a * b
    print(f"Вопрос {i}/{n}")
    start_time = time.time()
    user_input = input(f"{a} × {b} = ")
    end_time = time.time()
    question_time = end_time - start_time
    user_answer = int(user_input)
    if user_answer == correct_result:
       print(f"Верно! (Время: {question_time:.1f} сек)")
       correct_answers += 1
    else:
       print(f"Неверно! Правильно: {correct_result} (Время: {question_time:.1f} сек)")
       total_time += question_time
       question_times.append(question_time)
print("СТАТИСТИКА:\n")
print(f"Общее время: {total_time:.1f} секунд")
if n > 0:
  average_time = total_time / n
  print(f"Среднее время на вопрос: {average_time:.1f} сек")
else:
  print("Среднее время на вопрос: 0.0 сек")
print(f"Правильных ответов: {correct_answers}/{n}")
if n > 0:
  percentage = (correct_answers / n) * 100
  print(f"Процент правильных: {percentage:.1f}%")
else:
  print("Процент правильных: 0.0%")