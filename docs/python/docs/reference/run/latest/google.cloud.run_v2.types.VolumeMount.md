---
url: https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.types.VolumeMount
title: Class VolumeMount (0.16.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:33.564773+00:00
---

# Class VolumeMount (0.16.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.types.VolumeMount

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class VolumeMount (0.16.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.2 (latest)  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.19  0.9.1  0.8.1  0.7.1  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    VolumeMount(mapping=None, *, ignore_unknown_fields=False, **kwargs)

VolumeMount describes a mounting of a Volume within a container.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. This must match the Name of a Volume.   
`mount_path` |  `str`   
Required. Path within the container at which the volume should be mounted. Must not contain ':'. For Cloud SQL volumes, it can be left empty, or must otherwise be `/cloudsql`. All instances defined in the Volume will be available as `/cloudsql/[instance]`. For more information on Cloud SQL volumes, visit https://cloud.google.com/sql/docs/mysql/connect-run   
`sub_path` |  `str`   
Optional. Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
