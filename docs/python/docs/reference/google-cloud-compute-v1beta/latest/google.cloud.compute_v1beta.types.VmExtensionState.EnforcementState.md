---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.VmExtensionState.EnforcementState
title: Class EnforcementState (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:26.827024+00:00
---

# Class EnforcementState (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.VmExtensionState.EnforcementState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EnforcementState (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    EnforcementState(value)

The enforcement state of the extension. If the extension is not enforced yet, then the health status will not be specified.

## Enums  
  
---  
**Name** | **Description**  
`UNDEFINED_ENFORCEMENT_STATE` | A value indicating that the enum field is not set.  
`APPLYING_CONFIG` | A new configuration is being applied to the extension. Depending on each extensions' behavior, an extension restart might be involved in this process to get new configuration applied properly.  
`ENFORCEMENT_STATE_UNSPECIFIED` | Enforcement state of the extension is unspecified.  
`INCOMPATIBLE` | None of the extension revisions of the given extension version is compatible with the VM's architecture and Operating System.  
`INSTALLED` | The extension has been successfully installed.  
`INSTALLING` | The extension is being installed.  
`INSTALL_FAILED` | The installation of the extension failed, and there's no recorded stable extension revision to rollback to.  
`REMOVING` | The extension is being removed from the resource.  
`ROLLBACK_FAILED` | The rollback of the extension failed.  
`ROLLED_BACK` | The extension has been successfully rolled back. This value describes the rollback state of the extension, not the health status. It's possible that the extension is rolled back to the last stable revision but still keeps crashing, e.g. there's a change to the VM and no extension revisions can run normally.  
`ROLLING_BACK` | The extension is being rolled back to the last stable revision the system recorded.  
`SERVICE_DISABLED` | The service requiring this extension is disabled.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
