import numpy as np

# #1
temps = np.array([15.2, 16.8, 14.5, 17.0, 16.1])

print(f"cумму {np.sum(temps)}, среднее  {np.mean(temps)}, минимум  {np.min(temps)} и максимум массива  {np.max(temps)}")

#2

h1 = np.array([45, 50, 47])
h2 = np.array([48, 46, 52])

print(h1+h2)
print(h1*h2)
print(np.dot(h1, h2))

#3
X = np.array([
[20.1, 20.3, 19.8],
[21.0, 20.7, 20.2],
[19.5, 19.8, 19.3],
[20.8, 21.1, 20.6]
])

print(f"Среднее по столбцам {np.mean(X, axis=0)}")
print(f"Сумму по строкам {np.sum(X, axis=1)}")
print(f"Дисперсию по столбцам с ddof=1 {np.var(X, axis=0, ddof=1)}")
print (f"индекс столбца (сенсора) с минимальной дисперсией {np.var(X, axis=0, ddof=1).argmin()}")


