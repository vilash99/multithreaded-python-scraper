# Build Multi-Threaded Web Scraper in Python

For detail explaination of this code, please check blog https://www.kushalstudy.com/blog/how-to-build-multi-threaded-web-scraper-in-python/

## Libraries Needed
BeautifulSoup: BeautifulSoup is a python library that makes it easy to scrape information from any web pages. It sits at top of an HTML or XML parser, providing Pythonic ways for iterating, searching, and modifying the parse tree. To install this library, type the following command in IDE/terminal.

```bash
pip install beautifulsoup4
```
requests: Requests is a simple, yet elegant, HTTP library. This library allows you to send HTTP/1.1 requests very easily.

```bash
pip install requests
```
### Stepwise implementation
We will follow following steps to build multithreaded script.
1. Import required library
2. Create main program and object of class MultiThreadedScraper with argument source_url.
3. MultiThreadedScraper class implementation. 
4. Scrap all URLs in the given source URL.
5. Create scrap_pages function which will scrap required data.
6. Call ThreadPoolExecutor to run scraper

When you run above code, the output will look like below.

URL: https://www.kushalstudy.com/blog/what-is-raid-in-operating-systems/, Title: What is RAID in Operating Systems, Category: BCA Study, Likes: Likes 2

URL: https://www.kushalstudy.com/blog/disk-scheduling-algorithms-in-operating-systems/, Title: Disk Scheduling Algorithms in Operating Systems, Category: BCA Study, Likes: Likes 2

URL: https://www.kushalstudy.com/blog/what-is-disk-cache-in-operating-systems/, Title: What is Disk Cache in Operating Systems, Category: BCA Study, Likes: Likes 1

URL: https://www.kushalstudy.com/blog/data-structures-programs-implementation-using-c/, Title: Data Structures Programs Implementation Using C++, Category: BCA Study, Likes: Likes 3

URL: https://www.kushalstudy.com/blog/io-buffering-disk-io-in-operating-systems/, Title: I/O Buffering & Disk I/O In Operating Systems, Category: BCA Study, Likes: Likes 6

URL: https://www.kushalstudy.com/blog/what-is-memory-management-in-operating-system/, Title: What is Memory Management in Operating System, Category: BCA Study, Likes: Likes 4

URL: https://www.kushalstudy.com/blog/simple-c-programs-based-on-discrete-mathematics/, Title: Simple C Programs Based on Discrete Mathematics, Category: BCA Study, Likes: Likes 4

URL: https://www.kushalstudy.com/blog/memory-allocation-method-in-operating-systems/, Title: Memory Allocation Method in Operating Systems, Category: BCA Study, Likes: Likes 5

URL: https://www.kushalstudy.com/blog/simple-c-programs-based-on-the-mathematical-statistics/, Title: Simple C Programs Based on the Mathematical Statistics, Category: BCA Study, Likes: Likes 3
