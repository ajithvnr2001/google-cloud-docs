---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-RecognitionFeatures-MultiChannelMode/
title: Cloud Speech-to-Text V2 API - Module Google::Cloud::Speech::V2::RecognitionFeatures::MultiChannelMode (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:12.086477+00:00
---

# Cloud Speech-to-Text V2 API - Module Google::Cloud::Speech::V2::RecognitionFeatures::MultiChannelMode (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-RecognitionFeatures-MultiChannelMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Speech-to-Text V2 API - Module Google::Cloud::Speech::V2::RecognitionFeatures::MultiChannelMode (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Speech-to-Text V2 API module Google::Cloud::Speech::V2::RecognitionFeatures::MultiChannelMode.

Options for how to recognize multi-channel audio.

## Constants 

### MULTI_CHANNEL_MODE_UNSPECIFIED

**value:** 0  
Default value for the multi-channel mode. If the audio contains multiple channels, only the first channel will be transcribed; other channels will be ignored.

### SEPARATE_RECOGNITION_PER_CHANNEL

**value:** 1  
If selected, each channel in the provided audio is transcribed independently. This cannot be selected if the selected [model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-Recognizer#Google__Cloud__Speech__V2__Recognizer_model_instance_ "Google::Cloud::Speech::V2::Recognizer#model \(method\)") is `latest_short`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
