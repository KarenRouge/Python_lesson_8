class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'сумма двух комплексных чисел равна: ({self.a + other.a}, {self.b + other.b}).'

    def __mul__(self, other):
            return f'произведение двух комплексных чисел равна: ({self.a * other.a - (self.b * other.b)}, {self.b * other.a}).'




z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)

print(z_1 + z_2)
print(z_1 * z_2)