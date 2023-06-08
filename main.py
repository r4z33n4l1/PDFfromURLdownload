import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://www.physicsandmathstutor.com/a-level-maths-papers/c3-edexcel/"

# If there is no such folder, the script will create one automatically
folder_location = r'pdfs'
if not os.path.exists(folder_location):
    os.mkdir(folder_location)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the list of all links
pdf_links = soup.select("a[href$='.pdf']")[6:]

# Get the total number of pdfs
total_pdfs = len(pdf_links)

print('Starting download of {} PDFs'.format(total_pdfs))

for index, link in enumerate(pdf_links, start=1):
    # Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location, link['href'].split('/')[-1])

    # Log the current progress
    print('Downloading {} of {}: {}'.format(index, total_pdfs, filename))

    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url, link['href'])).content)

print('Download completed.')
