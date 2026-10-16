import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Сервер запущен.")
print(f"Ожидание подключения по адресу {HOST}:{PORT}...")

try:
    client_socket, client_address = server_socket.accept()
    print(f"Клиент подключён: {client_address}")

    with client_socket:
        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode("utf-8")
            print(f"Сообщение от клиента: {message}")

            if message.strip().lower() == "exit":
                client_socket.send(
                    "Соединение завершено.".encode("utf-8")
                )
                break

            response = f"Длина сообщения: {len(message)} символов"
            client_socket.send(response.encode("utf-8"))

    print("Клиент завершил работу.")

finally:
    server_socket.close()
    print("Сервер завершил работу.")