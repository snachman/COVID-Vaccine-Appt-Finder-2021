import time

import utils
from provider import Provider

# https://www.marylandvax.org/clinic/search?service%5B%5D=Vaccination&location=Prince+George%27s+County%2C+MD%2C+USA&search_radius=100%2B+miles&search_name=&search_date=&commit=Search#search_results

def known_working():
    utils.log("Begin vax search")
    gbmc = Provider("GBMC", "There are currently no available appointments", "https://www.gbmc.org/covid-vaccine")
    holycross = Provider("Holy Cross Hospital", "Holy Cross Health vaccine clinics are now full", "https://www.holycrosshealth.org/health-and-wellness/covid-19-vaccine/schedule-appointment")
    adventist = Provider("Adventist Health", "null", "https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/")
    giant = Provider("Giant Foods Stores", "There are currently no COVID vaccine appointments available. Please check back tomorrow as we continue to add availability", "https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory")



    # giant.act()
    adventist.adventist_act()
#    gbmc.act()
    holycross.act()
    time.sleep(3)
    utils.log("End vax search")


def obsolete():
    # garrett = Provider("Garrett Co.", "THERE ARE NO APPOINTMENTS AVAILABLE AT THIS TIME", "https://health.maryland.gov/allegany/Pages/COVIDVaccination.aspx")
    # stagnes = Provider("St. Agnes", "Due to overwhelming demand Ascension Saint Agnes has no vaccination appointments available at this time", "https://healthcare.ascension.org/COVID-19/vaccinations")

    pass


def development():
    # fred = Provider("Frederick Co.", "All Clinics currently full, check back on Tues. Jan. 19", "https://health.frederickcountymd.gov/629/COVID-19-Vaccine")
    # fred.frederick_act_full_appts(debug_flag=True)
    martins = Provider("Martins Grocery Store", "Vaccination Scheduler - COMING SOON!", "https://martinsfoods.com/pages/tgc-vaccines")
    martins.act(debug=True)

if __name__ == '__main__':
    known_working()
