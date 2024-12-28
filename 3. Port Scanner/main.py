import socket
import threading
import pyfiglet

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        pass
    
def scan_ports(ip, start_port, end_port):
    threads = []
    banner = pyfiglet.figlet_format("Port Scanner")
    print(banner)
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    hostname = input("Enter target hostname: ")
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"Host not resolved")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    
    scan_ports(ip, start_port, end_port)
        
    
        
        

        