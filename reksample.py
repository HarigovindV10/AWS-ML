import boto3

client = boto3.client('rekognition','eu-west-1')
with open('source3.jpg', 'rb') as source_image:
    source_bytes = source_image.read()
response = client.detect_text(
    Image={
        'Bytes': source_bytes
    }
)
s=""


for i in response['TextDetections']:
    if i["Type"]=='LINE':
        s+=" "+i['DetectedText']
print(s)
