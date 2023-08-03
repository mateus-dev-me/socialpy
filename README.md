# Socialpy

## Sobre o Projeto 

 A Ideia desse projeto é ser uma API REST de uma rede social baseada no Twitter, onde um usuário
pode fazer publicações sobre o que está pensando e fazendo.

## Tecnologias usadas

- Poetry
- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy
- Taskipy
- Dynaconf
- Typer
- Ruff
- isort
- blue


## Todo

- [x] Definir estrutura do projeto.
- [x] Criar conexão com o Banco de dados.
- [x] Definir Models.
    - [x] Entindade User.
    - [x] Entindade Posts.
    - [x] Criar Entidades Associativas.
        - [x] Follower.
        - [x] Like.
        - [x] Share.
- [ ] Criar Views de Auth.
    - [ ] Definir endpoint access_token.
    - [ ] Definir endpoint refresh_token.
- [ ] Criar Views de CRUD do usuário.
    - [ ] Definir endpoint para registrar um usuário.
    - [ ] Definir um endpoint para retornar informações do usuário.
    - [ ] Definir um endpoint para atualizar informações de um usuário.
    - [ ] Definir um endpoint  deletar um usuário.
- [ ] Criar Views de CRUD de Posts.
    - [ ] Definir enpoint para publicar um post.
    - [ ] Definir um endpoint que listas os posts mais recentes.
    - [ ] Definir um endpoint para compartilhar um post.
    - [ ] Definir um endpoint para curtir um post.
- [ ] Pipeline
    - [ ] Criar Pipeline de Lint/Test.
    - [ ] Criar Pipeline de Deploy.


## Tests

- [x] Tests de Modelos
    - [x] Criar Test que verifica se é possível criar um resgitro de User.
    - [x] Criar Test que verifica se é possível criar um resitro de Post.

- [ ] Tests de Views
    - [ ] Criar Test que verifca se um usuário pode curtir uma publicação.
    - [ ] Criar Test que verifica se um usuário pode compartilhar uma publicação.
        - [ ] Verificar também se ele pode compartilhar a própria publicação, na qual
        não deve ser permitido.
    - [ ] Criar Test que verifica se um usuário pode excluir a publicação de outro usuário.
    - [ ] Criar Test que verifica se um usuário pode seguir outro usuário.
    - [ ] Criar Test que verifica se um usuário pode seguir ele mesmo, na qual não deve ser possível. 

- [ ] Test de Security
    - [ ] Criar Test que verifica se um usuário pode acessar um endpoint sem autorização.
    - [ ] Criar Test que verifica o tempo de expiração do access_token.
