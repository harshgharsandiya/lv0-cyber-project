import requests
from bs4 import BeautifulSoup
import pyfiglet
import re
from urllib.parse import urljoin

def fetch_page(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        #raise error if response was error
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def extract_mails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def parse_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    #Extract Title
    title = soup.title.string if soup.title else "No title Found"
    print(f"Title: {title}")
    
    #Extract All the Links
    print(f"\n[+] Links found on the page:")
    links = soup.find_all('a', href=True)
    
    #Collect all links
    all_links = set()
    for link in links:
        href = link['href']
        
        # Skip 'mailto:' links
        if href.startswith('mailto:'):
            continue
        
        full_url = urljoin(url, href)
        all_links.add(full_url)
        print(full_url)
    
    # Extract emails from the main page
    print(f"\n[+] Emails found on the page:")
    emails = extract_mails(html_content)
    for email in emails:
        print(email)    
    
        
    #Extract mails from linked page
    print(f"\n[+] Emails emails from linked page:")
    all_emails = set(emails)
    for l in all_links:
        html_cnt = fetch_page(l)
        if html_cnt:
            emails_in_link = extract_mails(html_cnt)
            for email in emails_in_link:
                all_emails.add(email)
        for email in all_emails:
            print(email)
                
    #Print all emails
    print(f"\n[+] All Emails Found: ")
    for email in all_emails:
        print(email)
    


if __name__ == "__main__":
    banner = pyfiglet.figlet_format("Web Scrappy")
    print(banner)
    
    url = input("Enter URL to scrape: ")
    if "https://" not in url:
        url = "https://" + url
    html_content = fetch_page(url)
    parse_page(html_content)    