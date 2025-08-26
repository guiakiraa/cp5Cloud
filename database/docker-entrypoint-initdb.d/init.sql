USE meubanco;

CREATE TABLE usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO usuario(nome, email) VALUES('Guilherme Akira', 'guiakira@fiap.com.br');
INSERT INTO usuario(nome, email) VALUES('Anne Rezendes', 'annere@fiap.com.br');
INSERT INTO usuario(nome, email) VALUES('Alice Nunes', 'alicenunes@fiap.com.br');