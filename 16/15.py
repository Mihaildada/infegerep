"""
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное
число, задан следующими соотношениями:

F(0) = 0
F(n) = F(n/2)     если n > 0 и при этом n чётно
F(n) = 1 + F(n−1) если n нечётно

Сколько существует таких чисел n, что 1 <= n <= 500 и F(n) = 8?
"""
