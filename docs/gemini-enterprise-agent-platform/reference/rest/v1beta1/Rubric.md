---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric/
title: Rubric \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:44:24.593271+00:00
---

# Rubric  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Rubric Stay organized with collections  Save and categorize content based on your preferences. 

message representing a single testable criterion for evaluation. One input prompt could have multiple rubrics.

Fields  
  
`rubricId` `string` Unique identifier for the rubric. This id is used to refer to this rubric, e.g., in RubricVerdict. | `content` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric#Content)`)` Required. The actual testable criteria for the rubric. | `type` `string` Optional. A type designator for the rubric, which can inform how it's evaluated or interpreted by systems or users. It's recommended to use consistent, well-defined, upper snake_case strings. Examples: "SUMMARIZATION_QUALITY", "SAFETY_HARMFUL_CONTENT", "INSTRUCTION_ADHERENCE". | `importance` `enum (`[Importance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric#Importance)`)` Optional. The relative importance of this rubric. | JSON representation  
---  
      
    
    {
      "rubricId": string,
      "content": {
        object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric#Content))
      },
      "type": string,
      "importance": enum ([Importance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric#Importance))
    }  
  
## Content

Content of the rubric, defining the testable criteria.

Fields  
  
`content_type` `Union type`  
  
The specific type of content that defines the rubric. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`property` `object (`[Property](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric#Property)`)` Evaluation criteria based on a specific property. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // content_type
      "property": {
        object ([Property](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric#Property))
      }
      // Union type
    }  
  
## Property

Defines criteria based on a specific property.

Fields  
  
`description` `string` description of the property being evaluated. Example: "The model's response is grammatically correct." | JSON representation  
---  
      
    
    {
      "description": string
    }  
  
## Importance

Importance level of the rubric.

Enums  
---  
`IMPORTANCE_UNSPECIFIED` | Importance is not specified.  
`HIGH` | High importance.  
`MEDIUM` | Medium importance.  
`LOW` | Low importance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-26 UTC."],[],[]] 
