#! python
import os
import boto3
import sys
from dotenv import load_dotenv

load_dotenv()


textract = boto3.client(
    'textract',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCES_KEY"),
    region_name=os.getenv("REGION_NAME")
)

#Load local document
with open(sys.argv[1], 'rb') as img:
    document_bytes = img.read()

response = textract.analyze_document(
    Document={'Bytes': document_bytes},
    FeatureTypes = ['FORMS', 'TABLES']
)

#Print text
print("Extracted text:")
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])

# print("\nKey-Value Paris:")
# for block in response['Blocks']:
#     if block['BlockType'] == 'KEY_VALUE_SET':
#         print(f"{block.get('Text', 'N/A')}")

# for block in response['Blocks']:
#     if block['BlockType'] == 'TABLE':
#         print(f"Table detected:e {block}")
