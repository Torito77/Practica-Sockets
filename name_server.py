import socket
from server_ABC import Server
from typing import Dict

# TODO: Reduce code by creating parent Server class
class NameServer(Server):
    def __init__(self, host, port):
        self.server_addreses: Dict[str,str] = {}
        super().__init__(host, port)

    def server_start(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            msg = data.decode().strip()
            print(f"[{addr}]: {msg}")
            parts = msg.split()
            
            # REGISTER name ip port
            if len(parts) == 4 and parts[0] == "REGISTER":
                _, name, ip, port = parts
                self.server_addreses[name] = f"{ip}:{port}"
                        
            # LOOKUP name
            elif len(parts) == 2 and parts[0] == "LOOKUP":
                name = parts[1]
                ans = self.server_addreses.get(name, "Not found")
                self.sock.sendto(ans.encode(), addr)
                        


def run_name_server():
    ns = NameServer(host="localhost", port=7777)

if __name__ == "__main__":
    run_name_server()