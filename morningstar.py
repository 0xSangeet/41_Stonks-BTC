import requests
from bs4 import BeautifulSoup

prompts = []

html = requests.get('https://www.morningstar.com/start-investing').text
soup = BeautifulSoup(html, 'lxml')

def scrape_morningstar_titles():
    prompt1 = soup.find('section', class_="mdc-topic-grid mdc-editorial-block mdc-topic-grid--listing").find('article', class_="mdc-grid-item mdc-article-grid-item mdc-grid-item--huge").find('div', class_="mdc-grid-item__content").a.text
    prompts.append(prompt1.replace('\n', '').replace('\t', ''))

    next_prompts1 = soup.find('section', class_="mdc-topic-grid mdc-editorial-block mdc-topic-grid--listing").find_all('article', class_="mdc-grid-item mdc-custom-grid-item mdc-grid-item--large")
    for prompt in next_prompts1:
        prompt = prompt.find('div', class_="mdc-grid-item__content").a.text
        prompts.append(prompt.strip())
    
    next_prompts2 = soup.find('section', class_="mdc-topic-grid mdc-editorial-block mdc-topic-grid--listing").find_all('article', class_="mdc-grid-item mdc-article-grid-item mdc-grid-item--large")
    for prompt in next_prompts2:
        prompt = prompt.find('div', class_="mdc-grid-item__content").a.text
        prompts.append(prompt.strip())
    
    with open('prompts.txt', 'a') as f:
        for prompt in prompts:
            f.write(prompt + '\n')

if __name__ == '__main__':
    scrape_morningstar_titles()
