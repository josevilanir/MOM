# Execução do Sistema com RabbitMQ e Flask API

## Passo 1: Instalação do RabbitMQ

Certifique-se de ter o RabbitMQ instalado e em execução na sua máquina ou em um servidor acessível.

- [Download e instalação do RabbitMQ](https://www.rabbitmq.com/download.html)

## Passo 2: Iniciar o RabbitMQ Server

  inicie o servidor RabbitMQ pela barra de execução do windows.

## passo 3: Clonar o Repositório
git clone https://github.com/josevilanir/MOM.git
cd MOM

## passo 4: Instalar Dependencias Python:
pip install flask pika

## passo 5: Executar o Produtor com a API
python produtor_api.py

## passo 6: Executar o Consumidor
python consumidor.py

## Passo 7: Enviar Mensagem via API
Invoke-RestMethod -Uri "http://localhost:5000/enviar-mensagem" -Method Post -Body '{"mensagem": "Exemplo de mensagem"}' -Headers @{"Content-Type"="application/json"}
