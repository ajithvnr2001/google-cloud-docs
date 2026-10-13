---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo
title: Class ResourceBundleDeploymentInfo (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:16.775349+00:00
---

# Class ResourceBundleDeploymentInfo (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResourceBundleDeploymentInfo (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    ResourceBundleDeploymentInfo(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

ResourceBundleDeploymentInfo represents the status of a resource bundle deployment.

## Attributes  
  
---  
**Name** | **Description**  
`release` |  `str`   
Output only. Refers to a `ResourceBundle` release.   
`version` |  `str`   
Output only. Refers to a version of the `ResourceBundle` release.   
`variant` |  `str`   
Output only. Refers to a variant in a `ResourceBundle` release.   
`sync_state` |  `[google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo.SyncState](https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo.SyncState)`   
Output only. Synchronization state of the `ResourceBundle` deployment.   
`messages` |  `MutableSequence[str]`   
Output only. Unordered list. Messages contains information related to the `ResourceBundle` deployment. For example, in case of an error, indicate the reason for the error. In case of a pending deployment, reason for why the deployment of new release is pending.   
  
## Classes 

### SyncState
    
    
    SyncState(value)

Synchronization state of the resource bundle deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
