---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/projects/translateText/
title: Method: projects.translateText \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:11.735170+00:00
---

# Method: projects.translateText  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/projects/translateText/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Method: projects.translateText Stay organized with collections  Save and categorize content based on your preferences. 

Translates input text and returns translated text.

### HTTP request

`POST https://{TRANSLATION_GDC_ENDPOINT}/v3/{parent}:translateText`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Project to make a call. Must refer to a caller's project.Format: `/projects/{project-id}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "contents": [
        string
      ],
      "mime_type": string,
      "source_language_code": string,
      "target_language_code": string,
        string: string,
        ...
      }
    }  
  
Fields  
---  
`contents[]` |  `string` Required. The content of the input in string format. We recommend the total content be less than 30k codepoints. The max length of this field is 1024.  
`mime_type` |  `string` Optional. The format of the source text, for example, "text/html", "text/plain". If left blank, the MIME type defaults to "text/html".  
`source_language_code` |  `string` Optional. The BCP-47 language code of the input text if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in Language Support. If the source language isn't specified, the API attempts to identify the source language automatically and returns the source language within the response.  
`target_language_code` |  `string` Required. The BCP-47 language code to use for translation of the input text, set to one of the language codes listed in Language Support.  
  
### Response body

If successful, the response body contains an instance of `[TranslateTextResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/TranslateTextResponse)`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
