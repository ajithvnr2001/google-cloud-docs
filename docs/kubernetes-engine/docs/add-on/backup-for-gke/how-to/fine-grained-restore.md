---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore/
title: Enable fine-grained restore \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:13.177860+00:00
---

# Enable fine-grained restore  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Enable fine-grained restore Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to select resources for restoration with finer granularity.

## Overview

The fine-grained restore feature lets you restore a subset of resources from a backup. The fine-grained restore feature provides the flexibility to refine the restore scope defined in the parent restore plan. If the fine-grained restore scope has no overlap with the original scope defined in the parent restore plan, no resources will be restored.

The fine-grained restore feature can be enabled for restore plans with individual resource level conflict handling modes:

  * Merge skip
  * Merge replace
  * Merge replace volume



If your restore plans are using namespace or ProtectedApplication level conflict handling modes, such as **Fail on conflict** or **Rollback** and you want to enable fine-grained restore, then you need to update your restore plan to use supported modes or create a new restore plan. For more information about the restore modes, see [Handle resource conflicts during restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/resource-conflict).

To use fine-grained restore, you can define one or more filter conditions under inclusion and exclusion filters. You can select a specific subset of resources from the backup for restoration or restore all resources except for a subset. You may define inclusion and exclusion filters simultaneously. If inclusion filters are used, only resources matching those filters are restored. If exclusion filters are used, it excludes matching resources from the restore process. When both inclusion and exclusion filters are specified, inclusion filters are applied first, followed by exclusion filters. This means that exclusion filters have priority over inclusion filters. If no filters are specified, the restore is performed on the entire scope defined in the parent restore plan.

There are four optional attributes when constructing a filter condition:

  * GroupKind: the Kubernetes API group and kind for the resource
  * Namespace: the namespace for namespace scoped resources
  * Resource name: the name of the resource
  * Labels: the key-value pairs to select resource based on Kubernetes [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)



You can use a combination of the preceding four attributes to define a filter condition. If more than one attribute is specified, the relationships between attributes are considered as `AND`. A resource is selected if it matches all attributes defined in the filter condition. You can also provide multiple filter conditions at the same time, the relationships between different filter conditions are `OR`. A resource is selected if it matches any filter condition of all provided ones.

## Before you begin

[Plan a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).

## Create a restore with fine-grained restore filter

### gcloud

  1. Create a YAML or JSON file with fine-grained restore filters. You can use the following YAML example.
         
         exclusionFilters:
         - groupKind:
             resourceGroup: foo.io
             resourceKind: Bar
           name: name1
           namespace: ns1
         inclusionFilters:
         - labels:
             key1: value1
             key2: value2
         

  2. Create a restore using the fine-grained restore filter file you created.
         
         gcloud beta container backup-restore restores create RESTORE \
             --project=PROJECT_ID \
             --location=LOCATION \
             --restore-plan=RESTORE_PLAN \
             --backup=BACKUP \
             --filter-file=FILTER_FILE
         

Replace the following:

     * `RESTORE`: the name of the restore that you want to create.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the parent restore plan.
     * `RESTORE_PLAN`: the name of the parent restore plan this restore is derived from.
     * `BACKUP`: the backup to restore. This must be located in the backup plan to which the parent restore plan refers as `projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUP_PLAN/backups/BACKUP`

     * `FILTER_FILE`: the path of your fine-grained restore filters.

For the full list of options, refer to the [`gcloud beta container backup-restore restores create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restores/create) documentation.




### Console

Use the following instructions to create a fine-grained restore in the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. In the list of backups, select the backup that you want to restore and click **Set up a restore**.

  5. Choose a restore plan from the list of plans that apply to this backup.

  6. Enter a **Name** and optional **Description** for the restore.

  7. Click the **Enable fine-grained restore** checkbox.

  8. In the **Inclusion filters** or **Exclusion filters** section, click **Add filter condition**.

  9. In the **Restore filter condition** , define the condition and click **Save changes**.

  10. If you want to add more conditions, click **Add filter conditions** again.

  11. Click **Restore**.




## Fine-grained restore filter file examples

The following examples are provided in the YAML format used by Google Cloud CLI or the step-by-step instructions for Google Cloud console.

### Restore a single namespace scoped resource

This example restores a resource kind `ConfigMap` with name `nginx-vars` in the namespace `webserver`, using the fine-grained restore `InclusionFilters` to select the resource. If you want to choose resources under `core` group, use empty string for `resourceGroup`.

### gcloud
    
    
      inclusionFilters:
      - groupKind:
          resourceKind: ConfigMap
        name: nginx-vars
        namespace: webserver
    

### Console

  1. Enable fine-grained restore as you did in the Create a restore with fine-grained restore filter procedure.
  2. In the **Inclusion filters** section, click **Add filter condition**.
  3. In the **Resource name** field, enter `nginx-vars`.
  4. In the **Namespace** field, enter `webserver`.
  5. In the **Object kind** field, enter `ConfigMap`.
  6. Click **Save changes**.



### Exclude a single cluster scoped resource

This example restores all available resources except for one resource GroupKind `storage.k8s.io/StorageClass` with name `sc1`, using the fine-grained restore `ExclusionFilters` to exclude the resource.

### gcloud
    
    
    exclusionFilters:
    - groupKind:
        resourceGroup: storage.k8s.io
        resourceKind: StorageClass
      name: sc1
    

### Console

  1. Enable fine-grained restore as you did in the Create a restore with fine-grained restore filter procedure.
  2. In the **Exclusion filters** section, click **Add filter condition**.
  3. In the **Resource name** field, enter `sc1`.
  4. In the **API group** field, enter `storage.k8s.io`.
  5. In the **Object kind** field, enter `StorageClass`.
  6. Click **Save changes**.



### Restore resources with two labels

This example restores resources which have both labels `key1:value1` and `key2:value2`, using the fine-grained restore `InclusionFilters` to select the resources.

### gcloud
    
    
    inclusionFilters:
    - labels:
        key1: value1
        key2: value2
    

### Console

  1. Enable fine-grained restore as you did in the Create a restore with fine-grained restore filter procedure.
  2. In the **Inclusion filters** section, click **Add filter condition**.
  3. In the **Labels** Section:

     1. Click **Add label**
     2. In the **Key 1** field, enter `key1`.
     3. In the **Value 1** field, enter `value1`.
     4. Click **Add label**.
     5. In the **Key 2** field, enter `key2`.
     6. In the **Value 2** field, enter `value2`.
  4. Click **Save changes**.




### Exclude all resources of some GroupKinds

This example restores all available resources except for GroupKind `ConfigMap` and `storage.k8s.io/StorageClass`, using the fine-grained restore `ExclusionFilters` to exclude these two GroupKinds.

### gcloud
    
    
    exclusionFilters:
    - groupKind:
        resourceKind: ConfigMap
    - groupKind:
        resourceGroup: storage.k8s.io
        resourceKind: StorageClass
    

### Console

  1. Enable fine-grained restore as you did in the Create a restore with fine-grained restore filter procedure.
  2. In the **Exclusion filters** section, click **Add filter condition**. 
     1. In the **Object kind** field, enter `ConfigMap`.
     2. Click **Save changes**.
  3. In the **Exclusion filters** section, click **Add filter condition**. 
     1. In the **API group** field, enter `storage.k8s.io`.
     2. In the **Object kind** field, enter `StorageClass`.
     3. Click **Save changes**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
