---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/InstanceData/
title: InstanceData \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:27:29.936924+00:00
---

# InstanceData  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/InstanceData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  InstanceData Stay organized with collections  Save and categorize content based on your preferences. 

Instance data used to populate placeholders in a metric prompt template.

Fields  
  
`data` `Union type`  
  
Supported formats for instance data. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`text` `string` Text data. | `contents` `object (`[Contents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/InstanceData#Contents)`)` List of Gemini content data. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // data
      "text": string,
      "contents": {
        object ([Contents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/InstanceData#Contents))
      }
      // Union type
    }  
  
## Contents

List of standard Content messages from Gemini API.

Fields  
  
`contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Optional. Repeated contents. | JSON representation  
---  
      
    
    {
      "contents": [
        {
          object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
