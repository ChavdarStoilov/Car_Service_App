FROM python:3.10.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt upgrade -y && apt-get install -y postgresql-client gcc python3-dev musl-dev netcat

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY . /app/
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# run entrypoint.sh
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]