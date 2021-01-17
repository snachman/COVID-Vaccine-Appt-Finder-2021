import datetime
import os

import requests


class Provider():
    def __init__(self, organization,test_phrase, url):
        self.organization = organization
        self.test_phrase = test_phrase
        self.url = url

    def get_org_name(self):
        return self.organization

    def alert(self, message):
        curl = """curl -X POST -H 'Content-type: application/json' --data '{"text":"%s"}' https://hooks.slack.com/services/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""" % (
            message)
        os.popen(curl)

    def log(self, message):
        now = datetime.datetime.now()
        stamp = now.strftime("%m/%d/%Y,%H:%M,")
        with open("log.txt", "a") as file:
            file.write("\n" + stamp + message)
            file.close()

    def get_data(self):
        ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        headers = {"User-Agent": ua}
        r = requests.get(self.url, headers=headers)
        return r

    def check_for_claimed_phrase(self, body):
        if self.test_phrase in body:
            return True
        else:
            return False

    def act(self):
        data = self.get_data()
        if data.status_code == 200:
            if self.check_for_claimed_phrase(data.text):
                results = "No appts"
                self.log(results)
                self.alert(results + "\n" + data.url)
            else:
                results = "APPTS AVAILABLE"
                self.log(results)
        else:
            self.log(str(data.status_code))
