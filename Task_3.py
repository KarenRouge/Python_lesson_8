class OwnError(Exception):
    def __init__(self):
        self.list = []

    def func(self):

        while True:
            try:
                inp_data = int(input(" Введите число. Для завершения введите 'stop': "))
                self.list.append(inp_data)
                return list
            except:
                print("недопустимое значение")

a = OwnError()
print(a.func())



