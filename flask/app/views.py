from app import app

import os


@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"<h2>Holla from {app_name}: We are now dockerized people behind Nginx!</h2>"

    return "<h2>Hello from Flask</h2>"
