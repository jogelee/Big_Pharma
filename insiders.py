# insiders.py web scrapes SEC EDGAR for recent executive insider transactions
# currently geared for big name C19 vaccine developers, but the input file can be changed to track any company's executives
# by John Lee

import requests
from bs4 import BeautifulSoup
import csv
from csv import reader
import os
from datetime import date

os.chdir('C:\\Users\\jogel\\Desktop\\insiders')

tickers = {'PFE': 'PFIZER INC', 'MRNA': 'Moderna, Inc.', 'INO': 'INOVIO PHARMACEUTICALS, INC.', 'JNJ': 'JOHNSON & JOHNSON', 'NVAX': 'NOVAVAX INC'}

timeframe = int(input('Look back how many days?: '))

# read csv as a list of lists
with open('BIG_PHARMA.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    execs = list(csv_reader)

master = []

# web scraper
for exec in execs[1:]:
    url = exec[3]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id = 'transaction-report')
    elems = results.find_all('td')
    count = 0
    row = [exec[0], exec[1], exec[2], exec[3]]

    for elem in elems:
        if count % 12 == 0:
            row.append(elem.text)
        elif count % 12 == 1:
            row.append(elem.text)
        elif count % 12 == 3:
            row.append(elem.text)
        elif count % 12 == 7:
            row.append(elem.text)
        elif count % 12 == 11:
            row.append(elem.text)
        if len(row) == 9:
            dt_str = row[5]
            if dt_str != '-':
                dt = date(*map(int, dt_str.split('-')))
                if (date.today() - dt).days <= timeframe:
                    if tickers[row[0]] == row[6]:
                        master.append(row)
            row = [exec[0], exec[1], exec[2], exec[3]]
        count += 1

master.insert(0, ['ticker', 'name', 'position', 'SEC_url', 'A/D', 'date', 'issuer', 'transacted', 'type'])

# output csv
with open(str(date.today()) + '.csv', 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(master)

csv_file.close()
