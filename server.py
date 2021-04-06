import socket


def clean():
    file = open("logFile.txt", 'w+')
    file.seek(0)
    file.close()


def writeData(data):
    with open("logFile.txt", "a") as file:
        file.write(f'{data}\n')


clean()

while True:
    msg = ''
    running = True
    while running:
        print("~Запуск сервера~")
        writeData("~Запуск сервера~")
        sock = socket.socket()
        sock.bind(('', 9090))
        print("~Начало прослушивания порта~")
        writeData("~Начало прослушивания порта~")
        sock.listen(0)
        print("~Ожидаем подключение клиента~")
        writeData("~Ожидаем подключение клиента~")
        conn, addr = sock.accept()
        print(f"Клиент {addr} был подключен")
        writeData(f"Клиент {addr} был подключен")
        running = False
    running = True
    # conn.send(data)
    while running:
        data = conn.recv(1024)
        if not data:
            print(f"Клиент {addr} был отключен")
            writeData(f"Клиент {addr} был отключен")
            break
        if data.decode() == 'exit':
            print("!!!Сервер остановили!!!")
            writeData("!!!Сервер остановили!!!")
            running = False
            break
        print(f'Получили сообщение: {data.decode()}')
        writeData(f'Получили сообщение: {data.decode()}')
        msg += data.decode()
        conn.send(data)
        print(f'Отправленное сообщение: {data.decode()}')
        writeData(f'Отправленное сообщение: {data.decode()}')

