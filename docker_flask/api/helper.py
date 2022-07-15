import json
from datetime import datetime as dt



class Utilities:
    column_names = ['date','slot_id', 'desktop', 'impressions']
    input_file = 'inputdata.json'

def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

def get_date(string_date):
    date = dt.strptime(string_date, '%d/%m/%Y').date()
    return date

    
