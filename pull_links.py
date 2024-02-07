
#This file first pulls elements from a json input file, it then uses beautiful soup to scrape the profile page of each person 
#it then prints a json that includes all links to papers for each person


#Run using the following command:
# python3 pullprofilelinks.py > output.json

import json
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#pull json data
input_filename = 'profilepage.json'  
with open(input_filename, 'r') as infile:
    data = json.load(infile)

name_array = []
link_array = []
affil_array = []

for entry in data:
    link = entry.get('link')
    link_array.append(link)

    name = entry.get('name')
    name_array.append(name)

    affil = entry.get('affiliations')
    affil_array.append(affil)

    # if link:  
    #     print(name + '\n')
    #     print(link + '\n')



pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

big_df = pd.DataFrame()
headers = {
    'accept-language': 'en-US,en;q=0.9',
    'x-requested-with': 'XHR',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
s = requests.Session()
s.headers.update(headers)

payload = {'json': '1'}

result = []
i = 0
for x in link_array:
    url = x

    r = s.post(url, data=payload)
    soup = bs(r.json()['B'], 'html.parser')
    works = [(x.get_text(), 'https://scholar.google.com' + x.get('href')) for x in soup.select('a') if 'javascript:void(0)' not in x.get('href') and len(x.get_text()) > 7]
    df = pd.DataFrame(works, columns=['Paper', 'Link'])
    #creat new json with links included
    result.append({
        'name': name_array[i], 
        'affiliations': affil_array[i],
        'links': [{'name': row[0], 'link': row[1]} for row in works]
    })
    i = i + 1

#print all info
print(json.dumps(result, indent=4))






