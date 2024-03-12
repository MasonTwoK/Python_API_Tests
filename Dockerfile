FROM python:latest

RUN pip install pytest
RUN pip install requests

WORKDIR /app
COPY . /app

CMD ["pytest", "-v"]