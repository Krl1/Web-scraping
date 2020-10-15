from lxml import html
from datetime import date
import requests
import re


def priceStrToNumber(text):
    return float(text[0][0:6].replace(',', '.'))


today = date.today()
data = today.strftime('%d-%m-%Y')

items = []
items.append('https://www.skalnik.pl/namiot-cloud-up-2-20d-light-grey-red-naturehike-665608')
items.append('https://www.skalnik.pl/namiot-cloud-up-2-20d-updated-nh17t001-t-mustard-green-678946')

for item in items:
    page = requests.get(item)
    tree = html.fromstring(page.text)

    nrOfItem = item[-6:]
    xpathOut = '//*[@id="product-price-' + nrOfItem + '"]/span/text()'
    xpathIn = '//*[@id="old-price-' + nrOfItem + '"]/span/text()'

    textOut = tree.xpath(xpathOut)
    textIn = tree.xpath(xpathIn)

    textOut = priceStrToNumber(textOut)
    try:
        textIn = priceStrToNumber(textIn)
    except IndexError:
        textIn = textOut

    print(data, ': ', textIn, ' -> ', textOut)
 

