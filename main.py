import time

import utils
from provider import Provider

# https://www.marylandvax.org/clinic/search?service%5B%5D=Vaccination&location=Prince+George%27s+County%2C+MD%2C+USA&search_radius=100%2B+miles&search_name=&search_date=&commit=Search#search_results

def known_working():
    utils.log("Begin vax search")

    holycross = Provider("Holy Cross Hospital", "Holy Cross Health will release the date of our next COVID-19 vaccine clinics today, Feb. 1 at 4 p.m", "https://www.holycrosshealth.org/health-and-wellness/covid-19-vaccine/schedule-appointment")
#    holycross.act(debug=True)

    gbmc = Provider("GBMC", "No appointments currently available", "https://www.gbmc.org/covid-vaccine")
    gbmc.act()


    adventist = Provider("Adventist Health", "null", "https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/")
    adventist.adventist_act()







    mercy = Provider("Mercy Medical", "Vaccine appointments may not be scheduled online or via MyChart", "https://mdmercy.com/news-and-events/updates-for-patients-and-visitors/vaccine-faqs?sc_lang=en")
    mercy.act()


    giant = Provider("Giant Foods Stores",
                     "Please check back later",
                     "https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory")
    giant.act(debug=True)

    six_flags = Provider("6 Flags America", "Please continue to check this site for updates about appointment availability", "https://www.arcgis.com/sharing/rest/content/items/4b361dcb49464fcda4fd27428c3a50e3/data?f=json")
    six_flags.act()

    # cvs = Provider("CVS Pharmacy", "The COVID-19 vaccine is not yet available at CVS Pharmacy in Maryland.", "https://www.cvs.com/bizcontent/marketing/covidvaccine_landingpage/acn-tool.js")
    # cvs.act()

    riteaid = Provider("Rite Aid", "but is not currently able to schedule appointments", "https://www.riteaid.com/Covid-19")
    riteaid.act(debug=True)

    time.sleep(3)
    utils.log("End vax search")


def obsolete():
    # garrett = Provider("Garrett Co.", "THERE ARE NO APPOINTMENTS AVAILABLE AT THIS TIME", "https://health.maryland.gov/allegany/Pages/COVIDVaccination.aspx")
    # stagnes = Provider("St. Agnes", "Due to overwhelming demand Ascension Saint Agnes has no vaccination appointments available at this time", "https://healthcare.ascension.org/COVID-19/vaccinations")
    pass


def development(debug=True):
    pass


if __name__ == '__main__':
    known_working()