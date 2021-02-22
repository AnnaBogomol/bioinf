seq = input()
seq = seq + "$"  # стартоввый маркер $

table = [seq[i:] + seq[:i] for i in range(len(seq))]  # таблица циклических сдвигов последовательности

table = sorted(table)  # лексикографическая сортировка

last_column = [string[-1:] for string in table]  # вывод последнего столбца таблицы
bwt = ''.join(last_column)

S = input().split()  # суффиксный массив
list = ''  # пустой список

for i in S:
    list += seq[int(i) - 1]
C = [0] * 5

for i in list:
    if i == "$":
        C[1] += 1
        C[2] += 1
        C[3] += 1
        C[4] += 1
    elif i == "A":
        C[2] += 1
        C[3] += 1
        C[4] += 1
    elif i == "C":
        C[3] += 1
        C[4] += 1
    elif i == "G":
        C[4] += 1

print(bwt)  # Результат преобразования Барроуза-Уилера
print("C($) = 0 ,", "C(A) = ", C[1], ",", "C(C) = ", C[2], ",", "C(G) = ", C[3], ",", "C(T) = ", C[4], ".")
