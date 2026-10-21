---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-onprem/
title: Transcribe a local file \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:26.484664+00:00
---

# Transcribe a local file  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-onprem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a local file Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe a short audio file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Send a transcription request to Cloud Speech-to-Text On-Prem](https://docs.cloud.google.com/speech-to-text/priv/docs/transcribe)



## Code sample

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
