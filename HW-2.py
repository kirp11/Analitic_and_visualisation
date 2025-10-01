

import numpy as np
import matplotlib.pyplot as plt

# alcohol - объем спирта;
# volatile acidity - летучая кислота;
# sulphates - уровень сульфатов;
# pH - уровень щелочи;
# quality - качество вина.


# alcohol,     volatile acidity,    sulphates,   pH,    quality
dataset = np.loadtxt(
"wine_quality.csv",
delimiter=",",
skiprows=1,
)
# mean, median, var, min, max
print(f"среднее по столбцам {np.mean(dataset,axis=0)}, \nмедиана по столбцам {np.median(dataset,axis=0)}, \nдисперсия по столбцам {np.var(dataset,axis=0, ddof=1)}\n"
      f"минимум по столбцам {np.min(dataset,axis=0)},\nмаксимум по столбцам {np.max(dataset,axis=0)}")

print(dataset[:,-1].max())

# Найдите max(quality) . Для всех записей (строчек таблицы) с этим quality вычислите средний pH.
mask = dataset[:,-1] == dataset[:,-1].max()
print(f"средний pH с максимальным quality   {np.mean(dataset[mask], axis=0)[-2]}")


# 3. Проведите операцию "нормализации" для колонки quality :
# Определите, чему равны min(quality) и max(quality) ;
# Вычтите min(quality) из колонки quality ;
# Поделите полученные значения на max(quality) - min(quality) . Таким образом, значения в колонке перейдут в диапазон [0; 1] .

min_qual = np.min(dataset,axis=0)[-1]
max_qual = np.max(dataset,axis=0)[-1]
dataset[:,-1] = dataset[:,-1] - min_qual
dataset[:,-1] = dataset[:,-1] /(max_qual - min_qual)
print(dataset)


# ВИЗУАЛИЗАЦИЯ
# 1. Постройте столбчатую диаграмму ( plt.bar ) или круговую диаграмму ( plt.pie ) для quality . Необходимо посчитать, сколько различных
# уровней качества есть, после чего построить соответсвующую диаграмму распределения (функция np.unique с параметром return_counts в
# помощь).
unique_values, counts = np.unique(dataset[:,-1], return_counts=True)
print(unique_values, counts)
# plt.pie(counts, labels=unique_values)
#
# plt.show()
#
# plt.bar(unique_values, counts)
# plt.show()




# 2. Постройте точечный график ( plt.scatter ) для x = volatile acidity и y = alcohol .

# plt.scatter(dataset[:,1], dataset[:,0], color = 'red')
# plt.show()
# Поделите исходный датасет на 2 таблицы (матрицы): с низким уровнем quality (т.е. min(quality) ) и высокими (т.е. max(quality) ).

avg_quality = np.mean(dataset, axis=0)[-1]
mask_high_qual = dataset[:,-1] > avg_quality
mask_low_qual = dataset[:,-1] <= avg_quality

plt.scatter(dataset[mask_high_qual][:,1], dataset[mask_high_qual][:,0], color = 'green')

plt.scatter(dataset[mask_low_qual][:,1], dataset[mask_low_qual][:,0], color = 'orange')
plt.xlabel("летучая кислота")
plt.ylabel("объем спирта")
plt.legend("низкое качество")
plt.show()

# Вызовите функцию plt.scatter 2 раза: с точками, у которых низкий уровень quality (окрасьте их зеленым цветом) и с точками, у которых он
# высокий (окрасьте их оранжевым цветом).
# Есть ли какая-то зависимость между качеством вина и объемом спирта и летучей кислотой? Если есть, то какая?
# Зависимость качества вина от содержания летучей кислоты - в вине низкго качества характерно повышенное содержание летучей кислоты
# Зависимость от алкоголя следующая - для вина высокого качества характерно повышенное содержание спирта

# Таким образом, при выборе вина, если выбирать с низким содержанием летучейц кислоты и высоким содержанием спирта - большая вероятность купить вино высокого качества.

