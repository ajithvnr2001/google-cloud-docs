---
url: https://docs.cloud.google.com/natural-language/docs/languages/
title: Language Support \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:00.531654+00:00
---

# Language Support  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Reference ](https://docs.cloud.google.com/natural-language/docs/apis)



Send feedback 

#  Language Support Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Natural Language API supports a variety of languages. These languages are specified within a request using the optional [`language`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents#Document.FIELDS.language) parameter. Language code parameters conform to [ISO-639-1](https://en.wikipedia.org/wiki/ISO_639-1) or [BCP-47](https://tools.ietf.org/html/bcp47) identifiers. If you do not specify a `language` parameter, then the language for the request is auto-detected by the Natural Language API.

The list of supported languages differs depending on the feature.

## Content classification

### [V2 Model](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/ClassificationModelOptions)

Language | ISO-639-1 Code  
---|---  
Chinese (Simplified) | `zh`  
Chinese (Traditional) | `zh-Hant`  
Dutch | `nl`  
English | `en`  
French | `fr`  
German | `de`  
Italian | `it`  
Japanese | `ja`  
Korean | `ko`  
Portuguese (Brazilian & Continental) | `pt`  
Russian | `ru`  
Spanish | `es`  
  
### [V1 Model](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/ClassificationModelOptions)

Language | ISO-639-1 Code  
---|---  
English | `en`  
  
## Syntactic analysis

Language | ISO-639-1 Code  
---|---  
Chinese (Simplified) | `zh`  
Chinese (Traditional) | `zh-Hant`  
English | `en`  
French | `fr`  
German | `de`  
Italian | `it`  
Japanese | `ja`  
Korean | `ko`  
Portuguese (Brazilian & Continental) | `pt`  
Russian | `ru`  
Spanish | `es`  
  
## Entity analysis

Language | ISO-639-1 Code  
---|---  
Chinese (Simplified) | `zh`  
Chinese (Traditional) | `zh-Hant`  
English | `en`  
French | `fr`  
German | `de`  
Italian | `it`  
Japanese | `ja`  
Korean | `ko`  
Portuguese (Brazilian & Continental) | `pt`  
Russian | `ru`  
Spanish | `es`  
  
## Sentiment analysis

Language | ISO-639-1 Code  
---|---  
Arabic | `ar`  
Chinese (Simplified) | `zh`  
Chinese (Traditional) | `zh-Hant`  
Dutch | `nl`  
English | `en`  
French | `fr`  
German | `de`  
Indonesian | `id`  
Italian | `it`  
Japanese | `ja`  
Korean | `ko`  
Portuguese (Brazilian & Continental) | `pt`  
Spanish | `es`  
Thai | `th`  
Turkish | `tr`  
Vietnamese | `vi`  
  
## Entity sentiment analysis

Language | ISO-639-1 Code  
---|---  
English | `en`  
Japanese | `ja`  
Spanish | `es`  
  
## Text moderation

Language | ISO-639-1 Code  
---|---  
Arabic | *`ar`  
Chinese (Simplified) | `zh`  
Dutch | *`nl`  
English | `en`  
French | `fr`  
German | `de`  
Hindi | *`hi`  
Indonesian | *`id`  
Italian | `it`  
Japanese | `ja`  
Korean | `ko`  
Portuguese (Brazilian & Continental) | `pt`  
Russian | *`ru`  
Spanish | `es`  
  
*language support is limited based on the type of text (eg. webpage, chat message, etc) for some attributes. In any case, we recommend thorough evaluation for your use case.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
