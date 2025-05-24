import requests
from bs4 import BeautifulSoup
import json

URL = 'https://kishanptl34.github.io/kishan-goyani-portfolio/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

h1_text = soup.find('h1').text.strip()

with open('scraped_data.json', 'w') as json_file:
    json.dump({'h1_heading': h1_text}, json_file, indent=2)

with open('scraped_data.txt', 'w') as txt_file:
    txt_file.write(h1_text)

print("Scraped and saved:", h1_text)