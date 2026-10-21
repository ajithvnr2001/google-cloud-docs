---
url: https://docs.cloud.google.com/speech-to-text/docs/transcription-model/
title: Compare transcription models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:01.897249+00:00
---

# Compare transcription models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/transcription-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Compare transcription models Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use a specific machine learning model for audio transcription requests to Cloud Speech-to-Text.

## Select the right transcription model

Cloud Speech-to-Text detects words in an audio clip by comparing input to one of many machine learning _models_. Each model has been trained by analyzing millions of examples—in this case, many, many audio recordings of people speaking.

Cloud STT has specialized models which are trained from audio for specific sources. These models provide better results when applied toward similar kinds of audio data to the data they were trained on.

The following table shows the transcription models that are available for use with the Cloud Speech-to-Text API V2.

Model name | Description  
---|---  
`chirp_3` | Use the latest generation of Google's multilingual Automatic Speech Recognition (ASR)-specific generative models that are designed to meet your user's needs based on feedback and experience. Chirp 3 provides enhanced accuracy and speed beyond earlier Chirp models and provides diarization and automatic language detection.  
`chirp_2` | Use the Universal large Speech Model (USM) that's powered by our large language model (LLM) technology for streaming and batch, and provides transcriptions and translations in diverse linguistic content and multilingual capabilities.  
`telephony` | Use this model for audio that originates from an audio phone call, typically recorded at an 8 kHz sampling rate. Ideal for customer service, teleconferencing, and automated kiosk applications.  
  
## Select a model for audio transcription

To transcribe short audio clips (under 60 seconds), [synchronous recognition](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize) is the simplest method. It processes your audio and returns the full transcription result in a single response after all audio has been processed.

### Python
    
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    # TODO(developer): Update and un-comment below line
    # PROJECT_ID = "your-project-id"
    
    # Instantiates a client
    client = SpeechClient()
    
    # Reads a file as bytes
    with open("resources/audio.wav", "rb") as f:
        audio_content = f.read()
    
    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
        language_codes=["en-US"],
        model="chirp_3",
    )
    
    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
        config=config,
        content=audio_content,
    )
    
    # Transcribes the audio into text
    response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(request=request)
    
    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
    

To transcribe audio files longer than 60 seconds or for transcribing audio in real-time, you can use one of the following methods:

  * **Batch recognition** : Ideal for transcribing long audio files (minutes to hours) stored in a Cloud Storage bucket. This is an asynchronous operation. To learn more about batch recognition, see [Batch Recognition](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize).


  1. **Streaming recognition** : Perfect for capturing and transcribing audio in real time, such as from a microphone feed or a live stream. To learn more about streaming recognition, see [Streaming Recognition](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize).



## What's next

  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). 
  * Learn how to [transcribe long audio files](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize). 
  * Learn how to [transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * For best performance, accuracy, and other tips, see the [best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices) documentation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
