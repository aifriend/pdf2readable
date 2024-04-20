export FLASK_APP=api.py
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export ELK_URL=https://search-samelan-elk-sandbox-4vyd2rkds6jljgamh7aofo6qam.eu-west-1.es.amazonaws.com
export LOG_FILE=logFile.log
export ELK_INDEX=gbcml-
export APPLICATION=GBC.OCR.IMAGE.PDF2READABLE
export ENVIRONMENT=Development
export LOG_LEVEL=DEBUG
export LIBRARYS_LOG_LEVEL=ERROR
export FILE_ENABLED=True
export ELK_ENABLED=False

python -m ptvsd --host 0.0.0.0 --port 5678 --wait -m flask run -h 0.0.0.0 -p 7003
