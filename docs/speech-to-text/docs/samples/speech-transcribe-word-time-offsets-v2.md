---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-word-time-offsets-v2/
title: Transcribe Word Time Offsets \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:21.559493+00:00
---

# Transcribe Word Time Offsets  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-word-time-offsets-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe Word Time Offsets Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to transcribe audio with word time offsets using the Speech-to-Text API.

## Code sample

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def transcribe_word_time_offsets_v2(
        audio_file: str,
    ) -> cloud_speech.RecognizeResponse:
        """Transcribes an audio file into text using with word time offsets.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
                Example: "resources/audio.wav"
        Returns:
            cloud_speech.RecognizeResponse: The response containing the transcription results
                with word time offsets.
        """
        # Instantiates a client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as file:
            audio_content = file.read()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=["en-US"],
            model="long",
            features=cloud_speech.RecognitionFeatures(
                enable_word_time_offsets=True,
            ),
        )
    
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            config=config,
            content=audio_content,
        )
    
        # Transcribes the audio into text
        response = client.recognize(request=request)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
