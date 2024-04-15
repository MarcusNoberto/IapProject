# Guia de Utilização da Ferramenta

Este guia explica como configurar e utilizar a ferramenta.

## 1. Criar e Ativar Ambiente Virtual

sh
 - python3 -m venv env
 - source env/bin/activate

## 2. Instalar Django
sh
 - pip install django

3. Instalar Django REST Framework
sh

 - pip install djangorestframework

4. Instalar Django Filter
sh

 - pip install django-filter

5. Realizar as Migrações do Banco de Dados
sh

 - python manage.py makemigrations
 - python manage.py migrate

6. Acessar a Rota para Processar IAPs
Para processar os IAPs, acesse a seguinte rota no navegador ou em um cliente HTTP:

bash

 - http://localhost:8000/processar_iaps/

7. Acessar a API
Após processar os IAPs, a API estará disponível em:


 - http://localhost:8000/

Lembre-se de substituir python por python3 e pip por pip3 se necessário, dependendo da sua configuração.
