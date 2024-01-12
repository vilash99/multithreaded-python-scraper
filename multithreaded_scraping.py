import re
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from urllib.parse import urljoin, urlparse


class MultiThreadedScraper:
    def __init__(self, source_url):
        self.source_url = source_url
        self.root_url = (
            f'{urlparse(self.source_url).scheme}:'
            f'//{urlparse(self.source_url).netloc}'
        )
        self.all_urls = set([])
        self.total_threads = 10  # change total numbers of threads you want

    def scrape_urls(self):
        """Scrape all urls present in given home page url"""
        page_data = requests.get(self.source_url).content
        soup = BeautifulSoup(page_data, 'lxml')

        all_urls = soup.select('article.product_pod h3 a')

        # Extract only books urls
        for link in all_urls:
            url = urljoin(self.root_url, link['href'])
            self.all_urls.add(url)

    def scrape_pages(self, page_url):
        page_data = requests.get(page_url).content
        soup = BeautifulSoup(page_data, 'lxml')

        # Scrape book title
        title = soup.select('h1')[0].text.strip()

        # Scrape price
        price = soup.select('p.price_color')[0].text.strip()

        # Scrape total stocks
        quantity = soup.select('p.instock')[0].text.strip()

        match = re.search(r'\b((\d+)\b)', quantity)
        if match:
            quantity = int(match.group(1))  # Extract number as integer
        else:
            quantity = 0

        print(
            f'URL: {page_url}, Title: {title}, '
            f'Price: {price}, Quantity: {quantity}'
        )

    def start_scraper(self):
        """Begin concurrent scraper"""
        with concurrent.futures.ThreadPoolExecutor(self.total_threads) as executor:
            executor.map(self.scrape_pages, self.all_urls)


if __name__ == '__main__':
    cc = MultiThreadedScraper('https://books.toscrape.com/')
    cc.scrape_urls()
    cc.start_scraper()
