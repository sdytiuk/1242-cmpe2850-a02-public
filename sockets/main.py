import socket

if __name__ == '__main__':

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        s.settimeout(None)

        #s.connect(('W213-INST', 1666))
        s.connect(('10.132.8.166',1666))
        errVal = s.sendall('Hello Jacob'.encode('utf-8'))
        print(errVal)
        data = s.recv(1024).decode('utf-8')
        print(data)
    except socket.gaierror:
        print("Invalid address or hostname")
    except socket.timeout:
        print("Connection timed out")
    except ConnectionRefusedError:
        print("Connection refused by the server")
    except Exception as e:
        print("unexpected error", e)
    else:
        print("Connection successful")
        s.shutdown(socket.SHUT_RDWR)
        s.close()
