---
url: https://docs.cloud.google.com/python/docs/reference/workstations/latest/google.cloud.workstations_v1.types.UpdateWorkstationConfigRequest
title: Class UpdateWorkstationConfigRequest (0.8.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:22.719708+00:00
---

# Class UpdateWorkstationConfigRequest (0.8.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/workstations/latest/google.cloud.workstations_v1.types.UpdateWorkstationConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdateWorkstationConfigRequest (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.13  0.4.1  0.3.0  0.2.1  0.1.1 
    
    
    UpdateWorkstationConfigRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for UpdateWorkstationConfig.

## Attributes  
  
---  
**Name** | **Description**  
`workstation_config` |  `[google.cloud.workstations_v1.types.WorkstationConfig](https://docs.cloud.google.com/python/docs/reference/workstations/latest/google.cloud.workstations_v1.types.WorkstationConfig)`   
Required. Workstation configuration to update.   
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Mask specifying which fields in the workstation configuration should be updated.   
`validate_only` |  `bool`   
Optional. If set, validate the request and preview the result, but do not actually apply it.   
`allow_missing` |  `bool`   
Optional. If set and the workstation configuration is not found, a new workstation configuration will be created. In this situation, update_mask is ignored.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
