# Trab2 Web2

Instruções para execução:

Como boa prática, recomenda-se a criação de um ambiente virtual (Utilizar o [venv](https://docs.python.org/pt-br/3/library/venv.html) , por exemplo):

```
python -m venv .
```

(Windows) Ativá-lo através do comando:

```
.\Scripts\Activate.ps1
```

Após clonar o projeto, acessar sua pasta raiz e fazer o download das dependências, com o seguinte comando:

```
pip install -r requirements.txt
```

Executar as migrations do BD:

```
python manage.py makemigrations
python manage.py migrate
```
Em seguida, criar um super usuário, com o seguinte comando (Rodar na pasta raiz do projeto, onde se encontra o manage.py):

```
python manage.py createsuperuser
```
Finalmente, executar o projeto:

```
python manage.py runserver
```
Para utilizar a área restrita do site (Cadastrar Aluno), cadastrar um usuário primeiro, acessando o admin:

http://127.0.0.1:8000/admin/

(Logar utilizando as credenciais do superuser criado anteriormente)

Em seguida, ao lado de "Usuários", clicar em "Adicionar"

![trab2](https://github.com/LucasPepper/trab2web2/assets/42626914/7bbdb9b9-77bf-4e17-96b6-76cb427aaf7c)

Crie um usuário e salve. Utilize essas credenciais para acessar a área restrita.

Para acessar o index:

http://127.0.0.1:8000/

ou

http://localhost:8000/
