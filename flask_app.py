from flask import Flask
import requests
from flask import request
app = Flask(__name__)

url= 'https://openmrs-staging.callnigeriandoc.com/openmrs/module/idgen/generateIdentifier.form?source=1&username=admin&password=Admin123'
registerUrl='https://openmrs-staging.callnigeriandoc.com/openmrs/ws/rest/v1/patient'
username= 'telemedtest3'
password= 'Asdfg123'


@app.route('/fetch')
def hello_world():
   response = requests.get(url)
   return (response.text)

@app.route('/register',methods=['POST'])
def register_patient():
    print(request.get_json(force=True))
    response = requests.post(registerUrl,auth=(username,password), json=request.get_json(force=True))
    return response.text


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)