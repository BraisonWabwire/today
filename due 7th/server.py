import socket
import threading
import time
import os

def handle_client(client_socket, client_address):
    try:
        # Receive request from client
        request = client_socket.recv(1024).decode()
        print(f"Received request from {client_address}:\n{request}")

        # Parse the requested file
        headers = request.split('\n')
        if len(headers) > 0 and headers[0].startswith('GET'):
            file_name = headers[0].split()[1][1:]  # Remove the '/' from file path
            if file_name == '':
                file_name = 'index.html'  # Default file

            # Check if file exists and serve it
            if os.path.isfile(file_name):
                with open(file_name, 'rb') as file:
                    content = file.read()
                response = b"HTTP/1.1 200 OK\r\n\r\n" + content
            else:
                response = b"HTTP/1.1 404 Not Found\r\n\r\nFile not found."
        else:
            response = b"HTTP/1.1 400 Bad Request\r\n\r\nInvalid request."

        # Send response back to client and close connection
        client_socket.sendall(response)
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Server listening on port {port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        
        # Handle client in a new thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    PORT = 8080
    start_server(PORT)
