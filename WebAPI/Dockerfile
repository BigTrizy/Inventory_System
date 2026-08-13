FROM python:3.13.14

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/scripts
COPY ./tests /app/tests
COPY ./pytest.ini /app/pytest.ini

CMD ["uvicorn", "scripts.main:app", "--host", "0.0.0.0", "--port", "9001"]