import socket
import struct
import sys

print(sys.argv)



packer = struct.Struct('20si')

domains = ('www.this.com','www.that.com','www.these.com','www.those.com','www.my.com')


def get_service_by_port(row):
    with open ('domains.bin','rb')as f:
        f.seek(packer.size * row)
        dataInBin = f.read(packer.size)
        data = packer.unpack(dataInBin)
        port = data[1]
        global resp
        try:
            resp = socket.getservbyport(port,'tcp')
        except:
            resp ='err'
    return resp

def get_adress_by_domain(row):
    with open ('domains.bin','rb')as f:
        f.seek(packer.size * row)
        dataInBin = f.read(packer.size)
        data = packer.unpack(dataInBin)
        domain = data[0].decode().strip('\x00')
        hostip = socket.gethostbyname(domain)
    return hostip

print(get_adress_by_domain(1))
print(get_service_by_port(5))