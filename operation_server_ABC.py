from server_ABC import Server
from abc import abstractmethod


class OperationServer(Server):
    def __init__(self, host, port):
        super().__init__(host, port)
        
    def server_start(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            msg = data.decode().strip()
            print(f"Data received: {msg}")
            try:
                nums = [int(num) for num in msg.split(",")]
                res = self.operate(nums)
                #TODO: Return to client: Result: {res}
            except ValueError as ve:
                #TODO: Return to client: Invalid format
                pass
    
    @abstractmethod
    def operate(self, *nums) -> int:
        pass
        