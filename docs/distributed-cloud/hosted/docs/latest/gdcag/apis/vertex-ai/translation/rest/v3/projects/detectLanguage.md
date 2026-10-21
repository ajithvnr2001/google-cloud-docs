---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects/detectLanguage/
title: Method: projects.detectLanguage \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:46.261777+00:00
---

# Method: projects.detectLanguage  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects/detectLanguage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Method: projects.detectLanguage Stay organized with collections  Save and categorize content based on your preferences. 

Detects the language of text within a request.

### HTTP request

`POST https://{TRANSLATION_GDC_ENDPOINT}/v3/{parent}:detectLanguage`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Project to make a call. Must refer to a caller's project.Format: `projects/{project-id}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mime_type": string,
        string: string,
        ...
      },
      "content": string
    }  
  
Fields  
---  
`mime_type` |  `string` Optional. The format of the source text, for example, "text/html", "text/plain". If left blank, the MIME type defaults to "text/html".  
`content` |  `string` The content of the input stored as a string.  
  
### Response body

If successful, the response body contains an instance of `[DetectLanguageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/DetectLanguageResponse)`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
