import boto3
from contextlib import closing
import os

client = boto3.client('polly')

response = client.synthesize_speech(

    OutputFormat='mp3',
    Text='Bright and fine quality paper',
    TextType='text',
    VoiceId='Joanna'
)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = "polly-boto.mp3"

        try:
            # Open a file for writing the output as a binary stream
            with open(output, "wb") as file:
                file.write(stream.read())

        except IOError as error:
            # Could not write to file, exit gracefully
            print(error)
            sys.exit(-1)
        os.system("start polly-boto.mp3")
