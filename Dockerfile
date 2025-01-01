FROM python:3.12.8-slim

WORKDIR /app

# Install system-level dependencies for tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set non-root user for added security
RUN useradd -m appuser
USER appuser

# Start app
EXPOSE 80
ENTRYPOINT [ "uvicorn", "app.main:app" ]
CMD [ "--host", "0.0.0.0", "--port", "80" ]