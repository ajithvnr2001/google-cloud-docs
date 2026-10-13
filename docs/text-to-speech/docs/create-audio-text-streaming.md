---
url: https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-streaming/
title: Quickstart: Synthesize speech with bidirectional streaming quickstart \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:46.938026+00:00
---

# Quickstart: Synthesize speech with bidirectional streaming quickstart  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Guides ](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Synthesize speech with bidirectional streaming

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document walks you through the process of synthesizing audio using bidirectional streaming.

Bidirectional streaming lets you send text input and receive audio data simultaneously. This means that you can start synthesizing speech before the complete input text is sent, which reduces latency and enables real-time interactions. Voice assistants and interactive games use bidirectional streaming to create more dynamic and responsive applications.

To learn more about the fundamental concepts in Cloud Text-to-Speech, read [Cloud Text-to-Speech Basics](https://docs.cloud.google.com/text-to-speech/docs/basics).

## Before you begin

Before you can send a request to the Cloud Text-to-Speech API, you must have completed the following actions.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Text-to-Speech API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable texttospeech.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Text-to-Speech API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable texttospeech.googleapis.com




## Synthesize speech with bidirectional streaming

### Install the client library

### Python

Before installing the library, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-cloud-texttospeech

### Send a stream of text and receive a stream of audio

The API accepts a stream of requests with type `StreamingSynthesizeRequest`, which contain either `StreamingSynthesisInput` or `StreamingSynthesizeConfig`.

Before sending a stream `StreamingSynthesizeRequest` with `StreamingSynthesisInput`, which provides text input, send exactly one `StreamingSynthesizeRequest` with a `StreamingSynthesizeConfig`.

Streaming Cloud Text-to-Speech is only compatible with [Chirp 3: HD voices](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd).

### Python

Before running the example, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    #!/usr/bin/env python
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    
    """Google Cloud Text-To-Speech API streaming sample application .
    
    Example usage:
        python streaming_tts_quickstart.py
    """
    
    
    def run_streaming_tts_quickstart():
        """Synthesizes speech from a stream of input text."""
        from google.cloud import texttospeech
    
        client = texttospeech.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html)()
    
        # See https://cloud.google.com/text-to-speech/docs/voices for all voices.
        streaming_config = texttospeech.[StreamingSynthesizeConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeConfig.html)(
            voice=texttospeech.[VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams.html)(
                name="en-US-Chirp3-HD-Charon",
                language_code="en-US",
            )
        )
    
        # Set the config for your stream. The first request must contain your config, and then each subsequent request must contain text.
        config_request = texttospeech.[StreamingSynthesizeRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeRequest.html)(
            streaming_config=streaming_config
        )
    
        text_iterator = [
            "Hello there. ",
            "How are you ",
            "today? It's ",
            "such nice weather outside.",
        ]
    
        # Request generator. Consider using Gemini or another LLM with output streaming as a generator.
        def request_generator():
            yield config_request
            for text in text_iterator:
                yield texttospeech.[StreamingSynthesizeRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeRequest.html)(
                    input=texttospeech.[StreamingSynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesisInput.html)(text=text)
                )
    
        streaming_responses = client.[streaming_synthesize](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_streaming_synthesize)(request_generator())
    
        for response in streaming_responses:
            print(f"Audio content size in bytes is: {len(response.audio_content)}")
    
    
    if __name__ == "__main__":
        run_streaming_tts_quickstart()
    

## Clean up

To avoid unnecessary Google Cloud Platform charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you do not need it.

## What's next

  * Learn more about Cloud Text-to-Speech by reading the [basics](https://docs.cloud.google.com/text-to-speech/docs/basics). 
  * Review the list of [available voices](https://docs.cloud.google.com/text-to-speech/docs/voices) you can use for synthetic speech. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
