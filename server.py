import errno
import socket


def clean():
    file = open("logFile.txt", 'w+')
    file.seek(0)
    file.close()


def writeData(data):
    with open("logFile.txt", "a") as file:
        file.write(f'{data}\n')


def freePort(sock, s_port):
    try:
        sock.bind(('', s_port))
        print(f'Порт: {s_port}')
        return True
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            s_port += 1
            return freePort(sock, s_port)


clean()
sock = socket.socket()
s_port = 9090
# while True:
#     msg = ''
#     running = True
#     while running:
#         print("~Запуск сервера~")
#         writeData("~Запуск сервера~")
#         sock = socket.socket()
#         sock.bind(('', 9090))
#         print("~Начало прослушивания порта~")
#         writeData("~Начало прослушивания порта~")
#         sock.listen(0)
#         print("~Ожидаем подключение клиента~")
#         writeData("~Ожидаем подключение клиента~")
#         conn, addr = sock.accept()
#         print(f"Клиент {addr} был подключен")
#         writeData(f"Клиент {addr} был подключен")
#         running = False
#     running = True
#     # conn.send(data)
#     while running:
#         data = conn.recv(1024)
#         if not data:
#             print(f"Клиент {addr} был отключен")
#             writeData(f"Клиент {addr} был отключен")
#             break
#         if data.decode() == 'exit':
#             print("!!!Сервер остановили!!!")
#             writeData("!!!Сервер остановили!!!")
#             running = False
#             break
#         print(f'Получили сообщение: {data.decode()}')
#         writeData(f'Получили сообщение: {data.decode()}')
#         msg += data.decode()
#         conn.send(data)
#         print(f'Отправленное сообщение: {data.decode()}')
#         writeData(f'Отправленное сообщение: {data.decode()}')


if freePort(sock, s_port):
    print("~Начало прослушивания порта~")
    writeData("~Начало прослушивания порта~")
    sock.listen(1)

    while True:
        file = open('logFile.txt', 'a')
        conn, addr = sock.accept()
        running = True
        print(f'Клиент {addr} был подключен')
        writeData(f'Клиент {addr} был подключен\n')
        while running:
            data = conn.recv(1024)
            if not data:
                print(f'Клиент {addr} был отключен')
                writeData(f'Клиент {addr} был отключен\n')
                break
            if data.decode() == 'exit':
                print('!!!Сервер остановили!!!')
                writeData('!!!Сервер остановили!!!\n')
                running = False
                break
            print(f'Получили сообщение:{data.decode()}')
            print(f'Отправленное сообщение: {data.decode()}')
            writeData(f'Получили сообщение:{data.decode()}')
            writeData(f'Отправленное сообщение: {data.decode()}')
            conn.send(data)