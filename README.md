# Gold Box

## Nome do Projeto

**Gold Box**

Projeto Integrador desenvolvido em Django para criação de um sistema web de uma loja de suplementos alimentares.

## Descrição do Projeto

O **Gold Box** é um sistema web de uma loja de suplementos alimentares, desenvolvido utilizando o framework Django.

O sistema terá como objetivo permitir que os clientes conheçam os produtos disponíveis, realizem cadastro e login, consultem o catálogo e tenham acesso a conteúdos e informações relacionadas a suplementos alimentares.

Além da área destinada aos clientes, o sistema contará com funcionalidades administrativas para gerenciamento dos produtos e das publicações do blog.

O projeto busca solucionar a necessidade de uma loja de suplementos possuir uma plataforma online para divulgar seus produtos, apresentar informações aos clientes e facilitar o acesso aos conteúdos da loja.

O sistema será desenvolvido inicialmente com as seguintes funcionalidades:

* Página inicial da loja;
* Cadastro de usuários;
* Login e logout;
* Catálogo de produtos;
* Categorias de produtos;
* Cadastro e gerenciamento de produtos;
* Blog com dicas e informações;
* Cadastro e gerenciamento de publicações;
* Visualização das publicações;
* Página de contato;
* Área administrativa.

## Tecnologias Utilizadas

As principais tecnologias utilizadas no desenvolvimento do projeto serão:

* **Python** — linguagem de programação utilizada no desenvolvimento do sistema;
* **Django** — framework utilizado para desenvolvimento da aplicação web;
* **HTML** — utilizado para estruturar as páginas do sistema;
* **CSS** — utilizado para estilização e organização visual das páginas;
* **JavaScript** — utilizado para funcionalidades e interações da interface;
* **SQLite** — banco de dados utilizado durante o desenvolvimento;
* **Bootstrap Icons** — utilizado para os ícones da interface.

## Equipe

| Integrante          | Responsabilidade                                                                                     |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| **João Vitor Vaz**  | Desenvolvimento do app `contas`, responsável pelo cadastro, login e autenticação dos usuários.       |
| **Davi Honorato**   | Desenvolvimento do app `produtos`, responsável pelo catálogo, produtos e categorias.                 |
| **Lucas Da Silva**  | Desenvolvimento do app `blog`, responsável pelas publicações, dicas e informações sobre suplementos. |
| **Rayssa Borchatd** | Desenvolvimento do app `institucional`, responsável pela página inicial e página de contato.         |

## Apps Django

O projeto será dividido em quatro aplicativos Django, cada um responsável por uma parte específica do sistema.

### `contas`

Responsável pelas funcionalidades relacionadas aos usuários.

**Principais funcionalidades:**

* Cadastro de usuários;
* Login;
* Logout;
* Autenticação;
* Controle de acesso.

### `produtos`

Responsável pelo catálogo e gerenciamento dos produtos da loja.

**Principais funcionalidades:**

* Cadastro de produtos;
* Listagem de produtos;
* Visualização dos detalhes;
* Edição de produtos;
* Exclusão de produtos;
* Cadastro e organização por categorias.

### `blog`

Responsável pelas publicações e conteúdos informativos da loja.

**Principais funcionalidades:**

* Cadastro de publicações;
* Listagem de publicações;
* Visualização dos detalhes;
* Edição de publicações;
* Exclusão de publicações;
* Divulgação de dicas e informações sobre suplementos.

### `institucional`

Responsável pelas páginas institucionais do sistema.

**Principais funcionalidades:**

* Página inicial;
* Apresentação da empresa;
* Informações sobre a loja;
* Página de contato;
* Formulário de contato.

## Models e Views

### App `contas`

**Models:**

* Utilização do model `User` padrão do Django para gerenciamento dos usuários.

**Views:**

* `CadastroView` — responsável pelo cadastro dos usuários;
* `GoldBoxLoginView` — responsável pelo login;
* `GoldBoxLogoutView` — responsável pelo logout.

**Responsável:** João Vitor Vaz.

### App `produtos`

**Models:**

* `Categoria` — representa as categorias dos produtos;
* `Produto` — representa os produtos disponíveis na loja.

**Views:**

* `produto_list` — lista os produtos;
* `produto_detail` — apresenta os detalhes de um produto;
* `produto_create` — realiza o cadastro de produtos;
* `produto_update` — realiza a edição de produtos;
* `produto_delete` — realiza a exclusão de produtos.

**Responsável:** Davi Honorato.

### App `blog`

**Models:**

* `Publicacao` — representa uma publicação realizada no blog.

**Views:**

* `post_list` — lista as publicações;
* `post_detail` — apresenta os detalhes de uma publicação;
* `post_create` — realiza o cadastro de publicações;
* `post_update` — realiza a edição de publicações;
* `post_delete` — realiza a exclusão de publicações.

**Responsável:** Lucas Da Silva.

### App `institucional`

**Models:**

* `Contato` — responsável pelo armazenamento das mensagens enviadas pelo formulário de contato.

**Views:**

* `landing` — responsável pela página inicial;
* `contato` — responsável pela página de contato.

**Responsável:** Rayssa Borchatd.

## Arquivos e Responsabilidades

### João Vitor Vaz — App `contas`

**Arquivos principais:**

```text
contas/
├── models.py
├── views.py
├── forms.py
├── urls.py
└── templates/
    └── contas/
        ├── cadastro.html
        └── login.html
```

**Responsabilidades:**

* Desenvolver o cadastro de usuários;
* Desenvolver o sistema de login;
* Desenvolver o logout;
* Configurar a autenticação;
* Criar e modificar os arquivos relacionados ao app `contas`.

### Davi Honorato — App `produtos`

**Arquivos principais:**

```text
produtos/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
└── templates/
    └── produtos/
        ├── produto_list.html
        ├── produto_detail.html
        ├── produto_form.html
        └── produto_confirm_delete.html
```

**Responsabilidades:**

* Desenvolver os Models `Categoria` e `Produto`;
* Criar o catálogo;
* Criar o cadastro de produtos;
* Criar edição e exclusão de produtos;
* Desenvolver a organização por categorias;
* Configurar o gerenciamento dos produtos no Django Admin.

### Lucas Da Silva — App `blog`

**Arquivos principais:**

```text
blog/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
└── templates/
    └── blog/
        ├── post_list.html
        ├── post_detail.html
        ├── post_form.html
        └── post_confirm_delete.html
```

**Responsabilidades:**

* Desenvolver o blog;
* Criar o Model `Publicacao`;
* Criar o cadastro de publicações;
* Criar edição e exclusão de publicações;
* Desenvolver a listagem das publicações;
* Desenvolver a visualização dos detalhes;
* Criar conteúdos com dicas e informações sobre suplementos;
* Configurar o gerenciamento das publicações no Django Admin.

### Rayssa Borchatd — App `institucional`

**Arquivos principais:**

```text
institucional/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── templates/
│   └── institucional/
│       ├── index.html
│       └── contato.html
└── static/
    └── institucional/
        ├── css/
        │   └── style.css
        └── js/
            └── script.js
```

**Responsabilidades:**

* Desenvolver a página inicial;
* Desenvolver a página de contato;
* Criar o formulário de contato;
* Desenvolver o layout das páginas institucionais;
* Implementar a estilização com CSS;
* Implementar interações necessárias com JavaScript.

## Estrutura Geral Planejada

```text
Gold_Box/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── contas/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── produtos/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│
├── institucional/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Status do Projeto

**Em desenvolvimento.**

A estrutura inicial do projeto está sendo desenvolvida em Django, com divisão das funcionalidades entre os integrantes da equipe e organização por aplicativos.
