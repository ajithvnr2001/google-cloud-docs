---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.EncodingType
title: Cloud Natural Language v2 API - Enum EncodingType (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:18.168946+00:00
---

# Cloud Natural Language v2 API - Enum EncodingType (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.EncodingType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Natural Language v2 API - Enum EncodingType (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.EncodingType)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/1.0.0-beta05/Google.Cloud.Language.V2.EncodingType)


    
    
    public enum EncodingType

Reference documentation and code samples for the Cloud Natural Language v2 API enum EncodingType.

Represents the text encoding that the caller uses to process the output. Providing an `EncodingType` is recommended because the API provides the beginning offsets for various outputs, such as tokens and mentions, and languages that natively use different text encodings may access offsets differently.

## Namespace

[Google.Cloud.Language.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2)

## Assembly

Google.Cloud.Language.V2.dll

## Fields   
  
---  
**Name** | **Description**  
`None` | If `EncodingType` is not specified, encoding-dependent information (such as `begin_offset`) will be set at `-1`.  
`Utf16` | Encoding-dependent information (such as `begin_offset`) is calculated based on the UTF-16 encoding of the input. Java and JavaScript are examples of languages that use this encoding natively.  
`Utf32` | Encoding-dependent information (such as `begin_offset`) is calculated based on the UTF-32 encoding of the input. Python is an example of a language that uses this encoding natively.  
`Utf8` | Encoding-dependent information (such as `begin_offset`) is calculated based on the UTF-8 encoding of the input. C++ and Go are examples of languages that use this encoding natively.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
