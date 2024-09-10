import dotenv

# Load .env vars
dotenv.load_dotenv(".prod.env", override=False)
dotenv.load_dotenv(".dev.env", override=False)

from project.utils import config as conf

bind = conf.GUNICORN_BIND
workers = conf.GUNICORN_WORKERS
worker_class = conf.GUNICORN_WORKER_CLASS
timeout = conf.GUNICORN_TIMEOUT

if conf.FLASK_ENV == "dev":
    reload = True
