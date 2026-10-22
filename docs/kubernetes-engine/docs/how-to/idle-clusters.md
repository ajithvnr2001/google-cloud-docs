---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters/
title: Identify idle GKE clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:51.860449+00:00
---

# Identify idle GKE clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Identify idle GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how you can identify idle Google Kubernetes Engine (GKE) Standard clusters using insights and recommendations. After you verify that the identified idle clusters are unused, you can delete them to save costs. If possible, the recommendation includes projected monthly savings for deleting a cluster. For more information, see Understand cost estimation for idle clusters.

GKE provides insights and recommendations for cost optimization scenarios such as idle clusters, overprovisioned workloads or clusters, and reliability improvement scenarios such as underprovisioned workloads or clusters. GKE provides corresponding recommendations to scale up or down the workloads or clusters, or delete the clusters. For more information about scenarios other than idle clusters, see [Identify underprovisioned and overprovisioned GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization), and [Identify underprovisioned and overprovisioned workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization).

GKE doesn't provide insights for Autopilot clusters, which incur minimal operational costs as you only pay for the resources that your workloads request. For more information, see [Autopilot Pricing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#pricing).

GKE monitors your clusters and delivers guidance to optimize your usage through [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist), a service that provides recommenders that generate insights and recommendations for using resources on Google Cloud.

For more information about how to manage insights and recommendations, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

## Identify idle clusters

To identify idle clusters, [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) using the Google Cloud console, the Google Cloud CLI, or the Recommender API. Use the insight subtypes shown in the table in the following section and the `CLUSTER_IDLE` recommendation subtype. In the console, these insights appear in the **Cost Optimization** tab on the **Clusters** page.

After you identify idle clusters, see the considerations when deleting idle clusters.

## How GKE identifies idle clusters

GKE uses utilization signals to determine whether you receive an insight and recommendation.

The following table describes the signals that GKE uses and the threshold for each signal. Each signal triggers an independent insight. If a cluster has multiple insights, GKE displays a single recommendation.

Insight subtype | Signal | Observation period | Details  
---|---|---|---  
`CLUSTER_IDLE_NO_RUNNING_PODS` | No running customer Pods | Last 30 days |  There are zero Pods in the `Running` state outside of the `kube-system` and `gmp-system` namespace in the cluster metrics events logs for the cluster during the last 30 days.   
`CLUSTER_IDLE_NO_NODES` | No nodes or node pools | Last 30 days |  There are zero nodes or zero node pools in the cluster metrics events logs for the cluster during the last 30 days.   
`CLUSTER_IDLE_LOW_CPU_UTILIZATION` | Low CPU utilization and no new Pods | Last 30 days |  A GKE cluster is idle with low CPU utilization when _both_ of the following are true: 

  * CPU utilization consistently averages under 7% during every hour, over the last 30 days.
  * Active Pod count remains unchanged over the last 30 days.

  
  
GKE doesn't send recommendations for clusters that were created less than 30 days ago.

## Understand cost estimation for idle clusters

If possible, GKE includes with the recommendation an estimated monthly cost of the idle cluster, projecting how much money you'd save each month if you deleted the cluster. This estimate is derived from the cluster costs over the past 30 days.

Any estimated savings are projections based on previous spending, and are not a guarantee of future cost or savings.

To see these estimates, ensure that you have the required `billing.accounts.getSpendingInformation` permission to get spending information. For more information, see [Cloud Billing access](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing-access).

To get more information about the cost of all of your GKE clusters, including a more granular breakdown based on namespaces and workloads, see [Get key spending insights for your GKE resource allocation and cluster costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

For more information about the costs of running a GKE cluster, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Considerations when deleting idle clusters

Before you delete a cluster that GKE determines is idle, consider the following possibilities:

  * Does anyone use the cluster? For example, a cluster might be intentionally idle if its purpose is to maintain failover capacity.
  * Should the cluster be scaled down instead of deleted? For example, a cluster running a useful workload might have low utilization and be identified as idle because more resources were provisioned than necessary.



## Implement the recommendation to delete idle clusters

If you've received an insight and recommendation that you have an idle cluster that can be deleted and have ruled out the considerations for keeping the cluster running, follow the instructions in the recommendation and delete the cluster.

## What's next

  * [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).
  * [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
