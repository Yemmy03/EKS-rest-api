# Stage 1: build dependencies
FROM python:3.11-slim AS builder

# Expose the app port
EXPOSE 8001

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: runtime
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app ./app

# Start App
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
