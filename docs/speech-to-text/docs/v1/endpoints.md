---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/endpoints/
title: Supported regional endpoints \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:31.505098+00:00
---

# Supported regional endpoints  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/endpoints/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Supported regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Speech-to-Text offers US and EU regional API endpoints. If you use a regional endpoint, your data at-rest and in-use will stay within the continental boundaries of Europe or the USA. Specifying an endpoint is important if your data's location must be controlled in order to comply with local regulatory requirements. There is no functional change to the behavior of the API.

## Use regional endpoints

When you use a regional endpoint, make sure to include the matching `us` or `eu` location in the `parent` string. See the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig) documentation for more information about configuring the recognition request body.

### Protocol

To perform speech recognition using a regional endpoint, run the applicable command in the table below to configure the correct endpoint:

Multi-region | Endpoint override  
---|---  
EU | `$ export CLOUD_SPEECH_ENDPOINT=https://eu-speech.googleapis.com`  
US | `$ export CLOUD_SPEECH_ENDPOINT=https://us-speech.googleapis.com`  
  
The following code sample demonstrates how to send a [`recognize request`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/speech/recognize) that keeps all data confined to a specified region. You can substitute either the `EU` or `US` regional endpoint for the CLOUD_SPEECH_ENDPOINT variable.
    
    
    $ curl   -H "Content-Type: application/json"  \
             -H  "Authorization: Bearer "$(gcloud auth print-access-token)   \
              $CLOUD_SPEECH_ENDPOINT/v1/speech:recognize \
             --data "{
            'config': {
                'encoding': 'LINEAR16',
                'languageCode': 'en-US'
            },
            'audio': {
                'uri':'gs://speech-samples-00/commercial_mono.wav'
            }
        }"

This example uses [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) to generate credentials for your user account. To learn how to install and initialize the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-api).

The audio content supplied in the request body is base64-encoded. For more information on how to base64-encode audio, see [Base64 Encoding Audio Content](https://docs.cloud.google.com/speech-to-text/docs/v1/base64-encoding). For more information on the `content` field, see [RecognitionAudio](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionAudio).

### gcloud

The following commands set a regional endpoint:

Multi-region | Endpoint override  
---|---  
EU | `gcloud config set api_endpoint_overrides/speech https://eu-speech.googleapis.com/`  
US | `gcloud config set api_endpoint_overrides/speech https://us-speech.googleapis.com/`  
  
After you set the regional endpoint, all data will be confined to the specified region when you send subsequent [`recognize requests`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/speech/recognize). The following example demonstrates a recognize request.
    
    
    $ gcloud ml speech recognize gs://cloud-samples-tests/speech/brooklyn.flac \
        --language-code=en-US --log-http

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    from google.api_core import client_options
    from google.cloud import speech
    
    
    def sync_recognize_with_multi_region_gcs() -> speech.RecognizeResponse:
        """Recognizes speech synchronously in the GCS bucket."""
    
        # Instantiates a client
    
        # Pass an additional argument, ClientOptions, to specify the new endpoint.
        _client_options = client_options.ClientOptions(
            api_endpoint="eu-speech.googleapis.com"
        )
    
        client = speech.SpeechClient(client_options=_client_options)
    
        # The name of the audio file to transcribe
        gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    
        audio = speech.RecognitionAudio(uri=gcs_uri)
    
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
    
        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response.results

## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
