---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement/
title: Define compact placement for GKE nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:03.362900+00:00
---

# Define compact placement for GKE nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Define compact placement for GKE nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can control whether your Google Kubernetes Engine (GKE) nodes are physically located relative to each other within a [zone](https://docs.cloud.google.com/compute/docs/regions-zones#zones_and_clusters) by using a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

## Overview

When you create node pools and workloads in a GKE cluster, you can define a _compact placement policy_ , which specifies that these nodes or workloads should be placed in closer physical proximity to each other within a [zone](https://docs.cloud.google.com/compute/docs/regions-zones#zones_and_clusters). Having nodes closer to each other can reduce network latency between nodes, which can be especially useful for tightly-coupled batch workloads.

## Use compact placement with GKE Autopilot

In Autopilot clusters, you can request compact placement for specific workloads by adding node selectors to your Pod specification. You can use the default Autopilot compact placement policy or an existing Compute Engine compact placement policy that uses the N2 machine series or the N2D machine series.

### Limitations

  * GKE provisions workloads within a compact placement in the same zone.
  * Available with GPU Pods or with the `Balanced` and `Performance` ComputeClasses.
  * Available only on C2, C2D, C3, C3D, C4A, C4D, C4N, H3, H4D, N2, N2D, and Z4D [machine types](https://docs.cloud.google.com/compute/docs/machine-resource).
  * Available only with [A100, L4, and H100 GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).
  * Compact placement is available for Pods grouped on up to 1,500 nodes.



### Enable a compact placement policy

To enable compact placement for GKE Autopilot, add a `nodeSelector` to the Pod specification with the following keys:

  * `cloud.google.com/gke-placement-group`: the identifier you assign for the group of Pods that should run together, in the same compact placement group. Each placement group is limited to 1,500 nodes. We recommend you limit a placement group only to the workloads that benefit from the grouping, and distribute your workloads into separate placement groups where possible.

  * One of the following keys to define the type of resource:

    * `cloud.google.com/compute-class: "Balanced"`
    * `cloud.google.com/gke-accelerator: "nvidia-tesla-a100"`
  * `cloud.google.com/placement-policy-name`: optionally, the name of an existing Compute Engine compact placement policy. You can only specify a custom compact placement policy in GKE version 1.31.1-gke.2010000 and later.

For instructions, see the Create a compact placement policy section on this page.




The following example Pod specification enables compact placement with a custom compact placement policy:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
    # lines omitted for clarity
    spec:
      nodeSelector:
        cloud.google.com/gke-placement-group: "placement-group-1"
        cloud.google.com/compute-class: "Balanced"
        cloud.google.com/placement-policy-name: PLACEMENT_POLICY_NAME
    

Replace `PLACEMENT_POLICY_NAME` with the name of an existing Compute Engine compact placement policy. To use the default compact placement policy for Autopilot, omit the `cloud.google.com/placement-policy-name` line.

### Use a custom compact placement policy without placement groups

To use a custom compact placement policy without placement groups, you must either add the `cloud.google.com/placement-policy-name` node selector to your Pod specification, or define a [custom compute class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#request-placement-policy) with placement priority.

#### Add the `cloud.google.com/placement-policy-name` node selector to your Pod specification

This approach might be useful if you want to use a [JobSet](https://jobset.sigs.k8s.io/docs/concepts/) to schedule each job separately, but you also want to use a custom compact placement policy to place the nodes that run the same job closer to each other.

Because JobSet doesn't support specifying different node selectors for each job, you can't use JobSet with placement groups in this scenario. However, you can use JobSet's built-in support for exclusive topologies to achieve the same effect.

The following example Pod specification enables compact placement with a custom compact placement policy for a JobSet workload:
    
    
    apiVersion: jobset.x-k8s.io/v1alpha2
    kind: JobSet
    metadata:
      name: my-jobset
      annotations:
        alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
    spec:
     replicatedJobs:
        - name: my-job
          template:
            spec:
              # lines omitted for clarity
              template:
                spec:
                  nodeSelector:
                    cloud.google.com/placement-policy-name: PLACEMENT_POLICY_NAME
                    cloud.google.com/machine-family: "n2"
                  # lines omitted for clarity
    

Replace `PLACEMENT_POLICY_NAME` with the name of an existing Compute Engine compact placement policy.

#### Use a custom compute class to define placement policy

Refer to [custom compute class with placement priority](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#request-placement-policy) documentation to see the specifics.

Instead of adding a `nodeSelector` with policy name directly to your workload specification, you can apply a compact placement policy by setting the `placement` field in a `ComputeClass` definition. For details, see [custom compute class with placement priority](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#request-placement-policy).

## Use compact placement with GKE Standard

### Limitations

Compact placement in GKE Standard node pools has the following limitations:

  * Supported only in new node pools. You cannot enable or disable compact placement on existing node pools.
  * Available only for [node pools operating in a single zone](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster#create-regional-single-zone-nodepool).
  * Available only on A2, A3, A4, C2, C2D, C3, C3D, C4, C4D, G2, G4, H3, H4D, N2, and N2D [machine types](https://docs.cloud.google.com/compute/docs/machine-resource). However, for [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) and [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms), we recommend using block-targeted reservations instead of compact placement. For details, see [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute#reserve-capacity).
  * Supports up to 1,500 [Compute Engine VM instances](https://docs.cloud.google.com/compute/docs/instances) in each policy. Any node pool that exceeds this limit at any time will be rejected during creation.
  * Supplying a custom resource policy using the `placement-policy` flag is not supported with blue-green upgrades.



### Create a compact placement policy

To create compact placement policies, in the Google Cloud CLI, you specify the `placement-type=COMPACT` option during node pool or cluster creation. With this setting, GKE attempts to place nodes within a node pool in closer physical proximity to each other.

To use an existing [resource policy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies) in your cluster, specify the location of your custom policy for the `placement-policy` flag during node pool or cluster creation. This enables the flexibility of using reserved placements, multiple node pools with the same placement policy, and other advanced placement options. However, it also requires more manual operations than specifying the --placement-type=COMPACT flag. For example, you need to create, delete, and maintain your custom resource policies. Make sure that the maximum number of VM instances is respected across all node pools using the resource policy. If this limit is reached while some of your node pools haven't reach their maximum size, adding any more nodes will fail.

If you don't specify the `placement-type` and `placement-policy` flags, then by default there are no requirements on node placement.

### Create a compact placement policy in a new cluster

When you create a new cluster, you can specify a compact placement policy that will be applied to the default node pool. Any subsequent node pools that you create for the cluster, you will need to specify whether to apply compact placement.

To create a new cluster where the default node pool has a compact placement policy applied, use the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --machine-type MACHINE_TYPE \
        --placement-type COMPACT \
        --max-surge-upgrade 0 \
        --max-unavailable-upgrade MAX_UNAVAILABLE
    

Replace the following:

  * `CLUSTER_NAME`: The name of your new cluster.
  * `MACHINE_TYPE`: The type of machine to use for nodes, which must be a supported machine type listed in the Standard cluster limitations.
  * `--placement-type COMPACT`: Applies compact placement for the nodes in the default node pool.
  * `MAX_UNAVAILABLE`: Maximum number of nodes that can be unavailable at the same time during a node pool upgrade. For compact placement we recommend [fast no surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#optimizing-surge) to optimize the likelihood of finding colocated nodes during upgrades.



### Create a compact placement policy on an existing cluster

On an existing cluster, you can create a node pool that has a compact placement policy applied.

To create a node pool that has a compact placement policy applied, use the following command:
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --machine-type MACHINE_TYPE \
        --cluster CLUSTER_NAME \
        --placement-type COMPACT \
        --max-surge-upgrade 0 \
        --max-unavailable-upgrade MAX_UNAVAILABLE
    

Replace the following:

  * `NODEPOOL_NAME`: The name of your new node pool.
  * `MACHINE_TYPE`: The type of machine to use for nodes, which must be a supported machine type listed in the Standard cluster limitations.
  * `CLUSTER_NAME`: The name of your existing cluster.
  * `--placement-type COMPACT`: Indicates to apply compact placement for the nodes in the new node pool.
  * `MAX_UNAVAILABLE`: Maximum number of nodes that can be unavailable at the same time during a node pool upgrade. For compact placement we recommend [fast no surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#optimizing-surge) to optimize the likelihood of finding colocated nodes during upgrades.



### Create node pools using a shared custom placement policy

You can manually create a [resource policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement) and use it in multiple node pools.

  1. Create the resource policy in the cluster Google Cloud region:
         
         gcloud compute resource-policies create group-placement POLICY_NAME \
             --region REGION \
             --collocation collocated
         

Replace the following:

     * `POLICY_NAME`: The name of your resource policy.
     * `REGION`: The region of your cluster.
  2. Create a node pool using the custom resource policy:
         
         gcloud container node-pools create NODEPOOL_NAME \
             --machine-type MACHINE_TYPE \
             --cluster CLUSTER_NAME \
             --placement-policy POLICY_NAME \
             --max-surge-upgrade 0 \
             --max-unavailable-upgrade MAX_UNAVAILABLE
         

Replace the following:

     * `NODEPOOL_NAME`: The name of your new node pool.
     * `MACHINE_TYPE`: The type of machine to use for nodes, which must be a supported machine type listed in the Standard cluster limitations.
     * `CLUSTER_NAME`: The name of your existing cluster.
     * `MAX_UNAVAILABLE`: Maximum number of nodes that can be unavailable at the same time during a node pool upgrade. For compact placement we recommend [fast no surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#optimizing-surge) to optimize the likelihood of finding colocated nodes during upgrades.



### Use a Compute Engine reservation with a compact placement policy

[Reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) help you guarantee that hardware is available in a specified zone, reducing the risk of node pool creation failure caused by insufficient hardware.

  1. Create a reservation that specifies a compact placement policy:
         
         gcloud compute reservations create RESERVATION_NAME \
             --vm-count MACHINE_COUNT \
             --machine-type MACHINE_TYPE \
             --resource-policies policy=POLICY_NAME \
             --zone ZONE \
             --require-specific-reservation
         

Replace the following:

     * `RESERVATION_NAME`: The name of your reservation.
     * `MACHINE_COUNT`: The number of reserved nodes.
     * `MACHINE_TYPE`: The type of machine to use for nodes, which must be a supported machine type listed in the Standard cluster limitations.
     * `POLICY_NAME`: The name of your resource policy.
     * `ZONE`: The zone where to create your reservation.
  2. Create a node pool by specifying both the compact placement policy and the reservation you created in the previous step:
         
         gcloud container node-pools create NODEPOOL_NAME \
             --machine-type MACHINE_TYPE \
             --cluster CLUSTER_NAME \
             --placement-policy POLICY_NAME \
             --reservation-affinity specific \
             --reservation RESERVATION_NAME \
             --max-surge-upgrade 0 \
             --max-unavailable-upgrade MAX_UNAVAILABLE
         




Replace the following:

  * `NODEPOOL_NAME`: The name of your new node pool.
  * `MACHINE_TYPE`: The type of machine to use for nodes, which must be a supported machine type listed in the Standard cluster limitations.
  * `CLUSTER_NAME`: The name of your existing cluster.



### Create a workload on nodes that use compact placement

To run workloads on dedicated nodes that use compact placement, you can use several Kubernetes mechanisms, such as [assigning pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) and [preventing scheduling unwanted pods on a group of nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to achieve this.

In the following example, we add a [taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to the dedicated nodes and add a corresponding toleration and affinity to the Pods.

  1. Add a taint to nodes in the node pool that has a compact placement policy:
         
         kubectl taint nodes -l cloud.google.com/gke-nodepool=NODEPOOL_NAME dedicated-pool=NODEPOOL_NAME:NoSchedule
         

  2. In the workload definition, specify the necessary toleration and a node affinity. Here's an example with a single Pod:
         
         apiVersion: v1
         kind: Pod
         metadata:
           ...
         spec:
           ...
           tolerations:
           - key: dedicated-pool
             operator: "Equal"
             value: "NODEPOOL_NAME"
             effect: "NoSchedule"
           affinity:
             nodeAffinity:
               requiredDuringSchedulingIgnoredDuringExecution:
                 nodeSelectorTerms:
                 - matchExpressions:
                   - key: dedicated-pool
                     operator: In
                     values:
                     - NODEPOOL_NAME
         




In some locations, it might not be possible to create a large node pool using a compact placement policy. To limit the size of such node pools to what's necessary, you should consider creating a node pool per workload requiring compact placement.

### Use compact placement for node auto-provisioning

With node auto-provisioning, GKE automatically provisions node pools based on cluster resource demand. For more information, see [Using node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).

To enable compact placement for node auto-provisioning, add a `nodeSelector` to the Pod specification like in the following example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
    # lines omitted for clarity
    spec:
      nodeSelector:
        cloud.google.com/gke-placement-group: PLACEMENT_GROUP_IDENTIFIER
        cloud.google.com/machine-family: MACHINE_FAMILY
        cloud.google.com/placement-policy-name: PLACEMENT_POLICY_NAME
    # lines omitted for clarity
    

Replace the following:

  * `PLACEMENT_GROUP_IDENTIFIER`: the identifier that you assign for the group of Pods that should run together, in the same compact placement group.
  * `MACHINE_FAMILY`: the name of the machine family. Use one of the machine families that support compact placement. We recommend you use C2 or C2D machine families for workloads with compute and networking performance requirements.
  * `PLACEMENT_POLICY_NAME`: optionally, the name of an existing Compute Engine compact placement policy. GKE uses the specified compact placement policy when node auto-provisioning creates a new node pool to group your Pods together. You can only specify a custom compact placement policy in GKE version 1.31.1-gke.2010000 and later.

For instructions, see the Create a compact placement policy section on this page.




You can omit the `cloud.google.com/machine-family` key if the Pod configuration already defines a machine type supported with compact placement. For example, if the Pod specification includes `nvidia.com/gpu` and the cluster is configured to use A100 GPUs, you don't need to include the `cloud.google.com/machine-family` key.

The following example is a Pod specification that defines `nvidia.com/gpu` request and the cluster is configured to use A100 GPUs. This Pod `spec` doesn't include the `cloud.google.com/machine-family` key:
    
    
      apiVersion: v1
      kind: Pod
      metadata:
        ...
      spec:
        ...
        nodeSelector:
          cloud.google.com/gke-placement-group: PLACEMENT_GROUP_IDENTIFIER
          cloud.google.com/gke-accelerator: "nvidia-tesla-a100"
        resources:
          limits:
            nvidia.com/gpu: 2
    

To learn more, see [how to configure Pods to consume GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#pods_gpus).

#### Optimize placement group size

Because GKE finds the best placement for smaller deployments, we recommend you instruct GKE to avoid running different type of Pods in the same placement group. Add a toleration key with the `cloud.google.com/gke-placement-group` key and the compact placement identifier you defined.

The following example is a Pod specification that defines a Pod toleration with compact placement:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      ...
    spec:
      ...
      tolerations:
      - key: cloud.google.com/gke-placement-group
        operator: "Equal"
        value: PLACEMENT_GROUP_IDENTIFIER
        effect: "NoSchedule"
    

For more information about node auto-provisioning with Pod toleration, see [Workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation)

## What's next

  * Learn about [Defining instance placement policies](https://docs.cloud.google.com/compute/docs/instances/define-instance-placement#support_and_restrictions) in Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
