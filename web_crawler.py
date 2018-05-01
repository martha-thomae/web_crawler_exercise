# Create a Python program that crawls a web page by downloading the page 
# and all HTML pages that are linked from that page. The crawler should 
# continue following links recursively, up to a certain depth.

# Parameters:
# start_url
# max_depth (max. crawling depth)
# page download time-out
# whether to limit crawling only to the original page's domain

import requests
from lxml import html

start_url = "http://econpy.pythonanywhere.com/ex/001.html"
page = requests.get(start_url)
tree = html.fromstring(page.content)
html_refs = tree.xpath('//a[@href]')

urls = [ref.get('href') for ref in html_refs]

print(urls)