---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareGroupRequest
title: Class CreateHardwareGroupRequest (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:43.093668+00:00
---

# Class CreateHardwareGroupRequest (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareGroupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateHardwareGroupRequest (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    CreateHardwareGroupRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A request to create a hardware group.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The order to create the hardware group in. Format: `projects/{project}/locations/{location}/orders/{order}`  
`hardware_group_id` |  `str`   
Optional. ID used to uniquely identify the HardwareGroup within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The hardware_group.name field in the request will be ignored.   
`hardware_group` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup)`   
Required. The hardware group to create.   
`request_id` |  `str`   
Optional. An optional unique identifier for this request. See `AIP-155 `__.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
