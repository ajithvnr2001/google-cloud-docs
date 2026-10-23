---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster/
title: Enable Backup for GKE for a cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:38.499605+00:00
---

# Enable Backup for GKE for a cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Enable Backup for GKE for a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to enable [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) for a cluster.

You can enable Backup for GKE for Standard and Autopilot clusters in the following ways:

  * During cluster creation or updates with the Cloud console, gcloud, or Terraform.
  * Automatically enabled when you create your first backup plan or restore plan for Standard or Autopilot clusters.



Enabling Backup for GKE during cluster creation is preferable as it saves time and is faster to create a cluster with the agent installed than to create the cluster and then enable the agent.

## Enable Backup for GKE for a Standard cluster

You can enable Backup for GKE for a Standard cluster with the Google Cloud CLI, Google Cloud console, or Terraform.

### gcloud

To install the Backup for GKE agent, add the following parameter: `sh --addons=BackupRestore` to the Google Cloud CLI cluster creation command.

The following example shows how you can create a 1.24 cluster with the Backup for GKE agent installed:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --project=PROJECT_ID  \
        --location=LOCATION \
        --cluster-version=1.24.2-gke.1900 \
        --addons=BackupRestore
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to back up.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, for example `us-central1`.



### Console

Use the following instructions to enable Backup for GKE for a Standard cluster in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. In the **Create cluster** dialog, click **Configure** that is next to Standard cluster mode.

  4. In the navigation menu, click **Backup plan** and then select the **Enable Backup for GKE** checkbox.

  5. Optional: Select the **Create backup plan** checkbox.

     1. In the **Backup plan name** field, enter a name.
     2. From the **Region** list, select a location where the backups to be stored. The **Regions** list displays the regions where Backup for GKE is supported. For a list of Backup for GKE supported regions, see [Backup for GKE locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations).

The **Backup plan details** section displays the plan details with the daily scheduled backups and seven days of retention period by default.

     3. Click **Edit backup plan details** to update backup plan details.

  6. Click **Create**.




### Terraform

Enable using a `gke_backup_agent_config` entry in your `google_container_cluster` resource:
    
    
    resources "google_container_cluster" "primary" {
       name = "my_cluster"
       ...
       addons_config {
         gke_backup_agent_config {
           enabled = true
         }
       }
     }
    

For more information, see [container_cluster gke_backup_agent_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#gke_backup_agent_config)

## Enable Backup for GKE for a Autopilot cluster

You can enable Backup for GKE for a Autopilot cluster with the Google Cloud CLI, Google Cloud console, or Terraform.

### gcloud

To install the Backup for GKE agent, add the following parameter: `sh --enable-backup-restore` to the Google Cloud CLI cluster creation command.

The following example shows how you can create a autopilot cluster with the Backup for GKE agent installed:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
       --project=PROJECT_ID  \
       --location=LOCATION \
       --release-channel=RELEASE_CHANNEL \
       --enable-backup-restore
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to back up.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, for example `us-central1`.
  * `RELEASE_CHANNEL`: the name of the [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels) for the cluster. The default is `Regular`.



### Console

Use the following instructions to enable Backup for GKE for a Autopilot cluster in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. In the **Create cluster** dialog, click **Configure** that is next to Autopilot cluster mode.

  4. In the navigation menu, click **Advanced settings**.

  5. Click the **Backup plan** section and select the **Create backup plan** checkbox.

  6. In the **Backup plan name** field, enter a name.

  7. From the **Region** list, select a location where the backups to be stored. The **Regions** list displays the regions where Backup for GKE is supported. For a list of Backup for GKE supported regions, see [Backup for GKE locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations).

  8. Click **Create**.

The **Backup plan details** section displays the plan details with the daily scheduled backups and seven days of retention period by default.




### Terraform

Enable using a `gke_backup_agent_config` entry in your `google_container_cluster` resource:
    
    
    resources "google_container_cluster" "primary" {
      name = "my_cluster"
      enable_autopilot = true
      ...
      addons_config {
        gke_backup_agent_config {
          enabled = true
        }
      }
    }
    

For more information, see [container_cluster gke_backup_agent_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#gke_backup_agent_config)

## Enable Backup for GKE on an existing cluster

You can enable Backup for GKE on an existing cluster with Google Cloud CLI, Google Cloud console, or Terraform.

### gcloud

To install the Backup for GKE agent, add the `--update-addons=BackupRestore=ENABLED` parameter to the `gcloud container clusters update` command.

The following example shows how you can update an existing cluster with the Backup for GKE agent.
    
    
    gcloud container clusters update CLUSTER_NAME \
       --project=PROJECT_ID  \
       --location=LOCATION \
       --update-addons=BackupRestore=ENABLED
    

Replace the following:

  * `CLUSTER_NAME`: the name of the existing cluster.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, for example `us-central1`.



### Console

Use the following instructions to enable Backup for GKE for an existing cluster in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Features** , next to the **Backup for GKE** field, click _edit_ **Edit Backup for GKE**.

  4. Select the **Enable Backup for GKE** checkbox.

  5. Click **Save Changes**.




### Terraform

Enable using a `gke_backup_agent_config` entry in your `google_container_cluster` resource:
    
    
    resources "google_container_cluster" "primary" {
      name = "my_cluster"
      enable_autopilot = true
      ...
      addons_config {
        gke_backup_agent_config {
          enabled = true
        }
      }
    }
    

For more information, see [container_cluster gke_backup_agent_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#gke_backup_agent_config)

## Verify that Backup for GKE is enabled on your cluster

You can verify that your cluster is using Backup for GKE with the gcloud CLI or the Google Cloud console.

### gcloud

Verify that Backup for GKE is enabled for your cluster:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --project=PROJECT_ID  \
        --location=LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, for example `us-central1`.



If Backup for GKE is enabled, the output of the command includes these lines:
    
    
    addonsConfig:
      gkeBackupAgentConfig:
        enabled: true
    

### Console

Perform the following tasks in the Google Cloud console:

Use the following instructions to verify Backup for GKE for a cluster in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster that you want to inspect.

  3. In the **Features** section, verify that **Backup for GKE** is **Enabled**.




## What's next

  * Learn more about [defining custom backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application).
  * Learn more about [planning a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
