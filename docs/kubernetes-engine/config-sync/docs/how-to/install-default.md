---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default/
title: Install Config Sync with default settings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:36.214895+00:00
---

# Install Config Sync with default settings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Install Config Sync with default settings Stay organized with collections  Save and categorize content based on your preferences. 

Config Sync synchronizes your Kubernetes configurations with your clusters. This document explains how to enable and configure Config Sync by using default settings. It focuses on syncing configurations from an unstructured Git repository.

This page is for Operators who want to implement [GitOps](https://opengitops.dev/) tools to centralize configuration management for their teams. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For instructions on installing Config Sync with advanced settings, see [Customize your Config Sync installation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).

## Before you begin

Before you install Config Sync, prepare your Git repository and your GKE clusters.

### Create a Git repository and grant access to Config Sync

To synchronize configuration from a Git repository to your clusters, Config Sync requires read-only access to your repository. To authorize Config Sync to read your configurations, complete the following steps:

  * Create, or have access to, a Git repository that contains the configuration files that you want Config Sync to sync to your clusters.

**Tip:** If you don't have a repository, you can [fork or clone the sample repository](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/config-sync-quickstart).
  * If your Git repository is public, no further action is needed. Config Sync doesn't require extra permissions.

  * If your Git repository is private, follow the instructions in [Grant Config Sync access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git).




### Create a cluster

If you already have a cluster prepared, for example if you followed the steps to [Grant Config Sync access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git), then proceed to Install Config Sync.

Config Sync requires that your clusters are registered to a fleet. To register your clusters, complete the following step:

###  console 

No action is required. Your clusters are automatically registered to a fleet when you install Config Sync.

###  gcloud 

  * To create an Autopilot cluster that is registered to a fleet, run the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME --enable-fleet
        

  * To create a Standard cluster that is registered to a fleet, run the following command:
        
        gcloud container clusters create CLUSTER_NAME --enable-fleet \
            --workload-pool=PROJECT_ID.svc.id.goog
        




Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `PROJECT_ID`: your project ID.



For more information about registering clusters, see [Register a cluster to a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#gcloud).

## Install Config Sync

To enable and configure Config Sync to sync configurations from your Git repository to your registered clusters, complete the following steps:

###  console 

If you use the Google Cloud console, you first install Config Sync on your clusters and then you configure a package that enables Config Sync to sync from your Git repository.

### Install Config Sync

  1. Go to the **Config Sync** page in the Google Cloud console.

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)

  2. Click **Install Config Sync**.

  3. Select **Install on all clusters in the fleet**.

  4. Leave all other settings at their default.

  5. Click **Install Config Sync**.




In the **Settings** tab, after a few minutes, **Enabled** appears in the **Status** column for the clusters in your fleet.

### Deploy a package

  1. Click **Deploy cluster package**.

  2. In the **Select clusters** tab, select the cluster that you want to deploy a package to and then click **Continue**.

  3. Click the **Configure package** tab and enter a name for your package.

  4. In the **Source** section, complete the following:

     1. In the **Repository URL** field, enter the URL of your Git repository.

     2. Optional: Review and update the other field settings. You might not need to update these settings depending on your repository structure.

  5. Optional: If your repository is private, expand the **Advanced settings** section to configure your authentication method. The Google Cloud console provides embedded instructions to help you configure your authentication settings.

  6. Leave all other settings at their default.

  7. Click **Deploy package**.




You are redirected to the Config Sync **Packages** page. After a few minutes, **Synced** appears in the **Sync status** column for the cluster that you configured.

###  gcloud 

If you use the gcloud CLI, you install Config Sync by creating a manifest that contains your Config Sync settings and then applying those settings to your cluster.

  1. Enable the `ConfigManagement` fleet feature:
         
         gcloud beta container fleet config-management enable
         

  2. Create a manifest called `apply-spec.yaml`. This example manifest contains the default settings that are recommended:
         
         applySpecVersion: 1
         spec:
           configSync:
             enabled: true
             sourceFormat: unstructured
             syncRepo: REPO_URL
             # syncRev: REVISION
             secretType: none
         

Replace the following:

     * `REPO_URL`: The URL of your Git repository, for example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples`.
     * (Optional) `REVISION`: The Git revision (tag or hash) or branch that you want to sync from. Uncomment and replace this field if you need to sync from a location other than `HEAD`.

For private repositories, you can change the `secretType` field to a supported authentication method. A Google service account (`gcpserviceaccount`) with Secure Source Manager is generally recommended. Alternatively, use `ssh` because it works with most Git providers. For more detailed instructions on supported authentication methods, see [Grant access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git).

  3. Apply the manifest to your cluster:
         
         gcloud beta container fleet config-management apply \
             --membership=MEMBERSHIP_NAME \
             --config=apply-spec.yaml \
             --project=PROJECT_ID
         

Replace the following:

     * `MEMBERSHIP_NAME`: the fleet membership name that you chose when you registered your cluster. Get the name with the `gcloud container fleet memberships list` command.
     * `PROJECT_ID`: Your project ID.



## Verify the installation

After you install and configure Config Sync, verify that the installation completed successfully.

###  console 

  1. Go to the **Config Sync** page in the Google Cloud console.

[Go to Config Sync](https://console.cloud.google.com/kubernetes/config/details)

  2. On the **Packages** tab, check the **Sync status** column in the cluster table. A successful installation of Config Sync shows a status of **Installed**. A successfully configured Git repository shows a status of **Synced**.




###  gcloud 

Run the following command:
    
    
    nomos status
    

A successful installation shows a status of `SYNCED` or `PENDING`.

For more details on the information supplied by the `nomos status` command, including reported errors, see [Check Config Sync status](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install) in the `nomos` command-line tool documentation.

## What's next

  * [Customize your Config Sync installation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).
  * [Use the `nomos` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command).
  * Read the [Introduction to troubleshooting Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
