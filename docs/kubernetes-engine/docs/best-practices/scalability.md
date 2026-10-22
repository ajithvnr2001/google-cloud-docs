---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/scalability/
title: Best practices for GKE scalability \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:26.079855+00:00
---

# Best practices for GKE scalability  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/scalability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for GKE scalability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides a set of recommendations for planning, architecting, deploying, scaling, and operating large workloads on Google Kubernetes Engine (GKE) clusters. We recommend you follow these recommendations to keep your scaling workloads within [service-level objectives (SLOs)](https://landing.google.com/sre/sre-book/chapters/service-level-objectives). For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## Available recommendations for scalability

Before planning and designing a GKE architecture, map parameters specific to your workload (for example the number of active users, expected response time, required compute resources) with the resources used by Kubernetes (such as Pods, Services, and 'CustomResourceDefinition'). With this information mapped, review the GKE scalability recommendations.

The scalability recommendations are divided based in the following planning scopes:

  * **Plan for scalability** : To learn about the general best practices for designing your workloads and clusters for reliable performance when running on both small and large clusters. These recommendations are useful for architects, platform administrators, and Kubernetes developers. To learn more, see [Plan for scalability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-scalability).
  * **Plan for large-size GKE clusters** : To learn how to plan to run very big-size GKE clusters. Learn about known limits of Kubernetes and GKE and ways to avoid reaching them. These recommendations are useful for architects and platform administrators. To learn more, see [Plan for large GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters).
  * **Plan for large workloads** : To learn how to plan architectures that run large Kubernetes workloads on GKE. It covers recommendations for distributing the workload among projects and clusters, and adjusting these workload required quotas. These recommendations are useful for architects and platform administrators. To learn more, see [Plan for large workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-workloads).



These scalability recommendations are general to GKE and are applicable to both GKE Standard and GKE Autopilot modes. GKE Autopilot provisions and manages the cluster's underlying infrastructure for you, therefore some recommendations are not applicable.

**Caution:** Test your planned cluster configuration before its implementation. Some design decisions might include fixed parameters, for example, CIDRs definition. Changing these parameters on existing clusters is not available and it requires cluster recreation.

## What's next?

  * [Plan for scalability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-scalability).
  * [Plan for large GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters)
  * [Plan for large workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-workloads)
  * See our episodes about [building large GKE clusters](https://www.youtube.com/watch?v=542XwAPKh4g).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
