import dotenv

# Load .env vars
dotenv.load_dotenv(".prod.env", override=False)
dotenv.load_dotenv(".dev.env", override=False)

from flask import Flask
from flask_restx import Api

from project.services.events.routes import events_ns
from project.services.sports.routes import sports_ns
from _version import __version__ as API_VERSION

# Create flask swagger API
api = Api(
    title="Brasa App Backend",
    description="A simple flask backend for Brasa App ",
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
    api.add_namespace(events_ns, path="/events")
    # Sports routes
    api.add_namespace(sports_ns, path="/sports")

    api.init_app(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()
