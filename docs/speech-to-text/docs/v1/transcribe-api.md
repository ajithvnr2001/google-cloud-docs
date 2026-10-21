---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-api/
title: Quickstart: Transcribe speech to text by using the API \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:19.670109+00:00
---

# Quickstart: Transcribe speech to text by using the API  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Transcribe speech to text by using the API

This page shows you how to send a speech recognition request to Cloud Speech-to-Text using the [REST interface](https://docs.cloud.google.com/speech-to-text/docs/reference/rest) and the `curl` command.

Cloud Speech-to-Text enables easy integration of Google speech recognition technologies into developer applications. You can send audio data to the Cloud Speech-to-Text API, which then returns a text transcription of that audio file. For more information about the service, see [Cloud STT basics](https://docs.cloud.google.com/speech-to-text/docs/basics). 

## Before you begin

Before you can send a request to the Cloud Speech-to-Text API, you must have completed the following actions. See the [before you begin](https://docs.cloud.google.com/speech-to-text/docs/v1/before-you-begin) page for details.

  * Enable Cloud Speech-to-Text on a Google Cloud project. 
    * Make sure billing is enabled for Cloud Speech-to-Text.
  * Verify that you have the permissions required to complete this guide. If you created a new project for this guide, then you already have the required permissions.
  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * (Optional) Create a new Google Cloud Storage bucket to store your audio data.



### Required roles

To get the permissions that you need to transcribe speech to text, ask your administrator to grant you the [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Make an audio transcription request

Now you can use Cloud STT to transcribe an audio file to text. Use the following code sample to send a [`recognize`](https://docs.cloud.google.com/speech-to-text/docs/rest/v1/speech/recognize) REST request to the Cloud Speech-to-Text API.

  1. Create a JSON request file with the following text, and save it as a `sync-request.json` plain text file:
         
         {
           "config": {
               "encoding":"FLAC",
               "sampleRateHertz": 16000,
               "languageCode": "en-US",
               "enableWordTimeOffsets": false
           },
           "audio": {
               "uri":"gs://cloud-samples-tests/speech/brooklyn.flac"
           }
         }
           

This JSON snippet indicates that the audio file has a FLAC encoding format, a sample rate of 16000 Hz, and that the audio file is stored on Google Cloud Storage at the given URI. The audio file is publicly accessible, so you don't need authentication credentials to access the file.

  2. Use `curl` to make a `speech:recognize` request, passing it the filename of the JSON request you set up in step 1:

The sample `curl` command uses the `gcloud auth print-access-token` command to get an authentication token.
         
         curl -s -H "Content-Type: application/json" \
             -H "Authorization: Bearer "$(gcloud auth print-access-token) \
             https://speech.googleapis.com/v1/speech:recognize \
             -d @sync-request.json
           

Note that to pass a filename to `curl` you use the `-d` option (for "data") and precede the filename with an `@` sign. This file should be in the same directory in which you execute the `curl` command.

You should see a response similar to the following:
         
         {
           "results": [
             {
               "alternatives": [
                 {
                   "transcript": "how old is the Brooklyn Bridge",
                   "confidence": 0.98267895
                 }
               ]
             }
           ]
         }
           




Congratulations! You've sent your first request to Cloud STT.

If you receive an error or an empty response from Cloud STT, take a look at the [troubleshooting](https://docs.cloud.google.com/speech-to-text/docs/troubleshooting) and [error mitigation](https://docs.cloud.google.com/speech-to-text/docs/error-messages) steps. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  * Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you do not need it.



## What's next

  * Practice [transcribing short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * Learn how to [batch long audio files for speech recognition](https://docs.cloud.google.com/speech-to-text/docs/async-recognize). 
  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize) like from a microphone. 
  * Get started with the Cloud STT in your language of choice by using a [Cloud STT client library](https://docs.cloud.google.com/speech-to-text/docs/reference/libraries). 
  * Work through the [sample applications](https://docs.cloud.google.com/speech-to-text/docs/samples). 
  * For best performance, accuracy, and other tips, see the [best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices) documentation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
