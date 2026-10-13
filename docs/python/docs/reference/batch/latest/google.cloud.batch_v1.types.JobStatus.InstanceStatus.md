---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.InstanceStatus
title: Class InstanceStatus (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:27.347856+00:00
---

# Class InstanceStatus (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.InstanceStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InstanceStatus (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 
    
    
    InstanceStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

VM instance status.

## Attributes  
  
---  
**Name** | **Description**  
`machine_type` |  `str`   
The Compute Engine machine type.   
`provisioning_model` |  `[google.cloud.batch_v1.types.AllocationPolicy.ProvisioningModel](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.ProvisioningModel)`   
The VM instance provisioning model.   
`task_pack` |  `int`   
The max number of tasks can be assigned to this instance type.   
`boot_disk` |  `[google.cloud.batch_v1.types.AllocationPolicy.Disk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.Disk)`   
The VM boot disk.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
