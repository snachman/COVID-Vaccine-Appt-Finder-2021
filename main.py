import time

import utils
from provider import Provider

# https://www.marylandvax.org/clinic/search?service%5B%5D=Vaccination&location=Prince+George%27s+County%2C+MD%2C+USA&search_radius=100%2B+miles&search_name=&search_date=&commit=Search#search_results

def known_working():
    utils.log("Begin vax search")
    stagnes = Provider("St. Agnes", "Due to overwhelming demand Ascension Saint Agnes has no vaccination appointments available at this time", "https://healthcare.ascension.org/COVID-19/vaccinations")
    gbmc = Provider("GBMC", "There are currently no available appointments", "https://www.gbmc.org/covid-vaccine")
    holycross = Provider("Holy Cross Hospital", "Holy Cross Health vaccine clinics are now full", "https://www.holycrosshealth.org/health-and-wellness/covid-19-vaccine/schedule-appointment")
    gbmc.act()
    stagnes.act()
    holycross.act()
    time.sleep(3)
    utils.log("End vax search")


def obsolete():
    # umms = Provider("UMMS", "Please check back here Monday, January 18 for more details", "https://www.umms.org/coronavirus/covid-vaccine/get-vaccine")
    # garrett = Provider("Garrett Co.", "THERE ARE NO APPOINTMENTS AVAILABLE AT THIS TIME", "https://health.maryland.gov/allegany/Pages/COVIDVaccination.aspx")
    # giant = Provider("Giant Foods", "The following Giant Food locations will provide vaccinations to those who are eligible. Continue to check this site. More information will be provided as it becomes available", "https://coronavirus.maryland.gov/pages/maryland-retail-vaccination-sites")
    # calvert = Provider("Calvert Co.", "The pre-registration vaccine portal will open at 10 a.m. on Tuesday, Jan. 19, 2021", "https://www.calvertcountymd.gov/Vaccine")
    pass



if __name__ == '__main__':
    fred = Provider("Frederick Co.", "All Clinics currently full, check back on Tues. Jan. 19", "https://health.frederickcountymd.gov/629/COVID-19-Vaccine")


    # calvert.act(debug=True)
    # garrett.act(debug=True)
    # umms.act()
    # giant.act()
    # fred.frederick_act()
