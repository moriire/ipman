# IPToolz
IPToolz is a high-level core python package for Internet Protocol(IP) manipulations.

### Installation

```sh
 pip install IPToolz
```
### Helper Functions
```sh
>> import IPToolz
>> dir(IPToolz)

['IPType', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'binary', 'decimal', 'getIP', 'getlocal', 'hexadecimal', 'ip', 'isIPV4', 'isIPV6', 'mb', 'octet', 'web']
```

### Usage

```sh
from IPToolz import X
#e.g. 
from OPToolz import isIPV4
#or 
from IPtoolz import *
```
#### getlocal
This return device localhost ip address.
```sh
>> from IPToolz import getIP
>> getlocal()
127.0.0.1
```

#### getIP
This returns the ip address of a given url.
```sh
>> from IPToolz import getIP
>> getIP('www.google.com')
x.x.x.x
```

#### IPType
This returns the ip address of a given url.
```sh
>> from IPToolz import IPType
>> IPType('x.x.x.x')
IPV-4
```
#### isIPV4
This returns the ip address of a given url.
```sh
>> from IPToolz import isIPV4
>> isIPV4('x.x.x.x')
('x.x.x.x', True)
```
#### isIPV6
This returns the ip address of a given url.
```sh
>> from IPToolz import isIPV6
>> isIPV6('x:x:x::x')('x.x.x.x.x.x.x.x', 
True)
```

#### Others
```sh
>> #Conversion from decimal to binary
>> binary(10)
1010
>>
>> #Conversion from decimal to hexadecimal
>> hexadecimal(170)
1010A
>>
>> #Conversion from decimal to octet
>> octet(10)
12

```
