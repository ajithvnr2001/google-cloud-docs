---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException/
title: AssetException \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:06.358124+00:00
---

# AssetException  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  AssetException Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ExceptionType



An exception of an asset.

JSON representation  
---  
      
    
    {
      "exceptionType": enum ([ExceptionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException#ExceptionType)),
      "details": string
    }  
  
Fields  
---  
`exceptionType` |  `enum (`[ExceptionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException#ExceptionType)`)` The type of exception.  
`details` |  `string` The details of the exception.  
  
## ExceptionType

The type of exception.

Enums  
---  
`EXCEPTION_TYPE_UNSPECIFIED` | exceptionType is not applicable for the current asset.  
`TRUNCATION` | The asset content is truncated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
