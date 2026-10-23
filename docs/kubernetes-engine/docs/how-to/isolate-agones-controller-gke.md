---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-agones-controller-gke/
title: Isolate the Agones controller in your GKE cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:49.646522+00:00
---

# Isolate the Agones controller in your GKE cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-agones-controller-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Isolate the Agones controller in your GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

[Agones](https://agones.dev/site/docs/overview/) is an open source library for hosting, running, and scaling dedicated game servers on Kubernetes. When you run a production deployment of Agones in your Google Kubernetes Engine (GKE) cluster, it is a [best practice](https://agones.dev/site/docs/guides/best-practices/#separation-of-agones-from-gameserver-nodes) to run the Agones controller in a dedicated node pool for better isolation and resiliency. This is best suited for production workloads or cost-optimized workloads.

GKE monitors your clusters and uses the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview) to deliver guidance for how you can optimize your usage of the platform. The _Agones Recommender_ for GKE identifies clusters where you should isolate the Agones controller.

To learn more about how to manage insights and recommendations from Recommenders, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

## Identify clusters where you can isolate the Agones controller

The insights from the _Agones Recommender_ identify which clusters contain an Agones controller that should be isolated in a dedicated node pool.

To get these insights, follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) using the Google Cloud console, the Google Cloud CLI, or the Recommender API with the `AGONES_DEDICATED_NODE_POOL_NEEDED` subtype.

After you identify the clusters, you can implement the recommendation to create a dedicated node pool.

## How GKE Agones Recommender detects clusters

The Recommender generates an insight and recommendation if the following criteria are true for a GKE cluster:

  * The cluster is running an Agones controller. This is determined if any Pods have the `agones.dev/role:controller` label set.
  * The cluster has more than four nodes, which is an indicator that the cluster might be running a production workload.
  * The Agones controller is not running on the dedicated node for Agones. A dedicated node pool is considered to be one that has the following node label `agones.dev/agones-system=true` and node taint `agones.dev/agones-system=true:NoExecute`.



## Implement the recommendation to create a dedicated node pool

If you've received an insight and recommendation for your cluster and want to use a dedicated node pool for your Agones controller, follow the instructions to [create a dedicated node pool](https://agones.dev/site/docs/installation/creating-cluster/gke/#optional-creating-a-dedicated-node-pool) where your Agones controller can be scheduled.

The Recommender runs once daily so it might take up to 24 hours for the recommendation to resolve after changes have been implemented.

If you don't want to implement the recommendation, you can [dismiss it](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#dismiss-recommendation).

## What's next

  * [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders)
  * [Create a GKE cluster for your Agones install](https://agones.dev/site/docs/installation/creating-cluster/gke/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
