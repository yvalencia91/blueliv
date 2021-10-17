from settings import config
from src.lib.logger import setup_logger
from logging import getLogger
from db import db
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.resources.threat import ThreatList
from src.resources.user import UserLogin, UserRegister
from elasticapm.contrib.flask import ElasticAPM

setup_logger(config)
log = getLogger(__name__)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = config.secret_key
app.config['ELASTIC_APM'] = config.apm
apm = ElasticAPM(app)
api = Api(app)
jwt = JWTManager(app)

api.add_resource(ThreatList, '/api/v1/threat')
api.add_resource(UserLogin, '/api/v1/login')
api.add_resource(UserRegister, '/api/v1/register')


@app.before_first_request
def create_tables():
    db.init_app(app)


if __name__ == "__main__":

    apm.app.run(port=8000, host="0.0.0.0")
