---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization/
title: Identify underprovisioned and overprovisioned workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:14.756245+00:00
---

# Identify underprovisioned and overprovisioned workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Identify underprovisioned and overprovisioned workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to identify underprovisioned and overprovisioned workloads that run on Google Kubernetes Engine (GKE) clusters by using insights and recommendations. After you verify that the identified workloads would benefit from the recommendation to scale up or down, you can make the recommended change to save costs or increase the reliability of your workload. If possible, the recommendation includes projected monthly savings or cost. For more information, see Understand cost or savings estimates.

GKE provides these insights about workloads running on both Autopilot and Standard clusters. GKE also provides similar recommendations for entire clusters. For more information, see [Identify underprovisioned and overprovisioned GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-cluster-utilization).

GKE monitors your clusters and delivers guidance to optimize your usage through [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist), a service that provides recommenders that generate insights and recommendations for using resources on Google Cloud. For more information about how to manage insights and recommendations, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

## Get insights and recommendations for underprovisioned and overprovisioned workloads

You can receive these insights and recommendations through the Google Cloud CLI or the Recommender API. Follow the respective instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) and filter using the `WORKLOAD_UNDERPROVISIONED` and `WORKLOAD_OVERPROVISIONED` subtypes.

After you identify underprovisioned or overprovisioned workloads, see the considerations when rightsizing workloads.

## How GKE identifies underprovisioned and overprovisioned workloads

The following table describes the signals that GKE uses for identifying underprovisioned and overprovisioned workloads that can be scaled up or down, and the threshold for each signal. Additionally, this table shows the action that we recommend that you take in this scenario.

Subtype | Signal | Observation period | Details | Recommendation  
---|---|---|---|---  
`WORKLOAD_UNDERPROVISIONED` | CPU or memory usage is high | Last 15 days | A workload is underprovisioned when CPU or memory utilization is greater than 150% for at least 10% of the time over the last 15 days. | Scale up your workload to increase reliability  
`WORKLOAD_OVERPROVISIONED` | CPU or memory usage is low | Last 15 days |  A workload is overprovisioned when CPU or memory utilization is less than 50% for at least 90% of the time over the last 15 days.  | Scale down your workload to save costs  
  
GKE also uses the following guidelines to determine when to provide insights and recommendations:

  * GKE doesn't generate recommendations for the target metric of horizontal Pod autoscaling (HPA) because using this metric can cause interference.
  * If vertical Pod autoscaling (VPA) is enabled, the request values are automatically managed and GKE doesn't need to generate a recommendation.
  * GKE might wait up to three days before generating recommendations for new workloads.



## Understand cost or savings estimates

If possible, GKE's recommendation includes an estimate that projects the monthly cost or savings if you rightsized the workload. This estimate is derived from the workload costs, based on the weighted average of the request values combined with the CPU and memory cost of the workload over the past 30 days.

Any estimated costs or savings are projections based on previous spending, and are not a guarantee of future cost or savings.

To see these estimates, ensure that the following is true:

  * You have the required `billing.accounts.getSpendingInformation` permission to get spending information. For more information, see [Cloud Billing access](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing-access).
  * GKE cost allocation is enabled for the cluster. For more information, see [Enable GKE cost allocation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations#enable_breakdown).



For more information about the cost of all of your GKE clusters, including a more granular breakdown based on namespaces and workloads, see [Get key spending insights for your GKE resource allocation and cluster costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

For more information about the costs of running a GKE cluster, see [GKE pricing](https://docs.cloud.google.com/kubernetes-engine/pricing).

## Considerations when rightsizing workloads

Before you follow a recommendation to scale up or down a workload, consider the following:

  * Review the resource utilization of the workload to see how it's performing, and if it's using more or less CPU and memory than expected. For instructions, see [Analyze resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#get-resource-recommendations).
  * Batch processing workloads might intentionally maintain high utilization for cost efficiency. If the allocated resources are sufficient for the batch jobs, you don't need to scale up the highly utilized workload, which was identified as underprovisioned.
  * GKE has limited visibility into the actual memory usage of Java Virtual Machine (JVM)-based workloads. Use extra scrutiny before applying recommendations for these types of workloads.



## Implement the recommendation to rightsize a workload

You can adjust the size of a workload to better match the workload's resource utilization by doing either of the following:

  * Enable [vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) for the workload. For more information, see [Set Pod resource requests automatically](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#update-requests-automatically).
  * Change the requests and limits [manually](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#set-requests-manually) according to the recommendation:

    * **Underprovisioned workload** : to implement the recommendation to rightsize an underprovisioned workload, increase the resource requests and limits for the workload. When you implement this recommendation, you help to ensure that your workload remains reliable because it has the appropriate amount of resources for its applications.
    * **Overprovisioned workload** : to implement the recommendation to rightsize an overprovisioned workload, decrease the resource requests and limits for the workload. Adjust cluster CPU and memory allocations to match your workload needs. When you implement this recommendation, you help to ensure that you use only the resources that you need to run your workload.



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
