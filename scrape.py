import requests
from bs4 import BeautifulSoup
import pprint

def url():
	mega_links = []
	mega_subtext = []
	for page in range(1,4):
		res = requests.get('https://news.ycombinator.com/news?p=' + str(page))
		soup = BeautifulSoup(res.text, 'html.parser')

		links = soup.select('.storylink')
		for x in links:
			mega_links.append(x)
		
		subtext = soup.select('.subtext')
		for y in subtext:
			mega_subtext.append(y)

	return mega_links, mega_subtext
links, subtext = url()

def sort_stories(hnlist):
	return sorted(hnlist, key= lambda k:k['Votes'], reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):

		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points>99:
				hn.append({'Title': title, 'Link': href, 'Votes': points})
	return sort_stories(hn)

pprint.pprint(create_custom_hn(links, subtext))