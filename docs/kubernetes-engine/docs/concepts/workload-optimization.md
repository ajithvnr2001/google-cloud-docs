---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-optimization/
title: Optimize for workloads on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:25.103872+00:00
---

# Optimize for workloads on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Optimize for workloads on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how GKE generates optimizations to improve the performance of specific workloads, and how the optimized configurations are applied to the cluster and workload.

To recommend optimized configurations, the Google Cloud CLI command [`gcloud container workload profiles manifests create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/workload/profiles/manifests/create) generates Kubernetes manifests. These manifests can provide optimized application-level and node-level configurations, which can improve the performance of Redis and MySQL workloads. For the steps to optimize these specific workloads, see the following:

  * For MySQL workloads, see [Optimize MySQL workload performance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-mysql).

  * For Redis workloads, see [Optimize Redis workload performance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-redis).




## How workload optimization works

To improve workload performance, the Google Cloud CLI command `gcloud container workload profiles manifests create` generates Kubernetes manifests with recommended application-level and node-level configurations.

The generated manifests come in the form of ConfigMaps for application-level configurations, and ComputeClasses for node-level configuration. Once you apply the manifests, your workloads can reference the manifests to use the optimized configurations.

The ConfigMaps contain configuration that your application understands. For example, for Redis, the Google Cloud CLI command creates a [`redis.conf` file](https://redis.io/docs/latest/operate/oss_and_stack/management/config/). The ComputeClasses instruct GKE on what type of nodes to provision for your workloads.

The recommended optimizations are based on specific use cases, as well as your current configurations.

## How optimizations are referenced by your workloads

To take advantage of the optimized configurations provided by Workload Optimization, your Pod needs to reference them. Application-level optimizations (ConfigMaps) are mounted to your Pod as a volume. The mounted file can then be referenced by your application at startup time.

Node-level optimizations (ComputeClasses) are referenced in your Pod's `nodeSelector` field.

## What's next

  * To optimize for MySQL workloads, see [Optimize MySQL workload performance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-mysql).
  * To optimize for Redis workloads, see [Optimize Redis workload performance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-redis).
  * Learn more about [GKE ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
