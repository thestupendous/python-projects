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
from flask_restx import Namespace, Resource, fields
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

diagController = Namespace("diagnosis", path="/diag", description="Diagnosis records api controller")
getDiagsController = Namespace("get all diagnosises", path="/diags", description="get all list of diagnosises")

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

diagID = diagController.model("diagnosisID",{
    'diagnosis_id': fields.Integer(required=True, description="diagnosis ID"),
})

@getDiagsController.route("/")
class GetDiagnosises(Resource):
    @getDiagsController.marshal_list_with(diagFullModel)
    def get(self):
        # TODO db: all records
        return_string = json.dumps(diagnosis_records, indent=4, cls=diagnosis_model_encoder)
        return_data = json.loads(return_string)
        print("returning this ->",return_string,"<-")
        return return_data, 201

@diagController.route("/")
class Diagnosis(Resource):
    @diagController.expect(diagID)
    # @diagController.marshal_with(diagFullModel)
    def get(self):
        # TODO db: all records
        get_id = diagController.payload['diagnosis_id']
        for diag in diagnosis_records:
            if diag.diagnosis_id == get_id:
                print("found id, for returning",get_id)
                return_obj = json.loads(json.dumps(diag,cls=diagnosis_model_encoder))
                return return_obj,201
        return {"error":"diagnosis id not found!"},404

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

    @diagController.expect(diagFullModel)
    def put(self):
        got_record = diagController.payload

        # TODO DB
        for diag in diagnosis_records:
            if diag.diagnosis_id == got_record['diagnosis_id']:
                print("found id, for updating",got_record['diagnosis_id'])
                diag.patient_id = got_record['patient_id'] 
                diag.patient_name = got_record['patient_name'] 
                diag.diagnosis = got_record['diagnosis'] 
                diag.date = got_record['date'] 

                return_obj = json.loads(json.dumps(diag,cls=diagnosis_model_encoder))
                return return_obj,201
        return {"error": "Diagnosis ID not found"}, 404

    @diagController.expect(diagID)
    def delete(self):
        got_record = diagController.payload
        remove_id = got_record['diagnosis_id']

        # TODO DB
        remove_ind=-1
        for ind in range(len(diagnosis_records)):
            if diagnosis_records[ind].diagnosis_id == remove_id:
                remove_ind = ind
                print("found id, for deleting",remove_id)
        if remove_ind>-1:
            diagnosis_records.pop(remove_ind)
            return {"success": "Removed diagnosis Id {}".format(remove_id)}, 404
        else:
            return {"error": "Id not found"}, 404

