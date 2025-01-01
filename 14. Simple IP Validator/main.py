import re

def is_valid_ip4(ip):
    """
    Validate IPv4 address

    :param ip: str - IP address to validate
    :return: bool - True if valid, else false    
    """
    
    #regex pattern
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
    
    if not re.match(pattern, ip):
        return False
    
    segments = ip.split(".")
    for segment in segments:
        if not 0 <= int(segment) <=255:
            return False
        
    return True

def is_valid_ipv6(ip):
    """
    Validate IPv6 address
    :param ip: str - IP address to validate
    :return: bool - True if valid else False
    """
    
    #regex
    pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(pattern, ip))
    
def validate_ip(ip):
    if is_valid_ip4(ip):
        return "IPv4"
    elif is_valid_ipv6(ip):
        return "IPv6"
    else:
        return "Invalid"

#Main Program
if __name__ == "__main__":
    ip_address = input("Enter IP address to validate: ").strip()
    result = validate_ip(ip_address)
    
    if result != "Invalid":
        print(f"{ip_address} is valid {result} Address.")
    else:
        print(f"{ip_address} not valid IP Address.")