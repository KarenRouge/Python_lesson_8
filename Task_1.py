class Data:

    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def number(cls, data):
        number = list(map(int, data.split('-')))
        return number[0], number[1], number[2]

    @staticmethod
    def validation(data):
        number = list(map(int, data.split('-')))
        day = number[0]
        month = number[1]
        year = number[2]
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1900 < year < 2022:
                    print("Данные введены корректно")
        else:
            return print("Данные введены некорректно")


print(Data.number('12-12-2012'))
print(Data.validation('12-12-2012'))
