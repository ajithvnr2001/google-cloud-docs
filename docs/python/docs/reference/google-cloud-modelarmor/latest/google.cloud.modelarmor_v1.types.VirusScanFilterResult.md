---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusScanFilterResult
title: Class VirusScanFilterResult (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:05.602471+00:00
---

# Class VirusScanFilterResult (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusScanFilterResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class VirusScanFilterResult (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    VirusScanFilterResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Virus scan results.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`execution_state` |  `[google.cloud.modelarmor_v1.types.FilterExecutionState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterExecutionState)`   
Output only. Reports whether Virus Scan was successfully executed or not.   
`message_items` |  `MutableSequence[[google.cloud.modelarmor_v1.types.MessageItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MessageItem)]`   
Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution status is skipped then this field provides related reason/explanation.   
`match_state` |  `[google.cloud.modelarmor_v1.types.FilterMatchState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterMatchState)`   
Output only. Match status for Virus. Value is MATCH_FOUND if the data is infected with a virus.   
`scanned_content_type` |  `[google.cloud.modelarmor_v1.types.VirusScanFilterResult.ScannedContentType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusScanFilterResult.ScannedContentType)`   
Type of content scanned.   
`scanned_size` |  `int`   
Size of scanned content in bytes. This field is a member of `oneof`_ `_scanned_size`.   
`virus_details` |  `MutableSequence[[google.cloud.modelarmor_v1.types.VirusDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusDetail)]`   
List of Viruses identified. This field will be empty if no virus was detected.   
  
## Classes 

### ScannedContentType
    
    
    ScannedContentType(value)

Type of content scanned.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
