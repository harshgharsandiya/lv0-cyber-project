# Simple Ping Sweep

A simple Python-based tool that performs a ping sweep across all hosts in a given subnet. It uses multithreading to speed up the process and provides a basic way to check if a host is up or down within a network.

## Features
- Ping sweep for all hosts in a subnet.
- Multithreaded for faster execution.

## Prerequisites  
- Python 3.x
- `pyfiglet` library (can be installed using `pip install pyfiglet`)

## Usage  
1. Clone or download the project files.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. Enter Subnet(e.g., 192.168.1.0/24)
4. Program will display alive hosts.

## Output

```
Enter subnet (e.g., 192.168.1.0/24): 192.168.1.0/24
[+] Pinging all hosts in network 192.168.1.0/24
192.168.1.1 is up
192.168.1.2 is down
192.168.1.3 is up
```

## License  
This project is open-source and available under the MIT License.

## Author:  
> Created By: Harsh Gharsandiya