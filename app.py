from flask import Flask

from endpoints import cv as cv_endpoints
from commands import cv as cv_commands

app = Flask(__name__)

cv_endpoints.register_endpoints(app)
cv_commands.register_commands(app)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
