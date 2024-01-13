# FluxFeed - Your Personalized News Aggregator

<p align="center">
  <img src="https://github.com/avyuktsoni0731/fluxfeed/blob/main/assets/fluxfeed_banner.png" alt="FluxFeed Banner" width="600px">
</p>

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

- FluxFeed is a dynamic web-based news aggregator that empowers users to stay informed with the latest headlines, from diverse news sources, which keeps on updating every few seconds as the news on the source website gets updated. It uses Python, HTML, CSS, JavaScript, and the Flask web framework. FluxFeed not only delivers top headlines but also offers curated sections and a user-friendly interface.

- This is a web-scrapping project that extracts the latest news headlines from the top news providers around the world, namely **The New York Times** and **BBC**.

- Used multiple Python libraries like BeautifulSoup (for scraping images, headlines, and news descriptions from News Websites), Selenium WebDriver (for automation/opening a webpage for an instance in the background at the initiation and parsing the data into a Soup for aggregation), Time module (for sleeping the webpage for a while to extracting data into a Soup), Requests module, render_template, etc.

<p align="center">
  <img src="https://github.com/avyuktsoni0731/fluxfeed/blob/main/assets/fluxfeed_landing.png" alt="FluxFeed Banner" width="1000px">
</p>

## Features

- **Top Headlines:** Instantly access breaking news from around the globe.
- **Categorized Sections:** Dive deeper into specific areas of interest, including sports news, India news, and editor's picks.
- **Responsive Design:** (Under Work)

## Demo

**YouTube link to video demo->** [Link](https://youtu.be/gHkhUAnaXRo)

## Getting Started

### Prerequisites

- Python (3.x)
- Flask (`pip install Flask`)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/avyuktsoni0731/fluxfeed
2. **Check into FluxFeed directory & Open VS Code (preferably)**
   ```bash
   cd fluxfeed
   code .
3. **Run the Flask**
   ```bash
   python3 app.py
