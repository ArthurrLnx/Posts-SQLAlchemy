# Blog com Comentários - Flask e SQLAlchemy
Este é um projeto simples de blog desenvolvido com Flask e SQLAlchemy que permite criar posts e adicionar comentários a eles.

# Funcionalidades
- Criação automática de posts iniciais

- Listagem de todos os posts

- Adição de comentários a posts específicos

- Armazenamento de dados em banco SQLite

- Estrutura do Projeto
# Modelos de Dados
**Post:**

- id (Chave primária)

- title (Título do post)

- content (Conteúdo do post)

- Relacionamento one-to-many com Comment

**Comment:**

- id (Chave primária)

- content (Conteúdo do comentário)

- post_id (Chave estrangeira referenciando Post)
