# Usa Node.js 18 como base
FROM node:18

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências
RUN npm install

# Cria um usuário não-root
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expõe a porta padrão do Next.js
EXPOSE 3000

# Comando padrão para rodar em modo desenvolvimento
CMD ["npm", "run", "dev"]
