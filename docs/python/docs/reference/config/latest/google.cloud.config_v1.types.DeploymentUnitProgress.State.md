---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentUnitProgress.State
title: Class State (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:40.352161+00:00
---

# Class State (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentUnitProgress.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class State (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    State(value)

The possible steps a deployment unit provisioning may be running.

## Enums  
  
---  
**Name** | **Description**  
`STATE_UNSPECIFIED` | The default value. This value is unused.  
`QUEUED` | The deployment unit is queued for deployment creation or update.  
`APPLYING_DEPLOYMENT` | The underlying deployment of the unit is being created or updated.  
`SUCCEEDED` | The underlying deployment operation of the unit has succeeded.  
`FAILED` | The underlying deployment operation of the unit has failed.  
`ABORTED` | The deployment unit was aborted, likely due to failures in other dependent deployment units.  
`SKIPPED` | The deployment unit was skipped because there were no changes to apply.  
`DELETING_DEPLOYMENT` | The deployment is being deleted.  
`PREVIEWING_DEPLOYMENT` | The deployment is being previewed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
