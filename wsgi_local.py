import os

os.environ['ELK_URL'] = 'https://search-samelan-elk-sandbox-4vyd2rkds6jljgamh7aofo6qam.eu-west-1.es.amazonaws.com'
os.environ['ELK_INDEX'] = 'gbcml-'
os.environ['APPLICATION'] = 'ML.OCR'
os.environ['ENVIRONMENT'] = 'Development'
os.environ['LOG_LEVEL'] = 'DEBUG'
os.environ['LOG_FILE'] = 'logFile.log'
os.environ['LIBRARIES_LOG_LEVEL'] = 'ERROR'
os.environ['ELK_ENABLED'] = 'False'
os.environ['FILE_ENABLED'] = 'True'

from api import app

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(7003), debug=True)
