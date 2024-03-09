from bs4 import BeautifulSoup
from zenrows import ZenRowsClient

zenrows_api_key = '' #put your zenrows api key here
client = ZenRowsClient(zenrows_api_key) 
url = "https://www.investopedia.com/trading-4427765"
html = client.get(url).text
soup = BeautifulSoup(html, 'lxml')

def scrape_investopedia_titles():
    all_titles = soup.find('section', class_="comp mntl-taxonomysc", id="mntl-taxonomysc_1-0")
    print_titles = all_titles.find_all('div', {'data-tag': 'Trading'})

    with open('prompts.txt', 'a') as f:
        for req_title in print_titles:
            f.write(req_title.span.text.strip()+'\n')

if __name__ == '__main__':
    scrape_investopedia_titles()
