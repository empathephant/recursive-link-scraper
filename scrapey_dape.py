import requests as r
import os
import time
import random

from bs4 import BeautifulSoup

headers = {'user-agent': 'Shanti der Blatter (empathephant@gmail.com)'}

reynolds_url = "http://reynoldsnlp.com/scrape/aa.html"

foundURLs = set()

if not os.path.isdir("all_pages"):
    os.makedirs("all_pages");

def find_links(filename):

    print('making soup for ' + filename)
    f = open(os.path.join('all_pages', filename))
    html_to_parse = f.read()
    soup = BeautifulSoup(html_to_parse, "html5lib")

    time.sleep(random.uniform(1.5, 2.5))
    print('finding links in ' + filename)
    for link in soup.find_all('a'):
        if link.get('href') not in foundURLs:
            print("I found " + link.get('href')[-7:])
            foundURLs.add(link.get('href'))
            scrape_link(link.get('href'))
        else:
            print(link.get('href')[-7:] + ' is already in the list')
    f.close()

def scrape_link(url):

    page_body = r.get(url, headers=headers)
    filename = url[-7:]
    full_html = open(os.path.join("all_pages", filename),"w+")
    full_html.write(page_body.text)
    full_html.close()
    print("calling find links on " + filename)
    find_links(filename)

userInput = input("Paste a URL here to scrape, or type 'r' to use Dr. Reynolds site: ")
if (userInput == 'r'):
    scrape_link(reynolds_url)
else:
    scrape_link(userInput)
print("All links scraped.")
