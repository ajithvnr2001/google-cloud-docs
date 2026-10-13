---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.CreateOSPolicyAssignmentRequest
title: Class CreateOSPolicyAssignmentRequest (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:20.124091+00:00
---

# Class CreateOSPolicyAssignmentRequest (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.CreateOSPolicyAssignmentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateOSPolicyAssignmentRequest (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    CreateOSPolicyAssignmentRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

A request message to create an OS policy assignment

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource name in the form: projects/{project}/locations/{location}   
`os_policy_assignment` |  `[google.cloud.osconfig_v1.types.OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment)`   
Required. The OS policy assignment to be created.   
`os_policy_assignment_id` |  `str`   
Required. The logical name of the OS policy assignment in the project with the following restrictions: \- Must contain only lowercase letters, numbers, and hyphens. \- Must start with a letter. \- Must be between 1-63 characters. \- Must end with a number or a letter. \- Must be unique within the project.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
