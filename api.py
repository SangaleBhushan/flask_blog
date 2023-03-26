from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import mysql.connector

app = Flask(__name__)
api = Api(app)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'json_data'
}

# Helper function to create a database connection
def create_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Resource to get all records from the database
class Records(Resource):
    def get(self):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM data")
        rows = cursor.fetchall()
        records = []
        for row in rows:
            record = {
                'end_year' : row[0],
                'intensity': row[1],
                'sector': row[2],
                'topic': row[3],
                'region': row[6],
                'start_year': row[7],
                'country': row[11],
                'relevance': row[12],
                'pestle': row[13],
                'source': row[14],
                'likelihood': row[16],
            }
            records.append(record)
        print(records)
        connection.close()
        return jsonify(records)


# Resource to get a specific record from the database
class Record(Resource):
    def get(self, id):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            record = {
                'end_year' : row[0],
                'intensity': row[1],
                'sector': row[2],
                'topic': row[3],
                'region': row[4],
                'start_year': row[5],
                'country': row[6],
                'relevance': row[7],
                'pestle': row[8],
                'source': row[9],
                'likelihood': row[10],
            }
            connection.close()
            return jsonify(record)
        else:
            connection.close()
            return {'message': 'Record not found'}, 404



# Add the resources to the API
api.add_resource(Records, '/api/v1/records')
api.add_resource(Record, '/api/v1/records/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
