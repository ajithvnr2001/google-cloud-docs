---
url: https://docs.cloud.google.com/text-to-speech/quotas/
title: Quotas & limits \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:01.395865+00:00
---

# Quotas & limits  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Guides ](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



Send feedback 

#  Quotas & limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains current API restrictions and usage limits on use of Cloud Text-to-Speech. This page will be updated to reflect any changes to these restrictions and usage limits. We reserve the right to change these limits. To keep track of your content and request totals, see the documentation about [monitoring your API usage](https://cloud.google.com/apis/docs/monitoring).

You can use the audio data files you create using Cloud Text-to-Speech in your applications or media in compliance with the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms/) including compliance with all applicable law.

You can request an increase to the [requests limit](https://docs.cloud.google.com/text-to-speech/quotas#requests_limit) from the [Google Cloud console](https://console.cloud.google.com/). The [content limits](https://docs.cloud.google.com/text-to-speech/quotas#content_limits) cannot be increased. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage).

After submitting your request, Google may contact you for more information, and inform you whether your request is approved or denied.

## Content limits

Content to Cloud TTS is provided as text data, either as raw strings or SSML-formatted data.

The API contains the following limits on the size of this content (and are subject to change):

Speech Synthesis Limit | Value  
---|---  
Total bytes per request | 5,000  
**Note:** In some locales (for example ja-JP), a single character is made up of multiple bytes.

## Requests limit

The current API usage limits for Cloud TTS are as follows (and are subject to change):

Type of Limit | Usage Limit  
---|---  
Chirp3RequestsPerMinutePerProject | 200  
ChirpVoiceCloningRequestsPerMinutePerProject | 30  
ConcurrentStreamingSessionsPerProject | 100  
GenerateVoiceCloningKeyRequestsPerMinutePerProject | 10  
LongAudioSynthesisQueryRequestsPerMinutePerProject | 100  
LongAudioSynthesisRequestsPerMinutePerProject | 100  
Neural2RequestsPerMinutePerProject | 1,000  
PolyglotRequestsPerMinutePerProject | 1,000  
RequestsPerMinutePerProject | 1,000  
StudioRequestsPerMinutePerProject | 500  
**Note:** The `RequestsPerMinutePerProject` quota applies to all Cloud TTS voices that don't have a dedicated quota listed in this table.

## Gemini-TTS Usage Limits

Starting with Gemini 3.1 Flash TTS, Gemini-TTS models support dynamic throughput-based usage limits. See a detailed explanation of [consumption options](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deploy/consumption-options).

Model name | Consumption options  
---|---  
gemini-3.1-flash-tts-preview | [Standard PayGo](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/standard-paygo)  
  
The API usage limits for earlier models are as follows:

Model name | Usage limit (QPM1)  
---|---  
gemini-2.5-flash-tts | 1502  
gemini-2.5-pro-tts | 1252  
  
1Queries Per Minute

2The usage limits stated are default maximum values and they are subject to change. The effective quota limits may vary by project, and may be increased upon request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
