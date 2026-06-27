import socket

def grab_banner(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return None