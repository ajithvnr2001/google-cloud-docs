---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Value/
title: Value \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:58:24.537001+00:00
---

# Value  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Value/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Value Stay organized with collections  Save and categorize content based on your preferences. 

`value` represents a dynamically typed value which can be either null, a number, a string, a boolean, a recursive struct value, or a list of values. A producer of value is expected to set one of these variants. Absence of any variant indicates an error.

Fields  
  
`kind` `Union type`  
  
The kind of value. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`nullValue` `null` Represents a null value. | `numberValue` `number` Represents a double value. | `stringValue` `string` Represents a string value. | `boolValue` `boolean` Represents a boolean value. | `structValue` `object (`[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Struct)`)` Represents a structured value. | `listValue` `object (`[ListValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Value#ListValue)`)` Represents a repeated `value`. | `contentValue` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Content)`)` Represents rich content (text, image, etc.). End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // kind
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object ([Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Struct))
      },
      "listValue": {
        object ([ListValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Value#ListValue))
      },
      "contentValue": {
        object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Content))
      }
      // Union type
    }  
  
## ListValue

`ListValue` is a wrapper around a repeated field of values.

Fields  
  
`values[]` `object (`[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Value)`)` Repeated field of dynamically typed values. | JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Value))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
