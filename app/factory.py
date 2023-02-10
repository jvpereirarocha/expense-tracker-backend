from flask import Flask
from app.rest import api_v1
from infra.database.adapters.mappers import start_mappers

def create_app(environment: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(f"app.config.configurations.{environment.capitalize()}Config")
    start_mappers()
    app.register_blueprint(api_v1)
    
    return app
