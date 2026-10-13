---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec.ParsingMode
title: Class ParsingMode (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:10.367650+00:00
---

# Class ParsingMode (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec.ParsingMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ParsingMode (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    ParsingMode(value)

Specifies the parsing mode for API specifications during creation and update.

  * `RELAXED`: Parsing errors in the specification content do not fail the API call.
  * `STRICT`: Parsing errors in the specification content result in failure of the API call. If not specified, defaults to `RELAXED`.



## Enums  
  
---  
**Name** | **Description**  
`PARSING_MODE_UNSPECIFIED` | Defaults to `RELAXED`.  
`RELAXED` | Parsing of the Spec on create and update is relaxed, meaning that parsing errors the spec contents will not fail the API call.  
`STRICT` | Parsing of the Spec on create and update is strict, meaning that parsing errors in the spec contents will fail the API call.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
