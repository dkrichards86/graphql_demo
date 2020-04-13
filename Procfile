release: flask db upgrade
web: gunicorn autoapp:app -b 0.0.0.0:$PORT --access-logfile -