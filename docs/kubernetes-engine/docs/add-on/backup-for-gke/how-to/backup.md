---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup/
title: Back up your workloads \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:12:02.828150+00:00
---

# Back up your workloads  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Back up your workloads Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to create a backup of your workloads in Google Kubernetes Engine (GKE) using the Backup for GKE service.

## Introduction

Two forms of data are captured in a backup:

  * **Config backup** : A set of Kubernetes resource descriptions extracted from the API server of the cluster undergoing backup.
  * **Volume backup** : A set of volumes that correspond to `PersistentVolumeClaim` resources found in the config backup.



If your backup plan defines a schedule for the backup, the backups are automatically created according to that schedule. You can also create a backup manually. For example, you might want to back up your workloads before you upgrade your applications.

## Before you begin

[Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create).

## Required roles

To get the permissions that you need to create and manage a backup, ask your administrator to grant you the Backup for GKE Backup Admin (`roles/gkebackup.backupAdmin`), which is a subset of Backup for GKE Admin (`roles/gkebackup.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a manual backup

You can manually create a backup for a backup plan by using the Google Cloud CLI or the Google Cloud console.

### gcloud

Run the following command:
    
    
    gcloud beta container backup-restore backups create BACKUP \
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN \
        WAIT_OPTION
    

Replace the following:

  * `BACKUP`: the name of the backup that you want to create.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the parent backup plan.
  * `BACKUP_PLAN`: the name of the parent backup plan that this backup is derived from.
  * `WAIT_OPTION`: defines when the command should return:

    * `--async`: The command returns as soon as the service acknowledges receipt. Will return almost immediately.
    * (default): The command will return once the service has instructed the agent in the cluster to begin the backup process. Will usually return within a few seconds.
    * `--wait-for-completion`: Wait until the agent has completed the backup operation in the cluster. May take several minutes.



For the full list of options, refer to the [`gcloud beta container backup-restore backups create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/create) documentation.

### Console

Use the following instructions to create a manual backup in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backup Plans** tab.

  4. Expand the cluster and find the plan that you want to create a backup for.

  5. Click **Start a backup**.

  6. Enter a backup name and optional description.

  7. (Optional) Set the number of days to retain the backup before the backup is automatically deleted.

  8. (Optional) Set the number of days during which backups cannot be deleted.

  9. Click **Start backup**.




## View a backup

View a backup and its details by using the gcloud CLI or the Google Cloud console.

### gcloud

To list all the backup plans for a backup plan, run the following command:
    
    
    gcloud beta container backup-restore backups list \
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN
    

For **`list`** commands only, you can provide "-" as the value for any parameters except `PROJECT_ID` and `-` acts as a wildcard. `-` is the default value for any parameter if you don't specify a command-line option or set a property.

For the full list of options, refer to the [`gcloud beta container backup-restore backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/list) documentation.

To see the details of a backup, run the following command:
    
    
    gcloud beta container backup-restore backups describe BACKUP \
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN
    

For the full list of options, refer to the [`gcloud beta container backup-restore backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/describe) documentation.

### Console

Use the following instructions to view a backup and its details in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. Expand the backup plan and click the backup name.




## View backup index

The backup index provides information about the resources that are included in a backup. With the backup index, you can identify if a specific resource is backed up or not. The backup index displays the resource details such as resource name, resource type, group, and version.

You can view the backup index by using the gcloud CLI or the Google Cloud console.

### gcloud

View the group, version, kind, and name of each resource in a backup:
    
    
    gcloud beta container backup-restore backups get-backup-index-download-url BACKUP \
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN
    

The command generates a URL which lets you view and download the backup index. The URL expires after 10 minutes.

For the full list of options, refer to the [`gcloud beta container backup-restore backups get-backup-index-download-url`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/get-backup-index-download-url) documentation.

### Console

Use the following instructions to view backup index and its details in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine.](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. Expand the backup plan and click the backup name.

  5. Click **Backup index**.




## View a volume backup

Volume backup resources are automatically created by the agent when `PersistentVolumeClaims` are encountered within the scope of a backup. Each volume backup corresponds to a persistent disk snapshot. These resources are created and managed by the agent automatically as part of the backup operation. You can view a volume backup and its details by using the gcloud CLI or the Google Cloud console.

### gcloud

To list all the volume backups for a backup, run the following command:
    
    
    gcloud beta container backup-restore volume-backups list \
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN \
        --backup=BACKUP
    

For the full list of options, refer to the [`gcloud beta container backup-restore volume-backups list` ](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/volume-backups/list) documentation.

To see the details of a volume backup, run the following command:
    
    
    gcloud beta container backup-restore volume-backups describe VOLUME_BACKUP \
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN \
        --backup=BACKUP
    

For the full list of options, refer to the [`gcloud beta container backup-restore volume-backups describe` ](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/volume-backups/describe) documentation.

### Console

Use the following instructions to view the volume backup details in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine.](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. Expand the backup plan and click the backup name.

  5. Click the **Storage contents** tab.

The backup displays the following storage content details: persistent volume claim name, persistent volume name, namespace, disk handle, volume type, and volume backup name.

  6. Click **Volume backup** to view volume backup details.




## Update a backup

You might want to edit the information about a backup, for example its description or labels. Changing the description or labels does not impact how the backup is handled.

You might also want to modify the retention policy for the backup, for example how long to retain the backup, or the period of time during which backups cannot be deleted. You can only increase retention policy parameters.

Update a backup by using the gcloud CLI or the Google Cloud console.

### gcloud

To update a backup, for example by adding a new description, run the following command:
    
    
    gcloud beta container backup-restore backups update BACKUP\
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN \
        --description=DESCRIPTION
    

For the full list of options, refer to the [`gcloud beta container backup-restore backups update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/update) documentation.

### Console

Use the following instructions to update a backup in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. Expand the backup plan and click the backup name.

  5. Click _edit_ **Edit** to edit a backup section and click **Save changes**.




## Delete a backup

Backups can be deleted in two ways:

  * If the backup plan defines a retention period, backups created for that plan are automatically deleted after that period expires.
  * You can manually delete the backup.



If the backup plan for this backup defines a minimum lifetime for backups, configured with the `--backup-delete-lock-days` flag, then backups created for this plan cannot be deleted (either automatically or manually) until that lifetime expires.

You can manually delete a backup by using the gcloud CLI or the Google Cloud console.

### gcloud

To delete a backup, run the following command:
    
    
    gcloud beta container backup-restore backups delete BACKUP \
        --project=PROJECT_ID \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN
    

For the full list of options, refer to the [`gcloud beta container backup-restore backups delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/delete) documentation.

### Console

Use the following instructions to delete a backup in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. Expand the plan and click the backup name.

  5. Click _delete_ **Delete backup**.

  6. Type the backup plan name and then click **Delete backup** in the confirmation dialog.




## What's next

  * Learn more about [planning a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
