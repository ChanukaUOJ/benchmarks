FROM python:3.10-slim

RUN mkdir /app
WORKDIR /app

# Create a new user with UID 10014
RUN addgroup --gid 10014 choreo && \
    adduser --uid 10014 --ingroup choreo --disabled-password --no-create-home choreouser

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY opengin/api/perf /app

RUN chown -R choreouser:choreo /app

USER 10014

EXPOSE 8089

CMD ["sh", "-c", "locust -f ${LOCUST_FILE:-locust.py} \
  --host=${LOCUST_HOST} \
  --users=${LOCUST_USERS:-50} \
  --spawn-rate=${LOCUST_SPAWN_RATE:-5} \
  --run-time=${LOCUST_RUN_TIME:-5m}" ]
