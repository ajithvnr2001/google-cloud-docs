---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volume-attach-limits/
title: Persistent volume attach limits for GKE nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:01.937789+00:00
---

# Persistent volume attach limits for GKE nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volume-attach-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Persistent volume attach limits for GKE nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document helps you understand how persistent volume attach limits for Compute Engine Persistent Disks and Hyperdisks work on Google Kubernetes Engine (GKE) nodes. For proper workload scheduling and node pool sizing it's crucial for you to understand the maximum number of persistent volumes that can be attached to a GKE node. If you want greater control over workload scheduling, especially when you use multiple disk types with varying attach limits on a single instance, you can use a node label to override the default attach limits.

This document is for Storage specialists who create and allocate storage, and GKE administrators who manage workload scheduling and node pool sizing. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE Enterprise user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

In GKE, when you request a PersistentVolume (PV) using the [Compute Engine Persistent Disk CSI driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) (`pd.csi.storage.gke.io`), a block storage volume is provisioned from the Google Cloud Persistent Disk service.

When you [enable the Compute Engine Persistent Disk CSI driver (PDCSI)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_an_existing_cluster) on GKE clusters, the PDCSI driver calculates and reports the per-node persistent volume attach limit to the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/). Based on this information, the Kubernetes scheduler makes scheduling decisions to help ensure that it doesn't schedule too many Pods that require persistent volumes on a node that has reached its attachment capacity. If the PDCSI driver reported inaccurate attach limits, more specifically a number higher than the actual limit, the Pods will fail to get scheduled, getting stuck in a `Pending` state. This can happen on third generation machine types such as, C3, which have different attach limits for Hyperdisks and Persistent Disks.

## Understand persistent volume attach limits

For machine generations older than the fourth, Compute Engine PDCSI driver sets an _aggregate_ persistent volume attach limit of 128 disks (127 data disks plus one boot disk) across all machine types. The attach limit applies to both Persistent Disk and Hyperdisk volumes combined. For Hyperdisk, the attach limit is determined by the underlying Compute Engine machine type, the number of vCPUs the machine has, and the specific Hyperdisk type.

For example:

  * For the fourth generation machine types like [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series), the PDCSI driver accurately reports a default attach limit to Kubernetes that's _calculated based on the node's vCPU count_. The reported attach limit typically falls within a range of [8-128 persistent volumes](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4).
  * In contrast, for the third generation machine types like [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series), the PDCSI driver reports a default attach limit to Kubernetes as the _fixed limit of 128 disks_ , which can lead to Pod scheduling failure because the actual limit can be lower than 128 based on the vCPU count.



You can override the default attach limit by using a node label.

Refer to the following helpful resources in the Compute Engine documentation:

  * For the available generations of Compute Engine machines, see the table in the [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) section.
  * For the list of machine types and their compatible Persistent Disk types, see [Machine series support](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pd-machine-series).
  * To know the maximum supported Hyperdisk attach limits based on different CPU counts of different Hyperdisk types, see [Maximum Hyperdisk volumes per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#max-total-disks-per-vm).
  * To understand how the Hyperdisk attach limits are applied to a node, see [Summary of Hyperdisk per-VM limits.](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#per-vm-limits-summary).



## Override the default persistent volume attach limit

If you have specific requirements or node configurations where you want to attach a specific number of persistent volumes to your nodes, you can override the default persistent volume attach limit for a node pool by using the following node label: `node-restriction.kubernetes.io/gke-volume-attach-limit-override: VALUE`.

You can use this node label on the following GKE versions:

  * `1.32.4-gke.1698000` and later.
  * `1.33.1-gke.1386000` and later.

**Note:** You can set only one attach limit per node pool. The attach limit applies to all the nodes in that node pool.

### New node pool

To create a new node pool with a specific persistent volume attach limit, run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --node-labels=node-restriction.kubernetes.io/gke-volume-attach-limit-override=VALUE
    

### Existing node pool

To modify current persistent volume attach limit of an existing node pool, follow these steps:

  1. Update the attach limit on the node pool:
         
         gcloud container node-pools update NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --node-labels=node-restriction.kubernetes.io/gke-volume-attach-limit-override=VALUE
         

  2. Restart the `pdcsi-node` DaemonSet:
         
         kubectl rollout restart ds pdcsi-node -n kube-system
         

The new attach limit applies after the `pdcsi-node` Pods are in `Running` state.




Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool you want to create or update.
  * `CLUSTER_NAME`: the name of the cluster for the node pool you want to create or update.
  * `VALUE`: an integer between `0` and `127` to specify the new number of persistent volumes that can be attached. If you specify a value higher than 127, the node label is ignored and the PDCSI driver uses the default persistent volume attach limit instead. The default limit is 128 for third generation machines and a vCPU count-based value for fourth generation machines.



### Verify the override

To verify if the override was applied correctly, check the node labels and the node capacity.

In the following commands, replace `NODE_NAME` with the name of a node that is part of the specific node pool where you applied the override node label.

  1. Check the node labels:
         
         kubectl get node NODE_NAME --show-labels
         

The output should include the label `node-restriction.kubernetes.io/gke-volume-attach-limit-override`.

  2. Check the node capacity:
         
         kubectl describe node NODE_NAME
         

The output should include the `attachable-volumes-gce-pd` capacity, which should match the override value you set for the node pool. For more information, see [Check allocatable resources on a node](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#check_allocatable_resources_on_a_node).




## What's next

  * [Learn about the GKE persistent volume storage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).
  * [Learn how the Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) works.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
