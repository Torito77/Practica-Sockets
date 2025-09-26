from socket import socket, AF_INET, SOCK_DGRAM

addr = ("localhost",7777)

def msg_server(msg, addr=addr) -> str:
    
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.sendto(msg.encode(), addr)
        msgs, res_addr = s.recvfrom(1024)
        return msgs.decode()

if __name__ == "__main__":
    print(f"Received: {msg_server(input(f"Send to [{addr[0]}:{addr[1]}]: "))}")