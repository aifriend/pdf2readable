celery -A gbc_pdf2readable_processor worker --loglevel=info --concurrency 4 --max-tasks-per-child 4 -n worker1
