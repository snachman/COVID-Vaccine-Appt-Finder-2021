import datetime
import os
import random

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
        uas = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36", "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36", "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"]
        current_ua = random.choice(uas)
        print(current_ua)
        headers = {"User-Agent": current_ua}
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
            else:
                results = "APPTS AVAILABLE"
                self.alert(results + "\n" + data.url)
                self.log(results)
        else:
            self.log(str(data.status_code))
