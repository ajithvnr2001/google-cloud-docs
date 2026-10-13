---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1beta.types.DeletionPropagationPolicy
title: Class DeletionPropagationPolicy (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:55.404333+00:00
---

# Class DeletionPropagationPolicy (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1beta.types.DeletionPropagationPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeletionPropagationPolicy (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    DeletionPropagationPolicy(value)

Deletion Propagation Policy determines what happens to the underlying Kubernetes resources on a cluster when the `FleetPackage` managing those resources no longer targets the cluster or is deleted.

## Enums  
  
---  
**Name** | **Description**  
`DELETION_PROPAGATION_POLICY_UNSPECIFIED` | Unspecified deletion propagation policy. Defaults to FOREGROUND.  
`FOREGROUND` | Foreground deletion propagation policy. Any resources synced to the cluster will be deleted.  
`ORPHAN` | Orphan deletion propagation policy. Any resources synced to the cluster will be abandoned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
