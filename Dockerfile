FROM python:3.12.3-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY ./src .
COPY ./requirements.txt .

RUN pip install -r requirements.txt
RUN pip install -e gimme_shelter
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "gimme_shelter/server.py", "--server.port=8501", "--server.address=0.0.0.0"]