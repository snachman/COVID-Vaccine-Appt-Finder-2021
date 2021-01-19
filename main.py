import time

import utils
from provider import Provider

# https://www.marylandvax.org/clinic/search?service%5B%5D=Vaccination&location=Prince+George%27s+County%2C+MD%2C+USA&search_radius=100%2B+miles&search_name=&search_date=&commit=Search#search_results
# https://www.gbmc.org/covid-vaccine

if __name__ == '__main__':
    utils.log("Begin vax search")
    stagnes = Provider("St. Agnes", "Due to overwhelming demand Ascension Saint Agnes has no vaccination appointments available at this time", "https://healthcare.ascension.org/COVID-19/vaccinations")
    stagnes.act()
    umms = Provider("UMMS", "Please check back here Monday, January 18 for more details", "https://www.umms.org/coronavirus/covid-vaccine/get-vaccine")
    # umms.act()
    gbmc = Provider("GBMC", "All available slots filled. Check back soon!", "https://www.gbmc.org/covid-vaccine")
    gbmc.act()
    garrett = Provider("Garrett Co.", "THERE ARE NO APPOINTMENTS AVAILABLE AT THIS TIME", "https://health.maryland.gov/allegany/Pages/COVIDVaccination.aspx")
    garrett.act()
    time.sleep(3)
    utils.log("End vax search")
