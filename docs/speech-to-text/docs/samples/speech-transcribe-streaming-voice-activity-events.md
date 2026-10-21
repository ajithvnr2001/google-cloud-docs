---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming-voice-activity-events/
title: Transcribe audio with voice activity events \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:33.400166+00:00
---

# Transcribe audio with voice activity events  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming-voice-activity-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe audio with voice activity events Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to transcribe audio from a file into text, and detect speech activity events such as when someone starts or stops speaking.

## Code sample

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def transcribe_streaming_voice_activity_events(
        audio_file: str,
    ) -> cloud_speech.StreamingRecognizeResponse:
        """Transcribes audio from a file into text and detects voice activity
            events using Google Cloud Speech-to-Text API.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
                Example: "resources/audio.wav"
        Returns:
            list[cloud_speech.StreamingRecognizeResponse]: A list of `StreamingRecognizeResponse` objects.
        """
        # Instantiates a client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as file:
            audio_content = file.read()
    
        # In practice, stream should be a generator yielding chunks of audio data
        chunk_length = len(audio_content) // 5
        stream = [
            audio_content[start : start + chunk_length]
            for start in range(0, len(audio_content), chunk_length)
        ]
        audio_requests = (
            cloud_speech.StreamingRecognizeRequest(audio=audio) for audio in stream
        )
    
        recognition_config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=["en-US"],
            model="long",
        )
    
        # Sets the flag to enable voice activity events
        streaming_features = cloud_speech.StreamingRecognitionFeatures(
            enable_voice_activity_events=True
        )
        streaming_config = cloud_speech.StreamingRecognitionConfig(
            config=recognition_config, streaming_features=streaming_features
        )
    
        config_request = cloud_speech.StreamingRecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
            streaming_config=streaming_config,
        )
    
        def requests(config: cloud_speech.RecognitionConfig, audio: list) -> list:
            yield config
            yield from audio
    
        # Transcribes the audio into text
        responses_iterator = client.streaming_recognize(
            requests=requests(config_request, audio_requests)
        )
        responses = []
        for response in responses_iterator:
            responses.append(response)
            if (
                response.speech_event_type
                == cloud_speech.StreamingRecognizeResponse.SpeechEventType.SPEECH_ACTIVITY_BEGIN
            ):
                print("Speech started.")
            if (
                response.speech_event_type
                == cloud_speech.StreamingRecognizeResponse.SpeechEventType.SPEECH_ACTIVITY_END
            ):
                print("Speech ended.")
            for result in response.results:
                print(f"Transcript: {result.alternatives[0].transcript}")
    
        return responses
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
