---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore/
title: Restore a backup \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:37.285685+00:00
---

# Restore a backup  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Restore a backup Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to restore a backup into a cluster in Google Kubernetes Engine (GKE) using the Backup for GKE service.

This page is for Backup and disaster recovery (DR) administrators who manage and perform backup and recoveries across the organization. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Introduction

After a backup is created, administrators can create a restore for that backup, which initiates the restoration of some portion of the contents of that backup into a target cluster (which might be different from the cluster from which the backup was originally created).

When a backup is restored, the Kubernetes resources are re-created in the target cluster. After the resources are created, actual restoration of workload capability is subject to the regular cluster reconciliation process (for example, Pods are scheduled to Nodes and then started on those Nodes).

## Before you begin

[Plan a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).

## Required roles

To get the permissions that you need to create and manage a restore, ask your administrator to grant you the Backup for GKE Restore Admin (`roles/gkebackup.restoreAdmin`), which is a subset of Backup for GKE Admin (`roles/gkebackup.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a restore

You can restore a backup by using the Google Cloud CLI or the Google Cloud console.

### gcloud

To restore a backup, run the following command:
    
    
    gcloud beta container backup-restore restores create RESTORE \
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN \
        --backup=BACKUP
    

Replace the following:

  * `RESTORE`: the name of the restore that you want to create.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the parent restore plan.
  * `RESTORE_PLAN`: the name of the parent restore plan this restore is derived from.
  * `BACKUP`: the backup to restore (must be located in the backup plan to which the parent restore plan refers):

    * `projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUP_PLAN/backups/BACKUP`



For the full list of options, refer to the [`gcloud beta container backup-restore restores create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restores/create) documentation.

The restore operation completes after all Kubernetes resources are successfully restored from the backup. You must validate that all the applications are running after the restore.

### Console

Use the following instructions to create a restore in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. In the list of backups, find the backup that you want to restore and click **Set up a restore**.

  5. Choose a restore plan from the list of plans that apply to this backup.

  6. Enter a name and optional description for the restore.

  7. Click **Restore**.




The restore operation completes after all Kubernetes resources are successfully restored from the backup. You must validate that all the applications are running after the restore.

## View a restore

View a restore and its details by using the gcloud CLI or the Google Cloud console.

### gcloud

To list the restores for a restore plan, run the following command:
    
    
    gcloud beta container backup-restore restores list \
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN
    

For **`list`** commands only, you can provide `-` as the value for any parameters except `PROJECT_ID`. The `-` value acts as a wildcard. The `-` value is the default for any parameter if you don't specify a command-line option or set a property.

For the full list of options, refer to the [`gcloud beta container backup-restore restores list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restores/list) documentation.

To see the details of a restore, run the following command:
    
    
    gcloud beta container backup-restore restores describe RESTORE \
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN
    

For the full list of options, refer to the [`gcloud beta container backup-restore restores describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restores/describe) documentation.

### Console

Use the following instructions to view a restore and its details in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restores** tab.

  4. In the list of restores, click the restore name and view its details.




## View a volume restore

A volume restore is a record of a volume restoration. This resource is automatically created and managed by the agent as part of the restore operation.

View a volume restore and its details by using the gcloud CLI. 

### gcloud

To list all the volume restores for a restore, run the following command:
    
    
    gcloud beta container backup-restore volume-restores list \
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN \
        --restore=RESTORE
    

For the full list of options, refer to the [`gcloud beta container backup-restore volume-restores list` ](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/volume-restores/list) documentation.

To see the details of a volume restore, run the following command:
    
    
    gcloud beta container backup-restore volume-restores describe VOLUME_RESTORE \
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN \
        --restore=RESTORE
    

For the full list of options, refer to the [`gcloud beta container backup-restore volume-restores describe` ](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/volume-restores/describe) documentation.

## Update a restore

Update a restore by using the gcloud CLI or the Google Cloud console.

### gcloud

To update a restore, for example by adding a new description, run the following command:
    
    
    gcloud beta container backup-restore restores update RESTORE\
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN \
        --description=DESCRIPTION
    

For the full list of options, refer to the [`gcloud beta container backup-restore restores update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restores/update) documentation.

### Console

Use the following instructions to update a restore in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore** tab.

  4. In the list of restores, click the restore name.

  5. In the Description field, click _edit_ **Edit**. Update the description, and then click **Save changes**.




## Delete a restore

Unlike backups, restores don't have associated artifacts. After you restore a backup, you can delete the restore without impacting either the target cluster or the source backup.

You can delete a restore by using the gcloud CLI or the Google Cloud console.

### gcloud

To delete a restore, run the following command:
    
    
    gcloud beta container backup-restore restores delete RESTORE \
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN
    

For the full list of options, refer to the [`gcloud beta container backup-restore restores delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restores/delete) documentation.

### Console

Use the following instructions to delete a restore in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restores** tab.

  4. In the list of restores, click the restore name.

  5. Click _delete_ **Delete**.

  6. Type the restore plan name and then click **Delete** in the confirmation dialog.




## Considerations

For GKE versions 1.32.3-gke.1748000 and later: if a PersistentVolumeClaim (PVC) uses a StorageClass with the `WaitForFirstConsumer` volume binding mode, and no Pod references the PVC during a restore, the PersistentVolume (PV) is still restored and bound to the PVC. This behavior applies even if no Pod is consuming the PVC.

## What's next

  * Learn how to [plan a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).
  * Learn more about [backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke).
  * Learn how to [plan a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).
  * Learn how to [enable a fine-grained restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore).
  * Learn how to [define custom backup and restore logic](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
