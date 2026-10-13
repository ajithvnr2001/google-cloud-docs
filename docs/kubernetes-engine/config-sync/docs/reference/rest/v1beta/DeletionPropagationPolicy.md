---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1beta/DeletionPropagationPolicy/
title: DeletionPropagationPolicy \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:55.944211+00:00
---

# DeletionPropagationPolicy  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1beta/DeletionPropagationPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)



Send feedback 

#  DeletionPropagationPolicy Stay organized with collections  Save and categorize content based on your preferences. 

Deletion Propagation Policy determines what happens to the underlying Kubernetes resources on a cluster when the `FleetPackage` managing those resources no longer targets the cluster or is deleted.

Enums  
---  
`DELETION_PROPAGATION_POLICY_UNSPECIFIED` | Unspecified deletion propagation policy. Defaults to FOREGROUND.  
`FOREGROUND` | Foreground deletion propagation policy. Any resources synced to the cluster will be deleted.  
`ORPHAN` | Orphan deletion propagation policy. Any resources synced to the cluster will be abandoned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-28 UTC."],[],[]] 
