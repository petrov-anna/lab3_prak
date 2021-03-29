import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
print("~Соединение с сервером~")
sock.connect(('127.0.0.1', 9090))

while True:
    message = input("Введите сообщение => ")
    sock.send(message.encode())
    print("Отправили сообщение")
    data = sock.recv(1024)
    print(f'Получили сообщение => {data.decode()}')
    if message == 'exit':
        print(f'Мы были отключены от сервера')
        sock.close()
        break
