class OwnError(ValueError):
    def __init__(self, text):
        self.text = text


list = []
while True:
    inp_data = input(" Введите число. Для завершения введите 'stop': ")
    try:
        if int(inp_data) == int(inp_data):
            list.append(int(inp_data))
            print(list)
        elif inp_data == 'stop':
            print(f'Операция завершена. список чисел: {list}.')
            break
        elif int(inp_data) != int(inp_data) or inp_data != 'stop':
            raise OwnError("Необходимо вводить только числа!")

    except OwnError as err:
        print(err)
