# Transcrevendo-uma-Imagem-em-Texto-com-AWS-Textract

## OCR Lista Escolar
Projeto usado para exemplificar o uso do AWS Textract na extração de textos em imagens simples.

## Pré requisitos:
 - Python
 - Uv
 - Conta AWS

## Configuração do ambiente:
É necessário configurar um usuário no IAM com acesso ao serviço Textract.

## Instalação:
Para instalar as dependências do projeto utilize o comando:
 - uv install

## Execução:
 - uv run main.py

## Funções e Ajustes:
 - boto3.client('textract'): Cria o cliente para interagir com o AWS Textract.
 - detect_document_text(): Detecta blocos de texto simples.
 - analyze_document(): Pode ser usado para detectar formulários e tabelas, se necessário.

## Dependências:
Instale o SDK Boto3:
 - pip install boto3

## Configure suas credenciais AWS:
 - aws configure
Insira a Access Key, Secret Key, região e formato desejado.
