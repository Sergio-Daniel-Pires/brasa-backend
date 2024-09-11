export PYTHONPATH="${PYTHONPATH}:/brasa"

# Migrate DB
python3 brasa/utils/register_bots.py

gunicorn -c gunicorn_config.py brasa.app:app
