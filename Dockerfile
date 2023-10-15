FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

RUN pip install gunicorn

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predictdock.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predictdock:app"]