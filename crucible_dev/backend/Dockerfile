FROM python:3.12.9

#Set working directory
WORKDIR /app

#Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy application code
COPY app/ ./app

# #Copy environment variables (dotenv will load this at runtime)
# COPY .env .env

#Expose FastAPI port
EXPOSE 8000

#Launch the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]