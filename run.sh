export PYTHONPATH="${PYTHONPATH}:/brasa"

# Migrate DB
# python3 brasa/utils/register_bots.py

# Execute WSGI server
gunicorn -c gunicorn_config.py brasa.app:app
