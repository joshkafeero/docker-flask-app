from flask import Flask, request, jsonify, render_template
import sqlite3 as sqlite
import sys
import model
import os
app = Flask(__name__)



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
    conn = sqlite.connect('../advertisings.db')
    # conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute("SELECT * FROM advertisings;").fetchall()
    # all_books = model.Advertising.query.all()
    return jsonify(all_books) 

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d  
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite.connect('../data/books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute("SELECT * FROM books;").fetchall()
    # all_books = model.Advertising.query.all()
    return jsonify(all_books)


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

