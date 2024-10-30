
FROM python:3.11-slim


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /abanTask


COPY requirements.txt /abanTask/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /abanTask/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
