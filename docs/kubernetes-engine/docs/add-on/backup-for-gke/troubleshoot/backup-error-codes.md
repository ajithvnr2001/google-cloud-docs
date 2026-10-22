---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes/
title: Overview of Backup for GKE error codes for failed backup operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:13.072322+00:00
---

# Overview of Backup for GKE error codes for failed backup operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Overview of Backup for GKE error codes for failed backup operations Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page provides a comprehensive overview of common Backup for GKE error codes that you might encounter during backup operations. It includes each error code number, error code message, and a link to specific troubleshooting instructions to help you resolve them. This page is intended for use when a backup operation fails and you receive an error code. Use the following table to identify the error code you received and its corresponding troubleshooting steps.

Error code number | Error code message | Link to troubleshooting instructions  
---|---|---  
  
### `100010100`

| `Failed to backup PVC - Default snapshot creation failure` | For instructions about how to resolve this issue, see [Failure to back up `PersistentVolumeClaim` due to default snapshot creation failure](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/common-errors#default-snapshot-failure).  
  
### `100010101`

| `Failed to backup PVC - Missing IAM binding for tenant project` | For instructions about how to resolve this issue, see [Failure to backup `PersistentVolumeClaim` due to missing Identity and Access Management binding for tenant project](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#missing-iam-binding-for-tenant-project).  
  
### `100010104`

| `Failed to backup PVC - Org policy constraint violation while creating snapshot` | For instructions about how to resolve this issue, see [Failure to back up `PersistentVolumeClaim` due to organization policy constraint violation during snapshot creation](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#org-policy-constraint-violation-during-snapshot-creation).  
  
### `100010105`

| `Failed to backup PVC - Disk referenced by PVC does not exist` | For instructions about how to resolve this issue, see [Failure to back up `PersistentVolumeClaim` due to nonexistent disk](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/storage-errors#non-existent-disk).  
  
### `100010106`

| `Failed to backup PVC - Missing IAM binding for Backup for GKE service agent` | For instructions about how to resolve this issue, see [Failure to back up `PersistentVolumeClaim` due to missing Identity and Access Management binding for Backup for GKE service agent](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#missing-iam-binding-for-service-agent).  
  
### `100010107`

| `Failed to backup PVC - Missing IAM binding - agent service account (KCP)` | For instructions about how to resolve this issue, see [Failure to back up `PersistentVolumeClaim` due to missing Identity and Access Management binding for agent service account (KCP)](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#missing-iam-binding-for-agent-service-account).  
  
### `100010108`

| `Failed to backup PVC - Missing Backup Plan CMEK for encrypted disk` | For instructions about how to resolve this issue, see [Failure to back up `PersistentVolumeClaim` due to missing Backup Plan CMEK for encrypted disk](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/system-errors#missing-backup-plan-cmek).  
  
### `100010109`

| `Failed to backup PVC - Target backup region not permitted by DiskSettings policy` | For instructions about how to resolve this issue, see [Failure to back up `PersistentVolumeClaim` due to target backup region not permitted by DiskSettings policy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#target-backup-region-not-permitted).  
  
### `100010202`

| `Snapshotting volume failed` | For instructions about how to resolve this issue, see [Error 100010202: Snapshotting volume failed](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/storage-errors#snapshot-error).  
  
### `100020101`

| `PersistentVolumeClaims are bound to PersistentVolumes of unsupported types and cannot be backed up.` | For instructions about how to resolve this issue, see [Error 100020101: Failure to back up `PersistentVolumeClaim` \- `PersistentVolumeClaim` bound to an supported `PersistentVolume` type](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#persistentvolumeclaims-bound-to-unsupported-persistentvolumes).  
  
### `100020102`

| `CustomResourceDefinition - has an invalid schema - Unsupported v1beta1 API version` | For instructions about how to resolve this issue, see [Error 100020102: Failure to backup CRD due to unsupported `v1beta1` API version](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/system-errors#unsupported-v1beta1-api-version).  
  
### `100020103`

| `Failed to query API resources` | For instructions about how to resolve this issue, see [Error 100020103: Failed to query API resources](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/system-errors#failed-to-query-api-resources).  
  
### `100020104`

| `Failed to backup PVC - PVC not bound to a PersistentVolume` | For instructions about how to resolve this issue, see [Error 100020104: Failure to back up `PersistentVolumeClaim` \- `PersistentVolumeClaim` not bound to a `PersistentVolume`](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors#strict-permissive-mode-pvc-not-bound-to-pv).  
  
### `100040102`

| `Namespace not found` | For instructions about how to resolve this issue, see [Error 100040102: Namespace not found](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/system-errors#namespace-not-found).  
  
Back to top

## What's next

  * [Read the Backup for GKE error codes overview page for failed restore operations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-error-codes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
