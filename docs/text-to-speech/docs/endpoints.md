---
url: https://docs.cloud.google.com/text-to-speech/docs/endpoints/
title: Specify a regional endpoint \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:54.498349+00:00
---

# Specify a regional endpoint  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Guides ](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



Send feedback 

#  Specify a regional endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Text-to-Speech offers `global`, `us`, `eu` multiregional and regional API endpoints. If you use a regional endpoint, your data at-rest and in-use stay within the regional or continental boundaries of Europe or the USA, respectively. If your data's location must be controlled in order to comply with local regulatory requirements, then specifying an endpoint is important. There is no functional change to the behavior of the API.

### Global

Model name | Global  
---|---  
Gemini 2.5 Flash TTS (`gemini-2.5-flash-tts`) |   
Gemini 2.5 Flash TTS (`gemini-2.5-pro-tts`) |   
Chirp 3: HD voices |   
Chirp 3: Instant Custom Voice |   
  
### United States

Model name | US multi-region  
---|---  
Gemini 2.5 Flash TTS (`gemini-2.5-flash-tts`) |   
Gemini 2.5 Flash TTS (`gemini-2.5-pro-tts`) |   
Chirp 3: HD voices |   
Chirp 3: Instant Custom Voice |   
  
### Europe

| EU multi-region | London, United Kingdom (europe-west2) | Frankfurt, Germany (europe-west3) |  Eemshaven, Netherlands (europe-west4)  
---|---|---|---|---  
Gemini 2.5 Flash TTS (`gemini-2.5-flash-tts`) |  |  |  |   
Gemini 2.5 Flash TTS (`gemini-2.5-pro-tts`) |  |  |  |   
Chirp 3: HD voices |  |  |  |   
Chirp 3: Instant Custom Voice |  |  |  |   
  
### Asia Pacific

| Tokyo, Japan (asia-northeast1) | Sydney, Australia (australia-southeast1) | Mumbai, India (asia-south1) | Singapore (asia-southeast1) | Seoul, Korea (asia-northeast3)  
---|---|---|---|---|---  
Gemini 2.5 Flash TTS (`gemini-2.5-flash-tts`) |  |  |  |  |   
Gemini 2.5 Flash TTS (`gemini-2.5-pro-tts`) |  |  |  |  |   
Chirp 3: HD voices |  |  |  |  |   
Chirp 3: Instant Custom Voice |  |  |  |  |   
  
## Use regional endpoints

When you use a regional endpoint, make sure to include the matching `us` or `eu` location in the `parent` string. See the [`Synthesize`](https://docs.cloud.google.com/text-to-speech/docs/create-audio) documentation for more information about configuring the synthesize request body.

### Protocol

To perform text to speech synthesis using a regional endpoint, run the applicable command in the table below to configure the correct endpoint:

Multi-region | Endpoint override  
---|---  
EU | `$ export CLOUD_TTS_ENDPOINT=https://eu-texttospeech.googleapis.com`  
US | `$ export CLOUD_TTS_ENDPOINT=https://us-texttospeech.googleapis.com`  
  
Only Neural2 voices are available from these endpoints:

Single-region | Endpoint override  
---|---  
US Central1 | `$ export CLOUD_TTS_ENDPOINT=https://us-central1-texttospeech.googleapis.com`  
  
The following code sample demonstrates how to send a [`synthesis request`](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize) that keeps all data confined to a specified region. You can substitute either the `EU` or `US` regional endpoint for the CLOUD_TTS_ENDPOINT variable. Replace PROJECT_ID with your project ID.
    
    
    $ curl   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "x-goog-user-project: PROJECT_ID" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
              'input':{
                'text':'Android is a mobile operating system developed by Google,
                 based on the Linux kernel and designed primarily for
                 touchscreen mobile devices such as smartphones and tablets.'
               },
              'voice':{
                'languageCode':'en-gb',
                'name':'en-GB-Neural2-A',
                'ssmlGender':'FEMALE'
              },
            'audioConfig':{
              'audioEncoding':'MP3'
            }
          }" $CLOUD_TTS_ENDPOINT/v1/text:synthesize > synthesize-text.txt

This example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) to create an access token for your Google Account. For instructions on installing the gcloud CLI, see [Authenticate to Cloud TTS](https://docs.cloud.google.com/text-to-speech/docs/authentication).

## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
