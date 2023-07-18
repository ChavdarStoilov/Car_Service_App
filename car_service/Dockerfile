FROM python:3.10.11

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt upgrade -y && apt-get install -y postgresql-client gcc python3-dev musl-dev netcat

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/bin/bash", "/usr/src/app/entrypoint.sh"]