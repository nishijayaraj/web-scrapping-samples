#!/usr/bin/env python3

"""Download jpg/png images from Imgur that match a user's search term(s)."""

import os
import requests
import bs4
from pathlib import Path

def download_image(extension):
    """Search for and download all images of the argument type from Imgur."""
    home = str(Path.home())
    url = f'http://imgur.com/search?q={search}&ext=${extension}'
    print(url)
    os.makedirs(f'{home}/Downloads/imgur', exist_ok=True)

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image_elem = soup.select('.post > .image-list-link img')

    for i, image in enumerate(image_elem):
        
         image_url = 'https:' + image_elem[i].get('src')
         print(image_url)
         print('Downloading image {}'.format(image_url))
         res = requests.get(image_url)
         res.raise_for_status()
         img = open(os.path.join(f'{home}/Downloads/imgur',
                                     os.path.basename(image_url)), 'wb')
         for data in res.iter_content(1000000):
             img.write(data)
         img.close()

    return len(image_elem)


search = input('Enter desired search term(s): ')
downloaded_files = download_image('jpg')

if downloaded_files == 0:
    print('No images found.')

else:
    print('All ' + str(downloaded_files) + ' files successfully downloaded.')
