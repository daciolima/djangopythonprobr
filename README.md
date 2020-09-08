# djangopythonprobr
Módulo Django do Curso PythonPro

[![Build Status](https://travis-ci.org/daciolima/djangopythonprobr.svg?branch=master)](https://travis-ci.org/daciolima/djangopythonprobr)



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


