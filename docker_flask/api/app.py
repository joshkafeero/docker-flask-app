from flask import Flask, request, jsonify, render_template
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

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d  
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404




if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

