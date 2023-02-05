FROM python:3.10

RUN mkdir -p /home/app

RUN groupadd app && useradd -g app app

ENV APP_HOME=/home/app/api
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install -e .

RUN chown -R app:app $APP_HOME
USER app

CMD ["uvicorn","socialpy.app:app","--reload", "--host", "0.0.0.0", "--port", "8000"]
