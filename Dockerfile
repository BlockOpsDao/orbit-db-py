FROM python:3.8.6

RUN pip install javascript

COPY pyjs.py pyjs.py

CMD ["python", "pyjs.py"]