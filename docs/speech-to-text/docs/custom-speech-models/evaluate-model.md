---
url: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/evaluate-model/
title: Evaluate models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:33.524504+00:00
---

# Evaluate models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/evaluate-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Evaluate models Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use the benchmarking functionality of the Cloud Cloud Speech-to-Text Console to measure the accuracy of any of the [transcription models](https://docs.cloud.google.com/speech-to-text/docs/transcription-model) used in the Cloud Speech-to-Text V2 API.

Cloud Cloud Speech-to-Text Console provides visual benchmarking for pre-trained and Custom Speech-to-Text models. You can inspect the recognition quality by comparing Word-Error-Rate (WER) evaluation metrics across multiple transcription models to help you decide which model best fits your application.

## Before you begin

Ensure you have signed up for a Google Cloud account, created a project, trained a custom speech model, and deployed using an endpoint.

## Create a ground-truth dataset

To create a custom benchmarking dataset, gather audio samples that accurately reflect the type of traffic the transcription model will encounter in a production environment. The aggregate duration of these audio files should ideally span a minimum of 30 minutes and not exceed 10 hours. To assemble the dataset, you will need to:

  1. Create a directory in a Cloud Storage bucket of your choice to store the audio and text files for the dataset.
  2. For every audio-file in the dataset, create reasonably accurate transcriptions. For each audio file (such as `example_audio_1.wav`), a corresponding ground-truth text file (`example_audio_1.txt`) must be created. This service uses these audio-text pairings in a Cloud Storage bucket to assemble the dataset.



## Benchmark the model

Using the Custom Speech-to-Text model and your benchmarking dataset to assess the accuracy of your model, follow the [Measure and improve accuracy guide](https://docs.cloud.google.com/speech-to-text/docs/measure-accuracy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
