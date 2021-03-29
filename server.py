import socket

print("~Запуск сервера~")
sock = socket.socket()
sock.bind(('', 9090))
print("~Начало прослушивания порта~")
sock.listen(0)
print("~Подключение клиента~")
conn, addr = sock.accept()
print(f"Клиент {addr} был подключен")

msg = ''

while True:
    data = conn.recv(1024)
    if not data:
        print(f"Клиент {addr} был отключен")
        break
    print(f'Получили сообщение: {data.decode()}')
    msg += data.decode()
    conn.send(data)

    if data.decode() == 'exit':
        print("Сервер остановили")
        running = False
        conn.close()
        break
    print(f'Отправленное сообщение: {data.decode()}')

conn.close()
