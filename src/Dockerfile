# Utiliza a imagem do Python 3.10 (Alpine Linux)
FROM python:3.10

# Baixa msodbcsql18 e unixodbc-dev para conexão com o banco de dados
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg && \
    curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && apt-get install -y \
    unixodbc-dev \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Seta variáveis de ambiente necessárias
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala as dependencias de ambiente
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

# Cria o diretório de trabalho
WORKDIR /app
COPY . /app

# Roda o comando python para iniciar a API
CMD  ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]