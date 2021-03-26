import time

import requests
import os
import utils




def publix_act():
    epoch = round(time.time())
    url = f"https://www.publix.com/covid-vaccine/florida/florida-county-status.txt?t={epoch}"
    r = requests.get(url)
    lines = (r.content.decode("utf-16").splitlines())
    for line in lines:
        parsed = line.split("|")
        town = parsed[0]
        status = parsed[1]
        formatted = f"PUBLIX\n{town}: {status} appnts remaining"
        if "dade" in line.lower():
            if "Fully Booked" in status:
                utils.log(formatted)
            elif "None Available" in status:
                utils.log(formatted)
            elif "Coming Soon".lower() in "status".lower():
                utils.log(formatted)
            elif "100".lower() in "status".lower():
                utils.log(formatted)
            else:
                utils.log(formatted)
                utils.alert(formatted + "\nhttps://www.publix.com/covid-vaccine/florida", 'florida')





if __name__ == '__main__':
    publix_act()
