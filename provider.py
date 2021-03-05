import os
import random
import time
import json
import utils
import requests
from pyzipcode import ZipCodeDatabase


class Provider:
    def __init__(self, organization, test_phrase, url):
        self.organization = organization
        self.test_phrase = test_phrase
        self.url = url

    def get_org_name(self):
        return self.organization

    def get_data(self):
        uas = [
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/62.0.3202.84 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/12.0 Mobile/15E148 Safari/604.1"]
        current_ua = random.choice(uas)
        headers = {"User-Agent": current_ua}
        r = requests.get(self.url, headers=headers)
        return r

    def check_for_claimed_phrase(self, body):
        if self.test_phrase in body:
            return True
        else:
            return False

    def act(self, channel):
        data = self.get_data()
        if data.status_code == 200:
            if self.check_for_claimed_phrase(data.text):
                results = "No appts"
                utils.log(self.get_org_name() + "," + results)
            else:
                results = "CHECK SITE"
                utils.alert(results + "\n" + data.url, channel)
                utils.log(self.get_org_name() + "," + results)
        else:
            utils.log(str(data.status_code))

    def frederick_act_full_appts(self, channel):
        data = self.get_data()
        if data.status_code == 200:
            number_of_full = (data.text.count("Full"))
            if number_of_full != 7:
                results = "CHECK SITE"
                utils.alert(results + "\n" + data.url, channel)
                utils.log(self.get_org_name() + "," + results)
            else:
                print("equal to 7")

    def adventist_act(self, channel):
        data = self.get_data()
        # print(data.status_code)
        # print(data.text)
        if data.status_code == 200:
            number_of_alert_me = (data.text.count("Alert Me"))
            if number_of_alert_me != 4:
                results = "CHECK SITE"
                utils.alert(results + "\n" + data.url, channel)
                utils.log(self.get_org_name() + "," + results)
            else:
                results = "No appts"
                utils.log(self.get_org_name() + "," + results)
        else:
            utils.log(str(data.status_code))

        # https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/

    def cvs_act(self, channel):
        booking_page = "https://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-banner-1-link2" \
                       "-coronavirus-vaccine "
        data_url = "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.MD.json?vaccineinfo"
        # fully_booked_string = "Fully Booked"

        r = requests.get(
            booking_page)
        time.sleep(3)
        r = requests.get(data_url)
        data = json.loads(r.text)
        stores = (data['responsePayloadData']['data']["MD"])
        for store in stores:
            state = store['state']
            city = store['city']
            city = city.title()
            total_available = str(store['totalAvailable'])
            pct_available = str(store['pctAvailable'])
            # status = store['status']
            if int(total_available) <= 1:
                utils.log(f"CVS {city},no appts")
            elif int(total_available) > 1:
                utils.log(f"city,CHECK SITE")
                alert_string = f"CVS {city}: {total_available} available which makes up {pct_available}% of the total available"
                utils.alert(alert_string, channel)
            else:
                print(r.status_code)

    def walgreens_act(self, zip_code, channel):
        time.sleep(20)
        zcdb = ZipCodeDatabase()
        code = zcdb[zip_code]
        lat = str(code.latitude)
        long = str(code.longitude)
        cmd = """curl 'https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability' \
  -H 'authority: www.walgreens.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'dnt: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' \
  -H 'content-type: application/json; charset=UTF-8' \
  -H 'origin: https://www.walgreens.com' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.walgreens.com/findcare/vaccination/covid-19/location-screening' \
  -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' \
  -H 'cookie: mbox=session#1a91c7cfa7434b4285fb5653017d3993#1613229408|PC#1a91c7cfa7434b4285fb5653017d3993.34_0#1676472353; USER_LOC=2%2BsKJSc9HtJQOXi9Ou12uguAIjJ7tdA3geN582eaqhPpoJ0Uwr9Ujs0O6uydMJPA; bm_sz=A627F779733FF6A74725727D5FE21332~YAAQwkMkF6yRao93AQAA/82FqgpUg58coGPbdvYmCYHOFwEp6IqKbA+D8y1cmoj8Li/d3pVr/ZdPxFJvfXc/nwsPLaQVkGiPR2EzvP8/t7vCU6P0CJEVPvtMa4QFat1UNjJ1EWTviVC8yQntSW0fAPX4h8iTZfTBnfBb62T/5u2bqNDtIcoaaiiA3p2GuhAEvew=; XSRF-TOKEN=D4POV4d5Z8H1tQ==.HcLRJLcZ6+qBT1qsEVrmfaJGY7dihNwNwzc1OHERfrc=; dtCookie=2$2E0F9259A62B5D351D407FFB54C9B415; ak_bmsc=59D2FF39BC48B7390CCCCD27802B119A172443C2B65300005FA72B6005DDE474~plcrVvoKOxYNK6xB+k9EASPiP2/qqIgIE8YQPxvVpvX2DcHQc9seNLW2Ga9+WmlvPsIL7DQPVRr7F2iUvhJpf9bsVBuNv9u0wsQoBfd4/tHyMNzBF78ax5PYpp978pav7XFTUsUMPbjkMu7i9Rbm2VXhW9nNOoQTM1Q6qGbO+jfWuGR0qSIPJy1xOaOmT8PjrOUfu1nsl5r16IwXwPFfZ6Ha4bB4355mnSziqMa0kzAy0=; bm_mi=166AA071D1390D8457EC84763906318C~iqpkBLeuYvADMVpxjXN2Y3pM7Gfx1goTVNm+ku0DO5Ey4Zmw3qPMmoJhMCLV7uzFm5SYjSP+ehupQ/7nik93Z5wGEzwIBv6uIgW//DTSFpUtckgZlmQ7Ozs7s2AJ1mojVclNKdIvkp0O7yr9qZnutNfPXJpvLiUwva3NaCMy2MISwR9zNi99lx+Cfnp5hvhjaE0JQFT21IEXwwSsKrXJnKQEsmSQLaEqfcnbQE4oetPxfMYaWf55ez7PEjb9lQT3yH2WJsKg65BoQZSd6LBYfw==; wag_sid=v0z1nzvh9o8pf43lq8tahxci; uts=1613473633781; fc_vnum=2; fc_vexp=true; firstVisit=fc_fVisit; AMCVS_5E16123F5245B2970A490D45%40AdobeOrg=1; AMCV_5E16123F5245B2970A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C18675%7CMCMID%7C76041403865188180393295259207093113240%7CMCOPTOUT-1613480835s%7CNONE%7CvVersion%7C5.2.0; session_id=b1e27ba4-93e3-4080-a532-37b0d3624233; gRxAlDis=N; _abck=13986FEABCCCA2F2E8487E2D5D00990E~0~YAAQwkMkF5OTao93AQAADxWGqgWqduFrva9uvOZOfkqY3saDHFYYvHI6j/anYUfwhKKwqBnZAC538jK5FfUWKUcrl8oIx4dm8TPDJ7xWFAnZCFU2catYUYMO/2hCijxSGRTB8q5rQSTW6+Fj3bZgVeEI8bWe2TSoN7QFIY3/wdDHib0gVsf8dhrr/86z2MW4U1N6T/kd3yhM7wAZmj5ZlMMmEwG35FstGc+OXkobpoK+FF76eDMOY8cuJAZOtZ8xs8DVmA0w8LO0eVE5nXqEnfDJ+CuxO1K5TbcohF2W7pWv15XC1uMCJjf3NiKaWPXk/o9b5D28+pMAZkx5mS//wIqFrS68rNOEBg==~-1~-1~-1; akavpau_walgreens=1613473955~id=01fa1eeb6c4cc5ddca304ddca65b868b; bm_sv=0CC5F0FB6BA8C3AA674B07C4F7FA073F~HGa8UiNthQzWo6qItfzJyCXiNy/7jtalJu5j0cDaPQpiuPWeObU3bBoLTusC4z1zm5ipmxlp2REuzsL/s9nfap2v9hfEVpaFULFeNlh6xFECzjApcuJ5hc+kJs4imqmWfGfDNfir1lV+HPt1nablYm1f3mi2c0qK0o6YnUTcWtY=' \
  --data-raw '{"serviceId":"99","position":{"latitude":""" + lat + ""","longitude":""" + long + """},"appointmentAvailability":{"startDateTime":"2021-02-17"},"radius":25}' \
  --compressed"""
        response = os.popen(cmd)
        data = (response.read())
        response.close()
        utils.write_to_scratchpad(data)
        j = json.loads(data)
        if not j['appointmentsAvailable']:
            message = "Walgreens - No available appts within " + str(j['radius']) + ' miles of ' + j['zipCode']
            utils.log(message)
            utils.write_to_scratchpad("if - no appts available")
            utils.alert("walgreens: " + data, channel='debug')

        elif j['appointmentsAvailable']:
            message = "Walgreens - APPTS AVAILABLE within " + str(j['radius']) + ' miles of ' + j[
                'zipCode'] + " " + code.city
            utils.log(message)
            utils.write_to_scratchpad("elif - true")
            utils.alert("walgreens: " + data, channel='debug')

            utils.alert(message, channel)
        else:
            utils.write_to_scratchpad("else triggered")


    def rite_aid_act(self, store_number, store_name, channel):
        store_number = str(store_number)
        url = f"https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={store_number}"
        r = requests.get(url)
        no_appts = """{"1":false,"2":false}"""
        low_confidance = """{"1":true,"2":false}}"""
        high_confidance = """{"1":true,"2":true}}"""
        utils.write_to_scratchpad("rite aid " + store_name)

        if no_appts in r.text:
            utils.write_to_scratchpad("no appt:\n" + r.text)
            utils.log(f"Rite Aid Store {store_number}, {store_name} no appts")
        elif low_confidance in r.text:
            utils.write_to_scratchpad("low confidence:\n" + r.text)
            message = f"Low confidence - Rite Aid Store {store_number}, {store_name} APPT AVAILABLE\nhttps://www.riteaid.com/pharmacy" \
                      f"/covid-qualifier?utm_source=state&utm_medium=web&utm_campaign=Covid19&utm_content" \
                      f"=Covid19scheduler_NJ_2_12_21 "
            utils.log(message)

        elif high_confidance in r.text:
            utils.write_to_scratchpad("high confidence:\n" + r.text)
            message = f"High confidence - Rite Aid Store {store_number}, {store_name} APPT AVAILABLE\nhttps://www.riteaid.com/pharmacy" \
                      f"/covid-qualifier?utm_source=state&utm_medium=web&utm_campaign=Covid19&utm_content" \
                      f"=Covid19scheduler_NJ_2_12_21 "
            utils.log(message)
            utils.alert(message, channel)
            utils.log("APPT DATA CAPTURE")
        time.sleep(10)
