---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem/
title: ByteContentItem \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:42.419351+00:00
---

# ByteContentItem  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  ByteContentItem Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * BytesType



Container for bytes to inspect or redact.

JSON representation  
---  
      
    
    {
      "type": enum ([BytesType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem#BytesType)),
      "data": string
    }  
  
Fields  
---  
`type` |  `enum (`[BytesType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem#BytesType)`)` The type of data stored in the bytes string. Default will be TEXT_UTF8.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Content data to inspect or redact.A base64-encoded string.  
  
## BytesType

The type of data being sent for inspection. To learn more, see [Supported file types](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).

Only the first frame of each multiframe image is inspected. Metadata and other frames aren't inspected.

Enums  
---  
`BYTES_TYPE_UNSPECIFIED` | Unused  
`IMAGE` | Any image type.  
`IMAGE_JPEG` | jpeg  
`IMAGE_BMP` | bmp  
`IMAGE_PNG` | png  
`IMAGE_SVG` | svg  
`TEXT_UTF8` | plain text  
`WORD_DOCUMENT` | docx, docm, dotx, dotm  
`PDF` | pdf  
`POWERPOINT_DOCUMENT` | pptx, pptm, potx, potm, pot  
`EXCEL_DOCUMENT` | xlsx, xlsm, xltx, xltm  
`AVRO` | avro  
`CSV` | csv  
`TSV` | tsv  
`AUDIO` | Audio file types. Only used for profiling.  
`VIDEO` | Video file types. Only used for profiling.  
`EXECUTABLE` | Executable file types. Only used for profiling.  
`AI_MODEL` | AI model file types. Only used for profiling.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
