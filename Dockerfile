FROM --platform=linux/amd64 apache/airflow:2.8.1

RUN pip install apache-airflow-providers-airbyte == 3.5.1 \
  apache-airflow-providers-mongo==3.5.0 \
  airflow-provider-great-expectations==0.2.7
