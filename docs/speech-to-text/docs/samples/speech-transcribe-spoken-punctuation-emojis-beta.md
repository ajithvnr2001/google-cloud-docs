---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-spoken-punctuation-emojis-beta/
title: Speech-to-Text with spoken punctuation and emojis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:28.232180+00:00
---

# Speech-to-Text with spoken punctuation and emojis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-spoken-punctuation-emojis-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Speech-to-Text with spoken punctuation and emojis Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to use the Speech-to-Text API to transcribe audio with spoken punctuation and emojis.

## Code sample

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    from google.protobuf import wrappers_pb2
    
    client = speech.SpeechClient()
    
    speech_file = "resources/commercial_mono.wav"
    
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="en-US",
        # Enable spoken punctuation
        enable_spoken_punctuation=wrappers_pb2.BoolValue(value=True),
        # Enable spoken emojis
        enable_spoken_emojis=wrappers_pb2.BoolValue(value=True),
    )
    
    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
    
    return response.results

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
