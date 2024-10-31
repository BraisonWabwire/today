import socket
import time

def get_file(server_ip, port, file_name):
    try:
        # Create client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, port))
        
        # Send HTTP GET request
        request = f"GET /{file_name} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
        start_time = time.time()
        client_socket.send(request.encode())
        
        # Receive and process response
        response = client_socket.recv(4096)
        rtt = time.time() - start_time
        print(f"Response:\n{response.decode()}")
        print(f"Round Trip Time (RTT): {rtt:.6f} seconds")

        # Close the socket
        client_socket.close()
    except Exception as e:
        print(f"Error connecting to server: {e}")

if __name__ == "__main__":
    SERVER_IP = '127.0.0.1'  # Assuming server is on the same machine
    PORT = 8080
    FILE_NAME = 'index.html'  # Replace with the name of the requested file
    get_file(SERVER_IP, PORT, FILE_NAME)
