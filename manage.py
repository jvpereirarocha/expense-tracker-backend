from app.factory import create_app
from os import getenv

if __name__ == "__main__":
    environment = getenv("ENVIRONMENT") or "production"
    app = create_app(environment=environment)
    run_as_debug = app.config.get("DEBUG", False)
    port_to_run = app.config.get("PORT")
    app.run(host="127.0.0.1", port=port_to_run, debug=run_as_debug)
