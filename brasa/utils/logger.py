import logging

logging.basicConfig(filename="/var/log/brasa.log")
formatter = logging.Formatter(
    "[%(asctime)s] %(pathname)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Handler para o console
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Logger personalizado
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(handler)
