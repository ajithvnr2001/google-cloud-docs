---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-with-speech-to-storage-beta/
title: Export Speech-to-Text transcript to Cloud Storage (Beta) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:41.442630+00:00
---

# Export Speech-to-Text transcript to Cloud Storage (Beta)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-with-speech-to-storage-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Export Speech-to-Text transcript to Cloud Storage (Beta) Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to export a speech-to-text transcript to a Cloud Storage bucket.

## Code sample

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.speech_v1 import types
    
    
    def export_transcript_to_storage_beta(
        audio_uri: str,
        output_bucket_name: str,
        output_filename: str,
    ) -> types.LongRunningRecognizeResponse:
        """Transcribes an audio file from Cloud Storage and exports the transcript to Cloud Storage bucket.
        Args:
            audio_uri (str): The Cloud Storage URI of the input audio, e.g., gs://[BUCKET]/[FILE]
            output_bucket_name (str): Name of the Cloud Storage bucket to store the output transcript.
            output_filename (str): Name of the output file to store the transcript.
        Returns:
            types.LongRunningRecognizeResponse: The response containing the transcription results.
        """
    
        audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(uri=audio_uri)
        output_storage_uri = f"gs://{output_bucket_name}/{output_filename}"
    
        # Pass in the URI of the Cloud Storage bucket to hold the transcription
        output_config = speech.[TranscriptOutputConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.TranscriptOutputConfig.html)(gcs_uri=output_storage_uri)
    
        # Speech configuration object
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=8000,
            language_code="en-US",
        )
    
        # Compose the long-running request
        request = speech.[LongRunningRecognizeRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.LongRunningRecognizeRequest.html)(
            audio=audio, config=config, output_config=output_config
        )
    
        # Create the speech client
        speech_client = speech.SpeechClient()
        # Create the storage client
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        # Run the recognizer to export transcript
        operation = speech_client.[long_running_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_long_running_recognize)(request=request)
        print("Waiting for operation to complete...")
        operation.result(timeout=90)
    
        # Get bucket with name
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(output_bucket_name)
        # Get blob (file) from bucket
        blob = bucket.[get_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_get_blob)(output_filename)
    
        # Get content as bytes
        results_bytes = blob.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)()
        # Get transcript exported in storage bucket
        storage_transcript = types.[LongRunningRecognizeResponse](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.LongRunningRecognizeResponse.html).from_json(
            results_bytes, ignore_unknown_fields=True
        )
    
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        for result in storage_transcript.results:
            # The first alternative is the most likely one for this portion.
            print(f"Transcript: {result.alternatives[0].transcript}")
            print(f"Confidence: {result.alternatives[0].confidence}")
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
