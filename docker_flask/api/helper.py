import json
from datetime import datetime as dt
from itertools import cycle



class Utilities:
    column_names = ['date','slot_id', 'desktop', 'impressions']
    input_file = 'api/inputdata.json'

def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

def get_date(string_date):
    date = dt.strptime(string_date, '%m/%d/%Y').date()
    return date

def build_select_books_query(author, id, published, to_filter):
    query = "SELECT * FROM books WHERE"
    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)
    query = query[:-4] + ';'
    return query
    
def build_advert_sql_query(json_payload):
    query = "SELECT * FROM adverts WHERE "
    filter_list = json_payload['filter']
    device_list = json_payload['device']
    start_time_param = json_payload['start_time'] 
    start_time_param = json_payload['end_time'] 
    group_by_list = json_payload['group_by']
    
    filter_cyle = cycle(filter_list)
    filter_params = 'slot_id == ' + next(filter_cyle)
    while True:
        filter_params = ' OR slot_id == ' + next(filter_cyle)
    
    device_cycle = cycle(device_list)
    device_params = 'device == ' + next(device_cycle)
    while True:
        device_params = ' OR device == ' + next(device_cyle)
        
    
    group_by_cycle = cycle(group_by_list)
    group_by_params = 'group by ' + next(group_by_cycle)
    while True:
        group_by_params = " , " + next(group_by_cyle)
    
    query = query + fitler_params + device_params + group_by_params
    return query