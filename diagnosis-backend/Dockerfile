# get python
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .

# pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn","--bind","0.0.0.0:8000","app:app","-e", "MONGOHOST=localhost", "-w", "3"]

# gunicorn app:app
