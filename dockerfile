FROM apache/airflow:2.9.3

COPY requirements.txt .
RUN pip install --no-cahe-dir -r requirements.txt

