---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/DataProtectionPolicy/
title: DataProtectionPolicy \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:09.187521+00:00
---

# DataProtectionPolicy  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/DataProtectionPolicy/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  DataProtectionPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SensitiveDataProtectionPolicy
    * JSON representation



Contains the data protection policy config for a DataStore or a connector.

JSON representation  
---  
      
    
    {
      "sensitiveDataProtectionPolicy": {
        object ([SensitiveDataProtectionPolicy](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/DataProtectionPolicy#SensitiveDataProtectionPolicy))
      }
    }  
  
Fields  
---  
`sensitiveDataProtectionPolicy` |  `object (`[SensitiveDataProtectionPolicy](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/DataProtectionPolicy#SensitiveDataProtectionPolicy)`)` Optional. Specifies the sensitive data protection policy for the connector source.  
  
## SensitiveDataProtectionPolicy

Specifies a Sensitive data Protection (<https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview>) policy.

JSON representation  
---  
      
    
    {
      "policy": string
    }  
  
Fields  
---  
`policy` |  `string` Optional. Specifies the resource name of the Sensitive data Protection content policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
