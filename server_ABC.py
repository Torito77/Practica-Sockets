import socket
from abc import ABC, abstractmethod

class Server(ABC):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host, port))
        
        print(f"Server running on {self.host}:{self.port}")
        self.server_start()
        
    @abstractmethod
    def server_start():
        pass