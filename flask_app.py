from flask import Flask
import requests
from flask import request
app = Flask(__name__)
import os

openmrs_host = 'http://refapp:8080/'
idgen_path = 'openmrs/module/idgen/generateIdentifier.form?source=1&username=admin&password=Admin123'
registeration_path ='openmrs/ws/rest/v1/patient'

username = os.environ['MOBILE_USERNAME']
password = os.environ['MOBILE_PASSWORD']


@app.route('/fetch')
def hello_world():
   response = requests.get(openmrs_host + idgen_path)
   return (response.text)

@app.route('/register',methods=['POST'])
def register_patient():
   print(request.get_json(force=True))
   response = requests.post(
      openmrs_host + registeration_path,
      auth=(username,password), 
      json=request.get_json(force=True)
   )
   
   return response.text


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)