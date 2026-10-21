---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/upgrade-cluster/
title: Upgrade your Azure cluster version \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:40:48.847322+00:00
---

# Upgrade your Azure cluster version  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/upgrade-cluster/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade your Azure cluster version

This page explains how to upgrade the Kubernetes version of your GKE on Azure clusters.

## Prerequisites

Upgrading your cluster's Kubernetes version is a specific case of the more general cluster update operation. You can read about cluster update operations in general at the [update your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-cluster) page. To upgrade your cluster version:

  * You must upgrade through every minor version between the current and target version. For example, to upgrade from 1.20 to 1.22, you must first upgrade from 1.20 to 1.21, and then upgrade from 1.21 to 1.22.
  * You must have the `gkemulticloud.googleapis.com/azureClusters.update` Identity and Access Management permission.



## How GKE on Azure performs updates

Because upgrading a cluster requires restarting the control plane nodes, GKE on Azure performs a "rolling update" with the following steps:

  1. Choose one control plane instance to update. GKE on Azure updates unhealthy instances, if any, before healthy ones.
  2. Delete the instance. GKE on Azure recreates the instance and the instance boots with the new configuration.
  3. Perform health checks on the new instance.
  4. If the health checks succeed, select another instance and perform the same steps on it. Repeat this cycle until all instances are restarted or recreated. If the health check fails, GKE on Azure places the cluster into a `DEGRADED` state and stops the update. For more information, see the following section.



## When an update fails

After an update, GKE on Azure performs a health check on the cluster. If the health check fails, the cluster is marked as `DEGRADED`. You can display the status of your cluster with the following Google Cloud CLI command:
    
    
    gcloud container azure clusters describe CLUSTER_NAME \
      --location=GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster



## Perform the upgrade

### Check your cluster version

Before upgrading your cluster version, use the following command to check which versions are available in your region:
    
    
    gcloud container azure get-server-config \
        --location=GOOGLE_CLOUD_LOCATION
    

Replace `GOOGLE_CLOUD_LOCATION` with the Google Cloud location from which you manage your clusters.

### Choose an upgrade method

You can upgrade your cluster version through either the Google Cloud console, the Google Cloud CLI or the GKE Multi-Cloud API. If you want to use the console to upgrade a cluster, you must first choose and configure an authentication method for logging in to the cluster. For more information, see [Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster).

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. In the cluster list, select the name of the cluster, and then select **View details** in the side panel.

  4. On the **Details** tab, select edit  **Upgrade**.

  5. In the **Upgrade the Kubernetes version for the cluster** dialog box, select the version that you want to upgrade to and click **Done**. Note that you must upgrade through all minor versions when upgrading your cluster.




### gcloud

To upgrade your cluster's Kubernetes version, run the following command:
    
    
    gcloud container azure clusters update CLUSTER_NAME \
        --location=GOOGLE_CLOUD_LOCATION \
        --cluster-version=CLUSTER_VERSION
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster—for example, `us-west1`
  * `CLUSTER_VERSION`: the new [supported cluster version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-versions)



### API

To update your cluster through the API, use a `PATCH` operation on the GKE Multi-Cloud API.

  1. Create a JSON file named `cluster_update.json` with the following contents:
         
         {
             "controlPlane": {
                "version": "CLUSTER_VERSION",
             },
         }
         

Replace the following:

     * `CLUSTER_VERSION`: the new [supported cluster version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-versions). Note that you must upgrade through all minor versions when upgrading your cluster
  2. Update these settings through the GKE Multi-Cloud API with following command.
         
         curl -d @cluster_update.json -X PATCH \
            ENDPOINT/projects/PROJECT_ID/locations/GOOGLE_CLOUD_LOCATION/azureClusters/CLUSTER_ID?update_mask=controlPlane.Version
         




Replace the following:

  * `ENDPOINT`: Your Google Cloud [service endpoint](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest#rest_endpoints)
  * `PROJECT_ID`: Your Google Cloud project
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster—for example, `us-west1`
  * `CLUSTER_ID`: Your cluster ID



For more information, see the [`projects.locations.azureClusters.patch`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters/patch) method documentation.

## Upgrade your node pools

After you upgrade your cluster version, upgrade your node pools to complete the process. To learn how, see [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-node-pool).

## What's next

  * Learn how to perform other [cluster updates](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-cluster).

  * For more information on updatable fields, see the [`gcloud container azure clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update) reference documentation.

  * See the [`projects.locations.azureClusters.patch`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters/patch) REST API documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
