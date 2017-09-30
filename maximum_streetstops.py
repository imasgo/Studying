import csv

class max:
    def __init__(self, stop_name = '', street_name = '',max_stops = ''):
        self.stop_name = stop_name
        self.street_name = street_name
        self.max_stops = max_stops



with open('data-398-2017-09-14.csv','r',encoding='utf-8') as f:
    # из этого важны поля Name и Street
    fields = ["ID","Name","Longitude_WGS84","Latitude_WGS84","Street","AdmArea","District","RouteNumbers","StationName","Direction","Pavilion","OperatingOrgName","EntryState","global_id","geoData"]
    reader = csv.DictReader(f, fields, delimiter = ';')

