---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.PatchJobInstanceDetails
title: Class PatchJobInstanceDetails (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:26.475591+00:00
---

# Class PatchJobInstanceDetails (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.PatchJobInstanceDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PatchJobInstanceDetails (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    PatchJobInstanceDetails(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Patch details for a VM instance. For more information about reviewing VM instance details, see `Listing all VM instance details for a specific patch job <https://cloud.google.com/compute/docs/os-patch-management/manage-patch-jobs#list-instance-details>`__.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The instance name in the form `projects/*/zones/*/instances/*`  
`instance_system_id` |  `str`   
The unique identifier for the instance. This identifier is defined by the server.   
`state` |  `[google.cloud.osconfig_v1.types.Instance.PatchState](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Instance.PatchState)`   
Current state of instance patch.   
`failure_reason` |  `str`   
If the patch fails, this field provides the reason.   
`attempt_count` |  `int`   
The number of times the agent that the agent attempts to apply the patch.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
