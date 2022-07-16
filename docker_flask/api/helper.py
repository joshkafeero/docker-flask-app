import json
from datetime import datetime as dt



class Utilities:
    column_names = ['date','slot_id', 'desktop', 'impressions']
    input_file = './inputdata.json'

def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

def get_date(string_date):
    date = dt.strptime(string_date, '%d/%m/%Y').date()
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
    
