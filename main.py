import time

import utils
from provider import Provider


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

    walgreens = Provider("Walgreens", "", "")
    walgreens.walgreens_act(21202, debug_flag=True)
    time.sleep(10)
    walgreens.walgreens_act(21702, debug_flag=True)
    time.sleep(10)
    walgreens.walgreens_act(21401, debug_flag=True)
    walgreens.allentown_nj_walgreens_act(debug_flag=True)

    hackensack = Provider("Hackensack Meridian Health", "All appointments currently are full. We hope to schedule "
                                                        "again as more vaccines are received. Thank you for your "
                                                        "patience. Please continue to check back",
                          'https://www.hackensackmeridianhealth.org/covid19/')
    hackensack.act(debug=True)

    time.sleep(3)
    utils.log("End vax search")


def obsolete():
    pass


def development(debug=True):
    pass


if __name__ == '__main__':
    known_working()
