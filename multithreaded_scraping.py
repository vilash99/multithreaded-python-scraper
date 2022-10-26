import requests
from bs4 import BeautifulSoup
import concurrent.futures
from urllib.parse import urljoin, urlparse


class MultiThreadedScraper:

    def __init__(self, source_url):
        self.source_url = source_url
        self.root_url = '{}://{}'.format(urlparse(self.source_url).scheme, urlparse(self.source_url).netloc)
        self.all_urls = set([])
        self.total_threads = 5

    def scrap_urls(self):
        page_data = requests.get(self.source_url).content
        soup = BeautifulSoup(page_data, "lxml")

        all_urls = soup.find_all("a", class_="artical-card", href=True)
        for link in all_urls:
            url = urljoin(self.root_url, link['href'])
            self.all_urls.add(url)


    def scrap_pages(self, page_url):
        page_data = requests.get(page_url).content
        soup = BeautifulSoup(page_data, "lxml")

        # Extract Title
        blog_title = soup.find("h1", class_="blog-title").text.strip()

        # Extract Category
        blog_category = soup.find("a", class_="blog-category-name").text.strip()

        # Extract Likes
        blog_total_likes = soup.find("span", class_="like-count").text.strip()

        print("URL: {}, Title: {}, Category: {}, Likes: {}".format(page_url, blog_title, blog_category, blog_total_likes))
        print("*"*20)

    def start_scraper(self):
        # Scrap url content concurrently
        with concurrent.futures.ThreadPoolExecutor(self.total_threads) as executor:
        	executor.map(self.scrap_pages, self.all_urls)


if __name__ == '__main__':
    cc = MultiThreadedScraper("https://www.kushalstudy.com/")
    cc.scrap_urls()
    cc.start_scraper()
