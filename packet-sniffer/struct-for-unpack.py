from struct import *

#store as bytes _data
packed_data = pack('iif',3,4232,34.234909)

print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#decode byte data
data = unpack('iif',packed_data)

print(data)
