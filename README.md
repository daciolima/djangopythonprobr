# Python - Django
Django com Deploy no Heroku

Estudo e desenvolvimento Web buscando está conforme orientações dos Doze Fatores:
https://12factor.net/pt_br/

[![Build Status](https://travis-ci.org/daciolima/djangopythonprobr.svg?branch=master)](https://travis-ci.org/daciolima/djangopythonprobr)
[![codecov](https://codecov.io/gh/daciolima/djangopythonprobr/branch/master/graph/badge.svg)](https://codecov.io/gh/daciolima/djangopythonprobr)
[![Updates](https://pyup.io/repos/github/daciolima/djangopythonprobr/shield.svg)](https://pyup.io/repos/github/daciolima/djangopythonprobr/)
[![Python 3](https://pyup.io/repos/github/daciolima/djangopythonprobr/python-3-shield.svg)](https://pyup.io/repos/github/daciolima/djangopythonprobr/)


#### Instalando as libs em ambiente de desenvolvimento

#### Flake8
Instalar a lib flake8 com o comando abaixo:
```console
pipenv install --dev flake8
```

Configuração: Criar o arquivo .flake8 na raiz do projeto e colocar as seguintes configurações:
```console
[flake8]
max-line-length = 120
exclude = .venv
```


##########################################


#### PyUp (Monitor de update de libs)
> - Setar o repositório do projeto que está no github configurando no site pyup.io;
> - Criar arquivo .pyup.yml e realizar configuração:

````console
requirements:
  - Pipfile
  - Pipfile.lock
````

##########################################


#### Travis-CI (Integração Contínua)
> - Setar o repositório  do projeto que está no github configurando no site travis-ci.org;
> - Criar arquivo .travis.yml e realizar configuração:
```console
language: python
python:
  - 3.8
env:
  global:
    - PIPENV_VENV_IN_PROJECT=1
    - PIPENV_IGNORE_VIRTUALENVS=1
install:
  - pip install pipenv
  - pipenv sync --dev
script:
  - pipenv run flake8
```


##########################################


#### Pytest-Django
Instalar a lib pytest-django
```console
pipenv install -d pytest-django
````
Criar o arquivo pytest.ini na raiz e setar a seguinte configuração:
```console
[pytest]
DJANGO_SETTINGS_MODULE = admin.settings
````

1 - Setar no Pycharm em preferences/Tools/Python Integrated Tools/Testing
para testes com o pytest
2 - Criar um diretorio tests dentro de cada app a ser testada e dentro o 
mesmo os módulos de testes.

##########################################

#### Pytest-Cov (Cobertura de tests e relatório)
Com a cobertura de teste podemos dizer qual área do 
projeto a ser testado e obter o relatório deste.
Instalar em ambiente de desenvolvimento as libs:
- pytest-cov -> Cobertura de teste.
- codecov -> Gerador de relatório de cobertura (https://codecov.io/)
```console
pipenv install --dev 'pytest-cov' codecov
```
Rodar cobertura via terminal:
```console
pipenv run pytest --cov=apps
```
##########################################

#### Arquivo para Heroku 
Criar na raiz o arquivo Procfile e colocar a seguinte configuração
```console
web: gunicorn admin.wsgi --log-file -
```

##########################################


#### Comandos Django
Criar projeto django na raiz
```console
django-admin startproject <nome_projeto> .
````

Ver os comandos disponíveis pelo arquivo manager.py
```console
python manager.py --help
````

Subir o server em ambiente de desevolvimento
```console
python manager.py runserver
````

Coletar staticfiles
```console
python manager.py collectstatic
````

Gerar um alias para o arquivo manager.py através da variável local
criada pelo .venv
```console
alias mng='python $VIRTUAL_ENV/../manage.py'
````

Gerar nova SECRET_KEY, caso necessário.
Dentro do ambiente ./venv ativado entre no shell do python.
```console
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
````

##########################################

#### Comandos Heroku
Instalando em máquinas MacOS
```console
brew tap heroku/brew && brew install heroku
````

Logando via terminal no Heroku
```console
heroku login
````

Criando uma aplicação no Heroku via terminal
```console
heroku apps:create <Nome_aplicação>
````

Enviando entrega via git para o Heroku
```console
git push heroku branch_local:master -f
````

Configurando variável de ambiente DEGUG do arquivo settings do Django 
dentro do Heroku
```console
heroku config:set DEGUB=False
````

Desabilitando coleta de arquivos estáticos no Heroku
```console
heroku config:set DISABLE_COLLECTSTATIC=1
````

Setando uma SECRET_KEY do arquivo settings.py no ambiente Heroku
```console
heroku config:set SECRET_KEY='Chave Secreta'
````

Configurando domains no Heroku. Obs: Conta Heroku deve está verificada
```console
heroku domains:add DOMINIO
````

Listando as variável de ambiente no Heroku
```console
heroku config
````

Removendo um variável de ambiente no Heroku
```console
heroku config:unset DISABLE_COLLECTSTATIC
````

Visualizando logs da aplicação no Heroku
````console
heroku logs --tail 
````

Agendar backup postgresql no Heroku
````console
heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Recife'
````

Interromper agenda de backup
````console
heroku pg:backups:unschedule DATABASE_URL --app Nome_APP
````

Visualizar agenda de backup
````console
heroku pg:backups:schedules --app Nome_APP
````

Criando URL pública para download de backup
````console
heroku pg:backups:url b001 --app Nome_APP
````

Visualizando a URL pública do download de backup
````console
heroku pg:backups:url --app Nome_APP | cat
````

Realizar download de backup
````console
heroku pg:backups:download
````

Checando download de backup realizados
````console
heroku pg:backups --app Nome_APP
````

Ver detalhes de um backup específico baixado
````console
heroku pg:backups:info <ID_BACKUP> --app Nome_APP
````

Deletando backup específico
````console
heroku pg:backups:delete <ID_BACKUP> --app Nome_APP
````

Restaurando backup específico
````console
heroku pg:backups:restore b101 DATABASE_URL --app sushi
````

Restaurando backup de uma APP para outra APP
````console
heroku pg:backups:restore sushi::b101 DATABASE_URL --app sushi-staging
````


##########################################

#### Comandos Docker
Docker: Sobe imagem do docker descrita no arquivo docker-compose.yml
Obs: Após a criação do container é criado dentro do projeto um diretório .pgdata 
```console
docker-compose up
````



##########################################

