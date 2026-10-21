---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor/
title: LabelDescriptor \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:17.501616+00:00
---

# LabelDescriptor  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  LabelDescriptor Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ValueType



A description of a label.

JSON representation  
---  
      
    
    {
      "key": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor#ValueType)),
      "description": string
    }  
  
Fields  
---  
`key` |  `string` The key for this label. The key must meet the following criteria:

  * Does not exceed 100 characters.
  * Matches the following regular expression: `[a-zA-Z][a-zA-Z0-9_]*`
    * The first character must be an upper- or lower-case letter.
    * The remaining characters must be letters, digits, or underscores.

  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor#ValueType)`)` The type of data that can be assigned to the label.  
`description` |  `string` A human-readable description for the label.  
  
## ValueType

Value types that can be used as label values.

Enums  
---  
`STRING` | A variable-length string, not to exceed 1,024 characters. This is the default value type.  
`BOOL` | Boolean; true or false.  
`INT64` | A 64-bit signed integer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
