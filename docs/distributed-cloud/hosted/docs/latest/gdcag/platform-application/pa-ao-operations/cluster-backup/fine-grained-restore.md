---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/fine-grained-restore/
title: Create a fine-grained restore \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:15.629878+00:00
---

# Create a fine-grained restore  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/fine-grained-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a fine-grained restore Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a fine-grained restore for a backup in Google Distributed Cloud (GDC) air-gapped.

The fine-grained restore feature lets you restore a subset of resources from a backup. This feature provides the flexibility to refine the restore scope defined in the restore plan.

## Before you begin

Ensure you have an existing backup. For more information, see [Plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups).

### Request IAM roles

To create a fine-grained restore for a backup, ask your Organization IAM Admin or Project IAM Admin to grant you one of the following roles:

  * **User Cluster Backup Admin** (`user-cluster-backup-admin`): creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup and restore plans in user clusters. Contact your Organization IAM Admin to request this role.

  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests. Contact your Project IAM Admin to request this role.




## Create a fine-grained restore

To create a restore with a fine-grained filter, follow these steps:

  1. Create the fine-grained restore filters. You can use the following YAML example.
         
         inclusionFilters:
           - groupKind:
               group: foo.io
               kind: Bar
             name: name1
             namespace: ns1
         exclusionFilters:
           - labels:
               key1: value1
               key2: value2
         

  2. Create a `ManualRestoreRequest` custom resource to plan restores from an existing `Backups`. Here's an example of a `ManualRestoreRequest`:
         
         apiVersion: backup.gdc.goog/v1
         kind: ManualRestoreRequest
         metadata:
           name: RESTORE_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           restoreName: RESTORE_NAME
           restorePlanName: RESTORE_PLAN
           backupName: BACKUP_NAME
           filter:
             FINE_GRAINED_RESTORE_FILTERS
         




Replace the following:

  * `RESTORE_NAME`: the name of the restore that you want to create.
  * `PROJECT_NAMESPACE`: the name of your GDC project.
  * `RESTORE_PLAN`: the name of the restore plan this restore is derived from.
  * `BACKUP_NAME`: the backup to restore. This backup must be associated with the backup plan to which the restore plan refers to. For more information, see [Plan a set of restores](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-restores#create-restore-plan).
  * `FINE_GRAINED_RESTORE_FILTER`: the fine-grained restore filters. For examples, see Fine-grained restore filter examples.



## Fine-grained restore filter examples

The following examples are provided in the YAML format used by Google Cloud CLI.

### Restore a single namespace scoped resource

This example restores a `ConfigMap` resource with the name `nginx-vars` in the namespace `webserver`, using the fine-grained restore `inclusionFilters` to select the resource. If you want to choose resources under the core group, use an empty string for the `group` field.
    
    
    filter:
      inclusionFilters:
      - groupKind:
          kind: ConfigMap
        name: nginx-vars
        namespace: webserver
    

### Exclude a single cluster scoped resource

This example restores all available resources except for one `groupKind` resource with the name `sc1`, using the fine-grained restore `exclusionFilters` to exclude the resource.
    
    
    filter:
      exclusionFilters:
      - groupKind:
          group: storage.k8s.io
          kind: StorageClass
        name: sc1
    
    

### Restore resources with two labels

This example restores resources which have both labels `key1:value1` and `key2:value2`, using the fine-grained restore `inclusionFilters` to select the resources.
    
    
    filter:
      inclusionFilters:
      - labels:
          key1: value1
          key2: value2
    

### Exclude all resources of some GroupKinds

This example restores all available resources except for the `groupKind` resources of `ConfigMap` and `storage.k8s.io/StorageClass`, using the fine-grained restore `exclusionFilters` to exclude these two GroupKinds.
    
    
    filter:
      exclusionFilters:
      - groupKind:
          kind: ConfigMap
      - groupKind:
          group: storage.k8s.io
          kind: StorageClass
    

## What's next

  * [View and delete a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/view-and-delete-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
