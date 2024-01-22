from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

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
url2 = 'https://www.bbc.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get(url2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(0.1)
html_content = driver.page_source
driver.quit()

soup2 = BeautifulSoup(html_content, 'html5lib')

# for url
all_headlines = []
top_headlines = []
top_headlines_description = []
top_headlines_images = []
latest_images = []
latest_headlines = []
latest_descriptions = []
all_top_href = []
new_top_href = []

# for url2
all_images_list = []
all_headlines_list = []
all_descriptions_list = []
news_images = []
sports_images = []
india_news_images = []
authors_picks_images = []
news_headlines = []
sports_headlines = []
india_news_headlines = []
authors_picks_headlines = []
news_descriptions = []
sports_descriptions = []
india_news_descriptions = []
authors_picks_descriptions = []
all_href_list = []
news_href = []
sports_href = []
india_news_href = []
authors_picks_href = []

# defs of url
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

def scrape_top_href(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_descriptions = soup.find_all('a', class_='css-1u3p7j1')
    return all_descriptions

# def of url2
def scrape_all_headlines(url2):
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_headlines = soup.find_all('a', class_='media__link')
    return [all_headline.text.strip() for all_headline in all_headlines]

def scrape_all_href(url2):
    response = requests.get(url2)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_descriptions = soup.find_all('a', class_='media__link')
    return all_descriptions

def scrape_all_descriptions(url2):
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_descriptions = soup.find_all('p', class_='media__summary')
    return [all_description.text.strip() for all_description in all_descriptions]

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
    
for i in scrape_top_href(url):
    all_top_href.append(i['href'])
    
for i in range(1, 4):
    new_top_href.append("https://www.nytimes.com"+all_top_href[i])
    
new_top_href.insert(0, all_top_href[0])
    
#######

## url2
## all images
#################

all_images = soup2.find_all('img', class_='image-replace')
for image_tag in all_images:
    all_images_list.append(image_tag['src'])
    
### News images
for i in range(5, 8):
    news_images.append(all_images_list[i])
    
### Sport images
for i in range(8, 11):
    sports_images.append(all_images_list[i])

### India News images
for i in range(15, 19):
    india_news_images.append(all_images_list[i])

### Authors Picks images
for i in range(20, 26):
    authors_picks_images.append(all_images_list[i])
    

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

### Author's Picks headlines
for i in range(16, 22):
    authors_picks_headlines.append(all_headlines_list[i])

## all hrefs
for i in scrape_all_href(url2):
    all_href_list.append(i['href'])
    
### News hrefs
for i in range(5, 8):
    news_href.append('https://www.bbc.com'+all_href_list[i])

### Sport hrefs
for i in range(8, 11):
    sports_href.append('https://www.bbc.com'+all_href_list[i])

### India News hrefs
for i in range(11, 15):
    india_news_href.append('https://www.bbc.com'+all_href_list[i])

### Author's Picks hrefs
for i in range(16, 22):
    authors_picks_href.append(all_href_list[i])

## all descriptions
for source in news_sources2:
    all_description = scrape_all_descriptions(source)
    all_descriptions_list.extend(all_description)

### News descriptions
for i in range(1, 4):
    news_descriptions.append(all_descriptions_list[i])

### Sports descriptions
for i in range(4, 7):
    sports_descriptions.append(all_descriptions_list[i])

### India News descriptions
for i in range(7, 11):
    india_news_descriptions.append(all_descriptions_list[i])

### Author's Picks descriptions
for i in range(12, 18):
    authors_picks_descriptions.append(all_descriptions_list[i])
    
    

@app.route('/')
def index():
    return render_template('index.html', top_headlines=top_headlines, top_headlines_description=top_headlines_description, top_headlines_images=top_headlines_images, new_top_href=new_top_href, news_headlines=news_headlines, sports_headlines=sports_headlines, india_news_headlines=india_news_headlines, authors_picks_headlines=authors_picks_headlines, news_images=news_images, sports_images=sports_images, india_news_images=india_news_images, authors_picks_images=authors_picks_images, news_href=news_href, sports_href=sports_href, india_news_href=india_news_href, authors_picks_href=authors_picks_href, news_descriptions=news_descriptions, sports_descriptions=sports_descriptions, india_news_descriptions=india_news_descriptions, authors_picks_descriptions=authors_picks_descriptions)

if __name__ == '__main__':
    app.run(debug=True)
