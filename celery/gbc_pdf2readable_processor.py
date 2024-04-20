import requests
from celery import Celery
from kombu.utils.url import safequote

aws_access_key = safequote("AKIAVLYZM7DFGCFPQEKT")
aws_secret_key = safequote("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")
broker_url = "sqs://{aws_access_key}:{aws_secret_key}@sqs.eu-central-1.amazonaws.com/368883595466/ocrqueue".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)
app = Celery('tasks', backend='rpc://', broker=broker_url)
app.conf.broker_transport_options = {'region': 'eu-central-1'}


@app.task(ignore_result=True)
def execTask(bucket, bucket_facade, key):
    try:
        URL = 'http://192.168.1.117:7003'
        method = URL + '/api/gbc/ocr/image/pdf/readable'
        obj = {
            'bucket': bucket_facade,
            'source': 'S3',
            'persistence': 'S3',
            'domain': 'payroll',
            'idRequest': key,
            'disableocr': '1',
            'forcescan': '0',
            'forcenonative': '0',
            'data': key,
            'key': key
        }

        try:
            print(method)
            r = requests.post(url=method, json=obj)
            print('done')
            data = r.json()
            print(data)
        except Exception as e:  # This is the correct syntax
            print('Error in request ' + str(key))
            print(e)
            data = {
                'body': {
                    'Error': e,
                    'key': str(key)
                },
                'status': 'False',
                'statusCode': 500
            }

        return
    except Exception as e:  # This is the correct syntax
        print('Error in request ' + str(key))
        print(e)


def getNotNull(data, item):
    if not item in data:
        return ''

    return data[item]
