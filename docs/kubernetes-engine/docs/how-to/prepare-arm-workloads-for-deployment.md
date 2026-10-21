---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment/
title: Prepare to deploy an Arm workload in a Standard cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:45:19.058201+00:00
---

# Prepare to deploy an Arm workload in a Standard cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Prepare to deploy an Arm workload in a Standard cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to prepare a workload to be scheduled on Arm nodes in a GKE Standard cluster. To learn more about scheduling Arm workloads with Autopilot, see [Deploy Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads).

To successfully schedule a workload to an Arm node, you must have the following:

  * An Arm-compatible container image. For guidance on how to check this, see [Is my workload ready for Arm?](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm#workload-arm-readiness-check)
  * Arm nodes where your Arm-compatible workloads can be scheduled. To create the necessary resources, see [Create clusters and node pools with Arm nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes).
  * A cluster in a Google Cloud region or zone that has available Arm virtual machines (VMs). For a filterable table of machine types and platforms, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).



## Overview

By default, GKE schedules workloads only to x86-based nodes—Compute Engine machine series with [Intel](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors) or [AMD](https://docs.cloud.google.com/compute/docs/cpu-platforms#amd_processors) processors—by placing a [taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) (`kubernetes.io/arch=arm64:NoSchedule`) on all Arm nodes. This taint prevents x86-compatible workloads from being inadvertently scheduled to your Arm nodes. You can optionally remove this default taint if you want x86-compatible workloads to be scheduled on Arm nodes without needing the corresponding toleration. For more information, see Configure the default Arm architecture taint.

If you want to deploy a workload to an Arm node which has the default taint, use the fields described in this document to guide the scheduler to send the workload to the requested type of node.

Use one of the following fields:

  * A [node selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector).
  * A [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) rule.



When you use a node selector or node affinity rule, GKE will only schedule your Arm-compatible workloads when you've declared that the workload's container image can run on the node's architecture.

If you schedule an Arm-compatible workload with a node selector or with a node affinity rule as described in the following sections, GKE automatically adds a [toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to the workload configuration so that the Pods can run on the Arm nodes.

This toleration added to the workload matches the taint (`kubernetes.io/arch=arm64:NoSchedule`) added to all Arm nodes, by default, to allow your workload to be scheduled on Arm nodes.

In some situations, such as when you have multi-architecture images that can run on any node, you might want to manually add this toleration to the workload configuration. For instructions, refer to Use toleration for scheduling multi-arch workloads to any architectures.

## Use a node selector to schedule an Arm workload

Add the following node selector to the specification:
    
    
    nodeSelector:
        kubernetes.io/arch: arm64
    

The node selector specifies that this workload should only be scheduled to nodes with the `arm64` label, which all Arm nodes on GKE clusters have.

When this node selector is included in the workload configuration, GKE adds the toleration to match the taint to permit the workload to be scheduled on Arm nodes.

## Use a node affinity rule to schedule an Arm workload

You can also use node affinity to schedule your workload.

### Schedule workload to a single architecture

Add the following node affinity to the specification:
    
    
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/arch
                operator: In
                values:
                - arm64
    

The node affinity rule specifies that the workload should only be scheduled to nodes with the `arm64` label, which all Arm nodes on GKE clusters have.

When this node affinity rule is included in the workload configuration, GKE adds the toleration to match the taint to permit the workload to be scheduled on Arm nodes.

### Schedule workload to x86 and Arm architectures

If you want to schedule a workload across both x86 (Intel and AMD processors) and Arm architectures, and your Arm node pools use the default taint behavior, you can specify this in different ways. The following instructions assume that your Arm node pools use the default taint.

#### Use toleration for scheduling multi-arch workloads to any architectures

If you have a multi-arch image that you want to be scheduled to any available architecture type in a Standard cluster, you only need to add the toleration to the workload specification. You do not need the node selector or node affinity rules described on this page as the workload can be scheduled to all architecture types.

Add the toleration:
    
    
      tolerations:
        - key: kubernetes.io/arch
          operator: Equal
          value: arm64
          effect: NoSchedule
    

Using this toleration, GKE could schedule a workload to nodes with any architecture type.

For example, if you have a cluster with the following node pools:

  * **my-c4a-node-pool** , using c4a-standard-16 VMs (`arm64`).
  * **my-c2-node-pool** , using c2-standard-8 VMs (`amd64`).
  * **my-t2d-node-pool** , using t2-standard-48 VMs (`amd64`).



If you deploy to this cluster a workload which uses a multi-arch image and the `arm64` toleration in the workload configuration, GKE may schedule the workload across all of the node pools.

#### Use node affinity rule for scheduling multi-architecture workloads to any architectures

If you want a workload to be scheduled on nodes across architecture types including x86 and Arm, you can also use a node affinity rule. With node affinity rules, you can specify exactly which architecture types you want to schedule the workload on. This approach is recommended for scheduling workloads on Autopilot clusters. To learn more, see [Deploy Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads#nodeaffinity).

With x86-based workloads, you do not need these node selectors, node affinity rules, or tolerations for the workload to be scheduled. If you have an image that you only want to schedule to x86-based nodes, you do not need to use these fields.

To schedule workloads to any architecture type, list both `arm64` and `amd64` the `values` section of the node affinity field. `amd64` includes any nodes using [x86 processors](https://docs.cloud.google.com/compute/docs/cpu-platforms#x86_processors).

The following example specifies that this workload could be scheduled on nodes with Arm processors or x86 processors:
    
    
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/arch
                operator: In
                values:
                - arm64
                - amd64
    

The labels for each architecture type are:

  * `arm64` for [nodes using Arm processors](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors) (for example, C4A).
  * `amd64` for [nodes using AMD processors](https://docs.cloud.google.com/compute/docs/cpu-platforms#amd_processors) (for example, Tau T2D) or [nodes using Intel processors](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors) (for example, C2).



For example, if you have a cluster with the following node pools and the given node affinity rule:

  * **my-c4a-node-pool** , using c4a-standard-16 VMs (`arm64`).
  * **my-c2-node-pool** , using c2-standard-8 VMs (`amd64`).
  * **my-t2d-node-pool** , using t2-standard-48 VMs (`amd64`).



If you deploy to this cluster a workload which uses a multi-arch image and the node affinity with `arm64` included in the `values` list, GKE adds the toleration in the workload configuration and may schedule the workload across all of the node pools.

## Configure the default Arm architecture taint

By default, GKE taints all Arm nodes with the `kubernetes.io/arch=arm64:NoSchedule` taint. This taint prevents workloads compatible with only the x86 architecture, but not the Arm architecture, from being scheduled to Arm nodes. If you have workloads that are compatible with both x86 and Arm, you can disable this taint to let GKE schedule these workloads on Arm nodes without needing a toleration corresponding to the taint.

You can update the default behavior only in Standard node pools in GKE clusters where the control plane runs version 1.35.0-gke.2141000 or later, or with nodes created for custom ComputeClasses. For more information, see [Configure the default Arm architecture taint](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#architecture-taint). Updating the taint behavior doesn't apply to deploying Arm workloads with Autopilot. For more information, see [Deploy Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads).

You can configure this behavior in the following situations with Standard node pools:

  * During cluster creation, for the default Standard node pool
  * When you create or update a Standard node pool



If you have any workloads running in the cluster that aren't compatible with Arm, don't remove the default taint, because incompatible workloads could be scheduled to the untainted Arm nodes.

To configure the default node taint for Arm nodes, select one of the following options:

###  gcloud CLI 

To set the taint behavior with the gcloud CLI, use the `--node-architecture-taint-behavior` flag when you do any of the following operations:

  * Create a Standard cluster with specific taint behavior for the default node pool using the [`gcloud container cluster create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-architecture-taint-behavior) command:
        
        gcloud container cluster create CLUSTER_NAME
            --location=CONTROL_PLANE_LOCATION \
            --node-architecture-taint-behavior=BEHAVIOR
        

  * Create a Standard node pool using the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-architecture-taint-behavior) command:
        
        gcloud container node-pools create POOL_NAME \
            --cluster=CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --node-architecture-taint-behavior=BEHAVIOR
        

  * Update a Standard node pool using the [`gcloud container node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--node-architecture-taint-behavior) command:
        
        gcloud container node-pools update POOL_NAME \
            --cluster=CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --node-architecture-taint-behavior=BEHAVIOR
        




For these commands, replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `POOL_NAME`: the name of your node pool.
  * `BEHAVIOR`: one of the following settings:

    * `none`: GKE omits the default taint of `kubernetes.io/arch=arm64:NoSchedule`.
    * `arm`: explicitly sets the default behavior, which adds the `kubernetes.io/arch=arm64:NoSchedule` taints for all nodes in the Arm node pool.



When you modify the node architecture taint behavior for a Standard node pool, GKE immediately updates the taints without needing to re-create the nodes.

###  Terraform 

Add the following `taint_config` block in `node_config` to configure the architecture taint behavior:
    
    
    taint_config {
      architecture_taint_behavior = "BEHAVIOR"
    }
    

Replace `BEHAVIOR` with one of the following settings:

  * `NONE`: GKE omits the default taint of `kubernetes.io/arch=arm64:NoSchedule`.
  * `ARM`: explicitly sets the default behavior, which adds the `kubernetes.io/arch=arm64:NoSchedule` taints for all nodes in the Arm node pool.



A complete `node_config` for a Standard node pool that includes this block looks like the following:
    
    
    resource "google_container_node_pool" "primary_preemptible_nodes" {
      name       = "NODE_POOL_NAME"
      location   = "NODE_POOL_LOCATION"
      cluster    = google_container_cluster.primary.name
      node_count = 1
    
      node_config {
        preemptible  = true
        machine_type = "ARM_MACHINE_TYPE"
    
        # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
        service_account = google_service_account.default.email
        oauth_scopes    = [
          "https://www.googleapis.com/auth/cloud-platform"
        ]
        taint_config {
          architecture_taint_behavior = "BEHAVIOR"
        }
      }
    }
    

In this example, `NODE_POOL_NAME` represents the name of the node pool, and `NODE_POOL_LOCATION` represents the location of the cluster's control plane.

## Deploy the workload

Now that you have specified where your Arm-compatible workloads should be scheduled, you can deploy your workload.

When you deploy a workload to a GKE cluster, the instructions are the same across architecture types. You can deploy an Arm-compatible workload as you would deploy any other workload, as long as you've completed the prerequisite steps. To see examples of deploying workloads, view the following pages:

  * [Deploying a stateless Linux application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps#console).
  * [Deploying a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).
  * [Running a Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/).



## Troubleshooting

For common errors and troubleshooting information, refer to [Troubleshooting Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-arm-workloads).

## What's next

  * [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke)
  * [Migrate x86 application on GKE to multi-arch with Arm](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
