import time

import utils
from provider import Provider


def known_working():
    utils.log("Begin vax search")

    gbmc = Provider("GBMC", "No appointments currently available", "https://www.gbmc.org/covid-vaccine")

    adventist = Provider("Adventist Health",
                         "null",
                         "https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/")


    mercy = Provider("Mercy Medical",
                     "Vaccine appointments may not be scheduled online or via MyChart",
                     "https://mdmercy.com/news-and-events/updates-for-patients-and-visitors/vaccine-faqs?sc_lang=en")

    giant = Provider("Giant Foods Stores",
                     "Please check back later",
                     "https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory")

    six_flags = Provider("6 Flags America",
                         "Please continue to check this site for updates about appointment availability",
                         "https://www.arcgis.com/sharing/rest/content/items/4b361dcb49464fcda4fd27428c3a50e3/data?f"
                         "=json")

    riteaid = Provider("Rite Aid", "but is not currently able to schedule appointments",
                       "https://www.riteaid.com/Covid-19")

    shoprite = Provider("Shoprite NJ", "There are currently no COVID-19 vaccine appointments available. Please check "
                                       "back later. We appreciate your patience as we open as many appointments as "
                                       "possible. Thank you.",
                        "https://covidinfo.reportsonline.com/covidinfo/ShopRite.html")
    walgreens = Provider("Walgreens", "", "")

    hackensack = Provider("Hackensack Meridian Health", "All appointments currently are full. We hope to schedule "
                                                        "again as more vaccines are received. Thank you for your "
                                                        "patience. Please continue to check back",
                          'https://www.hackensackmeridianhealth.org/covid19/')

    chemed_oc_nj = Provider("CHEMED Health Center", "At this time, CHEMED Health Center does not have available first dose vaccine supplies. We are therefore not currently taking appointments for first doses", "https://www.chemedhealth.org/news/519/covid-vaccine-scheduling-information/")

    # Maryland

    adventist.adventist_act()
    six_flags.act()
    giant.act(debug=True)
    mercy.act()
    gbmc.act()
    walgreens.walgreens_act(21202, debug_flag=True)
    time.sleep(20)
    walgreens.walgreens_act(21702, debug_flag=True)
    time.sleep(20)
    walgreens.walgreens_act(21401, debug_flag=True)
    time.sleep(20)
    walgreens.walgreens_act(95482, debug_flag=True)
    md_rite_aid_stores = {
        "11213":"York Road South",
        "02214":"Smith Ave",
        "04686":"Pikesville",
        "00349":"Park Heights Ave",
        "00362":"Northern Pkwy",
        "03871":"Owings Mills",
        "00390":"Randallstown",
    }
    for store in md_rite_aid_stores.keys():
        num = store
        name = md_rite_aid_stores[store]
        riteaid.rite_aid_act(store_number=num, store_name=name, debug=True)



    # New Jersey
    shoprite.act(debug=True)
    hackensack.act(debug=True)
    walgreens.allentown_nj_walgreens_act(debug_flag=True)
    chemed_oc_nj.act(debug=True)
    nj_rite_aid_stores = {"10505":"Robbinsville, NJ",
                          "01326": "Trenton, NJ",
                          "02526": "Wrightstown, NJ",
                          "07830": "Burlington, NJ",
                          "11115": "Morrisville, NJ",
                          "11106": "Fairless Hills, NJ",
                          "00850": "Levittown, NJ",
                          "03483": "Browns Mills, NJ",
                          "04879": "Burlington, NJ",
                          "10496": "Jackson, NJ",
                          "02521": "Lumberton, NJ",
                          "00135": "Willingboro, NJ",
                          "10517": "Whiting, NJ",
                          }
    for store in nj_rite_aid_stores.keys():
        num = store
        name = nj_rite_aid_stores[store]
        riteaid.rite_aid_act(store_number=num, store_name=name, debug=True)

    utils.log("End vax search")


def obsolete():
    pass


def development(debug=True):
    pass


if __name__ == '__main__':
    known_working()
