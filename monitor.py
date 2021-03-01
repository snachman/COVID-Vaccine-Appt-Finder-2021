import requests
import utils
import json
import hashlib


def write_to_file(data):
    with open("site_list.txt", "a") as f:
        f.write(data)
        f.write("\n")
        f.close()


def check_file(data):
    with open('site_list.txt', 'r') as f:
        if data in f.read():
            return True
        else:
            return False


def hash_data(string):
    unique_hash = hashlib.sha256(str.encode(string)).hexdigest()
    return unique_hash


if __name__ == '__main__':
    arcgis = "https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    r = requests.get(arcgis)
    j = json.loads(r.text)
    for location in (j['features']):
        facility_id = (location['attributes']['facilityid'])
        schedule_url = (location['attributes']['schedule_url'])
        name = (location['attributes']['name'])
        county = (location['attributes']['County'])
        site_type = (location['attributes']['site_type'])
        hash = hash_data(facility_id + name)
        if check_file(hash):
            # exists
            pass
        else:
            # needs notification
            message = ("NEW SITE: " + name)
            # utils.alert(message, 'personal')
            utils.log(message)
            write_to_file(hash)
