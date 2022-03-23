import socket
import re
from .errors import *

class MBit:
    def __init__(self):
        self.bit=[]

    def __comp__(self, R):
        if R==10:
            return self.bit.append('A')
        elif R==11:
            return self.bit.append('B')
        elif R==12:
            return self.bit.append('C')
        elif R==13:
            return self.bit.append('D')
        elif R==14:
            return self.bit.append('E')
        elif R==15:
            return self.bit.append('F')
        else:
            return self.bit.append(R)

    def bits(self, dec, base=2):
        if not isinstance(dec, int):
            raise IPValueError
        else:
            Q,R=dec//base, dec%base
            self.__comp__(R)
                
            if Q>0:
                return self.bits(Q)
            bits=""
            for i in self.bit.__reversed__():
                bits+=str(i)
            return bits
    
    def __eq__(self, param):
        if param=='A':
            return 10
        elif param=='B':
            return 11
        elif param=='C':
            return 12
        elif param=='D':
            return 13
        elif param=='E':
            return 14
        elif param=='F':
            return 15
        else:
            raise HexConversionError
            
        

    def dec(self, bits, base=2):
        val=[]
        for i, bit in enumerate(bits):
            if bit.isalpha():
                bit=self.__eq__(bit)
            val.append(int(bit)*base**(len(bits)-1-i))
        return sum(val)
    
class IPAddr:
    def __init__(self, addr):
        self.addr=addr


    def __count__(self, param):
        count=self.addr.count(param)
        return count

    def __str__(self, param):
        return re.sub('::',param*':0000'+':', self.addr)       
       
    def __type__(self):
        if self.__count__('.')==4:
            if  re.match(r'[0-255].[0-255].[0-255].[0-255]', self.addr):
                return self.addr, 'IPV-4'
            
        elif self.__count__(':'):
            if (re.match(r'(\w+):(\w+):(\w+):(\w+):(\w+):(\w+):(\w+):(\w+)', self.addr))and(re.findall('::', self.addr)==[]):
                    return 'IPV-6'
                
            elif not re.match(r'(\w+):(\w+):(\w+):(\w+):(\w+):(\w+):(\w+):(\w+)', self.addr):
                if len(re.findall('::', self.addr))==1:
                    norm=re.sub('::', ':', self.addr)
                    length=8-len(norm.split(':'))
                    return self.__str__(length), 'IPV-6'
            else:
                raise InvalidIPError
        else:
            raise IPSegmentError

    def __split__(self, sym=':' or '.'):
        return self.addr.split(sym) 
   
    def __comp__(self):
        bounds=int(self.__split__()[0])
        if 0<bounds<=127:
            return 'A'
        elif 127<bounds<=191:
            return 'B'
        elif 191<bounds<=223:
            return 'C'
        elif 224<bounds<=239:
            return 'D'
        elif 239<bounds<=255:
            return 'E'
        else:
            raise InvalidIPRangeError
        
    def IPType(self):
        return self.__type__()

    def isIPV4(self):
        return self.__type__()[1].__eq__('IPV-4')

    def isIPV6(self):
        return self.__type__()[1].__eq__('IPV-6')

    def hex(self):
        dec=[MBit().dec(seg, 16) for seg in self.__split__()]
        hexa=[MBit().bits(i, 16) for i in dec]
        return ':'.join(hexa)

    def bits(self, addr):
        return MBit().bits(addr, 16)
    

class Web:
    def __init__(self, url):
        self.ip=socket.gethostbyname(url)
    def __str__(self):
        return self.ip
