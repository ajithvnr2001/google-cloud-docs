---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization/
title: Identify underprovisioned and overprovisioned GKE clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:15.693611+00:00
---

# Identify underprovisioned and overprovisioned GKE clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Identify underprovisioned and overprovisioned GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) provides insights and recommendations for cost optimization scenarios such as overprovisioned clusters and [idle clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters), and reliability improvement scenarios such as underprovisioned clusters. This document explains how to identify underprovisioned and overprovisioned GKE clusters. GKE provides corresponding recommendations to scale up or scale down the clusters. GKE also provides similar rightsizing recommendations for workloads. For more information, see [Identify underprovisioned and overprovisioned workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization).

After you verify that the identified clusters would benefit from the recommendation to scale up or down, you can make the recommended change to save costs or increase the reliability of your cluster. If possible, the recommendation includes projected monthly savings or cost. For more information, see Understand cost or savings estimates.

GKE doesn't provide these insights for Autopilot clusters, which incur minimal operational costs because you only pay for the resources that your workloads request. For more information, see [Autopilot Pricing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#pricing).

GKE monitors your clusters and delivers guidance to optimize your usage through [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist), a service that provides recommenders that generate insights and recommendations for using resources on Google Cloud. For more information about how to manage insights and recommendations, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

## Get insights and recommendations for underprovisioned and overprovisioned clusters

GKE surfaces these insights and recommendations in the following locations in the Google Cloud console after observing the specific behavior discussed in the following section:

  * [**Kubernetes Clusters** page](https://console.cloud.google.com/kubernetes/list), in the following locations:

    * In the **Kubernetes clusters** list, in the **Notifications** column for the applicable clusters
    * Notification banners on the **Clusters** page for a specific cluster
  * [FinOps hub](https://console.cloud.google.com/billing/optimize)




The recommendations have the following titles in the **Kubernetes Clusters** page:

  * **Overprovisioned clusters** : "Decrease cluster resources to reduce costs"
  * **Underprovisioned clusters** : "Increase cluster resources to improve reliability"



You can also receive these insights and recommendations through the Google Cloud CLI or the Recommender API, using the `CLUSTER_UNDERPROVISIONED` and `CLUSTER_OVERPROVISIONED` subtypes.

Follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

After you identify underprovisioned or overprovisioned clusters, see the considerations when rightsizing clusters.

## How GKE identifies underprovisioned and overprovisioned clusters

The following table describes the signals that GKE uses for identifying underprovisioned and overprovisioned clusters that can be scaled up or down, and the threshold for each signal. Additionally, this table shows the action that we recommend that you take in this scenario.

Subtype | Signal | Observation period | Details | Recommendation  
---|---|---|---|---  
`CLUSTER_UNDERPROVISIONED` | CPU or memory usage is high | Last 30 days | A GKE cluster is underprovisioned when both CPU and memory utilization average greater than 80% during every hour, over the last 30 days. | Scale up your cluster to increase reliability  
`CLUSTER_OVERPROVISIONED` | CPU and memory usage is low | Last 30 days |  A GKE cluster is overprovisioned when CPU and memory utilization average between 7% and 20% during every hour, over the last 30 days. **Note:** A cluster with under 7% CPU utilization over the last 30 days is considered an [idle cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters#how-idle-clusters).  | Scale down your cluster to save costs  
  
GKE doesn't send recommendations for clusters that were created less than 30 days ago.

## Understand cost or savings estimates

If possible, GKE's recommendation includes an estimate that projects the monthly cost or savings if you rightsized the cluster. This estimate is derived from the cluster costs over the past 30 days.

Any estimated costs or savings are projections based on previous spending, and are not a guarantee of future cost or savings.

To see these estimates, ensure that you have the required `billing.accounts.getSpendingInformation` permission to get spending information. For more information, see [Cloud Billing access](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing-access).

To get more information about the cost of all of your GKE clusters, including a more granular breakdown based on namespaces and workloads, see [Get key spending insights for your GKE resource allocation and cluster costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

For more information about the costs of running a GKE cluster, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Considerations when rightsizing clusters

Before you follow a recommendation to scale up or down a cluster, consider the following:

  * Review the resource utilization of applications running on your cluster to see how they're performing, and if they're using more or less CPU and memory than expected. For instructions, see [Analyze resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#get-resource-recommendations).
  * Batch processing workloads might intentionally maintain high utilization of cluster resources for cost efficiency. If the allocated cluster resources are sufficient for the batch jobs running on the cluster, you don't need to scale up the highly utilized cluster, which was identified as underprovisioned.



## Implement the recommendation to rightsize a cluster

Review the following to understand how you can adjust the size of a cluster to better match your resource utilization.

### Rightsize an underprovisioned cluster

To implement the recommendation to minimize the risk of reliability by rightsizing an underprovisioned cluster, increase resources on the cluster. You can do so by taking some of the following actions:

  * Enable [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning), or adjust the settings to allow for greater scaling up.
  * Horizontally scale up your cluster by increasing the number of nodes. Follow the instructions to [horizontally scale by changing the node count](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#resizing_a_node_pool).
  * Choose a larger machine type for your node pools. Follow the instructions to [vertically scale by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes).
  * Monitor and review the CPU and memory resource usage of applications that run on your cluster. See if you can scale down applications. For instructions about monitoring resource usage, see [Analyze resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#get-resource-recommendations).



When you implement this recommendation, you ensure that your cluster remains reliable because it has the appropriate amount of resources for its applications.

### Rightsize an overprovisioned cluster

To implement the recommendation to save costs by rightsizing an overprovisioned cluster, decrease resources on the cluster. Adjust cluster CPU and memory allocations to match your workload needs. You can do so by taking some of the following actions:

  * Adjust [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) to more aggressively scale down underutilized resources.
  * Horizontally scale down your cluster by decreasing the number of nodes. Follow the instructions to [horizontally scale by changing the node count](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#resizing_a_node_pool).
  * Choose a smaller machine type for your node pools. Follow the instructions to [vertically scale by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes).
  * Monitor and review the CPU and memory resource usage of applications that run on your cluster. See if you can scale up applications. For instructions about monitoring resource usage, see [Analyze resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#get-resource-recommendations).



When you implement this recommendation, you ensure that you're not using more resources than necessary to run your cluster's applications.

## What's next

  * [View cost-related optimization metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics)
  * [Reducing costs by scaling down GKE clusters during off-peak hours](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/reducing-costs-by-scaling-down-gke-off-hours)
  * [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders)
  * [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke)
  * [5 GKE features to help you optimize your clusters](https://cloud.google.com/blog/products/containers-kubernetes/boost-your-gke-game-with-these-tips-and-tutorials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
