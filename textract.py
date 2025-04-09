import boto3

textract = boto3.client('textract')

with open('test1.jpg', 'rb') as img:
    document_bytes = img.read()