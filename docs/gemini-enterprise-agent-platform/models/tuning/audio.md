---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/audio/
title: Audio tuning \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:05.079061+00:00
---

# Audio tuning  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/audio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Audio tuning Stay organized with collections  Save and categorize content based on your preferences. 

This page provides prerequisites and detailed instructions for fine-tuning Gemini models on audio data using supervised learning.

## Use cases

Tuning audio models enhances their performance by tailoring them to specific needs. This can involve improving speech recognition for different accents, fine-tuning music genre classification, optimizing sound event detection, customizing audio generation, adapting to noisy environments, improving audio quality, and personalizing audio experiences. Here are some common audio tuning use cases:

  * **Enhanced voice assistants** :

    * Voice food ordering: Develop voice-activated systems for seamless food ordering and delivery.
  * **Audio content analysis** :

    * Automated transcription: Generate highly accurate transcripts, even in noisy environments.
    * Audio summarization: Summarize key points from podcasts or audiobooks.
    * Music classification: Categorize music based on genre, mood, or other characteristics.
  * **Accessibility and assistive technologies** :

    * Real-time captioning: Provide live captions for events or video calls.
    * Voice-controlled applications: Develop applications controlled entirely by voice.
    * Language learning: Create tools that provide personalized feedback on pronunciation.



## Limitations

### Gemini 2.5 models

Specification | Value  
---|---  
Maximum audio length per example | 60 minutes  
Maximum audio files per example | 1  
Maximum audio file size | 100MB  
  
To learn more about audio sample requirements, see the [Audio understanding (speech only)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding#audio-requirements) page.

## Dataset format

The `fileUri` for your dataset can be the URI for a file in a Cloud Storage bucket, or it can be a publicly available HTTP or HTTPS URL.

To see the generic format example, see [Dataset example for Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini-supervised-tuning-prepare#dataset-example).

The following is an example of an audio dataset.
    
    
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "fileData": {
                "mimeType": "audio/mpeg",
                "fileUri": "gs://cloud-samples-data/generative-ai/audio/pixel.mp3"
                }
            },
            {
              "text": "Please summarize the conversation in one sentence."
            }
          ]
        },
        {
          "role": "model",
          "parts": [
            {
              "text": "The podcast episode features two product managers for Pixel devices discussing the new features coming to Pixel phones and watches."
            }
          ]
        }
      ]
    }
    

## What's next

  * To learn more about the Gemini audio understanding model, see [Audio understanding (speech only)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding).
  * To start tuning, see [Tune Gemini models by using supervised fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning).
  * To learn how supervised fine-tuning can be used in a solution that builds a generative AI knowledge base, see [Jump Start Solution: Generative AI knowledge base](https://docs.cloud.google.com/architecture/ai-ml/generative-ai-knowledge-base).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
