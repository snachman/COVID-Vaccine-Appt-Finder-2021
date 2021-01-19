import time

import utils
from provider import Provider

# https://www.marylandvax.org/clinic/search?service%5B%5D=Vaccination&location=Prince+George%27s+County%2C+MD%2C+USA&search_radius=100%2B+miles&search_name=&search_date=&commit=Search#search_results

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
    # giant = Provider("Giant Foods", "The following Giant Food locations will provide vaccinations to those who are eligible. Continue to check this site. More information will be provided as it becomes available", "https://coronavirus.maryland.gov/pages/maryland-retail-vaccination-sites")
    # giant.act()
    calvert = Provider("Calvert Co.", "The pre-registration vaccine portal will open at 10 a.m. on Tuesday, Jan. 19, 2021", "https://www.calvertcountymd.gov/Vaccine")
    calvert.act()
    fred = Provider("Frederick Co.", "All Clinics currently full, check back on Tues. Jan. 19", "https://health.frederickcountymd.gov/629/COVID-19-Vaccine")
    fred.act()
    time.sleep(3)
    utils.log("End vax search")
