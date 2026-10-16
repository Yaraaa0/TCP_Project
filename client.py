import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    print("Подключено к серверу.")
    print("Введите сообщение или exit для выхода.")

    while True:
        message = input("> ")
        client_socket.send(message.encode("utf-8"))

        response = client_socket.recv(1024).decode("utf-8")
        print(f"Ответ сервера: {response}")

        if message.strip().lower() == "exit":
            break

print("Клиент завершил работу.")