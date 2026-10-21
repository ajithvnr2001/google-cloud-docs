---
url: https://docs.cloud.google.com/vision/docs/service-announcements/
title: Service announcements \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:30.581078+00:00
---

# Service announcements  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/service-announcements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Support ](https://docs.cloud.google.com/vision/docs/support)



Send feedback 

#  Service announcements Stay organized with collections  Save and categorize content based on your preferences. 

Learn about Vision changes such as backward incompatible API changes, product or feature deprecations, mandatory migrations, or potentially disruptive maintenance.

Date Published | Description | Instructions  
---|---|---  
01 October 2021 |  OCR model update ([release notes announcement](https://docs.cloud.google.com/vision/docs/release-notes#October_01_2021)) |  An improved model is now available for [Text Detection (OCR)](https://docs.cloud.google.com/vision/docs/ocr). The new model can be used with `TEXT_DETECTION` and `DOCUMENT_TEXT_DETECTION` features. The same model is used for requests sent to both features.  **With the new model, the distribution of confidence scores of responses will change.** For more information, see the October 1, 2021 note.  You have 90 days from today to test the new model by specifying "builtin/latest" in the model field of the `[Feature](https://docs.cloud.google.com/vision/docs/reference/rest/v1/Feature)` object. At the end of that period, it will be promoted to the default model accessible as "builtin/stable". After that event, the original models will still be available for another 90 days using "builtin/legacy".  If you encounter problems with this upgrade, please contact the Vision API engineering team by submitting a ticket in the [private issue tracker](https://issuetracker.google.com/issues/new?component=491447).   
  
## October 01, 2021

Differences in the distribution of confidence scores of responses ("builtin/latest" versus "builtin/stable").

**FNR (False Negative Ratio)** : The ratio of correct symbol predictions with confidence score less than the threshold.

![False negative ratio graph](https://docs.cloud.google.com/static/vision/docs/images/FNR.png)

**FPR (False Positive Ratio)** : The ratio of incorrect symbol predictions with confidence score greater than or equal to the threshold.

![False positive ratio graph](https://docs.cloud.google.com/static/vision/docs/images/FPR.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
