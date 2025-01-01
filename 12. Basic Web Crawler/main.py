import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
import pyfiglet
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

class WebCrawler:
    def __init__(self, max_depth=2, max_workers=10):
        self.visited = set()
        self.visited_lock = Lock()
        self.csv_lock = Lock()
        self.max_depth = max_depth
        self.max_workers = max_workers
        self.active_crawls = 0
        self.active_crawls_lock = Lock()

    def is_visited(self, url):
        with self.visited_lock:
            return url in self.visited

    def add_visited(self, url):
        with self.visited_lock:
            self.visited.add(url)

    def increment_active_crawls(self):
        with self.active_crawls_lock:
            self.active_crawls += 1

    def decrement_active_crawls(self):
        with self.active_crawls_lock:
            self.active_crawls -= 1

    def is_valid_url(self, url, root_domain):
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return bool(parsed_url.scheme) and bool(parsed_url.netloc) and root_domain in domain

    def save_to_csv(self, url, title):
        with self.csv_lock:
            with open('crawled_urls.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([url, " ", title])

    def crawl(self, url, depth, root_url, executor):
        if depth > self.max_depth or self.is_visited(url):
            return

        self.increment_active_crawls()
        self.add_visited(url)

        try:
            print(f"Crawling URL: {url} at depth {depth}")
            
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code != 200:
                print(f"Error: {response.status_code} for {url}")
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            print(f"Title: {title}")
            self.save_to_csv(url, title)

            if depth < self.max_depth:
                futures = []
                root_domain = urlparse(root_url).netloc
                
                for link in soup.find_all('a', href=True):
                    next_url = urljoin(url, link['href'])
                    if self.is_valid_url(next_url, root_domain) and not self.is_visited(next_url):
                        futures.append(
                            executor.submit(self.crawl, next_url, depth + 1, root_url, executor)
                        )

                for future in futures:
                    future.result()

        except requests.exceptions.RequestException as e:
            print(f"Request error for {url}: {e}")
        except Exception as e:
            print(f"Unexpected error for {url}: {e}")
        finally:
            self.decrement_active_crawls()

    def start_crawl(self, root_url):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            self.crawl(root_url, 0, root_url, executor)
            while self.active_crawls > 0:
                time.sleep(0.1)  # Wait for all crawls to complete

if __name__ == "__main__":
    print(pyfiglet.figlet_format("Web Crawler"))

    try:
        root_url = input("Enter URL: ")
        depth = int(input("Enter depth: "))
        
        crawler = WebCrawler(max_depth=depth)
        crawler.start_crawl(root_url)
        
        print("\nCrawling completed!")
        print(f"Total URLs crawled: {len(crawler.visited)}")
        
    except KeyboardInterrupt:
        print("\nProgram Terminated")
        sys.exit(0)