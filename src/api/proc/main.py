import sys
import psycopg2
from flask import Flask, jsonify, request
import psycopg2.extras
from flask_cors import CORS
import xmlrpc.server

server = xmlrpc.client.ServerProxy('http://0.0.0.0:9000')

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/best_players', methods=['GET'])
def get_best_players():
    return [{
        "id": "7674fe6a-6c8d-47b3-9a1f-18637771e23b",
        "name": "Ronaldo",
        "country": "Portugal",
        "position": "Striker",
        "imgUrl": "https://cdn-icons-png.flaticon.com/512/805/805401.png",
        "number": 7
    }]



@app.route('/api/searchValue/<string:value>', methods=['GET'])
def search_value(value):
    return jsonify(server.searchValue(value))

@app.route('/api/query1', methods=['GET'])
def query_1():
    return jsonify(server.query1())

@app.route('/api/searchId/<string:id>', methods=['GET'])
def search_id(id):
    return jsonify(server.searchId(id))   

@app.route('/api/orderValue/<string:ordValue>', methods=['GET'])
def order_value(ordValue):
    return jsonify(server.orderValue(ordValue))

@app.route('/api/classFind/<string:time>', methods=['GET'])
def class_find(time):
    return jsonify(server.classFind(time))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
