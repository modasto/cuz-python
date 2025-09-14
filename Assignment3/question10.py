import socket
import threading
import time

# --- Server Code ---
def server_program():
    """
    Listens for incoming connections and sends a welcome message.
    """
    host = '127.0.0.1'  # Standard loopback interface address (localhost)
    port = 65432        # Port to listen on (non-privileged ports are > 1023)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        # Accept a connection
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            message = "Hello from server!"
            conn.sendall(message.encode('utf-8'))
            print("Message sent to the client.")

    except socket.error as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server socket closed.")


# --- Client Code ---
def client_program():
    """
    Connects to the server and receives a message.
    """
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 65432        # The port used by the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        data = client_socket.recv(1024)  # Receive data from the server
        print(f"Received from server: '{data.decode('utf-8')}'")

    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")
    except socket.error as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()
        print("Client socket closed.")


if __name__ == '__main__':
    # To run this program:
    # 1. Open a terminal and run this script: python your_script_name.py
    # 2. The server will start.
    # 3. Open a second terminal and run the same script again.
    # 4. The client will start and connect to the server.

    # We use threading to run both in the same script for demonstration.
    # A simple check to see if a server might already be running on the port.
    try:
        # Attempt to connect as a client first
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.connect(('127.0.0.1', 65432))
        test_socket.close()
        # If connection succeeds, a server is likely running, so we run the client.
        print("--- Running Client ---")
        client_program()
    except ConnectionRefusedError:
        # If connection fails, no server is running, so we start the server.
        print("--- Running Server ---")
        server_program()
