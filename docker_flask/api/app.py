from flask import Flask, request, jsonify, render_template
from flask_negotiate import consumes, produces
import sqlite3 as sqlite
import sys
# import model
# from seed import seed_db
import os
app = Flask(__name__)


# seed_db()
@app.route('/', methods=['GET'])
def home():
    return """<h1>ML project</h1>
    <p>A prototype API for distant reading data home</p>
    """


@app.route('/alldata', methods=['GET'])
def all_data():
    results  = model.Advertising.query.all()
    print(results)
    return jsonify(results)

@app.route('/alldata2', methods=['GET'])
def all_data2():
    conn = sqlite.connect('../api/advertisings.db')
    cur = conn.cursor()
    all_data = cur.execute("SELECT * FROM advertisings;").fetchall()
    return jsonify(all_data) 


@app.route('/request_data', methods=['POST'])
@consumes('application/json')
@produces('application/json')
def request_data():
    json_payload = request.json
    
    if ( (json_payload['filter'] == None) or
         (json_payload['device'] == None) or
         (json_payload['start_date'] == None) or
         (json_payload['end_date'] == None) or
         (json_payload['group_by'] == None) ) :
        
        return "error"
    else:
        sql_query = build_advert_sql_query(json_payload)
        
    conn = sqlite.connect('../api/advertisings.db')
    cur = conn.cursor()
    all_data = cur.execute(sql_query).fetchall()
    return jsonify(all_data) 


@app.errorhandler(404)
def page_not_found(e):
    return """<h1> Ohh no :(</h1>
    <h3> We dont have that route please check your entry</h3>
    """




if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

