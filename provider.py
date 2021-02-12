import random
import utils
import requests


class Provider():
    def __init__(self, organization,test_phrase, url):
        self.organization = organization
        self.test_phrase = test_phrase
        self.url = url

    def get_org_name(self):
        return self.organization

    def get_data(self):
        uas = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36", "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36", "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"]
        current_ua = random.choice(uas)
        headers = {"User-Agent": current_ua}
        r = requests.get(self.url, headers=headers)
        return r

    def check_for_claimed_phrase(self, body):
        if self.test_phrase in body:
            return True
        else:
            return False

    def act(self, debug=False):
        data = self.get_data()
        if data.status_code == 200:
            if self.check_for_claimed_phrase(data.text):
                results = "No appts"
                utils.log(self.get_org_name() + "," + results)
            else:
                results = "CHECK SITE"
                utils.alert(results + "\n" + data.url, debug)
                utils.log(self.get_org_name() + "," + results)
        else:
            utils.log(str(data.status_code))


    def frederick_act_full_appts(self, debug_flag=False):
        data = self.get_data()
        if data.status_code == 200:
            number_of_Full = (data.text.count("Full"))
            if number_of_Full != 7:
                results = "CHECK SITE"
                utils.alert(results + "\n" + data.url, debug_flag)
                utils.log(self.get_org_name() + "," + results)
            else:
                print("equal to 7")


    def adventist_act(self, debug_flag=False):
        data = self.get_data()
        # print(data.status_code)
        # print(data.text)
        if data.status_code == 200:
            number_of_Alert_Me = (data.text.count("Alert Me"))
            if number_of_Alert_Me != 4:
                results = "CHECK SITE"
                utils.alert(results + "\n" + data.url, debug_flag)
                utils.log(self.get_org_name() + "," + results)
            else:
                results = "No appts"
                utils.log(self.get_org_name() + "," + results)
        else:
            utils.log(str(data.status_code))

        # https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/