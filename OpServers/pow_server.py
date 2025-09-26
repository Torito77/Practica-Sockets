from operation_server_ABC import OperationServer
from typing import List

class PowServer(OperationServer):
    def __init__(self, host, port, name):
        super().__init__(host, port, name, '^')
        
    def operate(self, nums: List[int]):
        super().operate(nums)
        
        n = nums[0]
        e = 1
        for number in nums[1::]:
            e *= number
        return n**e
