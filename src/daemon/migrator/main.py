import sys
import time

import psycopg2
import psycopg2.extras
from psycopg2 import OperationalError

POLLING_FREQ = int(sys.argv[1]) if len(sys.argv) >= 2 else 60


def print_psycopg2_exception(ex):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()
    #efwf
    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print("\npsycopg2 ERROR:", ex, "on line number:", line_num)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", ex.diag)

    # print the pgcode and pgerror exceptions
    print("pgerror:", ex.pgerror)
    print("pgcode:", ex.pgcode, "\n")

def create_airline(connection, name):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT id FROM airlines WHERE name = %s", [name])
    rows = cursor.fetchall()

    if rows:
        return rows[0]['id']
    else:
        cursor.execute("INSERT INTO airlines(name) VALUES(%s)", [name])
        connection.commit()

        cursor.execute("SELECT id FROM airlines WHERE name = %s", [name])
        row = cursor.fetchall()
        connection.commit()

        if rows:
            return rows[0]['id']

        

def create_classe(connection, name):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT id FROM classes WHERE name = %s", [name])
    rows = cursor.fetchall()

    if rows:
        return rows[0]['id']
    else:
        cursor.execute("INSERT INTO classes(name) VALUES(%s)", [name])
        connection.commit()

        cursor.execute("SELECT id FROM classes WHERE name = %s", [name])
        row = cursor.fetchall()
        connection.commit()

        if rows:
            return rows[0]['id']


def create_route(connection, destination, source):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT id FROM routes WHERE destination = %s AND source = %s", [destination, source])
    rows = cursor.fetchall()

    if rows:
        return rows[0]['id']
    else:
        cursor.execute("INSERT INTO routes(destination, source) VALUES(%s, %s)", [destination, source])
        connection.commit()

        cursor.execute("SELECT id FROM routes WHERE destination = %s AND source = %s", [destination, source])
        rows = cursor.fetchall()
        connection.commit()

        if rows:
            return rows[0]['id']

def create_times(connection, departure, arrival):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT id FROM times WHERE departure = %s AND arrival = %s", [departure, arrival])
    rows = cursor.fetchall()

    if rows:
        return rows[0]['id']
    else:
        cursor.execute("INSERT INTO times(departure, arrival) VALUES(%s, %s)", [departure, arrival])
        connection.commit()

        cursor.execute("SELECT id FROM times WHERE departure = %s AND arrival = %s", [departure, arrival])
        rows = cursor.fetchall()
        connection.commit()

        if rows:
            return rows[0]['id']

def create_flights(connection, id_airline, id_route, id_classe, name, price, stop):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT id FROM flights WHERE name = %s", [name])
    rows = cursor.fetchall()

    if rows:
        return rows[0]['id']
    else:
        cursor.execute("INSERT INTO flights(name, price, stops, id_airline, id_routes, id_classes) VALUES(%s, %s, %s, %s, %s, %s)", [name, price, stop, id_airline, id_route, id_classe])
        connection.commit()

        cursor.execute("SELECT id FROM flights WHERE name = %s", [name])
        rows = cursor.fetchall()
        connection.commit()

        if rows:
            return rows[0]['id']

def create_times_flights(connection, id_flight, id_times, duration, days):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("INSERT INTO times_fligths(id_fligths, id_times, duration, days) VALUES(%s, %s, %s, %s)", [id_flight, id_times, duration, days])
    connection.commit()
        


if __name__ == "__main__":

    db_org = psycopg2.connect(host='db-xml', database='is', user='is', password='is')
    db_dst = psycopg2.connect(host='db-rel', database='is', user='is', password='is')

    while True:

        # Connect to both databases
        db_org = None
        db_dst = None

        try:
            db_org = psycopg2.connect(host='db-xml', database='is', user='is', password='is')
            db_dst = psycopg2.connect(host='db-rel', database='is', user='is', password='is')
        except OperationalError as err:
            print_psycopg2_exception(err)

        if db_dst is None or db_org is None:
            continue

        cursor = db_org.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        print("Checking updates...")
        # !TODO: 1- Execute a SELECT query to check for any changes on the table
        # !TODO: 2- Execute a SELECT queries with xpath to retrieve the data we want to store in the relational db
        # !TODO: 3- Execute INSERT queries in the destination db
        # !TODO: 4- Make sure we store somehow in the origin database that certain records were already migrated.
        #          Change the db structure if needed.


        # primeiro fazer select á tabela imported_documents onde o is_on_db_rel é false (db_xml)
        # extrair os dados do xml de cada row (db_xml)
        # usar os dados extraidos e inserir na base de dados relacional (db_rel)
        # dps dos dados serem inseridos na db_rel, meter a true o is_on_db_rel para informar que essa row foi migrada

        imported_documents = []

        cursor.execute("SELECT id FROM imported_documents WHERE is_on_db_rel IS FALSE")

        for row in cursor.fetchall():
            imported_documents.append(row['id'])


        for id in imported_documents:
            xml_data = []
            

            cursor.execute(
                "WITH flights as ("
                "    SELECT unnest(xpath('//flights/flight', xml)) as flight "
                "        FROM imported_documents"
                "    WHERE id = %s"
                ") SELECT "
                "    (xpath('/flight/@name', flight))[1]::text                  as name, "
                "    (xpath('/flight/@airline', flight))[1]::text                    as airline, "
                "    (xpath('/flight/route/@source', flight))[1]::text               as source, "
                "    (xpath('/flight/route/@destination', flight))[1]::text               as destination, "
                "    (xpath('/flight/details/price/@value', flight))[1]::text::decimal                   as price, "
                "    (xpath('/flight/details/price/@class', flight))[1]::text                   as class, "
                "    (xpath('/flight/details/stops/@count', flight))[1]::text                   as stops, "
                "    (xpath('/flight/details/time/@departure', flight))[1]::text                   as departure, "
                "    (xpath('/flight/details/time/@arrival', flight))[1]::text                   as arrival, "
                "    (xpath('/flight/details/time/@duration', flight))[1]::text::decimal                   as duration, "
                "    (xpath('/flight/details/time/@days', flight))[1]::text::integer                   as days "
                "        FROM flights",
                [id]
            )
            
            for row in cursor.fetchall():
                airline_id = create_airline(db_dst, row['airline'])
                classe_id = create_classe(db_dst, row['class'])
                route_id = create_route(db_dst, row['destination'], row['source'])
                times_id = create_times(db_dst, row['departure'], row['arrival'])

                flight_id = create_flights(db_dst, airline_id, route_id, classe_id, row['name'], row['price'], row['stops'])

                create_times_flights(db_dst, flight_id, times_id, row['duration'], row['days'])

            
            






        db_org.close()
        db_dst.close()

        time.sleep(POLLING_FREQ)
