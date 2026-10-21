---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/identify-clusters-autopilot-migration/
title: Identify clusters for Autopilot migration \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:53.065515+00:00
---

# Identify clusters for Autopilot migration  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/identify-clusters-autopilot-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Identify clusters for Autopilot migration Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to potentially reduce your cluster operating costs by identifying Google Kubernetes Engine (GKE) Standard clusters with underutilized nodes that would benefit from a migration to GKE Autopilot.

## Potential cost savings in Autopilot

In GKE Standard clusters, you're billed for the Compute Engine virtual machine (VM) infrastructure that backs each node, regardless of how efficiently your running workloads _use_ the compute resources. Continually managing your resource usage using efficient resource consumption methods such as _bin-packing_ is essential to run cost-efficient Standard clusters.

In Autopilot, you're billed for the compute resources, such as CPU or memory, that your running workloads request. This billing model removes the need for you to monitor and manage workload resource usage efficiency. For detailed pricing information, see [Autopilot mode pricing](https://cloud.google.com/kubernetes-engine/pricing#autopilot-mode).

GKE monitors your running Standard clusters to detect node underutilization and recommends migrating to Autopilot clusters if the migration would potentially reduce your operating costs. GKE provides these recommendations through [Recommender](https://docs.cloud.google.com/recommender/docs/overview), a service that provides insights and recommendations for using resources on Google Cloud.

## Identify underutilized Standard clusters

GKE generates insights and recommendations that help you to identify underutilized Standard clusters. To view these insights, use the Google Cloud console, the gcloud CLI, or the Recommender API and specify the following parameters:

  * **Recommender type:** `google.container.DiagnosisInsight`
  * **Subtype** : `CLUSTER_AUTOPILOT_OPTIMIZATION`



For instructions, see [View insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

## How GKE identifies clusters for potential Autopilot migration

GKE uses the following signals to determine whether a Standard mode cluster is underutilized. The cluster must satisfy the following signal for GKE to generate an insight:

Signal | Description | Threshold  
---|---|---  
CPU bin-packing score | The amount of node CPU requested by running workloads as a percentage of the total available CPU on the node. | <55%  
  
### Decide whether to migrate to Autopilot

Autopilot clusters shift node management responsibilities to GKE. Before you migrate your workloads to an Autopilot cluster, review the following resources to decide whether Autopilot fits your configurability and functionality needs:

  * [High-level comparison of cluster modes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [Detailed comparison of Autopilot and Standard](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison)
  * [Autopilot security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security)
  * [About GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)



In most production environments, we recommend Autopilot clusters.

### Limitations

If recent metrics from a GKE Standard cluster aren't available, you might not see an insight for that cluster.

## Act on the recommendation

If you see this recommendation, contact Cloud Customer Care for more information about how your environment might benefit from a migration to Autopilot clusters. Contact your account representative or see [contact Cloud Customer Care](https://cloud.google.com/contact).

If you decide to migrate from Standard, check workload compatibility with Autopilot and prepare for a migration by following the guidance in [Prepare to migrate to Autopilot form Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-migrate-cluster-mode).

## What's next

  * [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
