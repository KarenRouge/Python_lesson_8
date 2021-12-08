class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.a = self.a.split('+')
        self.a[1] = self.a[1].replace('j', '')
        self.b = self.b.split('+')
        self.b[1] = self.b[1].replace('j', '')

    def __add__(self):

        return f'сумма двух комплексных чисел равна: ({int(self.a[0]) + int(self.b[0])}+{int(self.a[1]) + int(self.b[1])}j).'

    def __mul__(self):

        return f'произведение двух комплексных чисел равно: ' \
               f'({int(self.a[0]) * int(self.b[0]) - int(self.a[1]) * int(self.b[1])}' \
        f'+{int(self.b[0]) * int(self.a[1]) + int(self.a[0]) * int(self.b[1])}j)'


z_1 = ComplexNumber('1+2j', '1+3j')
print(z_1.__add__())
print(z_1.__mul__())

