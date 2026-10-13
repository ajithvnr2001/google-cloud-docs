---
url: https://docs.cloud.google.com/python/docs/reference/gkemulticloud/latest/google.cloud.gke_multicloud_v1.types.AttachedCluster.State
title: Class State (0.9.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:32.222617+00:00
---

# Class State (0.9.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/gkemulticloud/latest/google.cloud.gke_multicloud_v1.types.AttachedCluster.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class State (0.9.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.2 (latest)  0.9.1  0.8.0  0.7.0  0.6.22  0.5.1  0.4.0  0.3.0  0.2.2  0.1.1 
    
    
    State(value)

The lifecycle state of the cluster.

## Enums  
  
---  
**Name** | **Description**  
`STATE_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the cluster is being registered.  
`RUNNING` | The RUNNING state indicates the cluster has been register and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that some work is actively being done on the cluster, such as upgrading software components.  
`STOPPING` | The STOPPING state indicates the cluster is being de-registered.  
`ERROR` | The ERROR state indicates the cluster is in a broken unrecoverable state.  
`DEGRADED` | The DEGRADED state indicates the cluster requires user action to restore full functionality.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
