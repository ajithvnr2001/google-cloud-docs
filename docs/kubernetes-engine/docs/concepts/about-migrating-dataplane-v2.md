---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-migrating-dataplane-v2/
title: About migrating to GKE Dataplane V2 \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:11.478410+00:00
---

# About migrating to GKE Dataplane V2  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-migrating-dataplane-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About migrating to GKE Dataplane V2 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Before you migrate your existing Google Kubernetes Engine (GKE) clusters from Dataplane V1 to GKE Dataplane V2, use this document to check whether your clusters are eligible, learn what happens during migration, and plan for workload disruption.

As a Platform admins and operators or Networking specialists, use this overview to plan your migration strategy. To perform the migration, see [Migrate an existing cluster to GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-dataplane-v2).

## Benefits of migrating

After you migrate to GKE Dataplane V2, you will gain the [scalability, security, and operational advantages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#advantages) it provides.

  * **Enforce network policies in place** : apply Cilium-based network policies to your existing cluster without moving workloads to a new cluster.
  * **Troubleshoot network issues faster** : debug network flows by using built-in GKE Dataplane V2 metrics and events.

**Caution:** You can't revert a cluster to Dataplane V1 after you migrate.

## Check whether your cluster is eligible

Before you migrate, verify that your cluster meets the following requirements:

  * **Routing type** : VPC-native. You can't migrate routes-based clusters.
  * **Cluster version** : 1.35.3-gke.1155000 or later.
  * **Node pool version** : 1.35.1-gke.1516000 or later.
  * **Istio version** : if you use Cloud Service Mesh or open source Istio, 1.23 or later. This version supports Container Network Interface (CNI) specification 1.1.0.



### Unsupported configurations

The following configurations are not supported in GKE Dataplane V2:

  * **Custom CNI plugins** : plugins that you install to replace the CNI plugin that GKE manages.
  * **Custom eBPF programs** : programs that you attach to managed interfaces. If you attach them before Cilium programs, they might prevent Cilium programs from running. If you attach them after Cilium programs, Cilium bypasses them.



To find these configurations in your cluster, check [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist) or the cluster details page for recommendations that might conflict with the migration.

## What happens during migration

Migration has four phases. GKE does most of the work, but some phases need action from you:

Phase | What GKE does | What you do  
---|---|---  
**Diagnose** | Monitors your cluster and flags unsupported configurations in Active Assist recommendations. | Review the recommendations and resolve flagged configurations.  
**Initiate** | — | Start the migration by updating your cluster by using a patch request. For more information, see [Migrate an existing cluster to GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-dataplane-v2).  
**Patch nodes** | Updates each Dataplane V1 node pool to use GKE Dataplane V2, following your maintenance windows and upgrade strategies. | Before you start, configure maintenance windows and upgrade strategies to control when and how your nodes update.  
**Finalize** | Patches the cluster to `ADVANCED_DATAPATH` after it updates all node pools. | No action required.  
  
### Plan for workload disruption

Because GKE recreates your nodes during migration, GKE reschedules your Pods onto the new nodes.

**Caution:** To reduce the impact on your workloads, schedule the migration during a period of low traffic.

## What's next

  * To migrate a cluster, see [Migrate an existing cluster to GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-dataplane-v2).
  * To understand how GKE Dataplane V2 works, see [About GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).
  * To troubleshoot network flows after you migrate, see [GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
