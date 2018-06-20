import boto3
from contextlib import closing
import os

client = boto3.client('polly')

response = client.synthesize_speech(

    OutputFormat='mp3',
    Text='Speech synthesis is the artificial production of human speech. A computer system used for this purpose is called a speech computer or speech synthesizer, and can be implemented in software or hardware products.',
    TextType='text',
    VoiceId='Joanna'
)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = "pollyboto.mp3"

        try:
            # Open a file for writing the output as a binary stream
            with open(output, "wb") as file:
                file.write(stream.read())

        except IOError as error:
            # Could not write to file, exit gracefully
            print(error)
            sys.exit(-1)
        os.system("start pollyboto.mp3")
