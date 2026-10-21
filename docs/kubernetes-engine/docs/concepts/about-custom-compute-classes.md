---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes/
title: About custom ComputeClasses \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:09.972186+00:00
---

# About custom ComputeClasses  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About custom ComputeClasses Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can create your own ComputeClasses to control the properties of the nodes that Google Kubernetes Engine (GKE) provisions when autoscaling your cluster. This document is for platform administrators who want to declaratively define autoscaling profiles for nodes, so that specific workloads run on hardware that meets their requirements. For more information about what ComputeClasses are, see [About GKE ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes).

## ComputeClasses overview

In GKE, a _ComputeClass_ is a profile that consists of a set of node attributes that GKE uses to provision the nodes that run your workloads during autoscaling events. ComputeClasses can target specific optimizations, like provisioning high-performance nodes or prioritizing cost-optimized configurations for cheaper running costs. _Custom_ ComputeClasses let you define profiles that GKE then uses to autoscale nodes to closely meet the requirements of specific workloads.

Custom ComputeClasses are available to use in GKE Autopilot mode and GKE Standard mode in version 1.30.3-gke.1451000 and later, and offer a declarative approach to defining node attributes and autoscaling priorities. Custom ComputeClasses are available to configure and use in all eligible GKE clusters by default.

### Benefits of custom ComputeClasses

Custom ComputeClasses offer the following benefits:

  * **Fallback compute priorities** : define a hierarchy of node configurations in each ComputeClass for GKE to prioritize. If the most preferred configuration is unavailable, GKE automatically chooses the next configuration in the hierarchy. This fallback model helps ensure that even when compute resources are unavailable, your workloads still run on optimized hardware with minimal scheduling delays.
  * **Granular autoscaling control** : define node configurations that are best suited for specific workloads. GKE prioritizes those configurations when creating nodes during scaling.
  * **Declarative infrastructure configuration** : adopt a declarative approach to infrastructure management so that GKE automatically creates nodes for you that match your specific workload requirements.
  * **Active migration** : if compute resources for a more preferred machine configuration become available in your location, GKE automatically migrates your workloads to new nodes that use the preferred configuration.
  * **Cost optimization** : prioritize cost-efficient node types like Spot VMs to reduce your cluster expenses.
  * **Default custom ComputeClasses** : set a custom ComputeClass as the default for an entire cluster or for specific Kubernetes namespaces, so that workloads run on optimized hardware even if they don't request a specific ComputeClass.
  * **Custom node consolidation thresholds** : define custom resource usage thresholds for nodes. If a specific node's resource usage falls below your threshold, GKE attempts to consolidate the workloads into a similar, available node and scales down the underutilized node.



### Use cases for custom ComputeClasses

Consider using custom ComputeClasses in scenarios like the following:

  * You want to run your AI/ML workloads on specific GPU or TPU configurations.
  * You want to set default hardware configurations for the workloads that specific teams run, taking the overhead off of the application operators.
  * You run workloads that perform optimally on specific Compute Engine machine series or hardware configurations.
  * You want to declare hardware configurations that meet specific business requirements, like high performance, cost optimized, or high availability.
  * You want GKE to hierarchically fallback to using specific hardware configurations during compute resource unavailability, so that your workloads always run on machines that suit their requirements.
  * You want to centrally decide on the optimal configurations across your enterprise's fleet, so that your costs are more predictable and your workloads run more reliably.
  * You want to centrally specify which of your Compute Engine capacity reservations GKE should use to provision new nodes for specific workloads.
  * You want to specify a compact placement policy to use with GKE Autopilot. For details, see: compact placement.



## How custom ComputeClasses work

Custom ComputeClasses are Kubernetes custom resources that provision Google Cloud infrastructure. You define a `ComputeClass` object in the cluster, and then request that ComputeClass in workloads or set that ComputeClass as the default for a Kubernetes namespace. When a matching workload demands new infrastructure, GKE provisions new nodes in line with the priorities that you set in your ComputeClass definition.

The attributes that you set in your ComputeClasses define how GKE configures new nodes to run workloads. When you modify an existing ComputeClass, all future nodes that GKE creates for that ComputeClass use the modified configuration. GKE doesn't retroactively change the configuration of existing nodes to match your modifications.

Custom ComputeClasses influence autoscaling decisions but are not considered by kube-scheduler. During Pod scheduling, the scheduler might not prioritize nodes with higher custom ComputeClass priorities, even when existing nodes are available across various priorities.

To ensure that your custom ComputeClasses are optimized for your fleet, consider the following guidelines:

  * Understand the compute requirements of your fleet, including any application-specific hardware requirements.
  * Decide on a theme that guides the design of each ComputeClass. For example, a performance-optimized ComputeClass might have a fallback strategy that uses only high-CPU machine types.
  * Decide on the Compute Engine machine family and machine series that most closely fit your workloads. For details, see [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).
  * Plan a fallback strategy within each ComputeClass so that workloads always run on nodes that use similar machine configurations. For example, if the N4 machine series isn't available, you can fall back to C3 machines.



## View the complete custom resource definition

To view the latest custom resource definition (CRD) for the `ComputeClass` custom resource, including all fields and their relationships, refer to the [ComputeClass reference documentation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass).

You can also view the CRD in your cluster by running the following command:
    
    
    kubectl describe crd computeclasses.cloud.google.com
    

## Plan a custom ComputeClass

To effectively plan, deploy, and use a custom ComputeClass in your cluster, you do the following steps:

  1. Choose your fallback compute priorities: Define a series of rules that govern the properties of the nodes that GKE creates for the ComputeClass.
  2. Configure GKE Standard node pools and ComputeClasses: For Standard mode clusters, perform _required configuration steps_ to use the ComputeClass with your node pools.
  3. Define scaling behavior when no priority rules apply: optionally, tell GKE what to do if nodes that meet your priority rules can't be provisioned.
  4. Set autoscaling parameters for node consolidation: tell GKE when to consolidate workloads and remove underutilized nodes.
  5. Configure active migration to higher priority nodes: optionally, tell GKE to move workloads to more preferred nodes as hardware becomes available.
  6. Consume Compute Engine reservations: optionally, tell GKE to consume existing Compute Engine zonal reservations when creating new nodes.



## Choose your fallback compute priorities

The primary advantage of using a custom ComputeClass is to have control over the fallback strategy when your preferred nodes are unavailable due to factors like resource exhaustion and quota limitations.

You create a fallback strategy by defining a list of _priority rules_ in the `priorities` field in the ComputeClass specification. Each priority rule can request nodes in one of the following ways:

  * **Node properties** : define the properties of the nodes that you want Pods to run on, such as machine families to use. When a Pod triggers a scale-up operation, GKE tries to create a node that has those properties. Each priority rule must specify a type of hardware to provision, as described in the Top-level node properties for priority rules section.

  * **Node pool selection** : in GKE Standard clusters, specify the names of existing node pools to associate with the ComputeClass. When a Pod triggers a scale-up operation, GKE tries to place the Pod in those node pools. Priority rules that select node pools don't support any other fields. For more information, see the GKE Standard node pools and ComputeClasses section.




By default, when a new node is needed for an incoming Pod that selects a ComputeClass, GKE attempts to create nodes in the order in which the priority rules appear in the ComputeClass manifest. In GKE version 1.35.2-gke.1842000 and later, you can also explicitly set a score for every priority rule in a ComputeClass by using the `priorityScore` field, in which case GKE processes rules in order from the highest score to the lowest score. If all of the priority rules in a ComputeClass are exhausted, then GKE creates nodes based on the behavior described in Define scaling behavior when no priority rules apply.

### Priority rule scores

_Requires GKE version 1.35.2-gke.1842000 or later._

For granular control over the order in which GKE processes priority rules for a ComputeClass, use the `priorityScore` field in your rules. During scaling, GKE processes your priority rules based on the score, with larger score values having a higher priority than smaller values.

The `priorityScore` field has the following properties:

  * The field accepts an integer value with a minimum value of `1` and a maximum value of `1000`.
  * You must use the `priorityScore` field in all of your priority rules or in none of your priority rules.
  * You can set the same priority score for up to three separate rules. During scaling, GKE processes rules that have the same score together. GKE chooses a specific rule to use based on the [operating criteria of the cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#operating_criteria).

Grouped rules might increase the latency of autoscaling, because GKE must run more simulations to determine the optimal node configuration. The probability of you noticing a latency increase depends on how broad the hardware selection in the rule is, as follows:

    * Rules that have a broad scope, such as the `machineFamily` property, are more likely to contribute to a slight increase in autoscaling latency. However, GKE is more likely to find available hardware that meets the requirements of those rules.
    * Rules that have a narrow scope, such as the `machineType` property, are less likely to contribute to a latency increase. However, GKE is more likely to be unable to find available hardware that meets the requirements of those rules.



The following example shows a ComputeClass that sets priority rule scores:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: priority-rule-score-class
    spec:
      nodePoolAutoCreation:
        enabled: true
      **priorities :
      # Highest priority score in the ComputeClass
      - machineFamily: e2
        spot: true
        priorityScore: 30
      # Grouped priority rules that have the same score.
      - machineFamily: n2
        spot: true
        priorityScore: 20
      - machineFamily: t2d
        spot: true
        priorityScore: 20
      # Lowest priority score in the ComputeClass.
      - machineFamily: n1
        spot: true
        priorityScore: 10**
      whenUnsatisfiable: ScaleUpAnyway
    

During a scale-up event for this example ComputeClass, GKE does the following:

  1. GKE tries to create E2 instances.
  2. If E2 instances aren't available, GKE creates either N2 or T2D instances, depending on the result of the cluster autoscaler.
  3. If N2 and T2D instances aren't available, GKE tries to create N1 instances.
  4. If N1 instances aren't available, GKE falls back to the default machine series for the cluster.



## Top-level node properties for priority rules

When you specify priority rules that define node properties, you must select a top-level hardware type that you want for the nodes. The other properties that you can specify for a rule depend on the top-level property of that rule.

You can use any of the following top-level properties for a rule:

  * `machineFamily`: a Compute Engine machine series, such as `n4`.
  * `machineType`: a specific Compute Engine machine type, such as `n4-standard-32`.
  * `gpu`: a GPU configuration, which might include a GPU type, a specific number of GPUs, and driver configuration.
  * `tpu`: a Cloud TPU configuration, which might include a TPU version, topology, and number of chips.



Accelerator configurations don't require the `machineType` or `machineFamily` field to be explicitly specified unless you use them in combination with reservations.

Each Compute Engine machine series generation supports specific disk types. For example, the N4 machine series supports Hyperdisk ML disk types, but the N2 machine series doesn't. In ComputeClasses that span multiple generations, stateful workloads that request a specific disk type might not be able to access persistent data if the machine type doesn't support that disk type. Depending on how you create and use disks in your workloads, use any of the following methods to reduce the risk of inaccessible persistent data:

  * **Dynamic volume provisioning** : in GKE version 1.35.3-gke.1290000 and later, use a StorageClass that configures [automated disk type selection](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#automated_disk_type_selection). GKE creates a disk type that's compatible with the machine type of the node that runs your workload. In earlier GKE versions, verify that all of the machine series in your ComputeClass support the disk type that your StorageClasses provision.

  * **Pre-existing persistent disks** : verify that all of the machine series in your ComputeClass support the disk types of your pre-existing persistent disks.




For more information about the supported disk types for each machine series, see the [machine series comparison table](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).

### machineFamily configurations

The `machineFamily` field accepts any [Compute Engine machine series that GKE supports](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-support#machine-support), like `n2` or `c3`. If unspecified, the default is `e2`. When you use the `machineFamily` field, GKE provisions nodes from that series with a machine type that is large enough to run your Pods. The autoscaler algorithm determines the most appropriate size based on the aggregate resource requests of all pending Pods. For more control over the exact machine size, use the `machineType` field instead.

Requesting a broader machine family doesn't provision bare metal machine types. For example, requesting `c3` or `c4a` doesn't provision machine types such as `c3-standard-192-metal` or `c4a-standard-72-metal` respectively. Because bare metal node types require requesting an exact machine type, you cannot use the predefined Autopilot `Performance` ComputeClass either. Instead, you must create a custom ComputeClass and specify the exact machine type in the `machineType` field. Using `c3` or `c4a` bare metal machine types with ComputeClasses, node pool auto-creation, or Autopilot mode requires GKE version 1.35.3-gke.1389000 or later.

You can use other `spec.priorities` fields alongside the `machineFamily` field to declaratively define your compute requirements. For example:

  * `spot`: Spot VMs. The default value is `false`.
  * `minCores`: minimum vCPUs per node. The default value is `0`. This field is useful for preventing the creation of nodes that are too small for your needs.
  * `minMemoryGb`: minimum memory per node. The default value is `0`.
  * `storage.bootDiskType`: boot disk type. On Autopilot clusters, only the `pd-balanced` type of `bootDiskType` is supported. Requires GKE version 1.34.1-gke.1431000 or later.
  * `storage.bootDiskSize`: size in GB for the node boot disk. Requires GKE version 1.34.1-gke.1431000 or later.
  * `storage.bootDiskKMSKey`: path to Cloud Key Management Service key to use for boot disk encryption.
  * `storage.secondaryBootDisks`: Persistent Disks that are used to preload GKE nodes with data, such as a machine learning (ML) model or a container image. Requires GKE version 1.31.2-gke.1105000 or later. To set up a secondary boot disk for your cluster to use, see [configure secondary boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading#configure). 
    * `storage.secondaryBootDisks.diskImageName`: the name of the disk image to preload.
    * `storage.secondaryBootDisks.project`: the name of the project to which the disk image belongs. If this value is unspecified, the default is your cluster project.
    * `storage.secondaryBootDisks.mode`: the mode in which the secondary boot disk should be used. If this value is set to `CONTAINER_IMAGE_CACHE`, the secondary boot disk is used as a container image cache. The value must be equal to either `CONTAINER_IMAGE_CACHE` or `MODE_UNSPECIFIED`. If this value is unspecified, the default is `MODE_UNSPECIFIED`.
  * `placement`: the specifics of machine placement: 
    * `policyName`: the name of either a GKE Autopilot [compact placement policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement#compact-placement-autopilot) or a [workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy).
  * `enableNestedVirtualization`: whether to enable [nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization) on the nodes. The default value is `false`.



The following example shows a priority rule that uses `machineFamily`:
    
    
    priorities:
    - machineFamily: n4
      spot: true
      minCores: 16
      minMemoryGb: 64
      storage:
        bootDiskType: hyperdisk-balanced
        bootDiskSize: 100
        bootDiskKMSKey: projects/example/locations/us-central1/keyRings/example/cryptoKeys/key-1
        secondaryBootDisks:
        - diskImageName: pytorch-mnist
          project: k8s-staging-jobset
    

### machineType configurations

The `machineType` field accepts a Compute Engine predefined machine type, like `n4-standard-32`, or a [custom machine type string](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create), like `n4-custom-8-20480`. Using custom machine types requires GKE version 1.33.2-gke.1111000 or later. You can specify machine types from any [machine series that GKE supports](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-support#machine-support).

You can specify other `spec.priorities` fields alongside the `machineType` field to declaratively define your compute requirements, for example:

  * `spot`: use Spot VMs. Default is `false`.
  * `storage`: configure node storage. 
    * `storage.bootDiskType`: boot disk type. On Autopilot, only the `pd-balanced` type of `bootDiskType` is supported.
    * `storage.bootDiskKMSKey`: path to Cloud KMS key to use for boot disk encryption.
    * `storage.bootDiskSize`: size in GB for the node boot disk.
    * `storage.localSSDCount`: number of local SSDs to attach to the node. If specified, must be at least `1`.
  * `enableNestedVirtualization`: whether to enable [nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization) on the nodes. The default value is `false`.



The following example shows a priority rule that uses `machineType` to provision `n4-standard-32` machine types:
    
    
    priorities:
    - machineType: n4-standard-32
      spot: true
      storage:
        bootDiskType: hyperdisk-balanced
        bootDiskSize: 250
        localSSDCount: 2
        bootDiskKMSKey: projects/example/locations/us-central1/keyRings/example/cryptoKeys/key-1
    

### GPU configuration

To select GPUs in your priority rules, specify the type, count, and driverVersion (optional) of the GPU in the `gpu` field of a priority rule. The following fields are supported:

  * `gpu.type`: a GPU type, like `nvidia-l4`. For details, see [Choose GPU support using Autopilot or Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#autopilot-standard-gpus).
  * `gpu.count`: the number of GPUs to attach. For supported quantities by GPU type, see [Supported GPU quantities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#supported-quantities).
  * `gpu.driverVersion`: the NVIDIA driver version to install. Must be `default` or `latest`. Requires GKE version 1.31.1-gke.1858000 or later.
  * `acceleratorNetworkProfile`: The accelerator network profile for the GPU, such as `auto`. _Requires GKE version 1.35.2-gke.1842000 or later._



You can also specify other `spec.priorities` [fields](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities) such as Spot VMs, [storage options](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage), and reservations in combination with the `gpu` fields.

The following example shows a rule for GPUs:
    
    
    priorities:
    - gpu:
        type: nvidia-l4
        count: 1
      storage:
        secondaryBootDisks:
        - diskImageName: big-llm
          project: k8s-llm
      spot: true
    

### TPU configuration

_Requires GKE version 1.31.2-gke.1518000 or later_

To select TPUs in your priority rules, specify the type, count, and topology of the TPU in the `tpu` field of a priority rule. The following fields are required:

  * `tpu.type`: the TPU type, like `tpu-v5p-slice`. For details, see [TPU availability in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#availability-autopilot).
  * `tpu.count`: the number of TPUs to attach.
  * `tpu.topology`: the TPU topology to use, like `"2x2x1"`. For details, see [Choose a topology for Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#autopilot-tpu-topology).



You can also specify other `spec.priorities` [fields](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities) alongside the `tpu` field in your priority rule, for example:

  * `spot`: use Spot VMs. Default is `false`.
  * `storage`: configure node storage. 
    * `storage.bootDiskType`: boot disk type.
    * `storage.bootDiskKMSKey`: path to Cloud KMS key to use for boot disk encryption.
    * `storage.bootDiskSize`: size in GB for the node boot disk.
  * `reservations`: use a Compute Engine reservation. For details, see the Consume Compute Engine reservations section.
  * `location`: 
    * `zones`: a list of Google Cloud zones where GKE can provision nodes. If unspecified, GKE provisions nodes in the zones configured in the cluster's [node auto-provisioning settings](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#locations). If no zones are configured for node auto-provisioning, GKE provisions nodes in any of the standard zones that the control plane uses. 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

    * `zoneTypes`: a list of zone types that specifies a set of Google Cloud zones where GKE can provision nodes. The supported values are `CLUSTER_DEFAULT` (default), `STANDARD`, and `AI`. For more information, see [Using location zoneTypes priority](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-zonal-topology#using-zone-types).



The following example shows a rule for TPUs:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: tpu-class
    spec:
      priorities:
      - tpu:
          type: tpu-v5p-slice
          count: 4
          topology: 4x4x4
        reservations:
          specific:
          - name: tpu-reservation
            project: reservation-project
          affinity: Specific
      - spot: true
        tpu:
          type: tpu-v5p-slice
          count: 4
          topology: 4x4x4
      nodePoolAutoCreation:
        enabled: true
    

This example defines the following fallback behavior:

  1. GKE attempts to provision a 16-node multi-host TPU v5p slice by consuming a shared Compute Engine reservation named `tpu-reservation` from the `reservation-project` project.
  2. If the reservation has no available TPUs, GKE attempts to provision a 16-node multi-host TPU v5p slice running on Spot VMs.
  3. If none of the preceding rules can be satisfied, GKE follows the logic in the Define scaling behavior when no priority rules apply section.



After you deploy a TPU custom ComputeClass to your cluster, select that custom ComputeClass in your workload:

  * **Autopilot workloads** : see the "Provision TPUs by using custom ComputeClasses" section in [Deploy TPU workloads on GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot#custom-compute-classes)
  * **Standard workloads** : see the "Provision TPUs by using custom ComputeClasses" section in [Deploy TPU workloads on GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#custom-compute-classes).



Additionally, for TPU workloads you can do the following:

  * Define workload type
  * Define SLO
  * Group in collections in TPU Trillium (v6e)
  * Target AI zones



#### Target AI zones

You can also use a compute class to specify AI zones for your Pods. [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) are specialized locations within Google Cloud regions optimized for AI/ML workloads. The following compute class sets a prioritized list of zones that includes AI zones:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: accelerator-ai-preferred
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorities:
        # --- Priority 1: TPU in a specific AI zone (On-Demand) ---
        - tpu:
            type: tpu-v5p-slice
            count: 4
            topology: 4x4x4
          location:
            zones:
              - "us-central1-ai1a" # Specify your target AI zone
          # machineFamily: a3 # Optional
    
        # --- Priority 2: TPU in any AI zone (On-Demand)  ---
        - tpu:
            type: tpu-v5p-slice
            count: 4
            topology: 4x4x4
          location:
            zoneTypes:
              - "AI" # All AI zones in the cluster's region
    
        # --- Priority 3: GPU in a specific Standard zone (On-Demand) ---
        - gpu:
            type: nvidia-tesla-a100
            count: 1
          location:
            zones:
              - "us-central1-a" # Fallback to a standard zone
              - "us-central1-b"
      whenUnsatisfiable: DoNotScaleUp

This ComputeClass configures GKE to provision nodes with v5p TPUs or A100 GPUs for the workload. The nodes have the following preferences:

  * **Priority 1:** attempt to provision the TPU in the `us-central1-ai1a` AI zone.
  * **Priority 2:** if the TPU is not available in the specific AI zone, attempt to provision it in any AI zone of the cluster's region.
  * **Priority 3:** if the TPU is not available in AI zones, attempt to provision the GPU in the `us-central1-a` or `us-central1-b` standard zones.
  * If A100 GPUs are not available in any of the specified zones, GKE will not scale up the node pool.



### DRANET network configuration

_Requires GKE version 1.35.2-gke.1842000 or later_

To use GKE managed DRANET to request and allocate network interfaces for Pods, you must enable the feature in your `ComputeClass`. You need to:

  * Enable the DRANET networking driver by setting `nodePoolConfig.dra.networking.enabled` to `true`.
  * Set the `acceleratorNetworkProfile` to `auto` in the `priorities` list.



For more information about how to use DRANET, see [Allocate network resources by using GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra).

## How GKE creates nodes using priority rules

When you deploy a workload that requests a ComputeClass and a new node is needed, GKE processes the list of rules in the `priorities` field of the `ComputeClass` specification in order of appearance or, if the `priorityScore` field is set, from the highest to the lowest score.

For example, consider the following specification:
    
    
    spec:
      ...
      priorities:
      - machineFamily: n4
        spot: true
        minCores: 64
      - machineFamily: n4
        spot: true
      - machineFamily: n4
        spot: false
    

When you deploy a workload that requests a ComputeClass with these priority rules, GKE matches nodes as follows:

  1. GKE places Pods on any existing nodes that are associated with this ComputeClass.
  2. If existing nodes can't accommodate the Pods, GKE provisions new nodes that use the N4 machine series, are Spot VMs, and have at least 64 vCPU.
  3. If N4 Spot VMs with at least 64 vCPU aren't available in the region, GKE provisions new nodes that use N4 Spot VMs that can fit the Pods, regardless of the number of cores.
  4. If no N4 Spot VMs are available in the region, GKE provisions new on-demand N4 VMs.
  5. If none of the preceding rules can be satisfied, GKE follows the logic in the Define scaling behavior when no priority rules apply section.



## Default values for priority rules

You can set default values for some of the fields in the priority rules of your ComputeClass specification. These default values apply if the corresponding fields in a specific rule are omitted. You can set these default values by using the `priorityDefaults` field in your ComputeClass specification.

The `priorityDefaults` field has the following limitations:

  * Requires GKE version 1.32.1-gke.1729000 or later.
  * Isn't compatible with the `nodepools` priority rule, which doesn't contain any fields.



For details about the types of default values that you can set, see the `priorityDefaults` section in the [ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorityDefaults).

## GKE Standard node pools and ComputeClasses

If you use GKE Standard mode, you might have to perform manual configuration to ensure that your ComputeClass Pods schedule as expected.

  * **Auto-created node pools** : no manual configuration required. GKE automatically performs ComputeClass configuration steps for you. For details, see Node pool auto-creation and ComputeClasses.
  * **Manually-created node pools** : manual configuration is required. You must add node labels and node taints to your manually created node pools to associate the nodes with a specific ComputeClass. For details, see Configure manually-created node pools for ComputeClass use.



### Configure manually-created node pools for ComputeClass use

If your GKE Standard clusters have node pools that you manually created, you must configure those node pools to associate them with specific ComputeClasses. GKE only schedules Pods that request a specific ComputeClass on nodes in node pools that you associate with that ComputeClass. This requirement doesn't apply to a ComputeClass that you configure as the [cluster-level default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes#cluster-default-computeclass).

GKE Autopilot mode and auto-created node pools in GKE Standard mode perform this configuration for you.

To associate a manually created node pool with a ComputeClass, you add _node labels_ and _node taints_ to the node pool during creation or during an update by specifying the `--node-labels` flag and the `--node-taints` flag, as follows:

  * **Node label** : `cloud.google.com/compute-class=COMPUTE_CLASS`
  * **Taint** : `cloud.google.com/compute-class=COMPUTE_CLASS:NoSchedule`



In these attributes, `COMPUTE_CLASS` is the name of your custom ComputeClass.

For example, the following commands together update an existing node pool and associate the node pool with the `dev-class` ComputeClass:
    
    
    gcloud container node-pools update dev-pool \
        --cluster=example-cluster \
        --node-labels="cloud.google.com/compute-class=dev-class"
    
    gcloud container node-pools update dev-pool \
        --cluster=example-cluster \
        --node-taints="cloud.google.com/compute-class=dev-class:NoSchedule"
    

You can associate each node pool in your cluster with one custom ComputeClass. Pods that GKE schedules on these manually-created node pools only trigger node creation inside those node pools during autoscaling events.

### Node pool auto-creation and ComputeClasses

You can use node pool auto-creation with a custom ComputeClass to let GKE automatically create and delete node pools based on your priority rules.

To let GKE automatically create node pools for a ComputeClass, you must do the following:

  1. Add the `nodePoolAutoCreation` field with the `enabled: true` value to your `ComputeClass` specification.
  2. If your cluster is running a version earlier than GKE version 1.33.3-gke.1136000, you must also [enable cluster-level node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable-cluster-level).



GKE can then create new node pools for Pods that use your ComputeClass. GKE decides whether to scale up an existing node pool or create a new node pool based on factors like the size of the clusters and Pod requirements. Pods with ComputeClasses that don't configure node pool auto-creation continue to only scale up existing node pools.

You can use ComputeClasses that enable node pool auto-creation alongside ComputeClasses that interact with manually created node pools in the same cluster.

Consider the following interactions with node pool auto-creation:

  * You can't use the [machine family](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#custom_machine_family) or the [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#spotvms-nap) node selectors because these selectors conflict with ComputeClass behavior. GKE rejects any Pods that request a ComputeClass and also request Spot VMs or specific machine series.
  * If you [set a default ComputeClass for your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes#cluster-default-computeclass), Pods that use a machine family node selector only trigger node creation for that default class in one of the following situations:

    * The Pods select a machine family that matches one of the priority rules in the cluster-level default class. For example, a Pod that selects N4 instances triggers node creation if the cluster-level default class has a priority rule for N4 instances.
    * The cluster-level default ComputeClass has a value of `ScaleUpAnyway` in the `spec.whenUnsatisfiable` field. Even if the Pods select a machine family that isn't in the ComputeClass priorities, GKE creates new nodes with that machine family.

Pods that select a machine family that isn't in the cluster-level default class priorities won't trigger node creation if the ComputeClass has a value of `DoNotScaleUp` in the `whenUnsatisfiable` field.

  * You can configure node pool auto-creation for ComputeClasses that use the `nodepools` field to reference existing node pools. GKE processes the priorities in order and attempts to scale the existing node pools up to place your Pods.




Consider the following example for a cluster that has both manually-created node pools and node pool auto-creation:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: my-class
    spec:
      priorities:
      - nodepools: [manually-created-pool]
      - machineFamily: n4
      - machineFamily: c4
      nodePoolAutoCreation:
        enabled: true
    

In this example, GKE attempts to do the following:

  1. Create new nodes in the `manually-created-pool` node pool.
  2. Provision N4 nodes, either in existing N4 node pools or by creating a new node pool.
  3. If GKE can't create N4 nodes, it attempts to scale up existing C4 node pools or create new C4 node pools.



### Target specific node pools in a ComputeClass definition

The `priorities.nodepools` field lets you specify a list of manually created node pools on which GKE attempts to schedule Pods in no specific order in GKE Standard clusters that use cluster autoscaling. This field only supports a list of node pools; you can't specify additional machine properties like the machine series in the same priority rule. When you deploy a workload that requests a ComputeClass that has named node pools, GKE attempts to schedule the pending Pods in those node pools. GKE might create new nodes in those node pools to place the Pods.

The node pools that you specify in the `priorities.nodepools` field _must_ be associated with that ComputeClass by using node labels and node taints, as described in the Configure manually created node pools for ComputeClasses section.

The list of node pools that you specify in the `nodepools` field has no priority. To configure a fallback order for named node pools, you must specify multiple separate `priorities.nodepools` items. For example, consider the following specification:
    
    
    spec:
      ...
      priorities:
      - nodepools: [pool1, pool2]
      - nodepools: [pool3]
    

In this example, GKE first attempts to place pending Pods that request this ComputeClass on existing nodes in node pools that are labeled with the ComputeClass. If existing nodes aren't available, GKE tries to provision new nodes in `pool1` or `pool2`. If GKE can't provision new nodes in these node pools, GKE attempts to provision new Pods in `pool3`.

## Define scaling behavior when no priority rules apply

The `ComputeClass` custom resource lets you specify what GKE should do if there are no nodes that can meet any of the priority rules. The `whenUnsatisfiable` field in the specification supports the following values.

**Best practice:** If you omit this field, the default behavior depends on the GKE version of your cluster. To avoid unexpected scaling behavior after a version upgrade, explicitly specify this field in your ComputeClass manifest.

  * `ScaleUpAnyway`: create a new node that uses the cluster's default machine configuration. In GKE versions earlier than 1.33, this is the default behavior if you omit this field.

GKE takes one of the following actions:

    * In Autopilot clusters, GKE places the Pod on a new or existing node, regardless of the node machine configuration.
    * In Standard clusters that don't use node pool auto-creation, GKE tries to scale up any manually created node pool that defines a label and taint matching a given ComputeClass.
    * In Standard clusters that use node pool auto-creation, GKE might create a new node pool that uses the default E2 machine series to place the Pod.
  * `DoNotScaleUp`: leave the Pod in the `Pending` status until a node that meets the ComputeClass requirements is available. In GKE version 1.33 and later, this is the default behavior if you omit this field.




## Request a placement policy

Starting with GKE version 1.33.2-gke.1335000, in GKE Autopilot clusters, you can use compact placement with a custom placement policy or workload policy. For more information, see [Comparison of compact placement policy and workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#comparison).

Both placement policy and workload policy place nodes physically close together to reduce network latency. To use a specific policy, you provide its name in a `policyName` field. The policy must be a Compute Engine resource policy that already exists in the GKE project.

Consider the following example:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: my-class
    spec:
      priorities:
      - machineFamily: n4
        placement:
          policyName: my-placement-policy
      nodePoolAutoCreation:
        enabled: true
    

In this configuration, GKE applies the compact placement policy for all workloads that use this ComputeClass and provisions their nodes according to the existing resource policy named `my-placement-policy`.

## Set autoscaling parameters for node consolidation

By default, GKE removes nodes that are underutilized by running workloads, consolidating those workloads on other nodes that have capacity. For all ComputeClasses, this is the default behavior because all clusters that use ComputeClasses must use the cluster autoscaler or are Autopilot clusters. During a node consolidation, GKE drains an underutilized node, recreates the workloads on another node, and then deletes the drained node.

The timing and criteria for node removal depends on the [autoscaling profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles). You can fine-tune the resource underutilization thresholds that trigger node removal and workload consolidation by using the `autoscalingPolicy` section in your custom ComputeClass definition. You can fine-tune the following parameters:

  * `consolidationDelayMinutes`: the number of minutes after which GKE removes underutilized nodes
  * `consolidationThreshold`: the utilization threshold for CPU and memory as a percentage of the node's available resources. GKE only considers nodes for removal if the resource utilization is less than this threshold.
  * `gpuConsolidationThreshold`: the utilization threshold for GPU as a percentage of the node's available resources. GKE only considers nodes for removal if the resource utilization is less than this threshold. Consider setting this to `100` or to `0` so that GKE consolidates any nodes that don't have 100% utilization of attached GPUs.



Consider the following example:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: my-class
    spec:
      priorities:
      - machineFamily: n4
      - machineFamily: c4
      autoscalingPolicy:
        consolidationDelayMinutes: 5
        consolidationThreshold: 70
    

In this configuration, GKE removes unused nodes after five minutes, and nodes only become candidates for consolidation if both their CPU and memory utilization is less than 70%.

## Active migration

Active migration is an optional autoscaling feature in ComputeClasses that automatically replaces existing nodes with new nodes. The following types of active migration are supported:

  * `optimizeRulePriority`: GKE replaces nodes that use a lower-priority configuration with nodes that use a higher-priority configuration. This option helps you to ensure that your Pods eventually run on your most preferred node configuration, even if GKE originally had to run those Pods on a less preferred node configuration.
  * `ensureAllDaemonSetPodsRunning`: GKE replaces nodes that have unschedulable DaemonSet Pods with larger nodes that can run all of the required DaemonSet Pods. This option helps you to ensure that all of your DaemonSets eventually run on your nodes.



During an active migration, GKE does the following:

  1. GKE creates a new node with a configuration that meets the requirements of the active migration type.
  2. GKE cordons the existing node so that new Pods don't run on that node.
  3. GKE drains the existing node, which evicts Pods from the node. The following factors affect how quickly the node is drained:

     * [PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
     * [`terminationGracePeriodSeconds`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-flow)

Kubernetes controllers, such as Deployments or Jobs, create Pods to replace evicted Pods. GKE schedules these new Pods on the new node.

  4. After the existing node is drained, GKE deletes the node.




Active migration doesn't affect Pods and nodes in the following scenarios:

  * Active migration doesn't evict Pods that have the `cluster-autoscaler.kubernetes.io/safe-to-evict: "false"` annotation.
  * Active migration doesn't evict Pods if the eviction would violate a PodDisruptionBudget.
  * Active migration doesn't replace nodes that can't be removed. For example, active migration doesn't replace a node if doing so violates the `--min-nodes` node pool setting.



Before you enable active migration for a ComputeClass, consider the following potential effects:

  * Active migration doesn't migrate data that's stored in persistent storage, such as Compute Engine Persistent Disks. To minimize the risk of data loss, don't enable active migration in ComputeClasses that stateful workloads use.
  * In Standard clusters, if you use node pool auto-creation, active migration might trigger the creation of new node pools if existing node pools don't meet the criteria defined in your ComputeClass.
  * Workloads using persistent volumes with zonal resources such as Hyperdisk might not work well with active migration. Zonal restrictions and the machine type restrictions of some Hyperdisk products can reduce the effectiveness of active migration. Also, some stateful workloads might not tolerate the disruption caused by active migration.
  * If you update an existing ComputeClass to enable active migration, GKE migrates existing Pods to new nodes when compute resources become available.



### Active migration to higher priority nodes

The `optimizeRulePriority` active migration type lets GKE replace existing nodes that use a lower-priority configuration with nodes that use a higher-priority configuration.
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: my-class
    spec:
      priorities:
      - machineFamily: n4
      - machineFamily: c4
      activeMigration:
        optimizeRulePriority: true
    

If N4 nodes were unavailable when you deployed a Pod with this ComputeClass, GKE would have used C4 nodes as a fallback option. If N4 nodes become available to provision later, like if your quota increases or if N4 VMs become available in your location, the following steps happen:

  1. GKE creates a new N4 node.
  2. GKE cordons and drains the existing C4 node. Your Pods are evicted, respecting any PodDisruptionBudgets and graceful termination configurations.
  3. Kubernetes controllers create Pods to replace your evicted Pods. These new Pods run on the N4 node.
  4. After the C4 node is drained, GKE deletes the node.



Similarly, if you use the `priorityScore` field to set explicit scores for your priority rules, GKE replaces nodes that have a lower score with nodes that have a higher score.

### Active migration to run unschedulable DaemonSet Pods

The `ensureAllDaemonSetPodsRunning` active migration type lets GKE automatically replace existing nodes that have unschedulable DaemonSet Pods with larger nodes that can run those DaemonSet Pods.

For example, the following ComputeClass specification configures the N4 machine family:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: my-class
    spec:
      priorities:
      - machineFamily: n4
      activeMigration:
        ensureAllDaemonSetPodsRunning: true
    

Consider a scenario in which you created a single-Pod Deployment that used this ComputeClass and requested two vCPUs. To run this Pod, GKE created an `n4-standard-2` node. Later, you create a DaemonSet that also requests two vCPUs. The DaemonSet Pod can't run on the `n4-standard-2` node. In this scenario, GKE does the following:

  1. GKE creates a node that uses a larger N4 machine type, such as `n4-standard-4`, which can run your Pod and the DaemonSet Pod. The pending DaemonSet Pod gets scheduled on this new node.
  2. GKE cordons and drains the `n4-standard-2` node.
  3. When your Pod is evicted, the Deployment creates a replacement Pod. GKE schedules this Pod on the `n4-standard-4` node, alongside the DaemonSet Pod.
  4. After the `n4-standard-2` node is drained, GKE deletes the node.



## Consume Compute Engine reservations

_Available in GKE version 1.31.1-gke.2105000 and later_

If you use Compute Engine [_capacity reservations_](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to get a higher level of assurance of hardware availability in specific Google Cloud zones, you can configure each fallback priority in your custom ComputeClass so that GKE consumes reservations when creating new nodes.

To consume Compute Engine reservations by using a custom ComputeClass, you can use the following methods:

  * **Node pool auto-creation** : GKE automatically creates new node pools to consume your specified reservations. For more information, see Node pool auto-creation and ComputeClasses.
  * **Manually created node pools** : on Standard mode clusters, you can route workloads to manually created node pools by specifying the `spec.priorities.nodepools` field in your ComputeClass.



Starting in GKE version 1.36.0-gke.3204000, you can configure your workloads to consume any matching reservation without falling back to on-demand capacity by using the `AnyThenFail` affinity setting.

### Consume reservations in manually created node pools

To consume reservations in manually created node pools in Standard clusters by using ComputeClasses, follow these steps:

  1. Bind the reservations to the node pools by following the steps in [Consuming reserved instances in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#consuming_reserved_instances_in).

  2. Create a ComputeClass that uses the `nodepools` priority rule to select your manually created node pools.




For example, consider a scenario in which you have two node pools, each of which you linked to a separate capacity reservation. You prefer that Pods use the reserved capacity in the `reservation-pool-1` node pool instead of the `reservation-pool-2` node pool. The ComputeClass that implements these preferences is similar to the following example:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: manual-pool-reservations
    spec:
      priorities:
      - nodepools: ['reservation-pool-1']
      - nodepools: ['reservation-pool-2']
    

In this example, GKE tries to place Pods in the `reservation-pool-1` first, because that priority rule appears first in the `priorities` field.

### Auto-create node pools to consume reservations

If you use node pool auto-creation, you can request that GKE uses capacity reservations to create node pools for specific priority rules. To consume reservations in auto-created node pools, you must meet the following requirements:

  * The ComputeClass must enable node pool auto-creation.
  * Non-TPU reservations can be used only when either the `machineType` or `machineFamily` is defined.
  * ComputeClasses that configure local SSDs must use the `machineType` priority rule, not `machineFamily`. For details, see the machineType rule type section.
  * ComputeClasses that specify reservations for a `machineType` that has attached local SSDs must include a `localSSDCount:` field explicitly.



Consider the following example ComputeClass specification, which prioritizes a specific shared reservation for use when provisioning `a3-highgpu-1g` instances. If the prioritized instance types aren't available, GKE then falls back to any matching reservations in the specification:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: accelerator-reservations
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorities:
      - machineType: a3-highgpu-1g
        storage:
          localSSDCount: 2
        gpu:
          type: nvidia-h100-80gb
          count: 1
        **reservations :
          specific:
          - name: a3-shared-reservation
            project: reservation-project
          affinity: Specific**
      - machineType: a3-highgpu-1g
        storage:
          localSSDCount: 2
        gpu:
          type: nvidia-h100-80gb
          count: 1
        **reservations :
          affinity: AnyBestEffort**
      whenUnsatisfiable: DoNotScaleUp
    

If you deploy a Pod that uses the `accelerator-reservations` ComputeClass, GKE first attempts to use the `a3-shared-reservation` reservation when creating new `a3-highgpu-1g` instances to run the Pod. If this specific reservation doesn't have available capacity, GKE tries to scale up `a3-highgpu-1g` instances by using any matching reservation. If no reservations are accessible, GKE falls back to `a3-highgpu-1g` Spot VMs. Finally, if no Spot VMs are available, the scale operation fails.

In this example, both priority rules with reservation references explicitly require the `localSSDCount:` field because the `a3-highgpu-1g` machine shape includes local SSDs.

The following example shows a shared specific reservation, which falls back to Spot VMs, and then finally to on-demand VMs:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: shared-specific-reservations
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorities:
      - machineFamily: n4
        **reservations :
          specific:
          - name: n4-shared-reservation
            project: reservation-project
          affinity: Specific**
      - machineFamily: n4
        spot: true
      - machineFamily: n4
      whenUnsatisfiable: DoNotScaleUp
    

You can consume the following types of reservations:

  * **Specific single-project reservations** : configure the following fields:

    * Specify the reservation name in the `reservations.specific.name` field.
    * Ensure that the value of the `reservations.affinity` field is `Specific`.
  * **Specific shared reservations** : configure the following fields:

    * Specify the reservation name in the `reservations.specific.name` field.
    * Specify the project ID of the project that owns the reservation in the `reservations.specific.project` field.
    * Ensure that the value of the `reservations.affinity` field is `Specific`.
  * **Any matching reservations with fallback** : configure the following fields:

    * Ensure that the value of the `reservations.affinity` field is `AnyBestEffort`.
    * Don't set a reservation name or project.
  * **Any matching reservations without fallback** : configure the following fields:

    * Ensure that the value of the `reservations.affinity` field is `AnyThenFail`.
    * Don't set a reservation name or project.
    * Optional. To strictly enforce the failure if any matching reservations are exhausted, configure the `whenUnsatisfiable: DoNotScaleUp` setting at the `spec` level of the ComputeClass.



TPU reservations require Specific affinity. The `reservations.affinity: AnyBestEffort` and `reservations.affinity: AnyThenFail` settings are not supported.

If GKE can't find available capacity in a reservation, the resulting behavior depends on the type of reservation being selected in the ComputeClass priority rule, as follows:

  * **Specific reservations** : GKE tries the next priority rule in the ComputeClass.
  * **Any matching reservations with fallback (`AnyBestEffort`)**: GKE tries to provision an on-demand node that meets the requirements of that priority rule. If GKE can't provision an on-demand node, GKE tries the next priority rule in the ComputeClass.
  * **Any matching reservations without fallback (`AnyThenFail`)**: GKE skips provisioning an on-demand node and tries the next priority rule in the ComputeClass. If no other rules apply, the scale operation fails depending on the value of `whenUnsatisfiable` setting.



If GKE can't meet the requirements of any of the priority rules for the ComputeClass, the behavior when no rules apply occurs.

### Consume specific reservation blocks

Starting with GKE version 1.31.4-gke.1072000, you can target a specific reservation block within a hardware-backed reservation. This feature is available for the **A3 Ultra** and **A4** machine types.

To consume a specific reservation block, configure your ComputeClass resource as shown in this example:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: specific-reservations
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorities:
      - machineFamily: a3
        gpu:
          type: nvidia-h200-141gb
          count: 8
        **reservations :
          specific:
          - name: a3ultra-specific-reservation
            reservationBlock:
              name: RESERVATION_BLOCK_NAME
          affinity: Specific**
    

Replace RESERVATION_BLOCK_NAME with the target reservation block name.

Starting with GKE version 1.33.1-gke.1788000, you can target a specific reservation sub-block within a reservation block. This feature is available for the **A4X** machine type.

To consume a specific reservation sub-block, configure your ComputeClass resource as shown in the example in [Consume specific reservation sub-blocks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#autopilot-reservation-sub-block).

When you use this feature, be aware of these considerations:

  * These features apply only to _specific reservations_ in either a single or a shared project.



## Customize the node system configuration

You can customize certain parameters in the kubelet and the Linux kernel by using the `nodeSystemConfig` field in your ComputeClass specification. You can specify this field in any priority rule that defines a Compute Engine machine series or machine type. You can also set default global values for any node system configuration fields that are omitted in priority rules by adding the `nodeSystemConfig` field to the `priorityDefaults` field in your ComputeClass.

This feature is available in GKE version 1.32.1-gke.1729000 and later.

For more information, see the following:

  * [ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodeSystemConfig)
  * [Customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config)



## Specify node labels and taints

In your ComputeClass specification, the `nodeLabels` and `taints` fields let you define configurations that both match existing node pools and govern the creation of new ones. These configurations can be applied globally within the `nodePoolConfig` field for the entire ComputeClass or scoped to a specific priority using the `priority` field; however, you must ensure that labels and taints defined at the priority level don't overlap with those that were set globally.

These features are available in the following:

  * Priority node labels in GKE version 1.33.2-gke.1111000 and later.
  * Priority taints in GKE version 1.33.4-gke.1350000 and later.
  * Global node labels and taints in GKE version 1.34.1-gke.3084002 and later.



In addition to custom labels, GKE automatically assigns the `cloud.google.com/compute-class` system label to all nodes provisioned for or associated with a ComputeClass. You can filter and list nodes by ComputeClass:
    
    
    kubectl get nodes -l cloud.google.com/compute-class=COMPUTECLASS_NAME
    

For more information, see [ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass).

### Configure the default Arm architecture taint

By default, GKE adds the `kubernetes.io/arch=arm64:NoSchedule` taint to all Arm nodes, including nodes created for custom ComputeClasses. GKE schedules only workloads that have a toleration for this taint on the Arm nodes, which helps to prevent x86 workloads from running on incompatible architecture. If your workloads are compatible with both x86 and Arm, then you can disable this default taint. Any workload that selects the ComputeClass can run on the Arm nodes, even if those workloads don't have the toleration for Arm architecture.

You can update the default taint behavior in Standard node pools, and with nodes created for custom ComputeClasses. For more information about configuring the behavior for Standard node pools, see [Configure the default Arm architecture taint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#configure-default-taint).

To change the default behavior and let GKE schedule workloads that don't have a corresponding toleration to Arm nodes that are created for a custom ComputeClass, configure your ComputeClass as shown in this example:
    
    
    taintConfig:
      architectureTaintBehavior: NONE
    

This field requires a cluster running GKE version 1.36.2-gke.1498000 or later.

## Default ComputeClasses for clusters and namespaces

You can configure GKE to apply a ComputeClass by default to Pods that don't select a specific ComputeClass. You can define a default ComputeClass for specific namespaces or for an entire cluster. For more information about how to configure your clusters or namespaces with a default class, see [Apply ComputeClasses to Pods by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).

## Group node pools

Starting with GKE version 1.32.2-gke.1359000, you can group multiple node pools into a single logical unit called a _collection_ by using the `nodePoolGroup` field in your ComputeClass specification. This grouping lets you apply shared configurations across many node pools.

### TPU multi-host collection

_Requires GKE version 1.31.2-gke.1518000 or later. Only available in TPU Trillium (v6e)_

You can group your TPU multi-host deployment to set a Service Level Objective (SLO) across all node pools within the collection. To group node pools, specify the name of the group in the `nodePoolGroup` field. All node pools provisioned using this ComputeClass belong to the same group.
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: tpu-multi-host-collection
    spec:
      nodePoolGroup:
        name: my-tpu-collection
      ...
    

For more information, see the following:

  * [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus)
  * [Multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host)
  * [Schedule TPU collections for inference workloads](https://docs.cloud.google.com/tpu/docs/collection-scheduling)



## Node pool configuration

The `nodePoolConfig` field in your ComputeClass specification lets you apply configuration that is reflected in all nodes within the node pools created using that class.

### Specify image type

You can specify the base operating system for the nodes in the node pool by using the `imageType` field. This field lets you choose an image type for the node pools that will run on the nodes. If you omit this field, the default value is `cos_containerd`. The following example shows how to specify the `imageType` in your ComputeClass:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: my-node-pool-config
    spec:
      nodePoolConfig:
        imageType: cos_containerd
    

For more information, see the [Node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

### Service account

The `serviceAccount` field specifies the Google Cloud service account used by the nodes within node pools that are managed by the ComputeClass. The following example shows how to specify the `serviceAccount` in your ComputeClass:
    
    
    spec:
      nodePoolConfig:
        serviceAccount: my-service-account@my-project.iam.gserviceaccount.com
    

For more information, see [About service accounts in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts).

### Define workload type for TPU SLO

Starting with GKE version 1.32.2-gke.1359000, you can define the Service Level Objective (SLO) for your TPU workloads by using the `workloadType` field within `nodePoolConfig`. The value in this field tells GKE the intended use for the TPU resources. The `workloadType` field supports the following values:

  * `HIGH_AVAILABILITY`: use this value for availability-focused workloads, such as inference serving, to limit and streamline interruptions.
  * `HIGH_THROUGHPUT`: use this value for batch or training jobs that require all underlying infrastructure to run most of the time to make progress. This value can be used only when `nodePoolGroup` is also specified.



The following example defines a ComputeClass for a multi-host TPU collection optimized for high-availability inference workloads.
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: multi-host-inference
    spec:
      nodePoolGroup:
        name: my-inference-collection
      nodePoolConfig:
        workloadType: HIGH_AVAILABILITY
      nodePoolAutoCreation:
        enabled: true
      priorities:
      - tpu:
          type: tpu-v6e-slice
          topology: 2x4
    

For more information, see the following:

  * [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)
  * [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus)



### Sandbox configuration

_Requires GKE version 1.36.2-gke.1368000 or later_

You can isolate workloads from the host kernel of nodes by running the Pods in _sandboxes_ by using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods). In ComputeClasses, you can enable GKE Sandbox and select a sandbox type for the nodes by using the `nodePoolConfig.sandbox` field. The following sandbox types are supported:

  * `gvisor`: requires GKE version 1.36.2-gke.1368000 or later.
  * `microvm`: requires GKE version 1.37.0-gke.4713000 or later and nodes that use nested virtualization.



For more information about the features, limitations, and requirements of these sandbox types, see [About GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

To use a ComputeClass to enable and request sandboxes, see [Isolate workloads by using GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).

### Instance metadata configuration

_Requires GKE version 1.36.2-gke.1498000 or later._

The `instanceMetadata` field in a ComputeClass specification lets you add custom metadata key-value pairs directly into the Compute Engine VM instances provisioned for your node pools by Cluster Autoscaler or Node Auto-provisioning. This is analogous to specifying the `--metadata` flag when creating node pools manually with the Google Cloud CLI.

Custom instance metadata configuration using ComputeClasses is supported only on GKE Standard mode clusters (`spec.autopilot.enabled: false`).

You can specify `instanceMetadata` in two places within a ComputeClass:

  * **Global configuration (`spec.nodePoolConfig.instanceMetadata`)**: applies custom metadata key-value pairs globally to all new node pools and VMs created by the ComputeClass.
  * **Priority-specific overrides (`spec.priorities[].instanceMetadata`)**: applies custom metadata key-value pairs only when GKE provisions nodes using that specific priority in the hierarchy.



If the same metadata key is defined in both `nodePoolConfig.instanceMetadata` and `priorities[].instanceMetadata`, the value specified in `priorities[].instanceMetadata` overrides the global value.

#### Schema and validation rules

When defining `instanceMetadata`, adhere to the following validation constraints:

  * **Type** : key-value pairs structured as a `map` (`map[string]string`).
  * **Size limits** : 
    * The maximum size of an individual metadata value is 32 KB (32,768 bytes).
    * The maximum combined size of all metadata key-value pairs across the entire `ComputeClass` resource cannot exceed 512 KB (524,288 bytes).
  * **Key limits and formatting** : 
    * You can define a maximum of 32 custom metadata key-value pairs per `ComputeClass`.
    * Keys must be fewer than 128 characters long and can contain only alphanumeric characters, hyphens (`-`), and underscores (`_`).
  * **Reserved keys** : GKE and Compute Engine reserve specific system metadata keys required to manage cluster operations (such as `kube-env`, `user-data`, `startup-script`, and `cluster-name`). You cannot override or specify reserved system metadata keys.
  * **Immutability on existing node pools** : modifying `instanceMetadata` on an existing `ComputeClass` applies only when GKE provisions new node pools (when `nodePoolAutoCreation` is enabled). Existing node pools and VMs are not retroactively modified.



The following example shows how to configure both global instance metadata across all node pools and a priority-specific metadata override:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: metadata-example-class
    spec:
      nodePoolAutoCreation:
        enabled: true
      nodePoolConfig:
        instanceMetadata:
          environment: "production"
          team: "backend-platform"
      priorities:
      - machineFamily: n4
        instanceMetadata:
          workload-tier: "high-performance"
      - machineFamily: e2
        instanceMetadata:
          workload-tier: "fallback-general"
          team: "shared-infra"
    

## Configure autoscaling limits

_Available in GKE version 1.36.2-gke.2064000 and later._

By default, GKE provisions new nodes for a ComputeClass up to the overall cluster [autoscaling limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_limits). To enforce stricter resource boundaries for a specific ComputeClass, such as limiting the maximum number of GPUs, CPUs, or total nodes that can be provisioned for the ComputeClass, you can apply a CapacityQuota custom resource.

For more information, see [Configure granular resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-quotas).

### Shielded GKE Nodes configuration

_Requires GKE version 1.36.3-gke.1244000 or later_

To configure [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) features, such as Secure Boot and Integrity Monitoring, for auto-created node pools managed by a ComputeClass, specify `shieldedInstanceConfig` field under `nodePoolAutoCreation` block ([`spec.nodePoolAutoCreation.shieldedInstanceConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#shieldedInstanceConfig)).

The default values for `shieldedInstanceConfig` depend on your cluster mode and ComputeClass configuration:

  * **In Standard mode clusters** : when `shieldedInstanceConfig` is initialized during `nodePoolAutoCreation` reconciliation, `enableIntegrityMonitoring` field defaults to `true` and `enableSecureBoot` field defaults to `false` unless you explicitly configure them.
  * **In Autopilot clusters** (or when `spec.autopilot.enabled` is `true` in a ComputeClass): both `enableSecureBoot`and `enableIntegrityMonitoring` fields default to `true` and can't be disabled.



The following example demonstrates how to configure `shieldedInstanceConfig` field inside `nodePoolAutoCreation` block to enable Shielded GKE Nodes features across auto-created node pools:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: shielded-ccc
    spec:
      nodePoolAutoCreation:
        enabled: true
        shieldedInstanceConfig:
          enableSecureBoot: true
          enableIntegrityMonitoring: true
    

## Request ComputeClasses in workloads

To use a custom ComputeClass, your Pod must explicitly request that ComputeClass by using a `nodeSelector` in the Pod specification. You can optionally set a ComputeClass as the default for a specific Kubernetes namespace. Pods in that namespace use that ComputeClass unless the Pods request a different ComputeClass.

For example, the following manifest requests the `cost-optimized` ComputeClass:
    
    
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
    

### Node selectors for system node labels

GKE adds system labels to nodes to identify nodes by criteria like the machine type, attached hardware accelerators, or the boot disk type. These system labels have one of the following prefixes in the label key:

  * `k8s.io`
  * `cloud.google.com`
  * `gke.io`
  * `node.kubernetes.io/instance-type`



In GKE version 1.32.3-gke.1499000 and later, you can deploy workloads that use a node selector to select system labels and a ComputeClass at the same time. If you select system labels in Pods that select ComputeClasses, verify that those Pods schedule as expected. A conflict between the configuration of a ComputeClass and the node selectors in a Pod might result in issues like the following:

  * GKE can't create nodes that use the highest-priority configuration for the ComputeClass.
  * The Pod remains in the `Pending` status.



GKE also rejects any Pods that select system labels that have a corresponding field in the `ComputeClass` specification. When you use ComputeClasses, update your workloads to remove the following labels from node selectors and configure the corresponding field in the ComputeClasses that you create:

Node label | `ComputeClass` field  
---|---  
`cloud.google.com/machine-family` | [`priorities.machineFamily`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities)  
`cloud.google.com/machine-type` | [`priorities.machineType`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities)  
`cloud.google.com/gke-spot` | [`priorities.spot`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities)  
`cloud.google.com/gke-accelerator` | [`priorities.gpu.type`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#gpu)  
`cloud.google.com/gke-gpu-driver-version` | [`priorities.gpu.driverVersion`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#gpu)  
`cloud.google.com/reservation-name` | [`priorities.reservations.specific.name`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#specific)  
`cloud.google.com/reservation-project` | [`priorities.reservations.specific.project`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#specific)  
`cloud.google.com/reservation-affinity` | [`priorities.reservations.affinity`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#reservations)  
`cloud.google.com/gke-ephemeral-storage-local-ssd` | [`priorities.storage.localSSDCount`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage)  
`cloud.google.com/gke-boot-disk` | [`priorities.storage.bootDiskType`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage)  
`cloud.google.com/gke-boot-disk-size` | [`priorities.storage.bootDiskSize`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage)  
`cloud.google.com/gke-node-pool-group-name` | [`nodePoolGroup.name`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolgroup)  
`cloud.google.com/gke-workload-type` | [`nodePoolConfig.workloadType`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig)  
`node.kubernetes.io/instance-type` | [`priorities.machineType`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities)  
  
## Limitations

  * ComputeClass name can't begin with `gke` or `autopilot` (reserved for system ComputeClasses).
  * Certain clusters have high rates of Pod creation and deletion, which increases the evaluation time for the cluster autoscaler. During a scaling operation, the cluster autoscaler might not have time to evaluate subsequent priority rules in a ComputeClass before the backoff period for preceding priority rules expires. As a result, Pods might remain in a Pending state. To mitigate this issue, reduce the rate of Pod creation and deletion, for example by disabling active migration for the ComputeClass.



## What's next

  * Learn about [best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses).
  * Learn how to [control autoscaled node attributes with custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes).
  * Learn more about [Balanced and Scale-Out ComputeClasses in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).
  * Learn how to [configure node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * Learn more about [about GKE cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * Learn how to [choose compute classes for Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes).
  * [Troubleshoot custom ComputeClass issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
