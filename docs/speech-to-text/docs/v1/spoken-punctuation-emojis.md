---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/spoken-punctuation-emojis/
title: Enable spoken punctuation and spoken emoji \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:56.252211+00:00
---

# Enable spoken punctuation and spoken emoji  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/spoken-punctuation-emojis/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Enable spoken punctuation and spoken emoji Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Speech-to-Text API offers spoken punctuation and spoken emoji features. When you enable this feature, instances of spoken punctuation and emoji detected in your audio data will be replaced by the corresponding punctuation and emoji symbols. For example, if you send a request with spoken punctuation enabled, the transcript "how are you question mark" becomes "how are you?".

To determine whether this feature is available for your language, see [Language support](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages). For complete lists of available spoken symbols, see [Supported spoken punctuation](https://docs.cloud.google.com/speech-to-text/docs/v1/spoken-punctuation) and [Supported spoken emoji](https://docs.cloud.google.com/speech-to-text/docs/v1/spoken-emoji).

To enable the spoken punctuation and emoji features, set `enableSpokenPunctuation` and `enableSpokenEmojis` to `true` in [RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig).

Spoken punctuation is enabled by default for the `command_and_search` model, but can be disabled using the `enableSpokenPunctuation` field. For all other requests, spoken punctuation and spoken emoji are disabled by default.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
