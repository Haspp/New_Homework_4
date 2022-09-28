# Вычислить число c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141

def prec():
    precision = input("Введите точность: ")
    if '.' in precision:
        n = len(str(precision).split('.')[1])
        return int(n)
    else:
        return


def toFixed(f: float, n=0):
    a, b = str(f).split('.' or ',')
    return '{}.{}{}'.format(a, b[:n], '0' * (n - len(b)))


f = prec()
number = input("Введите число: ")
print(toFixed(number, f))
