from .CBit.mo import MBit as Toolz
from .CBit.mo import IPAddr, Web
from .CBit.errors import *
__all__=['binary', 'octet', 'hexadecimal', 'decimal', 'getlocal', 'getIP', 'IPType', 'isIPV4', 'isIPV6']

def binary(dec):
    """This function converts decimal nuToolzer into binary bits.
        e.g. 10-decimal is equivalent to 1010-binary.
    """
    return Toolz().bits(dec, 2)
def octet(dec):
    """This function converts decimal nuToolzer into octet bits.
        e.g. 10-decimal is equivalent to 12-octet.
    """
    return Toolz().bits(dec, 8)
def hexadecimal(dec):
    """This function converts decimal nuToolzer into hexadecimal.
       e.g. 10-decimal is equivalent to 12-octet bits.
    """
    return Toolz().bits(dec, 16)

def decimal(bits):
    """This function converts binary bits to decimal.
        e.g. 1010 in base 2 is equivalent to 10.
    """
    return Toolz().dec(bits, 2)

def getlocal():
    """
    This return default machine ip address.
    >> from IPToolz import getIP
    >> getIP('www.instagram.com')
    127.0.0.0
    """
    return Web('localhost')

def getIP(url):
    """
    This returns the ip address of a given url.
    e.g.
    >> from IPToolz import getIP
    >> getIP('www.instagram.com')
    xxx.xxx.xxx.xxx
    """
    return Web(url)

def IPType(addr):
    """
    addr --> str
    >> from IPToolz import IPType
    >> IPType('x.x.x.x')
    IPV-4
    """
    return IPAddr(addr).IPType()

def isIPV4(addr):
    """
    addr --> str
    >> from IPToolz import IPType
    >> IPType('x.x.x.x')
    True
    """
    return IPAddr(addr).isIPV4()

def isIPV6(addr):
    """
    addr --> str
    >> from IPToolz import IPType
    >> IPType('x:x::x.x')
    IPV-4
    """
    return IPAddr(addr).isIPV6()
