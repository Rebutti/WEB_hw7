import socket
import sys


def client():
    host = socket.gethostname()
    port = 8000

    with socket.socket() as client_socket:
        try:
            client_socket.connect((host, port))
        except ConnectionRefusedError:
            print(f'Server doesn`t work')
            sys.exit(1)
        except ConnectionAbortedError:
            print(f'An established connection was aborted')
            sys.exit(1)
        except OSError:
            print('could not open socket')
            sys.exit(1)
        message = input('-->')

        while message.lower().strip() != 'end':
            try:
                client_socket.send(message.encode())
            except ConnectionResetError:
                print(f'An existing connection was forcibly closed by the remote host')
                sys.exit(1)
            try:
                data = client_socket.recv(1024).decode()
            except ConnectionResetError:
                print(f'An existing connection was forcibly closed by the remote host')
                sys.exit(1)
            print(f"recieved message: {data}")
            message = input("-->")
    


if __name__ == "__main__":
    client()