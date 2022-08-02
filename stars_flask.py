from flask import Flask, request, jsonify
from stars_data import data

app = Flask(__name__)

@app.route('/')
def stars():
    return jsonify({
        'stars' : data,
        'message' : 'success'
    }), 200
@app.route('/star')
def sub_info():
    name = request.args.get('name')
    stars_data = next(i for i in data if i['name'] == name)
    return jsonify({
        'star' : stars_data,
        'message' : 'success'
    })
app.run()