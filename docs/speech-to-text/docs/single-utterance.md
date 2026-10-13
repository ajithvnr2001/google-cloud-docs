---
url: https://docs.cloud.google.com/speech-to-text/docs/single-utterance/
title: Single utterance behavior \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:00.742265+00:00
---

# Single utterance behavior  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/single-utterance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Single utterance behavior Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Speech-to-Text provides the `latest_short` model for recognizing speech that consists of single utterances. This may be useful for applications where users are issuing single voice commands as opposed to long-form monologue or dictation.

When a recognizer with the `latest_short` model is used for a recognition request, Cloud STT will stop performing recognition once it detects an utterance has finished. Cloud STT will return a speech activity event response with the type `END_OF_SINGLE_UTTERANCE` followed by the transcription results.

## Single utterance and `StreamingRecognize`

In the case where a `latest_short` model [`Recognizer`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v2/projects.locations.recognizers#Recognizer) is selected for a [`StreamingRecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#google.cloud.speech.v2.Speech.StreamingRecognize) request, Cloud STT will close the stream automatically after the utterance has ended.

### With voice activity events

In the case where voice activity events have also been enabled for a `StreamingRecognize` request, Cloud STT will still return speech begin and end voice activity events.

Voice activity timeouts for speech begin will still be applied. Voice activity timeouts for speech end won't be applied, since the stream will be closed as soon as the utterance ends.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
