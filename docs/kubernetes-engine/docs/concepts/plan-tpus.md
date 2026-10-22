---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus/
title: Plan TPUs in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:31.964616+00:00
---

# Plan TPUs in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Plan TPUs in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to plan your usage of Tensor Processing Units (TPUs) in Google Kubernetes Engine (GKE) to reduce the risk of TPU misconfiguration, non-availability errors, or out-of-quota interruptions.

Before you use TPUs in GKE, ensure that you are familiar with [TPUs definitions and terminology in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

## Plan your TPU configuration

To work with TPUs in GKE clusters, you must plan their configuration. We recommend that you follow these steps:

  1. **Choose a GKE mode of operation**: Run your workloads on TPUs in a GKE Autopilot or Standard cluster.

**Best practice** : 

Use an Autopilot cluster for a fully managed Kubernetes experience.

  2. **Choose the TPU version**: Different TPU types have different capabilities, like price-performance ratios, training throughput, and serving latency. The TPU types affect the available CPU and memory capacities.

  3. **Validate TPU availability**: TPUs are available in specific Google Cloud regions. To use a TPU type in your GKE workload, your cluster must be in a supported region for that type.

  4. **Choose the TPU Topology**: The physical arrangement of the TPUs within a TPU slice. Select a topology that matches your model's parallelism requirements.




Use the reference tables on this page to identify if your node pools are single-host or multi-host TPU slice nodes.

## Choose a GKE mode of operation

You can use TPUs in the available GKE modes of operation for clusters:

  * **Standard mode** : You manage the underlying infrastructure, including configuring the individual nodes.
  * **Autopilot mode (recommended)** : GKE manages the underlying infrastructure such as node configuration, autoscaling, auto-upgrades, baseline security configurations, and baseline networking configuration. In Autopilot, you choose a TPU type and topology, then specify them in your Kubernetes manifest. GKE manages provisioning nodes with TPUs and scheduling your workloads.



To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

## Choose a TPU consumption option

When you plan your TPU configuration in GKE, select a consumption option that aligns with your workload needs. Your choice of consumption option impacts the available TPU versions and the quota you need to configure. GKE offers the following TPU consumption options to help you optimize resource allocation and cost while maintaining workload performance:

  * **Flex-start:** to provision Flex-start VMs for up to seven days, with GKE automatically allocating the hardware on a best-effort basis based on availability. For more information, see [About GPU, TPU, and H4D provisioning with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).
  * **Spot VMs:** to provision Spot VMs, you can get significant discounts, but Spot VMs can be preempted at any time, with a 30-second warning. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
  * **Future reservation for up to 90 days (in calendar mode):** to provision TPU resources for up to 90 days, for a specified time period. For more information, see [Request TPUs with future reservation in calendar mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-calendar-mode).
  * **TPU reservations:** to [request a future reservation for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation).
  * **On-demand:** to consume TPUs without arranging capacity in advance. Before requesting resources, you must have enough [on-demand quota](https://docs.cloud.google.com/tpu/docs/quota#on-demand-quotas) for the specific type and quantity of TPU VMs. On-demand is the most flexible consumption option; however, there is no guarantee that enough on-demand resources will be available to satisfy your request.



On-demand is the default consumption model for TPUs in GKE if you don't specify another option. To choose the consumption option that meets your workload requirements, see [About accelerator consumption options for AI/ML workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option).

## Choose the TPU version

The VMs in a TPU slice have the following technical characteristics.

Ironwood (TPU7x)TPU TrilliumTPU v5pTPU v5eTPU v4TPU v3Clear all

### Standard

TPU version | Machine type | `cloud.google.com/gke-tpu-accelerator` | Number of vCPUs | Number of chips per VM | Number of [NUMA](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#memory_system) nodes | Likelihood of being preempted  
---|---|---|---|---|---|---  
Ironwood (TPU7x) | `tpu7x-standard-4t` | `tpu7x` | 224 | 4 | 2 | Not applicable  
[TPU Trillium (v6e)](https://docs.cloud.google.com/tpu/docs/v6e-intro) | `ct6e-standard-1t` | `tpu-v6e-slice` | 44 | 1 | 1 | Higher  
[TPU Trillium (v6e)](https://docs.cloud.google.com/tpu/docs/v6e-intro) | `ct6e-standard-4t` | `tpu-v6e-slice` | 180 | 4 | 1 | Medium  
[TPU Trillium (v6e)](https://docs.cloud.google.com/tpu/docs/v6e-intro) | `ct6e-standard-8t` | `tpu-v6e-slice` | 180 | 8 | 2 | Lower  
[TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p-training#v5p_tpu_configurations)  
| `ct5p-hightpu-4t` | `tpu-v5p-slice` | 208 | 4 | 2 | Not applicable  
[TPU v5e](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_v5e)  
| `ct5lp-hightpu-1t` | `tpu-v5-lite-podslice` | 24 | 1 | 1 | Higher  
[TPU v5e](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_v5e)  
| `ct5lp-hightpu-4t` | `tpu-v5-lite-podslice` | 112 | 4 | 1 | Medium  
[TPU v5e](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_v5e)  
| `ct5lp-hightpu-8t` | `tpu-v5-lite-podslice` | 224 | 8 | 1 | Low  
[TPU v4](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_v4)  
| `ct4p-hightpu-4t` | `tpu-v4-podslice` | 240 | 4 | 2 | Not applicable  
[TPU v3 (single-host only)](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_v3)  
| `ct3-hightpu-4t` | `tpu-v3-device` | 96 | 4 | 2 | Not applicable  
[TPU v3](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_v3)  
| `ct3p-hightpu-4t` | `tpu-v3-slice` | 48 | 4 | 1 | Not applicable  
  
Multi-host `ct5lp-` machine types are more suitable for serving large models or training. Multi-host `ct5lp-` machines are interconnected with high-speed links.

### Autopilot

TPU version | `cloud.google.com/gke-tpu-accelerator` | Number of vCPUs | Number of [NUMA](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#memory_system) nodes | Maximum TPU chips in a TPU slice node  
---|---|---|---|---  
Ironwood (TPU7x) | `tpu7x` | 224 | 2 | 2048  
[TPU Trillium (v6e)](https://docs.cloud.google.com/tpu/docs/v6e-intro) | `tpu-v6e-slice` | 44 to 180 | 1 to 2 | 256  
[TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p-training#v5p_tpu_configurations)  
| `tpu-v5p-slice` | 208 | 2 | 6,144  
[TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e)  
| `tpu-v5-lite-podslice` | 24 to 224 | 1 | 256  
[TPU v4](https://docs.cloud.google.com/tpu/docs/v4)  
| `tpu-v4-podslice` | 240 | 2 | 4,096  
[TPU v3 (single-host only)](https://docs.cloud.google.com/tpu/docs/v3)  
| `tpu-v3-device` | 96 | 2 | 8  
[TPU v3](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_v3)  
| `tpu-v3-slice` | 48 | 1 | 256  
  
Review the TPU specifications and pricing in the [Cloud TPU pricing documentation](https://cloud.google.com/tpu/pricing) to decide which TPU configuration to use.

### Limitations

Consider these limitations when choosing the TPU to use:

  * Ironwood (TPU7x) has the following limitations:

    * Standard clusters in version 1.34.0-gke.2201000 and later.
    * Autopilot clusters in version 1.34.1-gke.3084001 and later.
    * Only [Google Cloud Hyperdisk Balanced and Hyperdisk ML](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) are supported.
  * TPU Trillium is available in the following versions:

    * Standard clusters in version 1.31.1-gke.1846000 and later.
    * Autopilot clusters in version 1.31.2-gke.1115000 and later.
  * TPU Trillium doesn't support configuring [SMT](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt) set to `2` on `ct6e-standard-8t`.

  * TPU v5p autoscaling is supported on GKE clusters with control planes running at least version 1.29.2-gke.1035000 or 1.28.7-gke.1020000.

  * For capacity reservations, use a _specific_ reservation.

  * You can run a maximum of 256 Pods in a single TPU VM.

  * [GKE cost allocation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations) and usage metering don't include any data about the usage or costs of TPUs.

  * The cluster autoscaler cancels TPU node pool scale-up operations that remain in waiting status for more than 10 hours. The cluster autoscaler retries such scale-up operations when resources are available. This behavior might reduce TPU availability if you don't use reservations.

  * Ubuntu nodes are not supported.

  * [TPU Node architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu-node-arch) is deprecated. TPU v3 is the only TPU version that still supports the TPU Node architecture in GKE.




## Validate TPU availability in GKE

TPUs are available in specific Google Cloud regions. To use a TPU type in your GKE cluster, your cluster must be in a supported region for that type.

Ironwood (TPU7x)TPU TrilliumTPU v5pTPU v5eTPU v4TPU v3asia-northeast1-beurope-west4-aeurope-west4-bus-central1-aus-central1-bus-central2-bus-east1-dus-east5-aus-east5-bus-east5-cus-south1-aus-west1-cus-west4-asouthamerica-west1-aClear all

### Standard

TPU version |  Machine type beginning with  | Minimum [GKE version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) | Availability | Zone  
---|---|---|---|---  
TPU Ironwood (TPU7x) |  `tpu7x-standard-4t` |  1.34.0-gke.2201000  | GA | 

  * `us-central1-ai1a`
  * `us-central1-c`

  
TPU Trillium (v6e) |  `ct6e-` |  1.31.2-gke.1115000  | GA | 

  * `asia-northeast1-b`
  * `europe-west4-a`
  * `southamerica-west1-a`
  * `us-central1-b`
  * `us-east1-d`
  * `us-east5-a`
  * `us-east5-b`
  * `us-south1-ai1b`

  
TPU v5e |  `ct5lp-` |  1.27.2-gke.2100  | GA | 

  * `europe-west4-b`
  * `us-central1-a`
  * `us-south1-a`
  * `us-west1-c`
  * `us-west4-a`

  
TPU v5p |  `ct5p-` |  1.28.3-gke.1024000  | GA | 

  * `europe-west4-b`
  * `us-central1-a`
  * `us-east5-a`

  
TPU v4 |  `ct4p-` |  1.26.1-gke.1500  | GA | 

  * `us-central2-b`

  
TPU v3 |  `ct3p-` |  1.31.1-gke.1146000  | GA | 

  * `europe-west4-a`
  * `us-central1-a`
  * `us-central1-b`

  
TPU v3 |  `ct3-` |  1.31.0-gke.1500  | GA | 

  * `europe-west4-a`
  * `us-central1-a`
  * `us-central1-b`

  
  
### Autopilot

TPU version |  `cloud.google.com/gke-tpu-accelerator` | Minimum [GKE version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) | Availability | Zone  
---|---|---|---|---  
TPU Ironwood (TPU7x) |  `tpu7x` |  1.34.1-gke.3084001  | GA | 

  * `us-central1-ai1a`
  * `us-central1-c`

  
TPU Trillium (v6e) |  `tpu-v6e-slice` |  1.31.2-gke.1384000  | GA | 

  * `asia-northeast1-b`
  * `europe-west4-a`
  * `southamerica-west1-a`
  * `us-central1-b`
  * `us-east1-d`
  * `us-east5-a`
  * `us-east5-b`
  * `us-south1-ai1b`

  
TPU v5e |  `tpu-v5-lite-podslice` |  1.27.2-gke.2100  | GA | 

  * `europe-west4-b`
  * `us-central1-a`
  * `us-south1-a`
  * `us-west1-c`
  * `us-west4-a`

  
TPU v5p |  `tpu-v5p-slice` |  1.28.3-gke.1024000  | GA | 

  * `europe-west4-b`
  * `us-central1-a`
  * `us-east5-a`

  
TPU v4 |  `tpu-v4-podslice` |  1.26.1-gke.1500  | GA | 

  * `us-central2-b`

  
TPU v3 |  `tpu-v3-slice` |  1.31.1-gke.1146000  | GA | 

  * `europe-west4-a`
  * `us-central1-a`
  * `us-central1-b`

  
TPU v3 |  `tpu-v3-device` |  1.31.0-gke.1500  | GA | 

  * `europe-west4-a`
  * `us-central1-a`
  * `us-central1-b`

  
  
## Choose a topology

After you choose a TPU version, select a supported topology. A topology defines the physical arrangement of TPU chips within a TPU slice. Larger topologies provide more TPU chips, which enables more parallel processing to train large models faster or with larger data sets.

While GKE automatically manages VM provisioning, understanding the difference between single-host and multi-host node pools helps clarify how the number of chips in your topology relates to the underlying VMs:

  * **[Single-host](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#single-host):** a TPU slice where all chips reside on a single VM. This involves smaller chip counts, usually four chips or fewer.
  * **[Multi-host](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host):** a TPU slice where the chips are distributed across multiple VMs. This is common for most high-scale TPU workloads.



If you request a topology where the total number of chips exceeds the number of chips available on a single VM for that TPU version, GKE automatically provisions it as a multi-host environment. In this scenario, GKE brings up multiple nodes to distribute the chips.

For example, consider the `ct6e-standard-4t` machine type and a `4x4` topology:

  * The machine type `ct6e-standard-4t` has 4 chips per VM.
  * The topology `4x4` requires a total of 16 chips (4 * 4).
  * Since 16 (topology chip count) is greater than 4 (chips per VM), this configuration results in a multi-host TPU slice node pool. GKE will distribute the 16 chips across 4 VMs.



Use the following table to choose the TPU machine type and topology for your use case:

Ironwood (TPU7x)TPU TrilliumTPU v5pTPU v5eTPU v4TPU v3Single-hostMulti-hostClear all

### Standard

After you choose a TPU type and topology, specify these in your workload manifest. For instructions, see [Deploy TPU workloads on GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus).

TPU version | Machine type | Node pool type | Technical specifications  
---|---|---|---  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Single-host | 

  * Topology: 2x2x1
  * Number of TPU chips for the topology: 4
  * Number of hosts: 1
  * Number of VMs: 1
  * Cubes count: 1/16

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of hosts: 2
  * Number of VMs: 2
  * Cubes count: 1/8

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 2x2x4
  * Number of TPU chips for the topology: 16
  * Number of hosts: 4
  * Number of VMs: 4
  * Cubes count: 1/4

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of hosts: 8
  * Number of VMs: 8
  * Cubes count: 1/2

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 4x4x4
  * Number of TPU chips for the topology: 64
  * Number of hosts: 16
  * Number of VMs: 16
  * Cubes count: 1

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 4x4x8
  * Number of TPU chips for the topology: 128
  * Number of hosts: 32
  * Number of VMs: 32
  * Cubes count: 2

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 4x8x8
  * Number of TPU chips for the topology: 256
  * Number of hosts: 64
  * Number of VMs: 64
  * Cubes count: 4

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 8x8x8
  * Number of TPU chips for the topology: 512
  * Number of hosts: 128
  * Number of VMs: 128
  * Cubes count: 8

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 8x8x16
  * Number of TPU chips for the topology: 1024
  * Number of hosts: 256
  * Number of VMs: 256
  * Cubes count: 16

  
Ironwood (TPU7x) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: {A}x{B}x{C} (where A, B, and C are multiples of two)
  * Number of TPU chips for the topology: A*B*C
  * Number of hosts: (A*B*C)/4
  * Number of VMs: (A*B*C/4)
  * Cubes count: (A*B*C/64)

  
TPU Trillium (v6e) | `ct6e-standard-1t` | Single-host | 

  * Topology: 1x1
  * Number of TPU chips for the topology: 1
  * Number of VMs: 1

  
TPU Trillium (v6e) | `ct6e-standard-8t` | Single-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 1

  
TPU Trillium (v6e) | `ct6e-standard-4t` | Single-host | 

  * Topology: 2x2
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU Trillium (v6e) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU Trillium (v6e) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 4x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU Trillium (v6e) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 4x8
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU Trillium (v6e) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 8x8
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU Trillium (v6e) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 8x16
  * Number of TPU chips for the topology: 128
  * Number of VMs: 32

  
TPU Trillium (v6e) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 16x16
  * Number of TPU chips for the topology: 256
  * Number of VMs: 64

  
TPU v5p | `ct5p-hightpu-4t` | Single-host | 

  * Topology: 2x2x1
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: 2x2x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: {A}x{B}x{C} (where A, B, and C are multiples of two)
  * Number of TPU chips for the topology: A*B*C
  * Number of VMs: (A*B*C/4)1

  
TPU v5e | `ct5lp-hightpu-1t` | Single-host | 

  * Topology: 1x1
  * Number of TPU chips for the topology: 1
  * Number of VMs: 1

  
TPU v5e | `ct5lp-hightpu-4t` | Single-host | 

  * Topology: 2x2
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v5e | `ct5lp-hightpu-8t` | Single-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 1

  
TPU v5e | `ct5lp-hightpu-4t` | Multi-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v5e | `ct5lp-hightpu-4t` | Multi-host | 

  * Topology: 4x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v5e | `ct5lp-hightpu-4t` | Multi-host | 

  * Topology: 4x8
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v5e | `ct5lp-hightpu-4t` | Multi-host | 

  * Topology: 8x8
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU v5e | `ct5lp-hightpu-4t` | Multi-host | 

  * Topology: 8x16
  * Number of TPU chips for the topology: 128
  * Number of VMs: 32

  
TPU v4 | `ct4p-hightpu-4t` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v4 | `ct4p-hightpu-4t` | Multi-host | 

  * Topology: 2x2x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v4 | `ct4p-hightpu-4t` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v4 | `ct4p-hightpu-4t` | Multi-host | 

  * Topology: {A}x{B}x{C} (where A, B, and C are multiples of two)
  * Number of TPU chips for the topology: A*B*C
  * Number of VMs: (A*B*C/4)1

  
TPU v3 | `ct3-hightpu-4t` | Single-host | 

  * Topology: 2x2
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v3 | `ct3p-hightpu-4t` | Multi-host | 

  * Topology: 4x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v3 | `ct3p-hightpu-4t` | Multi-host | 

  * Topology: 4x8
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v3 | `ct3p-hightpu-4t` | Multi-host | 

  * Topology: 8x8
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU v3 | `ct3p-hightpu-4t` | Multi-host | 

  * Topology: 8x16
  * Number of TPU chips for the topology: 128
  * Number of VMs: 32

  
TPU v3 | `ct3p-hightpu-4t` | Multi-host | 

  * Topology: 16x16
  * Number of TPU chips for the topology: 256
  * Number of VMs: 64

  
TPU v3 | `ct3p-hightpu-4t` | Multi-host | 

  * Topology: 16x32
  * Number of TPU chips for the topology: 512
  * Number of VMs: 128

  
TPU v3 | `ct3p-hightpu-4t` | Multi-host | 

  * Topology: 32x32
  * Number of TPU chips for the topology: 1024
  * Number of VMs: 256

  
  
  1. Calculated by the topology product divided by four. ↩




### Autopilot

After you choose a TPU type and topology, specify these in your workload manifest. For instructions, see [Deploy TPU workloads on GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot).

TPU version | Machine type | Node pool type | Technical specifications  
---|---|---|---  
Ironwood (TPU7x) | `tpu7x` | Single-host | 

  * Topology: 2x2x1
  * Number of TPU chips for the topology: 4
  * Number of hosts: 1
  * Number of VMs: 1
  * Cubes count: 1/16

  
Ironwood (TPU7x) | `tpu7x` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of hosts: 2
  * Number of VMs: 2
  * Cubes count: 1/8

  
Ironwood (TPU7x) | `tpu7x` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of hosts: 8
  * Number of VMs: 8
  * Cubes count: 1/2

  
Ironwood (TPU7x) | `tpu7x` | Multi-host | 

  * Topology: 4x4x4
  * Number of TPU chips for the topology: 64
  * Number of hosts: 16
  * Number of VMs: 16
  * Cubes count: 1

  
Ironwood (TPU7x) | `tpu7x` | Multi-host | 

  * Topology: 8x8x8
  * Number of TPU chips for the topology: 512
  * Number of hosts: 128
  * Number of VMs: 128
  * Cubes count: 8

  
Ironwood (TPU7x) | `tpu7x` | Multi-host | 

  * Topology: 8x8x16
  * Number of TPU chips for the topology: 1024
  * Number of hosts: 256
  * Number of VMs: 256
  * Cubes count: 16

  
Ironwood (TPU7x) | `tpu7x` | Multi-host | 

  * Topology: 8x16x16
  * Number of TPU chips for the topology: 2048
  * Number of hosts: 512
  * Number of VMs: 512
  * Cubes count: 32

  
TPU Trillium (v6e) | `tpu-v6e-slice` | Single-host | 

  * Topology: 1x1
  * Number of TPU chips for the topology: 1
  * Number of VMs: 1

| TPU Trillium (v6e) | `tpu-v6e-slice` | Single-host | 

  * Topology: 2x2
  * Number of TPU chips for the topology: 4
  * Number of VMs: 4

  
TPU Trillium (v6e) | `tpu-v6e-slice` | Single-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 8

  
TPU Trillium (v6e) | `tpu-v6e-slice` | Multi-host | 

  * Topology: 4x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU Trillium (v6e) | `tpu-v6e-slice` | Multi-host | 

  * Topology: 4x8
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU Trillium (v6e) | `tpu-v6e-slice` | Multi-host | 

  * Topology: 8x8
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU Trillium (v6e) | `tpu-v6e-slice` | Multi-host | 

  * Topology: 8x16
  * Number of TPU chips for the topology: 128
  * Number of VMs: 32

  
TPU Trillium (v6e) | `tpu-v6e-slice` | Multi-host| 

  * Topology: 16x16
  * Number of TPU chips for the topology: 256
  * Number of VMs: 64

  
TPU v5p | `tpu-v5p-slice` | Single-host | 

  * Topology: 2x2x1
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v5p | `tpu-v5p-slice` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v5p | `tpu-v5p-slice` | Multi-host | 

  * Topology: 2x2x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v5p | `tpu-v5p-slice` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v5p | `tpu-v5p-slice` | Multi-host | 

  * Topology: 4x4x4
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU v5p | `tpu-v5p-slice` | Multi-host | 

  * Topology: {A}x{B}x{C}
  * Number of TPU chips for the topology: {A}*{B}*{C}
  * Number of VMs: (A*B*C/4)1

  
TPU v5e | `tpu-v5-lite-podslice` | Single-host | 

  * Topology: 1x1
  * Number of TPU chips for the topology: 1
  * Number of VMs: 1

  
TPU v5e | `tpu-v5-lite-podslice` | Single-host | 

  * Topology: 2x2
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v5e | `tpu-v5-lite-podslice` | Single-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 1

  
TPU v5e | `tpu-v5-lite-podslice` | Multi-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v5e | `tpu-v5-lite-podslice` | Multi-host | 

  * Topology: 4x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v5e | `tpu-v5-lite-podslice` | Multi-host | 

  * Topology: 4x8
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v5e | `tpu-v5-lite-podslice` | Multi-host | 

  * Topology: 8x8
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU v5e | `tpu-v5-lite-podslice` | Multi-host | 

  * Topology: 8x16
  * Number of TPU chips for the topology: 128
  * Number of VMs: 32

  
TPU v5e | `tpu-v5-lite-podslice` | Multi-host | 

  * Topology: 16x16
  * Number of TPU chips for the topology: 256
  * Number of VMs: 64

  
TPU v4 | `tpu-v4-podslice` | Single-host | 

  * Topology: 2x2x1
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v4 | `tpu-v4-podslice` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v4 | `tpu-v4-podslice` | Multi-host | 

  * Topology: 2x2x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v4 | `tpu-v4-podslice` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v4 | `tpu-v4-podslice` | Multi-host | 

  * Topology: 4x4x4
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU v4 | `tpu-v4-podslice` | Multi-host | 

  * Topology: {A}x{B}x{C}
  * Number of TPU chips for the topology: {A}*{B}*{C}
  * Number of VMs: (A*B*C/4)1

  
TPU v3 | `tpu-v3-slice` | Multi-host | 

  * Topology: 4x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 2

  
TPU v3 | `tpu-v3-slice` | Multi-host | 

  * Topology: 4x8
  * Number of TPU chips for the topology: 32
  * Number of VMs: 4

  
TPU v3 | `tpu-v3-slice` | Multi-host | 

  * Topology: 8x8
  * Number of TPU chips for the topology: 64
  * Number of VMs: 8

  
TPU v3 | `tpu-v3-slice` | Multi-host | 

  * Topology: 8x16
  * Number of TPU chips for the topology: 128
  * Number of VMs: 16

  
TPU v3 | `tpu-v3-slice` | Multi-host | 

  * Topology: 16x16
  * Number of TPU chips for the topology: 256
  * Number of VMs: 32

  
TPU v3 | `tpu-v3-device` | Single-host | 

  * Topology: 2x2
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
  
  1. Calculated by the topology product divided by four. ↩

Custom topologies for more than 64 chips are supported. The following conditions apply:

     * For more than 64 chips, `{A}`, `{B}`, and `{C}` must be multiples of 4
     * The largest topology is `16x16x24`
     * The values must be `{A}`≤`{B}`≤`{C}`, like `8x12x16`.
  2. Custom topologies aren't supported.




## Advanced configurations

The following sections describe scheduling best practices for advanced TPU configurations.

### AI zones

AI zones are specialized zones used for AI/ML training and inference workloads. These zones provide significant ML accelerator capacity. For more information, see the [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) documentation.

In this document and the GKE documentation, "standard zones" or "zones" refer to non-AI zones within a Google Cloud region.

**Important:** Access to AI zones is restricted unless you've enabled them for your Google Cloud project. To use them, [enable AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#enable_ai_zones) ([Preview](https://cloud.google.com/products#product-launch-stages)).

Before you use an AI zone in GKE, consider the following characteristics:

  * AI zones are physically separate from standard zones to provide additional storage space and power. This separation might result in higher latency, which is generally tolerable for AI/ML workloads.
  * AI zones have a suffix with the `ai` notation. For example, an AI zone in the `us-central1` region is named `us-central1-**ai** 1a`.
  * Currently, only TPU VMs are supported.
  * The cluster's control plane runs in one or more standard zones within the same region as the AI zone.
  * You can run VMs without attached TPUs in an AI zone only if you meet the following requirements:

    * You are already running other workloads that use TPU VMs in the same zone.
    * The non-TPU VMs are either Spot VMs, tied to a reservation, or part of a node pool with a specific accelerator-to-general-purpose VM ratio.
**Note:** Even if GKE lets you create the node pool, Compute Engine provisions the VMs only if these conditions are met. For more information, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).
  * AI zones share components, such as networking connections and software rollouts, with standard zones that have the same suffix within the same region. For high-availability workloads, we recommend that you use different zones. For example, avoid using both `us-central1-ai1a` and `us-central1-a` for high availability.




By default, GKE doesn't deploy your workloads in AI zones. To use an AI zone, you must configure one of the following options:

  * **(Recommended) ComputeClasses** : set your highest priority to request on-demand TPUs in an AI zone. ComputeClasses help you define a prioritized list of hardware configurations for your workloads. For an example, see [About ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#ai-zones).
  * **Node auto-provisioning** : use a `nodeSelector` or `nodeAffinity` in your Pod specification to instruct node auto-provisioning to create a node pool in the AI zone. If your workload doesn't explicitly target an AI zone, node auto-provisioning considers only standard zones or zones from [`--autoprovisioning-locations`](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-locations) when creating new node pools. This configuration helps ensure that workloads that don't run AI/ML models remain in standard zones unless you explicitly configure otherwise. For an example of a manifest that uses a `nodeSelector`, see [Set the default zones for auto-created nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#auto-provisioning_locations).
  * **GKE Standard** : if you directly manage your node pools, use an AI zone in the `--node-locations` flag when you create a node pool. For an example, see [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#single-host).



### Autoscaling TPUs in GKE

GKE supports Tensor Processing Units (TPUs) to accelerate machine learning workloads. Both [single-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#node_pool) and [multi-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#node_pool) support autoscaling and auto-provisioning.

With the [`--enable-autoprovisioning`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--enable-autoprovisioning) flag on a GKE cluster, GKE creates or deletes single-host or multi-host TPU slice node pools with a TPU version and topology that meets the requirements of pending workloads.

When you use [`--enable-autoscaling`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--enable-autoscaling), GKE scales the node pool based on its type, as follows:

  * _Single-host_ TPU slice node pool: GKE adds or removes TPU nodes in the existing node pool. The node pool may contain any number of TPU nodes between zero and the maximum size of the node pool as determined by the [\--max-nodes](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-nodes) and the [\--total-max-nodes](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--total-max-nodes) flags. When the node pool scales, all the TPU nodes in the node pool have the same machine type and topology. To learn more how to create a single-host TPU slice node pool, see [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#single-host).

  * _Multi-host_ TPU slice node pool: GKE atomically scales up the node pool from zero to the number of nodes required to satisfy the TPU topology. For example, with a TPU node pool with a machine type `ct5lp-hightpu-4t` and a topology of `16x16`, the node pool contains 64 nodes. The GKE autoscaler helps ensure that this node pool has exactly 0 or 64 nodes. When scaling back down, GKE evicts all scheduled pods, and drains the entire node pool to zero. To learn more how to create a multi-host TPU slice node pool, see [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#multi-host).




### Provision additional storage to a TPU slice

A VM in a TPU slice includes a 10 GB boot disk by default. If your TPU slice needs additional storage for training or preprocessing, or if you need to save checkpoints, you can use [Google Cloud Hyperdisk](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) or [Balanced Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk_types) storage if it's available for your TPU. For more information about supported disk types for each TPU version, see [TPU support for Google Cloud Hyperdisk and Persistent Disk](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute#tpu-support).

### CPU for Standard clusters

This section doesn't apply to Autopilot clusters because GKE places each TPU slice on its own node. To learn more, see [How TPUs work in Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot#how-it-works).

For Standard clusters, consider the following scheduling best practices.

To schedule a non-TPU workload on a VM in a TPU slice node, ensure that your GKE Pod can tolerate the `google.com/tpu` taint. If you want the workload to be deployed to specific nodes, use [node selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector).

Kubernetes resource management and priority treats VMs in TPUs the same as other VM types. To give scheduling priority to Pods that require TPUs over other Pods on the same nodes, request the maximum CPU or memory for those TPU slices. Low-priority TPU slices should do the following:

  1. Set low CPU and memory requests to ensure that the node has enough allocatable resources for the TPU workloads. To learn more, see [How Kubernetes applies resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#how-pods-with-resource-limits-are-run).
  2. Set no CPU limit (unlimited) to ensure that Pods can [burst](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#what-is-bursting) to use all unused cycles.
  3. Set appropriate memory limits to ensure Pods can function correctly without risking [node-pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/).



If a Kubernetes Pod doesn't request CPU and memory (even if it is requesting TPUs), then Kubernetes considers it a best-effort Pod, and there is no guarantee that it needed any CPU and memory. Only Pods that explicitly request CPU and memory have such guarantees. For specific Kubernetes scheduling, configure the Pod needs with explicit CPU and memory request. For more information, see [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

To learn more best practices, see [Kubernetes best practices: Resource requests and limits](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits).

### Reduce workload interruption

If you are using TPUs to train a machine learning model and your workload is interrupted, all work performed since the last checkpoint is lost. To decrease the probability that your workload is interrupted, do the following:

  * _Set a higher priority for this Job than for all other Jobs_ : If resources are scarce, the GKE scheduler preempts lower priority Jobs to schedule a higher priority Job. This also helps ensure that your higher priority workload receives all the resources that it needs (up to the total resources available in the cluster). To learn more, see [Pod priority and preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/).
  * _Configure maintenance exclusion_ : A maintenance exclusion is a non-repeating window of time during which automatic maintenance is forbidden. To learn more, see [Maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).
  * _Use extended run time Pods in Autopilot_ : Use [extended run time Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods) for a grace period of up to seven days before GKE terminates your Pods for scale-downs or node upgrades.
  * _Use collection scheduling in TPU Trillium_ : Use collections to indicate that a TPU slice node pool is part of a serving workload. Google Cloud limits and streamlines interruptions to the operations of inference workloads. To learn more, see [How collection scheduling works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling).



These recommendations help to minimize interruptions, but not to prevent them. For example, a preemption due to a hardware failure or preemption for defragmentation can still occur. Similarly, setting a GKE maintenance exclusion doesn't prevent Compute Engine maintenance events.

**Best practice** : 

Save checkpoints frequently and add code to your training script to start from the last checkpoint when resumed.

### Handle disruption due to node maintenance

The GKE nodes that host the TPUs are subject to maintenance events or other disruptions that might cause node shutdown. In GKE clusters with the control plane running version 1.29.1-gke.1425000 and later, you can reduce disruption to workloads by configuring GKE to terminate your workloads gracefully.

To understand, configure, and monitor disruption events that might occur on GKE nodes running AI/ML workloads, see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#gcloud).

### Maximize TPU utilization

To maximize your investment in TPUs, schedule a mix of Job priorities and queue them to maximize the amount of time that your TPUs are operating. For Job-level scheduling and preemption, you need to use an add-on to Kubernetes that orchestrates Jobs into queues.

**Best practice** : 

Use [Kueue](https://kueue.sigs.k8s.io/) to orchestrate Jobs into queues.

## What's next

  * Follow the [Deploy TPU workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus) to set up Cloud TPU with GKE.
  * Learn about [best practices](https://docs.cloud.google.com/tpu/docs/tpus) for using Cloud TPU for your machine learning tasks.
  * [Build large-scale machine learning on Cloud TPUs with GKE](https://www.youtube.com/watch?v=wtKhG1aTgtY).
  * [Serve Large Language Models with KubeRay on TPUs](https://www.youtube.com/watch?v=RK_u6cfPnnw).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
