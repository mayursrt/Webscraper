

# Webscraper
Get useful tech news by scraping hackernews.
The site [Hackernews](https://news.ycombinator.com/news) has some wonderful news articles. This program scrapes all the news from this site filtering them with upvotes.<br>
How to use:
1. Install necessary packages:

		pip install beautifulsoup4
		pip install pprint
	Read beautifulsoup documentation [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. Edit the script and mention number of pages to be scraped. (default is 4 pages)
3. Run the script. It doesn't matter the location.
eg:

		python scrape.py
Note: It will only show the news which have more than 100 votes. You can tweak that in the script.
