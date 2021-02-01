import time

import utils
from provider import Provider

# https://www.marylandvax.org/clinic/search?service%5B%5D=Vaccination&location=Prince+George%27s+County%2C+MD%2C+USA&search_radius=100%2B+miles&search_name=&search_date=&commit=Search#search_results

def known_working():
    utils.log("Begin vax search")

    holycross = Provider("Holy Cross Hospital", "Holy Cross Health will release the date of our next COVID-19 vaccine clinics on Thursday, Jan. 28 at 4 p.m", "https://www.holycrosshealth.org/health-and-wellness/covid-19-vaccine/schedule-appointment")
    holycross.act()

    gbmc = Provider("GBMC", "No appointments currently available", "https://www.gbmc.org/covid-vaccine")
    gbmc.act()


    adventist = Provider("Adventist Health", "null", "https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/")
    adventist.adventist_act()


    giant = Provider("Giant Foods Stores", "There are currently no COVID-19 vaccine appointments available. Please check back later. We appreciate your patience as we open as many appointments as possible. Thank you", "https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory")
#    giant.act()


    riteaid = Provider("Rite Aid", "You cannot schedule a vaccination appointment directly through Rite Aid at this time, however you can schedule through your state or local jurisdiction", "https://www.riteaid.com/Covid-19")
    riteaid.act()


    time.sleep(3)
    utils.log("End vax search")


def obsolete():
    # garrett = Provider("Garrett Co.", "THERE ARE NO APPOINTMENTS AVAILABLE AT THIS TIME", "https://health.maryland.gov/allegany/Pages/COVIDVaccination.aspx")
    # stagnes = Provider("St. Agnes", "Due to overwhelming demand Ascension Saint Agnes has no vaccination appointments available at this time", "https://healthcare.ascension.org/COVID-19/vaccinations")
    pass


def development(debug=True):
    # fred = Provider("Frederick Co.", "All Clinics currently full, check back on Tues. Jan. 19", "https://health.frederickcountymd.gov/629/COVID-19-Vaccine")
    # fred.frederick_act_full_appts(debug_flag=True)
    # martins = Provider("Martins Grocery Store", "Vaccination Scheduler - COMING SOON!", "https://martinsfoods.com/pages/tgc-vaccines")
    # martins.act(debug=True)
    pass


if __name__ == '__main__':
    known_working()
