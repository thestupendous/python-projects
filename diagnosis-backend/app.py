'''
patients diagnosis model -
patient_id - int
diagnosis_id - int
name - str
diagnosis - str
date - str (in format yyyy-mm-dd)


routes -
GET - /diags - all patients id's and names
GET - /diag/id - get all details of specific patient
POST - /diag - add a record
PUT - /diag - update a record
POST - /diag - add a record
DELETE - /diag - delete a record
Documentation - /doc - full SwaggerUI api documentation
'''

from flask import Flask
from flask_restx import Api
from src.controllers.diagnosis import diagController, getDiagsController




app = Flask(__name__)
api = Api(app,
          title="Diagnosis records of Hospital Amrit",
          description="Diagnosis records of Hospital Amrit",
          version="1.0",
          doc="/doc",
          validate=True
          )
api.add_namespace(diagController)
api.add_namespace(getDiagsController)


if __name__ == '__main__':
    app.run('0.0.0.0',5005)
