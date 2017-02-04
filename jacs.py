from bs4 import BeautifulSoup
import urllib2
import time
from multiprocessing import Pool, Process
from itertools import islice

jacs_pages = open('jacs.txt', 'r').read().splitlines()

max_workers = 9

def scrape(page):
  with open('text/' + page.split("/")[-1].replace("html", "txt"), 'w') as f:
    id_num = 61  
    html = urllib2.urlopen(page).read()
    print "Reading in " + page
    soup = BeautifulSoup(html, 'html.parser')
    
    soupfind = soup.find('div', {'id': 'd' + str(id_num)})
    while soupfind:
      f.write(soupfind.getText().strip().encode('ascii', 'ignore') + '\n')
      id_num += 1
      soupfind = soup.find('div', {'id': 'd' + str(id_num)})

pool = Pool(processes=max_workers)
pool.map(scrape, jacs_pages)
