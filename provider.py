import os
import random
import time
import json
import utils
import requests
from pyzipcode import ZipCodeDatabase

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
            number_of_Full = (data.text.count("Full"))
            if number_of_Full != 7:
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
            number_of_Alert_Me = (data.text.count("Alert Me"))
            if number_of_Alert_Me != 4:
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
        booking_page = "https://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-banner-1-link2-coronavirus-vaccine"
        data_url = "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.MD.json?vaccineinfo"
        fullly_booked_string = "Fully Booked"

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
            totalAvailable = str(store['totalAvailable'])
            pctAvailable = str(store['pctAvailable'])
            status = store['status']
            if int(totalAvailable) <= 1:
                utils.log(f"CVS {city},no appts")
            elif int(totalAvailable) > 1:
                utils.log(f"city,CHECK SITE")
                alert_string = f"CVS {city}: {totalAvailable} available which makes up {pctAvailable}% of the total available"
                utils.alert(alert_string, channel)
            else:
                print(r.status_code)



    def walgreens_act(self, zip, channel):

        zcdb = ZipCodeDatabase()
        code = zcdb[zip]
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
            message = "Walgreens - APPTS AVAILABLE within " + str(j['radius']) + ' miles of ' + j['zipCode']
            utils.log(message)
            utils.write_to_scratchpad("elif - true")
            utils.alert("walgreens: " + data, channel='debug')

            utils.alert(message, channel)
        else:
            utils.write_to_scratchpad("else triggered")


    def allentown_nj_walgreens_act(self, channel):

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
  -H 'cookie: USER_LOC=2%2BsKJSc9HtJQOXi9Ou12uguAIjJ7tdA3geN582eaqhPpoJ0Uwr9Ujs0O6uydMJPA; ak_bmsc=D537396850C93FA9F295123CF19CB0E5172443D0A5020000D0DE2F60DD879519~plDrvOqcR9m7ufTqGpe/B8jcuNapzMRYf/CkqeBqVXonzdn3fHfIJdKyA+RgZ6XvINHeJZWqySuBOlhSxa85EgO3qPAhRiAb6zo0wfSx6siGXfWrv3Lde6NRk6gvLcGSmcTPtoSyUkNc6xqFPuS01fS6iS4+cH9XLyhGRO8oX9ekIcgTLCBtsGHaz7rE397K1v6uHfjS8xi+NpaUaWJyJmc860osh/1/kMP37jSQmC8rY=; bm_sz=2EDDA20179C3850B248144D3B534623B~YAAQ0EMkFz/tsrZ3AQAAZF/+ugr04pdQKALRaHkyfhDq5RSqM9BoxYNFI5BFa0jPJiveoUfIA4ntAm6gPKa6wlJn4K60skYUrE2mYCMkiy2pr0G8gqPr1E41hy2wRAz4WzwUnTdCBt0M5R87Ti6+/wFdHEJlxdO9MQR4AJEApKT6tS+Ns34dMezfda0PXdXwpLRm; wag_sid=dyj5xw5udlhfsdxc581olbmx; uts=1613749969357; XSRF-TOKEN=ErTgjFLNXfCRLw==.uF2aLBHMtSqJvsUiInc051RwrpUk+hQ+3O8gK6+EO7c=; at_check=true; session_id=cbfa8d7a-37db-48e4-81ec-7ffda834560c; dtCookie=6$CA84D8A628AE4D51221A8E4DFD3C0809; AMCVS_5E16123F5245B2970A490D45%40AdobeOrg=1; gRxAlDis=N; strOfrId={"WAStrId":"17609"}; str_nbr_do=17609; str=%7B%22sId%22%3A%2219957%22%2C%22lt%22%3A%2240.21946813%22%2C%22lg%22%3A%22-74.74531011%22%2C%22st%22%3A%22739%20GREENWOOD%20AVENUE%22%2C%22ct%22%3A%22TRENTON%22%2C%22zp%22%3A%2208609%22%2C%22stat%22%3A%22NJ%22%2C%22bag%22%3A%220%22%2C%22sdp%22%3A%221%22%2C%22t4hr%22%3A%22N%22%7D; gstPS={"ST":["trenton, nj","trenton, nj"]}; bm_mi=AAA8E34424FFA0420824175F9AAE9863~u2NRgqsQn18pVSJznoZ1Di5sIo5nteST91CJ9B6zxPndUqs85EFkq6Lvon0f2d6S3szUgWxLLtfUa7C+mdi93u9HD5kMulk7EdWxYpaSD8zgXozlSfdf34hiW08HY45L+OVq36wHqC0sM/rS+GSzBJMj7Zh5J+FHrM+0p/GM8ZZq6BXofnW85BI32gC/hnHkNkPu0eliSsham4GJ2r5Li0dYQnHOWD7e1XrQLhV3mSuZyDwbvRLNBIKmpYz4m03HQ/Vm8wNn8huWzCWpUAlR1Q==; mbox=PC#1a91c7cfa7434b4285fb5653017d3993.34_0#1676994812|session#a93d300339a34202b962e0788a478f0d#1613751830; fc_vnum=3; firstVisit=fc_fVisit; AMCV_5E16123F5245B2970A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C18678%7CMCMID%7C76041403865188180393295259207093113240%7CMCOPTOUT-1613757213s%7CNONE%7CvVersion%7C5.2.0; akavpau_walgreens=1613750393~id=13562da4c6da6ee4109fbdd5167d557f; bm_sv=77A82964CD30F341FEB82A96B8ACC8E4~lOod8lObMdixWhYaTg5F6Jnx2Nffax3LPhEiL8pFWIxntVmJ5ncVURV3HDsOwvkJXejGZteUPxzPJH++M1r9pdQ6aVK/xtPtt+isP+tS7VBu2rlBZGdWxdmCQ5KLOBU5pC2xU/Ch5OR07Nn5Q97tdvGQ+74g/STYwqzG1aKAJ6U=; _abck=13986FEABCCCA2F2E8487E2D5D00990E~0~YAAQz0MkF3US/rV3AQAAq0gAuwUZqS1Pzt3vi3vdyPRzzKiB9XLlpWUKe2CnNv0sEcOltmS/7D3nKLYADc4dedw6KsNvGmGK3TXl9MC2RqtU5LMIFxJPiEvf5Dqg5xsYpuFZRN8tQmqlv0prjPJDwqc5/B1P1nNg8z3AGVkLUKAuJ0QqrSW+6fCai/izSHBJXkFJOHjfqPj958scCeTiDUm+m4Y8uidCikLDW2X/6JDt3EnyhZ8hCXxL4AlXewxCnVB4dzkYqEy2FuF4hpr+yC2f6sunBG2VfKGSNSzvjQkhzCb93/ZQKmNVqwi5b5h/MmwHGpKnM4wvozT1SN/RB9PHcF8seSJ6Bg==~-1~-1~-1' \
  --data-raw '{"serviceId":"99","position":{"latitude":40.1778886,"longitude":-74.58348869999999},"appointmentAvailability":{"startDateTime":"2021-02-20"},"radius":25}' \
  --compressed"""
        response = os.popen(cmd)
        data = (response.read())
        response.close()
        j = json.loads(data)
        if not j['appointmentsAvailable']:
            message = "NJ: Walgreens - No available appts within " + str(j['radius']) + ' miles of ' + j['zipCode']
            utils.log(message)
            # utils.alert(message, debug_flag=True)

        elif j['appointmentsAvailable']:
            message = "NJ: Walgreens - APPTS AVAILABLE within " + str(j['radius']) + ' miles of ' + j['zipCode']
            utils.log(message)
            utils.alert(message, channel)




    def rite_aid_act(self, store_number, store_name, channel):
        store_number = str(store_number)
        url = f"https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={store_number}"
        r = requests.get(url)
        no_appts = """{"Data":{"slots":{"1":false,"2":false}},"Status":"SUCCESS","ErrCde":null,"ErrMsg":null,"ErrMsgDtl":null}"""
        if r.text == no_appts:
            utils.log(f"Rite Aid Store {store_number}, {store_name} no appts")
        else:
            message = f"Rite Aid Store {store_number}, {store_name} APPT AVAILABLE\nhttps://www.riteaid.com/pharmacy/covid-qualifier?utm_source=state&utm_medium=web&utm_campaign=Covid19&utm_content=Covid19scheduler_NJ_2_12_21"
            utils.log(message)
            utils.alert(message, channel)
            utils.log("APPT DATA CAPTURE", channel)
            try:
                utils.log("data: " + r.text, channel)
            except:
                utils.log("fail to print data", channel)
        time.sleep(7)



    def giant_zip_check(self, zip):
        s = requests.session()
        s.get("https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory")
        r = s.get('https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/CheckZipCode?zip=08759&appointmentType=5956&PatientInterfaceMode=0')
        print(r.text)