import sys
import psycopg2
from flask import Flask, jsonify, request
import psycopg2.extras
from flask_cors import CORS
from entities import *

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

# set of all teams
# !TODO: replace by database access

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/api/routes', methods=['GET'])
def get_routes():
    routes = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, destination, source, created_on, updated_on FROM routes")

    for row in cursor.fetchall():
        routes.append(row)

    db_rel.close()

    return jsonify(routes)

@app.route('/api/routes/<string:id_route>', methods=['GET'])
def get_routes_by_id(id_route):
    routes = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, destination, source, created_on, updated_on FROM routes WHERE id = %s", [id_route])

    for row in cursor.fetchall():
        routes.append(row)
    
    db_rel.close()

    return jsonify(routes)


@app.route('/api/times', methods=['GET'])
def get_times():
    times = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, departure, arrival, created_on, updated_on FROM times")

    for row in cursor.fetchall():
        times.append(row)

    db_rel.close()

    return jsonify(times)

@app.route('/api/times/<string:id_time>', methods=['GET'])
def get_times_by_id(id_time):
    times = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, departure, arrival, created_on, updated_on FROM times WHERE id = %s", [id_time])

    for row in cursor.fetchall():
        times.append(row)

    return jsonify(times)


@app.route('/api/airlines', methods=['GET'])
def get_airlines():
    airlines = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, name, created_on, updated_on FROM airlines")

    for row in cursor.fetchall():
        airlines.append(row)

    db_rel.close()

    return jsonify(airlines)


@app.route('/api/airlines/<string:id_airline>', methods=['GET'])
def get_airlines_by_id(id_airline):
    airlines = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, name, created_on, updated_on FROM airlines WHERE id = %s", [id_airline])

    for row in cursor.fetchall():
        airlines.append(row)

    return jsonify(airlines)



@app.route('/api/classes', methods=['GET'])
def get_classes():
    classes = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, name, created_on, updated_on FROM classes")

    for row in cursor.fetchall():
        classes.append(row)

    db_rel.close()

    return jsonify(classes)


@app.route('/api/classes/<string:id_classe>', methods=['GET'])
def get_classes_by_id(id_classe):
    classes = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT id, name, created_on, updated_on FROM classes WHERE id = %s", [id_classe])

    for row in cursor.fetchall():
        classes.append(row)

    return jsonify(classes)


@app.route('/api/flights', methods=['GET'])
def get_flights():
    flights = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT flights.id, flights.name, flights.price, flights.stops, routes.source, routes.destination, times.departure, times.arrival, times_fligths.duration, times_fligths.days,  flights.id_airline, flights.id_routes, flights.id_classes, flights.created_on, flights.updated_on FROM times_fligths INNER JOIN flights ON times_fligths.id_fligths = flights.id INNER JOIN times ON times_fligths.id_times = times.id INNER JOIN routes ON flights.id_routes = routes.id")

    for row in cursor.fetchall():
        flights.append(row)

    db_rel.close()

    return jsonify(flights)


@app.route('/api/flights/<string:id_fligth>', methods=['GET'])
def get_flights_by_id(id_fligth):
    flights = []
    db_rel = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
    
    cursor = db_rel.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT flights.id, flights.name, flights.price, flights.stops, routes.source, routes.destination, times.departure, times.arrival, times_fligths.duration, times_fligths.days,  flights.id_airline, flights.id_routes, flights.id_classes, flights.created_on, flights.updated_on FROM times_fligths INNER JOIN flights ON times_fligths.id_fligths = flights.id INNER JOIN times ON times_fligths.id_times = times.id INNER JOIN routes ON flights.id_routes = routes.id WHERE flights.id = %s", [id_fligth])

    for row in cursor.fetchall():
        flights.append(row)

    db_rel.close()

    return jsonify(flights)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
