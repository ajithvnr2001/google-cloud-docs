---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes/
title: Control autoscaled node attributes with custom ComputeClasses \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:06.419144+00:00
---

# Control autoscaled node attributes with custom ComputeClasses  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Control autoscaled node attributes with custom ComputeClasses Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to control the compute infrastructure and autoscaling behavior of Google Kubernetes Engine (GKE) clusters based on the specific needs of your workloads by using [_custom ComputeClasses_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

This document is intended for platform administrators who want to declaratively define autoscaling profiles for nodes, and for cluster operators who want to run their workloads on specific ComputeClasses.

### About custom ComputeClasses

Custom ComputeClasses are Kubernetes [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) that let you define priorities for GKE to follow when provisioning nodes to run your workloads. You can use a custom ComputeClass to do the following:

  * Give GKE a set of priorities to sequentially follow when provisioning nodes, each with specific parameters like a Compute Engine machine series or minimum resource capacity
  * Define autoscaling thresholds and parameters for removing underutilized nodes and consolidating workloads efficiently on existing compute capacity
  * Tell GKE to automatically replace less preferred node configurations with more preferred node configurations for optimal workload performance



To understand all of the configuration options and how they interact with each other and with GKE Autopilot mode and GKE Standard mode, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

## Pricing

The `ComputeClass` custom resource is provided at no extra cost in GKE. The following pricing considerations apply:

  * GKE Autopilot mode: you're billed using the node-based billing mode. For details, see [Autopilot mode pricing](https://cloud.google.com/kubernetes-engine/pricing#pods-that-have-specific-hardware-requirements).

  * GKE Standard mode: see [Standard mode pricing](https://cloud.google.com/kubernetes-engine/pricing#standard_mode).




## Limitations

The name of your ComputeClass can't begin with `gke` or `autopilot`.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing GKE cluster running version 1.30.3-gke.1451000 or later. For more information, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version).
  * If you're using a Standard mode cluster, ensure that you meet one of the following requirements:

    * Enable [autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler) on at least one node pool in the cluster.
    * If your Standard cluster runs a version earlier than 1.33.3-gke.1136000 and isn't enrolled in the Rapid release channel, [enable cluster-level node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable-cluster-level).



## Example scenario for ComputeClasses

This document presents an example scenario for which you define a custom ComputeClass. In practice, you should consider the requirements of your specific workloads and organization, and define ComputeClasses that meet those requirements. For full descriptions of all of the options for ComputeClasses, and for special considerations, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

Consider the following example scenario:

  * Your goal is to optimize running costs for your workloads
  * Your workloads are fault-tolerant and don't require graceful shutdown or extended runtime
  * Your workloads need at least 64 vCPU to run optimally
  * You're limited to the N4 Compute Engine machine series



Based on the example scenario, you decide that you want a ComputeClass that does the following:

  * Prioritizes N4 Spot nodes that have at least 64 vCPU
  * Lets GKE fall back to any N4 Spot node, regardless of compute capacity
  * If no N4 Spot nodes are available, lets GKE use on-demand N4 nodes
  * Tells GKE to move your workloads to Spot nodes whenever they're available again



## Configure a ComputeClass in Autopilot mode

In GKE Autopilot, you define a ComputeClass, deploy it to the cluster, and request that ComputeClass in your workloads. GKE performs any node configuration steps, like applying labels and taints, for you.

Save the following manifest as `compute-class.yaml`:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: cost-optimized
    spec:
      priorities:
      - machineFamily: n4
        spot: true
        minCores: 64
      - machineFamily: n4
        spot: true
      - machineFamily: n4
        spot: false
      activeMigration:
        optimizeRulePriority: true
      nodePoolAutoCreation:
        enabled: true
    

## Configure a ComputeClass in Standard mode

In GKE Standard mode clusters, you might have to perform manual configuration to ensure that your ComputeClass Pods schedule as expected. Manual configuration depends on whether your node pools are automatically created, as follows:

  * **Auto-created node pools** : No manual configuration required. GKE automatically performs ComputeClass configuration steps for you. For details, see [Node pool auto-creation and ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#autoprovisioning-and-compute-classes).
  * **Manually-created node pools** : Manual configuration is required. You must add node labels and node taints to your manually created node pools to associate the nodes with a specific ComputeClass. For details, see [Configure manually-created node pools for ComputeClass use](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#manual-node-pools).

**Caution:** If you use only manually-created node pools in your cluster and you don't associate any node pools with a ComputeClass, Pods that request the ComputeClass remain stuck in the `Pending` state. Conversely, if you associate every node pool with a specific ComputeClass, Pods that request a different ComputeClass and Pods that don't request a ComputeClass remain stuck in the `Pending` state.

To let GKE automatically create node pools for your ComputeClass, follow these steps:

  1. For Standard mode clusters that run a version earlier than 1.33.3-gke.1136000 and aren't enrolled in the Rapid release channel, [enable cluster-level node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable-cluster-level).
  2. Save the following example manifest as `compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: cost-optimized
         spec:
           priorities:
           - machineFamily: n4
             spot: true
             minCores: 64
           - machineFamily: n4
             spot: true
           - machineFamily: n4
             spot: false
           activeMigration:
             optimizeRulePriority: true
           nodePoolAutoCreation:
             enabled: true
         

When you deploy Pods that request this example ComputeClass and new nodes need to be created, GKE prioritizes creating nodes in the order of items in the `priorities` field. If required, GKE creates new node pools that meet the hardware requirements of the ComputeClass.




You can also specify a precise [custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) in your priorities. Using custom machine types requires GKE version 1.33.2-gke.1111000 or later. The following example configures a ComputeClass that prioritizes Spot VMs for the `n4-custom-8-20480` custom machine type, and falls back to on-demand VMs of the same type if Spot capacity is unavailable:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: custom-machine-type
    spec:
      priorities:
      - machineType: n4-custom-8-20480
        spot: true
      - machineType: n4-custom-8-20480
        spot: false
      nodePoolAutoCreation:
        enabled: true
    

To optimize capacity availability during capacity constraints, define a ComputeClass that spans multiple machine series and generations. For stateless or disruption-tolerant workloads, you can also enable active migration to return workloads to your preferred hardware when capacity recovers:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: multi-family-fallback
    spec:
      priorities:
      - machineFamily: c4d
      - machineFamily: c3d
      - machineFamily: c4
      - machineFamily: c3
      - machineFamily: n4
      - machineFamily: n2d
      activeMigration:
        optimizeRulePriority: true
      nodePoolAutoCreation:
        enabled: true
    

Newer machine series such as C4, C4D, and N4 support only Hyperdisk, and older series such as N2D use Persistent Disk. If stateful workloads use a ComputeClass that spans both generations, [disable active migration](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses#disable-active-migration) and, in GKE version 1.35.3-gke.1290000 and later, use the built-in `dynamic-rwo` StorageClass or a custom StorageClass with [automated disk type selection](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#automated_disk_type_selection) (`parameters.type: dynamic`), `use-allowed-disk-topology: "true"`, and `volumeBindingMode: WaitForFirstConsumer`. GKE then selects a compatible disk type when provisioning new volumes and schedules existing volumes only on compatible machine series.

### Use ComputeClasses with manually-created node pools

This section shows you how to define a ComputeClass in a cluster that only uses manually-created node pools.

  1. Save the following manifest as `compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: cost-optimized
         spec:
           priorities:
           - machineFamily: n4
             spot: true
             minCores: 64
           - machineFamily: n4
             spot: true
           - machineFamily: n4
             spot: false
           activeMigration:
             optimizeRulePriority: true
         

  2. Create a new autoscaled node pool that uses Spot VMs and associate it with the ComputeClass:
         
         gcloud container node-pools create cost-optimized-pool \
             --location=LOCATION \
             --cluster=CLUSTER_NAME \
             --machine-type=n4-standard-64 \
             --spot \
             --enable-autoscaling \
             --max-nodes=9 \
             --node-labels="cloud.google.com/compute-class=cost-optimized" \
             --node-taints="cloud.google.com/compute-class=cost-optimized:NoSchedule"
         

Replace the following:

     * `LOCATION`: the location of your cluster.
     * `CLUSTER_NAME`: the name of your existing cluster.
  3. Create a new autoscaled node pool with on-demand VMs and associate it with the ComputeClass:
         
         gcloud container node-pools create on-demand-pool \
             --location=LOCATION \
             --cluster=CLUSTER_NAME \
             --machine-type=n4-standard-64 \
             --enable-autoscaling \
             --max-nodes=9 \
             --num-nodes=0 \
             --node-labels="cloud.google.com/compute-class=cost-optimized" \
             --node-taints="cloud.google.com/compute-class=cost-optimized:NoSchedule"
         




When you deploy Pods that request this ComputeClass and new nodes need to be created, GKE prioritizes creating nodes in the `cost-optimized-pool` node pool. If new nodes can't be created, GKE creates nodes in the `on-demand-pool` node pool.

For more details about how manually-created node pools interact with custom ComputeClasses, see [Configure manually-created node pools for ComputeClass use](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#manual-node-pools).

## Customize autoscaling thresholds for node consolidation

By default, GKE removes underutilized nodes and reschedules your workloads onto other available nodes. You can further customize the thresholds and timing after which a node becomes a candidate for removal by using the `autoscalingPolicy` field in the ComputeClass definition, like in the following example:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: cost-optimized
    spec:
      priorities:
      - machineFamily: n4
        spot: true
        minCores: 64
      - machineFamily: n4
        spot: true
      - machineFamily: n4
        spot: false
      activeMigration:
        optimizeRulePriority: true
      autoscalingPolicy:
        consolidationDelayMinutes : 5
        consolidationThreshold    : 70
    

This example makes a node become a candidate for removal if it's underutilized by 70% of its available CPU and memory capacity for more than five minutes. For a list of available parameters, see [Set autoscaling parameters for node consolidation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#set-autoscaling).

### Deploy a ComputeClass in a cluster

After you define a ComputeClass, deploy it to the cluster:
    
    
    kubectl apply -f compute-class.yaml
    

This ComputeClass is ready to use in the cluster. You can request the ComputeClass in Pod specifications or, optionally, set it as the default ComputeClass in a specific namespace.

## Request a ComputeClass in a workload

To request a ComputeClass in a workload, add a node selector for that ComputeClass in your manifest, like in the following steps:

  1. Save the following manifest as `cc-workload.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: custom-workload
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: custom-workload
           template:
             metadata:
               labels:
                 app: custom-workload
             spec:
               nodeSelector:
                 cloud.google.com/compute-class: cost-optimized
               containers:
               - name: test
                 image: registry.k8s.io/pause
                 resources:
                   requests:
                     cpu: 1.5
                     memory: "4Gi"
         

  2. Deploy the workload:
         
         kubectl apply -f cc-workload.yaml
         




When you deploy this workload, GKE automatically adds a toleration to the Pods that corresponds to the node taint for the requested ComputeClass. This toleration helps ensure that only Pods that request the ComputeClass run on ComputeClass nodes.

## Filter nodes by ComputeClass

Any nodes that are associated with ComputeClasses have the `cloud.google.com/compute-class` label.

To view all of the nodes that are associated with a specific ComputeClass, run the following command::
    
    
    kubectl get nodes -l cloud.google.com/compute-class=COMPUTECLASS_NAME
    

Replace `COMPUTECLASS_NAME` with the name of the ComputeClass (for example, `cost-optimized`).

The output is similar to the following:
    
    
    NAME                                                  STATUS   ROLES    AGE   VERSION
    gke-cluster-1-cost-optimized-pool-f213e529-rx7d       Ready    <none>   5m    v1.32.4-gke.1236007
    gke-cluster-1-cost-optimized-pool-f213e529-ab12       Ready    <none>   5m    v1.32.4-gke.1236007
    

To display all of the nodes in the cluster that are associated with a ComputeClass, run the following command:
    
    
    kubectl get nodes -L cloud.google.com/compute-class
    

## Update a deployed ComputeClass

To update a deployed ComputeClass, modify the YAML manifest for the ComputeClass. Then, deploy the modified manifest by running the following command:
    
    
    kubectl apply -f PATH_TO_FILE
    

Replace `PATH_TO_FILE` with the path to your modified manifest. Ensure that the value in the `name` field remains unchanged.

When you deploy your updated ComputeClass, GKE uses your updated configuration to create new nodes. GKE doesn't modify any existing nodes with your updated configuration.

Over time, GKE might move existing Pods to nodes that use your updated configuration if the ComputeClass uses [active migration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#active-migration) and if the existing Pods are eligible to migrate.

## What's next

  * [Learn about best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses).
  * [Read more about custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).
  * [Apply custom ComputeClasses to Pods by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).
  * [Troubleshoot custom ComputeClass issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
