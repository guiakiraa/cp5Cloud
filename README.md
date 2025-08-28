# CP5 Docker Compose

Este projeto utiliza **Docker Compose** para orquestrar um ambiente completo com **MySQL**, **Backend em Python (FastAPI)** e **Frontend em Next.js**.  

---

## 🏗️ Arquitetura da Aplicação  

### 🔹 Antes do Docker Compose  

<img width="702" height="331" alt="Image" src="https://github.com/user-attachments/assets/5c39aea0-fe38-4f26-82c2-11f0ea537183" />

---

### 🔹 Depois do Docker Compose  

<img width="452" height="640" alt="Image" src="https://github.com/user-attachments/assets/d6822ffd-127c-4d89-b646-bff418adc525" />

---

## ✅ Pré-requisitos  

- Docker instalado na máquina  
- Docker Compose instalado (vem junto com Docker Desktop)  
- Git (opcional, para clonar o repositório)  

---

## 🔧 Configuração Inicial  

### 1. Clonar o repositório  

```bash
git clone https://github.com/guiakiraa/cp5Cloud
cd cp5Cloud
```

### 2. Criar arquivo `.env`  

```env
# Configurações do MySQL
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=meubanco
MYSQL_USER=gui
MYSQL_PASSWORD=qwerty123

# URL do banco de dados
DATABASE_URL=mysql://gui:qwerty123@mysql-db:3306/meubanco

# URL da API para o frontend
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 🚀 Deploy com Docker Compose  

```bash
docker compose up -d --build
```

Isso irá:  
- Construir imagens Docker  
- Criar a rede `cloud-network`  
- Criar volume `db_data` para persistência  
- Subir containers em background  

---

## 🗄️ Banco de Dados  

### Acessar MySQL  

```bash
docker exec -it mysql-db mysql -u root -p
```

Senha: `root`  

### Comandos úteis  

```sql
USE meubanco;
SHOW TABLES;
SELECT * FROM usuario;
DESCRIBE usuario;
```

---

## 🖥️ Acessando a Aplicação  

- **Frontend** → [http://localhost:3000](http://localhost:3000)  
- **Backend** → [http://localhost:8000](http://localhost:8000)  

---

## 🛠️ Troubleshooting  

### Container não inicia  
```bash
docker compose logs [nome-do-servico]
```

### Banco de dados não conecta  
```bash
docker compose ps mysql-db
docker exec -it mysql-db mysql -u root -proot -e "SHOW DATABASES;"
```

### Frontend não carrega  
```bash
curl http://localhost:8000
docker compose logs frontend
```

### Porta já em uso  
```bash
lsof -i :3000
lsof -i :8000
lsof -i :3306
```

---

## 📁 Estrutura do Projeto  

```
cp5Cloud/
├── docker-compose.yaml    
├── .env                   
├── backend/               
│   ├── Dockerfile
│   └── main.py
├── frontend/              
│   ├── Dockerfile
│   └── src/
└── database/              
    ├── Dockerfile
    └── docker-entrypoint-initdb.d/
        └── init.sql
```

---

## 🔄 Fluxo de Desenvolvimento  

1. Editar os arquivos  
2. Subir containers → `docker compose up -d --build`  
3. Acompanhar logs → `docker compose logs -f`  
4. Encerrar → `docker compose down -v`  

---

## 📞 Suporte  

Em caso de problemas:  
1. Verifique os logs: `docker compose logs`  
2. Consulte a seção de troubleshooting  
3. Confirme se as portas estão disponíveis  
4. Verifique se o `.env` está configurado corretamente  
