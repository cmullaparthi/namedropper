FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    zlib1g-dev \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        spacy==3.7.2 \
        numpy==1.24.4 \
        fastapi \
        uvicorn[standard] \
        langdetect \
        pytest \
        jieba \
        kiwipiepy \
    && python -m spacy download en_core_web_sm \
    && python -m spacy download fr_core_news_sm \
    && python -m spacy download de_core_news_sm \
    && python -m spacy download es_core_news_sm \
    && python -m spacy download ja_ginza

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
