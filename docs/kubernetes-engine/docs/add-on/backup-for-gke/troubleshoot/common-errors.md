---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/common-errors/
title: Troubleshoot common errors in Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:42.925997+00:00
---

# Troubleshoot common errors in Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/common-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Troubleshoot common errors in Backup for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes common errors you might experience when you use Backup for GKE, things to consider when you backup resources, and steps for troubleshooting the issue.

## Error 100010100: Failed to backup PersistentVolumeClaim - Default snapshot creation failure

Error `100010100` is a default error code for snapshot creation failure. When this error occurs, review the detailed error message to identify the specific cause.

Depending on the error message, refer to the following specific error guides:

  * If the error indicates a missing Backup Plan CMEK for an encrypted disk, see [Error 100010108: Failed to backup PersistentVolumeClaim - Missing Backup Plan CMEK for encrypted disk](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/system-errors#missing-backup-plan-cmek).
  * If the error indicates that the target backup region isn't permitted by your policy, see [Error 100010109: Failed to backup PersistentVolumeClaim - Target backup region not permitted by DiskSettings policy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#target-backup-region-not-permitted).
  * If the error indicates missing IAM bindings for the service agent, see [Error 100010106: Failed to backup PVC - Missing IAM binding for Backup for GKE service agent](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#missing-iam-binding-for-service-agent).



### Other Scenarios

There can be other error scenarios not covered by the specific codes mentioned here. If your error message does not match any of these cases, or if you are unable to resolve the issue, please contact Cloud Customer Care for assistance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
