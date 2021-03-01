import requests
import utils
import json


if __name__ == '__main__':
    arcgis = "https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    r = requests.get(arcgis)
    j = json.loads(r.text)
