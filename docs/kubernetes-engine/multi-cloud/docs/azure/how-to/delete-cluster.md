---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/delete-cluster/
title: Delete a cluster \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:19.619727+00:00
---

# Delete a cluster  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/delete-cluster/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete a cluster

This page explains how to delete a node pool, a cluster, and an AzureClient resource.

**Warning:** Soon after you delete a Google Cloud project, the resources in Azure are permanently deleted. To safeguard against the accidental deletion of a Google Cloud project, use a [Project lien](https://docs.cloud.google.com/resource-manager/docs/project-liens).

## Delete a node pool

To delete a cluster, you must first delete all of its node pools.

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. In the cluster list, select the name of the cluster, and then select **View details** in the side panel.

  4. Select the **Nodes** tab to see a list of all the node pools.

  5. Select a node pool from the list.

  6. Near the top of the window, click delete  **Delete**.

If the delete fails, follow the steps in the `gcloud` tab and add the `--ignore-errors` flag to the `gcloud container azure node-pools delete` command.




### gcloud

  1. Get a list of your node pools:
         
         gcloud container azure node-pools list \
           --cluster CLUSTER_NAME \
           --location GOOGLE_CLOUD_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that the node pool is attached to
     * `GOOGLE_CLOUD_LOCATION`: the Google Cloud location hosting the node pool
  2. For each of your node pools, delete it with the following command:
         
         gcloud container azure node-pools delete NODE_POOL_NAME \
           --cluster CLUSTER_NAME \
           --location GOOGLE_CLOUD_LOCATION
         

Replace the following:

     * `NODE_POOL_NAME`: the name of the node pool to delete
     * `CLUSTER_NAME`
     * `GOOGLE_CLOUD_LOCATION`

If the command returns an error and the delete fails, you can force the deletion by running the command again with the `--ignore-errors` flag. This flag is available in version 1.29 and later.

**Caution:** Adding the `--ignore-errors` flag to the delete command might result in orphaned Azure resources. If that happens, consult the Azure documentation on how to remove the orphaned resources.



#### How GKE on Azure protects workloads during node pool deletion

During node pool deletion, GKE on Azure performs graceful shut down on each node without honoring PodDisruptionBudget. It takes the following steps:

  1. Disable cluster autoscaler if it was enabled.
  2. Set up a deadline for the draining process. After this deadline, even if there are still Pod objects existing, GKE on Azure stops draining and proceeds to deleting underlying virtual machines. The default deadline is 5 minutes. For every 10 more nodes, 5 more minutes is added. 
  3. Cordon all the nodes in the node pool.
  4. Before deadline is met, delete Pod objects in the node pool with best efforts.
  5. Delete all the underlying compute resources.



## Delete a cluster

Before deleting a cluster, make sure that you have deleted all of its node pools.

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. In the cluster list, select the name of the cluster, and then select **View details** in the side panel.

  4. Near the top of the window, click delete  **Delete**.

If the delete fails, follow the steps in the `gcloud` tab and add the `--ignore-errors` flag to the `gcloud container azure clusters delete` command.




### gcloud

To delete a cluster, run the following command:
    
    
    gcloud container azure clusters delete CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to delete
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud location hosting this cluster

If the command returns an error and the delete fails, you can force the deletion by running the command again with the `--ignore-errors` flag. This flag is available in version 1.29 and later.

**Caution:** Adding the `--ignore-errors` flag to the delete command might result in orphaned Azure resources. If that happens, consult the Azure documentation on how to remove the orphaned resources.



## Delete an AzureClient resource

You should delete an AzureClient in the following cases:

  * You have removed all GKE on Azure and you don't need the AzureClient any more.
  * You have updated the cluster's Authentication from AzureClient to [workload identity federation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster#workload-identity-federation).



Note that before deleting an AzureClient, you need to have deleted all the clusters that use the AzureClient.

To delete an AzureClient resource, run the following command:
    
    
    gcloud container azure clients delete CLIENT_NAME \
        --location=GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLIENT_NAME`: the name of the AzureClient to delete
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud location where the client is located



After deleting the AzureClient resource, remove the certificate at Azure AD that you uploaded when you created the client.

## What's next

  * For more information, see the [`gcloud container azure clusters delete`](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/delete) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
