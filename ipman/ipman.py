import socket
import re
from .errors import *

class Address:
    def __init__(self, addr):
        self.addr = addr

    def __toBin(self, x: int):
        return bin(x).split("b")[1]
    
    def __list__(self):
        return self.addr.split(":")
    
    def to_byte(self, x):
        return "{(8-len(value))*0}{value}".format(value=self.__toBin())
    
    def __toDec(self, x: str):
        n = 128
        total = 0
        for (i, val) in enumerate(x):
            total += n*val
            n /= 2
        return total

    def from_dec2bin(self):
        return map(self.__toBin, self.__list__())
    
    def from_bin2dec(self):
        return map(self.__toDec, self.__list__())
    
class IP(Address):
    def __init__(self, addr) -> None:
        self.addr = addr
        super(IP, self).__init__(addr)
    
    def __type(self, first_bits):
        if (0<= first_bits<=127):
            return "A"
        elif (128<= first_bits<=191):
            return "B"
        elif (192<= first_bits<=223):
            return "C"
        elif (208<= first_bits<=239):
            return "D"
        elif (216<= first_bits<=247):
            return "E"
        
    def get_index(self):
        string = "ABC"
        index = string.index(self.__type(self.addr))+1
        return index
    
    def subnet_mask(self):
        null_count = 4-self.get_index()
        return ".".join(["255" for _ in range(self.get_index())] + ["0" for _ in range(null_count)])
    
    def hosts_count(self):
        return 2**(32-(self.get_index())) - 2
    
    def network_count(self):
        return 2**(4-self.get_index())
    
    def host_address(self):
        return f"{self.addr.rpartition('.')[0]}.0"
    
    def network_range(self):
        return 0
    
    def __repr__(self):
        return f"<IP {self.from_dec2bin(self.addr)}>"
    
    def __type__(self):
        return f"<IPType {self.__type(self.__list__()[0])} {self.addr}>"
        


                

        """
        if  re.match(r'[0-255].[0-255].[0-255].[0-255]', self.addr):
                return self.addr, 'IPV-4'
        elif not re.match(r'(\w+):(\w+):(\w+):(\w+):(\w+):(\w+):(\w+):(\w+)', self.addr):
            if len(re.findall('::', self.addr))==1:
                norm=re.sub('::', ':', self.addr)
                length=8-len(norm.split(':'))
                return self.addr, 'IPV-6'
            el  return self.addr, 'IPV-6'
            else:
                raise InvalidIPError
        """

    @classmethod
    def IPFromDecimal(cls, addr: int):
        return cls(cls.__str__())
    
    @classmethod
    def IPFromBinary(cls, addr: str):
        return cls(cls.__str__())