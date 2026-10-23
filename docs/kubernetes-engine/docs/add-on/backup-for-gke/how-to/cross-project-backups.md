---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-backups/
title: Perform cross-project backups \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:01.754293+00:00
---

# Perform cross-project backups  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Perform cross-project backups Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to perform a cross-project backup in Google Kubernetes Engine (GKE) using the Backup for GKE service.

## Overview

Cross-project backups let you decouple the backup project lifecycle from the cluster project. You can get access-controlled backups separately in a different project than the cluster project.

## Limitations

You cannot migrate existing backup plans to perform cross-project backups.

## Pricing

For pricing details, see [Pricing for cross-project backups and restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing#cross-project-backups-and-restores).

## Before you begin

  1. Before you start, make sure that you have performed the following tasks: 

     * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
     * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.
  2. Enable the Backup for GKE API in the project that contains the cluster you want to back up and the project where you want to store the backup. For more information, see [Enable the Backup for GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install#enable_the_api).

  3. Enable the Backup for GKE add-on in the cluster you want to backup. For more information, see [Enable Backup for GKE for a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster).




## Required roles

To get the permissions that you need to create and manage a cross-project backup, ask your administrator to grant you the Backup for GKE Backup Admin (`roles/gkebackup.backupAdmin`), which is a subset of Backup for GKE Admin (`roles/gkebackup.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up service accounts

If needed, create per-project service accounts to perform operations on your projects.

**Note:** Service accounts are created automatically in some scenarios. If you have Backup for GKE resources such as `BackupPlan`, `RestorePlan`, `BackupChannel`, or `RestoreChannel` in your cluster project, you don't need to execute the commands for your cluster or backup projects.

Using Google Cloud CLI, run the following commands to set up a service account:

  1. Create a service account by running the `gcloud beta services identity create` command:
         
         gcloud beta services identity create \
             --service=gkebackup.googleapis.com \
             --project=CLUSTER_PROJECT_ID
           gcloud projects add-iam-policy-binding CLUSTER_PROJECT_ID \
             --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com \
             --role=roles/gkebackup.serviceAgent \
         
           gcloud beta services identity create \
             --service=gkebackup.googleapis.com \
             --project=BACKUP_PROJECT_ID
           gcloud projects add-iam-policy-binding BACKUP_PROJECT_ID \
             --member=serviceAccount:service-BACKUP_PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com \
             --role=roles/gkebackup.serviceAgent
         

Replace the following:

     * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project that you want to create. For example, `cluster-project-id`.

     * `CLUSTER_PROJECT_NUMBER`: the unique numeric identifier for your Google Cloud project. For example, `123456789012`.

     * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

     * `BACKUP_PROJECT_NUMBER`: the unique numeric identifier of the project where your backup will be stored. For example, `123456789012`.

  2. Allow the backup project's service account to perform backups in the cluster project by running the `gcloud projects add-iam-policy-binding` command:
         
         gcloud projects add-iam-policy-binding CLUSTER_PROJECT_ID \
            --member=serviceAccount:service-BACKUP_PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com \
            --role=roles/gkebackup.serviceAgent
         

Replace the following:

     * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project. For example, `cluster-project-id`.

     * `BACKUP_PROJECT_NUMBER`: the unique numeric identifier of the project where your backup will be stored. For example, `123456789012`.

  3. Allow the cluster project's [agent](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke#agent_overview) to access `gkebackup.googleapis.com` in the backup project by running the `gcloud projects add-iam-policy-binding` command:
         
         gcloud projects add-iam-policy-binding BACKUP_PROJECT_ID \
            --member serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
            --role "roles/gkebackup.crossProjectServiceAgent"
         

Replace the following:

     * `BACKUP_PROJECT_ID`: the alphanumeric name of the Google Cloud project where your backup will be stored. For example, `backup-project-id`.

     * `CLUSTER_PROJECT_NUMBER`: the unique numeric identifier for your Google Cloud project. For example, `123456789012`.




## Create a backup channel

After you set up service accounts, you must create a backup channel in the same project and region as the cluster that you want to back up. After you create a backup channel, you can back up clusters in the project and region to the destination project.

### gcloud

To create a backup channel, run the `gcloud beta container backup-restore backup-channels create` command using Google Cloud CLI:
    
    
    gcloud beta container backup-restore backup-channels create BACKUP_CHANNEL_NAME \
     --project=CLUSTER_PROJECT_ID \
     --location=CLUSTER_LOCATION \
     --destination-project=projects/BACKUP_PROJECT_NUMBER
    

Replace the following:

  * `BACKUP_CHANNEL_NAME`: the name of the backup channel you want to create. For example, `my-backup-channel-name`.

  * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project where the cluster is located. For example, `cluster-project-id`.

  * `CLUSTER_LOCATION`: the region where the cluster is located. For example, `us-central1`.

  * `BACKUP_PROJECT_NUMBER`: the unique numeric identifier of the project where the backup will be stored.




### Console

To create a backup channel in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Backup channels** tab.

  4. In the **Backup channels** tab, click **Create a backup channel**.

  5. Using the **Cluster project** field, make sure you've selected the correct cluster project.

  6. Using the **Region** menu, select the region where your clusters are located.

  7. Using the **Backup project** field, select the project to which you want to allow backups.

  8. In the **Backup channel name** field, enter a name for your backup channel.

  9. **Optional** : in the **Backup channel description** field, enter a brief description for the backup channel.

  10. Click **Next**.

  11. Validate the service account permissions on the cluster and backup projects.

  12. Click **Create**.




## Create a backup plan

After you create a backup channel, you must create the backup plan. If the cluster being backed up resides in a different project, the backup plan is automatically bound to an existing backup channel. The `backup_channel` field in the backup plan shows the backup channel that the backup plan is bound to.

### Before you begin

Before you create a backup plan, see [Plan a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).

### Create a backup plan

To create a backup plan in the backup project using the Google Cloud console, use the following instructions:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Open the backup project you want to create the backup plan in.

  4. Click **Create a backup plan**.

  5. Select the **Configure cross-project backups** checkbox.

  6. In the **Cluster project** field, choose the project containing your source cluster.

  7. From the **Cluster** menu, select the region of the cluster.

  8. In the **Backup plan name** field, enter a name for the backup plan.

**Note:** Your choice is permanent. The name must contain lowercase letters, numbers, and hyphens; must begin with a letter and end with either a letter or number; and be between 1 to 63 characters.
  9. In the **Backup project** field, enter the name of the backup project you want to store your backups in.

  10. In the **Region** field, enter the location where your backups will be stored. If no backup channel is found, click **Create backup channel** , follow the prompts to create a backup channel, and click **Create**.

  11. Click **View backup channel details**.

  12. Click **Validate permissions**.

  13. Complete the remaining steps as described in [Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#console).

  14. Click **Create plan**.




## View a backup channel

Use the instructions in the following sections to view backup channels.

### View all backup channels within a project and region

### gcloud

To view all backup channels within a project and region, run the `gcloud beta container backup-restore backup-channels list` command using Google Cloud CLI:
    
    
      gcloud beta container backup-restore backup-channels list \
        --project=CLUSTER_PROJECT_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project where the cluster is located. For example, `cluster-project-id`.

  * `CLUSTER_LOCATION`: the region where the cluster is located. For example, `us-central1`.




### Console

To view all backup channels within a project and region in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console of your cluster project, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Backup channels** tab.

  4. Use the project and region menu to filter the list of backup channels.




The filtered list displays all backup channels in the selected project and region.

### View details of a backup channel

### gcloud

To view the details of a backup channel, run the `gcloud beta container backup-restore backup-channels describe` command using Google Cloud CLI:
    
    
      gcloud beta container backup-restore backup-channels describe BACKUP_CHANNEL_NAME \
      --project=CLUSTER_PROJECT_ID \
      --location=CLUSTER_LOCATION
    

Replace the following:

  * `BACKUP_CHANNEL_NAME`: the name of the backup channel you want to view. For example, `my-backup-channel-name`.

  * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project where the cluster is located. For example, `cluster-project-id`.

  * `CLUSTER_LOCATION`: the region where the cluster is located. For example, `us-central1`.




### Console

To view details of a backup channel in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console of your cluster project, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Backup channels** tab.

  4. Use the project and region menu to filter the list of backup channels.

  5. Click the name of the backup channel you want to view. A page with the details of that backup channel opens.




### View the backup plans bound to a backup channel

To view the backup plans that are bound to a backup channel, run the `gcloud beta container backup-restore backup-plan-bindings list` command using Google Cloud CLI:
    
    
       gcloud beta container backup-restore backup-plan-bindings list \
        --backup-channel=BACKUP_CHANNEL_NAME \
        --project=CLUSTER_PROJECT_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `BACKUP_CHANNEL_NAME`: the name of the backup channel you want to view. For example, `my-backup-channel-name`.

  * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project where the cluster is located. For example, `cluster-project-id`.

  * `CLUSTER_LOCATION`: the region where the cluster is located. For example, `us-central1`.




## Manage backup channels

The following sections describe how to manage backup channels after you create them.

### Update a backup channel

Use the following instructions to update a backup channel. Note that you can only modify the description of an existing backup channel. All other fields cannot be modified.

### gcloud

To update the description of a backup channel, run the `gcloud beta container backup-restore backup-channels update` command using Google Cloud CLI:
    
    
    gcloud beta container backup-restore backup-channels update BACKUP_CHANNEL_NAME \
      --project=CLUSTER_PROJECT_ID \
      --location=CLUSTER_LOCATION \
      --description=DESCRIPTION
    

Replace the following:

  * `BACKUP_CHANNEL_NAME`: the name of the backup channel you want to update. For example, `my-backup-channel-name`.

  * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project where the cluster is located. For example, `cluster-project-id`.

  * `CLUSTER_LOCATION`: the region where the cluster is located. For example, `us-central1`.

  * `DESCRIPTION`: the description you want to update.




### Console

To update a backup channel in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console of your cluster project, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Backup channels** tab.

  4. In the **Backup channels** page, click the backup channel you want to update. Note that you can only update the description of an existing backup channel. All other fields cannot be modified.

The **Backup Channel Details** page appears.

  5. Click **Validate permissions**.

  6. In the **Backup channel details** sections, click the edit **Edit description** icon.

The **Edit description** dialog displays.

  7. In the **Description** field, enter the updated description, then click **Save changes**.




### Delete a backup channel

You can only delete a backup channel if it does not contain any active backup plans. If active backup plans are bound to it, you must first deactivate or delete the backup plans before you can delete the backup channel.

### gcloud

To delete a backup channel, run the `gcloud beta container backup-restore backup-channels delete` command using Google Cloud CLI:
    
    
      gcloud beta container backup-restore backup-channels delete BACKUP_CHANNEL_NAME \
        --project=CLUSTER_PROJECT_ID \
        --location=CLUSTER_LOCATION
    

Replace the following:

  * `BACKUP_CHANNEL_NAME`: the name of the backup channel you want to delete. For example, `my-backup-channel-name`.

  * `CLUSTER_PROJECT_ID`: the alphanumeric name of your Google Cloud project where the cluster is located. For example, `cluster-project-id`.

  * `CLUSTER_LOCATION`: the region where the cluster is located. For example, `us-central1`.




### Console

To delete a backup channel in the Google Cloud console, use the following instructions:

  1. In the Google Cloud console of your cluster project, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. From the **Resource Management** menu, click **Backup for GKE**.

  3. Click the **Backup channels** tab.

  4. In the **Backup channels** page, click the backup channel you want to delete.

  5. Click **Delete channel**.

A dialog appears asking you to confirm that you want to delete the backup channel.

  6. In the **Backup channel name** field, enter the name of the backup channel to confirm delete.

  7. Click **Confirm**.




## What's next

  * Learn how to [perform a cross-project restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-restores).

  * Learn more about [planning a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
