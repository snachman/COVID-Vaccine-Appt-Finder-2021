import requests
import os
import utils




def publix_act():
    url = "https://www.publix.com/covid-vaccine/florida/florida-county-status.txt?t=1616597688230"
    r = requests.get(url)
    lines = (r.content.decode("utf-16").splitlines())
    for line in lines:
        parsed = line.split("|")
        town = parsed[0]
        status = parsed[1]
        formatted = f"PUBLIX\n{town}: {status}"
        if "dade" in line.lower():
            if "Fully Booked" in status:
                utils.log(formatted)
            elif "None Available" in status:
                utils.log(formatted)
            elif "Coming Soon".lower() in "status".lower():
                utils.log(formatted)
            else:
                utils.log(formatted)
                florida_alert(formatted + "\nhttps://www.publix.com/covid-vaccine/florida")





if __name__ == '__main__':
    publix_act()
