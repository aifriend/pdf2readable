from flask_restx import fields


class Pdf2ReadableArgParser:
    def init(self):
        pass

    @staticmethod
    def parse_args(parser, is_enqueuing):
        parser.add_argument('source', type=str, location='json')
        parser.add_argument('persistence', type=str, location='json')
        parser.add_argument('bucket', type=str, location='json')
        parser.add_argument('key', type=str, location='json')
        parser.add_argument('idRequest', type=str, location='json')
        parser.add_argument('data', type=str, location='json')
        parser.add_argument('lang', type=str, location='json')
        parser.add_argument('forcescan', type=int, location='json')
        parser.add_argument('forcenonative', type=int, location='json')
        parser.add_argument('disableocr', type=int, location='json')
        parser.add_argument('max_pages', type=int, location='json')
        parser.add_argument('txtLenForSkip', type=int, location='json')
        parser.add_argument('kb_limit_size', type=int, location='json')
        if is_enqueuing:
            parser.add_argument('queue', type=str, location='json')
            parser.add_argument('endpoint_push', type=str, location='json')
        return parser.parse_args()

    @staticmethod
    def api_model(is_enqueuing):
        model = {
            'persistence': fields.String(
                required=False, default='', description='Type of file persistence'),
            'source': fields.String(
                required=True,
                default='S3',
                description='The source channel to obtain the image (in PNG). [BASE64, FILE, S3]'),
            'bucket': fields.String(
                required=False, default='', description='The bucket of the file'),
            'key': fields.String(
                required=False, default='', description='Key of the file'),
            'idRequest': fields.String(
                required=False, default='', description='Request ID'),
            'data': fields.String(
                required=True,
                default='',
                description='Content of the file in [Base64 | URL | S3 URL]'),
            'lang': fields.String(
                required=True, default='spa', description='OCR language (spa/eng)'),
            'forcescan': fields.Integer(
                required=True,
                default=0,
                description='Force scan file and dismiss previous txt files'),
            'forcenonative': fields.Integer(
                required=True, default=0, description='Force no native scan file'),
            'disableocr': fields.Integer(
                required=True, default=0, description='Disable the OCR for native documents'),
            'max_pages': fields.Integer(
                required=True, default=99, description='Max number of pages processed'),
            'txtLenForSkip': fields.Integer(
                required=True, default=100, description='Max length to discard'),
            'kb_limit_size': fields.Integer(
                required=False, default=0, description='Max file size to process it'),
        }
        if is_enqueuing:
            model["queue"] = fields.String(required=True, description='Queue where is gonna append')
            model["endpoint_push"] = fields.String(required=False, description='Endpoint to send result')

        return model
