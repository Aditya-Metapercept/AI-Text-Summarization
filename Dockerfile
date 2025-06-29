FROM python:3.13.5

# set the working directory 
WORKDIR /app

#Copy your application code 
COPY . .
# install the dependency 
RUN python -m pip install -r requirements.txt

RUN mkdir -p /app/logs && chmod -R 777 /app/logs

# Expose the port fastapi will run on it
EXPOSE 5000
# command to run the fastapi app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "app.py"]
