# QR Code Generator
This is a Python-based web crawler that recursively crawls a website, extracts the page titles, and saves the URL and title data into a CSV file.

## Features
- Crawls a website starting from a specified URL.
- Recursively explores links up to a specified depth.
- Saves crawled URLs and their titles into a CSV file.
- Uses concurrent threads for efficient crawling

## Requirements
- Python 3.x
- `requests` library
- `BeautifulSoup` from `bs4` library
- `pyfiglet` library
- `ThreadPoolExecutor` from `concurrent.futures`
- `Lock` from `threading`

You can install using following command:
```bash
pip install requests
pip install beautifulsoup4
pip install pyfiglet
```

## Usage  
1. Clone or download the project files.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. Enter URL and maximum depth you want to crawl.
4. Output is store in CSV file `crawled_urls.csv`.

## Output

```
http://example.com, " ", "Example Domain"
```

## License  
This project is open-source and available under the MIT License.

## Author:  
> Created By: Harsh Gharsandiya