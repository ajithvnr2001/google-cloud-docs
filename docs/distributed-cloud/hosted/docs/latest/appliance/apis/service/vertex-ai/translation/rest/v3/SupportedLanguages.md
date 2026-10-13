---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/SupportedLanguages/
title: SupportedLanguages \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:11.899976+00:00
---

# SupportedLanguages  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/SupportedLanguages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  SupportedLanguages Stay organized with collections  Save and categorize content based on your preferences. 

The response message for discovering supported languages.

JSON representation  
---  
      
    
    {
      "languages": [
        {
          object ([SupportedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/SupportedLanguages#SupportedLanguage))
        }
      ]
    }  
  
Fields  
---  
`languages[]` |  `object (`[SupportedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/SupportedLanguages#SupportedLanguage)`)` A list of supported language responses. This list contains an entry for each language the Translation API supports.  
  
## SupportedLanguage

A single supported language response corresponds to information related to one supported language.

JSON representation  
---  
      
    
    {
      "language_code": string,
      "display_name": string,
      "support_source": boolean,
      "support_target": boolean
    }  
  
Fields  
---  
`language_code` |  `string` Supported language code, generally consisting of its ISO 639-1 identifier, for example, `en`, `ja`. In certain cases, BCP-47 codes including language and region identifiers are returned (for example, 'zh-TW' and 'zh-CN')  
`display_name` |  `string` Human-readable name of the language localized in the display language specified in the request.  
`support_source` |  `boolean` Can be used as source language.  
`support_target` |  `boolean` Can be used as target language.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
