# Openmrs-contrib-telemedicine-proxy
This repository contains a reverse proxy for the OpenMRS server. It helps increase security of the server from illegal access
and other attempts to harm the server. The proxy has been developed using [Flask](https://flask.palletsprojects.com/en/1.0.x/) 
and [Gunicorn](https://gunicorn.org/) as the WSGI client. 
<br>
#### The Flask app has two endpoints 
- fetch - For fetching the unique patient Uuid.
- register - For registering the patient with user provided detail

The proxy server runs inside a docker container in a python 3.6 environment. The container exposes port `3000` to the host machine.
This container is under use at the main fortitudo-infrastructure and is added to its docker-compose file.This proxy was specially designed 
for the project [Nigeria Telemedicine App](https://github.com/openmrs/openmrs-contrib-telemedicine-app).
