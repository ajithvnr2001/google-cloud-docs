---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options/
title: GKE consumption options \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:23:56.923240+00:00
---

# GKE consumption options  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  GKE consumption options Stay organized with collections  Save and categorize content based on your preferences. 

When you deploy AI and machine learning (ML) workloads with Google Kubernetes Engine (GKE) and Cluster Toolkit, you can select from multiple compute consumption options to balance capacity availability, cost, and provisioning speed.

This document explains how to configure compute consumption options and placement policies for GPU, H4D, and Cloud TPU node pools in Cluster Toolkit. [Cluster deployment files](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/cluster-deployment-files) let you deploy GKE clusters that feature one of the following consumption options:

  * Standard or future reservations
  * Dynamic Workload Scheduler flex-start provisioning mode
  * Dynamic Workload Scheduler flex-start with queued provisioning
  * Spot VMs
  * On-demand capacity



For information about supported consumption options by machine type, see the following documentation:

  * **GPUs** : [Consumption option availability by machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#consumption_option_availability_by_machine_type)
  * **Cloud TPU** : [Consumption option availability by Cloud TPU versions](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#consumption_option_availability_by_tpu_versions)
  * **H4D** : [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)



For more information about capacity planning across Google Cloud, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

## Understand the differences between Cloud TPU and GPU deployments

Cloud TPU deployments in Cluster Toolkit differ from GPU deployments in two key ways:

  * **Automatic node count calculation** : Cluster Toolkit automatically calculates the `static_node_count` value from your `machine_type`, `num_slices`, and `tpu_topology` settings by using the formula `(total_chips_in_topology / chips_per_machine)`. You don't need to manually specify the `static_node_count` field in your consumption option blocks.
  * **Compact placement enabled by default** : all Cloud TPU blueprints enable compact placement by default, so you don't need to manually add placement settings to your deployment file. For Cloud TPU 7x, the blueprint configures a workload policy. For Cloud TPU v5p and Cloud TPU v6e, the blueprint configures the `placement_policy` field with `type: COMPACT` and your `tpu_topology` setting directly on the node pool.



## How to configure consumption options

In Cluster Toolkit, GKE deployment files preconfigure consumption options as YAML blocks. The reservation block is uncommented by default, and the other consumption options are commented out. To change your consumption option, comment out the default reservation block and uncomment your target option.

Alternatively, you can enable [node auto-provisioning (NAP)](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-cluster-nap) in your cluster blueprint to provision node pools dynamically and target on-demand capacity, Spot VMs, or reservations at Job submission time by using the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit).

The rest of this document explains the different consumption options and how to configure them.

## Standard and future reservations

Standard and future reservations provide high assurance of obtaining capacity for continuous or preplanned AI and ML workloads, such as large-scale training and inference. Cluster Toolkit supports consuming both [standard reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#standard-reservations) and [future reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#future-reservations) (including [calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview)). In GKE, node pools consume these reservations by configuring a specific reservation target (`consume_reservation_type: SPECIFIC_RESERVATION`) with the reservation name. For more information about how reservations work and how GKE consumes them, see [About reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) and [Consume reserved resources in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

To configure a reservation, select one of the following options:

### GPU and H4D

  * A3 Mega and A3 High machine types support both standard reservations and future reservations.
  * A3 Ultra, A4, and A4X Max machine types support future reservations, including [calendar mode where supported](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview#limitations-gpu). After Google Cloud provisions your future reservation capacity at the start time, you consume it in Cluster Toolkit by using the same specific reservation configuration.



In the deployment files for GPU and H4D machine types, the reservation block is uncommented by default:
    
    
    ## --- Option 1: Specific Reservation ---
    static_node_count: STATIC_NODE_COUNT
    reservation_affinity:
      consume_reservation_type: SPECIFIC_RESERVATION
      specific_reservations:
      - name: "RESERVATION_NAME"
    

To configure a reservation for a GPU or H4D node pool, replace the following values in your deployment file:

  * `STATIC_NODE_COUNT`: the number of nodes to provision from your reservation, such as `2`. The `static_node_count` field is required for standard and future reservations in GPU and H4D deployments.
  * `RESERVATION_NAME`: the name of your reservation. To target an individual reservation block within a reservation, specify the full resource path: `RESERVATION_NAME/reservationBlocks/BLOCK_NAME`.



### Compact placement with reservations

If you created the reservation with an existing compact placement policy, then pass the policy name in the `placement_policy` setting:
    
    
    placement_policy:
      type: COMPACT
      name: "EXISTING_PLACEMENT_POLICY_NAME"
    

Replace `EXISTING_PLACEMENT_POLICY_NAME` with the name of your compact placement policy. For more information, see [Reduce latency by using compact placement policies](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies).

### Dynamic Workload Scheduler calendar reservations

Dynamic Workload Scheduler calendar mode lets you reserve capacity for fixed-duration blocks. To use a calendar reservation in Cluster Toolkit, specify the reservation name in the `reservation_affinity` block.

For more information about Dynamic Workload Scheduler calendar reservations, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

### Cloud TPU

Cloud TPU machine types support [future reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#future-reservations), including [calendar mode where supported](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview#limitations-tpu). Standard reservations aren't supported for Cloud TPU machine types. After Google Cloud provisions your future reservation capacity at the start time, you consume it in Cluster Toolkit by configuring a specific reservation target.

In Cloud TPU deployment files, the reservation block is uncommented by default:
    
    
    ## --- Option 1: Specific Reservation ---
    reservation_affinity:
      consume_reservation_type: SPECIFIC_RESERVATION
      specific_reservations:
      - name: "RESERVATION_NAME"
    

To configure a reservation for a Cloud TPU node pool, set the `consume_reservation_type` field to `SPECIFIC_RESERVATION` in the `reservation_affinity` block, and replace `RESERVATION_NAME` with the name of your reservation in the `specific_reservations` field.

## Dynamic Workload Scheduler flex-start

Use Dynamic Workload Scheduler flex-start to optimize availability if your AI and ML workloads don't require immediate provisioning. When you use flex-start, Dynamic Workload Scheduler queues your provisioning request and deploys all required nodes concurrently after full capacity is available.

Allocations that use flex-start run for a maximum duration of 7 days (168 hours). This duration makes flex-start suitable for batch training, parameter tuning, and evaluation runs. For more information about how flex-start provisions accelerators and manages disruptions, see [About GPU, TPU, and H4D consumption with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).

To configure flex-start, select one of the following options:

### GPU and H4D

### Configure flex-start

To configure flex-start for GPU or H4D deployments, comment out the default reservation block and uncomment the flex-start block in your deployment file:
    
    
    ## --- Option 2: DWS Flex Start ---
    enable_flex_start: true
    static_node_count: $(null)
    

This block includes the following preconfigured settings:

  * `enable_flex_start: true`: enables flex-start scheduling.
  * `static_node_count: $(null)`: allows workload requests to size the node pool dynamically.



###  Compact placement within Dynamic Workload Scheduler flex-start 

On A4, A3 Ultra, and H4D machines, you can enforce physical compaction by defining a Compute Engine resource policy of type `HIGH_THROUGHPUT` by using the [`resource-policy` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/resource-policy) and attaching it to the node pool.

The following example shows how to configure the `workload_policy` module and reference it in your node pool module:
    
    
    deployment_groups:
      # Several lines of code are omitted here.
      - id: workload_policy
        source: modules/compute/resource-policy
        settings:
          name: $(vars.deployment_name)-wl-policy
          project_id: $(vars.project_id)
          region: $(vars.region)
          workload_policy:
            type: HIGH_THROUGHPUT
            max_topology_distance: CLUSTER
    
      - id: a3-ultragpu-pool
        source: modules/compute/gke-node-pool
        use: [a3-ultragpu-cluster, node_pool_service_account, workload_policy]
        settings:
          machine_type: a3-ultragpu-8g
          # Several lines of code are omitted here.
          placement_policy: $(workload_policy.placement_policy)
    

In this example, the `workload_policy` module defines a `HIGH_THROUGHPUT` policy and is added to the node pool `use` list. The node pool maps the `placement_policy` field to the `$(workload_policy.placement_policy)` value, which binds the `HIGH_THROUGHPUT` constraint and `max_topology_distance` boundary to the node pool's underlying Managed Instance Group (MIG).

For sample workloads and benchmarks, see [`sample-job-flex.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/dws-sample-workloads/sample-job-flex.yaml).

### Limitations

Flex-start in GPU and H4D deployments has the following limitations:

  * Flex-start doesn't work with static nodes. The `static_node_count` field can't be set to a number and must remain set to `$(null)`.
  * Flex-start doesn't use standard Compute Engine compact placement policies directly. Only A4, A3 Ultra, and H4D machine types support compact placement with flex-start by defining a custom `HIGH_THROUGHPUT` workload policy. G4, A3 Mega, and A3 High machine types don't support compact placement with flex-start.
  * Node auto-repair isn't supported. When you set the `enable_flex_start` field to `true`, the blueprint automatically disables node auto-repair.



### Cloud TPU

To configure flex-start for Cloud TPU deployments, comment out the default reservation block and uncomment the flex-start block in your deployment file:
    
    
    ## --- Option 2: DWS Flex Start ---
    enable_flex_start: true
    autoscaling_min_node_count: 0
    autoscaling_max_node_count: 1
    

This block includes the following settings:

  * `enable_flex_start: true`: enables flex-start scheduling. When set to `true`, the blueprint automatically disables node auto-repair (`auto_repair: false`).
  * `autoscaling_min_node_count`: preconfigured to `0` so that the node pool scales down when idle.
  * `autoscaling_max_node_count`: set this field to the number of chips in your topology divided by the number of chips for the machine type (for example, `4` for the `tpu7x-standard-4t` machine type). This field is required for Cloud TPU deployments that use flex-start.



### Configure custom Job manifests

If you want to create a custom Job manifest, then make sure that it includes the following required settings:

  * **Node selectors and tolerations** : the Job must target the Cloud TPU 7x nodes and tolerate the standard Cloud TPU taint:
        
        nodeSelector:
          cloud.google.com/gke-tpu-accelerator: "tpu7x"
          cloud.google.com/gke-tpu-topology: "2x2x2"
        tolerations:
        - key: google.com/tpu
          operator: Equal
          value: "present"
          effect: NoSchedule
        

  * **Resource requests** : each Pod in the Job must request the total number of Cloud TPU chips available on the node, such as `4` for the `tpu7x-standard-4t` machine type:
        
        resources:
          limits:
            google.com/tpu: 4
          requests:
            google.com/tpu: 4
        

  * **Parallelism** : the values of the `parallelism` and `completions` fields in your Kubernetes Job object, or the `replicas` field in a ReplicatedJob object within a JobSet, must match the number of nodes in your Cloud TPU slice, such as `2` for a `2x2x2` topology.




## Dynamic Workload Scheduler flex-start with queued provisioning

In multi-tenant or multi-job environments, you can combine flex-start with GKE queued provisioning and [Kueue](https://kueue.sigs.k8s.io/) so that workload requests wait in an orchestration queue until capacity is available. For more information, see [Flex-start configurations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws#methods).

To configure flex-start with queued provisioning, select one of the following options:

### GPU and H4D

To configure queued provisioning for GPU deployments, comment out the default reservation block and uncomment the flex-start with queued provisioning block in your deployment file:
    
    
    ## --- Option 3: DWS Flex Start + Queued Provisioning ---
    kueue_configuration_path: $(ghpc_stage("../dws-sample-workloads/dws-queues.yaml.tftpl"))
    enable_flex_start: true
    enable_queued_provisioning: true
    static_node_count: $(null)
    

This block includes the following preconfigured settings:

  * `enable_flex_start: true` and `enable_queued_provisioning: true`: enables flex-start with GKE queued provisioning.
  * `static_node_count: $(null)`: allows GKE to provision nodes dynamically when you submit a Job (requiring the `autoscaling_total_min_nodes: 0` setting).
  * `kueue_configuration_path`: stages the Kueue queue configuration template (`dws-queues.yaml.tftpl`). When you deploy the cluster, Cluster Toolkit automatically installs Kueue and applies the `kueue_configuration_path` file to create a `LocalQueue` resource named `dws-local-queue`. You don't need to manually overwrite your cluster's `kueue-configuration.yaml.tftpl` file.



### Limitations

Queued provisioning in GPU deployments has the following limitations:

  * Queued provisioning doesn't work with static nodes. The `static_node_count` field can't be set to a number and must remain set to `$(null)`.
  * GPU node pools don't support compact placement policies or custom workload policies with queued provisioning.



### Cloud TPU

To combine flex-start with GKE queued provisioning and Kueue for Cloud TPU deployments, comment out the default reservation block and uncomment the flex-start with queued provisioning block in your deployment file:
    
    
    ## --- Option 3: DWS Flex Start + Queued Provisioning ---
    kueue_configuration_path: $(ghpc_stage("../dws-sample-workloads/tpu-dws-queues.yaml.tftpl"))
    enable_flex_start: true
    enable_queued_provisioning: true
    autoscaling_min_node_count: 0
    autoscaling_max_node_count: 1
    

This block includes the following settings:

  * `kueue_configuration_path`: stages the Cloud TPU Kueue queue configuration template (`tpu-dws-queues.yaml.tftpl`). When you deploy the cluster, Cluster Toolkit automatically calculates your Kueue `google.com/tpu` nominal quota from your slice topology and creates a `LocalQueue` resource named `dws-local-queue`.
  * `enable_flex_start: true` and `enable_queued_provisioning: true`: enables flex-start with GKE queued provisioning.
  * `autoscaling_min_node_count` and `autoscaling_max_node_count`: the `autoscaling_min_node_count` field is preconfigured to `0`. Set the `autoscaling_max_node_count` field to the number of chips in your topology divided by the number of chips for the machine type. These fields are required for Cloud TPU queued provisioning.



### Configure custom Job manifests

To route Kubernetes Jobs or JobSets through queued provisioning, include the following required settings in your workload manifest:

  * **Metadata** : submit the Job or JobSet to the Kueue queue and configure the Dynamic Workload Scheduler run duration. The `kueue.x-k8s.io/queue-name` label must match the `LocalQueue` resource that Cluster Toolkit creates, which defaults to the value `dws-local-queue`:
        
        metadata:
          labels:
            kueue.x-k8s.io/queue-name: dws-local-queue
          annotations:
            # Specify duration in seconds
            provreq.kueue.x-k8s.io/maxRunDurationSeconds: "3600"
        

  * **Node selectors and affinity** : target the provisioned queued provisioning node pool. For Cloud TPU deployments, also specify your slice topology and the `cloud.google.com/gke-queued: "true"` selector:
        
        nodeSelector:
          cloud.google.com/gke-tpu-topology: "2x2x2"
          cloud.google.com/gke-queued: "true"
        affinity:
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: cloud.google.com/gke-nodepool
                  operator: In
                  values: ["NODE_POOL_NAME"]
        

  * **Tolerations** : schedule Pods on tainted accelerator and queued provisioning nodes. Specify `nvidia.com/gpu` for GPU node pools or `google.com/tpu` for Cloud TPU node pools:
        
        tolerations:
        - key: "google.com/tpu"
          operator: "Equal"
          value: "present"
          effect: "NoSchedule"
        - key: "cloud.google.com/gke-queued"
          operator: "Equal"
          value: "true"
          effect: "NoSchedule"
        




For manifest configuration and monitoring guidance, see [Run a large-scale workload with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest), or view the [sample queued provisioning manifests and queue templates](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/dws-sample-workloads/sample-job-flex-queue.yaml) on GitHub.

## Spot VMs

Spot VMs provide access to unused Compute Engine capacity at a potential discount for fault-tolerant workloads with automated checkpointing. For more information, see [About Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) and [Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).

To configure Spot VMs, select one of the following options:

### GPU and H4D

To configure Spot VMs for GPU deployments, comment out the default reservation block and uncomment the Spot VMs block in your deployment file:
    
    
    ## --- Option 4: Spot ---
    spot: true
    static_node_count: STATIC_NODE_COUNT
    placement_policy:
      type: COMPACT
    

This block includes the following settings:

  * `spot: true`: enables Spot VMs for the node pool.
  * `static_node_count`: replace `STATIC_NODE_COUNT` with the number of Spot VM nodes to provision in your node pool, such as `2`. This field is required for GPU deployments that use Spot VMs.



### Compact placement with Spot VMs

Compact placement is required for multi-node GPU workloads that use [Kueue Topology-Aware Scheduling (TAS)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas) to expose `cloud.google.com/gce-topology-block` labels. By default, the GPU Spot VMs block configures a compact placement policy so that Compute Engine attaches these physical topology labels. Without a compact placement policy, Compute Engine omits topology metadata and Kueue TAS workloads remain suspended.

However, if compact capacity is constrained in a single physical block and your workloads don't use Kueue TAS, then you can remove or comment out the `placement_policy` field from your deployment file as a capacity fallback to run standard Kubernetes Jobs across scattered capacity. For more information, see [Reduce latency by using compact placement policies](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies).

### Cloud TPU

To configure Spot VMs for Cloud TPU deployments, comment out the default reservation block and uncomment the Spot VMs block in your deployment file:
    
    
    ## --- Option 4: Spot ---
    spot: true
    

In this block, the `spot: true` setting enables Spot VMs for the Cloud TPU node pool. For Cloud TPU 7x, Spot VMs require allowlist access. For more information, see [Consumption option availability by Cloud TPU versions](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#consumption_option_availability_by_tpu_versions).

## On-demand capacity

On-demand capacity provisions GKE node pools immediately from available Compute Engine stock without the need for an upfront reservation. For more information, see [Use on-demand capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#on-demand).

To configure on-demand capacity, select one of the following options:

### GPU and H4D

To configure on-demand capacity for GPU deployments, comment out the default reservation block and uncomment the on-demand capacity block in your deployment file:
    
    
    ## --- Option 5: On-Demand ---
    static_node_count: STATIC_NODE_COUNT
    placement_policy:
      type: COMPACT
    

This block includes the following settings:

  * `static_node_count`: replace `STATIC_NODE_COUNT` with the number of on-demand nodes to provision in your node pool, such as `2`. This field is required for on-demand capacity in GPU deployments.
  * `spot`: defaults to `false`, which provisions standard on-demand instances.



### Compact placement and on-demand capacity

By default, Cluster Toolkit GPU deployments that support on-demand capacity configure a compact placement policy to minimize network latency for multi-node training workloads and expose topology labels for Kueue TAS. If compact capacity is constrained in a single physical block and your workloads don't require TAS, then you can remove or comment out the `placement_policy` field from your deployment file as a capacity fallback to run standard Kubernetes Jobs across scattered capacity. For more information, see [Reduce latency by using compact placement policies](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies).

### Limitations

A3 Ultra, A4, and A4X Max machine types don't support on-demand provisioning.

### Cloud TPU

Configuring on-demand capacity for Cloud TPU deployments doesn't require setting any variables. To provision Cloud TPU slices by using on-demand capacity, comment out the default reservation block and leave the other consumption option blocks commented out in your deployment file.

## What's next

  * [Deploy a cluster with node auto-provisioning](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-cluster-nap).
  * Review advanced orchestration features in the [GKE deployments overview](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview).
  * [Deploy an A3 Mega GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-a3-mega-gke-cluster).
  * [Create an A4X Max GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-max-cluster).
  * [Deploy a GKE Cloud TPU v6e cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e).
  * Learn how to configure node pools in the [`gke-node-pool` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool).
  * Learn how to define custom placement constraints in the [`resource-policy` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/resource-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
