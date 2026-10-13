---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Internal.ListAdapter.Converter
title: Interface Internal.ListAdapter.Converter<F,T> (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:37.144057+00:00
---

# Interface Internal.ListAdapter.Converter<F,T> (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Internal.ListAdapter.Converter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Internal.ListAdapter.Converter<F,T> (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface Internal.ListAdapter.Converter<F,T>

Convert individual elements of the List from F to T.

## Type Parameters  
  
---  
**Name** | **Description**  
`F` |   
`T` |   
  
## Methods 

### convert(F from)
    
    
    public abstract T convert(F from)

**Parameter**  
---  
**Name** | **Description**  
`from` | `F`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
