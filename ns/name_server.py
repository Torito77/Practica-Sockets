import socket
from server_ABC import Server
from typing import Dict
import threading

class NameServer(Server):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.server_addreses: Dict[str,str] = {}
        self.ready = threading.Event()

    def server_start(self):
        self.ready.set()
        
        while True:
            data, addr = self.sock.recvfrom(1024)
            msg = data.decode().strip()
            print(f"[{addr}]: {msg}")
            parts = msg.split()
            
            # REGISTER name ip port
            # Registers an ip:port in the server list
            if len(parts) == 4 and parts[0].upper() == "REGISTER":
                _, name, ip, port = parts
                self.server_addreses[name] = f"{ip}:{port}"
                        
            # SHOW SERVER LIST
            # Returns a list of all the servers
            elif len(parts) == 3 and parts[0].upper() == "SHOW":
                if len(self.server_addreses) == 0:
                    sl = "None"
                else:
                    sl = f"[{",".join( list( self.server_addreses.keys() ) )}]"
                    
                self.sock.sendto(sl.encode(), addr)
            
            # LOOKUP name
            # Returns the ip:port of a server under name
            elif len(parts) == 2 and parts[0].upper() == "LOOKUP":
                name = parts[1]
                ans = self.server_addreses.get(name, "Not found")
                self.sock.sendto(ans.encode(), addr)
                
            # Invalid command
            else:
                self.sock.sendto("Invalid request".encode(), addr)