---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/enhance-kubernetes-ha/
title: Kubernetes workloads for high availability \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:29:38.495867+00:00
---

# Kubernetes workloads for high availability  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/enhance-kubernetes-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Kubernetes workloads for high availability Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document recommends Kubernetes container workload strategies to make your applications more fault tolerant in a Google Distributed Cloud (GDC) air-gapped multi-zone universe. GDC supports Kubernetes-native container applications that are widely consumed and supported on Google Kubernetes Engine (GKE).

The strategies in this document are intended for application developers who are responsible for creating resilient workloads.

For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Kubernetes considerations for HA apps

Achieving high availability (HA) in Kubernetes goes beyond just the control plane. You must also design and deploy container workloads in your Google Distributed Cloud (GDC) air-gapped universe resiliently. Kubernetes offers several powerful mechanisms to minimize downtime and provide highly available services even when facing infrastructure issues or during routine maintenance. The following topics are key strategies to consider for HA:

**Important:** To access the URLs listed on this page, you must connect to the internet. The URLs are provided to access outside of your air-gapped environment.

  * **Maintain availability with replicas and autoscaling** : ensure your application has enough running instances to handle its latency demand and survive individual pod failures.

    * **Pod replicas** : maintain a stable set of identical pod replicas. If a pod fails, the `ReplicaSet` controller automatically creates a new pod to replace it. For more information, see the [Kubernetes `ReplicaSet` documentation](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/).

    * **Horizontal Pod Autoscaler (HPA)** : automatically adjust the number of replicas based on metrics like CPU utilization, letting your application handle traffic spikes. For more information, see the [Kubernetes HPA documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

  * **Minimize downtime with`PodDisruptionBudget` (PDB)**: use a PDB to limit the number of pods that can be down simultaneously during voluntary disruptions, such as node maintenance. This strategy ensures a minimum level of availability. For more information, see the [Kubernetes PDB documentation](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

  * **Spread risk with anti-affinity rules** : use pod anti-affinity to ensure that multiple replicas of the same application aren't scheduled on the same node. This strategy prevents a single infrastructure failure from taking down all replicas. For more information, see the [Kubernetes affinity documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity).

  * **Health checks with probes** : implement liveness, readiness, and startup probes to help Kubernetes detect and recover from unhealthy pods. Probes ensure that traffic only reaches pods capable of handling it. For more information, see the [Kubernetes probe documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

  * **Stable endpoints with services** : use Kubernetes `Service` objects to provide a stable IP address and DNS name for your pods, decoupling clients from individual pod lifecycles and providing internal load balancing. For more information, see the [Kubernetes Services documentation](https://kubernetes.io/docs/concepts/services-networking/service/).

  * **Graceful updates and rollbacks with deployments** : use Kubernetes `Deployment` objects to provide graceful updates and rollbacks for your container workloads. For more information, see [Kubernetes Deployment documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment).

  * **Set resource requests and limits** : define the CPU and memory resources required for your containers. These specifications help the Kubernetes scheduler effectively place pods to prevent resource contention from affecting availability. For more information, see the [Kubernetes resource management documentation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).




## What's next

  * [Kubernetes concepts for GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/get-started-with-kubernetes)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)
  * [Create a cluster to run container workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-user-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
