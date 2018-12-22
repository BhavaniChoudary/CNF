import socket

def Main():
    host  = '10.10.11.38'
    port = 5027

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)

    while True:
        c, addr = s.accept()
        print ('connection from : '+ str(addr))
        while True:
            data = c.recv(1024).decode()
        if not data:
            break
        print ("from connected user : " + str(data))
        data = str(data).upper()
        print("server closed from" + str(addr))
    c.close()

if __name__ == '__main__':
    Main()