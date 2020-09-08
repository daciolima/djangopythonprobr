# djangopythonprobr
Módulo Django do Curso PythonPro

[![Build Status](https://travis-ci.org/daciolima/djangopythonprobr.svg?branch=master)](https://travis-ci.org/daciolima/djangopythonprobr)
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
##### -------------------------------------------------

#### PyUp (Monitor de código testado)
> - Setar o repositório do projeto que está no github configurando no site pyup.io;
> - Criar arquivo .pyup.yml e realizar configuração:

````console
requirements:
  - Pipfile
  - Pipfile.lock
````

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

##### Arquivo para Heroku 
Criar na raiz o arquivo Procfile e colocar a seguinte configuração
```console
web: gunicorn admin.wsgi --log-file -
```

##### Comandos Django
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

Gerar um alias para o arquivo manager.py através da variável local
criada pelo .venv
```console
alias mng='python $VIRTUAL_ENV/../manage.py'
````

##### Comandos Heroku
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

Desabilitando coleta de arquivos estáticos no Heroku
```console
heroku config:set DISABLE_COLLECTSTATIC=1
````

Visualizando logs da aplicação no Heroku
````console
heroku logs --tail 
````

##### Outros comandos
Git: Visualizar os remote configurados
```console
git remote -v
````