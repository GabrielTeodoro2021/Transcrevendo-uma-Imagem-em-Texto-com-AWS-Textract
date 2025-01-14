import boto3
import json

def transcrever_imagem_s3(bucket_name, image_file):
    # Inicializa o cliente Textract
    textract = boto3.client('textract')

    # Chamada para detectar texto no arquivo de imagem armazenado no S3
    response = textract.detect_document_text(
        Document={'S3Object': {'Bucket': bucket_name, 'Name': image_file}}
    )

    # Exibe o resultado formatado em JSON
    print("Texto detectado:")
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            print(block['Text'])

    # Salvar a resposta em um arquivo JSON (opcional)
    with open("resultado_textract.json", "w") as file:
        json.dump(response, file, indent=4)

# Configurações da imagem no S3
bucket_name = 'nome-do-seu-bucket'
image_file = 'caminho/para/sua-imagem.jpg'

transcrever_imagem_s3(bucket_name, image_file)