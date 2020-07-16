import socket
import config

server = config.server
port = config.port
nickname = config.nickname
token = config.token
buffer = ""

def connect():
    channel = input("plz input channel name : ")
    s = socket.socket()
    s.connect((server, port))
    s.send(f"PASS {token}\r\n".encode("utf-8"))
    s.send(f"NICK {nickname}\r\n".encode("utf-8"))
    s.send(f"JOIN #{channel}\r\n".encode("utf-8"))
    print("Joined twitch.tv/" + channel + " !!")
    print("if you want to stop, push ctrl+C or ctrl+D")
    try:
        while True:
            buffer = s.recv(4096).decode("utf-8")
            tmp = buffer.split(":")
            if buffer.startswith("PING"):
                print("PingPong")
                s.send(str("PONG :"+tmp[1]+"\r\n").encode("utf-8"))
            elif "PRIVMSG" in tmp[1].split():
                username = tmp[1].split("!")[0]
                msg = tmp[-1]
                print(username + ": " + msg, end="")
    except KeyboardInterrupt:
        s.close()
        exit()



