# Завдання 1

import numpy as np

array = np.array([12, -5, 7, 9, -3, 15])

new_array = np.append(array, 10)

print(new_array)

# Завдання 2

import numpy as np

array = np.array([[5, 2, 8],
                  [1, 7, 4],
                  [3, 6, 9]])

new_array = np.delete(array, 1, axis=0)
print(new_array)

# Завдання 3
import numpy as np

conversions = np.array([50, 65, 80, 45, 70, 90, 55, 85, 60, 75])
print(conversions)

median_arr = np.median(conversions)
variance_arr = np.var(conversions)
std_deviation = np.std(conversions)

print('Медіана: ', median_arr)
print('Дисперсія: ', variance_arr)
print('Стандартне відхилення: ', std_deviation)

uniform_arr = np.random.uniform(1, 101, 10)
integers = np.random.randint(1, 101, 10)
float_random = np.random.rand(10)
normal_arr=np.random.normal(70, 20, 10)

print('Рівномірний масив випадкових чисел: ', uniform_arr)
print('випадковий масив цілих чисел: ', integers)
print('випадковий масив дійсних чисел: ', float_random)
print('нормальний розподіл випадкових чисел: ', normal_arr)

combined = np.concatenate([conversions, uniform_arr, integers, float_random, normal_arr])
print('Об\'єднаний масив: \n', combined)

mean_value = np.mean(combined)
print('Середнє значення: ', mean_value)

is_more_than_2000 = mean_value > 2000
print('Чи є середнє більше за 2000: ', is_more_than_2000)
