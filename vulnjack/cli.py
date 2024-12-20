import time
import argparse
from scraply import scrape_urls
import vulheader

def check_headers(url):
    start_time = time.time()
    urls = scrape_urls(url)

    for scraped_url in urls:
        print(f"Checking URL: {scraped_url}")
        result = vulheader.check(scraped_url, "Strict-Transport-Security")
        if result == "missing":
            print(f"Strict-Transport-Security: Missing for {scraped_url}")
        else:
            print(f"Strict-Transport-Security: Present for {scraped_url}")

    end_time = time.time()
    print(f"Time taken to scrape: {end_time - start_time} seconds")

def main():
    parser = argparse.ArgumentParser(description="Check for Strict-Transport-Security header in URLs scraped from a website.")
    parser.add_argument('--url', type=str, required=True, help='The URL of the website to scrape.')

    args = parser.parse_args()

    check_headers(args.url)

if __name__ == '__main__':
    main()
