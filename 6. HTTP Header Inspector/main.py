import requests
import pyfiglet

def inspect_http_headers(url):
    if "https://" not in url or "http://" not in url:
        url = "https://" + url
    try:
        response = requests.get(url)
        headers = response.headers
        print("\nHTTP Headers for: ", url)
        for key, value in headers.items():
            print(f"{key}: {value}")    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    banner = pyfiglet.figlet_format("HTTP Header Analysis")
    print(banner)
    
    url = input("Enter URL to inspect: ")
    inspect_http_headers(url)