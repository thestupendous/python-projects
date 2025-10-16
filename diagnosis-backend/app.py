'''

patients model -
patient_id - int
diagnosis_id - int
name - str
diagnosis - str
date - str (in format yyyy-mm-dd)


routes -
GET - /patients - all patients id's and names
GET - /patient/{id} - get all details of specific patient
POST - /patient - add a record
PUT - /patient/{id} - update a record
POST - /patient - add a record
DELETE - /patient - delete a record

'''


from flask import Flask, request
from flask import Response, session


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h2>Ram Ram on Home Page!</h2>'

@app.route('/patients',methods=['GET'])
def getAllRecords():
    return '<h3>You are at "get all patients names" page</h3>'


@app.route('/patient',methods=['GET'])
def getOnePatientRecords():
    return '<h3>You are at "get 1 patient records" page</h3>'

@app.route('/diagnosis',methods=['GET'])
def getOneDiagnosisRecord():
    return '<h3>You are at "get 1 diagnosis record" page</h3>'


@app.route('/diagnosis',methods=['post'])
def addRecord():
    return '<h3>You are at "add record" page</h3>'

@app.route('/diagnosis',methods=['put'])
def updateRecord():
    return '<h3>You are at "update record" page</h3>'

@app.route('/diagnosis',methods=['delete'])
def deleteRecord():
    return '<h3>You are at "delete record" page</h3>'

if __name__ == '__main__':
    app.run('0.0.0.0',5005,debug=True)

