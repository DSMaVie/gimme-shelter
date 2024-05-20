FROM python:3.12.3-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


COPY ./dist/gimme_shelter-0.0.1-py3-none-any.whl .
RUN pip install gimme_shelter-0.0.1-py3-none-any.whl --no-cache-dir

COPY src/gimme_shelter/server.py .

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "server.py", "--server.port=8501"]