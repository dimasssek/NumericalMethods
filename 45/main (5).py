from math import e, sin, cos, pi


# # ex1
# l1, l2 = 0, 1
# def fi0(t):
#     return t
# def fi1(t):
#     return t+0.5
# def psi(x):
#     return x


# # ex2
# l1, l2 = 0, 2*pi
# def fi0(t):
#     return cos(t) - 1
# def fi1(t):
#     return 1
# def psi(x):
#     return sin(x)
#
#
# ## ex3
l1, l2 = 0, pi
def fi0(t):
    return t**2
def fi1(t):
    return e**(t/3)
def psi(x):
    return x**2


alpha1 = 2
m1, m2 = 100, 200
h = (l2 - l1) / m1
tay = (l2 * 2 - l1) / m2
t = [i * tay for i in range(int(l1 / tay), int(l1 / tay) + m2 + 1)]
x = [i * h for i in range(int(l1 / h), int(l1 / h) + m1 + 1)]
n = len(t)
m = len(x)
a, b, c, d = [0] * m, [0] * m, [0] * m, [0] * m
u = [[0] * n for i in range(m)]

for j in range(len(x)): u[j][0] = psi(x[j])
for k in range(1, n):
    a[0] = 0
    b[0] = 2 * alpha1 / h ** 2 + 1 / tay
    c[0] = -(alpha1/h**2)
    d[0] = 1 / tay * u[0][k - 1] + fi0(t[k]) * alpha1 / h ** 2
    a[-1] = -1
    b[-1] = 1
    c[-1] = 0
    d[-1] = h*fi1(t[k])
    for i in range(1, m - 1):
        a[i] = -(alpha1/h**2)
        b[i] = 2 * alpha1 / h ** 2 + 1 / tay
        c[i] = -(alpha1/h**2)
        d[i] = 1 / tay * u[i][k - 1]
    al, be = [0] * m, [0] * m
    for i in range(len(al)):
        al[i] = -c[i]/(b[i]+a[i]*al[i-1])
        be[i] = (d[i]-a[i]*be[i-1])/(b[i]+a[i]*al[i-1])
    u[-1][k] = be[-1]
    for i in range(m - 2, -1, -1):
        u[i][k] = al[i]*u[i+1][k]+be[i]

with open('a.txt', 'w') as f:
    sres = [''] * len(u)
    tres, xres = [0] * len(t), [0] * len(x)
    s = 'x; '
    for i in range(len(t)):
        s = s + str(t[i]).replace('.', ',') + ';'
    f.write(s + '\n')
    for i in range(len(u)):
        tres[i] = str(x[i]).replace('.', ',')
        for j in range(len(u[0])):
            sres[i] = sres[i] + str(u[i][j]).replace('.', ',') + ';'
        f.write(tres[i] + ';' + sres[i] + '\n')