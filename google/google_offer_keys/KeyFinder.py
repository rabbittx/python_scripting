import requests
from bs4 import BeautifulSoup
import csv


# this script will help you find google offer keys !
# you can use list or string


class KeyFinder:
    def __init__(self, word_list, output_filename='all_keys_list.csv'):
        self.word_list = word_list
        self.keyWord_list = []
        try:
            self.csv_file = csv.writer(open(output_filename, 'w'), delimiter=',')
        except FileExistsError:
            print('[-] Error loading CSV file for writing.')
        self.csv_file.writerow(['Key', 'KeyWord'])

    def find_key_word(self, key):
        self.keyWord_list.clear()
        if " " in self.word_list:
            key = self.word_list.replace(' ', '+')
            key = key
        url = f'https://www.google.com/search?q={key}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for line in soup.find_all('span'):
            children = line.findChildren("div", {'class': 'lRVwie'}, recursive=False)
            for child in children:
                self.keyWord_list.append(child.string)
        return self.keyWord_list

    def save_keys(self, ):
        for word in self.word_list:
            print(f'[*] Processing word : {word}')
            key = self.find_key_word(word)
            try:
                self.csv_file.writerow([word, *key])
            except FileNotFoundError:
                print("'NoneType' object has no attribute 'string'")
        print('[*] processing done ! [*]')

    def start(self):
        self.save_keys()


# TODO how to run it on terminal like this
# python get_google_keys.py start('key')
# TODO try to read keys form .txt
# python get_google.keys.py start('./KeyList.txt')


if __name__ == '__main__':
    # KeyList = 'key word'
    # KeyList = ['Key Word one ', 'key word two' ,' key word n ']
    KeyList = ['! INSERT YOUR KEYS HERE !']
    scraper = KeyFinder(KeyList)
    scraper.start()
