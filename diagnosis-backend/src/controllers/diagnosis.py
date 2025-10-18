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
from pymongo import MongoClient
import bson.json_util as json_util # for _id of mongo documents

try:
    db_client = MongoClient("mongodb://localhost:27017")
    db = db_client["hospital"]
    collection = db["diagnosis_records"]
    collection2 = db["last_diagnosis_id"]
    
except Exception as e:
    raise Exception(
            "This error occured in mongodb connection", e)

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
getDiagsController = Namespace("get all diagnosises", path="/diags",
                               description="get all list of diagnosises")

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
        diag_records_cursor = collection.find()
        if not diag_records_cursor:
            return {"error":"db error in collection retrieval"},502

        # here, could have converted all db docs to class object then dumped to json list 
        # but the already dict items are faster to dumpt to json
        diag_dict_list = []
        for diag_dict_record in diag_records_cursor:
            print("type--->",type(diag_dict_record))
            diag_dict_record.pop("_id")
            diag_dict_list.append(diag_dict_record)
        
        print("type of list->>>",type(diag_dict_list))
        print("size ->>",len(diag_dict_list))
        print("start[[[\n",diag_dict_list,"]]]end")
        return json.loads(json.dumps(diag_dict_list)),200
        return diag_dict_list,200

            
            # new_diag_obj = diagnosis_model()
            # new_diag_obj.diagnosis_id = diag_record["diagnosis_id"]
            # new_diag_obj.patient_id = diag_record["patient_name"]
            # new_diag_obj.patient_name = diag_record["patient_name"]
            # new_diag_obj.diagnosis = diag_record[""]
            # new_diag_obj.date = diag_record["patient_name"]
        # return_string = json.dumps(diagnosis_records, indent=4, cls=diagnosis_model_encoder)
        # return_data = json.loads(return_string)
        # print("returning this ->",return_string,"<-")
        # return return_data, 201

@diagController.route("/<int:search_id>")
class Diagnosis(Resource):
    # @getDiagsController.marshal_with(diagFullModel)
    def get(self,search_id):
        # TODO db: all records
        print("got search id->>>> ",search_id)
        record = collection.find_one({"diagnosis_id":search_id})
        if not record:
            return {"error":"DB error in finding or Record Not Found!"},404
        # for record in found_record_cursor:

        record.pop("_id")
        print("type ? ->>",type(record))
        print("record ->>",record)
        # records.append(record)
        return record, 200


        # for diag in diagnosis_records:
        #     if diag.diagnosis_id == get_id:
        #         print("found id, for returning",get_id)
        #         return_obj = json.loads(json.dumps(diag,cls=diagnosis_model_encoder))
        #         return return_obj,201
        # return {"error":"diagnosis id not found!"},404


@diagController.route("/")
class Diagnosis(Resource):

    @diagController.expect(diagModel)
    def post(self):
        exists = collection2.find_one({})
        if not exists:
            collection2.insert_one({"last_diagnosis_id":0})
        collection2.find_one_and_update(
            {},
            {"$inc": {"last_diagnosis_id":1} },
        )
        new_diagnosis_id_cursor = collection2.find()
        print(new_diagnosis_id_cursor)
        for diagnosis_itr in new_diagnosis_id_cursor:
            new_diagnosis_id = diagnosis_itr["last_diagnosis_id"]

        got_record = diagController.payload
        new_diag = diagnosis_model()
        new_diag.diagnosis_id = new_diagnosis_id 
        new_diag.patient_id = got_record['patient_id'] 
        new_diag.patient_name = got_record['patient_name'] 
        new_diag.diagnosis = got_record['diagnosis'] 
        new_diag.date = got_record['date'] 

        return_obj = json.loads(json.dumps(new_diag,cls=diagnosis_model_encoder))
        new_diag_dict = vars(new_diag)
        insert_result = collection.insert_one(new_diag_dict)
        if insert_result:
            return return_obj, 200
        else:
            return {"error":"monogo insert error"}, 501

    @diagController.expect(diagFullModel)
    def put(self):
        got_record = diagController.payload
        search_id = got_record["diagnosis_id"]

        return_obj = diagnosis_model()
        return_obj.patient_id =  got_record['patient_id']
        return_obj.diagnosis_id =  got_record['diagnosis_id']
        return_obj.patient_name =  got_record['patient_name']
        return_obj.diagnosis =  got_record['diagnosis']
        return_obj.date =  got_record['date']
        updated = collection.find_one_and_update(
                {"diagnosis_id": search_id },
                {"$set": {
                    "patient_id": got_record['patient_id'],
                    "diagnosis_id": got_record['diagnosis_id'],
                    "patient_name": got_record['patient_name'],
                    "diagnosis": got_record['diagnosis'],
                    "date": got_record['date'],
                    }
                 }
        )
        if updated:
            return return_obj.__dict__, 200
        else:
            return {"Error":"db error or Record not Found!"}, 404

        # for diag in diagnosis_records:
        #     if diag.diagnosis_id == got_record['diagnosis_id']:
        #         print("found id, for updating",got_record['diagnosis_id'])
        #         diag.patient_id = got_record['patient_id'] 
        #         diag.patient_name = got_record['patient_name'] 
        #         diag.diagnosis = got_record['diagnosis'] 
        #         diag.date = got_record['date'] 

        #         return_obj = json.loads(json.dumps(diag,cls=diagnosis_model_encoder))
        #         return return_obj,201
        # return {"error": "Diagnosis ID not found"}, 404

    @diagController.expect(diagID)
    def delete(self):
        search_id = diagController.payload["diagnosis_id"]

        delete_result = collection.delete_one(
                {"diagnosis_id": search_id}
        )

        if delete_result.deleted_count > 0:
            return {"Success":"deleted One record with id {}".format(search_id)}, 200
        else:
            return {"Error":"Record not found!"},404


        # # TODO DB
        # remove_ind=-1
        # for ind in range(len(diagnosis_records)):
        #     if diagnosis_records[ind].diagnosis_id == remove_id:
        #         remove_ind = ind
        #         print("found id, for deleting",remove_id)
        # if remove_ind>-1:
        #     diagnosis_records.pop(remove_ind)
        #     return {"success": "Removed diagnosis Id {}".format(remove_id)}, 404
        # else:
        #     return {"error": "Id not found"}, 404

