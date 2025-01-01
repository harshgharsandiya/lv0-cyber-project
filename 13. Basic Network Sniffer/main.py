from scapy.all import sniff
from scapy.layers.inet import TCP, IP
from scapy.packet import Raw
import sys

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        #extract payload
        payload = packet[Raw].load.decode(errors="ignore")
        if "HTTP" in payload:
            print(f"Source IP: {packet[IP].src}")
            print(f"Destination IP: {packet[IP].dst}")
            print("HTTP Data: ")
            print(payload)
            print("=" * 50)

try:         
    sniff(filter="tcp port 80", prn=packet_callback, store=0)
except KeyboardInterrupt:
    print("\nSniffer stopped.")