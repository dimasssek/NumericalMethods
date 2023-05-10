from math import e

## №1
alpha1 = 1
beta1 = 2*e**8-1/e**4
a_sb, b_sb = 0, 4
def f(x):
    return 0
def p(x):
    return -1
def q(x):
    return -2
def res(x):
    return e**(2*x)+1/e**x


# # №2
# alpha1 = 1
# beta1 = 2*8+1
# a_sb, b_sb = 0, 8
# def f(x):
#     return 0
# def p(x):
#     return -2/x
# def q(x):
#     return 2/x**2
# def res(x):
#     return x**2+x


# ## №3
# alpha1 = 3/8
# beta1 = 3*9**2/8+1-1/9**2
# a_sb, b_sb = 1, 9
# def f(x):
#     return x
# def p(x):
#     return 1/x
# def q(x):
#     return -1/x**2
# def res(x):
#     return x**3/8+x+1/x


####
h = 0.001
m = int((b_sb-a_sb)/h)
t = [a_sb+i*h for i in range(m+1)]
n = len(t)
a, b, c, d = [0]*n, [0]*n, [0]*n, [0]*n
y = [0]*n

a[0] = 0
b[0] = -1
c[0] = 1
d[0] = alpha1*h
a[-1] = -1
b[-1] = 1
c[-1] = 0
d[-1] = beta1*h
for i in range(1, n-1):
    a[i] = 1-h/2*p(t[i])
    b[i] = h**2*q(t[i])-2
    c[i] = 1+h/2*p(t[i])
    d[i] = h**2*f(t[i])
al, be = [0]*n, [0]*n
for i in range(n):
    al[i] = -c[i]/(b[i]+a[i]*al[i-1])
    be[i] = (d[i]-a[i]*be[i-1])/(b[i]+a[i]*al[i-1])
y[-1] = be[-1]
for i in range(n-2, -1, -1):
    y[i] = al[i]*y[i+1]+be[i]


ymax, rmax = 0, 0
R = [res(t[i]) for i in range(len(t))]
for i in range(len(y)):
    if len(str(y[i])) > ymax:     ymax = len(str(y[i]))
    if len(str(R[i])) > ymax:     rmax = len(str(R[i]))
with open('res.txt', 'w') as file:
    for i in range(len(t)):
        t[i] = round(t[i], len(str(h))-2)
        tstr = str(t[i])+'0'*(len(str(h))-len(str(t[i])))
        ind = str(y[i]).find('e')
        ystr = str(y[i])[:ind] + '0'*(ymax-len(str(y[i]))) + str(y[i])[ind:] if ind != -1 else str(y[i]) + '0'*(ymax-len(str(y[i])))
        ind = str(R[i]).find('e')
        rstr = str(R[i])[:ind] + '0'*(rmax-len(str(R[i]))) + str(R[i])[ind:] if ind != -1 else str(R[i]) + '0'*(rmax-len(str(R[i])))
        print (f'x = {tstr}, y = {ystr},  y(точное) = {rstr}')      # (f'x = {t[i]}, y = {y[i]},  y(точное) = {R[i]}')
        tstr, ystr, rstr = str(t[i]).replace('.', ','), str(y[i]).replace('.', ','), str(R[i]).replace('.', ',')
        file.write(f'{tstr}; {ystr}; {rstr} \n')
print(f'{h = }')

