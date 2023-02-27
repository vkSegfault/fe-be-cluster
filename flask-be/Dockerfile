FROM python:3.11.1-slim

WORKDIR /app

COPY . /app
RUN pip install pipenv
RUN pipenv install
#RUN pipenv lock -r > requirements.txt
#RUN pip install -r requirements.txt

EXPOSE 5000

# "--host=0.0.0.0" arg is needed to access container
CMD ["python", "-m", "flask", "--app", "main.py", "--debug", "run", "--host=0.0.0.0"]   
# , "--cert=crt.pem", "--key=key.pem"