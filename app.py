from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

# news sources
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

news_sources2 = [
    'https://www.bbc.com/'
]

url = 'https://www.nytimes.com/section/world'

# for url
all_headlines = []
top_headlines = []
top_headlines_description = []
top_headlines_images = []
latest_images = []
latest_headlines = []
latest_descriptions = []

# for url2
all_images_list = []
all_headlines_list = []
news_headlines = []
sports_headlines = []
india_news_headlines = []
authors_picks_headlines = []

# defs of url
def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('a', class_='css-14u258h')
    return [headline.text.strip() for headline in headlines]

def scrape_descriptions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    descriptions = soup.find_all('p', class_='css-tskdi9')
    return [description.text.strip() for description in descriptions]

# def of url2
def scrape_all_images(url2):
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_images = soup.find_all('img', class_='image-replace')
    return all_images

def scrape_all_headlines(url2):
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_headlines = soup.find_all('a', class_='media__link')
    return [all_headline.text.strip() for all_headline in all_headlines]

## preparing response for url
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

## top headlines images
images_top_headlines = soup.find_all('img', class_='css-19ucebh')
for image_tag in images_top_headlines:
    top_headlines_images.append(image_tag['src'])
    
## top headlines
for source in news_sources:
    headlines = scrape_headlines(source)
    all_headlines.extend(headlines)

## top headlines descriptions
description = scrape_descriptions(news_sources[0])
top_headlines_description.extend(description)
    
for i in range (0,4):
    top_headlines.append(all_headlines[i])
    
#######

## url2
## all headlines
for source in news_sources2:
    all_headline = scrape_all_headlines(source)
    all_headlines_list.extend(all_headline)

### News headlines
for i in range(5, 8):
    news_headlines.append(all_headlines_list[i])

### Sports headlines
for i in range(8, 11):
    sports_headlines.append(all_headlines_list[i])
    
### India News headlines
for i in range(11, 15):
    india_news_headlines.append(all_headlines_list[i])

### Author's Picks
for i in range(16, 22):
    authors_picks_headlines.append(all_headlines_list[i])


@app.route('/')
def index():
    return render_template('index.html', top_headlines=top_headlines, top_headlines_description=top_headlines_description, top_headlines_images=top_headlines_images)

if __name__ == '__main__':
    app.run(debug=True)
