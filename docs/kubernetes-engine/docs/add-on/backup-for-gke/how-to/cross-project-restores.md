---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-restores/
title: Perform cross-project restores \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:39.784209+00:00
---

# Perform cross-project restores  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-restores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Perform cross-project restores Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to perform a cross-project restore in Google Kubernetes Engine (GKE) by using the Backup for GKE service.

## Overview

Backup for GKE cross-project restores let you restore a backup from one project to a cluster in a destination project. You can store backups in a dedicated project and then restore these backups to clusters in other projects.

## Limitations

You cannot migrate existing restore plans to perform cross-project restores.

## Pricing

For pricing details, see [Pricing for cross-project backups and restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing#cross-project-backups-and-restores).

## Before you begin

  1. Before you start, make sure that you have performed the following tasks: 

     * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
     * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.
  2. Enable the Backup for GKE API in the project that contains the cluster you want to restore to. For more information, see [Enable the Backup for GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install#enable_the_api).

  3. Enable the Backup for GKE add-on in the cluster you want to restore to. For more information, see [Enable Backup for GKE for a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster).




## Required roles

To get the permissions that you need to create and manage a cross-project restore, ask your administrator to grant you the Backup for GKE Backup Admin (`roles/gkebackup.backupAdmin`), which is a subset of Backup for GKE Admin (`roles/gkebackup.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up service accounts

If needed, create per-project service accounts to perform operations on your projects.

  1. Create a service account by running the `gcloud beta services identity create` command using Google Cloud CLI:
         
         gcloud beta services identity create --service=gkebackup.googleapis.com --project=RESTORE_PROJECT_ID
         gcloud projects add-iam-policy-binding RESTORE_PROJECT_ID --member=serviceAccount:service-RESTORE_PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com --role=roles/gkebackup.serviceAgent
         

Replace the following:

     * `RESTORE_PROJECT_ID`: the alphanumeric name of your Google Cloud project that you want to restore. For example, `restore-project-id`.

     * `RESTORE_PROJECT_NUMBER`: the unique numeric identifier for your Google Cloud project. For example, `123456789012`.

  2. Permit the restore project's agent to access `gkebackup.googleapis.com` in the backup project by running the `gcloud projects add-iam-policy-binding` command:
         
         gcloud projects add-iam-policy-binding BACKUP_PROJECT_ID --member serviceAccount:service-RESTORE_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com --role "roles/gkebackup.crossProjectServiceAgent"
         

Replace the following:

     * `BACKUP_PROJECT_ID`: the alphanumeric name of your Google Cloud project that contains your backup. For example, `backup-project-id`.

     * `RESTORE_PROJECT_NUMBER`: the unique numeric identifier for the Google Cloud project you want to restore using the backup. For example, `123456789012`.




## Create a restore channel

You must create a restore channel in the same project and region as the backup that you want to restore, and configure the destination project in the channel. By doing so, you can restore backups in the original project and region to the destination project.

### gcloud

To create a restore channel, run the `gcloud beta container backup-restore restore-channels create` command using Google Cloud CLI:
    
    
    gcloud beta container backup-restore restore-channels create RESTORE_CHANNEL_NAME \
     --project=BACKUP_PROJECT_ID \
     --location=BACKUP_LOCATION \
     --destination-project=projects/RESTORE_PROJECT_NUMBER
    

Replace the following:

  * `RESTORE_CHANNEL_NAME`: the name of the restore channel you want to create.

  * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

  * `BACKUP_LOCATION`: the region where the backup will be stored. For example, `us-central1`.

  * `RESTORE_PROJECT_NUMBER`: the unique numeric identifier of the project where you want to restore your backup. For example, `123456789012`.




### Console

To create a restore channel in the Google Cloud console, use the following instructions:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Restore channels** tab.

  4. In the **Restore channels** tab, click **Create a restore channel**.




## Create a restore plan

After you create a restore channel, you must create the restore plan. If the restore plan you use resides in a different project, it becomes automatically bound to an existing restore channel. The `restore_channel` field in the restore plan shows the restore channel that the restore plan is bound to.

### Before you begin

Before you create a restore plan, see [Plan a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).

### Create a restore plan

Create a restore plan in the restore project using the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Ensure that you are in the project you want to create a restore plan in.

  4. Click **Create a restore plan**.

  5. Click the **Configure cross-project restore** box.

  6. In the **Backup project** field, choose the project that contains your backup plans and backups.

  7. In the **Backup plan** field, choose the corresponding backup plan.

  8. In the **Restore project** field, choose the project containing your restore plans and restores. If no restore channel is found, click **Create restore channel** , follow the prompts to create a restore channel, and click **Create**.

  9. Click **View restore channel details**.

  10. Click **Validate permissions**.

  11. Complete the remaining steps as described in the Backup for GKE documentation on how to [create a restore plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).




## View restore channels

The following sections describe ways to view restore channels.

### View all restore channels within a project and region

### gcloud

To view all restore channels within a project and region, run the `gcloud beta container backup-restore restore-channels list` command using Google Cloud CLI:
    
    
      gcloud beta container backup-restore restore-channels list \
      --project=BACKUP_PROJECT_ID \
      --location=BACKUP_LOCATION
    

Replace the following:

  * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

  * `BACKUP_LOCATION`: the region where the backup will be stored. For example, `us-central1`.




### Console

To view all restore channels in the Google Cloud console, use the following instructions:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console of your backup project.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Restore channels** tab.

  4. To select the project you want to view, use the **Project** menu.

  5. To select the region of your restore channel, use the **Region** menu.

The console displays a table with all the restore channels for the selected project and region.




### View details of a restore channel

### gcloud

To view the details of a restore channel, run the `gcloud beta container backup-restore restore-channels describe` command using Google Cloud CLI:
    
    
      gcloud beta container backup-restore restore-channels describe RESTORE_CHANNEL_NAME \
        --project=BACKUP_PROJECT_ID \
        --location=BACKUP_LOCATION
    

Replace the following:

  * `RESTORE_CHANNEL_NAME`: the name of the restore channel you want to view.

  * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

  * `BACKUP_LOCATION`: the region where the backup will be stored. For example, `us-central1`.




### Console

To view details of a restore channel in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console of your backup project, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Restore channels** tab.

  4. To select the project you want to view, use the **Project** menu.

  5. To select the region of your restore channel, use the **Region** menu.

  6. Click the name of the restore channel you want to view.

The Google Cloud console displays the details of the selected restore channel.




### View restore plans bound to a restore channel

To view restore plans that are bound to a restore channel, run the `gcloud beta container backup-restore restore-plan-bindings list` command using Google Cloud CLI:
    
    
      gcloud beta container backup-restore restore-plan-bindings list \
       --restore-channel=RESTORE_CHANNEL_NAME \
       --project=BACKUP_PROJECT_ID \
       --location=BACKUP_LOCATION
    

Replace the following:

  * `RESTORE_CHANNEL_NAME`: the name of the restore channel you want to view.

  * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

  * `BACKUP_LOCATION`: the region where the backup will be stored. For example, `us-central1`.




## Manage restore channels

The following sections describe how to manage restore channels.

### Update a restore channel

Use the following instructions to update a restore channel. Note that you can only update the description of an existing restore channel. All other fields cannot be modified.

### gcloud

To update the description of a restore channel, run the `gcloud beta container backup-restore restore-channels update` command using Google Cloud CLI:
    
    
    gcloud beta container backup-restore restore-channels update RESTORE_CHANNEL_NAME \
    --project=BACKUP_PROJECT_ID \
    --location=BACKUP_LOCATION \
    --description=DESCRIPTION
    

Replace the following:

  * `RESTORE_CHANNEL_NAME`: the name of the restore channel you want to update.

  * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

  * `BACKUP_LOCATION`: the region where the backup will be stored. For example, `us-central1`.

  * `DESCRIPTION`: the updated description of the restore channel.




### Console

To update a restore channel in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console of your backup project, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Restore channels** tab.

  4. In the **Restore channels** page, click the restore channel you want to update. Note that you can only update the description of an existing restore channel. All other fields cannot be modified.

The **Restore channel details** page displays.

  5. Click **Validate permissions**.

  6. In the **Restore channel details** section, click the edit **Edit description** icon.

The **Edit description** dialog displays.

  7. In the **Description** field, enter the updated description of the restore channel, then click **Save changes**.




### Delete a restore channel

Use the following instructions to delete a restore channel. Note that a restore channel can only be deleted if it doesn't have any restore plans bound to it. If any restore plans are bound to it, you need to delete the restore plans before you attempt to delete the restore channel.

### gcloud

To delete a restore channel, run the `gcloud beta container backup-restore backup-channels delete` command using Google Cloud CLI:
    
    
      gcloud beta container backup-restore backup-channels delete RESTORE_CHANNEL_NAME \
      --project=BACKUP_PROJECT_ID \
      --location=BACKUP_LOCATION
    

Replace the following:

  * `RESTORE_CHANNEL_NAME`: the name of the restore channel you want to delete.

  * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

  * `BACKUP_LOCATION`: the region where the backup will be stored. For example, `us-central1`.




### Console

To delete a restore channel in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console of your backup project, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Restore channels** tab.

  4. In the **Restore channels** page, click the restore channel you want to delete.

  5. Click **Delete channel**.

A dialog appears asking you to confirm that you want to delete the restore channel.

  6. In the **Restore channel name** field, enter the name of the restore channel to confirm delete.

  7. Click **Confirm**.




## What's next

  * Learn more about [planning a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
