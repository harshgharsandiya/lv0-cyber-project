import subprocess
import ipaddress
import threading
import pyfiglet
import sys

def ping_ip(ip):
    try:
        response = subprocess.run(['ping', '-n', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            print(f"{ip} is up")
    except Exception as e:
        pass
        
def ping_sweep(network):
    threads = []
    try:
        for ip in network.hosts():
            thread = threading.Thread(target=ping_ip, args=(ip,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("Program Terminated")
        sys.exit(0)
        
if __name__ == "__main__":
    banner = pyfiglet.figlet_format("IP SWEEP")
    print(banner)
    
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    network = ipaddress.IPv4Network(subnet, strict=False)
    print(f"[+] Pinging all hosts in network {subnet}")
    ping_sweep(network)
    