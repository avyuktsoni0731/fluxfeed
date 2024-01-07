from flask import Flask, render_template

app = Flask(__name__)

# Your news aggregator code here (steps 2-6 from the previous answer)

import requests
from bs4 import BeautifulSoup

news_sources = [
    'https://www.nytimes.com/section/world'
]

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

def scrape_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    images_scraped = soup.find_all('img')
    for item in images_scraped:
        print(item['src'])
    


all_headlines = []
top_headlines = []
top_headlines_description = []

# for source in news_sources:
#     headlines = scrape_headlines(source)
#     top_headlines.extend(headlines)
    
for source in news_sources:
    headlines = scrape_headlines(source)
    all_headlines.extend(headlines)
    
for source in news_sources:
    description = scrape_descriptions(source)
    top_headlines_description.extend(description)
    
for i in range (0,4):
    top_headlines.append(all_headlines[i])

# for i, headline in enumerate(top_headlines, start=1):
#     print(f"{i}.{headline}")
    
# for i, description in enumerate(top_headlines_description, start=1):
#     print(f"{i}.{description}")


@app.route('/')
def index():
    return render_template('index.html', top_headlines=top_headlines, top_headlines_description=top_headlines_description)

if __name__ == '__main__':
    app.run(debug=True)
