import math

from openpyxl import Workbook

def u(t):
    return t + (t / (t + 1))

def u1(t):
    return (t * t) / (1 + t)

def u2(t):
    return t / (2 - math.log(t))

def f(t, u_val):
    return (1 / t) * ((2 * t + 1) * u_val - u_val * u_val - t * t)

def average(array_list):
    return sum(array_list) / len(array_list)

def frange(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step

abscissa, ordinates, solution, solution1, solution2 = [], [], [], [], []

with open("input2.txt") as file:
    t0, b, u0, h = map(float, file.readline().split())

a = t0
t_prev = t0
y_prev = u0

k1 = h * f(t_prev, y_prev)
k2 = h * f(t_prev + h, y_prev + h * k1)
y_curr = y_prev + 0.5 * (k1 + k2)
t_curr = t_prev + h

for dot in frange(a,b,h):
    abscissa.append(dot)
    solution.append(u(dot))
    solution1.append(u1(dot))
    solution2.append(u2(dot))

ordinates.append(y_prev)
ordinates.append(y_curr)

for i in range(2, len(abscissa)):
    y_curr = y_curr + h * (1.5 * f(abscissa[i-1], ordinates[i-1]) - 0.5 * f(abscissa[i-2], ordinates[i-2]))
    ordinates.append(y_curr)

delta = []
for i in range(len(abscissa)):
    delta.append(abs(ordinates[i] - solution[i]))

print("delta:")
for i in range(len(delta)):
    print(delta[i])

print("abscissa:")
for i in range(len(abscissa)):
    print(abscissa[i])

print()

print("ordinates:")
for i in range(len(ordinates)):
    print(ordinates[i])

# -----------------------------------------------------------------------
t_prev = t0
y_prev = u0
h = 2 * h
k1 = h * f(t_prev, y_prev)
k2 = h * f(t_prev + h, y_prev + h * k1)
y_curr = y_prev + 0.5 * (k1 + k2)
t_curr = t_prev + h

abscissa2, ordinates2, solution2, solution1_2, solution2_2, solution_2_new = [], [], [], [], [], []

for dot in frange(a,b,h):
    abscissa2.append(dot)
    solution2.append(u(dot))
    solution1_2.append(u1(dot))
    solution2_2.append(u2(dot))

for i in range(len(abscissa2)):
    solution_2_new.append(u(abscissa2[i]))

ordinates2.append(y_prev)
ordinates2.append(y_curr)

for i in range(2, len(abscissa)):
    y_curr = y_curr + h * (1.5 * f(abscissa2[i-1], ordinates2[i-1]) - 0.5 * f(abscissa2[i-2], ordinates2[i-2]))
    ordinates2.append(y_curr)

delta2 = []
for i in range(len(abscissa2)):
    if i % 2 == 0:
        delta2.append(abs(ordinates2[i] - solution_2_new[i]))

workbook = Workbook()
sheet1 = workbook.active
sheet1.title = "Пример 1"

row = sheet1[1]
row[0].value = "X"
row[1].value = "Y"
row[2].value = "Точное"
row[3].value = "delta"
row[5].value = "X"
row[6].value = "Y"
row[7].value = "Точное"
row[8].value = "delta"

for i in range(1, len(abscissa) + 1):
    row = sheet1[i + 1]
    row[0].value = abscissa[i - 1]
    row[1].value = ordinates[i - 1]
    row[2].value = solution[i - 1]
    row[3].value = abs(ordinates[i - 1] - solution[i - 1])
    if i <= len(abscissa) // 2 + 1:
        row[5].value = abscissa2[i - 1]
        row[6].value = ordinates2[i - 1]
        row[7].value = solution_2_new[i - 1]
        row[8].value = abs(ordinates2[i - 1] - solution_2_new[i - 1])

    if i == 54:
        row[15].value = f"max delta (при h = {h / 2})"
        row[18].value = f"max delta (при h = {h})"
        row[21].value = "Отношение погрешностей"
    if i == 55:
        row[16].value = max(delta)
        row[19].value = max(delta2)
        row[22].value = max(delta2) / max(delta)
    if i == 57:
        row[15].value = f"средн. delta (при h = {h / 2})"
        row[18].value = f"средн. delta (при h = {h})"
        row[21].value = "Отношение погрешностей"
    if i == 58:
        row[16].value = mean(delta)
        row[19].value = mean(delta2)
        row[22].value = mean(delta2) / mean(delta)

with open("Adams8.xlsx", "wb") as fos:
    workbook.save(fos)