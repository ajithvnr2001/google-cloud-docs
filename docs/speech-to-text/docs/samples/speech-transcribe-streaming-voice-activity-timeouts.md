---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming-voice-activity-timeouts/
title: Transcribe audio with voice activity timeouts \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:03.599183+00:00
---

# Transcribe audio with voice activity timeouts  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming-voice-activity-timeouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe audio with voice activity timeouts Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to transcribe audio from a file with voice activity timeouts. It uses the Speech-to-Text API to transcribe the audio and prints the transcript to the console. The sample also prints out speech activity events, such as when speech starts and ends.

## Code sample

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    from time import sleep
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    from google.protobuf import duration_pb2  # type: ignore
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def transcribe_streaming_voice_activity_timeouts(
        speech_start_timeout: int,
        speech_end_timeout: int,
        audio_file: str,
    ) -> cloud_speech.StreamingRecognizeResponse:
        """Transcribes audio from audio file to text.
        Args:
            speech_start_timeout: The timeout in seconds for speech start.
            speech_end_timeout: The timeout in seconds for speech end.
            audio_file: Path to the local audio file to be transcribed.
                Example: "resources/audio_silence_padding.wav"
        Returns:
            The streaming response containing the transcript.
        """
        # Instantiates a client
        client = SpeechClient()
    
        # Reads a file as bytes
        with open(audio_file, "rb") as file:
            audio_content = file.read()
    
        # In practice, stream should be a generator yielding chunks of audio data
        chunk_length = len(audio_content) // 20
        stream = [
            audio_content[start : start + chunk_length]
            for start in range(0, len(audio_content), chunk_length)
        ]
        audio_requests = (
            cloud_speech.StreamingRecognizeRequest(audio=audio) for audio in stream
        )
    
        recognition_config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
            language_codes=["en-US"],
            model="long",
        )
    
        # Sets the flag to enable voice activity events and timeout
        speech_start_timeout = duration_pb2.Duration(seconds=speech_start_timeout)
        speech_end_timeout = duration_pb2.Duration(seconds=speech_end_timeout)
        voice_activity_timeout = (
            cloud_speech.[StreamingRecognitionFeatures](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.StreamingRecognitionFeatures.html).VoiceActivityTimeout(
                speech_start_timeout=speech_start_timeout,
                speech_end_timeout=speech_end_timeout,
            )
        )
        streaming_features = cloud_speech.[StreamingRecognitionFeatures](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.StreamingRecognitionFeatures.html)(
            enable_voice_activity_events=True, voice_activity_timeout=voice_activity_timeout
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
            for message in audio:
                sleep(0.5)
                yield message
    
        # Transcribes the audio into text
        responses_iterator = client.[streaming_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_streaming_recognize)(
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
