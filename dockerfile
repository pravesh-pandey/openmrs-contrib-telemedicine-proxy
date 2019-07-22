FROM python:3.6
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn requests
EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "wsgi:app"]