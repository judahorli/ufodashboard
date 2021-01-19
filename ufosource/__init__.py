"""Initialize Flask app."""
from flask import Flask

def init_app():
    """Construct core Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.debug = False

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        from .plotlydashboard.dashboard import init_dashboard
        app = init_dashboard(app)

        return app

