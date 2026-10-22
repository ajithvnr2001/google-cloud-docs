---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/vertex-ai-stt-rpc-ref/
title: Speech-to-Text RPC API reference \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:57.365271+00:00
---

# Speech-to-Text RPC API reference  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/vertex-ai-stt-rpc-ref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Speech-to-Text RPC API reference Stay organized with collections  Save and categorize content based on your preferences. 

This is the gRPC API reference for Speech-to-Text. It is one of the Vertex AI pre-trained APIs available on Google Distributed Cloud air-gapped (GDC). 

Use this guide to programmatically integrate speech recognition technologies into developer applications. Send audio and receive a text transcription from the Vertex AI Speech-to-Text API service. For example, if you submit audio in [Spanish](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-stt), a corresponding text transcription in Spanish is the result.

### Speech-to-Text methods

There are two methods available in GDC:

  * [Recognize](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1): Performs synchronous speech recognition. `Recognize` receives results after all audio has been sent and processed.
  * [StreamingRecognize](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1): Performs bidirectional streaming speech recognition. `StreamingRecognize` receives results while sending audio. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
