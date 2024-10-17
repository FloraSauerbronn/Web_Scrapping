# Web Scraping Tutorial with Scrapy

Welcome to the **Web Scraping with Scrapy** tutorial! This tutorial will guide you through the process of extracting data from websites using Scrapy, a powerful and efficient Python framework for web scraping.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [webscraping_superbasico.py](#webscraping_superbasico.py)
- [Project Setup](#project-setup)
- [Creating a Spider](#creating-a-spider)
- [Running the Spider](#running-the-spider)
- [Exporting Data](#exporting-data)


---

## Introduction

Web scraping is the process of automatically collecting information from websites. **Scrapy** is a popular Python framework that simplifies web scraping by providing tools to extract, process, and store data efficiently.

In this tutorial, you'll learn how to:
1. Set up a Scrapy project.
2. Create a spider to crawl a website.
3. Extract data from web pages.
4. Export the scraped data into different formats (e.g., CSV, JSON).

## Installation

Before starting, make sure you have Python installed. To install Scrapy, run the following command:

```bash
pip install scrapy

## webscraping_superbasico.py
This file is a simple python script notebook, that was creates in onw of my classes. The moast simple crawler for extracting
headlines from website. In this case it was used to extract head lines, date, location and details from enviromental news
from the government website GOV.BR.

## Project Setup

### Create a Scrapy project:

Run the following command in your terminal to create a new Scrapy project:

```bash
scrapy startproject web_scraping_tutorial

Inside the spiders/ directory, create a new file called gov_news_spider.py and add the code from the webscraping_superbasico.py example.

## Creating a Spider
In Scrapy, a spider is a class that defines how to follow links and extract data from web pages. We already created the spider in the previous step, but here’s a breakdown of how it works:

start_urls: This defines the website where the spider will begin scraping.
parse: This method processes the response from the website and extracts the relevant data.

## Running the Spider
To run the spider and start scraping data, use the following command:

```bash
Copiar código
scrapy crawl gov_news
This will start the scraping process, and you should see the data (headlines, dates, locations, and details) being extracted in the terminal.

## Exporting Data
You can easily export the scraped data into different formats such as JSON or CSV. For example, to export the data into a JSON file, run:

```bash
Copiar código
scrapy crawl gov_news -o news_data.json
This will save the extracted data in news_data.json.

### For CSV format:

bash
Copiar código
scrapy crawl gov_news -o news_data.csv
Conclusion
In this tutorial, you learned how to:

Install and set up a Scrapy project.
Create a spider to extract data from a government news website.
Export the scraped data into useful formats like JSON and CSV.
Scrapy is a versatile tool, and with this basic foundation, you can explore more advanced features such as following links, handling pagination, and using Scrapy's powerful pipeline system to clean and process the data.

Happy scraping!

