from flask import Flask
from flask_restx import Api
from src.controllers.todos import todosCtrlr

app = Flask(__name__)

# @app.route("/")
# def root_route():
#     return "Raam Raam!"

api = Api(app,
          title="example api app",
          description="example api app",
          version="1.0",
          doc="/swagger/",
          validate=True)

api.add_namespace(todosCtrlr)


app.run(host='0.0.0.0',port=5000,debug=True)
