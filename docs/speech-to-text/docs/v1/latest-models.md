---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/latest-models/
title: Introduction to Latest Models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:37.544333+00:00
---

# Introduction to Latest Models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/latest-models/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Introduction to Latest Models Stay organized with collections  Save and categorize content based on your preferences. 

The "latest" model tags in the Cloud Speech-to-Text API give access to two new model tags that can be used when you specify the model field. These models are designed to give you access to the latest speech technology and machine learning research from Google, and can provide higher accuracy for speech recognition over other available models. However, some features that are supported by other available models are not yet supported by the "latest" models.

The latest models are based on the Conformer Speech Model technology from Google. To find out more, see [Google Research Publications](https://research.google/pubs/).

Using the latest models requires a general understanding of using the Cloud Speech-to-Text API or UI.

### Model identifiers

The latest models are available in two different versions:

  * The `latest_short` model is for short utterances that are a few seconds in length. It is useful for trying to capture commands or other single shot directed speech use cases. Consider using `latest_short` instead of the `command_and_search` model.

  * The `latest_long` model is for any kind of long form content such as media or spontaneous speech and conversations. Consider using `latest_long` in place of `video`, especially if `video` is not available in your target language. You can also use `latest_long` in place of the `default` model.




### Model technology

The goal of the latest models is to bring the latest in speech technology directly to Google Cloud users. Our current Latest models are based on the Conformer Speech Model technology from Google, but this may change in the future. To find out more, check out [Google Research Publications](https://research.google/pubs/) list.

### Pricing

The `latest_long` and `latest_short` models are billed as "Standard" and subject to the same usage and costs as the `command_and_search` or `default` models. For more information, see [Pricing](https://docs.cloud.google.com/speech-to-text/pricing).

### Model updates

Latest models are based on rapidly advancing machine learning technology. For this reason we might perform model updates or refreshes more frequently than on our other models. These updates can add additional features or make slight changes to accuracy or latency.

### Languages

Latest models are available in more than 20 languages and more than 50 variants. We are always adding languages, so refer to [Languages](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) for the most up to date list.

### Feature Support and Limitations

Feature support varies by language. See [Languages](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) for a full list of supported features.

The latest models don't support the following feature:

  * **Confidence scores** \- The API will return a value, but it is not truly a confidence score.



### Model Service Level Agreement

The latest models are considered a Generally Available part of the Cloud Speech-to-Text API. As such the functionality they support is available in the V1 API and eligible for the same Service Level Agreement and other protections afforded to Generally Available products and features.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
