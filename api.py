import os
import sys
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api
from urllib.error import HTTPError

from commonsLib import loggerElk

app = Flask(__name__)
api = Api(app, version='1.0', prefix='/api', title='GBC OCR Pdf2Readable API',
          description='Microservice for OCR text from an scanned PDF, and inserting in the same PDF',
          )

# Enable Swagger and CORS
ns = api.namespace('gbc/ocr/image/pdf/readable',
                   description='OCR text from an scanned PDF, and inserting in the same PDF')
Swagger(app)
cors = CORS(app)

# JWT configuration
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

app.config.from_json('./config/config.json')
print('----- CONFIG TEST -----')
print(app.config['WELCOME'])

logger = loggerElk(__name__)

from GbcOcrImagePdf2ReadableResource import GbcOcrImagePdf2ReadableResource

ns.add_resource(GbcOcrImagePdf2ReadableResource, '')
from GbcOcrImagePdf2ReadableCacheCleanerResource import GbcOcrImagePdf2ReadableCacheCleanerResource

ns.add_resource(GbcOcrImagePdf2ReadableCacheCleanerResource, '/clear')

# HealthCheck
from healthcheck import HealthCheck, EnvironmentDump

health = HealthCheck()
envdump = EnvironmentDump()


def service_avaliable():
    ELK_ENABLED = os.environ["ELK_ENABLED"]
    if isinstance(ELK_ENABLED, str):
        ELK_ENABLED = True if ELK_ENABLED == "True" else False

    logger = loggerElk(__name__)
    logger.LogResult("HealthCheck - OK", "service ok")
    return True, "service ok"


health = HealthCheck(checkers=[service_avaliable])
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())


@api.errorhandler(Exception)
def handle_error(e):
    ELK_ENABLED = os.environ["ELK_ENABLED"]
    if isinstance(ELK_ENABLED, str):
        ELK_ENABLED = True if ELK_ENABLED == "True" else False

    logger = loggerElk(__name__)
    logger.Information("Error Handler")
    code = 500
    if isinstance(e, HTTPError):
        code = e.code
    logger.Error(str(e), sys.exc_info())
    return {'message': 'Something went wrong: ' + str(e)}, code
