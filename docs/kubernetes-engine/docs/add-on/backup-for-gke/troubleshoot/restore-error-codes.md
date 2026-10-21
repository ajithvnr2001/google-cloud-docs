---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-error-codes/
title: Overview of Backup for GKE error codes for failed restore operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:43.225694+00:00
---

# Overview of Backup for GKE error codes for failed restore operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-error-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Overview of Backup for GKE error codes for failed restore operations Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page provides a comprehensive overview of common Backup for GKE error codes that you might encounter during restore operations. It includes each error code number, error code message, and a link to specific troubleshooting instructions to help you resolve them. This page is intended for use when a restore operation fails and you receive an error code. Use the following table to identify the error code you received and its corresponding troubleshooting steps.

Error code number | Error code message | Link to troubleshooting instructions  
---|---|---  
  
### `200010301`

| `Failed calling webhook` | For instructions about how to resolve this issue, see [Failure to complete restore operation due to unavailable admission webhook service](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors#webhook-call-failed-internal-error).  
  
### `200010302`

| `Admission webhook denied the request` | For instructions about how to resolve this issue, see [Failure to complete restore operation due to denied resource creation request](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors#denied-resource-creation-request).  
  
### `200060202`

| `Workload validation error` | For instructions about how to resolve this issue, see [Failure to complete restore operation due to missing GKE resource during workload validation](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors#restore-error-due-to-missing-gke-resource-during-workload-validation).  
  
### `200060201`

| `Workload validation timed out` | For instructions about how to resolve this issue, see [Failure to complete restore operation due to workload validation timeout](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors#failure-to-complete-restore-operation-due-to-workload-validation-timeout).  
  
### `200060102`

| `Volume validation error` | For instructions about how to resolve this issue, see [Failure to complete restore operation due to volume validation error](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors#volume-validation-error).  
  
### `200060101`

| `Volume validation timeout` | For instructions about how to resolve this issue, see [Failure to complete restore operation due to volume validation timeout](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors#volume-validation-timeout).  
  
Back to top

## What's next

  * [Read the Backup for GKE error codes overview page for failed backup operations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
