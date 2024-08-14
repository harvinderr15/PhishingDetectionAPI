# Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Install dependencies
RUN pip install flask pandas scikit-learn xgboost

# Copy the model and application files
COPY xgb_model.pkl /app/
COPY app.py /app/

WORKDIR /app

# Run the Flask app
CMD ["flask", "run"]
