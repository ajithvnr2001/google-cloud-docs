---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ModelType/
title: ModelType \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:47:18.296492+00:00
---

# ModelType  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ModelType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ModelType Stay organized with collections  Save and categorize content based on your preferences. 

Enums  
---  
`MODEL_TYPE_UNSPECIFIED` | Should not be set.  
`CLOUD` | A Model best tailored to be used within Google Cloud, and which cannot be exported. Default.  
`CLOUD_1` | A model type best tailored to be used within Google Cloud, which cannot be exported externally. Compared to the CLOUD model above, it is expected to have higher prediction accuracy.  
`MOBILE_TF_LOW_LATENCY_1` | A model that, in addition to being available within Google Cloud, can also be exported (see ModelService.ExportModel) as TensorFlow or Core ML model and used on a mobile or edge device afterwards. Expected to have low latency, but may have lower prediction quality than other mobile models.  
`MOBILE_TF_VERSATILE_1` | A model that, in addition to being available within Google Cloud, can also be exported (see ModelService.ExportModel) as TensorFlow or Core ML model and used on a mobile or edge device with afterwards.  
`MOBILE_TF_HIGH_ACCURACY_1` | A model that, in addition to being available within Google Cloud, can also be exported (see ModelService.ExportModel) as TensorFlow or Core ML model and used on a mobile or edge device afterwards. Expected to have a higher latency, but should also have a higher prediction quality than other mobile models.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
