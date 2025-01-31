FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*
RUN pip install flask gunicorn yfinance matplotlib

# Copy project files
COPY update_graphs.py /app
COPY stocks.txt /app

# Create log directory for cron
RUN mkdir -p /var/log/cron

# Copy crontab file and set permissions
COPY crontab /etc/cron.d/update_cron
RUN chmod 0644 /etc/cron.d/update_cron && crontab /etc/cron.d/update_cron

# Start cron and run Gunicorn
CMD cron && gunicorn -w 4 -b 0.0.0.0:5000 app:app
