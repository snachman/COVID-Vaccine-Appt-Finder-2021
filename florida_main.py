import requests
import os

def alert(message):
    end = ""
    cmd = """curl -X POST -H 'Content-type: application/json' --data '{"text":" %s"}' https://hooks.slack.com/services/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""" % (message)
    os.popen(cmd)

def florida_act():
    url = "https://www.publix.com/covid-vaccine/florida/florida-county-status.txt?t=1616597688230"
    r = requests.get(url)
    lines = (r.content.decode("utf-16").splitlines())
    for line in lines:
        parsed = line.split("|")
        town = parsed[0]
        status = parsed[1]
        if "dade" in line.lower():
            alert(f"PUBLIX\n{town}: {status}")

if __name__ == '__main__':
    florida_act()