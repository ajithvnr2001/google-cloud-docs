---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning/
title: About node pool auto-creation \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:07.473372+00:00
---

# About node pool auto-creation  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About node pool auto-creation Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) can automatically create and manage node pools in your clusters based on the configuration of your workloads. This document describes how node pool auto-creation works, scaling parameters and default behavior, and provides recommendations that can help you to improve scalability. This document is intended for cluster administrators who want to reduce the costs associated with manual infrastructure management in their Standard mode clusters.

You should already be familiar with the following concepts:

  * [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
  * [About GKE cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)



In Autopilot mode, GKE always creates and manages nodes and node pools for you based on your workloads. You don't need to manually configure node pool auto-creation for Autopilot clusters or for Autopilot workloads in Standard clusters. For more information, see [GKE Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

## What is node pool auto-creation?

In GKE, _node pools_ are logical groups of nodes. Every node in a node pool has the same configuration as every other node in that node pool. Node pool auto-creation is an infrastructure autoscaling mechanism that lets GKE create new node pools in your cluster that meet the requirements of your workloads. GKE manages these auto-created node pools, performing tasks like updating node metadata, creating and deleting nodes in the node pool, and deleting the entire node pool when it's no longer needed. Node pool auto-creation is an extension of the GKE [_cluster autoscaler_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), which automatically scales nodes in individual node pools.

Node pool auto-creation is designed to let GKE automatically scale down and remove empty node pools from your cluster. You can't set a minimum number of nodes that every auto-created node pool must have, because a minimum number greater than zero would prevent the removal of empty node pools. If your use case requires a minimum number of nodes to always run in your cluster, [manually create a node pool with autoscaling enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#adding_a_node_pool_with_autoscaling).

## How it works

Node pool auto-creation extends the GKE cluster autoscaler to let GKE provision new node pools that meet the hardware requirements and resource requests of pending Pods. You can define your hardware requirements in the following ways:

  * Use [_ComputeClasses_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes), which you then select in various Pods by using a node selector. We recommend this method, because you can centrally define common node configurations that multiple workloads can use.
  * Use [node selectors or node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) to request specific GKE node labels in Pod specifications.



GKE configures new node pools based on parameters like the following:

  * CPU, memory, and ephemeral storage [resource requests](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) in your Pods and containers, including any Pods that are managed by DaemonSets.
  * [GPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) and [TPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) requests in Pod specifications or in ComputeClasses.
  * Hardware requirements, such as machine types or boot disk types, in the specifications of pending Pods or in ComputeClasses.
  * [Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) in the specifications of pending Pods that have matching node selectors.



GKE configures the resource capacity of each node in an auto-created node pool to be greater than or equal to the resource requests of your pending Pods. You must ensure that your resource requests are large enough for the Pod to function as expected. If your Pod requests are too low, the Pods won't run as expected after GKE schedules them on auto-created nodes.

### Node metadata configuration

GKE also configures node metadata (like labels, annotations, and node taints) based on your workload requirements, such as in the following examples:

  * If you request the N2 machine series, GKE adds the `cloud.google.com/machine-family: n2` node label to each of the nodes.
  * If you select a ComputeClass in your Pod, GKE adds a node label with the `cloud.google.com/compute-class` key set to the name of that ComputeClass.
  * If your Pod has both a [toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) and a node selector for the same node label, GKE adds node taints for those tolerations to the auto-created nodes.

**Note:** When using custom node labels for workload separation, your Pod specification must include a corresponding toleration for each custom label key used in node selectors or in node affinity or anti-affinity rules. If a required toleration is missing, node pool auto-creation cannot provision nodes for the workload.



### Deletion of auto-created node pools

Node pool auto-creation lets the cluster autoscaler create new node pools and nodes to run incoming pending Pods. If the number of Pods in an auto-created node pool decreases, the cluster autoscaler gradually scales the node pool down. When possible, GKE drains under-utilized nodes in the node pool, consolidates Pods on other nodes, and removes the empty nodes.

If the number of nodes in an auto-created node pool is zero, GKE deletes that node pool. GKE doesn't delete node pools that you exclude from node pool auto-creation, such as manually created node pools. For more information about how the cluster autoscaler scales node pools down, see [How cluster autoscaler works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#how_cluster_autoscaler_works).

### GKE scaling preferences

The following preferences apply when GKE autoscales your infrastructure:

  * **Reduce wasted compute resources** : GKE uses the resource capacity of existing auto-created node pools in your cluster to determine the machine type to use for new node pools. As the size of your cluster increases, GKE prefers to use larger machine types for new node pools, so that more of your Pods can run on each node in the node pool.
  * **Optimize scalability and latency** : GKE always prioritizes scaling up existing, compatible node pools instead of creating new node pools. The strength of this preference increases as the number of distinct node pools in your cluster increases. When the number of distinct node pools approaches the [supported limits for optimal latency and scalability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters), GKE de-prioritizes creating new node pools.



These priorities help to ensure that your clusters have efficient compute resource usage at scale, like in the following example scenarios:

  * In clusters that have a small number of node pools and less resource usage, GKE creates new node pools more frequently and uses smaller machine types for those node pools.
  * In clusters that have a large number of node pools, resource usage is high. GKE creates new node pools less frequently and uses larger machine types for those node pools, so that Pod scheduling can continue while also slowing down progress towards cluster scalability and latency limits.



You can manually control the minimum size of the instances that GKE uses for your auto-created node pools by using a ComputeClass that has the [`priorities.machineFamily` field](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities) and either the `priorities.minCores` field or the `priorities.minMemoryGb` field.

## Enablement methods for node pool auto-creation

GKE can automatically create node pools for specific ComputeClasses or for any workload that uses a compatible configuration, depending on how you configure your cluster.

Enablement methods  
---  
Workload-level (recommended) | In GKE version 1.33.3-gke.1136000 and later, use ComputeClasses to enable node pool auto-creation without using cluster-level node auto-provisioning. GKE creates new node pools only for workloads that select specific ComputeClasses that have auto-creation enabled. Existing workloads in the cluster aren't affected. Even in GKE versions earlier than 1.33.3-gke.1136000, ComputeClasses are the recommended way to request and configure infrastructure for your workloads. ComputeClasses provide unique capabilities and give you a flexible way to optimize scaling in your cluster. For more information, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#benefits).  
Cluster-level | Enable node auto-provisioning for the entire cluster. You must set limits for resources like CPU and memory in your cluster. These limits apply to the entire cluster. The cluster-level configuration is required to enable node pool auto-creation in GKE versions earlier than 1.33.3-gke.1136000. GKE can create new node pools for any pending workload in the cluster by using ComputeClasses or selectors in the Pod specifications.  
  
These configuration methods aren't mutually exclusive. You can use ComputeClasses to auto-create node pools in clusters that use node auto-provisioning. If you use both of these methods to enable node pool auto-creation in a cluster, GKE uses the following order of preference to find the value of a configuration setting to use for a node pool:

  1. **ComputeClass or Pod specification** : if you specify a setting (such as a machine type) in a ComputeClass or in a Pod specification, GKE uses that setting.
  2. **Cluster-level node auto-provisioning default** : if a setting isn't specified in a ComputeClass or a Pod specification, GKE checks whether you set a default value for node auto-provisioning in the cluster. If a cluster-level default value exists, GKE uses that value.
  3. **Cluster-level default** : if a setting isn't specified in ComputeClasses, Pod specifications, or as a default value for cluster-level node auto-provisioning, GKE uses the default value that Google Cloud sets for the cluster.



For example, consider a scenario in which GKE attempts to find a machine type to use for an auto-created node pool. The preceding order of preference applies as follows:

  1. GKE checks whether the Pod specification or the Pod's ComputeClass specifies a machine type.
  2. If the Pod specification or ComputeClass don't specify a machine type, GKE checks whether you set a default machine type for node auto-provisioning in the cluster.
  3. If you didn't set a default machine type for node auto-provisioning, GKE uses the cluster's default machine type.



We recommend that you use only the ComputeClass enablement method in most situations. The following sections provide details about each of these configuration methods, including any limitations and considerations.

### Workload-level enablement with ComputeClasses

You can enable node pool auto-creation for any ComputeClass in your cluster by using one of the following fields in the ComputeClass specification:

  * `nodePoolAutoCreation`: let GKE auto-create node pools as needed. You can still interact with the node pools. GKE implements only the settings or constraints that you configure.
  * `autopilot`: run the workloads that select this ComputeClass in Autopilot mode. Similarly to an Autopilot cluster, GKE fully manages the nodes for you and implements various Autopilot constraints and settings. If you use the `autopilot` field, you can skip this document. For more information, see [About Autopilot mode workloads in Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).



In clusters that use GKE version 1.33.3-gke.1136000 and later, you can use these fields in a ComputeClass without enabling node auto-provisioning at the cluster level.

If you configure node pool auto-creation in a ComputeClass without enabling node auto-provisioning for the cluster, GKE creates new node pools only for workloads that use the ComputeClass. Other workloads aren't affected.

The following example ComputeClass manifest enables node pool auto-creation for any Pod that uses the ComputeClass:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: example-computeclass
    spec:
      priorities:
      - machineFamily: n4
      - machineFamily: c4
      whenUnsatisfiable: ScaleUpAnyway
      **nodePoolAutoCreation :
        enabled: true**
    

### Cluster-level enablement with node auto-provisioning

To enable node pool auto-creation for the entire cluster, you enable the _node auto-provisioning_ feature for the cluster by using the Kubernetes Engine API. Node auto-provisioning lets GKE create new node pools as needed for any workload in the cluster based on Pod specifications or ComputeClass configurations. GKE doesn't manage any existing node pools in the cluster, but you can mark individual node pools as auto-provisioned after you enable node auto-provisioning for the cluster.

Enable node auto-provisioning in situations like the following:

  * You want GKE to automatically create node pools in a cluster that runs a GKE version earlier than 1.33.3-gke.1136000.
  * You want to manually set cluster-wide resource limits. In GKE versions earlier than 1.33.3-gke.1136000, you must set cluster-wide resource limits even if you use ComputeClasses.

**Caution:** At scale, these explicit resource limits might cause stuck Pods. Use a different method, such as [quota adjustments](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota), to control resource usage.
  * You want to use specific features or configurations that aren't supported by ComputeClasses.

  * You want to set default node configuration values for the entire cluster.




After you enable node auto-provisioning, you can configure default values for various node settings by using the Google Cloud CLI or a YAML configuration file.

### Cluster-level resource limits with node auto-provisioning

When you enable node auto-provisioning for an entire cluster, you must also configure limits for resources like CPU, memory, GPUs, and TPUs in the cluster. These limits apply to the sum of all of the resource capacity in the cluster, _including manually created node pools and ComputeClasses_. GKE doesn't create new nodes or node pools if the operation would exceed one of these resource limits.

These cluster-level resource limits are required only if you enable node auto-provisioning in the cluster. In clusters that use GKE version 1.33.3-gke.1136000 and later, you can use node pool auto-creation in ComputeClasses without enabling node auto-provisioning.

If your cluster meets these requirements, we recommend that you use only ComputeClasses to configure auto-created node pools.

## Default settings for auto-created node pools

You can specify default values that GKE applies to auto-created node pools at the workload level or at the cluster level.

  * **Workload-level default settings** : you can use the [`spec.nodePoolConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig) field and the [`spec.priorityDefaults`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorityDefaults) field in the ComputeClass specification to set default values for specific node settings. These default values apply only to the node pools that GKE creates for that ComputeClass.
  * **Cluster-level default settings** : you can set default values for auto-created node pools when you configure node auto-provisioning. To specify default values, you use the gcloud CLI or a YAML configuration file.



These methods of setting defaults aren't mutually exclusive. If you configure default values for a specific setting in a ComputeClass and for the entire cluster, GKE uses the value for the ComputeClass. If the ComputeClass doesn't specify a value for that setting, GKE uses the cluster-level default value instead.

### Cluster-level default settings with a configuration file

When you enable node auto-provisioning, you can use a YAML configuration file to specify cluster-wide default settings for auto-created node pools. You can specify multiple settings in a single configuration file. Some advanced configurations (such as auto-repair settings) can only be specified by using a configuration file.

  * The following example configuration file enables [node auto-repair and auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#node_management) for any new auto-created node pools:
        
        management:
          autoRepair: true
          autoUpgrade: true
        

  * The following example configuration file sets the cluster-wide resource limits for node auto-provisioning and configures multiple default settings:
        
        resourceLimits:
          - resourceType: 'cpu'
            minimum: 4
            maximum: 10
          - resourceType: 'memory'
            maximum: 64
          - resourceType: 'nvidia-tesla-t4'
            maximum: 4
        management:
          autoRepair: true
          autoUpgrade: true
        shieldedInstanceConfig:
          enableSecureBoot: true
          enableIntegrityMonitoring: true
        diskSizeGb: 100
        

This configuration file sets the following default values:

    * Enables [node auto-repair and auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#node_management) for any new auto-created node pools.
    * Enables [Secure boot and integrity monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#node_integrity) for any new auto-created node pools.
    * Sets the boot disk size to 100 GiB for any new auto-created node pools.



After you apply the configuration file to the cluster, GKE uses the settings in the file only for new auto-created node pools in the cluster. The new or modified settings that you specify in the file don't apply to existing node pools that GKE created in the cluster. If you update a value that was previously set for the cluster, GKE uses the new value for all new node pools. For example, if you previously set the default machine series to N2, and you update the value to N4 in your configuration file, all new node pools use N4 machine types.

For more information about how to use the cluster-level configuration file, see [Configure settings with a node auto-provisioning configuration file](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#config_file).

## Node pool auto-creation use cases

The following sections describe some popular use cases and supported hardware for node pool auto-creation. For more information about additional use cases and supported configurations, see the documentation for your specific use case.

**Note:** Cluster-wide node auto-provisioning is required to get auto-created node pools with ComputeClasses in versions earlier than 1.33.3-gke.1136000. In these versions, you must set resource limits for the cluster when you enable node auto-provisioning. For example, if you use ComputeClasses to request TPUs in a version earlier than 1.33.3-gke.1136000, you must also enable node auto-provisioning and set cluster-wide TPU limits. For more information, see Cluster-level enablement with node auto-provisioning.

### Machine series or machine type selection

You can select a Compute Engine machine series or machine type for GKE to use for auto-created node pools in one of the following ways:

  * **ComputeClasses** : use the `machineFamily` or the `machineType` [priority rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#priority-rules).
  * **Pod specifications** : for a machine series, use a node selector for the `cloud.google.com/machine-family` node label. For a machine type, use both the `cloud.google.com/machine-family` and the `node.kubernetes.io/instance-type` node labels. For more information, see [Select a machine series or machine type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#custom_machine_family).



If you don't explicitly select a machine, GKE uses the [E2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) or a machine type that's compatible with the hardware that your workload requests. For example, GKE uses [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) for GPUs and specialized machines for [TPU resources](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).

When you request a machine series or a machine type, ensure that other node selectors and your Pod resource requests are compatible with the specified machine. For example, you can't request a GPU and the N2 machine series at the same time.

#### Supported machine series

You can explicitly request any supported Compute Engine machine series or machine type in a ComputeClass or workload. Your requests can include specific hardware configurations, such as [Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

Node pool auto-creation supports the following machine series only in specific GKE versions:

Machine series | Supported GKE versions  
---|---  
[C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) | 

  * 1.28.15-gke.1159000 and later
  * 1.29.10-gke.1227000 and later
  * 1.30.3-gke.1225000 and later

  
[C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) (VMs) | 

  * 1.30.7-gke.1136000 and later
  * 1.31.3-gke.1056000 and later

  
[C4A bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#c4a-metal) | 

  * `c4a-highmem-96-metal`: 1.35.3-gke.1389000 and later
  * `c4a-standard-96-metal`: Not supported

  
[C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_machine_types) (VMs) | 1.32.3-gke.1717000 and later  
[C4D bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#c4d-metal) | 1.37.0-gke.4713000 and later  
[C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series) | 1.36.0-gke.3009002 and later  
[N4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series) | 1.29.3 and later  
[N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) | 1.34.1-gke.3403001 and later  
[N4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series) | 

  * 1.33.12-gke.1208000 and later
  * 1.34.1-gke.2037000 and later

  
[Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series) | 1.29 and later  
[Z4D machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series) | 1.36.3-gke.1244000 and later  
[Z4M machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series) | 1.37.0-gke.4713000 and later  
  
Other machine series are supported in all GKE versions.

### GPU selection

You can request GPUs for auto-created node pools in one of the following ways:

  * **ComputeClasses** : 
    1. Use the [`gpu`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#gpu) priority rule to configure the GPUs.
    2. Request GPU resources in the Pods.
  * **Pod specifications** : 
    1. Configure cluster-wide GPU limits for node auto-provisioning.
    2. Use node selectors to configure the GPUs.
    3. Request GPU resources in the Pods.



GKE selects a [GPU machine type](https://docs.cloud.google.com/compute/docs/gpus) that's large enough to support the number of GPUs. The number of GPUs that you select affects the CPU and memory capacity of the nodes.

#### GKE version requirements for GPU

  * [**G4 machine series**](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series): 1.34.1-gke.1829001 and later.
  * [**A4X machine series**](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-machine-type): 1.33.4-gke.1036000 and later.
  * [**A3 Ultra machine series**](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms): 1.31.4-gke.1183000 and later.



### Cloud TPU selection

You can request Cloud TPU resources for auto-created node pools in one of the following ways:

  * **ComputeClasses** : use the [`tpu` priority rule](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#tpu) to configure TPUs. Then, request the same number of TPU resources in the Pods. For more information, see [Provision TPUs by using custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#custom-compute-classes).
  * **Pod specifications** : configure cluster-wide TPU limits. Then, use node selectors to configure the TPUs and request TPU resources in the Pods. For more information, see [Configuring Cloud TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#tpu).



Both [single-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#node_pool) and [multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#node_pool) support autoscaling and node pool auto-creation. For node pool auto-creation, GKE creates single-host or multi-host TPU slice node pools with a TPU version and topology that meet the requirements of pending workloads.

#### GKE version requirements for Cloud TPU

Node pool auto-creation supports the following Cloud TPUs only in specific GKE versions:

  * **TPU v3** : 1.31.0 and later.
  * **TPU v5 and TPU v4** : 1.29.0 and later.
  * **TPU Trillium** : 1.32.0 and later.
  * **Ironwood (TPU7x)** : 1.34.1-gke.2541000 or later.



Other Cloud TPU types are supported in all GKE versions. To learn more about the available GKE versions for TPUs, see [Validate TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).

#### Cloud TPU node pool autoscaling

GKE scales automatically created or manually created Cloud TPU node pools that use the cluster autoscaler in one of the following ways:

  * **Single-host TPU slice node pool** : GKE adds or removes TPU nodes in the existing node pool. The node pool might contain any number of TPU nodes between zero and the maximum size of the node pool as determined by the [`--max-nodes`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-nodes) and the [`--total-max-nodes`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--total-max-nodes) autoscaling flags. All of the TPU nodes in the node pool have the same machine type and topology. For more information about how to create a single-host TPU slice node pool, see [Create a single-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#single-host).
  * **Multi-host TPU slice node pool** : GKE atomically scales up the node pool from zero to the number of nodes required to satisfy the TPU topology. For example, with a TPU node pool that has the `ct5lp-hightpu-4t` machine type and a topology of `16x16`, the node pool always has either 64 nodes or zero nodes. GKE scales the node pool down if there are no TPU workloads in the node pool. To scale the node pool down, GKE evicts all scheduled Pods and removes all of the nodes in the node pool. For more information about how to create a multi-host TPU slice node pool, see [Create a multi-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#multi-host).



#### Cloud TPU node pool configuration

GKE uses the configuration in your Pod or ComputeClass to determine the configuration of your TPU nodes. The following manifest is an example of a Deployment specification that requests TPUs in the Pod specification. If the cluster-level node auto-provisioning setting is enabled, this Deployment triggers node pool auto-creation. When you create this example Deployment, GKE creates a node pool that contains a TPU v4 slice with a `2x2x2` topology and two `ct4p-hightpu-4t` machines.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: tpu-workload
      labels:
        app: tpu-workload
    spec:
      replicas: 2
      template:
        spec:
          nodeSelector:
            cloud.google.com/gke-tpu-accelerator: tpu-v4-podslice
            cloud.google.com/gke-tpu-topology: 2x2x2
          containers:
          - name: tpu-job
            image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
            ports:
            - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
            securityContext:
              privileged: true # Required for GKE versions earlier than 1.28 to access TPUs.
            command:
            - bash
            - -c
            - |
              python -c 'import jax; print("Total TPU chips:", jax.device_count())'
            resources:
              requests:
                google.com/tpu: 4
              limits:
                google.com/tpu: 4
            ports:
            - containerPort: 80
    

In this manifest, the following fields define TPU configuration:

  * `cloud.google.com/gke-tpu-accelerator`: the [TPU version and type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, use `tpu7x-standard-4t` for Ironwood (TPU7x).
  * `cloud.google.com/gke-tpu-topology`: the [topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology) with number and physical arrangement of TPU chips within a TPU slice. For example, use `2x2x2`.
  * `limits.google.com/tpu`: the number of [TPU chips per VM](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, if you use `tpu7x-standard-4t`, the number of TPU chips per VM is `4`.



### Spot VM selection

You can select [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) for auto-created node pools in one of the following ways:

  * **ComputeClasses** : use the `spot` field in a [priority rule](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities).
  * **Pod specifications** : use a toleration for the `cloud.google.com/gke-spot="true"` node label with the `NoSchedule` effect. Add a node selector for the `cloud.google.com/gke-spot=true` or the `cloud.google.com/gke-provisioning=spot` node labels. Alternatively, you can select [preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible) by using the `cloud.google.com/gke-preemptible` node label in your toleration and node selector. However, we strongly recommend Spot VMs instead.



### Ephemeral storage configuration

GKE uses a portion of the node boot disk for Pod ephemeral storage. You can customize the size of the boot disk that GKE uses for auto-created nodes in one of the following ways:

  * **ComputeClasses** : use the `storage.bootDiskSize` and the `storage.bootDiskType` fields in a [priority rule](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage). You can configure different boot disk settings for different ComputeClasses.
  * **Pod specifications** : use the `diskSizeGb` and the `diskType` fields in the cluster-level configuration file. You can't control the boot disk size and type for individual Pods by using this method.



For more information, see [Custom boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#custom_boot_disk). If you don't explicitly modify the boot disk settings, the default is a `pd-balanced` volume that has a capacity of 100 GiB.

GKE creates a new node pool only if the [allocatable](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage) ephemeral storage of a node with a specified boot disk is greater than or equal to the ephemeral storage request of a pending Pod. If the ephemeral storage request is greater than the allocatable ephemeral storage of a node, GKE won't create a new node pool and the Pod remains in a pending state. GKE doesn't dynamically adjust boot disk sizes based on your Pod ephemeral storage requests.

### Workload separation

You can request that specific Pods always run on separate nodes from other Pods in the cluster. GKE uses [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to prevent other workloads from running on those nodes. You can configure workload separation in auto-created node pools in the following ways:

  * **ComputeClasses** : the nodes that GKE creates for a specific ComputeClass can only run Pods that select that ComputeClass. You don't need to modify your Pod specifications. You can separate the Pods within a ComputeClass by using [inter-Pod affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity).
  * **Pod specifications** : if you enable node auto-provisioning for the cluster, you can configure workload separation by using fields in the Pod specification. During node pool auto-creation, GKE might create node pools with labels and taints if all of the following conditions are met: 
    * The Pod uses a node selector to request a custom node label key and value. You can't use system node labels for workload separation.
    * The Pod has a [toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for the same node label key.
    * The toleration effect is `NoSchedule`, `NoExecute`, or is unspecified.



For more information about configuring these fields and for limitations, see [Configure workload separation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation).

## Limitations

  * All of the limitations of the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#limitations) also apply to node pool auto-creation.
  * Clusters that have more than 200 total node pools might have increased latency during autoscaling. Any configuration that triggers the creation of a new node pool, such as [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) or the use of multiple ComputeClasses, increases this number. For more information about cluster limits, see [limits and best practices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters) in "Planning large clusters".
  * Any resource limits that you set for the cluster when you enable node auto-provisioning also apply to the node pools that GKE creates for ComputeClasses.
  * The following settings aren't supported by ComputeClasses: 
    * Surge upgrades or blue-green upgrades.
    * Node integrity and secure boot.
  * To enable node pool auto-creation for a [ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) in GKE versions earlier than 1.33.3-gke.1136000, you must also enable cluster-level node auto-provisioning. This limitation doesn't apply in GKE version 1.33.3-gke.1136000 and later.



### Unsupported configurations

GKE doesn't create new node pools that use the following configurations:

  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods)
  * [Windows operating systems](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#windows-server)
  * Autoscaling of [local PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#example_local_pvs).
  * Nodes that use dedicated [local SSDs for Pod ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#creating_a_node_pool_using_ephemeral_storage_on_local_ssds). GKE can, however, create new node pools that use Local SSDs for raw block storage.
  * Nodes that use altered [Filters](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#filter) for custom scheduling.
  * [Simultaneous multi-threading (SMT)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt).
  * [Performance monitoring unit (PMU)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/analyzing-cpu-performance-using-pmu).



The cluster autoscaler can scale nodes in existing node pools that use these configurations.

## What's next

  * Learn how to [configure node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * Read an overview of the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * Learn how to [configure the cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler).
  * Learn about [cluster autoscaler visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility).
  * Learn how to use [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) in GKE.
  * [Troubleshoot custom ComputeClass issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass).
  * Learn how to [deploy a cluster with node auto-provisioning in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-cluster-nap).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
