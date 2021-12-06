class Data:

    def __init__(self, data):
        self.data = data
        self.data = str(input("Введите число месяц и год в формате чч:мм:гггг: "))


    @classmethod
    def number(cls, data):
        number = list(map(int, data.split(':')))
        return number[0], number[1], number[2]


    @staticmethod
    def validation(number):
        if 1 >= number[0] <= 31:
            if 1 >= number[1] <= 12:
                if 1900 < number[2] > 2021:
                    print("Данные введены корректно")
        else:
            print("Данные введены некорректно")
        return Data.validation(number)


a = Data
print(a)
print(Data.number())
print(Data.validation)