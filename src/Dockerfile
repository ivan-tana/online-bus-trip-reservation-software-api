FROM python:3.11.6

WORKDIR /src  

COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt 

COPY ./api ./api 
COPY run.py .

EXPOSE 8000  


CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]  
