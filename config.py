celery worker --app newsClassifier.celery --loglevel=info
celery beat --app newsClassifier.celery --loglevel=info
