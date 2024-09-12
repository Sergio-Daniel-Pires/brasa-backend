import dotenv
from flask import Flask

# Load .env vars
dotenv.load_dotenv(".prod.env", override=False)
dotenv.load_dotenv(".dev.env", override=False)


from flask import Flask
from flask_restx import Api

from brasa._version import __version__ as API_VERSION
from brasa.metrics_collector import setup_metrics
from brasa.services.events.routes import events_ns
from brasa.services.sports.routes import sports_ns
from brasa.utils.logger import log

# Create flask swagger API
api = Api(
    title="Brasa App Backend",
    description="A simple flask backend for Brasa App",
    version=API_VERSION,
    doc="/docs"
)

def create_app() -> Flask:
    """
    Create an app with a given name
    """

    app = Flask(__name__)

    # Add routes
    # Events routes
    log.info("Adding routes")
    api.add_namespace(events_ns, path="/events")
    # Sports routes
    api.add_namespace(sports_ns, path="/sports")
    log.info("Routes added")

    log.info("Initializing API")
    api.init_app(app)

    return app

app = create_app()
setup_metrics(app)

if __name__ == "__main__":
    app.run()