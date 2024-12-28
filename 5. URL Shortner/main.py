import random
import string
import pyfiglet

def generate_short_code(length=6):
    ch = string.ascii_letters + string.digits
    return ''.join(random.choice(ch) for _ in range(length))

#map long url to short code
url_mapping = {}

def shorten_url(long_url):
    short_code = generate_short_code()
    url_mapping[short_code] = long_url
    return f"fShortened URL: http://short.ly/{short_code}"

def retrive_url(short_code):
    return url_mapping.get(short_code, "URL not found!")

if __name__ == "__main__":
    banner = pyfiglet.figlet_format("URL Shortener")
    while True:
        action = input("[1]. Shorten URL\n[2]. Retrive URL\n[0]. Exit\n")
        if action == '1':
            long_url = input("Enter long url: ")
            print(shorten_url(long_url))
        elif action == '2':
            short_code = input("Enter short code: ")
            print(f"Original URL: {retrive_url(short_code)}")
        elif action == '0':
            break
        else:
            print("Invalid choice.")

