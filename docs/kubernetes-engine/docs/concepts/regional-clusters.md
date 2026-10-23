---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters/
title: Regional clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:24.431871+00:00
---

# Regional clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Regional clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how regional clusters work in Google Kubernetes Engine (GKE).

Regional clusters increase the availability of a cluster by replicating the control plane across multiple zones in a [region](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones).

This configuration provides the following benefits:

  * **Resilience from single zone failure:** Regional clusters are available across a _region_ rather than a single zone within a region. If a single zone becomes unavailable, your control plane is not impacted.
  * **Continuous control plane upgrades, control plane resizes, and reduced downtime from control plane failures**. With redundant replicas of the control plane, regional clusters provide higher availability of the Kubernetes API, so you can access your control plane even during upgrades.



Also, by default, regional clusters are created as [multi-zonal clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#multi-zonal_clusters), so worker nodes are distributed across multiple zones in a region. This increases the availability of your workload, if you run sufficient replicas of the workload.

GKE Autopilot clusters are always regional. If you use GKE Standard, you can choose to create regional or zonal clusters. To learn about the different cluster availability types, see [Cluster availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#availability).

In regional clusters, including Autopilot clusters, the control plane is replicated across multiple zones of a region. GKE automatically replicates nodes across zones in the same region. In Standard clusters and node pools, you can optionally manually specify the zone(s) in which the nodes run. All zones must be within the same region as the control plane.

**Note:** Use regional clusters to run your production workloads, as they generally offer higher availability than zonal clusters. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

After creating a regional cluster, you cannot change it to a zonal cluster.

## How regional clusters work

Regional clusters replicate the cluster's control plane and nodes across multiple zones within a single [region](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available). For example, using the default configuration, a regional cluster in the `us-east1` region creates multiple replicas of the control plane in different `us-east1` zones and provisions nodes in three `us-east1` zones: `us-east1-b`, `us-east1-c`, and `us-east1-d`. In the event of an infrastructure outage, Autopilot workloads continue to run and GKE automatically rebalances nodes. If you use Standard clusters, you must rebalance nodes manually or by using the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

### Limitations

  * The default node pool created for regional Standard clusters consists of nine nodes (three per zone) spread evenly across three zones in a region. This consumes nine IP addresses for clusters using public nodes. You can reduce the number of nodes down to one per zone, if needed. Newly created Cloud Billing accounts are granted only eight IP addresses per region, so you may need to [request an increase in your quotas](https://docs.cloud.google.com/compute/quotas) for regional in-use IP addresses, depending on the size of your regional cluster. If you have too few available in-use IP addresses, cluster creation fails.

  * To run [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) in your regional cluster, choose a region that has at least one zone where the requested GPUs are available. You must use the [`--node-locations`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create) flag when creating the node pool to specify the zone or zones containing the requested GPUs.

If the region you choose doesn't have at least one zone where the requested GPUs are available, you might see an error like the following:
        
        ERROR: (gcloud.container.clusters.create) ResponseError: code=400, message=
            Accelerator type "nvidia-l4" does not exist in zone europe-west3-a.
        

For a complete list of regions and zones where GPUs are available, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

  * Zones for Standard mode node pools must be in the same region as the cluster's control plane. If you need to, you can [change a cluster's zones](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#add_or_remove_zones), which causes all new and existing nodes to span those zones.




### Pricing

All Autopilot clusters are regional, and are subject to the [Autopilot pricing model](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode).

In Standard mode, regional clusters require more of your project's [regional quotas](https://docs.cloud.google.com/kubernetes-engine/quotas) than a similar zonal or multi-zonal cluster. Ensure that you understand your quotas and [Standard pricing](https://cloud.google.com/kubernetes-engine/pricing#standard_mode) before using regional clusters. If you encounter an `Insufficient regional quota to satisfy request for resource` error, your request exceeds your available quota in the current region.

Also, you are charged for node-to-node traffic across zones. For example, if a workload running in one zone needs to communicate with a workload in a different zone, the cross-zone traffic incurs cost. For more information, see [Egress between zones in the same region (per GB)](https://docs.cloud.google.com/vpc/network-pricing#general) in the Compute Engine pricing page.

## Persistent storage in regional clusters

Zonal persistent disks are zonal resources and regional persistent disks are multi-zonal resources. When adding [persistent storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps#requesting_persistent_storage_in_a_statefulset) unless a zone is specified, GKE assigns the disk to a single, random zone. To learn how to control the zones, see [Zones in persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#pd-zones).

## Autoscaling regional clusters

Keep the following considerations in mind when using the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to automatically scale node pools in regional Standard mode clusters.

You can also learn more about [Autoscaling limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_limits) for regional clusters or about how Cluster Autoscaler [balances across zones](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#balancing_across_zones).

These considerations only apply to Standard mode clusters with the cluster autoscaler.

### Overprovisioning scaling limits

To maintain capacity in the unlikely event of zonal failure, you can allow GKE to overprovision your scaling limits, to ensure a minimum level of availability even when some zones are unavailable.

For example, if you overprovision a three-zone cluster to 150% (50% excess capacity), you can ensure that 100% of traffic is routed to available zones if one-third of the cluster's capacity is lost. In the preceding example, you would accomplish this by specifying a maximum of six nodes per zone rather than four. If one zone fails, the cluster scales to 12 nodes in the remaining zones.

Similarly, if you overprovision a two-zone cluster to 200%, you can ensure that 100% of traffic is rerouted if half of the cluster's capacity is lost.

You can learn more about the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) or read the [FAQ for autoscaling](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md) in the Kubernetes documentation.

## What's next

  * [Create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
  * Learn more about the different [types of clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * [Learn more about node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
  * [Learn more about cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
