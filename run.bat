set FLASK_APP=api.py
set FLASK_DEBUG=1
set ELK_URL=https://search-samelan-elk-sandbox-4vyd2rkds6jljgamh7aofo6qam.eu-west-1.es.amazonaws.com
set LOG_FILE=logFile.log
set ELK_INDEX=gbcml-
set APPLICATION=GBC.OCR.IMAGE.PDF2READABLE
set ENVIRONMENT=Development
set LOG_LEVEL=DEBUG
set LIBRARYS_LOG_LEVEL=ERROR
set ELK_ENABLED=False
set FILE_ENABLED=True

python -m flask run -h 0.0.0.0 -p 7003 --reload
