---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/State/
title: State \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:36.238330+00:00
---

# State  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/State/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  State Stay organized with collections  Save and categorize content based on your preferences. 

The current state of the deployment.

Enums  
---  
`STATE_UNSPECIFIED` | State not set (this is not a valid state).  
`ACTIVE` | The deployment is ready and in sync with the parent group.  
`CREATING` | The deployment is being created.  
`DELETING` | The deployment is being deleted.  
`OUT_OF_SYNC` | The deployment is out of sync with the parent group. In most cases, this is a result of a transient issue within the system (e.g. a delayed data-path config) and the system is expected to recover automatically. See the parent deployment group's state for more details.  
`DELETE_FAILED` | An attempt to delete the deployment has failed. This is a terminal state and the deployment is not expected to recover. The only permitted operation is to retry deleting the deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
