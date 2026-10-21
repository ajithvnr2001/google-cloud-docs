---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/UnitVariable/
title: UnitVariable \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:10.695808+00:00
---

# UnitVariable  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/UnitVariable/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  UnitVariable Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Type



UnitVariable describes a parameter for a Unit.

JSON representation  
---  
      
    
    {
      "variable": string,
      "type": enum ([Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/UnitVariable#Type)),
      "value": string
    }  
  
Fields  
---  
`variable` |  `string` Required. Immutable. Name of the variable from actuation configs.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/UnitVariable#Type)`)` Optional. Immutable. Name of a supported variable type. Supported types are string, int, bool.  
`value` |  `string` Optional. String encoded value for the variable.  
  
## Type

Enumeration of variable types. `STRUCT` and `LIST` values should be JSON-encoded strings.

Enums  
---  
`TYPE_UNSPECIFIED` | Variable type is unspecified.  
`STRING` | Variable type is string.  
`INT` | Variable type is int.  
`BOOL` | Variable type is bool.  
`STRUCT` | Variable type is struct.  
`LIST` | Variable type is list.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
