from flask import Flask
from RequestController import RequestController
import flask_routes

if __name__ == '__main__':
    flask_routes.flask_app.run(debug=True)
