FROM python:3.9-slim

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia o arquivo app.py do diretório local para o diretório de trabalho no contêiner (/app)
COPY app.py .

# Instala as dependências Python listadas em requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
