import os
import sys
from flask import jsonify
from flask_restx import Resource, reqparse

from api import api
from commonsLib import loggerElk
from services.Pdf2ReadableArgParser import Pdf2ReadableArgParser


class GbcOcrImagePdf2ReadableResource(Resource):
    logger = loggerElk(__name__)
    ELK_ENABLED = os.environ["ELK_ENABLED"]
    if isinstance(ELK_ENABLED, str):
        ELK_ENABLED = True if ELK_ENABLED == "True" else False

    print(f"ELK_ENABLED: {ELK_ENABLED}")
    DEFAULT_TXT_LEN_FOR_SKIP = 100

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from api import app
        try:
            from services import Pdf2ReadableService
            self.service = Pdf2ReadableService(app=app)
        except Exception as ex:
            raise IOError("OCR server not running")

    ocrRequest = api.model('OcrRequest', Pdf2ReadableArgParser.api_model(True))

    @api.doc(
        description='OCR text from an scanned PDF, and inserting in the same PDF',
        responses={
            200: 'OK',
            400: 'Invalid Argument',
            500: 'Internal Error'})
    @api.expect(ocrRequest)
    def post(self):
        key = ''
        try:
            self.logger.Information('GbcOcrImagePdf2ReadableResource::POST - init')

            parser = reqparse.RequestParser()
            args = Pdf2ReadableArgParser.parse_args(parser, False)
            key = args['key'] if 'key' in args else ''
            ret = self.service.post(args)

            self.logger.Information('GbcOcrImagePdf2ReadableResource::POST - end')

            return jsonify(ret)

        except Exception as e:
            self.logger.Error(f'ERROR - GbcOcrImagePdf2ReadableResource::'
                              f'POST- {key} ' + str(e.args), sys.exc_info())
            return jsonify({
                'status': 'False',
                'statusCode': 500,
                'result': key,
                'resultText': '',
                'resultTextNonNative': '',
                'was_readable': 'False'
            })
