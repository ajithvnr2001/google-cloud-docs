---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-cloning/
title: Voice cloning \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:46.278952+00:00
---

# Voice cloning  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-cloning/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Voice cloning Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When using text-to-speech for your agent, you can create personalized voice models by training a model with your own audio recordings.

## Limitations

This feature is only available for the following languages and locales:

  * ar-XA
  * cmn-CN
  * de-DE
  * en-AU
  * en-GB
  * en-IN
  * en-US
  * es-ES
  * es-US
  * fr-CA
  * fr-FR
  * gu-IN
  * hi-IN
  * id-ID
  * it-IT
  * ko-KR
  * mr-IN
  * nl-NL
  * pl-PL
  * pt-BR
  * ru-RU
  * ta-IN
  * te-IN
  * th-TH
  * tr-TR
  * ur-IN
  * vi-VN



## Configuration

To configure a voice cloning:

  1. This feature is provided via the Text-to-Speech product, and the feature is currently restricted access. See the [instructions for requesting access](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice).
  2. [Train your model](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice#use_chirp_3_instant_custom_voice). When creating your model, copy the voice key. You will need this value to configure your agent.
  3. Go to the Dialogflow CX agent settings, select the **Speech and IVR** tab, then scroll down to **Voice selection**.
  4. For the voice name, select **Cloned voice**.
  5. For the voice key, paste the voice key you copied above.
  6. You can click the **Test key** button to verify that the key is valid.



[ Previous arrow_back  Speech models  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models)

[ Next Speech adaptation  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
