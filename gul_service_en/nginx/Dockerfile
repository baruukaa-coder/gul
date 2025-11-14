FROM python:3.11-slim

# Install certificates for TLS (обязательно для MongoDB Atlas)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates openssl \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 10000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]

