---
url: https://docs.cloud.google.com/model-armor/reference/rest/v1/MultiLanguageDetectionMetadata/
title: MultiLanguageDetectionMetadata \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:46:30.488328+00:00
---

# MultiLanguageDetectionMetadata  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/rest/v1/MultiLanguageDetectionMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  MultiLanguageDetectionMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Message for Enabling Multi Language Detection.

JSON representation  
---  
      
    
    {
      "sourceLanguage": string,
      "enableMultiLanguageDetection": boolean
    }  
  
Fields  
---  
`sourceLanguage` |  `string` Optional. Optional Source language of the user prompt.If multi-language detection is enabled and this field is not set, the source language will be automatically detected. When a source language is provided, Model Armor uses it to sanitize the input. In that case the system does not perform auto-detection and relies solely on the specified language.This string field accepts a language code from the ISO-639 standard. For a list of languages supported by Model Armor, see [Model Armor supported languages](https://cloud.google.com/security-command-center/docs/model-armor-overview#languages-supported). For a comprehensive list of language codes, see [ISO-639](https://cloud.google.com/translate/docs/languages#nmt).  
`enableMultiLanguageDetection` |  `boolean` Optional. Enable detection of multi-language prompts and responses.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-24 UTC."],[],[]] 
