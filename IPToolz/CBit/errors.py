ERR='IP Error'
UIPE='Not an IP Address'
__all__=['UnrecognisedIPError',
         'InvalidIPError',
         'InvalidIPRangeError',
         'HexConversionError',
         'IPValueError',
         'IPSegmentError'
         ]
IIPE='Invalid IP Format'
IIRE='0=<value>=255, value out of range'
IVE='Not a valid decimal'
HCE='hexadecimal character conversion out of range'
ISE='IP incomplete segments X.X.X.X or X:X:X:X'
class IPErrors(Exception):
    def __init__(self, msg):
        self.msg=msg
        super().__init__(self, msg)

    def __str__(self):
        return self.msg

class UnrecognisedIPError(IPErrors):
    def __init__(self, msg=UIPE):
        self.msg=msg
        super().__init__(msg)

class InvalidIPError(IPErrors):
    def __init__(self, msg=IIPE):
        self.msg=msg
        super().__init__(msg)

class InvalidIPRangeError(IPErrors):
    def __init__(self, msg=IIRE):
        self.msg=msg
        super().__init__(msg)
        
class HexConversionError(IPErrors):
    def __init__(self, msg=HCE):
        self.msg=msg
        super().__init__(msg)

class IPValueError(IPErrors):
    def __init__(self, msg=IVE):
        self.msg=msg
        super().__init__(msg)
        
class IPSegmentError(IPErrors):
    def __init__(self, msg=ISE):
        self.msg=msg
        super().__init__(msg)
