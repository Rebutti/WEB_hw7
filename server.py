import socket
import sys

def main():
    host = socket.gethostname()
    port = 8000

    try:
        server_socket = socket.socket()
    except OSError:
        print('couldn`t open socket')
        sys.exit(1)
    server_socket.bind((host, port))
    print('server started')
    server_socket.listen(3)
    conn, address = server_socket.accept()
    print(f'Connection from {address}')
    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"recieved message: {data}")
            message = input("-->")
            conn.send(message.encode())

if __name__ == "__main__":
    main()