---
url: https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.types.EmptyDirVolumeSource
title: Class EmptyDirVolumeSource (0.16.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:11.428905+00:00
---

# Class EmptyDirVolumeSource (0.16.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.types.EmptyDirVolumeSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EmptyDirVolumeSource (0.16.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.2 (latest)  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.19  0.9.1  0.8.1  0.7.1  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    EmptyDirVolumeSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

In memory (tmpfs) ephemeral storage. It is ephemeral in the sense that when the sandbox is taken down, the data is destroyed with it (it does not persist across sandbox runs).

## Attributes  
  
---  
**Name** | **Description**  
`medium` |  `[google.cloud.run_v2.types.EmptyDirVolumeSource.Medium](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.types.EmptyDirVolumeSource.Medium)`   
The medium on which the data is stored. Acceptable values today is only MEMORY or none. When none, the default will currently be backed by memory but could change over time. +optional   
`size_limit` |  `str`   
Limit on the storage usable by this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers. The default is nil which means that the limit is undefined. More info: https://cloud.google.com/run/docs/configuring/in-memory-volumes#configure-volume. Info in Kubernetes: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir   
  
## Classes 

### Medium
    
    
    Medium(value)

The different types of medium supported for EmptyDir.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
