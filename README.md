# PDF2Readable

OCR service for converting PDF documents into readable, searchable text using Apache Tika and Tesseract.

## Overview

A microservice that processes PDF and image files through an OCR pipeline, extracting text content for further processing. Supports async processing via Celery, cloud storage via AWS S3, and multiple deployment options.

## Project Structure

```
├── common/              # Shared utilities and AWS service clients
├── config/              # Configuration files
├── services/            # Business logic services
├── celery/              # Async task queue processing
├── tika-server/         # Apache Tika server configuration
├── postman/             # API testing collection
├── .devcontainer/       # VS Code dev container config
├── api.py               # Flask API entry point
├── main.py              # Application entry point
├── Dockerfile_dev       # Development Docker image
├── Dockerfile_prod      # Production Docker image
├── serverless.yml       # AWS Lambda deployment
└── requirements.txt
```

## Tech Stack

- **Language:** Python 3
- **OCR:** Apache Tika, Tesseract
- **API:** Flask + Gunicorn
- **Queue:** Celery
- **Cloud:** AWS (S3, Lambda)
- **Deployment:** Docker, Serverless Framework

## Getting Started

### Docker (recommended)
```bash
docker compose build
docker-compose -p "ocr" up
```

### Local Development
```bash
cp .env.example .env
pip install -r requirements.txt
python main.py
```

## Configuration

Create a `.env` file from the template:
```bash
cp .env.example .env
```

Required variables:
```
TIKA_CLIENT_ONLY=True
TIKA_SERVER_ENDPOINT=http://127.0.0.1:9998
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

**Jose** — [@aifriend](https://github.com/aifriend)
