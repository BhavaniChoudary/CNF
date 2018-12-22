import socket
def main():
    host  = '10.10.11.38'
    port = 5027

    s = socket.socket()
    s.connect((host,port))

    message = input("Mark Attendence Roll_no : ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
    s.close()

if __name__ == "__main__":
    main()