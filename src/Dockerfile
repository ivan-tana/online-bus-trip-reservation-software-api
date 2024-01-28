FROM python:3.11.6

WORKDIR /api  

COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt 

COPY ./api . 

EXPOSE 8000  

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  
