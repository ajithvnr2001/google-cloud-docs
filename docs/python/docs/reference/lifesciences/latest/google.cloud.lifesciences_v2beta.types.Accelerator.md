---
url: https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.Accelerator
title: Class Accelerator (0.12.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:53.091659+00:00
---

# Class Accelerator (0.12.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/lifesciences/latest/google.cloud.lifesciences_v2beta.types.Accelerator

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Accelerator (0.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.2 (latest)  0.12.1  0.11.0  0.10.0  0.9.18  0.8.0  0.7.2  0.6.2  0.5.2  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    Accelerator(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Carries information about an accelerator that can be attached to a VM.

## Attributes  
  
---  
**Name** | **Description**  
`type_` |  `str`   
The accelerator type string (for example, "nvidia-tesla-t4"). Only NVIDIA GPU accelerators are currently supported. If an NVIDIA GPU is attached, the required runtime libraries will be made available to all containers under `/usr/local/nvidia`. The driver version to install must be specified using the NVIDIA driver version parameter on the virtual machine specification. Note that attaching a GPU increases the worker VM startup time by a few minutes.   
`count` |  `int`   
How many accelerators of this type to attach.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
