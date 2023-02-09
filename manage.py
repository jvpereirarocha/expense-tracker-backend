from app.factory import create_app
from os import getenv

if __name__ == "__main__":
    environment = getenv("ENVIRONMENT") or "production"
    app = create_app(environment=environment)
    app.run(host="127.0.0.1", port=5050, debug=True)
