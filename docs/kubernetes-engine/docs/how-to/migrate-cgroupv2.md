---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2/
title: Migrate nodes to Linux cgroupv2 \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:53.877195+00:00
---

# Migrate nodes to Linux cgroupv2  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Migrate nodes to Linux cgroupv2 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Starting with version 1.33, Google Kubernetes Engine (GKE) migrates clusters running `cgroupv1` to `cgroupv2`. This page instructs you how to do the following:

  * Check which cgroup mode your cluster's nodes are running, and if your workloads might be affected by transitioning between cgroup modes.
  * Migrate GKE Autopilot cluster nodes or Standard cluster node pools to `cgroupv2`.
  * Temporarily opt out of GKE automatically migrating nodes using `cgroupv1` to `cgroupv2`. Follow these instructions if your cluster runs workloads which might be affected by transitioning between cgroup modes.



You can skip reading this page if you know that your workloads run as expected on `cgroupv2`, or aren't impacted by cgroup mode configuration. GKE automatically migrates clusters running `cgroupv1` to `cgroupv2` with version 1.33 and later.

## About Linux control groups

The kubelet and the container runtime use Linux kernel [control groups (cgroups)](https://www.wikipedia.org/wiki/Cgroups) for resource management, such as limiting how much CPU or memory each container in a Pod can access. There are two modes of the cgroup subsystem in the kernel: `cgroupv1` and `cgroupv2`. Kubernetes support for `cgroupv2` was introduced as alpha in Kubernetes version 1.18, beta in 1.22, and GA in 1.25. For more details, refer to the [Kubernetes cgroups v2 documentation](https://kubernetes.io/docs/concepts/architecture/cgroups/).

To learn about configuring a cgroup mode for Standard clusters, see [Linux cgroup mode configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#cgroup-mode-options).

## How GKE is transitioning to `cgroupv2`

Review the following timeline to understand how GKE is transitioning existing clusters to use `cgroupv2`:

  * For versions earlier than 1.26, `cgroupv1` was the default for nodes. For versions 1.26 or later, `cgroupv2` is the default for new nodes. There is no change to existing nodes. To learn more about which cgroup mode your GKE clusters run by default, see Check the cgroup mode of cluster nodes.
  * With minor version 1.31, GKE deprecates `cgroupv1`.
  * Starting with version 1.33, GKE migrates clusters running `cgroupv1` to `cgroupv2`. You can temporarily prevent this automatic migration by explicitly specifying that a node pool use `cgroupv1`.
  * With minor version 1.35, GKE removes support for `cgroupv1`.



For approximate timing of automatic upgrades to later minor versions such as 1.31 and 1.33, see the [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Check the cgroup mode of cluster nodes

The default cgroup mode depends on the type of cluster or node pool, and the version. With version 1.26 or later, the default is `cgroupv2`. With version 1.25 or earlier, the default is `cgroupv1`:

  * For Autopilot clusters and new Standard cluster node pools created with node auto-provisioning, the cgroup mode is based on the initial cluster version. You can't set the cgroup mode during Autopilot cluster creation. For new node auto-provisioned nodes, you can't set the mode differently from the default cgroup mode based on the minor version.
  * For Standard cluster node pools manually created without node auto-provisioning, the cgroup mode is based on the initial node pool version, or the customized node system configuration.



To check the cgroup mode, follow the instructions based on your cluster mode.

###  Autopilot 

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --format='value(nodePools[0].config.effectiveCgroupMode)'
    

Replace `CLUSTER_NAME` with the name of your cluster.

If the output is `EFFECTIVE_CGROUP_MODE_V2`, the cluster is running on `cgroupv2`. If the output is `EFFECTIVE_CGROUP_MODE_V1`, the cluster is running on `cgroupv1`.

GKE Autopilot clusters that were initially created with GKE version 1.25 or earlier run `cgroupv1` until you migrate them.

###  Standard 

With GKE Standard clusters, the cgroup mode is set at the node pool level. To check the mode for individual node pools, follow the instructions to [Verify cgroup configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#verify-cgroup). If your cluster's nodes are already using `cgroupv2`, no further action is necessary.

## Migrate nodes to `cgroupv2`

We recommend that you migrate existing nodes before GKE automatically migrates them in version 1.33 or later.

Do the following steps to migrate nodes running `cgroupv1`:

  1. Check the cgroup mode of the nodes. If your cluster's nodes are already using `cgroupv2`, no further action is necessary.
  2. Review the considerations about the migration, [Migrating to cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/#migrating-cgroupv2), to ensure that your workloads are prepared to use the new version of the API.
  3. Migrate the nodes for your cluster.

**Note:** When you run these commands to update the cgroup mode, GKE updates the nodes using the [surge upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) strategy. GKE initiates these operations to update node pools or groups of Autopilot nodes immediately in a sequential order without respecting [maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) configured for the cluster.

###  Autopilot 

Explicitly set your cluster's nodes to use `cgroupv2`:
         
         gcloud container clusters update CLUSTER_NAME \
             --autoprovisioning-cgroup-mode=v2
         

Replace `CLUSTER_NAME` with the name of your cluster.

###  Standard 

     1. If you use [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) for the cluster, run the following command to ensure that existing and future node pools created with node auto-provisioning use `cgroupv2`:
            
            gcloud container clusters update CLUSTER_NAME \
                --autoprovisioning-cgroup-mode=v2
            

Replace `CLUSTER_NAME` with the name of your cluster.

     2. For existing node pools created without node auto-provisioning, [update the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#update-node-pool) to add the following to the node system configuration:
            
            linuxConfig:
              cgroupMode: 'CGROUP_MODE_V2'
            

To learn more, see [Customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#editing_by_updating_an_existing_node_pool).

When you manually create new node pools without node auto-provisioning, GKE uses `cgroupv2` by default.




## Temporarily opt out of automatic migration to `cgroupv2`

To temporarily avoid automatic migration of nodes running `cgroupv1` to `cgroupv2` with minor versions 1.33 and later, you must explicitly set `cgroupv1`. You can also use these instructions to temporarily revert to `cgroupv1` if migrating nodes to `cgroupv2` caused an issue for your cluster's workloads.

**Note:** When you run these commands to update the cgroup mode, GKE updates the nodes using the [surge upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) strategy. GKE initiates these operations to update node pools or groups of Autopilot nodes immediately in a sequential order without respecting [maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) configured for the cluster.

###  Autopilot 

Run the following command for clusters that you originally created using version 1.25 or earlier. If your cluster was created running version 1.26 or later, you can't set the cgroup mode to `cgroupv1`.

Explicitly set your cluster's nodes to use `cgroupv1`:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --autoprovisioning-cgroup-mode=v1
    

Replace `CLUSTER_NAME` with the name of your cluster.

###  Standard 

To continue to run `cgroupv1` with a GKE Standard cluster node pool running version 1.33 or later, do the following steps:

  1. If you use [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning), and your cluster was created running version 1.25 or earlier, use the following command to ensure that existing and future node pools created with node auto-provisioning use `cgroupv1`. If your cluster was created running version 1.26 or later, you can't set the cgroup mode to `cgroupv1`:
         
         gcloud container clusters update CLUSTER_NAME \
             --autoprovisioning-cgroup-mode=v1
         

Replace `CLUSTER_NAME` with the name of your cluster.

  2. For existing Standard node pools, [update the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#update-node-pool) to add the following to the node system configuration:
         
         linuxConfig:
           cgroupMode: 'CGROUP_MODE_V1'
         

You must also [set this node configuration for new node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#create-cluster) that you manually create without node auto-provisioning.

To learn more, see [Customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#editing_by_updating_an_existing_node_pool).




## What's next

  * Learn how to [customize node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config).
  * Learn more about [Node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).
  * Learn how to [configure Pod bursting in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke).
  * Learn how to [rotate your cluster credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation).
  * Learn more about [Node pool upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
