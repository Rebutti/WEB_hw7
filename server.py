import socket

def main():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f'Connection from {address}')
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"recieved message: {data}")
            message = input("-->")
            conn.send(message.encode())
    except OSError:
        print(f'An operation was attempted on something that is not a socket')
    finally:
        conn.close()


if __name__ == "__main__":
    main()