import socket
from time import sleep


def portVer(port):
    try:
        return True if 1024 <= int(port) <= 65535 else False
    except ValueError:
        return False


def ipVer(ip):
    try:
        sum = 0
        if ip == 'localhost':
            return True
        else:
            parts = ip.split(".")
            # print(len(parts))
            if len(parts) == 4:
                for part in parts:
                    if 0 <= int(part) <= 255:
                        sum += 1
            else:
                return False
            if sum != 4:
                return False
    except ValueError:
        return False


portInput = input("Введите порт: ")
ipInput = input("Введите ip: ")
port_auto = 9090
ip_auto = "127.0.0.1"

if portVer(portInput) is False:
    print(f'Вы ввели некорректные данные, порт по умолчанию -  {port_auto}')
    portInput = int(port_auto)
portInput = int(portInput)

if ipVer(ipInput) is False:
    print(f'Вы ввели некорректные данные, ip по умолчанию -  {ip_auto}')
    ipInput = ip_auto
ipInput = str(ipInput)


print(f'Ip -> {ipInput}, Порт -> {portInput}')
sock = socket.socket()
sock.setblocking(1)
print("~Соединение с сервером~")
sock.connect((ipInput, portInput))

while True:
    message = input("Введите сообщение => ")
    sock.send(message.encode())
    print("Отправили сообщение")
    if message == 'exit':
        print(f'Мы были отключены от сервера')
        sock.close()
        break
    data = sock.recv(1024)
    print(f'Получили сообщение => {data.decode()}')
