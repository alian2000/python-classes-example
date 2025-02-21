import socket
import hashlib
import bcrypt  # Ensure you have bcrypt installed: pip install bcrypt

# Store usernames and hashed passwords
users = {
    'user1': bcrypt.hashpw('pass1'.encode(), bcrypt.gensalt()),
    'user2': bcrypt.hashpw('pass2'.encode(), bcrypt.gensalt())
}

def handle_client(client_socket):
    try:
        client_socket.send(b'Username: ')
        username = client_socket.recv(1024).decode().strip()
        client_socket.send(b'Password: ')
        password = client_socket.recv(1024).decode().strip()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        if username in users and bcrypt.checkpw(password.encode(), users[username]):
            client_socket.send(b'Login successful!\n')
        else:
            client_socket.send(b'Login failed!\n')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Corrected: bind expects a tuple
    server_socket.listen(5)
    print("Server listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
