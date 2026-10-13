---
url: https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/Attributes/
title: Attributes \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:00.823288+00:00
---

# Attributes  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/Attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Reference ](https://docs.cloud.google.com/trace/docs/reference)



Send feedback 

#  Attributes Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AttributeValue
    * JSON representation



A set of attributes as key-value pairs.

JSON representation  
---  
      
    
    {
      "attributeMap": {
        string: {
          object ([AttributeValue](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/Attributes#AttributeValue))
        },
        ...
      },
      "droppedAttributesCount": integer
    }  
  
Fields  
---  
`attributeMap` |  `map (key: string, value: object (`[AttributeValue](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/Attributes#AttributeValue)`))` Optional. A set of attributes. Each attribute's key can be up to 128 bytes long. The value can be a string up to 256 bytes, a signed 64-bit integer, or the boolean values `true` or `false`. For example:
    
    
    "/instance_id": { "stringValue": { "value": "my-instance" } }
    "/http/request_bytes": { "intValue": 300 }
    "example.com/myattribute": { "boolValue": false }
      
  
`droppedAttributesCount` |  `integer` Optional. The number of attributes that were discarded. Attributes can be discarded because their keys are too long or because there are too many attributes. If this value is 0 then all attributes are valid.  
  
## AttributeValue

The allowed types for `[VALUE]` in a `[KEY]:[VALUE]` attribute.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "stringValue": {
        object ([TruncatableString](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/TruncatableString))
      },
      "intValue": string,
      "boolValue": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of the value. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`stringValue` |  `object (`[TruncatableString](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/TruncatableString)`)` Optional. A string up to 256 bytes long.  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. A 64-bit signed integer.  
`boolValue` |  `boolean` Optional. A Boolean value represented by `true` or `false`.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
