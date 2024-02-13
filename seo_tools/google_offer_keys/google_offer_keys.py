import requests
import csv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import argparse
import logging

class GoogleSearch:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.session = requests.Session()
        self.session.headers.update(self.make_user_agent())
        self.run()

    def make_user_agent(self):
        ua = UserAgent()
        return {'User-Agent': ua.random}

    def get_keys(self):
        with open(self.input_file, mode='r', encoding='utf-8-sig') as key_reader:
            keys = [item.strip() for item in key_reader if item.strip()]
        return keys

    def make_urls(self, keys):
        return [f'https://www.google.com/search?q={key}' for key in keys]

    def page_request(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None

    def soupify(self, page):
        try:
            return BeautifulSoup(page.content, 'html.parser')
        except Exception as e:
            logging.error(f"Failed to parse page: {e}")
            return None

    def find_keys(self, soup):
        offer_elements = soup.find_all('div', {'class': 's75CSd u60jwe r2fjmd AB4Wff'})
        return [offer.text for offer in offer_elements]

    def save_to_csv(self, data, search_key):
        fieldnames = ['search key', 'result']
        with open(self.output_file, mode='a+', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            for result in data:
                writer.writerow({'search key': search_key, 'result': result})

    def run(self):
        keys = self.get_keys()
        self.logging.info('[+] keys extrect form file successfully . ')
        urls = self.make_urls(keys=keys)
        self.logging.info('[+] urls ready for all keys ready . ')

        for url, key in zip(urls, keys):
            response = self.page_request(url)
            self.logging.info(f'[+] resposne get successfully for key {key}. ')
            if response:
                soup = self.soupify(response)
                self.logging.info(f'[+] soup get successfully for key {key}. ')
                if soup:
                    results = self.find_keys(soup)
                    self.logging.info(f'[+] google offer keys get successfully for key {key}. ')
                    self.save_to_csv(data=results, search_key=key)
                    self.logging.info(f'[+] google offer key save  into the CSV file successfully for key {key} . \n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Google Search Results Scraper")
    parser.add_argument('--input', help="Input file containing search keys", required=True)
    parser.add_argument('--output', help="Output CSV file", required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    
    GoogleSearch(input_file=args.input, output_file=args.output)
