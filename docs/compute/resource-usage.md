---
url: https://docs.cloud.google.com/compute/resource-usage/
title: Allocation quotas \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:35:47.499821+00:00
---

# Allocation quotas  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/resource-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Allocation quotas Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the _allocation quotas_ that apply to Compute Engine.

## Allocation quotas

Allocation quotas, also known as resource quotas, define the number of resources that your project has access to. Compute Engine enforces allocation quotas on resource usage for various reasons. For example, quotas help to protect the community of Google Cloud users by preventing unforeseen spikes in usage.

Google Cloud also offers [free trial quotas](https://cloud.google.com/free/docs/free-trial-quotas) that provide limited access for projects to help you explore Google Cloud on a free trial basis.

Not all projects have the same quotas. As you increasingly use Google Cloud over time, your quotas might increase accordingly. If you expect a notable upcoming increase in usage, you can proactively request quota adjustments from the [**Quotas**](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.

For information specific to quotas for rate limits for the Compute Engine API, see [API quota](https://docs.cloud.google.com/compute/api-quota).

**Important** : 

  * If you're using a [ Free Trial Cloud Billing account](https://docs.cloud.google.com/free/docs/free-cloud-features#confirm-status-of-account), then you can't request a change to your quota.
  * If your project's billing service is disrupted or if you change your project's billing account, your quotas reset to their default values.



## Quotas and resource availability

Allocation quotas are the maximum number of resources you can create of that resource type, if those resources are available. Quotas don't guarantee that resources are always available. If a resource is not available, or if the region you choose is out of the resource, you can't create new resources of that type, even if you have remaining quota in your region or project. For example, you might still have quota to create external IP addresses in `us-central1`, but there might not be available IP addresses in that region.

Similarly, even if you have a regional quota, a resource might not be available in a specific zone. For example, you might have quota to create VM instances in region `us-central1`, but you might not be able to create VM instances in the zone `us-central1-a` if the zone is depleted. In such cases, try creating the same resource in another zone, such as `us-central1-f`. To learn more about your options if zonal resources are depleted, see the documentation for [troubleshooting resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#resource_availability).

## Allocation quotas

When planning your VM instance needs, you should consider several quotas that affect how many VM instances you can create.

### Regional and global quotas

VM quotas are managed at the regional level. VM instance, instance group, disk quotas, and CPU can be consumed by any VM in the region, regardless of zone. For example, CPU quota is a regional quota, so there is a different limit and usage count for each region. To launch an `n2-standard-16` instance in any zone in the `us-central1` region, you need enough quota for at least 16 CPUs in `us-central1`.

Networking and load balancing quotas are required to create firewalls, load balancers, networks, and VPNs. These quotas are global quotas that don't depend on a region. Any region can use a global quota. For example, in-use and static external IP addresses assigned to load balancers and HTTP and HTTPS proxies consume global quotas.

### VM instances

The VM instances quota is a regional quota and limits the number of VM instances that can exist in a given region, regardless of whether the VM is running. This quota is visible in the Google Cloud console on the **Quotas** page. Compute Engine automatically sets this quota to be 10 times your regular CPU quota. You don't need to request this quota. If you need quota for more VM instances, request more CPUs because having more CPUs increases VM instance quota. The quota applies to both running and non-running VMs, and to normal and preemptible instances.

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the filter_list **Filter** list, select the following options:

     * For **Service** , select **Compute Engine API**.
     * For **Type** , select **Quota**.
     * For **Name** , select **VM instances**.
     * Optional: For **Metric** , select any other [CPU or Committed CPU quota name](https://docs.cloud.google.com/compute/resource-usage#cpu_quota) that you want to filter.
  3. Optional: To sort the table by region, click the **Dimensions (e.g. location)** column.

  4. Select the regions whose quota you want to change.

  5. Click edit **Edit**.

  6. Complete the form.

  7. Click **Submit Request**.




### Instance groups

To use instance groups, you must have available quota for all the resources that the group uses (for example, CPU quota) and available quota for the group resource itself. Depending on the type of group that you create, the following group resource usage quotas apply:

Service type | Service quota  
---|---  
Regional (multi-zone) managed instance group | `Regional instance group managers`  
Zonal (single-zone) managed instance group | Both of: 

  * `Instance group managers`
  * `Instance groups`

  
Unmanaged (single-zone) instance group | `Instance groups`  
Regional (multi-zone) autoscaler | `Regional autoscalers`  
Zonal (single-zone) autoscaler | `Autoscalers`  
  
### Disk quotas

The following Persistent Disk, Hyperdisk, and Local SSD quotas apply on a per-region basis:

  * `Hyperdisk Balanced Capacity (GB)`. This quota is the total combined size of [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) disks that you can create in a region. In the gcloud CLI and the API, this quota is referred to as `HDB-TOTAL-GB`.

This quota is shared between Hyperdisk Balanced and Hyperdisk Balanced High Availability disks. However, Hyperdisk Balanced High Availability disks consume quota at twice the rate of Hyperdisk Balanced disks. For example, creating 100 GB of Hyperdisk Balanced High Availability capacity counts as 200 GB against your `HDB-TOTAL-GB` limit.

  * `Hyperdisk Balanced Throughput (MB/s)`. This quota is the total amount of throughput that you can provision for all Hyperdisk Balanced disks in a zone. In the gcloud CLI and the API, this quota is referred to as `HDB-TOTAL-THROUGHPUT`.

  * `Hyperdisk Balanced IOPS`. This quota is the total amount of IOPS that you can provision for all Hyperdisk Balanced disks in a zone. In the gcloud CLI and the API, this quota is referred to as `HDB-TOTAL-IOPS`.

  * `Hyperdisk Extreme Capacity (GB)`. This quota is the total combined size of [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme) disks that you can create in a region. In the gcloud CLI and the API, this quota is referred to as `HDX-TOTAL-GB`.

**Note:** When you adjust your `HDX-TOTAL-GB` quota, you must also adjust your `SSD-TOTAL-GB`. `Hyperdisk Extreme Capacity` counts against `HDX-TOTAL-GB` and `SSD-TOTAL-GB` quotas simultaneously. If your `SSD-TOTAL-GB` quota is lower than your `HDX-TOTAL-GB` quota, you can't create additional disks once the `SSD-TOTAL-GB` limit is reached, even if you have remaining `HDX-TOTAL-GB` quota.
  * `Hyperdisk ML Capacity (GB)`. This quota is the total combined size of [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml) disks that you can create in a region. In the gcloud CLI and the API, this quota is referred to as `HDML-TOTAL-GB`.

  * `Hyperdisk ML Throughput (MB/s)`. This quota is the total amount of throughput that you can provision for all Hyperdisk ML disks in a region. In the gcloud CLI and the API, this quota is referred to as `HDML-TOTAL-THROUGHPUT`.

  * `Hyperdisk Throughput Capacity (GB)`. This quota is the total combined size of [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput) disks that you can create in a region. In the gcloud CLI and the API, this quota is referred to as `HDT-TOTAL-GB`.

**Note:** When you adjust your `HDT-TOTAL-GB` quota, you must also adjust your `DISKS-TOTAL-GB`. `Hyperdisk Throughput Capacity` counts against `HDT-TOTAL-GB` and `DISKS-TOTAL-GB` quotas simultaneously. If your `DISKS-TOTAL-GB` quota is lower than your `HDT-TOTAL-GB` quota, you can't create additional disks once the `DISKS-TOTAL-GB` limit is reached, even if you have remaining `HDT-TOTAL-GB` quota.
  * `Persistent disk standard (GB)`. This quota is the total size of [Standard Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) that can be created in a region. In the gcloud CLI and the API, this quota is referred to as `DISKS-TOTAL-GB`. This quota also applies to:

    * [Regional Standard Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#repds), but Regional Persistent Disk consume twice the amount of quota per GiB due to replication in two zones within a region.
    * When you choose to preserve Local SSD data when you stop or suspend a VM, an equivalent amount of Standard Persistent Disk quota is consumed. 
  * `Persistent disk SSD (GB)`. This quota is the total combined size of [SSD-backed Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) volumes that can be created in a region. In the gcloud CLI and the API, this quota is referred to as `SSD-TOTAL-GB`. This quota is separate from quota for Local SSD disks. This quota applies to the following disk types:

    * Zonal and Regional SSD Persistent Disk
    * Zonal and Regional Balanced Persistent Disk

[Regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#repds) volumes consume twice the amount of quota per GiB due to replication in two zones within a region.

  * `Persistent Disk IOPS`. This quota is the total number of I/O operations per second for Extreme Persistent Disk volumes that can be created in a region. In the gcloud CLI and the API, this quota is referred to as `PD-EXTREME-TOTAL-PROVISIONED-IOPS`. This quota is separate from the IOPS quota for Google Cloud Hyperdisk.

  * `Local SSD per machine family (GB)`. This quota is the total combined size of [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) disks you can attach to VMs in a region based on the machine type of each VM. Local SSD is a fast, ephemeral disk that should be used for scratch, local cache, or processing jobs with high fault tolerance because the disk is not intended to survive VM instance reboots.

Local SSD disks are sold in increments of 375 GiB or 3 TiB, depending on the machine type. There is also a [maximum number of Local SSD disks that can be attached to a single VM](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds), depending on the machine type. The maximum number of Local SSD disks, and the size of each Local SSD disk create a limit on the total amount of Local SSD disk capacity you can allocate for a VM. In the gcloud CLI and the API, this limit is referred to as the `LOCAL_SSD_TOTAL_GB_PER_VM_FAMILY` quota.

**Note:** `LOCAL_SSD_TOTAL_GB` quota has been deprecated. To view the local SSD quota usage and limits, you must use the quota metric `compute.googleapis.com/local_ssd_total_storage_per_vm_family` BETA in your Cloud Monitoring dashboards, alerts, and queries. For more information, see [View and manage local SSD quota](https://docs.cloud.google.com/compute/docs/quotas/migrate-local-ssd-quota).

For A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High, A3 Edge, A2 ultra, and G4 machine types, you don't need to request this quota as Local SSDs are automatically added to VMs created by using these machine types. However, you need to request `LOCAL_SSD_TOTAL_GB_PER_VM_FAMILY` for the other [accelerator-optimized VMs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).




### Storage pool quotas

For capacity, Hyperdisk Storage Pools with [Advanced capacity provisioning](https://docs.cloud.google.com/compute/docs/disks/storage-pools#advcap-pools) have the following quotas, measured in GB (or 1,000 MB): 

  * `Hyperdisk Balanced Storage Pools Advanced Capacity (GB)`: The total amount of disk space that you can reserve per region in a Hyperdisk Balanced Storage Pool with Advanced capacity provisioning.

    * gcloud CLI and the API: `HDB-STORAGE-POOL-TOTAL-ADVANCED-CAPACITY`
    * Metric: `compute.googleapis.com/hyperdisk_balanced_storage_pools_advanced_capacity`
  * `Hyperdisk Throughput Storage Pools Advanced Capacity (GB)`: The total amount of disk space you can reserve per region in a Hyperdisk Throughput Storage Pool with Advanced capacity provisioning.

    * gcloud CLI and the API: `HDT-STORAGE-POOL-TOTAL-ADVANCED-CAPACITY`
    * Metric: `compute.googleapis.com/hyperdisk_throughput_storage_pools_advanced_capacity`



For performance, Hyperdisk Storage Pools with [Advanced performance provisioning](https://docs.cloud.google.com/compute/docs/disks/storage-pools#advperf-pools) have the following quotas:

  * `Hyperdisk Balanced Storage Pools Advanced IOPS`: The total IOPS that you can reserve in a Hyperdisk Balanced Storage Pool with Advanced performance provisioning for a region.

    * gcloud CLI and the API: `HDB-STORAGE-POOL-TOTAL-ADVANCED-IOPS`
    * Metric: `compute.googleapis.com/hyperdisk_balanced_storage_pools_advanced_iops`
  * `Hyperdisk Balanced Storage Pools Advanced Throughput (MB/s)`: The total throughput that you can reserve in a Hyperdisk Balanced Storage Pool with Advanced performance provisioning for a region.

    * gcloud CLI and the API: `HDB-STORAGE-POOL-TOTAL-ADVANCED-THROUGHPUT`
    * Metric: `compute.googleapis.com/hyperdisk_balanced_storage_pools_advanced_throughput`
  * `Hyperdisk Throughput Storage Pools Advanced Throughput (MB/s)`: The total throughput that you can reserve in a Hyperdisk Throughput Storage Pool with Advanced performance provisioning for a region.

    * gcloud CLI and the API: `HDT-STORAGE-POOL-TOTAL-ADVANCED-THROUGHPUT`
    * Metric: `compute.googleapis.com/hyperdisk_throughput_storage_pools_advanced_throughput`



### Commitment and committed resource quotas

Committed use discounts (CUDs) help you save on your Compute Engine usage costs. You get these discounts by purchasing a committed use contract (also known as a _commitment_). Your commitment can be either a [resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) (where you commit to a minimum amount of usage) or a [spend-based commitment](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) (where you commit to spend a minimum amount for a product or service).

Spend-based commitments don't require any quotas, whereas resource-based commitments do. _Before_ you can purchase a resource-based commitment for specific regional resources, you must have quota available in that region for both of the following:

  * **Commitments**. Resource-based commitments are regional resources themselves, so you must have quota available to create that regional resource.

  * **Committed resources (except memory)**. These are the resources that you specify in your commitment. You must have quota in the region for the committed SKUs of any vCPUs, GPUs, or Local SSD disks that you want to specify in your commitment.




For more information, see [Quotas for commitments and committed resources](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#quota).

### CPU quota limits

CPU quota is the total number of virtual CPUs across all of your VM instances in a region. CPU quotas apply to running VMs and VM reservations. Both predefined and [preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible) consume this quota.

To help protect Compute Engine systems and other users, some new accounts and projects also have a global `CPUs (All Regions)` quota. That quota applies to all regions and is measured as a sum of all your vCPUs in all regions.

For example, if you have 48 vCPUs remaining in a single region such as `us-central1` but only 32 vCPUs remaining for the `CPUs (All Regions)` quota, you can launch only 32 vCPUs in the `us-central1` region, even though there is remaining quota in the region. This is because you reach the `CPU (All Regions)` quota and need to delete existing instances before you can launch new instances.

E2 and N1 machine types share a CPU quota pool. Unless otherwise noted, all other machine types have unique, separate CPU quota pools.

**Note:** M1 machine types started before November 2020 consume quota of type `CPUS`. M1 machine types created or restarted after November 2020 consume `M1_CPUS` quota.

The following table lists the quota names for Compute Engine machine types. If quota isn't applicable to the machine type, the value N/A for "Not applicable" is displayed.

Machine type | Quota pool | CPU quota name | Dimension | Committed CPU quota name | N1 | shared pool | `CPUS` | Not applicable | `Committed_CPUS`  
---|---|---|---|---  
E2 | shared pool | `CPUS` | Not applicable | `Committed_CPUS`  
N2 | separate pool | `N2_CPUS` | Not applicable | `Committed_N2_CPUS`  
N2D | separate pool | `N2D_CPUS` | Not applicable | `Committed_N2D_CPUS`  
N4 | separate pool | `CPUS_PER_VM_FAMILY`  
| `vm_family="N4"` | `Committed_N4_CPUS`  
N4A | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="N4A"` | `Committed_N4A_CPUS`  
N4D | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="N4D"` | `Committed_N4D_CPUS`  
T2D | separate pool | `T2D_CPUS` | Not applicable | `Committed_T2D_CPUS`  
T2A | separate pool | `T2A_CPUS` | Not applicable | Not available for T2A  
Z3 | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="Z3"` | `Committed_Z3_CPUS`  
Z4D | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="Z4D"` | `Committed_Z4D_CPUS`  
M1 | separate pool | `M1_CPUS` | Not applicable | `Committed_MEMORY-OPTIMIZED_CPUS`  
M2 | separate pool | `M2_CPUS` | Not applicable | `Committed_MEMORY-OPTIMIZED_CPUS`  
M3 | separate pool | `M3_CPUS` | Not applicable | `Committed_M3_CPUS`  
M4 | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="M4"` | `Committed_M4_CPUS`  
M4N | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="M4N"` | `Committed_M4N_CPUS`  
X5 | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="X5"` | `Committed_X5_CPUS`  
X4 | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="X4"` | `Committed_X4_CPUS`  
H4D | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="H4D"` | `Committed_H4D_CPUS`  
H3 | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="H3"` | `Committed_H3_CPUS`  
C2 | separate pool | `C2_CPUS` | Not applicable | `Committed_C2_CPUS`  
C2D | separate pool | `C2D_CPUS` | Not applicable | `Committed_C2D_CPUS`  
C3 | separate pool | `C3_CPUS` | Not applicable | `Committed_C3_CPUS`  
C3D | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="C3D"` | `Committed_C3D_CPUS`  
C4 | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="C4"` | `Committed_C4_CPUS`  
C4A | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="C4A"` | `Committed_C4A_CPUS`  
C4D | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="C4D"` | `Committed_C4D_CPUS`  
C4N | separate pool | `CPUS_PER_VM_FAMILY` | `vm_family="C4N"` | `Committed_C4N_CPUS`  
A2* | separate pool | `A2_CPUS` | Not applicable | `Committed_A2_CPUS`  
A4X Max† | N/A for A4X Max | N/A for A4X Max | Not applicable | N/A for A4X Max  
A4X† | N/A for A4X | N/A for A4X | Not applicable | N/A for A4X  
A4† | N/A for A4 | N/A for A4 | Not applicable | N/A for A4  
A3† | N/A for A3 | N/A for A3 | Not applicable | N/A for A3  
G4† | N/A for G4 | N/A for G4 | Not applicable | N/A for G4  
G2† | N/A for G2 | N/A for G2 | Not applicable | N/A for G2  
Preemptible VMs | shared pool | `PREEMPTIBLE_CPUS` | Not applicable | Not available for preemptible VMs  
  
*To create A2 VMs, you only need to have the required NVIDIA A100 GPU quotas. You don't need to request CPU quotas. 

† To create A4X Max, A4X, A4, A3, G4, and G2 VMs, you only need to have the required NVIDIA GB300, GB200, B200, H200, H100, RTX PRO 6000, or L4 GPU quotas for the VM type. You don't need to request CPU quotas.

### GPU quota

To ensure you have enough GPUs available in your project, check the [Quotas page](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console. Request a quota increase if you need one. New accounts and projects have a global GPU quota that applies to all regions.

Similar to virtual CPU quota, your GPU quota refers to the total number of virtual GPUs in all your VM instances in a region. Running instances and reservations consume GPU quotas. You have different quotas for creating standard instances, Spot VMs (for example, preemptible instances), virtual workstations, or instances that use committed use.

When you request a GPU quota, request a quota for the GPU models that you want to create in each region. Also request an additional global quota (`GPUs (all regions)`) for the total number of GPUs of all types in all regions.

The following table lists the GPU quotas available for each machine type.

**Caution:** NVIDIA T4 and P4 GPUs reach end of support on August 1, 2027. For more information, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) and [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos). 

Machine type | GPU type | Standard quota | Committed quota | Virtual workstation quota | Preemptible quota | Preemptible virtual workstation quota | A4X Max | GB300 | Not available | `COMMITTED_NVIDIA_GB300_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_GB300_GPUS` | Not available  
---|---|---|---|---|---|---  
A4X | GB200 | Not available | `COMMITTED_NVIDIA_GB200_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_GB200_GPUS` | Not available  
A4 | B200 | Not available | `COMMITTED_NVIDIA_B200_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_B200_GPUS` | Not available  
A3 Ultra | H200 | Not available | `COMMITTED_NVIDIA_H200_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_H200_GPUS` | Not available  
A3 Mega | H100 | `GPU_FAMILY:NVIDIA_H100_MEGA` | `COMMITTED_NVIDIA_H100_MEGA_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_H100_MEGA_GPUS` | Not available  
A3 Edge and A3 High | H100 | `GPU_FAMILY:NVIDIA_H100` | `COMMITTED_NVIDIA_H100_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_H100_GPUS` | Not available  
A2 Ultra | A100 80GB | `NVIDIA_A100_80GB_GPUS` | `COMMITTED_NVIDIA_A100_80GB_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_A100_80GB_GPUS` | Not available  
A2 Standard | A100 40GB | `NVIDIA_A100_GPUS` | `COMMITTED_NVIDIA_A100_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_A100_GPUS` | Not available  
G4 | RTX PRO 6000 | `GPU_FAMILY:NVIDIA_RTX_PRO_6000` | `COMMITTED_NVIDIA_RTX_PRO_6000_GPUS` | `NVIDIA_RTX_PRO_6000_VWS_GPUS` | `PREEMPTIBLE_NVIDIA_RTX_PRO_6000_GPUS` | `PREEMPTIBLE_NVIDIA_RTX_PRO_6000_VWS_GPUS`  
G2 | L4 | `GPU_FAMILY:NVIDIA_L4` | `COMMITTED_NVIDIA_L4_GPUS` | `NVIDIA_L4_VWS_GPUS` | `PREEMPTIBLE_NVIDIA_L4_GPUS` | `PREEMPTIBLE_NVIDIA_L4_VWS_GPUS`  
N1 | T4 | `NVIDIA_T4_GPUS` | `COMMITTED_NVIDIA_T4_GPUS` | `NVIDIA_T4_VWS_GPUS` | `PREEMPTIBLE_NVIDIA_T4_GPUS` | `PREEMPTIBLE_NVIDIA_T4_VWS_GPUS`  
N1 | V100 | `NVIDIA_V100_GPUS` | `COMMITTED_NVIDIA_V100_GPUS` | Not available | `PREEMPTIBLE_NVIDIA_V100_GPUS` | Not available  
N1 | P4 | `NVIDIA_P4_GPUS` | `COMMITTED_NVIDIA_P4_GPUS` | `NVIDIA_P4_VWS_GPUS` | `PREEMPTIBLE_NVIDIA_P4_GPUS` | `PREEMPTIBLE_NVIDIA_P4_VWS_GPUS`  
  
### TPU quota

To ensure you have enough TPUs available in your project, check the [Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console. [Request a quota increase](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota) if you need more quota.

Your TPU quota refers to the total number of TPU chips that your project can use in a region. Running instances and reservations consume TPU quotas. You have different quotas for creating standard (on-demand) instances or Spot VMs (for example, preemptible instances).

When you request a TPU quota, request a quota for the TPU version that you want to create in each region.

The following table lists the quota names for each TPU version. To view the quota for a specific version, filter by the quota name and, where applicable, the given dimension.

TPU version | Standard quota | Preemptible quota | TPU7x | `TPUs per TPU family`  
Dimension: `tpu_family:tpu7x` | `Preemptible TPU slices tpu7x`  
---|---|---  
v6e | `TPUs per TPU family`  
Dimension: `tpu_family:CT6E` | `Preemptible TPU slices v6e`  
v5p | `TPU v5p chips` | `Preemptible TPU v5p chips`  
  
### Preemptible quotas

You can [request](https://docs.cloud.google.com/docs/quotas/help/request_increase) preemptible quotas for `Preemptible CPUs`, `Preemptible GPUs`, and `Preemptible Local SSDs (GB)`. These preemptible quotas apply to the CPUs, GPUs, and Local SSDs of the following VMs:

  * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) and [legacy preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible)
  * [GPU VMs with predefined run times](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas)
  * [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)



If your project does not have preemptible quota, and you have never requested preemptible quota, these resources consume standard quota. However, after you request preemptible quota in your project, the applicable resources can only consume preemptible quota and can't revert to consuming standard quotas.

Requesting preemptible quotas can help you improve quota obtainability by providing separate quotas for temporary resources. After Compute Engine grants you preemptible quota in a region, all applicable resources automatically consume preemptible quota. If this quota is depleted, you must request preemptible quota for those resources.

### External IP addresses

You must have enough external IP addresses for every VM that needs to be directly reachable from the public internet. Regional IP quota is for assigning IPv4 or IPv6 addresses to VMs in that region. IPv6 IP addresses use the same quota types as for IPv4 IP addresses, except for external and internal IPv6 static addresses, which have their own quota types.

Global IP quota is for assigning IPv4 addresses to global networking resources such as load balancers.

Google Cloud offers different types of IP addresses, depending on your needs. For information about costs, refer to [External IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress). For information about quota specifics, see [Quotas and limits](https://docs.cloud.google.com/vpc/docs/quota).

  * **Static IP addresses**. The number of static regional external IPv4 addresses that you can reserve in each region in your project.
  * **Regional static external IPv6 address ranges:** The number of static regional external IPv6 address ranges that you can reserve in each region in your project.
  * **Static IP addresses global** : External IP addresses reserved for your resources that persist through machine restarts. You can register these addresses with DNS and domain provider services to provide a user-friendly address. For example, `www.example-site.com`.
  * **In-use IP addresses**. The number of static and ephemeral regional external IP addresses that you can use in your project simultaneously.
  * **In-use IP addresses global**. The number of static and ephemeral global external IP addresses that you can use in your project simultaneously.

**Note:** If the same IP address is assigned to more than one forwarding rule, Google Cloud counts and adds each usage of the address towards the `IN_USE_ADDRESSES` quota rather than a unique count of IP address objects that are used.



## Quota rollouts

Occasionally, Google Cloud changes the default quota for resources and APIs. These changes take place gradually. During the rollout of a new default quota, the maximum quota that appears in the Google Cloud console might not reflect the actual maximum quota that is available to you. You can [view the ongoing quota rollouts](https://docs.cloud.google.com/docs/quotas/view-ongoing-rollouts) by using Google Cloud console or Cloud Quotas API.

For example, suppose that Google Cloud changes the default maximum quota for firewall rules from `200` to `300`, and you use the Google Cloud console to view your quota, you might see the new quota of `300`, even though your actual quota is `200` until the rollout completes.

If a quota rollout is ongoing and you want to confirm the actual maximum quota that is available to you, [use the Google Cloud CLI to check your quota](https://docs.cloud.google.com/compute/quotas-limits#check_your_allocation_quota). If you need more quota than you have access to, [submit a quota adjustment request](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## What's next

  * Read about [resource-based pricing](https://docs.cloud.google.com/compute/resource-based-pricing).
  * Read about [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * Learn how to [view and manage quota](https://docs.cloud.google.com/docs/quotas/view-manage).
  * Learn how to [set up quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts).
  * Learn how to [automatically increase quota based on your Compute Engine resources' usage](https://docs.cloud.google.com/capacity-planner/docs/enable-quota-adjuster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
