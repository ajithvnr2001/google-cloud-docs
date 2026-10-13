---
url: https://docs.cloud.google.com/python/docs/reference/eventarc/latest/google.cloud.eventarc_v1.types.UpdateTriggerRequest
title: Class UpdateTriggerRequest (1.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:47.578277+00:00
---

# Class UpdateTriggerRequest (1.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/eventarc/latest/google.cloud.eventarc_v1.types.UpdateTriggerRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdateTriggerRequest (1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.3  1.14.0  1.13.2  1.12.0  1.11.5  1.10.0  1.9.2  1.8.1  1.7.0  1.6.3  1.5.1  1.4.2  1.3.0  1.2.1  1.1.0  1.0.2  0.2.4  0.1.0 
    
    
    UpdateTriggerRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request message for the UpdateTrigger method.

## Attributes  
  
---  
**Name** | **Description**  
`trigger` |  `[google.cloud.eventarc_v1.types.Trigger](https://docs.cloud.google.com/python/docs/reference/eventarc/latest/google.cloud.eventarc_v1.types.Trigger)`   
The trigger to be updated.   
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The fields to be updated; only fields explicitly provided are updated. If no field mask is provided, all provided fields in the request are updated. To update all fields, provide a field mask of "\\*".   
`allow_missing` |  `bool`   
If set to true, and the trigger is not found, a new trigger will be created. In this situation, `update_mask` is ignored.   
`validate_only` |  `bool`   
Optional. If set, validate the request and preview the review, but do not post it.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
