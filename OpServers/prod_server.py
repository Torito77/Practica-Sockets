from Abstracts.operation_server_ABC import OperationServer
from typing import List

class ProdServer(OperationServer):
    def __init__(self, host, port, name):
        super().__init__(host, port, name, 'x')
        
    def operate(self, nums: List[int]):
        super().operate(nums)
        
        n = 1
        for number in nums:
            n *= number
        return n
