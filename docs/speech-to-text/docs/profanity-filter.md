---
url: https://docs.cloud.google.com/speech-to-text/docs/profanity-filter/
title: Enable profanity filtering \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:26.204879+00:00
---

# Enable profanity filtering  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/profanity-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Enable profanity filtering Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud Speech-to-Text to automatically detect profanity in your audio data and censor them in the transcript.

You can enable the profanity filter by setting `profanityFilter=true` in the [`RecognitionFeatures`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v2/projects.locations.recognizers#recognitionfeatures). If enabled, Cloud Speech-to-Text will attempt to detect profane words and return only the first letter followed by asterisks in the transcript (for example, f***). If this field is set to `false` or not set, Cloud Speech-to-Text will not attempt to filter profanities.

The following sample demonstrates how to enable the profanity filter to recognize audio stored in a Cloud Storage bucket.

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    from google.cloud.speech import RecognizeResponse
    
    
    def sync_recognize_with_profanity_filter_gcs(audio_uri: str) -> RecognizeResponse:
        """Recognizes speech from an audio file in Cloud Storage and filters out profane language.
        Args:
            audio_uri (str): The Cloud Storage URI of the input audio, e.g., gs://[BUCKET]/[FILE]
        Returns:
            cloud_speech.RecognizeResponse: The full response object which includes the transcription results.
        """
        # Define the audio source
        audio = {"uri": audio_uri}
    
        client = speech.SpeechClient()
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,  # Audio format
            sample_rate_hertz=16000,
            language_code="en-US",
            # Enable profanity filter
            profanity_filter=True,
        )
    
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(config=config, audio=audio)
    
        for result in response.results:
            alternative = result.alternatives[0]
            print(f"Transcript: {alternative.transcript}")
    
        return response.results
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
