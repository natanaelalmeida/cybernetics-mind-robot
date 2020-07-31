from flask import Flask
from flask_restful import Api

from api.move_service import MoveService

app = Flask(__name__)
api = Api(app)

api.add_resource(MoveService, '/move')

if __name__ == "__main__":
    app.run(debug=True, host='172.17.0.2', port=5005)
