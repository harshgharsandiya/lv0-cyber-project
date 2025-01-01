# Packet Sniffer
This is a Python-based Packet Sniffer that captures network packets, analyzes them, and displays information such as source IP, destination IP, protocol, and payload. It can also filter specific types of packets (e.g., HTTP)

## Features
- Captures live network traffic.
- Displays source and destination IP addresses, protocol, and payload.
- Filters packets based on protocols (e.g., TCP, HTTP).
- Supports real-time packet monitoring.

## Requirements
- Python 3.x
- `scapy` library

You can install using following command:
```bash
pip install scapy
```

## Usage  
1. Clone or download the project files.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. The program will start capturing packets and display their details in real time.

## Output

```
Source IP: 192.168.1.5
Destination IP: 93.184.216.34
HTTP Data:
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
...
==================================================
```

## Note
> Ensure you run the script with appropriate privileges, as sniffing network packets requires elevated permissions.

> This program captures unencrypted packets like HTTP. It will not capture HTTPS traffic without SSL decryption, which requires additional steps.

## License  
This project is open-source and available under the MIT License.

## Author:  
> Created By: Harsh Gharsandiya