import time

import utils
from provider import Provider


def known_working():
    utils.log("Begin vax search")

    giant = Provider("Giant Foods Stores",
                     "Please check back later",
                     "https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory")

    six_flags = Provider("6 Flags America",
                         "Please continue to check this site for updates about appointment availability",
                         "https://www.arcgis.com/sharing/rest/content/items/4b361dcb49464fcda4fd27428c3a50e3/data?f"
                         "=json")

    riteaid = Provider("Rite Aid", "but is not currently able to schedule appointments",
                       "https://www.riteaid.com/Covid-19")

    walgreens = Provider("Walgreens", "", "")

    # gbmc = Provider("GBMC", "No appointments currently available", "https://www.gbmc.org/covid-vaccine")

    # adventist = Provider("Adventist Health",
    #                      "null",
    #                      "https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/")

    # shoprite = Provider("Shoprite NJ", "There are currently no COVID-19 vaccine appointments available. Please check "
    #                                    "back later. We appreciate your patience as we open as many appointments as "
    #                                    "possible. Thank you.",
    #                     "https://covidinfo.reportsonline.com/covidinfo/ShopRite.html")

    # mercy = Provider("Mercy Medical",
    #                  "Vaccine appointments may not be scheduled online or via MyChart",
    #                  "https://mdmercy.com/news-and-events/updates-for-patients-and-visitors/vaccine-faqs?sc_lang=en")

    # hackensack = Provider("Hackensack Meridian Health", "All appointments currently are full. We hope to schedule "
    #                                                     "again as more vaccines are received. Thank you for your "
    #                                                     "patience. Please continue to check back",
    #                       'https://www.hackensackmeridianhealth.org/covid19/')

    # chemed_oc_nj = Provider("CHEMED Health Center", "At this time, CHEMED Health Center does not have available first dose vaccine supplies. We are therefore not currently taking appointments for first doses", "https://www.chemedhealth.org/news/519/covid-vaccine-scheduling-information/")

    # penn = Provider("Penn Med", "At this time, all appointments for the COVID-19 Vaccine have been filled", "https://www.princetonhcs.org/")

    # Maryland

    # adventist.adventist_act(channel='maryland')
    six_flags.act(channel='maryland')
    giant.act(channel='maryland')
    # mercy.act(channel='maryland')
    # gbmc.act(channel='maryland')
    walgreens.walgreens_act(21202, channel='maryland')
    time.sleep(20)
    walgreens.walgreens_act(21702, channel='maryland')
    time.sleep(20)
    walgreens.walgreens_act(21401, channel='maryland')
    md_rite_aid_stores = {
        "2204": "Foster Ave Baltimore",
        "00349": "Park Heights Ave",
        "2210":"Sulpher Spring Road",
        "383":"Ebenezer Road",
    }
    for store in md_rite_aid_stores.keys():
        num = store
        name = md_rite_aid_stores[store]
        riteaid.rite_aid_act(store_number=num, store_name=name, channel="maryland")

    # New Jersey
    # penn.act(channel='new jersey')
    # shoprite.act(channel="new jersey")
    # hackensack.act(channel="new jersey")
    # walgreens.allentown_nj_walgreens_act(channel="new jersey")
    # chemed_oc_nj.act(channel="new jersey")
    # nj_rite_aid_stores = {"10505":"Robbinsville, NJ",
    #                       "01326": "Trenton, NJ",
    #                       "02526": "Wrightstown, NJ",
    #                       "07830": "Burlington, NJ",
    #                       "11115": "Morrisville, NJ",
    #                       "11106": "Fairless Hills, NJ",
    #                       "00850": "Levittown, NJ",
    #                       "03483": "Browns Mills, NJ",
    #                       "04879": "Burlington, NJ",
    #                       "10496": "Jackson, NJ",
    #                       "02521": "Lumberton, NJ",
    #                       "00135": "Willingboro, NJ",
    #                       "10517": "Whiting, NJ",
    #                       "02707":"Toms River",
    #                       "02527":"Manchester",
    #                       "10515":"Toms River",
    #                       "10513":"Toms River",
    #                       "03573":"Beachwood",
    #                       "10514":"Toms River",
    #                       "02522":"Bayville",
    #                       }
    # for store in nj_rite_aid_stores.keys():
    #     num = store
    #     name = nj_rite_aid_stores[store]
    #     riteaid.rite_aid_act(store_number=num, store_name=name, channel="new jersey")

    utils.log("End vax search")


def obsolete():
    pass


def development(channel="debug"):
    pass


if __name__ == '__main__':
    known_working()
