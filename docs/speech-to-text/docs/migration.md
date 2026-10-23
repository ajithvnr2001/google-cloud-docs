---
url: https://docs.cloud.google.com/speech-to-text/docs/migration/
title: Migrate to the latest version of Cloud Speech-to-Text API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:23.446613+00:00
---

# Migrate to the latest version of Cloud Speech-to-Text API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Migrate to the latest version of Cloud Speech-to-Text API Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Speech-to-Text API V2 brings the latest Google Cloud API design for customers to meet enterprise security and regulatory requirements out of the box.

These requirements are realized through the following:

  * [**Data residency**](https://docs.cloud.google.com/speech-to-text/docs/locations): Cloud STT V2 offers the broad range of our existing transcription models in [Google Cloud regions](https://cloud.google.com/about/locations) such as Belgium or Singapore. This allows the invocation of our transcription models through a fully regionalized service.

  * [**Recognizer resourcefulness**](https://docs.cloud.google.com/speech-to-text/docs/recognizers): Recognizers are reusable recognition configurations that can contain a combination of model, language, and features.

  * **Logging** : Resource creation and transcriptions generate logs available in the Google Cloud console, allowing for better telemetry and debugging.

  * [**Encryption**](https://docs.cloud.google.com/speech-to-text/docs/encryption): Cloud Speech-to-Text V2 supports [Customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) for all resources as well as batch transcription.

  * [**Audio auto-detect**](https://docs.cloud.google.com/speech-to-text/docs/encoding): Cloud Speech-to-Text V2 can automatically detect the sample rate, channel count, and format of your audio files, without needing to provide that information in the request configuration.




## Migrating from V1 to V2

Migration from the V1 API to the V2 API does not happen automatically. Minimal implementation changes are required to take advantage of the feature set.

### Migrating in the API

Similar to Cloud STT V1, to [transcribe audio](https://docs.cloud.google.com/speech-to-text/docs/transcribe-client-libraries), you need to create a [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#recognitionconfig) by selecting the language of your audio and the recognition model of your choice:

**Note:** The difference between the V1 and V2 versions of the Cloud Speech-to-Text API in the definition of `RecognitionConfig` message is the addition of the [`AutoDetectDecodingConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#autodetectdecodingconfig) message, which automatically detects the audio specifications.

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def quickstart_v2(audio_file: str) -> cloud_speech.RecognizeResponse:
        """Transcribe an audio file.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
        Returns:
            cloud_speech.RecognizeResponse: The response from the recognize request, containing
            the transcription results
        """
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        # Instantiates a client
        client = SpeechClient()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=["en-US"],
            model="long",
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
    
    

If needed, [select a region](https://docs.cloud.google.com/speech-to-text/docs/locations) in which you want to use the Cloud Speech-to-Text API, and check the [language and model availability](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) in that region:

### Python
    
    
    import os
    
    from google.api_core.client_options import ClientOptions
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def change_speech_v2_location(
        audio_file: str, location: str
    ) -> cloud_speech.RecognizeResponse:
        """Transcribe an audio file in a specific region. It allows for specifying the location
            to potentially reduce latency and meet data residency requirements.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
            location (str): The region where the Speech API will be accessed.
                E.g., "europe-west3"
        Returns:
            cloud_speech.RecognizeResponse: The full response object which includes the transcription results.
        """
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        # Instantiates a client to a regionalized Speech endpoint.
        client = SpeechClient(
            client_options=ClientOptions(
                api_endpoint=f"{location}-speech.googleapis.com",
            )
        )
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=["en-US"],
            model="long",
        )
    
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/{PROJECT_ID}/locations/{location}/recognizers/_",
            config=config,
            content=audio_content,
        )
    
        # Transcribes the audio into text
        response = client.recognize(request=request)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
        return response
    
    

Optionally, [create a recognizer resource](https://docs.cloud.google.com/speech-to-text/docs/recognizers) if you need to reuse a specific recognition configuration across many transcription requests:

### Python
    
    
    import os
    
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    def create_recognizer(recognizer_id: str) -> cloud_speech.Recognizer:
        """Сreates a recognizer with an unique ID and default recognition configuration.
        Args:
            recognizer_id (str): The unique identifier for the recognizer to be created.
        Returns:
            cloud_speech.Recognizer: The created recognizer object with configuration.
        """
        # Instantiates a client
        client = SpeechClient()
    
        request = cloud_speech.CreateRecognizerRequest(
            parent=f"projects/{PROJECT_ID}/locations/global",
            recognizer_id=recognizer_id,
            recognizer=cloud_speech.Recognizer(
                default_recognition_config=cloud_speech.RecognitionConfig(
                    language_codes=["en-US"], model="long"
                ),
            ),
        )
        # Sends the request to create a recognizer and waits for the operation to complete
        operation = client.create_recognizer(request=request)
        recognizer = operation.result()
    
        print("Created Recognizer:", recognizer.name)
        return recognizer
    
    

There are other differences in the requests and responses in the new V2 API. For more details, see the [reference documentation](https://docs.cloud.google.com/speech-to-text/docs/apis).

### Migrating in UI

To migrate through Speech Google Cloud console, follow these steps:

  1. Go to [Speech Google Cloud console](https://console.cloud.google.com/speech).

  2. Navigate to the **Transcriptions** Page.

  3. Click **New Transcription** and select your audio in the **Audio configuration** tab.

  4. In the **Transcription options** tab, select **V2**.




## What's next

* Use [client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) to transcribe audio using your favorite programming language. 
* Learn how to [transcribe short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
* Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize). 
* Learn how to [transcribe long audio files](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
