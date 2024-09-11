from brasa import config as conf

bind = conf.GUNICORN_BIND
workers = conf.GUNICORN_WORKERS
worker_class = conf.GUNICORN_WORKER_CLASS
timeout = conf.GUNICORN_TIMEOUT

if conf.FLASK_ENV == "dev":
    reload = True
