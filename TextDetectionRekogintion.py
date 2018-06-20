import boto3

client = boto3.client('rekognition','eu-west-1')
with open('source3.jpg', 'rb') as source_image:
    source_bytes = source_image.read()
response = client.detect_text(
    Image={
        'Bytes': source_bytes
    }
)
result=""


for words in response['TextDetections']:
    if words["Type"]=='WORD':
        result+=" "+words['DetectedText']
print(result)
