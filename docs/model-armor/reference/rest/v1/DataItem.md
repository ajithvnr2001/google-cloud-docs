---
url: https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem/
title: DataItem \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:36.870492+00:00
---

# DataItem  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  DataItem Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ByteDataItem
    * JSON representation
  * ByteItemType



Represents Data item

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "byteItem": {
        object ([ByteDataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem#ByteDataItem))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Either of text or bytes data. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Plaintext string data for sanitization.  
`byteItem` |  `object (`[ByteDataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem#ByteDataItem)`)` Data provided in the form of bytes.  
End of mutually exclusive fields.  
  
## ByteDataItem

Represents Byte Data item.

JSON representation  
---  
      
    
    {
      "byteDataType": enum ([ByteItemType](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem#ByteItemType)),
      "byteData": string,
      "fileLabel": string
    }  
  
Fields  
---  
`byteDataType` |  `enum (`[ByteItemType](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem#ByteItemType)`)` Required. The type of byte data  
`byteData` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Bytes DataA base64-encoded string.  
`fileLabel` |  `string` Optional. Label of the file. This is used to identify the file in the response.  
  
## ByteItemType

Option to specify the type of byte data.

Enums  
---  
`BYTE_ITEM_TYPE_UNSPECIFIED` | Unused  
`PLAINTEXT_UTF8` | plain text  
`PDF` | PDF  
`WORD_DOCUMENT` | DOCX, DOCM, DOTX, DOTM  
`EXCEL_DOCUMENT` | XLSX, XLSM, XLTX, XLYM  
`POWERPOINT_DOCUMENT` | PPTX, PPTM, POTX, POTM, POT  
`TXT` | TXT  
`CSV` | CSV  
`IMAGE` | IMAGE  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-07 UTC."],[],[]] 
