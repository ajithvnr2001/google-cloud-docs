---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.EncryptionInfo.KmsKeyState
title: Class KmsKeyState (0.5.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:53.014745+00:00
---

# Class KmsKeyState (0.5.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.EncryptionInfo.KmsKeyState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class KmsKeyState (0.5.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.5 (latest)  0.5.4  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    KmsKeyState(value)

The state of the KMS key perceived by the system. Refer to the public documentation for the impact of each state.

## Enums  
  
---  
**Name** | **Description**  
`KMS_KEY_STATE_UNSPECIFIED` | The default value. This value is unused.  
`ENABLED` | The KMS key is enabled and correctly configured.  
`PERMISSION_DENIED` | Permission denied on the KMS key.  
`DISABLED` | The KMS key is disabled.  
`DESTROYED` | The KMS key is destroyed.  
`DESTROY_SCHEDULED` | The KMS key is scheduled to be destroyed.  
`EKM_KEY_UNREACHABLE_DETECTED` | The EKM key is unreachable.  
`BILLING_DISABLED` | Billing is disabled for the project.  
`UNKNOWN_FAILURE` | All other unknown failures.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
