---
url: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/use-model/
title: Use models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:01.505311+00:00
---

# Use models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/use-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Use models Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use a trained Custom Speech-to-Text model in your production application or benchmarking workflows. As soon as you deploy your model through a dedicated endpoint, you automatically get programmatic access through a recognizer object, which can be used directly through the Cloud Speech-to-Text V2 API or in the Google Cloud console.

## Before you begin

Ensure you have signed up for a Google Cloud account, created a project, trained a custom speech model, and deployed it using an endpoint.

## Perform inference in V2

For a Custom Speech-to-Text model to be ready for use, the state of the model in the **Models** tab should be **Active** , and the dedicated endpoint in the **Endpoints** tab must be **Deployed**.

In our example, where a Google Cloud project ID is `custom-models-walkthrough`, the endpoint that corresponds to the Custom Speech-to-Text model `quantum-computing-lectures-custom-model` is `quantum-computing-lectures-custom-model-prod-endpoint`. The region that it's available is `us-east1`, and the batch transcription request is the following:
    
    
    from google.api_core import client_options
    from google.cloud.speech_v2 import SpeechClient
    from google.cloud.speech_v2.types import cloud_speech
    
    def quickstart_v2(
        project_id: str,
        audio_file: str,
    ) -> cloud_speech.RecognizeResponse:
        """Transcribe an audio file."""
        # Instantiates a client
        client = SpeechClient(
        client_options=client_options.ClientOptions(
          api_endpoint="us-east1-speech.googleapis.com"
        )
      )
    
        # Reads a file as bytes
        with open(audio_file, "rb") as f:
            content = f.read()
    
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.[AutoDetectDecodingConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.AutoDetectDecodingConfig.html)(),
            language_codes=["en-US"],
            model="projects/custom-models-walkthrough/locations/us-east1/endpoints/quantum-computing-lectures-custom-model-prod-endpoint",
        )
        request = cloud_speech.RecognizeRequest(
            recognizer=f"projects/custom-models-walkthrough/locations/us-east1/recognizers/_",
            config=config,
            content=content,
        )
    
        # Transcribes the audio into text
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(request=request)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")
    
        return response
    
    

**Note:** If you try to create a recognizer object in a different region than the one that the endpoint is created in, the request will fail.

## What's next

Follow the resources to take advantage of custom speech models in your application. See [Evaluate your custom models](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/evaluate-model).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
