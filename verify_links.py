#!/usr/bin/env python3
''' This program fetch the links from the given url and displays the list of links which returns 404
    Example input url :https://automatetheboringstuff.com/chapter11/
'''

import requests
import bs4
import sys

def process_links(links):
    for link in links:
        try:
            link_item = link['href']
            if link_item.startswith('http'):
                to_check = link_item

            elif link_item.startswith('//'):
                to_check = 'https:' + link_item

            elif link_item.startswith('#'):
                to_check = url + link_item

            result = requests.get(to_check)

            if result.status_code == 404:
                dead_links.append(to_check)

        except:
                pass

url = input('Please enter the URL which needs to be parsed: ')

try :
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    links = soup.select('a')
    dead_links = []   
    process_links(links)

    print('Following ' + str(len(dead_links)) + ' links returned error 404:')
    print('\n'.join(dead_links))
 
except:
    sys.exit("Invaid url")

