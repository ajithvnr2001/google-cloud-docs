---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/delete-node-pool/
title: Delete a node pool \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:50.932005+00:00
---

# Delete a node pool  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/delete-node-pool/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Delete a node pool Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to delete node pools in GKE on AWS.

## Before you begin

This page assumes you are familiar with the cluster autoscaler. For more information, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/cluster-autoscaler).

## Delete a node pool

To delete a node pool, run the following command:

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. In the cluster list, select the name of the cluster, and then select **View details** in the side panel.

  4. Select the **Nodes** tab to see a list of all the node pools.

  5. Select a node pool from the list.

  6. Near the top of the window, click delete  **Delete**.

If the delete fails, follow the steps in the `gcloud` tab and add the `--ignore-errors` flag to the `gcloud container aws node-pools delete` command.




### gcloud

  1. Get a list of your node pools:
         
         gcloud container aws node-pools list \
           --cluster CLUSTER_NAME \
           --location GOOGLE_CLOUD_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that the node pool is attached to
     * `GOOGLE_CLOUD_LOCATION`: the Google Cloud location hosting the node pool
  2. For each of your node pools, delete it with the following command:
         
         gcloud container aws node-pools delete NODE_POOL_NAME \
           --cluster CLUSTER_NAME \
           --location GOOGLE_CLOUD_LOCATION
         

Replace the following:

     * `NODE_POOL_NAME`: the name of the node pool to delete
     * `CLUSTER_NAME`
     * `GOOGLE_CLOUD_LOCATION`

If the command returns an error and the delete fails, you can force the deletion by running the command again with the `--ignore-errors` flag. This flag is available in version 1.29 and later.

**Caution:** Adding the `--ignore-errors` flag to the delete command might result in orphaned AWS resources. If that happens, consult the AWS documentation on how to remove the orphaned resources.



#### How GKE on AWS protects workloads during node pool deletion

During node pool deletion, GKE on AWS performs graceful shut down on each node without honoring PodDisruptionBudget. It takes the following steps:

  1. Disable cluster autoscaler if it was enabled.
  2. Set up a deadline for the draining process. After this deadline, even if there are still Pod objects existing, GKE on AWS stops draining and proceeds to deleting underlying virtual machines. The default deadline is 5 minutes. For every 10 more nodes, 5 more minutes is added. 
  3. Cordon all the nodes in the node pool.
  4. Before deadline is met, delete Pod objects in the node pool with best efforts.
  5. Delete all the underlying compute resources.



## What's next

  * Read the reference guide for [gcloud container aws node-pools ](https://cloud.google.com/sdk/gcloud/reference/container/aws/node-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
