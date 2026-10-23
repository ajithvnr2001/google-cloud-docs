---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/speech/speech-to-text/
title: Convert speech to text \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:48.486416+00:00
---

# Convert speech to text  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/speech/speech-to-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Convert speech to text Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Vertex AI Studio to convert speech to text.

To learn how to convert text to speech, see [Generate speech with Gemini TTS](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/text-to-speech/overview).

## Convert speech to text

To convert speech to text, do the following:

  1. In the Agent Platform section of the Google Cloud console, go to the **Vertex AI Studio** page.

[Go to Vertex AI Studio](https://console.cloud.google.com/agent-platform/studio/overview)

  2. Click **Generate speech**.

  3. Select the **Speech-to-text** tab.

  4. In **Speech** , click **Browse** to select the audio file that you want to convert to text.

  5. In the **Language** selector box, select the language of the speech in the audio file.

  6. Click **Submit**.

The converted text appears in **Text**.




## Limitations

  * Audio files can be a maximum 60 seconds or 10 MB (whichever is less).
  * Files are transcribed with the [Chirp](https://cloud.google.com/speech-to-text/v2/docs/usm/usm-model) model.
  * Only 16-bit linear PCM WAV files are supported.



You can use the [Speech-to-Text UI](https://docs.cloud.google.com/speech-to-text/docs/transcribe-console) directly to overcome these limitations.

## What's next

  * For more models, advanced features, and ability to transcribe files up to 8 hours, see [Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/transcribe-console).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
