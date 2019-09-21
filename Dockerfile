FROM python:3-alpine

ENV DEV_PROGRA="Daniel Hernández - 20180077"

WORKDIR /webscrapping

COPY . /webscrapping

RUN pip install -r requirements.txt

CMD [ "python", "soup.py" ]