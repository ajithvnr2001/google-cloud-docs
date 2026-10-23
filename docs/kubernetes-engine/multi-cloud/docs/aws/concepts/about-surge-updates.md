---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/about-surge-updates/
title: About surge updates \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:32.248122+00:00
---

# About surge updates  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/about-surge-updates/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  About surge updates Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a brief overview of standard rolling updates and then goes into detail about surge updates, which are a special kind of rolling update. Compared to standard rolling updates, surge updates let you configure the speed of the update. Surge updates also let you exert some control over how disruptive updates are to your workloads.

For information about how to enable and configure surge updates for GKE on AWS, see [Configure surge updates of node pools](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-surge-updates).

## How standard rolling updates work

Some updates to a node pool, such as when you modify a node pool's annotations, don't require the restart of nodes, and so don't elicit a rolling update. If GKE on AWS can apply changes to a node pool without having to restart or recreate resources, it will do so to prevent disruptions.

However, most updates to a node pool in GKE on AWS typically involve terminating existing nodes, and launching new nodes with the updated settings. The process of terminating existing nodes can disrupt workloads.

By default, GKE on AWS performs standard rolling updates. This method updates nodes one at a time, and they are replaced using a "terminate before create" approach: a node is terminated first, and then a new updated node is launched. This minimizes disruption because only one node is terminated and replaced at any given moment.

Here are the steps GKE on AWS takes during a standard rolling update:

  1. Selects a node from the node pool and marks the node as unavailable to ensure no new Pods start on it—this action is called _cordoning_.
  2. Relocates the active Pods from the cordoned node to other available nodes within the cluster. If other nodes have sufficient capacity, they accommodate the evicted Pods. Otherwise, the cluster autoscaler, which remains active during a standard rolling update, starts a scale up and provisions additional nodes to ensure that there's enough capacity to schedule the evicted Pods. For information about the measures taken to protect workloads during this process, see [Workload protection during resizing](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool#workload_protection_during_resizing).
  3. Terminates the cordoned node.
  4. Substitutes the cordoned node with a new one with the updated settings.
  5. Conducts a health check on the newly operational node. If the node pool fails the health check, it's marked with a `DEGRADED` status. This status can be viewed by executing the `gcloud container aws node-pools describe` command. When a node pool is marked as `DEGRADED`, new Pods might not be scheduled on the nodes within that pool.
  6. Continues updating, node by node, until all nodes in the pool have been updated.



## How surge updates work

In GKE on AWS, the standard rolling method updates nodes one at a time. Surge updates, which are a form of rolling update, let you update multiple nodes simultaneously. Surge updates are therefore faster than standard rolling updates. However, updating several nodes simultaneously can disrupt workloads. To mitigate this, surge updates provide options to modulate the level of disruption to your workloads.

Another way surge updates can differ from standard rolling updates is the way nodes are replaced. Standard rolling updates replace nodes using a "terminate before create" strategy. Depending on the settings you choose, surge updates can use either a "create before terminate" strategy, a "terminate before create" strategy, or even a combination of both.

The cluster autoscaler plays a more important role in surge updates than in standard rolling updates, which is why it figures prominently in the following list of actions GKE on AWS takes during a surge update:

  1. **Creation of new autoscaling group** : GKE on AWS provisions new nodes with the modifications specified by the update command, and assigns these new nodes to a new AWS autoscaling group (ASG).
  2. **Cluster autoscaler behavior** : As the surge update begins, the cluster autoscaler is activated for the new autoscaling group. The cluster autoscaler for the original autoscaling group is deactivated. This ensures that any scaling operations target only the new group.
  3. **Node replacement** : Depending on the surge update parameters, different strategies for node replacement are used: 
     * "create before terminate": this strategy is activated when the `max-surge-update` parameter is set to a value greater than zero. It spawns new nodes in the new ASG before terminating the old ones in the original ASG, aiming to minimize service disruptions.
     * "terminate before create": this method is triggered when the `max-surge-update` parameter is set to zero and the `max-unavailable-update` parameter has a value greater than zero. Nodes from the original ASG are terminated first, followed by the creation of new ones in the new ASG.
  4. **Node pool size adjustments** : During the update, the node pool size (that is, the sum of nodes in the old and the new ASG) might fluctuate above or below the original count of nodes present in the node pool before the update started. Specifically, GKE on AWS aims to maintain the total node count within the range of (`original_count` \- `max-unavailable-update`) to (`original_count` \+ `max-surge-update`). Eventually, the nodes in the old ASG (`original_count`) are replaced with updated nodes in the new ASG. The cluster autoscaler might launch more nodes in the new ASG if it detects that Pods are unable to be scheduled but it stays within the limits defined by `min-nodes` and `max-nodes`.



### An example to illustrate the process

To better understand how surge updates work, consider the following example. Suppose you have a node pool with 5 nodes, and you run the following command:
    
    
      gcloud container aws node-pools update production-node-pool
          --cluster my-cluster \
          --location us-west1 \
          --max-surge-update 2 \
          --max-unavailable-update 1 \
          --node-version 1.27.6-gke.700
    

In this example, `max-surge-update` is set to 2, `max-unavailable-update` is set to 1, and you're providing a new node pool version (that is, you're changing the GKE version that is running on the nodes in the node pool).

Running this command triggers a surge update and GKE on AWS performs the following actions:

  1. Creates 2 additional nodes because the value of `max-surge-update` equals 2.
  2. Assigns these 2 additional nodes to a new AWS autoscaling group.
  3. Removes nodes from the original autoscaling group once these new nodes are operational. GKE on AWS brings down up to 3 nodes (the combined value of `max-surge-update` and `max-unavailable-update`) but ensures that at most only one node becomes unavailable at any time (due to the `max-unavailable-update` value of 1).
  4. Repeat these steps until all the nodes in the node pool have been updated to the new GKE version.



During this update, the node pool contains between 4 to 7 operational nodes.

## Things to consider before running surge updates

Before running a surge update, keep in mind the following:

  * Additional instances created as part of this surge step can potentially exceed your AWS instance quota limit. If you don't have enough quota and these additional instances can't be provisioned, the update might fail.
  * If `max-unavailable-update` is set to 0, disruptions to workloads can still occur as Pods get evicted and rescheduled onto the newer nodes.
  * The maximum number of nodes that can be updated simultaneously is equal to the sum of `max-surge-update` and `max-unavailable-update`, and is limited to 20.



## Choose the right surge settings for your needs

While standard rolling updates often use a "terminate before create" approach, surge updates introduce more flexibility. Depending on the configuration, surge updates can follow a "create before terminate" strategy, a "terminate before create" strategy, or a combination of both. This section describes different configurations to help you select the best approach for your workloads.

The following table shows three example settings, and highlights their impact on the speed of the update and the potential disruption to your workloads:

**Name** | **Description** | **Configuration**  
---|---|---  
Balanced setting (default)  | Balanced, slower but least disruptive.  | maxSurge=1, maxUnavailable=0   
Rapid updates without extra resources  | Fast, no surge resources, most disruptive.  | maxSurge=0, maxUnavailable=20   
Rapid updates that are less disruptive  | Fast, most surge resources and less disruptive.  | maxSurge=20, maxUnavailable=0   
  
Each of the settings in the table is described in the following sections.

### Balanced setting (default)

The most straightforward way to use surge updates is with the default configuration of `max-surge-update=1` and `max-unavailable-update=0`. This configuration adds only 1 surge node to the node pool during the update, and only 1 node is updated at a time, following a "create before terminate" approach. Compared to the standard non-surge rolling update, which is equivalent to (`max-surge-update=0`, `max-unavailable-update=1`), this method is less disruptive, accelerates Pod restarts during updates, and is more conservative in its progression.

It's important to note that adopting the balanced setting can lead to extra costs because of the temporary surge node added during the update. This additional node incurs charges while it's active, slightly raising the overall expense compared to methods without surge nodes.

### Rapid updates without extra resources

For workloads that can tolerate interruptions, a faster update approach might be suitable. Configuring `max-surge-update=0` and `max-unavailable-update=20` achieves this. With this configuration, 20 nodes can be updated simultaneously without adding any surge nodes. This update method follows a "terminate before create" approach. Because no additional surge nodes are introduced during the process, this method is also the most cost-effective, avoiding extra expenses associated with temporary nodes.

### Rapid updates that are less disruptive

If your workloads are sensitive to disruption, you can increase the speed of the update with the following settings: `max-surge-update=20` and `max-unavailable-update=0`. This configuration updates 20 nodes in parallel in a "create before terminate" fashion.

However, the overall speed of the update can be constrained if you've set up [`PodDisruptionBudgets` (PDB)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) for your workloads. This is because the PDB restricts the number of Pods that can be drained at any given moment. Although the configurations of PDBs may vary, if you create a PDB with `maxUnavailable` equal to 1 for one or more workloads running on the node pool, then only one Pod of those workloads can be evicted at a time, limiting the parallelism of the entire update.

Recall that initiating multiple surge nodes at the start of the update process can lead to a temporary increase in costs, especially when compared to configurations that don't add extra nodes or add fewer nodes during updates.

## What's next

For information about how to enable and configure surge updates for GKE on AWS, see [Configure surge updates of node pools](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-surge-updates). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
