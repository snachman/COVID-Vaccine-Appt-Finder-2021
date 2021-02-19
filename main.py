import time

import utils
from provider import Provider

# https://www.marylandvax.org/clinic/search?service%5B%5D=Vaccination&location=Prince+George%27s+County%2C+MD%2C+USA&search_radius=100%2B+miles&search_name=&search_date=&commit=Search#search_results


def known_working():
    utils.log("Begin vax search")

    gbmc = Provider("GBMC", "No appointments currently available", "https://www.gbmc.org/covid-vaccine")
    gbmc.act()

    adventist = Provider("Adventist Health",
                         "null",
                         "https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/")
    adventist.adventist_act()

    mercy = Provider("Mercy Medical",
                     "Vaccine appointments may not be scheduled online or via MyChart",
                     "https://mdmercy.com/news-and-events/updates-for-patients-and-visitors/vaccine-faqs?sc_lang=en")
    mercy.act()

    giant = Provider("Giant Foods Stores",
                     "Please check back later",
                     "https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory")
    giant.act(debug=True)

    six_flags = Provider("6 Flags America",
                         "Please continue to check this site for updates about appointment availability",
                         "https://www.arcgis.com/sharing/rest/content/items/4b361dcb49464fcda4fd27428c3a50e3/data?f"
                         "=json")
    six_flags.act()

    riteaid = Provider("Rite Aid", "but is not currently able to schedule appointments",
                       "https://www.riteaid.com/Covid-19")
    riteaid.act(debug=True)

    shoprite = Provider("Shoprite NJ", "There are currently no COVID-19 vaccine appointments available. Please check "
                                       "back later. We appreciate your patience as we open as many appointments as "
                                       "possible. Thank you.",
                        "https://covidinfo.reportsonline.com/covidinfo/ShopRite.html")
    shoprite.act(debug=True)

    # cvs = Provider("CVS Pharmacy", "", "")
    # cvs.cvs_act(debug_flag=True)

    walgreens = Provider("Walgreens", "", "")
    walgreens.walgreens_act(21202, debug_flag=True)
    time.sleep(10)
    walgreens.walgreens_act(21702, debug_flag=True)
    time.sleep(10)
    walgreens.walgreens_act(21401, debug_flag=True)
    walgreens.jersey_walgreens_act(debug_flag=True)

    hackensack = Provider("Hackensack Meridian Health", "All appointments currently are full. We hope to schedule "
                                                        "again as more vaccines are received. Thank you for your "
                                                        "patience. Please continue to check back",
                          'https://www.hackensackmeridianhealth.org/covid19/')
    hackensack.act(debug=True)

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
