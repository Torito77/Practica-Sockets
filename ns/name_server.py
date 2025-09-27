import socket
from Abstracts.server_ABC import Server
from typing import Dict

class NameServer(Server):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.server_addreses: Dict[str,str] = {}

    def server_start(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            msg = data.decode().strip()
            print(f"[{addr}]: {msg}")
            parts = msg.split()
            
            # LOOKUP name
            # Returns the ip:port of a server under name
            if len(parts) == 2 and parts[0].upper() == "LOOKUP":
                name = parts[1]
                ans = self.server_addreses.get(name, "Not found")
                self.sock.sendto(ans.encode(), addr)
                
            # REGISTER name 
            # Registers an ip:port in the server list
            elif len(parts) == 2 and parts[0].upper() == "REGISTER":
                name= parts[1]
                ip, port = addr
                self.server_addreses[name] = f"{ip}:{port}"
                        
            # SHOW SERVER LIST
            # Returns a list of all the servers
            elif len(parts) == 3 and parts[0].upper() == "SHOW":
                if len(self.server_addreses) == 0:
                    sl = "None"
                else:
                    sl = f"[{",".join( list( self.server_addreses.keys() ) )}]"
                    
                self.sock.sendto(sl.encode(), addr)
                
            # Invalid command
            else:
                self.sock.sendto("Invalid request".encode(), addr)