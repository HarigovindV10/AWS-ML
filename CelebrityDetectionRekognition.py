import boto3

client = boto3.client('rekognition','eu-west-1')
with open('source6.jpg', 'rb') as source_image:
    source_bytes = source_image.read()
with open('target.jpg', 'rb') as target_image:
    target_bytes = target_image.read()
response = client.recognize_celebrities(
    Image={
        'Bytes': source_bytes
    }
)
print(response['CelebrityFaces'][0]['Name'])
