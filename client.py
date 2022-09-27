import socket


def client():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        message = input('-->')

        while message.lower().strip() != 'end':
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(f"recieved message: {data}")
            message = input("-->")
    except ConnectionRefusedError:
        print(f'Server doesn`t work')
    except ConnectionAbortedError:
        print(f'An established connection was aborted')
    except ConnectionResetError:
        print(f'An existing connection was forcibly closed by the remote host')
    finally:
        client_socket.close()


if __name__ == "__main__":
    client()