a = 0
b = 2
h = 0.5
K = 3.2
L = 1.6
x = [0]
y = [L]
# y = [2]

def r(arr):
    for i in range(len(arr)):
        arr[i] = round(arr[i], 3)

# def f(x, y):
#     return x**2 + y

def f(x, y):
    global K
    return x ** 2 + (K - 1) / 2 * y

print('%-10s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s' % ('n', 'X0', 'Y0', 'X1', 'Y1', 'X2', 'Y2', 'X3', 'Y3', 'X4', 'Y4'))


# Эйлер
t = 0
for i in range(int(abs(b - a) / h)):
    t += 1
    x.append(x[t - 1] + h)
    y.append(y[t - 1] + h * f(x[t - 1], y[t - 1]))
r(x)
r(y)
print('%-10s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s' % ('М.Э.', x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3], x[4], y[4]))

#Трапеци
x = [0]
y = [L]
t = 0
for i in range(int(abs(b - a) / h)):
    t += 1
    x.append(x[t - 1] + h)
    y.append(y[t - 1] + h / 2 * ((f(x[t - 1], y[t - 1]) + f(x[t], y[t - 1] + h * f(x[t - 1], y[t - 1])))))
r(x)
r(y)
print('%-10s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s' % ('М.трап.', x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3], x[4], y[4]))

# Рунге-Кутта
x = [0]
y = [L]
t = 0
for i in range(int(abs(b - a) / h)):
    k = [f(x[t], y[t])]
    t += 1
    x.append(x[t - 1] + h)
    for j in range(1, 3):
        k.append(f(x[t - 1] + h / 2, y[t - 1] + h * k[j - 1] / 2))
    k.append(f(x[t - 1] + h, y[t - 1] + h * k[2]))
    y.append(y[t - 1] + h / 6 * (k[0] + 2 * k[1] + 2 * k[2] + k[3]))
r(x)
r(y)
print('%-10s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s %-7s' % ('М.Р-К.', x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3], x[4], y[4]))

