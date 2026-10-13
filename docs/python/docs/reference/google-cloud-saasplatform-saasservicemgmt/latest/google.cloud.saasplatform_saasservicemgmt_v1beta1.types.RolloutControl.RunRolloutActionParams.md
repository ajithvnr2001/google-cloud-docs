---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutControl.RunRolloutActionParams
title: Class RunRolloutActionParams (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:30.827235+00:00
---

# Class RunRolloutActionParams (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutControl.RunRolloutActionParams

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RunRolloutActionParams (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    RunRolloutActionParams(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Parameters for the RUN action controlling the behavior of the rollout when it is resumed from a PAUSED state.

## Attribute  
  
---  
**Name** | **Description**  
`retry_failed_operations` |  `bool`   
Required. If true, the rollout will retry failed operations when resumed. This is applicable only the current state of the Rollout is PAUSED and the requested action is RUN.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
