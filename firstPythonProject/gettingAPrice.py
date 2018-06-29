import bs4, requests

def getEmpikPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser') #html parsing module
    elems = soup.select('#sellerNavBox-0 > div > div > div.productPriceInfo__price.withoutLpPromo > div.productPriceInfo__content.ta-price')
    return elems[0].text.strip() #removing white spaces, slashes n etc


price = getEmpikPrice('http://www.empik.com/automate-the-boring-stuff-with-python-sweigart-albert,p1104961024,ksiazka-p')
print('The price is: ' + str(price))

