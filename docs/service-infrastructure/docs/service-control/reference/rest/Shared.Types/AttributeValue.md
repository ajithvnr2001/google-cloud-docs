---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue/
title: AttributeValue \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:34.147619+00:00
---

# AttributeValue  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  AttributeValue Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TruncatableString
    * JSON representation



The allowed types for [VALUE] in a `[KEY]:[VALUE]` attribute.

JSON representation  
---  
      
    
    {
    
      // Union field value can be only one of the following:
      "stringValue": {
        object ([TruncatableString](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue#TruncatableString))
      },
      "intValue": string,
      "boolValue": boolean
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
Union field `value`. The type of the value. `value` can be only one of the following:  
`stringValue` |  `object (`[TruncatableString](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue#TruncatableString)`)` A string up to 256 bytes long.  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` A 64-bit signed integer.  
`boolValue` |  `boolean` A Boolean value represented by `true` or `false`.  
  
## TruncatableString

Represents a string that might be shortened to a specified length.

JSON representation  
---  
      
    
    {
      "value": string,
      "truncatedByteCount": integer
    }  
  
Fields  
---  
`value` |  `string` The shortened string. For example, if the original string is 500 bytes long and the limit of the string is 128 bytes, then `value` contains the first 128 bytes of the 500-byte string.Truncation always happens on a UTF8 character boundary. If there are multi-byte characters in the string, then the length of the shortened string might be less than the size limit.  
`truncatedByteCount` |  `integer` The number of bytes removed from the original string. If this value is 0, then the string was not shortened.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
