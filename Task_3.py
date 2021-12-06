class OwnError(ValueError):
    def __init__(self, text):
        self.text = text


list = []
while True:
    inp_data = input(" Введите число. Для завершения введите 'stop': ")
    try:
        if inp_data == 'stop':
            print(f'Операция завершена. список чисел: {list}.')
            break
        elif inp_data.isdigit() is False:
            raise OwnError("Необходимо вводить только числа!")
        list.append(inp_data)
        print(list)
    except OwnError as err:
        print(err)
