FROM python:3.9

WORKDIR /app
COPY requirements.txt /app/
COPY wheels/simpledb-0.1.0-py3-none-any.whl /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir simpledb-0.1.0-py3-none-any.whl
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]