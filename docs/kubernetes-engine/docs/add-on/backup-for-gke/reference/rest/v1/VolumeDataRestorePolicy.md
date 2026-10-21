---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy/
title: VolumeDataRestorePolicy \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:22:53.925760+00:00
---

# VolumeDataRestorePolicy  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  VolumeDataRestorePolicy Stay organized with collections  Save and categorize content based on your preferences. 

Defines how volume data should be restored.

Enums  
---  
`VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED` | Unspecified (illegal).  
`RESTORE_VOLUME_DATA_FROM_BACKUP` | For each PVC to be restored, create a new underlying volume and PV from the corresponding VolumeBackup contained within the Backup.  
`REUSE_VOLUME_HANDLE_FROM_BACKUP` | For each PVC to be restored, attempt to reuse the original PV contained in the Backup (with its original underlying volume). This option is likely only usable when restoring a workload to its original cluster.  
`NO_VOLUME_DATA_RESTORATION` | For each PVC to be restored, create PVC without any particular action to restore data. In this case, the normal Kubernetes provisioning logic would kick in, and this would likely result in either dynamically provisioning blank PVs or binding to statically provisioned PVs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
