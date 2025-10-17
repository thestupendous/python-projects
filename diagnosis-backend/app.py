'''

patients model -
patient_id - int
diagnosis_id - int
name - str
diagnosis - str
date - str (in format yyyy-mm-dd)


routes -
GET - /patients - all patients id's and names
GET - /patient - get all details of specific patient
POST - /patient - add a record
PUT - /patient - update a record
POST - /patient - add a record
DELETE - /patient - delete a record

'''

from flask import Flask, request
from flask import Response

from flask_restx import Namespace, Resource, fields
from flask_restx import Api
from typing import List
import json

class diagnosis_model():
    patient_id: int
    diagnosis_id: int
    patient_name: str
    diagnosis: str
    date: str

class diagnosis_model_encoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__



app = Flask(__name__)
api = Api(app,
          title="Diagnosis records of Hospital Amrit",
          description="Diagnosis records of Hospital Amrit",
          version="1.0",
          doc="/doc",
          validate=True
          )
diagController = Namespace("diagnosis", path="/diag", description="Diagnosis records api controller")
api.add_namespace(diagController)


# TODO mongo db will replace this
diagnosis_records: List[diagnosis_model] = []

diagFullModel = diagController.model("diagnosisFullModel",{
    'patient_id': fields.Integer(required=True, description="patient ID"),
    'diagnosis_id': fields.Integer(required=True, description="diagnosis ID"),
    'patient_name': fields.String(required=True, description="patient name"),
    'diagnosis': fields.String(required=True, description="full diagnosis"),
    'date': fields.String(required=True, description="date of diagnosis"),
})

diagModel = diagController.model("diagnosisModel",{
    'patient_id' : fields.Integer(required=True, description="patient ID"),
    # 'diagnosis_id': fields.Int(required=True, description="diagnosis ID"),
    'patient_name': fields.String(required=True, description="patient name"),
    'diagnosis': fields.String(required=True, description="full diagnosis"),
    'date': fields.String(required=True, description="date of diagnosis")
})

diagPatients = diagController.model("diagnosisPatientsModel",{
    'patient_id': fields.Integer(required=True, description="patient ID"),
    'diagnosis_id': fields.Integer(required=True, description="diagnosis ID"),
    'patient_name': fields.String(required=True, description="patient name")
})

@diagController.route("/")
class Diagnosis(Resource):
    def get(self):
        # TODO db: all records
        return json.dumps(diagnosis_records, cls=diagnosis_model_encoder), 201

    @diagController.expect(diagModel)
    def post(self):
        got_record = diagController.payload
        new_diag = diagnosis_model()
        new_diag.patient_id = got_record['patient_id'] 
        new_diag.patient_name = got_record['patient_name'] 
        new_diag.diagnosis = got_record['diagnosis'] 
        new_diag.date = got_record['date'] 

        # calculate diagnosis id
        # TODO fetch last diagnosis Id from DB
        diagId = 1 if len(diagnosis_records)==0 else 1+max([x.diagnosis_id for x in diagnosis_records])
        new_diag.diagnosis_id = diagId
        diagnosis_records.append(new_diag)
        return {"message": "record added", "diagnosis_id": diagId}, 201






if __name__ == '__main__':
    app.run('0.0.0.0',5005,debug=True)

# @app.route('/', methods=['GET'])
# def home():
#     response = Response(json.dumps(diagnosis_records, default=str), mimetype='application/json')
#     return response
# 
# @app.route('/patients',methods=['GET'])
# def getAllRecords():
#     return '<h3>You are at "get all patients names" page</h3>'
# 
# 
# @app.route('/patient',methods=['GET'])
# def getOnePatientRecords():
#     return '<h3>You are at "get 1 patient records" page</h3>'
# 
# @app.route('/diagnosis',methods=['GET'])
# def getOneDiagnosisRecord():
#     return '<h3>You are at "get 1 diagnosis record" page</h3>'
# 
# 
# @app.route('/diagnosis',methods=['post'])
# def addRecord():
#     return '<h3>You are at "add record" page</h3>'
# 
# @app.route('/diagnosis',methods=['put'])
# def updateRecord():
#     return '<h3>You are at "update record" page</h3>'
# 
# @app.route('/diagnosis',methods=['delete'])
# def deleteRecord():
#     return '<h3>You are at "delete record" page</h3>'

