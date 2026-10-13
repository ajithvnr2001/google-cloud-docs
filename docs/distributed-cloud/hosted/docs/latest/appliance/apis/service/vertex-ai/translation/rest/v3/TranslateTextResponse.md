---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/TranslateTextResponse/
title: TranslateTextResponse \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:11.664072+00:00
---

# TranslateTextResponse  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/TranslateTextResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  TranslateTextResponse Stay organized with collections  Save and categorize content based on your preferences. 

JSON representation  
---  
      
    
    {
      "translations": [
        {
          object ([Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/TranslateTextResponse#Translation))
        }
      ]
    }  
  
Fields  
---  
`translations[]` |  `object (`[Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/TranslateTextResponse#Translation)`)` Text translation responses. This field has the same length as `[`contents`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/projects/translateText#body.request_body.FIELDS.contents)`.  
  
## Translation

A single translation response.

JSON representation  
---  
      
    
    {
      "translated_text": string,
      "detected_language_code": string
    }  
  
Fields  
---  
`translated_text` |  `string` Text translated into the target language. If an error occurs during translation, this field might be excluded from the response.  
`detected_language_code` |  `string` The BCP-47 language code of source text in the initial request, detected automatically, if no source language was passed within the initial request. If the source language was passed, auto-detection of the language does not occur and this field is empty.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
