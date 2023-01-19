<h1><img height="50em" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" /> API Artigos</h1>
<h2>CRUD feito com FastAPI, Autenticação JWT e PostgreSQL <img height="50em" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" /> <img height="50em" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg" /></h2>
<hr>
<h2>Usuários</h2>
  <h3>&#x1F7E0 POST - Criar Usuário</h3>
  <p>/api/v1/usuarios/signup</p>
  <h5>Campos</h5>
    <ul>nome - str</ul>
    <ul>sobrenome - str</ul>
    <ul>email - str</ul>
    <ul>senha - str</ul>
    <ul>eh-admin - bool</ul>
<hr>
  <h3>&#x1F7E0 POST - Login</h3>
  <p>/api/v1/usuarios/signup</p>
  <h5>Form-Data</h5>
    <ul>username - {email}</ul>
    <ul>password - {senha}</ul>
<hr>
  <h3>&#x1F7E2 GET - Usuários</h3>
  <p>/api/v1/usuarios</p>
<hr>
  <h3>&#x1F7E2 GET [ID] - Usuário</h3>
  <p>/api/v1/usuarios/{id}</p>
<hr>
 <h3>&#x1F7E2 GET [Logado] - Usuário</h3>
  <p>/api/v1/usuarios/logado</p>
  <h5>Token</h5>
    <ul>Token - {token gerado JWT}</ul>
<hr>
  <h3>&#x1F535 PUT [ID] - Usuário</h3>
  <p>/api/v1/usuarios/{id}</p>
  <h5>Campos</h5>
    <ul>nome - str</ul>
    <ul>sobrenome - str</ul>
    <ul>email - str</ul>
    <ul>senha - str</ul>
    <ul>eh-admin - bool</ul>
<hr>
<h3>&#x1F534 DEL [ID] - Usuário</h3>
  <p>/api/v1/usuarios/{id}</p>
<hr>
<br>
<h2>Artigo</h2>
<h3>&#x1F7E0 POST - Criar Artigo</h3>
<p>/api/v1/usuarios/signup</p>
  <h5>Token</h5>
  AUth - Token
  <h5>Campos</h5>
    <ul>titulo - str</ul>
    <ul>descricao - str</ul>
    <ul>url_fonte - str</ul>
<hr>
<h3>&#x1F7E2 GET - Artigos</h3>
  <p>/api/v1/artigos</p>
<hr>
<h3>&#x1F7E2 GET [ID] - Artigo</h3>
  <p>/api/v1/artigos/{id}</p>
<hr>
<h3>&#x1F7E0 PUT [ID]- Artigo</h3>
<p>/api/v1/artigos/{id}</p>
  <h5>Token</h5>
  AUth - Token
  <h5>Campos</h5>
    <ul>titulo - str</ul>
    <ul>descricao - str</ul>
    <ul>url_fonte - str</ul>
<hr>
<h3>&#x1F534 DEL [ID] - Artigo</h3>
  <p>/api/v1/artigos/{id}</p>

  
