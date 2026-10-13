---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-capacityplanner/latest/google.cloud.capacityplanner_v1beta.types.MachineShape
title: Class MachineShape (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:21.135194+00:00
---

# Class MachineShape (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-capacityplanner/latest/google.cloud.capacityplanner_v1beta.types.MachineShape

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MachineShape (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    MachineShape(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Machine shape details Next : 13

## Attributes  
  
---  
**Name** | **Description**  
`machine_family` |  `str`   
Optional. The VM family.   
`machine_type` |  `str`   
Optional. The characteristics of the sampled VM expressed as a string.   
`machine_shape` |  `str`   
Optional. The customer visible string representing the type of VM.   
`cpu_cores` |  `float`   
Optional. Number of CPU cores per VM.   
`gpu_type` |  `str`   
Optional. The type of GPU with the VM.   
`gpu_compute_type` |  `str`   
Optional. The GPU name recognized by Compute Engine APIs.   
`gpu_cores` |  `int`   
Optional. The number of GPU cores per VM.   
`local_ssd_partitions` |  `int`   
Optional. The number of local SSD partitions per VM.   
`local_ssd_gb` |  `float`   
Optional. Total amount of local SSD storage.   
`memory_gb` |  `float`   
Optional. Total amount of memory with the VM.   
`local_ssd_interface` |  `str`   
Optional. The local SSD interface used such as nvme or scsi   
`min_cpu_platform` |  `str`   
Optional. The Min-cpu platform used such as icelake   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
