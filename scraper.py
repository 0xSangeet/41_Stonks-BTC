from investopedia import scrape_investopedia_titles
from morningstar import scrape_morningstar_titles

def scrape():
    scrape_investopedia_titles()
    scrape_morningstar_titles()

if __name__ == '__main__':
    scrape()
