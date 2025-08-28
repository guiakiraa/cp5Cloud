
# CP5 Docker Compose

Este projeto utiliza **Docker Compose** para orquestrar um ambiente completo com **MySQL**, **Backend em Python (FastAPI)** e **Frontend em Next.js**.

## ✅ Pré-requisitos

- Docker instalado na máquina
- Docker Compose instalado (vem junto com Docker Desktop)
- Git (opcional, para clonar o repositório)

## 🔧 Configuração Inicial

### 1. Clonar o repositório

```bash
git clone https://github.com/guiakiraa/cp5Cloud
cd cp5Cloud
```

### 2. Criar arquivo .env

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

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

### Passo 1: Construir e subir todos os serviços

```bash
docker compose up -d --build
```

Este comando irá:
- Construir as imagens Docker para todos os serviços
- Criar a rede `cloud-network`
- Criar o volume `db_data` para persistência do MySQL
- Subir todos os containers em modo detached (background)

### Passo 2: Verificar se todos os serviços estão rodando

```bash
docker compose ps
```

Você deve ver algo similar a:
```
NAME                COMMAND                  SERVICE             STATUS              PORTS
backend             "uvicorn main:app --…"   backend             running             0.0.0.0:8000->8000/tcp
frontend            "npm run dev"            frontend             running             0.0.0.0:3000->3000/tcp
mysql-db            "docker-entrypoint.s…"   mysql-db             running             0.0.0.0:3306->3306/tcp
```

### Passo 3: Verificar os logs dos serviços

```bash
# Ver logs de todos os serviços
docker compose logs

# Ver logs de um serviço específico
docker compose logs backend
docker compose logs frontend
docker compose logs mysql-db

# Acompanhar logs em tempo real
docker compose logs -f
```

---

## 🗄️ Acessando o Banco de Dados

### Conectar ao MySQL e verificar dados

```bash
# Entrar no container do MySQL
docker exec -it mysql-db mysql -u root -p
```

Senha: `root`

### Comandos SQL úteis

```sql
-- Verificar se está no banco correto
USE meubanco;

-- Verificar tabelas existentes
SHOW TABLES;

-- Verificar dados da tabela usuario
SELECT * FROM usuario;

-- Verificar estrutura da tabela
DESCRIBE usuario;

-- Sair do MySQL
exit
```

### Verificar dados diretamente via comando

```bash
# Executar SELECT diretamente
docker exec -it mysql-db mysql -u root -proot -e "USE meubanco; SELECT * FROM usuario;"
```

---

## 🖥️ Acessando a Aplicação

### Frontend
```
http://localhost:3000
```

### Backend (API)
```
http://localhost:8000
```


---

## 🔧 Comandos Docker Úteis

### Gerenciamento de Containers

```bash
# Ver status dos containers
docker compose ps

# Ver logs dos containers
docker compose logs

# Parar todos os serviços
docker compose down

# Parar e remover volumes
docker compose down -v

# Reiniciar um serviço específico
docker compose restart backend

# Reconstruir e subir um serviço específico
docker compose up -d --build backend
```

### Inspeção do Sistema

```bash
# Listar volumes Docker
docker volume ls

# Listar redes Docker
docker network ls

# Ver logs de um container específico
docker container logs mysql-db
docker container logs backend
docker container logs frontend

# Ver logs em tempo real
docker container logs -f mysql-db
```

### Limpeza do Sistema

```bash
# Remover containers parados, redes não utilizadas, imagens e volumes
docker system prune -a -f --volumes

# Remover apenas containers parados
docker container prune

# Remover apenas imagens não utilizadas
docker image prune -a

# Remover apenas volumes não utilizados
docker volume prune
```

---

## 🛠️ Troubleshooting

### Problema: Container não inicia

```bash
# Verificar logs detalhados
docker compose logs [nome-do-servico]

# Verificar se as portas estão disponíveis
netstat -an | grep :3000
netstat -an | grep :8000
netstat -an | grep :3306
```

### Problema: Banco de dados não conecta

```bash
# Verificar se o MySQL está rodando
docker compose ps mysql-db

# Testar conexão com o banco
docker exec -it mysql-db mysql -u root -proot -e "SHOW DATABASES;"

# Verificar logs do MySQL
docker compose logs mysql-db
```

### Problema: Frontend não carrega

```bash
# Verificar se o backend está respondendo
curl http://localhost:8000

# Verificar logs do frontend
docker compose logs frontend

# Verificar se as variáveis de ambiente estão corretas
docker exec -it frontend env | grep NEXT_PUBLIC
```

### Problema: Erro de permissão

```bash
# Reconstruir containers com permissões corretas
docker compose down
docker compose up -d --build
```

### Problema: Porta já em uso

```bash
# Verificar processos usando as portas
lsof -i :3000
lsof -i :8000
lsof -i :3306

# Parar processo conflitante ou alterar portas no docker-compose.yaml
```

---

## 🧹 Limpeza Completa

Para remover completamente o projeto e todos os recursos Docker:

```bash
# Parar e remover containers, redes e volumes
docker compose down -v

# Remover imagens do projeto
docker rmi $(docker images -q cp5cloud_*)

# Limpeza completa do sistema Docker
docker system prune -a -f --volumes
```

---

## 📁 Estrutura do Projeto

```
cp5Cloud/
├── docker-compose.yaml    # Configuração do Docker Compose
├── .env                   # Variáveis de ambiente
├── backend/               # Backend FastAPI
│   ├── Dockerfile
│   └── main.py
├── frontend/              # Frontend Next.js
│   ├── Dockerfile
│   └── src/
└── database/              # Configurações do MySQL
    ├── Dockerfile
    └── docker-entrypoint-initdb.d/
        └── init.sql
```

---

## 🔄 Fluxo de Desenvolvimento

1. **Desenvolvimento**: Edite os arquivos no seu editor
2. **Teste**: `docker compose up -d --build`
3. **Verificação**: `docker compose logs -f`
4. **Limpeza**: `docker compose down -v`

---

## 📞 Suporte

Em caso de problemas:
1. Verifique os logs: `docker compose logs`
2. Consulte a seção de troubleshooting
3. Verifique se todas as portas estão disponíveis
4. Certifique-se de que o arquivo `.env` está configurado corretamente
