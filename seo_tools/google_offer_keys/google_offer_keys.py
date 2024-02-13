import requests ,csv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def setup_logger():
    """
     Setup logger for the application.

     Returns:
         Logger object
        
    """
    logger = logging.getLogger("GoogleSearchOfferKey")
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to DEBUG
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Add formatter to console handler
    console_handler.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(console_handler)

    return logger

import logging




class  GoogleSearch:
    def __init__(self):
        self.logger = setup_logger()
        self.run()

    def make_user_agent(self):
        ua = UserAgent()
        random_user_agent = ua.random
        headers = {
            'User-Agent': random_user_agent
        }
        self.logger.info('User Agent is ready')
        return headers
    
    def get_keys(self):
        with open('key-to-serach.txt',mode='r',encoding='utf-8-sig') as key_reader:
            keys = key_reader.read()
            self.logger('key read from file ')
        return  [item for item in keys.split('\n') if item.strip()]
    
    def make_urls(self,keys):
        return [f'https://www.google.com/search?q={url}' for url in keys]

    def  page_request(self,url,headers):
       return requests.Session(url, headers=headers) if requests.Session(url, headers=headers).status_code == 200 else 'requests resposne error'

    def  soupify(self,page):
        try :
            return BeautifulSoup(page.text,'html.parser')
        except :
            raise('[-] response is not 200 soupify fail')
        
    def  find_keys(self,soup):
        offer_elements = soup.find_all('div',{'class' : 's75CSd u60jwe r2fjmd AB4Wff'})
        return [offer.text for offer in offer_elements]
    
    def save_to_csv(self, data, search_key, filename):
        fieldnames = ['search key', 'result']
        with open(filename, mode='a+', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            for result in data:
                writer.writerow({'search key': search_key, 'result': result})



    def run(self):
        keys = self.get_keys()
        urls = self.make_urls(keys=keys)
        for url in urls :
            agent = self.make_user_agent()
            response = self.page_request(url=url,headers=agent)
            soup = self.soupify(response)
            results = self.find_keys(soup)
            self.save_to_csv(data=results,search_key=url.split('search?q=')[-1],filename='result.csv')

if __name__ == '__main__' :
    GoogleSearch()