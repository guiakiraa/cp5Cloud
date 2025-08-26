# Usa Python 3.10 como base
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências necessárias
RUN pip install --no-cache-dir fastapi uvicorn mysql-connector-python

# Cria um usuário não-root
RUN useradd -m appuser
USER appuser

# Expõe a porta do Uvicorn
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
