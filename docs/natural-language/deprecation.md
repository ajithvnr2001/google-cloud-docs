---
url: https://docs.cloud.google.com/natural-language/deprecation/
title: Cloud Natural Language API v1beta1 Deprecation Notice \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:13.857884+00:00
---

# Cloud Natural Language API v1beta1 Deprecation Notice  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/deprecation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Resources ](https://docs.cloud.google.com/natural-language/docs/resources)



Send feedback 

#  Cloud Natural Language API v1beta1 Deprecation Notice Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Natural Language API v1beta1 version will be shut down on **December 27, 2019**. After this date, attempts to call the API will fail. You must upgrade to the v1 version of the API and client libraries before this date.

The notable implementation difference between the versions is the attributes of the [Sentiment](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment) type.

  * In v1beta1, the attributes were `"polarity"` and `"magnitude"`, which were used together to calculate the sentiment score (how large the sentiment was)
  * In v1, the attributes are `"magnitude"` and `"score"`, where the value of `"score"` corresponds to the product of v1beta1's `"polarity"` and `"magnitude"`.



If your v1beta1 application uses `"polarity"`, update it to use the sign of the `"score"`: the polarity is positive if the score is positive and negative if the score is negative. If your application uses `"polarity" * "magnitude"`, use `"score"` instead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
