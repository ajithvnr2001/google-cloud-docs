---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceControl
title: Class MaintenanceControl (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:25.789726+00:00
---

# Class MaintenanceControl (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceControl

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MaintenanceControl (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    MaintenanceControl(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The control of the maintenance.

## Attributes  
  
---  
**Name** | **Description**  
`control` |  `[google.cloud.maintenance_api_v1beta.types.MaintenanceControl.Control](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceControl.Control)`   
The control of the resource maintenance.   
`is_custom` |  `bool`   
Indicates whether the control is available only in Service Producer API (not through Unified Maintenance).   
`documentation` |  `str`   
Link to Service Producer documentation about maintenance control. Provided only when `isCustom` is `true`.   
  
## Classes 

### Control
    
    
    Control(value)

Sets the type of control supported. comment (as in logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
