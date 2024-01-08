from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)


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

def scrape_latest_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    images_latest = soup.find_all('img', class_='css-rq4mmj')
    return images_latest

def scrape_latest_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h3', class_='css-1kv6qi e15t083i0')
    return [headline.text.strip() for headline in headlines]

def scrape_latest_descriptions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    latest_descriptions = soup.find_all('p', 'css-1pga48a e15t083i1')
    return [latest_description.text.strip() for latest_description in latest_descriptions]

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

images_top_headlines = soup.find_all('img', class_='css-19ucebh')
for image_tag in images_top_headlines:
    top_headlines_images.append(image_tag['src'])
    
for source in news_sources:
    headlines = scrape_headlines(source)
    all_headlines.extend(headlines)

description = scrape_descriptions(news_sources[0])
top_headlines_description.extend(description)
    
for i in range (0,4):
    top_headlines.append(all_headlines[i])
    
for source in news_sources:
    images = scrape_latest_images(source)
    for image in images:
        latest_images.append(image['src'])


df_latest_images = pd.DataFrame({'col':latest_images})
df_latest_images.drop_duplicates(inplace=True)
latest_images = df_latest_images['col'].tolist()

for source in news_sources:
    l_headlines = scrape_latest_headlines(source)
    latest_headlines.extend(l_headlines)

df_latest_headlines = pd.DataFrame({'col':latest_headlines})
df_latest_headlines.drop_duplicates(inplace=True)
latest_headlines = df_latest_headlines['col'].tolist()

for source in news_sources:
    l_description = scrape_latest_descriptions(source)
    latest_descriptions.extend(l_description)

df_latest_description = pd.DataFrame({'col': latest_descriptions})
df_latest_description.drop_duplicates(inplace=True)
latest_descriptions = df_latest_description['col'].tolist()



@app.route('/')
def index():
    return render_template('index.html', top_headlines=top_headlines, top_headlines_description=top_headlines_description, top_headlines_images=top_headlines_images, latest_images=latest_images, latest_headlines=latest_headlines, len_latest=len(latest_headlines), latest_descriptions=latest_descriptions)

if __name__ == '__main__':
    app.run(debug=True)
