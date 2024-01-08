import requests
from bs4 import BeautifulSoup
import pandas as pd

news_sources = [
    'https://www.nytimes.com/section/world',
    'https://www.nytimes.com/section/world?page=2',
    'https://www.nytimes.com/section/world?page=3',
    'https://www.nytimes.com/section/world?page=4',
    'https://www.nytimes.com/section/world?page=5',
    'https://www.nytimes.com/section/world?page=6',
    'https://www.nytimes.com/section/world?page=7',
    'https://www.nytimes.com/section/world?page=8',
    'https://www.nytimes.com/section/world?page=9',
    'https://www.nytimes.com/section/world?page=10'
]

url = 'https://www.nytimes.com/section/world'


all_headlines = []
top_headlines = []
top_headlines_description = []
top_headlines_images = []
latest_images = []
latest_headlines = []
latest_descriptions = []

def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('a', class_='css-1u3p7j1')
    return [headline.text.strip() for headline in headlines]

def scrape_descriptions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    descriptions = soup.find_all('p', class_='css-tskdi9')
    return [description.text.strip() for description in descriptions]

def scrape_images_top_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    images_top_headlines = soup.find_all('img', class_='css-19ucebhs')
    return [image_top_headlines.text.strip() for image_top_headlines in images_top_headlines]


def scrape_latest_descriptions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    latest_descriptions = soup.find_all('p', 'css-1pga48a e15t083i1')
    return [latest_description.text.strip() for latest_description in latest_descriptions]

for source in news_sources:
    l_description = scrape_latest_descriptions(source)
    latest_descriptions.extend(l_description)

df_latest_description = pd.DataFrame({'col': latest_descriptions})
df_latest_description.drop_duplicates(inplace=True)
latest_descriptions = df_latest_description['col'].tolist()

print(latest_descriptions)