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
        r = requests.get(self.url)
        return r

    def check_for_claimed(self, body):
        claimed_string = self.test_phrase
        if claimed_string in body:
            return False
        else:
            return True

    def act(self):
        data = self.get_data()
        if self.check_for_claimed(data.text):
            results = "VACCINES AVAILABLE"
            self.log(results)
            self.alert(results + "\n" + data.url)
        else:
            results = "All appts claimed"
            self.log(results)
