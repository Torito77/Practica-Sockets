from server_ABC import Server
from abc import abstractmethod
from typing import List


class NotEnoughNumbersError(Exception):
    pass

class OperationServer(Server):
    def __init__(self, host:str, port:int, name:str, sign:str):
        super().__init__(host, port)
        self.name: str = name
        self.sign: str = sign
        
    def server_start(self):
        #TODO: Send a Register to name server
        self.sock.sendto(f"REGISTER {self.name} {self.host} {self.port}".encode(),("localhost",7777))
        while True:
            data, addr = self.sock.recvfrom(1024)
            msg = data.decode().strip()
            print(f"Data received: {msg}")
            
            try:
                n_list = msg.split(",")
                nums = [int(num) for num in n_list]
                res = self.operate(nums)
                self.sock.sendto(f"{self.sign.join(n_list)} = {res}".encode(), addr)
            except ValueError as ve:
                self.sock.sendto(f"Error: Formato inválido".encode(), addr)
            except NotEnoughNumbersError as nene:
                self.sock.sendto(str(nene).encode(), addr)
    
    @abstractmethod
    def operate(self, nums:List[int]):
        if len(nums) <= 1:
            raise NotEnoughNumbersError("At least two numbers are required")