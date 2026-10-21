---
url: https://docs.cloud.google.com/speech-to-text/priv/docs/transcribe/
title: Send a transcription request to Cloud Speech-to-Text On-Prem \u00a0|\u00a0 Cloud Speech-to-Text private documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:17.845302+00:00
---

# Send a transcription request to Cloud Speech-to-Text On-Prem  |  Cloud Speech-to-Text private documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/priv/docs/transcribe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text)
  * [ Cloud Speech-to-Text On-Prem ](https://docs.cloud.google.com/speech-to-text/priv)
  * [ Documentation ](https://docs.cloud.google.com/speech-to-text/priv/docs)



Send feedback 

#  Send a transcription request to Cloud Speech-to-Text On-Prem Stay organized with collections  Save and categorize content based on your preferences. 

**Private feature**  
This product is a private feature. The documentation is publicly available but you must [contact Google](https://cloud.google.com/contact) for full access. 

## Prerequisites

  1. Complete all required steps in the [before you begin](https://docs.cloud.google.com/speech-to-text/priv/docs/before-you-begin) quickstart.
  2. [Deploy the API](https://docs.cloud.google.com/speech-to-text/priv/docs/deploy).
  3. [Query the API](https://docs.cloud.google.com/speech-to-text/priv/docs/query) to make sure it's working.



## Install dependencies

  1. Clone `python-speech` and change the directory to the sample directory.
         
         $ git clone https://github.com/googleapis/python-speech.git
         $ cd python-speech/samples/snippets
         

  2. Install [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) if you have not already done so. Refer to the Google Cloud Platform [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup) for more information.

  3. Create a `virtualenv`. The samples below are compatible with Python 2.7 and 3.4+.
         
         $ virtualenv env
         $ source env/bin/activate
         

  4. Install the dependencies needed to run the samples.
         
         $ pip install -r requirements.txt
         




## Code sample

The code sample below uses the [google-cloud-speech library](https://github.com/googleapis/python-speech). You can use GitHub to [browse the source](https://github.com/googleapis/python-speech) and [report issues](https://github.com/googleapis/python-speech/issues).

### Transcribe an audio file

You can use the code sample below to transcribe an audio file using either a public IP or cluster level IP. For more information on IP types, see the documentation on [querying the API](https://docs.cloud.google.com/speech-to-text/priv/docs/query).

**Public IP:**
    
    
        # Using a Public IP
        $ python transcribe_onprem.py --file_path="../resources/two_channel_16k.wav" --api_endpoint=${PUBLIC_IP}:443
    

**Cluster level IP:**
    
    
        # Using a cluster level IP
        $ kubectl port-forward -n $NAMESPACE $POD 10000:10000
        $ python transcribe_onprem.py --file_path="../resources/two_channel_16k.wav" --api_endpoint="0.0.0.0:10000"
    

### Python

To authenticate to Speech-to-Text, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def transcribe_onprem(
        local_file_path: str,
        api_endpoint: str,
    ) -> speech_v1p1beta1.RecognizeResponse:
        """
        Transcribe a short audio file using synchronous speech recognition on-prem
    
        Args:
          local_file_path: The path to local audio file, e.g. /path/audio.wav
          api_endpoint: Endpoint to call for speech recognition, e.g. 0.0.0.0:10000
    
        Returns:
          The speech recognition response
              {
        """
        # api_endpoint = '0.0.0.0:10000'
        # local_file_path = '../resources/two_channel_16k.raw'
    
        # Create a gRPC channel to your server
        channel = grpc.insecure_channel(target=api_endpoint)
        transport = speech_v1p1beta1.services.speech.transports.SpeechGrpcTransport(
            channel=channel
        )
    
        client = speech_v1p1beta1.SpeechClient(transport=transport)
    
        # The language of the supplied audio
        language_code = "en-US"
    
        # Sample rate in Hertz of the audio data sent
        sample_rate_hertz = 16000
    
        # Encoding of audio data sent. This sample sets this explicitly.
        # This field is optional for FLAC and WAV audio formats.
        encoding = speech_v1p1beta1.RecognitionConfig.AudioEncoding.LINEAR16
        config = {
            "encoding": encoding,
            "language_code": language_code,
            "sample_rate_hertz": sample_rate_hertz,
        }
        with io.open(local_file_path, "rb") as f:
            content = f.read()
        audio = {"content": content}
    
        response = client.recognize(request={"config": config, "audio": audio})
        for result in response.results:
            # First alternative is the most probable result
            alternative = result.alternatives[0]
            print(f"Transcript: {alternative.transcript}")
    
        return response
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
