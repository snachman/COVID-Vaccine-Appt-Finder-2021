import requests
from provider import Provider

if __name__ == '__main__':
    stagnes = Provider("St. Agnes", "Due to overwhelming demand Ascension Saint Agnes has no vaccination appointments available at this time", "https://healthcare.ascension.org/COVID-19/vaccinations")
    stagnes.act()