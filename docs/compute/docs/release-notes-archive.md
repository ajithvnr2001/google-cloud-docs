---
url: https://docs.cloud.google.com/compute/docs/release-notes-archive/
title: Archived release notes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:28.499422+00:00
---

# Archived release notes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/release-notes-archive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Archived release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to the Compute Engine service.

**Latest API version: v1**

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/compute-engine-release-notes.xml) directly. 

## December 21, 2023

Feature

**Generally available** : The [accelerator-optimized A3 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) is now available on Compute Engine. The A3 machine type has NVIDIA® H100 80GB GPUs attached, which can be used to support your large artificial intelligence (AI) models, machine learning (ML), and high performance computing (HPC) workloads. The A3 machine type is available in the following regions and zones:

  * APAC 
    * Singapore: `asia-southeast1-b,c`
  * Europe 
    * Netherlands: `europe-west4-b.c`
  * North America 
    * Iowa: `us-central1-a,c`
    * Virginia: `us-east4-a,c`
    * Ohio: `us-east5-a`



## December 20, 2023

Feature

**Generally available** : You can rename an existing VM using the Google Cloud console, gcloud CLI, and REST. For more information, see [Rename a VM](https://docs.cloud.google.com/compute/docs/instances/rename-instance).

## December 13, 2023

Feature

**Generally available** : NVIDIA L4 GPUs are now available in the following additional regions and zones:

  * Seoul, South Korea (`asia-northeast3-a`)
  * Moncks Corner, South Carolina (`us-east1-c`)



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## December 12, 2023

Feature

**Preview** : The following quotas and metrics are now available to help you monitor the usage and limits for Compute Engine concurrent operation quotas:

  * Quotas for global concurrent operations (metric - `compute.googleapis.com/global_concurrent_operations`): 
    * `Concurrent global operations per project`
    * `Concurrent global operations per project operation type`
  * Quotas for regional concurrent operations (metric: `compute.googleapis.com/regional_concurrent_operations`): 
    * `Concurrent regional operations per project`
    * `Concurrent regional operations per project operation type`



For more information, see [Concurrent operation quotas](https://docs.cloud.google.com/compute/operations-quota).

## December 07, 2023

Feature

**Preview:** Managed instance groups (MIGs) let you create pools of suspended and stopped virtual machine (VM) instances. You can manually suspend and stop VMs in a MIG to save on costs, or use suspended and stopped pools to speed up scale out operations of your MIG.

For more information, see [Work with suspended and stopped VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig).

## December 04, 2023

Feature

**Generally available** : The following location and scale enhancements for [Persistent Disk Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) are generally available:

  * **Larger disk capacity:** the maximum disk size has increased from 2 TiB to 5 TiB.
  * **Faster replication rate:** the disk data replication rate has increased from 100 MB/min to 250 MB/min.
  * **Expanded regional support** : PD Async Replication is available in 15 additional regions across Europe, APAC, and North America. For the full list of available regions, see [Supported region pairs](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).



## November 13, 2023

Feature

**Preview** : When creating or modifying an on-demand reservation, you can configure reservations to be automatically deleted at a specific date and time. Automatically deleting reservations makes it easier to prevent charges from unused reservations when you no longer need them.

For more information, see the documentation for [creating on-demand reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project).

## November 10, 2023

Feature

**Preview** : In a managed instance group (MIG), you can turn off repairs to inspect failed and unhealthy VMs, to implement your own repair logic, or to monitor the application health without triggering repairs by MIG. For more information, see [Turn off repairs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).

## November 07, 2023

Feature

**Generally available:** A replica recovery checkpoint of a regional Persistent Disk volume represents the most recent crash-consistent point in time of the fully replicated disk. For disks that are not fully replicated, you can use the checkpoint to create disk snapshots from an incomplete zonal replica. You can create and use these snapshots to recover disk data in the rare scenario where your synced replica goes down before your incomplete replica catches up.

Learn more about [Regional Persistent Disk replica recovery checkpoints](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-replica-recovery-checkpoint) and [how to use checkpoints to recover a degraded disk](https://docs.cloud.google.com/compute/docs/disks/repd-failover#recover-repd-using-checkpoint).

## November 03, 2023

Feature

The `h3-node-88-352` [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) is now **Generally Available**.

## November 01, 2023

Feature

**Generally available:** When assigning a custom queue count for the [receive and transmit queues](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) for a vNIC, under certain conditions, you can configure a number of custom queue counts that exceeds the number of vCPUs allocated to the VM.

## October 31, 2023

Feature

**Preview:** Advanced maintenance control for sole-tenancy lets you control planned maintenance events for sole-tenant node groups and minimise maintenance-related disruptions. This feature is available only for sole-tenant node groups. To use this feature with your existing virtual machines, you must first move your VMs to sole-tenant node groups that have advanced maintenance control enabled.

The advanced maintenance control for sole-tenancy feature lets you:

  * Check for maintenance events scheduled for a sole-tenant node 28 days in advance.
  * Trigger maintenance immediately or schedule it for later. Note that if you trigger maintenance immediately, the maintenance takes place within 24-hours from the time you trigger the request.



For more information, see [Advanced maintenance control for sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control).

## October 27, 2023

Feature

**Preview** : Hyperdisk Balanced is now available in preview with H3 VMs. Hyperdisk Balanced is a good fit for a wide range of use cases such as LOB applications, web applications, and medium-tier databases that don't require the performance of Hyperdisk Extreme. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

## October 25, 2023

Feature

**Preview** : Project zonal metadata is custom project metadata that you can set exclusively for VMs in a specific zone in a project. Project zonal metadata helps you with fault isolation and provides greater reliability. By setting custom project zonal metadata, you gain more control over the project metadata for your VMs and limit the impact of any incorrect metadata updates to VMs within the specific zone.

Learn more about [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) and how to [set custom project zonal metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

## October 17, 2023

Feature

**Generally available** : `c3d-standard`, `c3d-highmem`, `c3d-highcpu`, and `c3d-standard-lssd` machine types for general-purpose [C3D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series) are generally available.

## October 13, 2023

Feature

**Generally available:** C3 VMs support Compute Engine flexible committed use discounts (CUDs).

Compute Engine flexible CUDs allow you to commit to a minimum hourly spend amount and use vCPUs and/or memory in any of the projects within your Cloud Billing account, across any region, and belonging to any eligible machine types. Learn more about [Compute Engine Flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) and [how to purchase flexible commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

Deprecated

If you want to modify a future reservation request using the Compute Engine API, the `paths` query parameter is deprecated. Instead, use the `updateMask` query parameter.

For more information, see [Modify future reservation requests](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#modify-future-reservations).

Feature

**Preview** : You can now use [workforce identity federation with OS Login](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#use_workforce_identity_federation_with_os_login).

## October 12, 2023

Feature

**Preview** : The following metrics are now available to help you monitor your Persistent Disk and Hyperdisk volume performance:

  * Average I/O latency (`compute.googleapis.com/instance/disk/average_io_latency`)

  * Average I/O queue depth (`compute.googleapis.com/instance/disk/average_io_queue_depth`)




To learn more about these metrics and how to view them, see [Review disk metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).

## October 11, 2023

Feature

**Generally available** : You can configure stateful IP addresses in a managed instance group. Stateful IP addresses are preserved when VM instances in the group are repaired, updated, and re-created. For more information, see [Configuring stateful IP addresses in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs).

## October 09, 2023

Feature

**Generally available** : H3 VMs, designed for compute-intensive high performance computing (HPC) workloads, are now generally available. For more information, see [H3 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series).

Change

When you install the Ops Agent on a Compute Engine VM by using the **Observability** tab on a Compute Engine VM details page, the agent is now installed with an Ops Agent OS policy. This installation method replaces the prior set of manual steps. For more information, see [Installing the agent by using the Google Cloud console](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#gce-ui-install).

## October 06, 2023

Feature

**Generally available** : NVIDIA L4 GPUs are now available in the following additional regions and zones:

  * APAC 
    * Seoul, South Korea (`asia-northeast3-b`)
  * Europe 
    * St. Ghislain, Belgium (`europe-west1-b`)
    * Frankfurt, Germany (`europe-west3-b`)
  * North America 
    * Council Bluffs, Iowa: (`us-central1-c`)
    * Las Vegas, Nevada (`us-west4-a,c`)



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## October 04, 2023

Feature

**Generally available** : NVIDIA L4 GPUs are now available in the following additional regions and zones:

  * Singapore(`asia-southeast1-a`)



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## September 27, 2023

Issue

Creating a reservation or future reservation request by using an instance template that specifies an A2, C3, or G2 machine type causes errors or problems with consumption. For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#reservations-with-template-error).

## September 26, 2023

Feature

**Preview** : `c3d-standard`, `c3d-highmem`, `c3d-highcpu`, and `c3d-standard-lssd` virtual machines are available in the following regions:

  * Council Bluffs, Iowa, North America, `us-central1`
  * Moncks Corner, South Carolina, North America, `us-east1`
  * Ashburn, Virginia, North America , `us-east4`
  * St. Ghislain, Belgium, Europe, `europe-west1`
  * Eemshaven, Netherlands, Europe, `europe-west4`
  * Jurong West, Singapore, Asia, `asia-southeast1`



See the [General purpose machines](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) document for details.

## September 22, 2023

Feature

**Preview** : You can now view the organization-wide [patch status dashboard](https://docs.cloud.google.com/compute/docs/os-patch-management/view-patch-summary) and [OS policy compliance reports](https://docs.cloud.google.com/compute/docs/os-configuration-management/view-compliance#policy-summary) by using VM Manager.

Feature

**Preview** : Compute Engine API now enforces the **Filtered list cost overhead** quota, which limits the number of resources to be filtered out from server-side `*.list` and `*.aggregatedList` methods.

The quota is charged against the following metrics:

  * Global: `compute.googleapis.com/filtered_list_cost_overhead`
  * Regional: `compute.googleapis.com/filtered_list_cost_overhead_per_region`



For more information, see [Rate quotas](https://docs.cloud.google.com/compute/api-quota#api-rate-limits) and [best practices for list filtering](https://docs.cloud.google.com/compute/docs/api/best-practices#client-side-filter).

Change

The Google Cloud console labels for **OS patch management** and **OS configuration management** on VM Manager pages have been renamed to **Patch** and **OS policies** respectively.

## September 21, 2023

Feature

**Generally available** : Autohealing in managed instance groups (MIG) supports [regional health checks](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks). To reduce cross-region dependency or to achieve data residency, use a regional health check. For more information, see [Set up an application health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

Feature

**Generally available** : Instance templates are available as both regional and global resources. To reduce cross-region dependency or to achieve data residency, use a regional instance template to create virtual machines (VM), managed instance groups (MIG), or reservations. For more information, see [Regional and global instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#regional_and_global_instance_templates).

## September 19, 2023

Feature

**Generally available** : Dammam, Kingdom of Saudi Arabia, Middle East `me-central2-a,b,c` has launched with [E2, N2, N2D, and T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines) VMs in all three zones. See the [Dammam region access](https://docs.cloud.google.com/docs/dammam-region-access) document to learn more.

## September 18, 2023

Feature

**Preview** : Snapshot settings are centralized configuration parameters for all snapshots in a project. You can use snapshot settings to customize the default storage location for all future snapshots in your project. By enabling you to do this, snapshot settings remove the need for you to manually specify a storage location during each individual snapshot creation.

Learn more about [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) and how to [set the default storage location for a project using snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings#snapshot_settings_how_to_update).

## September 15, 2023

Feature

**Generally available** : The Red Hat Knowledgebase provides you with access to articles, solutions, product documentation, and community discussions for Red Hat products.

You can now access the Red Hat Knowledgebase by using single-sign-on (SSO) through the Google Cloud console from your Red Hat Enterprise Linux (RHEL) VMs. For more information, see [Access Red Hat Knowledgebase](https://docs.cloud.google.com/compute/docs/images/premium/access-rhel-knowledgebase).

## September 14, 2023

Feature

**Generally available** : You can create C3-standard VMs with Local SSD attached using new machine types, for example `c3-standard-44-lssd`. For more information, see [Choosing a valid number of Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds).

## September 12, 2023

Change

You can manage future reservations using the Google Cloud console. Future reservations provide a high level of assurance to obtain important or difficult-to-obtain capacity in advance.

For more information, see the following pages:

  * [Create future reservation requests for a single project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations)
  * [Create shared future reservation requests](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations)
  * [Delete future reservation requests](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#delete-future-reservation)
  * [Modify future reservation requests](https://docs.cloud.google.com/compute/docs/instances/manage-future-reservations#modify-future-reservations)
  * [View future reservation requests](https://docs.cloud.google.com/compute/docs/instances/view-future-reservations)



## August 30, 2023

Feature

**Generally available** : NVIDIA L4 GPUs are now available in the following additional regions and zones:

  * APAC 
    * Taiwan (`asia-east1-a,c`)
    * Tokyo (`asia-northeast1-a,c`)
    * Singapore(`asia-southeast1-c`)
  * Europe 
    * Belgium (`europe-west1-c`)
    * London (`europe-west2-a,b`)
  * North America 
    * Northern virginia (`us-east4-c`)
    * Dalles (`us-west1-c`)



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## August 29, 2023

Feature

**Preview** : You can use future reservations to reserve resources at a specific date and time in the near future.

Future reservations are useful for obtaining capacity for future peak-demand events or highly-demanded resources. For more information, see [About future reservation requests](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview).

## August 25, 2023

Feature

**Preview** : You can reduce network latency between VMs by using compact placement policies to specify the maximum distance between VMs. Use compact placement policies to optimize workloads with frequent communication across VMs—for example, high-performance computing (HPC), machine learning (ML), or database server workloads. You can keep VMs in the same rack, across adjacent racks within the same cluster, or across adjacent clusters.

For more information, see [Reduce latency by using compact placement policies](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies).

## August 22, 2023

Feature

**Generally available** : Berlin, Germany, Europe `europe-west10-a,b,c` has launched with [E2, N2, N2D, and T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines) VMs available in all three zones.

## August 21, 2023

Feature

**Generally available** : When a managed instance group (MIG) repairs a failed or an unhealthy VM, you can apply the latest instance template and per-instance configuration to recreate the VM instead of applying the configuration originally used to create the VM. For more information, see [Apply configuration updates during repairs](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair).

Feature

**Generally available** : Hyperdisk Throughput is now available in the following additional regions and zones:

  * Council Bluffs, Iowa: `us-central1`
  * Moncks Corner, South Carolina: `us-east1`
  * Ashburn, Virginia: `us-east4-b, c`
  * Eemshaven, Netherlands: `europe-west4-a, c`
  * Jurong West, Singapore: `asia-southeast1`
  * Mumbai, India: `asia-south1-a`



## August 17, 2023

Feature

**Generally available** : The Ops Agent (version 2.38.0 and later) now supports the automatic tracking of GPU usage metrics reported from the NVIDIA Management Library (NVML) for Linux virtual machine instances that have attached NVIDIA GPUs. 

Through an available integration with NVIDIA's Data Center GPU Manager (DCGM), you can also track metrics such as Streaming Multiprocessor (SM) block utilization, SM occupancy, SM pipe utilization, PCIe traffic rate, and NVLink traffic rate. 

For more information, see [Monitoring GPU performance on Linux VMs](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).

## August 09, 2023

Feature

**Generally available** : You can use Cloud Monitoring to monitor the consumption of your reservations and set custom alerts. For more information, see [Monitor consumption of reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-monitor).

Feature

**Generally available** : If a host error occurs on a VM, you can control how much time Compute Engine spends recovering Local SSD data with the Local SSD recovery timeout setting. For more information, see [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence).

Feature

**Generally available** : Use the new [distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) ANY SINGLE ZONE in a regional Managed Instance Group (MIG) to automatically select a single zone that has available resources within your quota. Recommended for workloads that require low latency, high-bandwidth connections between VMs or when you want to avoid inter-zone network traffic costs.

## August 04, 2023

Feature

**Preview** : You can create C3 VMs with Local SSD attached using new machine types (`-lssd`). For more information, see [Add a local SSD to your VM](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd).

## August 02, 2023

Feature

**Preview** : H3 VMs, designed for compute-intensive high performance computing (HPC) workloads, are now in preview. For more information, see [H3 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series).

## July 28, 2023

Feature

**Generally available** : `c3-standard` and `c3-highmem` machine types for [general-purpose C3 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) are generally available.

## July 25, 2023

Feature

**Generally available** : You can modify the description, schedule frequency, retention policy, or labels for a snapshot schedule instead of creating a new snapshot schedule. For more information, see [Change a snapshot schedule](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots#change_snapshot_schedule).

## July 24, 2023

Feature

**Preview** : You can now use [SSH-in-browser to connect to TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm#tpu-connect).

## July 21, 2023

Feature

**Generally available** : NVIDIA T4 GPUs are now available in the following additional regions and zones:

  * Salt Lake City: `us-west3-b`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## July 12, 2023

Feature

**Generally available** : You can [enable faster network packet processing](https://docs.cloud.google.com/compute/docs/networking/use-dpdk) by using the Data Plane Development Kit (DPDK). DPDK helps you to optimize VMs that run network-intensive workloads, such as video streaming or voice calls.

## July 10, 2023

Feature

**Preview** : You can use instant snapshots to take in-place disk backups that can be restored to new disks under a minute. 

Instant snapshots are ideal for rapid data restoration within the same location as the source disk. For more information, see [Instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

## July 06, 2023

Feature

**Generally available** : You can now [use a regional Persistent Disk as a VM boot disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#use_repd_boot_disks).

## June 30, 2023

Feature

You can [suspend and resume](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) E2 VMs.

## June 29, 2023

Feature

**Preview** : `c3-standard` and `c3-highmem` machine types are now available for [general-purpose C3 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series).

## June 28, 2023

Feature

**Generally Available:** Persistent Disk Asynchronous Replication (PD Async Replication) is now generally available. For more information, see [About Persistent Disk Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).

## June 27, 2023

Feature

**Generally available** : NVIDIA A100 80GB GPUs are now available in the following additional regions and zones:

  * Ohio, North America: `us-east5-b`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## June 26, 2023

Feature

**Generally available** : For managed instance groups (MIGs), Google Cloud Console provides you with an improved way to configure [autoscaling based on Cloud Monitoring metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics). The redesigned user interface enables you to explore available metrics and filters. You can visualize the metric values in a chart, which also displays the aggregated value used for autoscaling.

## June 23, 2023

Feature

**Preview** : You can now use custom constraints to provide more granular and customizable control over specific fields for some Compute resources. For more information, see [Manage Compute Engine resources using custom constraints](https://docs.cloud.google.com/compute/docs/access/custom-constraints).

## June 09, 2023

Feature

**Generally available** : Hyperdisk Throughput provides cost-effective and throughput-oriented block storage with dynamically configurable capacity and throughput. Hyperdisk volumes are durable network storage devices that your VMs can access, similar to Persistent Disk. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

Feature

**Generally available** : NVIDIA A100 80GB GPUs are now available in the following additional regions and zones:

  * Iowa, North America: `us-central1-a`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## June 06, 2023

Issue

For MIGs that have T2D machine series VMs, autoscaling based on CPU utilization doesn't work as expected. For more details, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#managed_instance_group_having_t2d_machine_series_doesnt_autoscale_as_expected).

## June 05, 2023

Feature

**Generally available** : [Accelerator-optimized (G2) machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) with attached NVIDIA® L4 GPUs are generally available in the following regions and zones:

  * Singapore, APAC: `asia-southeast1-b`
  * Netherlands, Europe: `europe-west4-a,b,c`
  * Iowa, North America: `us-central1-a,b`
  * South Carolina, North America: `us-east1-b,d`
  * Virginia, North America: `us-east4-a`
  * Oregon, North America: `us-west1-a,b`



## May 31, 2023

Feature

**Preview** : In a managed instance group (MIG), you can set metadata and labels for all VMs in the group without the need to create a new instance template. For more information, see [Override instance template properties with an all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic).

Feature

The image import tool now supports importing [CentOS Stream 9 and CentOS Stream 8](https://docs.cloud.google.com/compute/docs/images/os-details#centos) images to Google Cloud.

## May 25, 2023

Feature

**Generally available** : NVIDIA A100 80GB GPUs are now available in the following additional regions and zones:

  * Netherlands, Europe: `europe-west4-a`
  * Singapore, APAC: `asia-southeast1-c`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## May 22, 2023

Feature

**Generally available** : [General purpose C3 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) are now generally available in the following regions:

  * Council Bluffs, Iowa, North America : `us-central1`
  * Moncks Corner, South Carolina, North America: `us-east1`
  * Ashburn, Virginia, North America: `us-east4`
  * St. Ghislain, Belgium, Europe: `europe-west1`
  * Eemshaven, Netherlands, Europe : `europe-west4`
  * Jurong West, Singapore, APAC: `asia-southeast1`



## May 19, 2023

Feature

**Preview:** You can now use the `discard-local-ssd=false` flag to preserve the contents of a single attached Local SSD disk when [suspending](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/suspend) or [stopping](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) a VM. For more information, see the [Local SSD Documentation](https://docs.cloud.google.com/compute/docs/disks/local-ssd).

## May 16, 2023

Feature

The image import tool now supports importing [Rocky Linux 9](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux) images to Google Cloud.

## May 15, 2023

Feature

**Generally available** : The local SSD quota per machine family (`LOCAL_SSD_TOTAL_GB_PER_VM_FAMILY`) is generally available. Use the quota metric `compute.googleapis.com/local_ssd_total_storage_per_vm_family` instead of `compute.googleapis.com/local_ssd_total_storage` to view the quota usage and limits for local SSD in your project. For more information, see [View and manage local SSD quota per machine family](https://docs.cloud.google.com/compute/docs/quotas/migrate-local-ssd-quota).

## May 05, 2023

Announcement

**End of life:** On May 1, 2024, NVIDIA K80s will be end of life and won't be available for new or existing VMs on Google Cloud.

For information about how to prepare for this EOL, see [NVIDIA K80 EOL](https://docs.cloud.google.com/compute/docs/eol/k80-eol).

## April 26, 2023

Security

Two vulnerabilities (CVE-2023-1017 and CVE-2023-1018) were discovered in Trusted Platform Module (TPM) 2.0.

For more information, see the [GCP-2023-004 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2023-004).

## April 25, 2023

Feature

In the Google Cloud console, the **Observability** tab on the [**VM instances**](https://console.cloud.google.com/compute/instances) page for Compute Engine has been enhanced. **Disk** and **Network** sections with additional charts have been added. The **Integrations > Detected** section lets you navigate to the dashboards for the third-party integrations that you have configured, like Apache or NGINX. The page also includes a set of recommended alerts for setting up pre-configured alerting policies for CPU, memory, and disk utilization and for host errors.

## April 24, 2023

Feature

You can now create regional Persistent Disk volumes when creating a new VM either directly, or through instance templates. For more information, see [Create a VM instance with additional non-boot disks](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#create_a_vm_instance_with_additional_non-boot_disks) or [Create a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

## April 20, 2023

Feature

**Preview** :

  * The [HPC Rocky Linux 8 image](https://docs.cloud.google.com/compute/docs/images#hpc_images) is now available for HPC workloads. 
  * The HPC VM Images now support Intel MPI 2021 with tools to easily installing the Intel MPI 2021 library, the net and psm3 libfabric providers. 
  * The HPC VM Images now support OpenMPI. For more details, see [Open MPI best practice guides](https://cloud.google.com/solutions/hpc#section-7).



## April 06, 2023

Feature

**Generally available** : You can now use the `gcloud` command-line tool to import images from AWS into Google Cloud. For more information, see [Importing images from AWS](https://docs.cloud.google.com/compute/docs/import/import-aws-image).

## April 04, 2023

Feature

**Preview** : [Accelerator-optimized (G2) machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) are now available on Compute Engine. Each G2 machine type has a fixed number of NVIDIA® L4 GPUs attached to support your next generation graphics performance workloads. The G2 machine types are available in the following three regions:

  * Iowa, North America: `us-central1-a,b`
  * Netherlands, Europe: `europe-west4-a`
  * Singapore, APAC: `asia-southeast1-b`



## March 31, 2023

Feature

**Generally available:** You can use the `Regional disk replica state` metric in [Cloud Monitoring](https://console.cloud.google.com/monitoring) to track the states of your regional Persistent Disk zonal replicas. You can also use the metric data to determine the replication state of your regional Persistent Disk volumes.

Learn more about [zonal replication for regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_zonal_replication) and [how to monitor the states of regional Persistent Disk zonal replicas](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state).

## March 30, 2023

Feature

**Preview** : Persistent Disk Asynchronous Replication (PD Async Replication) provides low recovery point objective (RPO) and low recovery time objective (RTO) block storage replication for cross-region active-passive disaster recovery. For more information, see [About Persistent Disk Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).

Feature

**Generally available** : Doha, Qatar, Middle East `me-central1-a,b,c` has launched with [E2 and N2 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) available in all three zones.

See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## March 28, 2023

Feature

**Generally Available** : You can test how workloads running on sole-tenant nodes behave during a host maintenance event, and see the effects of the sole-tenant VM's host maintenance policy on the applications running on the VMs.

For more information, see [Simulate host maintenance events on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#simulate_a_host_maintenance_event).

## March 23, 2023

Feature

**Generally available** : Turin, Italy, Europe `europe-west12-a,b,c` has launched with [E2, N2, N2D, and T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines) VMs available in all three zones. See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## March 21, 2023

Issue

Your automated processes might fail if they use API response data about your resource-based commitment quotas. For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues).

## March 17, 2023

Deprecated

**End of life** : On May 31, 2023, Ubuntu 18.04 LTS (Bionic) will reach end of life and the images deprecated on Google Cloud. If you use Ubuntu 18.04 LTS images in your project, review [Ubuntu LTS end of life](https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol).

## March 13, 2023

Feature

**Generally available** : Hyperdisk provides the fastest block storage for Compute Engine for your high-end, memory intensive workloads. Hyperdisk volumes are durable network storage devices that your VMs can access, similar to Persistent Disk. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

## February 28, 2023

Feature

**Generally available** : When creating a reservation, you can now include a compact placement policy to specify that VMs should be located as close to each other as possible to reduce network latency. Learn how to [create a reservation that specifies a compact placement policy](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#creating_a_reservation).

## February 22, 2023

Feature

**Generally available:** You can upgrade the term of your 1-year commitments and convert them into 3-year commitments to get a higher discount percentage for your committed resources and continue receiving the discounts for a longer time period.

For more information, see [Upgrade the term of commitments](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).

## February 21, 2023

Feature

**Generally available** : The image import tool now supports importing [SUSE Linux Enterprise Server 15 SP4 and SUSE Linux Enterprise Server 15 SP4 for SAP](https://docs.cloud.google.com/compute/docs/images/os-details#suse_linux_enterprise_server_sles) images to Google Cloud.

Feature

**Generally available** : NVIDIA® T4 GPUs are now available in the following region and zones:

  * Warsaw, Poland, Europe: `europe-central2-b,c`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

Change

Regional metrics for Compute Engine API limits are now available. Regional migration of API limits reduces the scope of global or multi-regional outages. For more information about the new regional metrics and changes in API limits, see [API rate limits](https://docs.cloud.google.com/compute/resource-usage#api-rate-limits-regional).

Due to this change, you might want to update your Cloud Monitoring dashboards, queries and alerts to use the regional metrics. For more information, see [Migrate Compute Engine API quota from global metrics to regional metrics](https://docs.cloud.google.com/compute/docs/api/how-tos/migrate-to-regional-api).

## February 20, 2023

Feature

**Preview** : You can autoscale a regional managed instance group with a BALANCED target distribution shape. With the BALANCED shape, the autoscaler is aware of the capacity in each zone and creates VMs in zones that have resource availability. For more information, see [Autoscaling a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#autoscaling_a_regional_mig).

## February 16, 2023

Feature

**Preview** : C3 VMs are now available in the following regions:

  * Council Bluffs, Iowa, North America : `us-central1`
  * Ashburn, Virginia, North America: `us-east4`
  * Eemshaven, Netherlands, Europe : `europe-west4`



Feature

**Preview** : You can now use a GPU-enabled Ops Agent to track GPU utilization and GPU memory usage rates for Linux virtual machine instances that have attached GPUs. 

Through an available integration with NVIDIA's Data Center GPU Manager (DCGM), you can also track metrics such as Streaming Multiprocessor (SM) block utilization, SM occupancy, SM pipe utilization, PCIe traffic rate, and NVLink traffic rate. 

For more information, see [Monitoring GPU performance on Linux VMs](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus#overview).

## February 14, 2023

Change

[Tau T2A VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) now support [secure boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).

## February 09, 2023

Feature

**Preview** : You can modify the description, schedule frequency, or labels for a snapshot schedule instead of creating a new snapshot schedule. For more information, see [Change a snapshot schedule](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots#change_snapshot_schedule).

## January 31, 2023

Feature

**Generally available** : You can now use an instance template to define the properties of a reservation and the VMs that can consume the reservation in the same place. Learn how to create a reservation by [specifying an instance template](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-instance-template).

## January 25, 2023

Feature

**Generally available:** Compute Engine committed use discounts are available for Red Hat Enterprise Linux (RHEL) image licenses. Learn more about [discounted RHEL image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) and [how to purchase a license commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchaselicensecommitment).

## January 20, 2023

Change

You can now use the **Observability** tab on the Compute Engine **VM instances** page to see the five virtual machines consuming the most of a resource. For more information, see [Troubleshooting VM performance issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#viewing-performance-metrics).

## January 16, 2023

Feature

**Preview** : When a managed instance group (MIG) repairs a failed or an unhealthy VM, you can apply the latest instance template and per-instance configuration to recreate the VM instead of applying the configuration originally used to create the VM. For more information, see [Apply configuration updates during repairs](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair).

## January 12, 2023

Feature

**Preview** : You can now simulate host maintenance events on sole-tenant nodes.

For more information, see [Simulate host maintenance events on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#simulate_a_host_maintenance_event).

## January 09, 2023

Feature

**Preview:** Use the Google Cloud console to rename VMs. For more information, see [Rename a VM](https://docs.cloud.google.com/compute/docs/instances/rename-instance).

## December 22, 2022

Feature

**Generally available:** N2 VMs with 64 or more vCPUs now support up to 4 GB/s (read) and 3 GB/s (write) throughput per instance with Extreme persistent disks (pd-extreme). Previously the maximum was 2.2 GB/s per instance.

## December 16, 2022

Feature

The image import tool now supports importing [RHEL 9](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel) images to Google Cloud.

## December 13, 2022

Feature

**Generally available** : NVIDIA® T4 GPUs are now available in the following region and zones:

  * Hong Kong, APAC: `asia-east2-a,c`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## December 08, 2022

Feature

**Generally available:** You can merge your active hardware resource commitments into one larger commitment to track and manage them as a single entity. You can now also merge your commitments by using the Google Cloud Console. For more information, see [Merging commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments#merging).

## November 17, 2022

Feature

**Preview:** You can limit the runtime of a VM to automatically stop or delete it when a time limit is reached. Limiting VM runtimes can help you optimize temporary workloads by minimizing costs and releasing quota. For more information, see [Limit the runtime of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime).

## November 16, 2022

Feature

**Generally available** : You can double the default size limit for a managed instance group (MIG): Zonal MIGs support up to 2,000 VMs and regional MIGs support up to 4,000 VMs. For more information, see [Increase the group's size limit](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit).

## November 15, 2022

Feature

**Preview** : Use the new [distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) ANY SINGLE ZONE in a regional managed instance group (MIG) to automatically select a single zone that has available resources within your quota. Recommended for workloads that require low latency, high-bandwidth connections between VMs or when you want to avoid inter-zone network traffic costs.

## November 14, 2022

Change

Balanced persistent disks and SSD persistent disks now offer baseline IOPS and throughput performance. To learn more, see [Baseline performance](https://docs.cloud.google.com/compute/docs/disks/performance#baseline_performance).

## November 10, 2022

Feature

**Generally available:** Share sole-tenant node groups with other projects or with your entire organization. For more information, see [Share sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups).

Change

Per VM Tier_1 networking performance now includes up to 25 Gbps egress for traffic going to public IP addresses (increased from 7 Gbps).

## November 08, 2022

Issue

The quota limits displayed in the Cloud console might be incorrect in the `asia-south1` region. For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#quota-asia-south1).

## November 07, 2022

Feature

**Generally available** : [Memory-optimized M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types) virtual machine instances are available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Frankfurt, Germany (europe-west3-a,b)
  * Eemshaven, Netherlands (europe-west4-a,b)
  * Council Bluffs, Iowa, USA (us-central1-a,b)
  * Las Vegas, Nevada, USA (us-west4-a,b)



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#memory-optimized) for details.

## November 01, 2022

Feature

The image import tool now supports importing [Ubuntu 22.04 LTS](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_lts) and [Windows 11](https://docs.cloud.google.com/compute/docs/images/os-details#windows_client) images to Google Cloud.

## October 27, 2022

Feature

**Generally available:** Compute Engine flexible committed use discounts (flexible CUDs) are spend-based discounts that add flexibility to your spending capabilities by eliminating the need to restrict your commitments to a single project, region, or machine series. You can purchase flexible commitments and commit to a minimum hourly spend amount to use vCPUs and/or memory in any of the projects within your Cloud Billing account, across any region, and belonging to any eligible general-purpose and/or compute-optimized machine types.

Learn more about [flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) and [how to purchase flexible commitments](https://docs.cloud.google.com/docs/cuds-spend-based#purchasing).

## October 19, 2022

Feature

**Generally available:** You can resize an existing hardware resource commitment and split it into smaller commitments to closely monitor and manage portions of one large commitment in the form of smaller individual commitments. You can now also split your commitments by using the Google Cloud Console. For more information, see [Splitting commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments#splitting).

Feature

**Generally available** : [Accelerator-optimized (A2 ultraGPU)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) machine types with their attached [A100 80GB GPUs](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) are now available in the following regions and zones:

  * Iowa, North America: `us-central1-c`
  * Ashburn, Virginia, North America: `us-east4-c`



Fixed

The incorrect quota limits displayed in the Cloud console in the `me-west1` region have been resolved.

## October 05, 2022

Feature

**Generally available:** [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines), Google Cloud's first general purpose VM family to run on Arm architecture, is now generally available in [these three regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).

For more information, including how to try T2A for free for a limited time, see [Creating an Arm VM instance](https://docs.cloud.google.com/compute/docs/instances/create-arm-vm-instance).

## September 23, 2022

Feature

**Generally available** : View the VM placement topology information to determine how close a VM is located in relation to another VM. For more information, see [View VM placement topology](https://docs.cloud.google.com/compute/docs/instances/define-instance-placement#topology).

## September 22, 2022

Feature

**Generally available:** Reduce licensing costs by [customizing the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores).

## September 21, 2022

Feature

**Generally Available** : [E2 shared-core custom VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) are now generally available. See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## September 20, 2022

Issue

The quota limits displayed in the Cloud console might be incorrect in the me-west1 region. For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#quota-me-west1).

## September 16, 2022

Feature

**Generally available** : A new machine type for the memory-optimized-machine family called `m2-hypermem-416` with 416 vCPUs and 8832 GB of memory. This new machine type is now generally available in the same regions as the other M2 machine types. 

For more information, see [Memory-optimized-machine family](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types).

## September 13, 2022

Feature

**Generally available** : NVIDIA® T4 GPUs are now available in the following region and zones in Middle East:

  * Tel Aviv, Israel: `me-west1-b,c`.



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

Feature

**Generally available** : Tel Aviv, Israel, Middle East `me-west1-a,b,c` has launched with E2 and N2 VMs available in all three zones, and M1 VMs in zones a and c.

See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## September 09, 2022

Feature

**Generally available:** Compute Engine supports importing a virtual disk with an UEFI bootloader. Learn more about using the [`--guest-os-features` flag to enable UEFI booting for the imported disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks#import_a_virtual_disk_with_uefi_bootloader).

## September 08, 2022

Fixed

The incorrect quota limits displayed in the Cloud console in the `us-east5` region have been resolved.

## September 07, 2022

Feature

**Generally available:** Archive snapshots are now available for more cost-efficient data retention as compared to regular snapshots, which are best suited for long-term back up and disaster recovery. For more information, see [Archive snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots#archive).

Feature

**Generally available:** To reduce image licensing cost, you can now bring your Red Hat Enterprise Linux subscriptions to Google Cloud. For more information, see [Create a VM using a RHEL BYOS image](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm).

Feature

**Preview** : [Accelerator-optimized (A2 ultraGPU)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) machine types with their attached [A100 80GB GPUs](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) are now available in the following region:

  * Iowa, North America: `us-central1-c`



## September 01, 2022

Change

The following changes have been introduced to how your resource usage is calculated to determine applicable sustained use discounts:

  * Usage will be calculated on an hourly basis instead of a per microsecond basis.
  * Usage will be calculated collectively for a billing account instead of on a per project basis.



## August 25, 2022

Feature

**Preview:** You can double the default size limit for a managed instance group (MIG): Zonal MIGs now support up to 2,000 VMs and regional MIGs support up to 4,000 VMs. For more information, see [Increase the group's size limit](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit)

## August 08, 2022

Feature

**Generally Available** : Internal and external IPv6 addresses for Google Compute Engine instances are available in all regions.

For more information, see [Configuring IPv6 for instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address) and [Creating instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).

## August 05, 2022

Feature

**Generally available** : You can now use the `os-config troubleshoot command` to help verify the setup of VM Manager. For more information, see [Verifying VM Manager setup](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-manager/verify-setup).

## August 04, 2022

Feature

**Generally available** : NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * Ashburn, Virginia, North America: `us-east4-a`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## July 29, 2022

Issue

The quota limits displayed in the Cloud console might be incorrect in the `us-east5` region. For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#quota).

Feature

**Generally available** : When you autoscale a MIG, you can view the reasons for why the autoscaler adds or removes VMs in your MIG. For more information, see [Viewing autoscaler logs](https://docs.cloud.google.com/compute/docs/autoscaler/viewing-autoscaler-logs).

## July 28, 2022

Feature

**Preview:** You can now merge or split your existing hardware resource commitments to create new upsized or downsized commitments. For more information, see [Merge and split commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments).

Feature

**Generally available:** Use the Cloud console, the gcloud tool, or the API to configure a VM to shut down when a Cloud KMS key is revoked. For more information, see [Configure VM shutdown on Cloud KMS key revocation](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#vm-shutdown).

Feature

**Generally available:** When you [create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk), you can now use the following new values with the `TARGET_SHAPE` flag:

  * `ANY`: Use this value to place VMs in zones to maximize unused zonal reservations.
  * `BALANCED`: Use this value to place VMs uniformly across zones.



## July 21, 2022

Feature

**Generally available:** Compute Engine committed use discounts are now Generally Available for SUSE Linux Enterprise Server (SLES) image licenses. Learn more about [discounted SLES image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#suse_sles_images) and [how to purchase a license commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchaselicensecommitment).

## July 20, 2022

Feature

**Generally available** : NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * Montréal, Québec, North America : `northamerica-northeast1-c`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## July 16, 2022

Feature

**Generally available:** Internal and external IPv6 addresses for Google Compute Engine instances are available in all regions.

For more information, see [Configuring IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#template-ipv6) and [Creating instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).

## July 14, 2022

Feature

**Generally available** : You can use the Cloud console to configure autoscaling based on unacknowledged messages in a Pub/Sub subscription. For more information, see [Autoscale based on unacknowledged messages in Pub/Sub](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics#scale_based_on_pubsub).

Feature

**Generally available** : NVIDIA® T4 GPUs are now available in the following additional regions and zones:

Ashburn, Virginia, North America : `us-east4-c`

For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## July 13, 2022

Feature

**Preview:** [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines), Google Cloud's first general purpose VM family to run on Arm architecture, is now available. Tau T2A VMs are available in three [regions](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

For more information, see [Arm VMs on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).

Feature

**Generally Available:** A version of Rocky Linux is now available that is optimized for running on Compute Engine. 

This version of Rocky Linux is configured to use the latest version of the Google virtual network interface (gVNIC) which is specifically designed to support workloads that require higher network bandwidths. For more information, see the _Rocky Linux_ section of the [Operating systems details documentation](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux).

## June 30, 2022

Feature

**Generally available:** You can now create shared reservations of Compute Engine zonal resources using the Google Cloud Console. Learn about [shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) and [creating a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared).

## June 27, 2022

Feature

**GA:** You can now use the SSH troubleshooting tool from the Cloud console to help you determine the cause of failed SSH connections. For more information, see [SSH troubleshooting tool](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh#ssh_troubleshooting_tool).

## June 22, 2022

Issue

The CPU utilization observability metric is incorrect for VMs that use one thread per core. For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#cpu).

## June 16, 2022

Feature

**Preview:** Windows VMs now support SSH connections from the gcloud CLI. For more information, see [Connect to Windows VMs using SSH](https://docs.cloud.google.com/compute/docs/connect/windows-ssh).

## June 15, 2022

Issue

Cloud console SSH-in-browser connections might fail if you use custom firewall rules. For workarounds, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues).

## June 14, 2022

Feature

**Generally available:** Optimize the distribution of VMs in sole-tenant node groups. For more information, see [About manual live migration](https://docs.cloud.google.com/compute/docs/nodes/about-manual-live-migration).

Feature

**Generally Available** : The image import tool now supports importing [Windows Server 2022](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) images to Google Cloud.

## June 13, 2022

Feature

**Generally Available** : Compute Engine can now use a maximum network packet size of `8896` when communicating between VMs on the same subnet. For details, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).

## June 07, 2022

Feature

**Generally available** : Dallas, Texas `us-south1-a,b,c` has launched with [E2 and N2 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) available in all three zones.

See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## June 06, 2022

Feature

**Generally available** : NVIDIA A100 GPUs are now available in the following additional regions and zones:

Las Vegas, Nevada, North America : `us-west4-b`

For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

Feature

**Preview:** When you [create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk), you can now use the following new values with the `TARGET_SHAPE` flag:

  * `ANY`: Use this value to place VMs in zones to maximize unused zonal reservations.
  * `BALANCED`: Use this value to place VMs uniformly across zones.



## May 31, 2022

Feature

**Generally available** : NVIDIA A100 GPUs are now available in the following additional regions and zones:

Seoul, South Korea, APAC : `asia-northeast3-a,b`

For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## May 27, 2022

Feature

**Preview:** You can now use the [SSH troubleshooting tool](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh#ssh_troubleshooting_tool) from the Cloud console to help you determine the cause of failed SSH connections.

## May 24, 2022

Feature

**Generally available** : Columbus, Ohio, USA `us-east5-a,b,c` has launched with [E2, N2, and N2D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) in all three zones. Additionally, you can create [C2 VMs](https://docs.cloud.google.com/compute/docs/compute-optimized-machines) in zones **a** and **b**.

See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## May 18, 2022

Feature

[N2D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) are now available in Paris, France `europe-west9-a,b,c`. 

See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## May 17, 2022

Feature

**Generally available** : You can access Google APIs and services from Compute Engine instances using either internal IPv6 addresses with [Private Google access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) or [external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip).

## May 10, 2022

Feature

**Generally available** : Madrid, Spain `europe-southwest1-a,b,c` has launched with [E2 and N2 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) available in all three zones.

See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## May 09, 2022

Feature

**Generally available** : Insights for idle VM and machine size recommendations help you assess the utilization of your Compute Engine resources. Insights are automatically generated based on system metrics or metrics gathered by the Cloud Monitoring service.

Learn more about [VM insights](https://docs.cloud.google.com/compute/docs/instances/view-and-understand-vm-insights) and [MIG insights](https://docs.cloud.google.com/compute/docs/instance-groups/view-and-understand-mig-insights).

## May 03, 2022

Feature

**Generally available** : Paris, France `europe-west9-a,b,c` has launched with general-purpose [E2 and N2 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) available in all three zones.

See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## April 29, 2022

Feature

**Generally available:** Spot VMs are available for all machine types, regions, and zones. Use Spot VMs for workloads that can withstand preemption to receive large discounts. Spot VMs provide discounts of 60-91% off the on-demand price for standard VMs for machine types and GPUs and also provide smaller discounts for local SSDs. Spot prices can change up to once a month to reflect the underlying supply and demand.

Spot VMs are the latest version of preemptible VM instances. Although new and existing preemptible VMs continue to be supported and use the same prices as Spot VMs, Spot VMs provide new features that are not supported for preemptible VMs. For example, preemptible VMs can only run for up to 24 hours at a time, but Spot VMs have no maximum runtime.

Learn more about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) and [preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible).

## April 21, 2022

Fixed

NVIDIA 510 driver is now supported for GPUs running on Compute Engine. For information about installing drivers, see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).

## April 20, 2022

Feature

**Generally available** : Milan, Italy `europe-west8-a,b,c` region has launched with general-purpose [E2, N2, and N2D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) available in all three zones.

See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## April 18, 2022

Feature

**Preview:** You can now [customize the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores).

## April 14, 2022

Feature

**Generally available** : NVIDIA A100 GPUs are now available in the following additional regions and zones:

  * Tokyo, Japan, APAC: `asia-northeast1-a,c`



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus). For pricing information, review the pricing tables for the [Accelerator-optimized machine type family](https://docs.cloud.google.com/compute/vm-instance-pricing#accelerator-optimized).

## April 13, 2022

Feature

[Tau T2D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) are now available in the following regions and zones:

  * Las Vegas, NV `(us-west4-a,b)`
  * São Paulo, Brazil, South America `(southamerica-east1-a,b,c)`
  * St. Ghislain, Belgium `(europe-west1-c)`



[N2 general-purpose VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machines) are available in Salt Lake City, UT `(us-west3-a,b,c)`.

See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## April 07, 2022

Feature

**Generally available** : You can now [set the number of threads per core on a VM](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

## April 04, 2022

Feature

**Generally available** : You can now autoscale both regional and zonal managed instance groups based on a Cloud Monitoring metric that provides an aggregated value for the group. You can also apply filters to group metrics to further scope the scaling signal. For more information, see [Scaling based on Cloud Monitoring metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics).

## March 22, 2022

Feature

[General purpose Tau T2D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) have [limited availability](https://docs.cloud.google.com/compute/docs/regions-zones#available) in London (europe-west2-a,c). If you are interested in trying out T2D, speak to your Google Cloud Account Team. For pricing details, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family).

Feature

**Preview** : You can now [share sole-tenant node groups with other projects or your entire organization](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups).

## March 16, 2022

Feature

[General-purpose Tau T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) virtual machine instances are available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Northern Virginia (us-east4-a,b,c)
  * South Carolina (us-east1-b,c,d)
  * Frankfurt (europe-west3-a,b,c)
  * Sydney (australia-southeast1-a,b,c)
  * Taiwan (asia-east1-a,b,c)



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## March 14, 2022

Feature

**Generally available** : Compute Engine now supports [Suspend and Resume](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) in General Availability.

Fixed

Fixed the [issue](https://docs.cloud.google.com/compute/docs/release-notes#February_03_2022) causing the [Compute Engine API Quotas page](https://console.cloud.google.com/apis/api/compute.googleapis.com/quotas) in the Cloud Console to display duplicate API quota groups.

## March 07, 2022

Feature

**Generally available** : NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * Council Bluffs, Iowa, North America : `us-central1-c`
  * Eemshaven, Netherlands, Europe : `europe-west4-a`



For more information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## March 04, 2022

Feature

**Public Preview** : You can set the maximum amount of time that Compute Engine waits before terminating or restarting an unresponsive VM. For more information, see [Set VM availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).

## February 23, 2022

Issue

NVIDIA 510 driver not yet supported for GPUs running on Compute Engine, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#nvidia-510).

## February 16, 2022

Change

New documentation for [licenses](https://docs.cloud.google.com/compute/docs/licenses/about) and [appending licenses](https://docs.cloud.google.com/compute/docs/licenses/view-append).

Change

[T2D machines](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones):

  * St. Ghislain, Belgium: `europe-west1`
  * The Dalles, Oregon: `us-west1`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## February 10, 2022

Feature

**Generally available** : Compute-optimized C2D machine types are now generally available. C2D machine types are built on top of third generation AMD EPYC Milan processors and are a great fit for high-performance computing (HPC) workloads. For more information, see [Compute-optimized machine family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines).

## February 09, 2022

Feature

**Public Preview** : You can now use the security keys registered for 2-Step Verification in your Google account to connect to VMs that use OS Login. For more information, see [Enable security keys with OS Login](https://docs.cloud.google.com/compute/docs/oslogin/security-keys).

## February 04, 2022

Feature

**Generally available** : The `n2-node-128-864` [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types).

Feature

**Generally available** : Support for the Intel [Ice Lake processor](https://docs.cloud.google.com/compute/docs/cpu-platforms) on general purpose [N2 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machines) has reached general availability.

## February 03, 2022

Change

Rate limits for all Compute Engine requests have the following changes:

  * All per-user rate limits are removed.
  * Rate limits are now enforced in 1-minute (60-second) intervals instead of 100-second intervals.
  * Due to this change, [you might receive more 403 `rateLimitExceeded` errors when bursting](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#possible_increase_in_403_ratelimitexceeded_errors). 
    * Although per-second rate limits increased slightly, the enforcement intervals are now shorter, so the maximum number of requests per enforcement interval is slightly reduced overall. For example, the default **Queries** group's rate limit is changing from 20 requests per second with a maximum of 2000 requests per 100 seconds to 25 requests per second with a maximum of 1500 requests per 60 seconds.



Additionally, rate limits are now documented for the following groups: 

  * **Instance list referrer requests**
  * **Instance get serial port output requests**



For details, see [API rate limits](https://docs.cloud.google.com/compute/docs/api-rate-limits).

Issue

Duplicate API quota groups are displayed in the Cloud Console. For more information about requesting API quota, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#duplicate_api_quota_groups).

## February 01, 2022

Deprecated

As of February 1, 2022, all CentOS 8 images are deprecated. CentOS 8 reached EOL on December 31, 2021. If you use CentOS 8 images in your project, review [CentOS 8 end of life](https://docs.cloud.google.com/compute/docs/eol/centos8).

## January 31, 2022

Change

Restructured documentation to better group content and improve discoverability.

## January 26, 2022

Feature

**Generally available** : Support for up to 48 vCPUs and 312 GB memory on virtual machine (VM) instances that have a single T4 GPU attached is now generally available.

For more information, see [Network bandwidths and GPUs](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#t4_vm_configuration).

## January 20, 2022

Change

Learn about the differences between multi-tenancy and sole-tenancy by reading the new [About VM tenancy](https://docs.cloud.google.com/compute/docs/instances/about-vm-tenancy) document.

## January 19, 2022

Feature

**Generally available** : You can now use the [SSH troubleshooting tool](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh#ssh_troubleshooting_tool) to help you determine the cause of failed SSH connections.

Feature

**Generally Available** : Configure commitments to renew automatically. For more information, see [Renew commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).

## January 14, 2022

Change

**Generally available:** Access the Compute Engine API using Cloud Client Libraries built on our latest client library model. Updated client libraries are now available in the following languages:

  * Go
  * Java
  * .NET
  * Node.js
  * PHP
  * Python
  * Ruby



For more information, see [Compute Engine client libraries](https://docs.cloud.google.com/compute/docs/api/libraries).

## January 11, 2022

Feature

**Generally available** : Compute Engine now supports [machine images](https://docs.cloud.google.com/compute/docs/machine-images) in General Availability. You can use machine images to store configuration, metadata, permission, and data required to create a VM instance.

## January 05, 2022

Feature

**Preview** : You can now [disable VM instance creation retries during resizing](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#disabling_creation_retries_mode_during_resize) of both regional and zonal managed instance groups.

## December 16, 2021

Issue

Accelerator-optimized (A2) machine types with gVNIC are currently experiencing a [known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues).

Feature

**Preview** : Compute-optimized C2D machine types are now available in preview. C2D machine types are built on top of third generation AMD EPYC Milan processors and are a great fit for high-performance computing (HPC) workloads. For more information, see [Compute-optimized machine family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines).

## December 15, 2021

Feature

**Generally available** : When rolling out configuration or application updates to a stateful or stateless managed instance group, use the minimum and most disruptive allowed actions to [control disruption](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#controlling_the_disruption_level_during_a_rolling_update) to your workload.

Feature

**Public preview** : You can use the gcloud tool or API to [configure stateful IP addresses in a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs). Stateful IP addresses are preserved when VM instances in the group are autohealed, updated, and recreated.

## December 14, 2021

Feature

**Generally available** : You can now share reservations of Compute Engine zonal resources between multiple projects. Learn about [shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) and [creating a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared).

## December 13, 2021

Change

You can now save copies of all charts from the Observability tab on Compute Engine's **VM instance details** page to one of your custom dashboards. To save copies of the charts, click **Add Charts to Dashboard**. You then select a new or existing custom dashboard as the destination.

## December 10, 2021

Feature

The `n2-node-128-864` [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) is now available in **Preview**.

## December 03, 2021

Feature

**Generally available:** Use OS configuration management to deploy and automate software configurations on your virtual machine (VM) instances using the Google Cloud console, `gcloud` command-line, and OS Config API.

With the OS configuration management GA, you can now edit assignments from the Cloud console and view OS policy assignment reports. For more information, see [OS configuration management](https://docs.cloud.google.com/compute/docs/os-configuration-management).

Feature

**Generally available:** NVIDIA® A100 GPUs are now available in the following additional regions and zones:

  * Moncks Corner, South Carolina : `us-east1-b`
  * The Dalles, Oregon : `us-west1-b`
  * Council Bluffs, Iowa : `us-central1-f`
  * Jurong West, Singapore : `asia-southeast1-b`



For more information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## November 16, 2021

Feature

**Generally available** : Santiago, Chile, South America `southamerica-west1-a,b,c` region has launched with [E2, N2, and C2 VMs](https://docs.cloud.google.com/compute/docs/machine-types) in all three zones. See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

Feature

**Generally available** : You can now configure [N2, N2D, and C2 VMs](https://docs.cloud.google.com/compute/docs/machine-types) with up to 100 Gbps of network bandwidth.

This feature is ideal for network-intensive, distributed workloads such as high-performance computing (HPC), machine learning (ML), and deep learning (DL).

Learn more about [high-bandwidth network configurations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration), and the [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) where these VMs are available.

## November 15, 2021

Feature

**Generally available** : [T2D Tau machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) are available in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). Tau T2D VMs offer excellent price-performance for a wide range of scale-out workloads. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

Feature

**Generally available** : [N2D machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) running on third generation [AMD EPYC Milan processors](https://docs.cloud.google.com/compute/docs/cpu-platforms#amd_cpu_processors). These machine types are only available in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

Feature

**Generally available** : You can now [monitor health state change logs](https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes) for VM instances in a managed instance group when you use application-based health checking.

## November 12, 2021

Change

You can now access vulnerability report data, available through the OS Config API service, from [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview). For more information, see [View vulnerability reports data from Cloud Asset Inventory](https://docs.cloud.google.com/compute/docs/instances/view-os-details#cai-integration-vuln-reports).

## November 11, 2021

Feature

**Generally available** : You can now use the `gcloud` command-line and the OS Config API to get inventory and vulnerability report data for your VMs in a specific zone. For more information, see [Viewing operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).

## November 09, 2021

Change

If you use local SSDs with sync-heavy workloads, you will now more consistently reach [write IOPS limits](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance) and experience lower latency, without having to disable [cache flushing](https://en.wikipedia.org/wiki/Disk_buffer#Cache_flushing). This is due to a recent SSD firmware update.

## November 08, 2021

Feature

You can now save a copy of a chart from the Observability tab on Compute Engine's **VM instance details** page to one of your custom dashboards. To save a copy of the chart, select **Add to Custom Dashboard** from chart option. You then select a new or existing custom dashboard, and have the option of renaming the new copy of the chart.

## October 28, 2021

Feature

**Generally available** : [Schedule-based autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules) for managed instance groups now lets you configure schedules without having another autoscaling signal.

## October 21, 2021

Feature

**Preview** : You can now configure up to 48 vCPUs and 312 GB memory on virtual machine (VM) instances that have a single T4 GPU attached.

For more information, see [Network bandwidths and GPUs](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#t4_vm_configuration).

## October 13, 2021

Feature

**Preview** : Spot VMs are now available! Spot VMs are the latest version of preemptible VM instances. Use Spot VMs for fault-tolerant workloads to get a 60-91% discount over the price of standard VMs. Spot prices can change up to once a month to reflect the underlying supply and demand. Like preemptible VMs, Spot VMs are available for all machine types, regions, and zones. 

Preemptible VMs continue to be supported for new and existing VMs, and preemptible VMs now use the same pricing model as Spot VMs. However, Spot VMs provide new features that are not supported for preemptible VMs. For example, preemptible VMs can only run for up to 24 hours at a time, but Spot VMs do not have a maximum runtime. 

Learn more about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) and [preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible).

## October 12, 2021

Feature

**Preview:** Third generation Intel Xeon Scalable Processor (Ice Lake) [N2 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machines) are now available in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). These new N2 VMs are offered at the [same price](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) as existing N2 VMs on second generation Intel Xeon Scalable Processors.

## October 11, 2021

Feature

**Preview:** [Tau T2D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) are now available in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). T2D VMs are ideal for a wide variety of workloads in a cloud-native environment. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## September 23, 2021

Feature

**Generally Available** : Use patch alerting to monitor the patch jobs running in your environment. For more information, see [Monitoring patch jobs](https://docs.cloud.google.com/compute/docs/os-patch-management/monitor-patch-jobs).

## September 22, 2021

Feature

**Preview** : You can now access installer properties for your Windows applications by using OS inventory management. For more information, see [OS inventory management](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management#installed-packages).

For information on setting up and using OS inventory management, see [Viewing operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).

## September 13, 2021

Feature

**Generally Available** : NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * Las Vegas, Nevada,: `us-west4-a,b`
  * Los Angeles, California: `us-west2-b,c`



For more information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## September 08, 2021

Feature

**Preview** : You can now review OS vulnerability report data, which is collected by VM Manager, from the Security Command Center. This feature is available for Security Command Center premium tier users. For more information, see [View vulnerability report data](https://docs.cloud.google.com/compute/docs/instances/view-os-details#view-report).

## September 01, 2021

Feature

**Generally available** : When [deleting VMs from a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#deleting_specific_instances), you can flag the operation to continue even if some instances were already deleted or if other instance validation errors occur.

## August 31, 2021

Feature

**Generally available:** You can now [reference the latest available image in a public image family for a specific zone](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#per_zone). This feature improves zonal fault tolerance for your workflows during Google image updates.

## August 25, 2021

Feature

**Generally available** : You can now collect core dumps for uses such as debugging of unresponsive VMs. For more information, see [Collecting core dumps](https://docs.cloud.google.com/compute/docs/troubleshooting/collecting-core-dumps).

## August 16, 2021

Feature

**Preview** : Manually live migrate VMs from one host to another. For more information, see [Manually live migrate sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate).

## August 06, 2021

Feature

**Preview** : You can now use the Slurm-Google Cloud workload manager to create clusters that are based on the [HPC virtual machine (VM) image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm) and comply to the [Intel Select Solution for Simulation and Modeling criteria](https://www.intel.com/content/www/us/en/products/solutions/select-solutions/hpc/simulation-modeling.html). For more information, see [Creating Intel Select Solution HPC clusters](https://docs.cloud.google.com/compute/docs/instances/create-intel-select-solution-hpc-clusters).

Change

**Generally available** : The Observability tab on Compute Engine's **VM instance details** page includes a category for [process metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-processes). You can use the new charts and reports to troubleshoot the behavior of processes running on your VMs.

## August 05, 2021

Change

[N2 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machines) are now available in all three zones in Warsaw, Poland `europe-central2-a,b,c`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## August 03, 2021

Feature

Disks, snapshots, and images are available in Toronto, Ontario, Canada `northamerica-northeast2` in all three zones. See [Disks and image pricing](https://cloud.google.com/compute/disks-image-pricing) for details.

Feature

Toronto, Ontario, Canada `northamerica-northeast2-a,b,c` region has launched with E2, N2, N1 [virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/machine-types) in all three zones. See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

Feature

**Generally available** : You can update the descriptions of your managed instance groups by using the API or [gcloud tool](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/update).

## August 02, 2021

Feature

**Preview:** You can now share reservations of Compute Engine zonal resources between multiple projects. Learn about [shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) and [creating a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared).

## July 22, 2021

Feature

**Preview** : You can use the Help Assistant in the Google Cloud Console to find answers to questions about Compute Engine.

## July 13, 2021

Feature

**Preview** : The Observability tab on Compute Engine's **VM instance details** page includes a new category for [process metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-processes). You can use the new charts and reports to troubleshoot the behavior of processes running on your VMs.

Feature

**Preview:** Access the Compute Engine API using Cloud Client Libraries built on our latest client library model. An updated client library is now available in the following language:

  * Go



For more information, see [Compute Engine client libraries](https://docs.cloud.google.com/compute/docs/api/libraries#google_cloud_client_libraries).

## July 01, 2021

Feature

**Preview** : You can now configure [N2D VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) with up to 100 Gbps of network bandwidth.

This feature is ideal for network-intensive distributed workloads.

Learn more about [higher bandwidth configurations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration), the [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) where these machines are available, and the [post preview pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing) for this new feature.

## June 30, 2021

Change

The Machine types documentation has been renamed to [Machine families](https://docs.cloud.google.com/compute/docs/machine-types). The URL remains the same.

New pages have been added to reflect the expansion of our machine fleet. 

  * [General-purpose family](https://docs.cloud.google.com/compute/docs/general-purpose-machines)
  * [Compute-optimized family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines)
  * [Memory-optimized family](https://docs.cloud.google.com/compute/docs/memory-optimized-machines)
  * [Accelerator-optimized family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines)



You can learn about Virtio memory balloon devices at the [Dynamic resource management](https://docs.cloud.google.com/compute/docs/dynamic-resource-management) page.

## June 29, 2021

Feature

**Preview** : You can now autoscale both regional and zonal managed instance groups based on a Cloud Monitoring metric that provides an aggregated value for the group. You can also apply filters to group metrics to further scope the scaling signal. For more information, see [Scaling based on Cloud Monitoring metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#per_group_metrics).

Feature

Delhi, India `asia-south2-a,b,c` region has launched with [E2, N2, N1, and C2](https://docs.cloud.google.com/compute/docs/machine-types) virtual machine (VM) instances in all three [zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) for details.

## June 28, 2021

Feature

[General-purpose N2D VMs](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in `us-west4-b` Las Vegas, NV. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

Feature

**Generally available** : Compute Engine's **VM instance details** page has a new Observability tab, which replaces the Monitoring tab. The enhanced Observability tab provides access to logs and greater visibility into CPU, disk, and network metrics.

## June 24, 2021

Feature

**Preview:** Use patch alerting to monitor the patch jobs running in your environment. For more information, see [Monitoring patch jobs](https://docs.cloud.google.com/compute/docs/os-patch-management/monitor-patch-jobs).

## June 23, 2021

Feature

[Best practices](https://docs.cloud.google.com/compute/docs/api/best-practices) are now available for the Compute Engine API.

## June 21, 2021

Feature

Melbourne, Australia `australia-southeast2-a,b,c` has launched with [E2, N2, N1, and M1 machines](https://docs.cloud.google.com/compute/docs/machine-types). M1 machines are only available in zones `b` and `c`.

See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for details.

## June 18, 2021

Feature

**Generally available** : You can now create application consistent snapshots of disks attached to Linux VMs. For more information, see [Creating Linux application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots).

## June 17, 2021

Feature

You can now [customize E2 shared-core](https://docs.cloud.google.com/compute/docs/machine-types#e2_shared-core_custom_machine_types) machine types. Shared-core machine types provide a fractional vCPU with the ability to burst to 2 vCPU for a short period of time.

  * E2 shared-core machine types support predefined platforms with Intel or AMD EPYC Rome processors.

  * The custom memory range is:

    * 1 to 2 GB for micro machines
    * 1 to 4 GB for small machines
    * 1 to 8 GB for medium machines



E2 shared-core custom machine pricing is the same as [E2 custom machine pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#e2_sharedcore_machine_types). E2 machines are available in all [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

[Create a custom E2 shared-core machine using `gcloud` or the API](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#gcloud).

Feature

[Memory-optimized M2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family) are now available in Belgium, `europe-west1-b,c`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#memory-optimized) for details.

## June 10, 2021

Feature

NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * St. Ghislain, Belgium: `europe-west1-b,c,d`



For more information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## June 08, 2021

Feature

**Preview** : When rolling out configuration or application updates to a stateful or stateless managed instance group, use the minimum and most disruptive allowed actions to [control disruption](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#controlling_the_disruption_level_during_a_rolling_update) to your workload.

Feature

**Generally available** : You can configure how your regional managed instance group distributes instances across zones by using capacity-aware [distribution shapes](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#setting_a_policy_for_distributing_instances_across_zones), which can automatically deploy instances to zones where capacity is available and optionally prioritize the use of reservations.

## June 03, 2021

Feature

[N2D machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in `us-west4-a` , Las Vegas, Nevada. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

## June 01, 2021

Feature

**Preview:** Access the Compute Engine API using Cloud Client Libraries built on our latest client library model. Updated client libraries are now available in the following languages:

  * Java
  * .NET
  * Node.js
  * PHP
  * Python
  * Ruby



For more information, see [Compute Engine client libraries](https://docs.cloud.google.com/compute/docs/api/libraries#google_cloud_client_libraries).

## May 26, 2021

Feature

**Preview** : Disable simultaneous multithreading (SMT) on VMs. For more information, see [Disabling simultaneous multithreading](https://docs.cloud.google.com/compute/docs/instances/disabling-smt).

## May 25, 2021

Feature

**Generally Available** : Enable nested virtualization directly when creating a VM. For more information, see [Nested virtualization overview](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview).

## May 19, 2021

Feature

**Generally Available** : You can now create VM instances with V100, A100, and T4 GPUs that support network bandwidths of up to 100 Gbps. See [Using network bandwidths of up to 100 Gbps](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus#high-bandwidth).

## May 13, 2021

Feature

**Preview** : You can use OS configuration management to deploy and automate software configurations on your virtual machine (VM) instances using gcloud command-line and OS Config API.

With the release of OS configuration management (preview), you can now rollout policies from the Cloud console, control the rollout pace, use more VM filter options, and view compliance reports. For more information, see [OS configuration management (preview)](https://docs.cloud.google.com/compute/docs/os-configuration-management).

## May 12, 2021

Feature

[N2 machines](https://docs.cloud.google.com/compute/docs/machine-types#n2_machine_types) are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Osaka, Japan: `asia-northeast2-a,b,c`
  * Seoul, South Korea: `asia-northeast3-a,b,c`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_predefined) for details.

## May 10, 2021

Feature

[N2D machines](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in Tokyo `asia-northeast1-c`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

## May 03, 2021

Feature

**Generally available** : Create virtual machines for high performance computing (HPC) workloads using the [HPC VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm).

## April 29, 2021

Feature

You can now create _extreme persistent disks_ in certain regions. With consistently high performance for both random access workloads and bulk throughput, extreme persistent disks are designed for high-end database workloads.

For more information, see [Extreme persistent disks](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk).

Feature

**Preview** : With the introduction of OS inventory management v2.0, you can now query the OS Config API to get inventory and vulnerability report data for your VMs in a specific zone, see [OS inventory management](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management).

## April 28, 2021

Feature

[C2 machines](https://docs.cloud.google.com/compute/docs/machine-types#compute-optimized_machine_type_family) are available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Osaka `asia-northeast2-a`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#compute-optimized_machine_types) for details.

## April 27, 2021

Feature

N2D machines are available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Osaka `asia-northeast2-c`
  * Montréal `northamerica-northeast1-a,c`
  * Finland `europe-north1-a,b,c`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

## April 19, 2021

Feature

[N2 VMs](https://docs.cloud.google.com/compute/docs/machine-types#n2_machine_types) are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Mumbai `asia-south1-a,b`
  * Jakarta `asia-southeast2-a,b,c`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_predefined) for details.

## April 16, 2021

Feature

[N2D machines](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are available in the following regions and zones:

  * Montréal `northamerica-northeast1-b`
  * Osaka `asia-northeast2-a,b`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for pricing details.

## April 15, 2021

Change

You can now see additional metrics for your managed instance groups from the **Instance Groups Monitoring tab**. Metrics include: group size, CPU utilization, disk I/O, and more. Use the time range picker to select the time window for the charts and view the corresponding logs from the integrated logs viewer panel. Follow the links on each chart to create alerts or to analyze the details in the Cloud Operations Metrics Explorer.

## April 13, 2021

Feature

**Generally available** : [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) integration with [VPC Service Control](https://docs.cloud.google.com/vpc-service-controls/docs).

Feature

**Generally available** : You can now configure [schedule-based autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules) for your managed instance groups. Schedule-based autoscaling lets you improve the availability of your application by scheduling capacity ahead of anticipated load.

## April 08, 2021

Feature

**Generally available** : [Predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling) for managed instance groups lets you improve the availability of your workloads by using Machine Learning to predict future demand and create virtual machines ahead of forecasted load.

## April 06, 2021

Feature

**Generally available** : You can now use [instance schedules](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop) from the [Google Cloud Console](https://console.cloud.google.com/compute/instances?tab=instanceSchedules).

Feature

[N2D machines](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones):

  * `us-central1-b` \- Iowa
  * `asia-northeast1-a,b` \- Tokyo



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

## April 01, 2021

Feature

[Memory-optimized machines](https://docs.cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family) are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * `M1 ultramem` (Jakarta ) `asia-southeast2-a,c`
  * `M1 ultramem` (Osaka) `asia-northeast2-a`
  * `M1 ultramem`, `M2 ultramem and M2 megamem` (Osaka) `asia-northeast2-b`
  * `M2 ultramem and M2 megamem` (Osaka) `asia-northeast2-c`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#memory-optimized) for details.

## March 31, 2021

Feature

**Preview** : You can now configure your VM to shutdown automatically when you revoke the Cloud KMS key protecting a persistent disk attached to the VM. For more information, see [Configuring VM shutdown on Cloud KMS key revocation](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#vm-shutdown).

## March 25, 2021

Feature

**Generally available** : Start and stop virtual machine (VM) instances automatically using [instance schedules](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop). By automating the deployment of your VMs, instance schedules can help you optimize costs and manage VMs more efficiently.

## March 24, 2021

Feature

General-purpose [E2 and N1 machines](https://docs.cloud.google.com/compute/docs/machine-types#general_purpose) are available in Warsaw, Poland `europe-central2` in all three zones. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#e2_predefined) for details.

Feature

Disks, snapshots, and images are available in Warsaw, Poland `europe-central2` in all three zones. See [Disks and image pricing](https://cloud.google.com/compute/disks-image-pricing) for details.

Feature

Support for [OS Login](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_os_login) in [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) is now **Generally Available**.

## March 19, 2021

Feature

[N2D machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are available in the following regions and zones:

  * Frankfurt, `europe-west3-a,b`
  * Hong Kong, `asia-east2-b,c`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for pricing details.

## March 17, 2021

Feature

**Generally Available** : Use the bulk instance API to create multiple, homogeneous VMs that are independent from each other. For more information, see [Using the bulk instance API](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api).

Feature

**Preview** : You can now configure N2 and C2 VMs with up to 100 Gbps of network bandwidth. 

This feature is ideal for network-intensive, distributed workloads such as high-performance computing (HPC), machine learning (ML), and deep learning (DL). 

Learn more about [higher bandwidth configurations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration), the [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) where these machines are available, and the [post preview pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing) for this new feature.

Feature

[M2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#m2_machine_types) are now available in the following regions and zones:

  * Sydney — `australia-southeast1-b,c`
  * London — `europe-west2-b,c`
  * Montréal — `northamerica-northeast1-b,c`



See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#larger_ultramem) for details.

## March 16, 2021

Feature

**Generally Available** : [Accelerator-optimized (A2) machine types](https://docs.cloud.google.com/compute/docs/machine-types#accelerator-optimized_machine_type_family) are now available in the following three regions:

  * Iowa, North America: `us-central1-a,b,c`
  * Netherlands, Europe: `europe-west4-a,b`
  * Singapore, APAC: `asia-southeast1-c`



Feature

[N2D machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in Frankfurt, `europe-west3-c` and Hong Kong, `asia-east2-a`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for pricing details.

Feature

[N2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2_machine_types) are now available in Zurich, `europe-west6` in all three zones. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_predefined) for details.

[C2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#c2_machine_types) are now available in Salt Lake City, `us-west3` in all three zones. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#c2_machine_types) for details.

[Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family) are now available in Tokyo, `asia-northeast1` in all zones. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#memory-optimized) for details.

Feature

[C2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#compute-optimized_machine_type_family) are now available in Zürich, `europe-west6` in all three zones. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#compute-optimized_machine_types) for details.

Feature

**Generally Available** : NVIDIA® A100 GPUs are now available in the following three regions:

  * Iowa, North America: `us-central1-a,b,c`
  * Netherlands, Europe: `europe-west4-a,b`
  * Singapore, APAC: `asia-southeast1-c`

For more information, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus).




## March 04, 2021

Change

The VM instance details page for Compute Engine now offers a guided installation path for [Monitoring agents](https://docs.cloud.google.com/monitoring/agent) when they are not detected.

## February 25, 2021

Feature

**Preview** : You can now use the `gcloud` command-line tool to import images from AWS into Google Cloud. For more information, see [Importing images from AWS](https://docs.cloud.google.com/compute/docs/import/import-aws-image).

## February 17, 2021

Feature

**Preview** : [Predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling) for managed instance groups lets you improve the availability of your workloads by using Machine Learning to predict future demand and create virtual machines ahead of forecasted load.

## February 12, 2021

Feature

Google Virtual NIC (gVNIC) driver is now **generally available**. For more information, see [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

## February 02, 2021

Feature

**Generally Available** : Specify when maintenance begins on VMs in a sole-tenant node group. For more information, see [Planned maintenance](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#planned_maintenance).

Feature

**Generally Available** : Sole-tenant nodes now support GPUs and local SSDs. For more information, see [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

## February 01, 2021

Feature

**Preview** : You can now create virtual machines for high performance computing (HPC) workloads using the [HPC VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm).

Feature

NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * Jakarta, Indonesia, APAC: `asia-southeast2-a,b`



For more information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

Feature

N2D machine types are now available in London, zone `europe-west2-c`. For pricing information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types).

Feature

**Preview:** You can now use [schedule-based autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules) from the [Google Cloud Console](https://console.cloud.google.com/).

Feature

You can now create instances with up to 24 local SSD partitions for 9 TB of local SSD space using N1, N2, and N2D machine types. This is **Generally available**. For more information, see [Local SSD 9 TB maximum capacity](https://docs.cloud.google.com/compute/docs/disks/local-ssd#capacity_9tb).

## January 28, 2021

Announcement

Manage your operating system environments by using VM Manager. VM Manager is a suite of services for reviewing, patching, and configuring your operating systems across both Linux and Windows VMs. For more information, see [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager).

## January 22, 2021

Feature

NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * Jurong West, Singapore, APAC: `asia-southeast1-a`



For more information about GPU availability on Compute Engine, see [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

## January 11, 2021

Feature

You can now create N2D VM instances in `us-east4-c` Northern Virginia. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

## December 17, 2020

Feature

The `m1-node-96-1433` [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) is now **Generally Available**.

## December 16, 2020

Feature

Compute-optimized (C2) machines are now available in Montréal, in all three [zones ](https://docs.cloud.google.com/compute/docs/regions-zones#available), `northamerica-northeast1-a,b,c`. For pricing, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#compute-optimized_machine_types).

## December 15, 2020

Feature

**Preview** : [Accelerator-optimized (A2) machine types](https://docs.cloud.google.com/compute/docs/machine-types#accelerator-optimized_machine_type_family) are now available in the following three regions:

  * Iowa, North America: `us-central1-a,c`
  * Netherlands, Europe: `europe-west4-a,b`
  * Singapore, APAC: `asia-southeast1-c`



Feature

**Preview** : NVIDIA® A100 GPUs are now available in the following three regions:

  * Iowa, North America: `us-central1-a,c`
  * Netherlands, Europe: `europe-west4-a,b`
  * Singapore, APAC: `asia-southeast1-c`

For more information, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus).




## December 10, 2020

Feature

You can [migrate a VM instance from one network to another](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks). This feature is **Generally available**.

Feature

**Preview** : You can configure how your regional managed instance group distributes instances across zones by using capacity-aware [distribution shapes](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#setting_a_policy_for_distributing_instances_across_zones), which can automatically deploy instances to zones where capacity is available and optionally prioritize the use of reservations.

## December 09, 2020

Feature

**GA** : You can now access [OS inventory data](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management#data-collected) from [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview). For more information, see [OS inventory and Cloud Asset Inventory integration](https://docs.cloud.google.com/compute/docs/instances/view-os-details#cai-integration).

Feature

**GA** : [Per-group metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#per_group_metrics) let you autoscale a zonal managed instance group based on any Cloud Monitoring metric—for example, a Pub/Sub queue size or custom metrics from your application.

Feature

**Preview** : [Schedule-based autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules) for managed instance groups lets you improve the availability of your workloads by scheduling capacity ahead of anticipated load.

## November 24, 2020

Feature

New [sole-tenant node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types):

  * **GA** :

    * `c2-node-60-240`
    * `m1-node-160-3844`
    * `m2-node-416-11776`
    * `n2-node-80-640`
    * `n2d-node-224-896`
  * **Beta** :

    * `m1-node-96-1433`



## November 20, 2020

Feature

**Preview** : [Reserve GPUs and local SSDs](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms) on [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

Feature

**Preview** : [Rename VM instances](https://docs.cloud.google.com/compute/docs/instances/rename-instance).

## November 17, 2020

Feature

You can now use security keys as a 2-step verification method when connecting to VMs using OS Login. For more information, see [Setting up OS Login with 2-step verification](https://docs.cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication#supported_methods_or_challenge_types).

## November 16, 2020

Feature

**GA** : [Collect diagnostic information from Windows Server VMs](https://docs.cloud.google.com/compute/docs/instances/collecting-diagnostic-information).

Feature

[N2D machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in `us-west1-a`, The Dalles, Oregon. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for pricing details.

## November 12, 2020

Change

The VM instance details page for Compute Engine now displays Memory Utilization and Disk Space Utilization charts. In addition, a new Monitor VM Instances link lets you go directly to the [VM instances dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance) in Cloud Monitoring.

## November 11, 2020

Feature

[Compute-optimized (C2) machine types](https://docs.cloud.google.com/compute/docs/machine-types#compute-optimized_machine_type_family) are now available in Hong Kong, `asia-east2`, in all three [zones](https://docs.cloud.google.com/compute/docs/regions-zones). For pricing information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#compute-optimized_machine_types).

## November 09, 2020

Feature

Identify resources like persistent disks, IP addresses, and custom disk images that aren't in use. [Viewing and applying idle resources recommendations](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations) can help reduce unused resources and reduce your Compute Engine bill. This feature is **Generally available**.

Feature

[Compute-optimized (C2) machine types](https://docs.cloud.google.com/compute/docs/machine-types#compute-optimized_machine_type_family) are now available in Sydney, Australia, `australia-southeast1-c`. For pricing details, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#compute-optimized_machine_types).

## October 29, 2020

Feature

NVIDIA® V100 GPUs are now available in the following additional regions and zones:

  * South Carolina, North America: `us-east1-c`



For information about using V100 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

Feature

You can use [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) in [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_vm_manager). This feature is available in [beta](https://cloud.google.com/products/#product-launch-stages).

## October 26, 2020

Feature

[N2D Machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in Eemshaven, Netherlands, `europe-west4-a`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

Feature

[N2D Machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now available in London, `europe-west2-a,b`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

## October 19, 2020

Feature

[Memory-optimized M1 machine types](https://docs.cloud.google.com/compute/docs/machine-types#m1_machine_types) are available in Frankfurt `europe-west3-a,b,c`. [Memory-optimized M2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#m2_machine_types) are available in Frankfurt, `europe-west3-a,b`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#memory-optimized) for details.

## October 15, 2020

Feature

Support for [1500 MTU in VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#mtu) is now **Generally available**.

## October 14, 2020

Feature

[Compute-optimized (C2) machine types](https://docs.cloud.google.com/compute/docs/machine-types#compute-optimized_machine_type_family) are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Finland: europe-north1-a,b,c
  * Seoul: asia-northeast3-a,b,c



See [VM-instance-pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#compute-optimized_machine_types) for details.

## October 12, 2020

Feature

[N2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2_machine_types) are now available in the following four regions and zones:

  * Las Vegas: us-west4-a,b,c
  * Montréal: northamerica-northeast1-a,b,c
  * Finland: europe-north1-a
  * Hong Kong: asia-east2-a,b,c



For pricing details, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_predefined).

## October 05, 2020

Feature

You can use [OS Login](https://docs.cloud.google.com/compute/docs/oslogin) in [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs). This feature is in [Beta stage support](https://cloud.google.com/products/#product-launch-stages).

## October 02, 2020

Feature

N2D machine types are available in The Dalles, Oregon, in the us-west1-c zone. For more information, see the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) page.

Feature

C2 machine types are now available in Sydney, Australia `australia-southeast1-b`. See the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#c2_machine_types) page for details.

## October 01, 2020

Feature

N2D machine types are now available in all three zones of us-east1-b,c,d in Moncks Corner, South Carolina. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) for details.

## September 28, 2020

Feature

N2D machine types are available in The Dalles, Oregon, the `us-west1-b` zone. For more information, see the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) page.

## September 25, 2020

Change

On [July 28, 2020](https://docs.cloud.google.com/compute/docs/release-notes#July_28_2020), we announced that improved validation checks will be introduced on API calls to the Compute Engine API. This change has been postponed and will be rescheduled for a later time.

## September 22, 2020

Feature

NVIDIA® T4 GPUs are now available in the following additional regions and zones:

  * Sydney, Australia: `australia-southeast1-a`



For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## September 17, 2020

Feature

You can now [migrate a VM instance from one network to another](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks). This feature is available in Beta.

## September 16, 2020

Feature

Troubleshoot VMs by [capturing a screenshot](https://docs.cloud.google.com/compute/docs/instances/capturing-vm-screenshots) from the VM. This is **Generally Available**.

## September 15, 2020

Change

SSD persistent disks attached to certain VMs with at least 64 vCPUs can now reach 100,000 write IOPS. To learn more about the requirements to reach these limits, see [Block storage performance](https://docs.cloud.google.com/compute/docs/disks/performance).

## September 14, 2020

Feature

Compute-optimized (C2) machine types are now available in Sydney, Australia `australia-southeast1-a`. See [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#c2_machine_types) for details.

## September 11, 2020

Feature

You can build highly available deployments of stateful workloads on VM instances using [stateful managed instance groups (stateful MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs). A stateful MIG preserves the unique state of each instance (instance name, attached persistent disks, and/or metadata) on machine restart, recreation, autohealing, or update. Stateful MIGs are Generally available.

## August 24, 2020

Feature

Compute Engine committed use discounts are **Generally Available** for SUSE Linux Enterprise Server for SAP images. Learn more about discounted image pricing at [Committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchasecommitmentSLES).

Feature

You can now protect your [Compute Engine resources](https://docs.cloud.google.com/compute/docs/instances/protecting-resources-vpc-service-controls) using VPC Service Controls. This feature is available in Beta.

## August 20, 2020

Feature

The Organization Policy for [restricting protocol forwarding creation](https://docs.cloud.google.com/compute/docs/protocol-forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization) has launched into general availability.

## August 18, 2020

Feature

N2D machine types are now available in `us-central1-c`. For more information, see the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) page.

Feature

N2D machine types are now available in Northern Virginia `us-east4-a,b`. For more information, see the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) page.

## August 12, 2020

Feature

Key metrics for persistent disks in the new disk-level Monitoring tab are now **Generally Available**. Select any persistent disk attached to a single VM from [Disks](https://console.cloud.google.com/compute/disks) to see mean throughput, peak throughput, mean operations, and peak operations. You can also open each metric in [Monitoring](https://console.cloud.google.com/monitoring) for querying, browsing, adding to a dashboard, or configuring alerts.

Feature

Compute Engine [Committed use discount recommendations](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#recommendations) are available in beta. Committed use recommendations give you opportunities to optimize your compute costs by analyzing your VM spending trends. For additional information, see [Understanding commitment recommendations](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-resource-based#understanding_commitment_recommendations).

Feature

[CPU overcommit on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms) lets you overprovision sole-tenant node resources and schedule more VM CPUs on a sole-tenant node than are normally available. This feature is **Generally Available**.

## August 07, 2020

Feature

You can now update multiple instance properties using a single request from the command-line tool or the Compute Engine API to update multiple instance properties. For more information, see [Updating instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties).

## August 04, 2020

Change

You can attach a maximum of 24 local SSD partitions for 9 TB per instance. This is **generally available** on instances with N1 machine types. For more information, see [Local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds).

## August 03, 2020

Feature

You can now access C2 machine types in the following zones: Taiwan: `asia-east1-a`, Singapore: `asia-southeast1-a`, Sao Paulo: `southamerica-east1-b,c`, and Oregon: `us-west1-b`. For more information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#c2_machine_types).

## July 31, 2020

Feature

N2D machine types are now available in `asia-east1` in all three zones. For more information, see the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) page.

## July 30, 2020

Feature

When creating patch jobs, you can now choose whether to deploy zones concurrently or one at a time. You can also now specify a disruption budget for your VMs. For more information, see [Patch rollout options](https://docs.cloud.google.com/compute/docs/os-patch-management/create-patch-job#rollout-options).

Feature

N2 machines are now available in Sao Paulo `southamerica-southeast1` in all three zones. For more information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_machine_types).

Feature

You can access `m2-megamem` memory-optimized machine types in all zones that already have `m2-ultramem` memory-optimized machine types. These two machine types have also been added to `asia-south1-b`. You can use `m1-ultramem` machine types in `asia-south1-a`. To learn more, read [Memory-optimized machine type family](https://docs.cloud.google.com/compute/vm-instance-pricing#memory-optimized).

## July 28, 2020

Change

Improved validation checks will be introduced on API calls to `compute.googleapis.com` starting on August 3, 2020 to increase reliability and REST API compliance of the Compute Engine platform for all users. Learn how to [Validate API Requests](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#validating_api_requests) to ensure your requests are properly formed.

## July 24, 2020

Feature

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

    * Ashburn, Northern Virginia, USA: `us-east4-b`

For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).




Feature

N2 machines are now available in Northern Virginia `us-east4-c`. Read more information on the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_machine_types) page.

## July 21, 2020

Feature

You can now create _balanced persistent disks_ , in addition to standard and SSD persistent disks. Balanced persistent disks are an alternative to SSD persistent disks that balance performance and cost. For more information, see [Persistent disk types](https://docs.cloud.google.com/compute/docs/disks#disk-types).

## July 17, 2020

Feature

The Organization Policy for [restricting protocol forwarding creation](https://docs.cloud.google.com/compute/docs/protocol-forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization) has launched into **Beta**.

## July 16, 2020

Feature

You can now [suspend and resume](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) your VM instances. This feature is available in **Beta**.

Change

SSD persistent disks on certain machine types now have a maximum write throughput of 1,200 MB/s. To learn more about the requirements to reach these limits, see [Block storage performance](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).

## July 06, 2020

Feature

E2 machine types now offer up to 32 vCPUs. See [E2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#e2_machine_types) for more information.

## June 26, 2020

Feature

To support a wide variety of BYOL scenarios, you can now [configure VMs to live migrate within a sole-tenant node group during host maintenance events](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses). This is **Generally Available**.

## June 22, 2020

Feature

N2D machine types are now available in Belgium, europe-west1, in all three zones. Read more information on the [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types) page.

## June 15, 2020

Feature

[New sole-tenant node types (c2-node-60-240, n1-node-96-1433, and n2d-node-224-896)](https://docs.cloud.google.com/compute/docs/nodes#node_types) are available in **Beta**.

## June 08, 2020

Feature

Enhancements to the pre-configured Cloud Monitoring Compute Engine **VM Instances** dashboard. Compute Engine cross-fleet metrics and detail views specific to CPU, Disk, Memory, and Network are now available. Use filters to narrow down the set of VMs being inspected, and use the time selector or in-chart time selection to change the time window. VMs with the Monitoring agent installed get detailed memory and disk analysis out of the box.

Feature

The `asia-southeast2` Jakarta, Indonesia region is now available to all projects and users. The zones in the `asia-southeast2` region have [E2 and N1 machine types](https://docs.cloud.google.com/compute/docs/machine-types). See [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.

## June 05, 2020

Feature

[New sole-tenant node types (m1-node-96-1433 and n2-node-80-640)](https://docs.cloud.google.com/compute/docs/nodes#node_types) are available in **Beta**.

Feature

[CPU overcommit on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms) lets you overprovision sole-tenant node resources and schedule more VM CPUs on a sole-tenant node than are normally available. This feature is in **Beta**.

## June 01, 2020

Feature

NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

  * Changua County, Taiwan `asia-east1-c`



For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## May 21, 2020

Feature

You can now SSH to your VMs using hardware-backed SSH key pairs. For more information, see [SSH with security keys](https://docs.cloud.google.com/compute/docs/tutorials/ssh-with-sk).

Feature

E2 shared-core machine types now support committed use discounts in all regions. See the [VM instance](https://docs.cloud.google.com/compute/vm-instance-pricing#e2_sharedcore_machine_types) pricing page for more information.

## May 20, 2020

Feature

If your managed instance group encountered errors - for example, if a VM could not be created - you can [view those errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors) to diagnose and mitigate the cause. This is **Generally available**.

## May 19, 2020

Feature

Troubleshoot VMs by [capturing screenshots](https://docs.cloud.google.com/compute/docs/instances/capturing-vm-screenshots). This is in **beta**.

## May 12, 2020

Feature

Automatically manage the size of sole-tenant node groups with the [sole-tenant node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/node-group-autoscaler). This is **Generally Available**.

## May 11, 2020

Feature

You can identify idle persistent disk resources by using [idle persistent disk recommendations](https://docs.cloud.google.com/compute/docs/disks/viewing-and-applying-idle-pd-recommendations). Following these recommendations will help reduce unused resources and reduce your compute bill. This feature is **Generally available**.

## April 30, 2020

Change

SSD persistent disks now have increased write throughput limits on instances with 1 to 15 vCPUs. This improvement applies to SSD persistent disks on all machine types except C2 machine types. To learn more about the requirements to reach these limits, see [Block storage performance](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).

## April 20, 2020

Feature

  * The `us-west4` Las Vegas, Nevada region is now available to all projects and users. The zones in the `us-west4` region have [N1 and E2 machine types](https://docs.cloud.google.com/compute/docs/machine-types). See [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## April 16, 2020

Feature

  * Committed use discount shared billing is now available in **beta**. You can share committed use discounts among all your projects that fall under the same billing account. For more information, see [Signing up committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).



## April 15, 2020

Feature

The latest stable version of the OS Config agent is [`20200402.01`](https://github.com/GoogleCloudPlatform/osconfig/releases/tag/20200402.01). If you were using OS patch management in Beta, you can update the agent on your existing VMs, see [Updating the OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#update-agent).

Feature

You can manage, maintain, and view patch compliance for your VM instances using the OS patch management feature. For more information, see [OS patch management](https://docs.cloud.google.com/compute/docs/os-patch-management). This feature is now **Generally available**.

Feature

You can identify VM instances that are not being used with [idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations). Use these recommendations to reduce unused resources and reduce your compute bill. This feature is **Generally available**.

## April 09, 2020

Feature

  * **GA:** [Compute Engine enables Shielded VM features by default](https://docs.cloud.google.com/compute/docs/instances/modifying-shielded-vm).



## April 08, 2020

Feature

  * You can identify idle persistent disk resources by using [idle persistent disk recommendations](https://docs.cloud.google.com/compute/docs/disks/viewing-and-applying-idle-pd-recommendations). Following these recommendations will help reduce unused resources and reduce your compute bill. This feature is in **Beta**.



## April 06, 2020

Feature

  * N2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * The Dalles, Oregon, USA `us-west1-b`
    * Ashburn, Northern Virginia, USA `us-east4-a`
    * St. Ghislain, Belgium `europe-west1-d`



Feature

  * [N2D machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now **Generally Available**.



Feature

  * C2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Ashburn, Northern Virginia, USA `us-east4-b,c`



## April 01, 2020

Feature

  * You can now define where your VM instances are located relative to each other on the underlying host systems in a Google datacenter. Create a placement policy to locate VM instances close to each other for low latency, or create a policy to spread VM instances out so that they do not share the same infrastructure. See [Defining instance location within a zone](https://docs.cloud.google.com/compute/docs/instances/define-instance-placement) to learn more.



Feature

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

    * Frankfurt, Germany: `europe-west3-b`

For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).




## March 31, 2020

Feature

  * N2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * The Dalles, Oregon, USA `us-west1-a`
    * Changua County, Taiwan `asia-east1-c`



Feature

  * **Beta:** [Collect diagnostic information from Windows VMs](https://docs.cloud.google.com/compute/docs/instances/collecting-diagnostic-information).



Feature

  * M1 megamem machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Eemshaven, Netherlands `europe-west4-b`



Feature

  * M2 ultramem machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Los Angeles, California, USA `us-west2-a,c`



Feature

  * M1 ultramem machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Ashburn, Northern Virginia, USA `us-east4-a`



Feature

  * C2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Frankfurt, Germany `europe-west3-a,b`
    * Ashburn, Northern Virginia, USA `us-east4-a`



## March 24, 2020

Feature

  * You can [update selected VM instances in a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances), with minimal disruption and in a controlled way. This is **Generally available**.



Feature

  * Committed use discounts no longer require specific ratios for cores and memory. Now you can create separate committed use discount contracts for either cores or memory. Separating cores and memory provides more flexibility and improved cost optimization. Learn more at [Purchasing commitments for machine types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchasecommitment).



Feature

  * You can [preserve the names](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#preserving_instance_names) of your VM instances when rolling out updates in a managed instance group. This is **Generally available**.



## March 19, 2020

Feature

  * [E2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#e2_machine_types) are **Generally available**.



## March 16, 2020

Feature

  * C2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * St. Ghislain, Belgium `europe-west1-c,d`



Feature

  * N2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * London, England UK `europe-west2-b`



## March 11, 2020

Feature

  * In **beta** , you can create an instance with 16 or 24 local SSD partitions for 6 TB and 9 TB of local SSD space, respectively. With 24 local SSD partitions, performance can reach a combined total of 2.4 million read IOPS. For more information, see [9 TB Local SSD maximum capacity beta](https://docs.cloud.google.com/compute/docs/disks/local-ssd#capacity_9tb).



Feature

  * You can identify VM instances that are not being used with [idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations). Use these recommendations to reduce unused resources and reduce your compute bill. This feature is **Beta**.



## March 09, 2020

Feature

  * [Machine image](https://docs.cloud.google.com/compute/docs/machine-images) is now available in **beta**. You can use machine images to store configuration, metadata, permission, and data required to create a VM instance in a single resource.



## March 05, 2020

Deprecated

  * CoreOS Container Linux images will reach their end of life on May 26, 2020. On Compute Engine, you can now use [Fedora CoreOS](https://docs.cloud.google.com/compute/docs/images/os-details#fedora_coreos).



## March 03, 2020

Feature

  * You can now create [E2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#e2_machine_types) in all [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).



## March 02, 2020

Feature

  * You can now [use the Google Cloud Console to export images to Cloud Storage](https://docs.cloud.google.com/compute/docs/images/export-image#exporting_an_image_with_a_single_command). This is **Generally Available**.



## February 27, 2020

Feature

  * You can now manage, maintain, and view patch compliance for your VM instances using the OS patch management feature. For more information, see [OS patch management](https://docs.cloud.google.com/compute/docs/os-patch-management). This feature is available in **beta**.



Feature

  * C2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Council Bluffs, Iowa, US `us-central1-a`



Feature

  * E2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Los Angeles, USA `us-west2-a,b,c`
    * London, England, UK `europe-west2-a,b,c`
    * Frankfurt, Germany `europe-west3-b,c`
    * Tokyo, Japan `asia-northeast1-a,b,c`
  * N2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Frankfurt, Germany `europe-west3 a,b`



Feature

  * M2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Mumbai, India `asia-south1-a`



## February 24, 2020

Feature

  * The `us-west3` Salt Lake City, UT region is now available to all projects and users. The zones in the `us-west3` region have the [Skylake CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms). See [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## February 21, 2020

Feature

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

    * Changhua County, Taiwan: `asia-east1-a`
    * London, England, UK: `europe-west2-b`

For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).




## February 19, 2020

Feature

  * M2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Northern Virginia `us-east4-a,b`



Feature

  * If you have configured autohealing for your managed instance group, you can [review the health state](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#checking_whether_instances_are_healthy) of each VM in the group. This is **Generally Available**.



## February 18, 2020

Feature

  * N2D machine types are available in beta. N2D machine types are built on top of second generation AMD EPYC Rome processors. They are a great fit for general purpose workloads and for workloads that require high memory bandwidth. Learn more about these [general purpose machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2d_machine_types_beta).



## February 13, 2020

Feature

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

    * London, England, UK: `europe-west2-a`
    * Seoul, South Korea: `asia-northeast3-b,c`

For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).




## February 12, 2020

Feature

  * You can now maintain consistent software configurations across VM instances using guest policies. For more information, see [OS configuration management](https://docs.cloud.google.com/compute/docs/os-config-management). This feature is available in **beta**.



## February 11, 2020

Feature

  * To support a wide variety of BYOL scenarios, you can now [configure VMs to live migrate within a sole-tenant node group during host maintenance events](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license). This is available in **Beta**.



## February 07, 2020

Feature

  * Google Workspace administrators can now choose whether to include the domain suffix in usernames generated by the OS Login API. For more information, see [Managing the OS Login API](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#manage-oslogin-api). This feature is **Generally Available**.



## February 05, 2020

Change

  * Read an [FAQ](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-accounting-faq) that can help you evaluate whether to classify [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes) payments as capital expenditures (CAPEX) or operational expenditures (OPEX).



## February 03, 2020

Feature

  * You can build highly available deployments of stateful workloads on VM instances using [stateful managed instance groups (stateful MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs). A stateful MIG preserves the unique state of each instance (instance name, attached persistent disks, and/or metadata) on machine restart, recreation, autohealing, or update. Stateful MIGs are available in **beta**.



## January 31, 2020

Feature

  * You can now enable an [autoscaler](https://docs.cloud.google.com/compute/docs/nodes/node-group-autoscaler) on your sole-tenant node groups. This is available in **Beta**.



Feature

  * You can now [reschedule VMs on, off, or between sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/vm-tenancy). This is **Generally Available**.



## January 24, 2020

Feature

  * The `asia-northeast3` Seoul region is now available to all projects and users. The zones in the `asia-northeast3` region have the [Skylake CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms). See [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## January 21, 2020

Feature

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional zones:

    * Tokyo: `asia-northeast1-c`
    * Singapore: `asia-southeast1-c`
    * Iowa: `us-central1-f`
    * Mumbai: `asia-south1-a`

For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).




Feature

  * You can temporarily turn off or restrict managed instance group autoscaling. The autoscaler's configuration remains intact, and all autoscaling activities resume when you turn it on again or lift the restriction. [Turning off or restricting autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#disable_or_restrict_an_autoscaler) for managed instance groups is now **Generally available**.



## January 09, 2020

Change

  * NVIDIA® Tesla® T4 GPU prices are reduced in all regions. For more information about the new prices for each region, see [GPU pricing](https://cloud.google.com/compute/gpus-pricing).



## December 18, 2019

Feature

  * Specifying an image storage location is now **Generally Available** for custom images. Specifying your image storage location helps you meet your regulatory and compliance requirements for data locality as well as your high availability needs by ensuring redundancy across regions. See [Creating, deleting, and deprecating custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images), and [Creating a Windows image](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image).



## December 17, 2019

Feature

  * E2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Iowa `us-central1-a`



## December 16, 2019

Change

  * On November 21, 2019, we announced that organizations would be disabled from using nested virtualization by default starting January 31, 2020. This will no longer happen and nested virtualization will be allowed by default. However, we recommend [explicitly setting your organizational policy](https://docs.cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances#enable_nested_virt_org) to allow or prevent nested virtualization as a best practice.



## December 13, 2019

Feature

  * N2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * Tokyo `asia-northeast1-a,b`
    * Singapore `asia-southeast1-a`
    * Sydney `australia-southeast1-b`



## December 11, 2019

Feature

  * E2 machine types are available in **beta**. These machine types are ideal for small to medium workloads that require 16 vCPUs or less, no local SSDs, and no GPUs. Learn more about these [cost-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#e2_machine_types).



## December 10, 2019

Feature

  * You can now create VM instances with V100 AND T4 GPUs that support network bandwidths of up to 100 Gbps. See [Using network bandwidths of up to 100 Gbps](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus#high-bandwidth). This feature is available in **beta**.



## November 22, 2019

Feature

  * Virtual machines with 2 or 4 vCPUs now have a maximum egress rate of 10 Gbps. This feature is now **Generally Available**. For more information, see [Machine types](https://docs.cloud.google.com/compute/docs/machine-types).



Feature

  * N2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * South Carolina `us-east1-d`
    * Belgium `europe-west1-c`
    * London `europe-west2-c`
    * Sydney `australia-southeast1-a`



## November 21, 2019

Breaking

  * After January 31, 2020, nested virtualization will be disabled by default by an organizational policy. To avoid interruptions to your workloads, [update the organization policy](https://docs.cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances#enable_nested_virt_org) to allow nested virtualization.



## November 08, 2019

Feature

  * N2 machine types are now available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

    * South Carolina `us-east1-c`
    * Belgium `europe-west1-b`
    * London `europe-west2-a`



## November 06, 2019

Feature

  * You can temporarily turn off or restrict managed instance group autoscaling. The autoscaler's configuration remains intact, and all autoscaling activities resume when you turn it on again or lift the restriction. [Turning off or restricting autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler) for managed instance groups is now available in **Beta**.



## October 25, 2019

Feature

  * As a Google Workspace admin, you can now complete the following tasks for the OS Login feature:

    * Enable OS Login using an organization policy. For more information, see [Setting up an OS Login organization policy](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#set_org_policy).
    * Track interactions with the OS Login API. For more information, see [Auditing OS Login events](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#audit-events)



## October 22, 2019

Feature

  * You can issue 100K read I/Os per second on SSD persistent disks. Read the [persistent disk performance](https://docs.cloud.google.com/compute/docs/disks#introduction) document for details.



Feature

  * You can attach up to 257 TB of persistent disk storage to each instance. This feature is **Generally available** for most [machine types](https://docs.cloud.google.com/compute/docs/machine-types).



## October 21, 2019

Feature

  * Increased the per-instance persistent disk write throughput performance for zonal and regional SSD. Read the [persistent disk performance documentation](https://docs.cloud.google.com/compute/docs/disks#introduction) for details.



## October 07, 2019

Feature

  * You can now create a VM instance from a persistent disk snapshot in the API or the `gcloud` tool. This feature is now **Generally available**. Read [Creating a VM instance from a snapshot](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#createsnapshot) for more information



## October 02, 2019

Feature

  * OS Inventory Management is now **Generally available**. For more information, read [Viewing operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).



## October 01, 2019

Feature

  * Importing VM instances using open virtual appliance (OVA) is now **Generally available**. For more information, read [Importing virtual appliances](https://docs.cloud.google.com/compute/docs/import/import-ovf-files).



## September 27, 2019

Feature

  * N2 machine types are now **Generally Available**. Learn more about [N2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2_machine_types).



## September 25, 2019

Feature

  * The gVNIC virtual network interface is now available in **Beta**. For more information, see [Creating VM instances that use the gVNIC network interface](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic).



Deprecated

  * The v1beta1 server and v0.1 metadata server endpoints are deprecated and are scheduled for shutdown. For information about transitioning to the v1 metadata server endpoint, see [Transitioning to the v1 metadata server endpoint](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#transitioning).



Feature

  * For additional security when connecting to Linux instances, you can now store your host keys as guest attributes. This feature is now in **General availability** , see [Storing host keys](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#store-host-key).



## September 24, 2019

Feature

  * Instances with more than 16 vCPUs have an increased standard persistent disk bandwidth limit of 1200 MB/s for reads and 400 MB/s for writes. Instances with between 8 and 15 vCPUs also have an increased standard persistent disk bandwidth limit of 800 MB/s reads and 400 MB/s for writes. Read the [Persistent Disk Performance](https://docs.cloud.google.com/compute/docs/disks#introduction) page for details.



## September 23, 2019

Feature

  * N2 machine types are now available in the following regions and zones:

    * Taiwan `asia-east1-a`, `asia-east1-b`
    * Netherlands `europe-west4-a`
    * Iowa `us-central1-f`



Feature

  * C2 machine types are now available in following regions and zones:

    * Singapore `asia-southeast1-b`, `asia-southeast1-c`
    * Netherlands `europe-west4-a`
    * Los Angeles `us-west2-a`, `us-west2-c`
    * Iowa `us-central1-f`



## September 16, 2019

Feature

  * C2 machine types are now available in the South Carolina `us-east1` region in all zones.



## September 13, 2019

Feature

  * Launched support for [virtual displays](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display) to **General availability**.



## September 04, 2019

Feature

  * [Reserving zonal resources](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) is now **Generally available**. Reserve VMs, with or without GPUs and local SSD, in a specific zone.



## September 03, 2019

Change

  * Renamed `n1-megamem` and `n1-ultramem` machine types to `m1-megamem` and `m1-ultramem` respectively.



Feature

  * M1 machine types are now available in Taiwan, London, and Mumbai.



## August 26, 2019

Feature

  * Larger memory-optimized machine types are now **Generally Available**. Learn more about these [larger ultramem machine types](https://docs.cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family).



## August 23, 2019

Feature

  * C2 machine types are now available in zones in Taiwan, Tokyo, London, and in the `europe-west4-a` zone in the Netherlands. See [machine types](https://docs.cloud.google.com/compute/docs/machine-types) for more information.



Feature

  * N2 machine types are now available in Singapore and in the `europe-west4-a` zone in the Netherlands. See [machine types](https://docs.cloud.google.com/compute/docs/machine-types) for more information.



## August 13, 2019

Feature

  * For additional security when connecting to Linux instances, you can now store your host keys as guest attributes. This feature is now available in **Beta** , see [Storing host keys](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#store-host-key).



Feature

  * Specifying an image storage location is now available in **Beta** for custom images. Specifying your image storage location helps you meet your regulatory and compliance requirements for data locality as well as your high availability needs by ensuring redundancy across regions. See [Creating, deleting, and deprecating custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images), and [Creating a Windows image](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image).



## August 12, 2019

Feature

  * New general-purpose [N2 machine types](https://docs.cloud.google.com/compute/docs/machine-types#n2_machine_types) are now available in **Beta**.



Feature

  * Scheduled snapshots for persistent disks are now **Generally Available**. For more information, see [Creating scheduled snapshots for persistent disk](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).



## July 31, 2019

Feature

  * [Compute-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#c2_machine_types), are now available in **General Availability**. Applicable [charges](https://docs.cloud.google.com/compute/vm-instance-pricing#c2_machine_types) will apply.



## July 25, 2019

Feature

  * New larger memory-optimized machine types are now available in **Beta**. Learn more about these [larger ultramem machine types](https://docs.cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family).



## July 17, 2019

Feature

  * Memory-optimized commitments are now available in **Beta**. Read about [Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).



## July 08, 2019

Feature

  * You can now create VMs with [compute-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#c2_machine_types), available in **Beta**. Applicable [charges](https://docs.cloud.google.com/compute/vm-instance-pricing#c2_machine_types) will apply.



Feature

  * You can now view operating system details for your VM instances using OS Inventory Management. This feature is available in **Beta**. For more information, read [Viewing operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).



## July 02, 2019

Feature

  * [Setting and querying guest attributes](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#guest_attributes) is now **Generally Available**. You can use guest attributes to communicate the status of applications and scripts within your instance.



Feature

  * [Updating selected VM instances in a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances), with minimal disruption and in a controlled way, is now available in **Beta**.



Feature

  * Importing VM Instances using OVA or OVF virtual appliances is now available in **Beta**. For more information, read [Importing OVF virtual appliances](https://docs.cloud.google.com/compute/docs/import/import-ovf-files).



## June 27, 2019

Feature

  * [Mounting a persistent disk as a data volume in a container on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers#mounting_a_persistent_disk_as_a_data_volume) is now **Generally Available**.



## June 18, 2019

Feature

  * [Bring your own license with in-place restarts](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license/bringing-your-own-license-sole-tenant-nodes) is now available in **General Availability**.



## May 17, 2019

Feature

  * You can now use the [Google Cloud Platform Console](https://console.cloud.google.com/) to [import virtual disks](https://docs.cloud.google.com/compute/docs/images/importing-virtual-disks#importing_virtual_disks).



Feature

  * Regional persistent disks can now be attached to multiple VMs in read-only mode. For more information, read [Sharing a regional persistent disk between multiple instances](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#use_multi_instances).



## May 16, 2019

Feature

  * Snapshot locations are now **Generally Available**. The storage location of a snapshot affects the availability of the snapshot and networking costs for creating and restoring a snapshot. For more information, see [Selecting the storage location for a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#selecting_a_storage_location).



Change

  * Multi-regional snapshot pricing is now separated from regional snapshot pricing. Read the [Persistent disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk) page to learn about multi-regional snapshot pricing.



## May 07, 2019

Feature

  * The following operating systems are now **Generally Available** as [public images](https://docs.cloud.google.com/compute/docs/images#rhel):

    * Red Hat Enterprise Linux 8
    * Red Hat Enterprise Linux for SAP with Update Services and High Availability 7.4 and 7.6



Deprecated

  * Red Hat has deprecated Red Hat Enterprise Linux 7 for SAP Applications and Red Hat Enterprise Linux 7 for HANA. For more information, read the [RHEL for SAP offerings](https://access.redhat.com/articles/3751271) page. As a result, these images are now marked deprecated on Compute Engine.



## April 29, 2019

Feature

  * [Reserving zonal resources](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) is now available in **Beta**. You can reserve memory-optimized and general purpose VMs, with or without GPUs and local SSD, in a specific zone.



## April 19, 2019

Feature

  * Regional persistent disk is now **Generally Available**. To learn more, read [Adding or resizing regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk). See the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#disk) to learn how this disk type is billed.



## April 18, 2019

Feature

  * The `asia-northeast2` Osaka region is now available to all projects and users. The zones in the `asia-northeast2` region have the [Skylake CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms). See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## April 10, 2019

Feature

  * NVIDIA® Tesla® T4 GPU and NVIDIA® Tesla® T4 Virtual Workstations are now **Generally available** , in eight regions. See the [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) page to learn more.



## April 05, 2019

Feature

  * [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the following zones:

    * `us-east4-b`
    * `us-east4-c`

See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.




## April 02, 2019

Feature

  * [Bringing your own licenses with sole-tenant nodes](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license) is now available in **Beta**.



## March 29, 2019

Feature

  * [Viewing VM serial port output in Stackdriver](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output) is now **Generally Available**. If you enable serial port output logging to Stackdriver, logs are retained for 30 days, even if your VM is deleted.



## March 28, 2019

Change

  * The Compute Engine [SLA](https://cloud.google.com/compute/sla) has been updated.



## March 27, 2019

Feature

  * You can now add extra security when connecting to instances using OS Login. For more information, see [Setting up OS Login with two-factor authentication](https://docs.cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication).



Feature

  * You can add virtual display devices to your instances. Use virtual display devices to run applications that require a display device without adding a phyiscal GPU device. Virtual display devices are available in **Beta**. Read [Enabling Virtual Displays on Instances](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display) to learn more.



## March 22, 2019

Feature

  * Increased the per-instance persistent disk throughput performance to 240 MB/s for read and write bandwidth. See the [Persistent Disk Performance](https://docs.cloud.google.com/compute/docs/disks#introduction) for details.



## March 11, 2019

Feature

  * Added new `europe-west6` region in Zürich, Switzerland. The `europe-west6` region contains Skylake zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## February 27, 2019

Feature

  * [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the following zones:

    * `asia-northeast1-a`
    * `asia-southeast1-b`
    * `northamerica-northeast1-b`
    * `northamerica-northeast1-c`
    * `southamerica-east1-b`
    * `southamerica-east1-c`
    * `us-central1-a`

See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.




## February 21, 2019

Feature

  * You can now attach up to 128 independent persistent disks to custom machine types and most predefined machine types. For more details, see [Persistent disk limits](https://docs.cloud.google.com/compute/docs/disks#pdnumberlimits).



## February 14, 2019

Feature

  * User-created scheduled snapshots for zonal and regional persistent disks is now available in **Beta**. Scheduled snapshots allows you to create an automatic snapshot schedule and include a retention policy for maintaining those snapshots. For more information, see [Creating scheduled snapshots for persistent disk](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).



## February 11, 2019

Feature

  * [Application-based health checking and autohealing for managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) is now **Generally Available**.



Feature

  * [Sole tenant nodes](https://docs.cloud.google.com/compute/docs/nodes) are now available in Hong Kong (`asia-east2`).



## February 06, 2019

Feature

  * The [Managed Instance Group Updater](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) is now **Generally Available**. This feature enables proactive, flexible rolling updates with the option to canary a new version on a subset of managed instance group VMs.



Feature

  * Users and applications can now write to instance-specific guest-writeable metadata values. You can use guest attributes to communicate status of applications and scripts within your instance. Read [Setting and querying guest attributes](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#guest-attributes) to learn more.



Feature

  * Selecting 16 KB physical block size is now in **Beta**. You can create zonal and regional persistent disks with a 16 KB physical block. Some database applications might see greater performance by using 16 KB physical block. Read [Adding Persistent Disks](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#physical_block_storage) for feature details. Read [Optimizing Persistent Disk and Local SSD Performance](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance) for performance comparisons. Read the [Best practices for persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) tutorial to learn more.



## January 29, 2019

Feature

  * [Granting access to specific Compute resources](https://docs.cloud.google.com/compute/docs/access/granting-access-to-resources), such as VM instances, disks, and images, is now **Generally Available**. This feature gives you flexibility to apply the principle of least privilege, for example, to grant collaborators permissions only to the specific resources that they need to do their work.



## January 24, 2019

Feature

  * Detaching and reattaching boot disks from a stopped VM instance is now available in **GA**. Use the [Google Cloud Platform Console](https://console.cloud.google.com/), `gcloud` or API to detach a failed boot disk, fix it, then reattach it back to the original VM instance. You can also use this feature for rollbacks: detach a disk, create a new disk using an earlier snapshot, and attach that restored disk to your VM. See [Detaching and Reattaching Boot Disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) for details.



Feature

  * [Creating a VM Instance with a Custom Hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm) is now **Generally Available**.



## January 16, 2019

Feature

  * NVIDIA® Tesla® T4 GPU and NVIDIA® Tesla® T4 Virtual Workstations are now available, as **Beta** , in eight regions. See the [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) page to learn more.



## January 11, 2019

Feature

  * Windows Server 2019 images are now **Generally Available** as a [public image](https://docs.cloud.google.com/compute/docs/images).



Feature

  * Windows Server, version 1809 images are now **Generally Available** as a [public image](https://docs.cloud.google.com/compute/docs/images). This is a Server Core image that is part of the [semi-annual release cycle](https://docs.microsoft.com/en-us/windows-server/get-started/semi-annual-channel-overview) for Windows Server.



## December 14, 2018

Feature

  * User-selected snapshot storage locations are now available in **Beta**. The storage location of a snapshot affects the availability of the snapshot and networking costs. For more information, see [Selecting the storage location for a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#selecting_a_storage_location).



Change

  * Snapshot creation might now incur networking charges. These charges will begin after this feature reaches General Availability (GA), and will depend upon the [storage location of a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#selecting_a_storage_location) and the location of the source disk. For more information, see [Network charges for snapshot creation and restoration](https://docs.cloud.google.com/compute/disks-image-pricing#disk).



## November 15, 2018

Feature

  * Windows Service Activation using Private Google Access is **Generally Available**. Read the [Private Google Access](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) page to learn more.



## November 13, 2018

Feature

  * Detaching and reattaching boot disks from a stopped VM instance is now available in **Beta**. Use the gcloud or API command to detach a failed boot disk, fix it, then reattach it to a different VM instance. See [Detaching and Reattaching Boot Disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) for details.



## November 08, 2018

Feature

  * [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the `southamerica-east1-a` zone. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.



## November 07, 2018

Feature

  * [Creating a VM Instance with a Custom Hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm) is available in **Beta**.



## October 24, 2018

Feature

  * [Viewing VM serial port output in Stackdriver](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output) is available in **Beta**. To help with troubleshooting, these logs can be retained for up to 30 days after a VM instance is deleted.



## October 22, 2018

Feature

  * The `asia-east2` Hong Kong region is now available to all projects and users. The zones in the `asia-east2` region have the [Skylake CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms). See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## October 19, 2018

Feature

  * [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the `asia-southeast1-c`, `australia-southeast1-c`, `europe-west3-a`, `europe-west3-b` and `us-west2-b` zones. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.



## October 02, 2018

Feature

2018-10-02

FEATURE * Protect data on Compute Engine with Cloud Key Management Service encryption keys. [Customer-Managed Encryption Keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) are now generally available.

Feature

  * Compute Engine now uses a [resource based pricing model](https://docs.cloud.google.com/compute/vm-instance-pricing#pricing) that provides greater savings from [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts). All machine types except for shared-core machine types are now billed by their individual vCPU and memory usage rather than billing by each machine type. Sustained use discounts are calculated for vCPU and memory usage across an entire region rather than separately for each machine type in each zone. See the [Compute Engine Pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#pricing) page for details.



## September 26, 2018

Feature

  * NVIDIA® Tesla® P4 GPUs are now **Generally Available**. For information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).



Feature

  * For graphics-intensive workloads, NVIDIA® GRID®-based virtual workstations using NVIDIA® Tesla® P4 and P100 GPUs are now **Generally Available**. For information on GPUs for graphics-intensive applications, see [GPUs for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations).



Feature

  * NVIDIA® Tesla® P4 GPUs are now available in the `australia-southeast1-a`, and `australia-southeast1-b` zones. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#gpus-list) for a complete list of zones where GPUs are available.



Feature

  * NVIDIA® Tesla® v100 GPUs are now available in the `us-central1-b` and `europe-west4-b` zones. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#gpus-list) for a complete list of zones where GPUs are available.



## September 25, 2018

Feature

  * Windows Server instances no longer require a public IP for Windows Service Activation. If your Windows Server instance uses a subnetwork that is enabled for [Private Google Access](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation), that instance can complete Windows Service Activation over its internal VPC network. Windows Service Activation using Private Google Access is available in **Beta**. Read the [Private Google Access](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) page to learn more.



## September 20, 2018

Feature

  * [Deploying Docker Containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/deploying-containers) is now **Generally Available**.



## September 12, 2018

Feature

  * Now in **Beta** , you can [grant access to specific Compute resources](https://docs.cloud.google.com/compute/docs/access/granting-access-to-resources), such as VM instances, disks, and images. This feature gives you flexibility to apply the principle of least privilege, for example, to grant collaborators permissions only to the specific resources that they need to do their work.



## September 06, 2018

Feature

  * [Zonal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#zonal-dns) are now **Generally Available**. Projects that enable the Compute Engine API after today will use zonal DNS names by default. Projects and organizations that enabled the Compute Engine API before today will continue to use global DNS names by default. Migrating a project to an organization will not change the default DNS name for the project. Zonal DNS names are unique to each zone on your internal [VPC](https://docs.cloud.google.com/vpc/docs/vpc) networks. Zonal DNS names improve the fault tolerance of your applications when they reference instances on your internal VPC network. New and existing projects can still use global DNS names, but [migration](https://docs.cloud.google.com/compute/docs/internal-dns#migrating-to-zonal) is encouraged. Read [Internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns) to learn more.



## September 04, 2018

Feature

  * The `simulateMaintenanceEvent` API method is **Generally Available**. Read [testing your availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies) to learn how to simulate a Compute Engine maintenance event and observe how the instance availability settings affect the behavior of your instances.



## August 27, 2018

Feature

  * NVIDIA® Tesla® V100 GPUs are now **Generally Available**. For information about using V100 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).



## August 17, 2018

Feature

  * Zonal SSD persistent disks and regional SSD persistent disks now have increased read throughput and read input/output operations per second (IOPS). See [Optimizing Persistent Disk and Local SSD Performance](https://docs.cloud.google.com/compute/docs/disks/performance) for more information.



## August 08, 2018

Feature

  * Sole-tenant nodes are now **Generally Available**. Read [Sole-tenant Nodes](https://docs.cloud.google.com/compute/docs/nodes) to learn how you can use these systems to isolate your workloads from each other and from other Compute Engine projects.



## August 03, 2018

Feature

  * If you have graphics-intensive workloads, such as 3D rendering or video editing, you can create virtual workstations that use NVIDIA® GRID® technology, using NVIDIA® Tesla® P4 and P100 GPUs. For information on GPUs for graphics-intensive applications, see [GPUs for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations).



Feature

  * You can use organization policies to restrict use of your disks, custom images, and snapshots so that they can be used only within your organization or specific projects. This prevents users from creating copies of disks, outside of your organization. Read [restricting use of your shared images, disks, and snapshots](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects#restrict) to learn more.



## July 25, 2018

Feature

  * [Shielded VM](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) is now available in **Beta**. Shielded VM images offer security features like UEFI-compliant firmware, Secure Boot, and vTPM-protected Measured Boot.



## July 23, 2018

Feature

  * The `n1-megamem-*` family of [memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with 1.4 TB of memory are now **Generally Available** to all projects. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.



## July 19, 2018

Feature

  * Windows Server for Containers is now **Generally Available** as a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support).



Feature

2018-07-19

FEATURE * Selecting specific zones for regional managed instance groups is now **Generally Available**. See [Distributing Instances using Regional Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selecting_zones).

## July 18, 2018

Feature

  * [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now **Generally Available**. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.



## July 17, 2018

Feature

  * If you need high availability and redundancy for your Microsoft SQL Server on Compute Engine, you can [configure an Always On Failover Cluster Instance (FCI) with Storage Spaces Direct (S2D)](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance).



## July 11, 2018

Feature

  * [Virtual machine sizing recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-sizing-recommendations-for-instances) are now **Generally Available**.



## July 10, 2018

Issue

  * If you try to create a new instance in this zone for a project that existed before this release date, you may receive the following error message: "No default subnetwork was found in the region of the instance." This issue will be resolved within three days of this launch. In the meantime, the workaround is to [manually create a subnet](https://docs.cloud.google.com/vpc/docs/using-vpc) and use it for a new VM.



Feature

  * Added new `us-west2` Los Angeles region. `us-west2` contains Skylake zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



Feature

  * [Creating an instance template from a VM instance](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) is now **Generally Available**. This feature can be used for instance duplication, backup, and recreation.



## July 02, 2018

Feature

  * You can now add 2 and 4 NVIDIA® Tesla® V100 GPUs to your Compute Engine instances. For information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).



## June 22, 2018

Feature

  * You can [purchase committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for [memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem). Memory-optimized machine types use their own commitment type with different pricing. You must [request access](https://docs.google.com/forms/d/e/1FAIpQLSe534-lhy0aQq4agiSi7ERSKddJS2QrwZo_jYQDNKkKnT3Y3Q/viewform?usp=sf_link) to use committed use discounts for memory-optimized machine types. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#committed_use) for pricing details about committed use discounts.



## June 19, 2018

Feature

  * The Compute Engine Trusted Images policy is now **Generally Available**. Use this policy to control which boot disk images your project members can access. Read [Restricting Access to Images](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) for more information.



## June 11, 2018

Issue

  * If you try to create a new instance in this zone for a project that existed before this release date, you may receive the following error message: "No default subnetwork was found in the region of the instance." This issue will be resolved within three days of this launch. In the meanwhile, the workaround is to [manually create a subnet](https://docs.cloud.google.com/vpc/docs/using-vpc) and use it for a new VM.



Feature

  * Added new `europe-north1` region. `europe-north1` contains Skylake zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



Feature

  * GPUs on preemptible VM instances are now **Generally Available**.

For information about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).




Change

  * The prices for GPUs on preemptible VM instances have reduced. For the updated prices, see the [GPUs pricing page](https://cloud.google.com/compute/gpus-pricing).



## June 07, 2018

Feature

  * You can create sole-tenant nodes, which are physical Compute Engine servers that are dedicated to hosting only VM instances from your specific project. Read [Sole-tenant Nodes](https://docs.cloud.google.com/compute/docs/nodes) to learn how you can use these systems to isolate your workloads from each other and from other Compute Engine projects.



## June 05, 2018

Feature

  * Protect data on Compute Engine with Cloud Key Management Service encryption keys. [Customer-Managed Encryption Keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) are now available in beta.



## May 28, 2018

Feature

NVIDIA® Tesla® V100 GPUs are now available in the following regions:

  * us-west1-a
  * us-central1-a
  * asia-east1-c



For information about using V100 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## May 23, 2018

Feature

  * Added support for [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks#repds) into **Beta**. This feature provides synchronous block-level replication across two zones in a region for each regional persistent disk.



## May 16, 2018

Feature

  * Instances with NVIDIA® Tesla® V100 GPUs can now use Local SSD devices. For information on using V100 GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).



## May 08, 2018

Feature

  * [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in **Beta**. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.



## May 07, 2018

Feature

  * Added local SSD support to the `europe-west4-a` zone. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## May 01, 2018

Feature

  * Added a third zone to the `asia-southeast1` region. This zone supports machine types with up to 96 vCPUs when using the Skylake platform. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## April 30, 2018

Feature

  * NVIDIA® Tesla® V100 GPUs are now available in **Beta**. For information on the zones where V100 GPUs are available, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).



## April 20, 2018

Feature

  * Creating multiple secondary non-boot disks when you [create your VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) is now **Generally Available**.



Feature

  * NVIDIA® Tesla® P100 GPUs are now **Generally Available**. To learn about the zones where P100 GPUs are available, read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).



## April 19, 2018

Change

  * The price of SLES for SAP images is reduced. Read [SUSE premium image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#suse_images) for details.



## April 17, 2018

Feature

NVIDIA® Tesla® P100 GPUs are now available in the following zones:

  * `asia-east1-c`
  * `europe-west4-a`



To learn more about using GPUs on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## April 11, 2018

Feature

  * [Nested Virtualization](https://docs.cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances) is now **Generally Available**.



Feature

  * You can now run simulated maintenance events to test the effects of live migration, termination, and preemption on your instances. Simulated maintenance events are available in **Beta**. Read [testing your availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies) to learn how to test maintenance events on your instances.



## March 28, 2018

Feature

  * You can import existing virtual disks (VMDKs, VHDs, etc) into Compute Engine as custom images. [Importing virtual disks](https://docs.cloud.google.com/compute/docs/images/importing-virtual-disks) is now **Generally Available**.



## March 23, 2018

Feature

  * You can import a Windows Server 2003 server to Compute Engine using the CloudEndure migration service. For steps, see [Migrating VMs to Compute Engine](https://docs.cloud.google.com/compute/docs/instances/migrating-vms-compute-engine).



## March 14, 2018

Feature

  * Creating an image from a snapshot is now **Generally Available**. See the [creating custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image) page.



## March 13, 2018

Feature

  * Added a third zone to the `europe-west4` region. This zone supports 96 vCPU high memory/high CPU machines. There is no support for local SSDs at this time. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information. For regional managed instance group users, the addition of a third zone in `europe-west4` offers you more flexibilty to specify zones in this region. Note that if you do not specify the zones for your instances, Compute Engine, by default, selects all three zones. See [Distributing Instances using Regional Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) to learn more.



## March 08, 2018

Feature

  * Added support for PTR records on VM instances to **General Availability**. See [Creating a PTR record for VM instances](https://docs.cloud.google.com/compute/docs/instances/create-ptr-record).



## March 07, 2018

Feature

  * You can import existing virtual disks (VMDKs, VHDs, etc) into Compute Engine as functioning images. [Importing virtual disks](https://docs.cloud.google.com/compute/docs/images/importing-virtual-disks) is available in **Beta**.



## March 02, 2018

Feature

  * [Mega-memory machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) with 1.4 TB of memory are now available in **Beta**. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.



## February 22, 2018

Feature

  * Creating multiple secondary non-boot disks when you [create your VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) is now available in Beta.



## February 09, 2018

Feature

  * [96 vCPU machine types](https://docs.cloud.google.com/compute/docs/machine-types) are **Generally Available**. These machine types are now available in several additional zones only on the Skylake platform. Read the list of [available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) to see where 96 vCPU machine types are available.



## February 01, 2018

Feature

  * Added support for [creating an instance template from a VM instance](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) into **Beta**. This feature can be used for instance duplication, backup, and recreation.



## January 31, 2018

Feature

  * You can filter Stackdriver monitoring metrics when you use them to configure autoscaling for your managed instance groups. [Filtering per-instance metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#filter_per_instance_metrics) is available in **Beta**.



Feature

  * Compute Engine supports [IAM Custom Roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles). Read the [IAM Custom Roles documentation](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) to learn more. You can identify which permissions are required to run Compute Engine methods in both the [V1 Compute Engine API reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1) and on the [Compute Engine IAM Permissions](https://docs.cloud.google.com/compute/docs/access/iam-permissions) page.



Feature

  * You can configure autoscaling for groups of instances based on a wider range of metrics, which allow you to scale managed instance groups on per-group metrics rather than average resource utilization across all of the instances in a group. [Autoscaling using per-group metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#per_group_metrics) is available in **Beta**.



## January 24, 2018

Feature

  * The OS Login API and key management feature is now **Generally Available**. You can associate your public SSH keys with your Google account or with individual member accounts in a Google Workspace organization or Cloud Identity organization. Read [Managing Instance Access](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) for more information.



## January 22, 2018

Feature

  * For NVIDIA® Tesla® K80 GPUs in the `asia-east1-a` and `us-east1-d` zones, you can create GPU instances with up to 416 GB of memory.



To learn more about the zones where GPUs are available, read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

## January 11, 2018

Feature

  * [VM Deletion Protection](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion) is now **Generally Available**.



## January 10, 2018

Feature

  * Added new `europe-west4` region. `europe-west4` contains Skylake zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



Feature

  * Added new `northamerica-northeast1` Montréal region. `northamerica-northeast1` contains Skylake zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## January 08, 2018

Feature

  * [Zonal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#zonal-dns) are available in **Beta**. Zonal DNS names are unique to each zone on your internal [VPC](https://docs.cloud.google.com/vpc/docs/vpc) networks. Global DNS names continue to resolve, but you can enable zonal DNS names to improve the fault tolerance of your applications when they reference instances on your internal VPC network. Read [Zonal DNS](https://docs.cloud.google.com/compute/docs/internal-dns#zonal-dns) to learn more.



## December 2017

**December 22, 2017**

* GPUs are now available in the following zones: 

  * NVIDIA® Tesla® P100 GPUs:
    * `us-central1-c`
    * `us-central1-f`
  * NVIDIA® Tesla® K80 GPUs:
    * `us-central1-c`

To learn more about the zones where GPUs are available, read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus/). 

**December 14, 2017**

  * The OS Login API accepts connections from users who have the Owner or Editor [basic roles](https://docs.cloud.google.com/compute/docs/access#basic-iam-roles). Read [Managing SSH keys using the OS Login API](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) to learn more about using OS Login to manage authentication and authorization on Compute Engine instances.



**December 13, 2017**

  * Added support for [Preventing VM Deletion](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion).



**December 06, 2017**

  * Added support for [creating a VM instance from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template) into **Beta**.



## November 2017

**November 21, 2017**

  * Added support for specifying a static internal IP to **General Availability**. See [Reserving a Static Internal IP Address](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address)



**November 16, 2017**

  * [Deploying Docker Containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/deploying-containers) is now available in **Beta**.



**November 15, 2017**

  * Effective today, the Skylake platform no longer incurs a premium charge. Prices for 96 vCPU machine types have been updated to reflect the removal of the Skylake premium. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#n1_predefined) for more information.



**November 13, 2017**

  * Launched new [mega-memory machine types](https://docs.cloud.google.com/compute/docs/machine-types#megamem) to private **Beta**. See the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed.



**November 06, 2017**

  * The User Accounts service (previously in Beta) is being discontinued and will stop being supported on February 15, 2018. It is recommended that users transition to the [OS Login API](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) in place of the User Accounts service.

  * Added support for viewing autoscaler logs into **Beta**. See [Viewing Autoscaler Logs](https://docs.cloud.google.com/compute/docs/autoscaler/viewing-autoscaler-logs) for more information.

  * Windows Server for Containers is now available in **Beta** as a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support).




**November 01, 2017**

  * You can associate PTR records with the primary network interface on your instance. Support for PTR records on VM instances is available in **Beta**. Read [Creating a PTR record for VM instances](https://docs.cloud.google.com/compute/docs/instances/create-ptr-record) to learn more.



## October 2017

**October 31, 2017**

  * Added new `asia-south1` Mumbai region. `asia-south1` contains Skylake zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



**October 30, 2017**

  * Windows Server, version 1709 is now **Generally Available** as a [public image](https://docs.cloud.google.com/compute/docs/images). This is a Server Core image that is part of the [semi-annual release cycle](https://docs.microsoft.com/windows-server/get-started/semi-annual-channel-overview) for Windows Server. Use these images to access newer Windows Server features that are not available in the Long-term Servicing Channel releases.

  * [SQL Server 2017 images](https://docs.cloud.google.com/compute/docs/instances/windows#sql_server) are now available. These images include Windows Server 2016 with SQL Server 2017 preinstalled.




**October 26, 2017**

  * Launched new [`roles/computeViewer`](https://docs.cloud.google.com/compute/docs/access/iam) roles to **General Availability**. For more information on IAM roles, read the Compute Engine [IAM documentation](https://docs.cloud.google.com/compute/docs/access/iam).



**October 19, 2017**

  * You can associate your public SSH keys with your Google account or with individual member accounts in a G Suite organization. When you connect to an instance, those public keys are automatically sent to instances where you have the necessary roles or permissions. This method is an alternative to managing your SSH key pairs in project or instance metadata. This feature is in **Beta**. Read [Managing Instance Access](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) for more information.



**October 18, 2017**

  * Launched support for [Specifying a Minimum CPU Platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) to **General Availability**.



**October 13, 2017**

  * Added support for sizing recommendations for managed instance groups to **Beta**. See [Applying Sizing Recommendations for Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/apply-sizing-recommendations-managed-instance-groups) for more information.



**October 12, 2017**

  * You can now copy images from other images, including images that are shared from other Cloud Platform projects. This feature is **Generally Available**. To learn how to copy images from these sources, see [Creating Custom Images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images).



**October 05, 2017**

  * Added support for [disabling external IPs for VM instances](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#disableexternalip) using Organization Polices to **General Availability**.

  * Launched new [`roles/compute.admin`](https://docs.cloud.google.com/compute/docs/access/iam) roles to **General Availability**. For more information on IAM roles, read the Compute Engine [IAM documentation](https://docs.cloud.google.com/compute/docs/access/iam).

  * [96-vCPU machine types](https://docs.cloud.google.com/compute/docs/machine-types) are now available in **Beta** on VM instances in specific zones. 96-vCPU machine types can run only on the Skylake platform. Read the list of [available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) to see where 96-vCPU machine types are available.




**October 02, 2017**

  * Added support for selecting specific zones for regional managed instance groups into **Beta**. See [Distributing Instances using Regional Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selecting_zones)



## September 2017

**September 28, 2017**

  * Added support for [Nested Virtualization](https://docs.cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances) into **Beta**.



**September 27, 2017**

  * NVIDIA® Tesla® P100 GPUs are now available in the `europe-west1-d` zone in addition to the previously announced zones. Read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) to learn more about the zones where P100 GPUs are available.

  * NVIDIA® Tesla® K80 GPUs are now available in the `asia-east1-b` zone in addition to the previously announced zones. Read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) to learn more about the zones where GPUs are available.




**September 26, 2017**

  * Billing increments for Compute Engine virtual machine instances are reduced from per-minute increments to per-second increments. Additionally, the minimum usage cost for these resources is reduced from 10 minutes to 1 minute. Read the [Compute Engine billing model](https://docs.cloud.google.com/compute/vm-instance-pricing#billingmodel) page for details.



**September 21, 2017**

  * NVIDIA® Tesla® P100 GPUs are now available in **Beta**. Read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) to learn more about the zones where P100 GPUs are available.

  * NVIDIA® Tesla® K80 GPUs are now **Generally Available**. Read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) to learn more about the zones where GPUs are available.




**September 19, 2017**

  * Instance identity verification is now **Generally Available** for all users and projects. Read [Verifying the Identity of Instances](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity) to learn how to request and verify signed instance tokens.



**September 13, 2017**

  * Committed Use Discounts are now **Generally Available**. To learn more, read the documentation for [Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).



**September 11, 2017**

  * The Compute Engine Trusted Images policy is now available in **Beta**. Use this policy to control which boot disk images your project members can access. Read [Restricting Access to Images](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) for more information.



**September 05, 2017**

  * Managed Instance Group Updater is now available in **Beta**. Read [Updating Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) for more information.

  * Added new `southamerica-east1` region. `southamerica-east1` contains Broadwell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.




## August 2017

**August 28, 2017**

  * Launched audit logging for Compute Engine to **General Availability**. For more information, read [Viewing Audit Logs](https://docs.cloud.google.com/compute/docs/audit-logging).



**August 25, 2017**

  * Launched new [`roles/compute.admin` and `roles/compute.viewer`](https://docs.cloud.google.com/compute/docs/access/iam) roles to **Beta**. For more information on IAM roles, read the Compute Engine [IAM documentation](https://docs.cloud.google.com/compute/docs/access/iam).



**August 21, 2017**

  * The Skylake Platform is now available in zones in the following regions: `us-central1`, `europe-west1`, `asia-east1`, `us-east1` and `asia-southeast1`. For a detailed list of zones that support Skylake, see the [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) documentation.



**August 17, 2017**

  * You can now create [custom images](https://docs.cloud.google.com/compute/docs/images#custom_images) from disks even while they are attached to instances. If necessary, you can create images while the instance is running. Read [Creating Custom Images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image) to learn more.



**August 11, 2017**

  * Added support for specifying a static internal IP to **Beta**. See [Reserving a Static Internal IP Address](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address) for more information.



**August 08, 2017**

  * Introduced new preemptible pricing for local SSD and lowered normal local SSD by up to 63%. For more information, see the [Pricing](https://docs.cloud.google.com/compute/disks-image-pricing#localssdpricing) documentation.



**August 04, 2017**

  * Added support for newer-style health checks that support TCP, SSL, HTTP, and HTTPS health checking to [managed instance group autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).



**August 02, 2017**

  * Launched audit logging for Compute Engine to **Beta**. For more information, read [Viewing Audit Logs](https://docs.cloud.google.com/compute/docs/audit-logging).



**August 01, 2017**

  * Added new `europe-west3` region. `europe-west3` contains Broadwell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## July 2017

**July 27, 2017**

  * You can now use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/downloads) to [connect to instances without external IP addresses](https://docs.cloud.google.com/compute/docs/instances/connecting-advanced#sshbetweeninstances). This feature is available in **Beta**.



**July 20, 2017**

  * Extended memory is now available in **general availability**. For more information, read [Adding extended memory to a machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory).



## June 2017

**June 28, 2017**

  * Instances with service accounts can now request JSON Web Tokens from their metadata servers. Your applications can use these tokens to verify the identity of an instance before transmitting data to the instance. Read [Verifying the Identity of Instances](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity) to learn how to request and verify signed instance tokens. This feature is available in **Beta**.



**June 23, 2017**

  * The [Skylake Platform](https://docs.cloud.google.com/compute/docs/regions-zones#available) is now available in the `us-central1-a` and `us-central1-b` zones.



**June 21, 2017**

  * [TCP Proxy Load Balancing](https://docs.cloud.google.com/compute/docs/load-balancing/tcp-ssl/tcp-proxy) is now **generally available** for all users and projects.

  * You can now copy images from other images and images that are shared from other Cloud Platform projects. This feature is available in **Beta**. To learn how to copy images from these sources, see [Creating Custom Images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images).




**June 20, 2017**

  * Added new `australia-southeast1` region. `australia-southeast1` contains Broadwell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



**June 19, 2017**

  * [Audit logging for the serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console#viewing_serial_console_logs) is now available in **General Availability**.



**June 14, 2017**

  * The ability to [change the service account identity and access scopes](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) for a VM instance is now **generally available**.



**June 07, 2017**

  * [Shared VPC](https://docs.cloud.google.com/compute/docs/shared-vpc) (Previously Cross-Project Networking (XPN)) is now available in **General Availability**.

  * NVIDIA® Tesla® K80 GPUs are now available in **Beta** in the `us-east1-c` and `europe-west1-d` zones. Read about [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) to learn more about the zones where GPUs are available.




**June 06, 2017**

  * Added new `europe-west2` region. `europe-west2` contains Broadwell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## May 2017

**May 31, 2017**

  * Launched new [Skylake Platform](https://docs.cloud.google.com/compute/docs/regions-zones#available) into **General Availability**.

  * Launched new feature for [Specifying a Minimum CPU Platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) to **Beta**.

  * Launched new [Extended Memory for Custom Machine Types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory) into **Beta**.




**May 30, 2017**

  * Added new zone, `us-west1-c`. See the [Zones and Region](https://docs.cloud.google.com/compute/docs/regions-zones#available) documentation for more details.



**May 25, 2017**

  * [Labels](https://docs.cloud.google.com/compute/docs/labeling-resources) are now available in **general availability**.



**May 15, 2017**

  * [SLES for SAP](https://www.suse.com/products/sles-for-sap/) images are now available as [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support). These images are optimized for SAP applications.



**May 11, 2017**

  * Server Core for Windows Server [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) are reduced in size from 50GB to 32GB to reduce the boot disk costs for your instances. By default, these images create boot persistent disks that are 32GB in size. If you require larger boot disks, specify a larger boot disk size when you create your instances or [resize the boot persistent disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk).



**May 09, 2017**

  * Added new `us-east4` region. `us-east4` contains Broadwell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



**May 01, 2017**

  * [64-vCPUs machine types](https://docs.cloud.google.com/compute/docs/machine-types) are now **Generally Available** to all users and projects.

  * Decoupled labels and tags so that creating either a label or a tag will not create the opposing resource. For example, creating a label will no longer create a tag and vice-versa. For more information, read [Relationship between instance labels and network tags](https://docs.cloud.google.com/compute/docs/labeling-resources#labels_tags).

You can now find information about network tags in the [Networking](https://docs.cloud.google.com/compute/docs/vpc/add-remove-network-tags) documentation.




## April 2017

**April 28, 2017**

  * [Ubuntu 17.04 Zesty Zapus](https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes) is available as a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). You can use this image to [create instances](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage).
  * [Ubuntu 12.04 Precise Pangolin](https://wiki.ubuntu.com/PrecisePangolin/ReleaseNotes) is no longer available as a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). Optionally, you can [upgrade instances](https://help.ubuntu.com/lts/serverguide/installing-upgrading.html) that run Ubuntu 12.04 to a newer Ubuntu LTS version.



**April 27, 2017**

  * Added an API for [listing references between resources](https://docs.cloud.google.com/compute/docs/instances/view-references-between-resources) into **Beta**.



**April 24, 2017**

  * Added support for [disabling external IPs for VM instances](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#disableexternalip) using Organization Polices to **Beta**.



**April 19, 2017**

  * Created project quota limits that apply to [All Regions](https://docs.cloud.google.com/compute/quotas#cpus).



**April 12, 2017**

  * Added new `asia-southeast1` region. `asia-southeast1` contains Broadwell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.

  * [Egress firewall rules](https://docs.cloud.google.com/compute/docs/firewalls) are now available in **Beta** to all users and projects.




**April 07, 2017**

  * Added support for [updating managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) to the [Google Cloud console](https://console.cloud.google.com/).



**April 05, 2017**

  * [TCP proxy load balancing](https://docs.cloud.google.com/compute/docs/load-balancing/tcp-ssl/tcp-proxy) is now available in **Beta** to all users and projects.



## March 2017

**March 28, 2017**

  * Added Debian 9 'Stretch' testing image to `debian-cloud-testing` project. For more information, see the [Debian Testing](https://docs.cloud.google.com/compute/docs/images#debian_testing) documentation.



**March 24, 2017**

  * Added support for [disabling interactive serial console access](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console#disabling_interactive_serial_console_access_through_organization_policy) using Organization Polices into **Beta**.



**March 21, 2017**

  * NVIDIA® Tesla® K80 GPUs are now available in **Beta** in the `us-west1-b` zone. Read about [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) to learn more about the zones where GPUs are available.



**March 09, 2017**

  * Launched new [Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) feature into Beta, which allows you to purchase committed use contracts in return for deeply discounted prices for VM usage. To learn more, read the documentation for [Signing Up for Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

  * Lowered prices for [predefined machine types](https://docs.cloud.google.com/compute/vm-instance-pricing#n1_predefined) and [custom machine types](https://docs.cloud.google.com/compute/vm-instance-pricing#custommachinetypepricing). Preemptible VM prices remain unchanged.




**March 07, 2017**

  * SSD persistent disks now have increased throughput and IOPS performance, which are particularly beneficial for database and analytics workloads. Instances with 32 vCPUs provide up to 40k read IOPS and 30k write IOPS as well as 800 MB/s of read throughput and 400 MB/s of write throughput. Instances with 16 - 31 vCPUs provide up to 25k read or write IOPS, 480 MB/s of read throughput, and 240 MB/S of write throughput. For complete details about persistent disk performance limits, read [Persistent Disk Performance](https://docs.cloud.google.com/compute/docs/disks/performance).

  * Simultaneous reads and writes on SSD persistent disks no longer share the same throughput limits. SSD persistent disks can simultaneously read and write at their individual advertised throughput limits. For more information about simultaneous read and write capabilities, read [Persistent Disk Performance](https://docs.cloud.google.com/compute/docs/disks/performance#simultaneous-read-write) for details.




**March 07, 2017**

  * [Cross-Project Networking (XPN)](https://docs.cloud.google.com/compute/docs/xpn) is now available in **Beta** to all users and projects.



**March 06, 2017**

  * SQL Server Enterprise Edition images are now generally available. You can use these [Public Images](https://docs.cloud.google.com/compute/docs/images#application_images) to run SQL Server Enterprise Edition on various versions of Windows Server. Additionally, you can use SQL Server Enterprise on Compute Engine to [create SQL Server Availability Groups](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability).

  * Volume Shadow Copy Service (VSS) snapshots for persistent disks are now generally available. Use VSS snapshots to [create snapshots of persistent disks](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot) on Windows instances without detaching the disk or stopping the instance.




**March 03, 2017**

  * [64-core machine types](https://docs.cloud.google.com/compute/docs/machine-types) are now available in **Beta** to all users and projects.



## February 2017

**February 21, 2017**

  * Launched new [`roles/compute.instanceAdmin.v1`](https://docs.cloud.google.com/compute/docs/access/iam) role to General Availability. For more information on IAM roles read the Compute Engine [IAM documentation](https://docs.cloud.google.com/compute/docs/access/iam).



**February 17, 2017**

  * NVIDIA® Tesla® K80 GPUs are now available on Compute Engine in **Beta**. Attach one or more of these GPUs to your instances to accelerate specific workloads and offload tasks from your vCPUs. [Add GPUs to your instances](https://docs.cloud.google.com/compute/docs/gpus/add-gpus) or read about [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) to learn more.



**February 14, 2017**

  * Launched the Compute Engine Image Sharing role, `compute.imageUser`, to General Availability. For more information, read [Sharing Images Across Projects](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects).



## January 2017

**January 30, 2017**

  * Launched new [VM Migration Service](https://docs.cloud.google.com/compute/docs/tutorials/migrating-vms-compute-engine) to help users migrate VMs into Compute Engine.



**January 18, 2017**

  * SQL Server Enterprise Edition images are now available in **Beta**. You can use these [Public Images](https://docs.cloud.google.com/compute/docs/images#application_images) to run SQL Server Enterprise Edition on various versions of Windows Server. Additionally, you can use SQL Server Enterprise on Compute Engine to [create SQL Server Availability Groups](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability).

  * Server Core for Windows Server 2016 and Server Core for Windows Server 2012 R2 are now available as [public images](https://docs.cloud.google.com/compute/docs/images). Use these images to run Windows Server on smaller instances, to save boot disk space, or to run applications that do not require the complete Desktop Experience.




**January 04, 2017**

  * The size limit for [importing boot disk images](https://docs.cloud.google.com/compute/docs/images/import-existing-image) increased from 100GB to 2048GB (2TB). See [image import requirements](https://docs.cloud.google.com/compute/docs/images/import-existing-image#requirements) for details.



**January 03, 2017**

  * Added support for autoscaling charts into the Google Cloud console. Read [Viewing autoscaling charts for CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#viewing_autoscaling_charts_for_cpu_utilization) for more information.



## December 2016

**December 15, 2016**

  * [Interacting with the Serial Console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console) is now generally available.



**December 14, 2016**

  * Added the [ability to change the service account and scopes](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) assigned to an instance to **Beta**.

  * It is now possible to view audit logs for the serial console. For more information, see [Viewing serial console logs](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console#viewing_serial_console_logs).




## November 2016

**November 22, 2016**

  * Container-VM Image is now called Container-Optimized OS from Google. Container-VM Image has been renamed to Container-Optimized OS to better reflect its focus on container technology and the value it provides. Learn more at [Container-Optimized OS from Google Documentation](https://docs.cloud.google.com/container-optimized-os/docs)



**November 21, 2016**

  * Volume Shadow Copy Service (VSS) snapshots for persistent disks are now available in **Beta**. Use VSS snapshots to [create snapshots of persistent disks](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot) on Windows instances without detaching the disk or stopping the instance.



**November 18, 2016**

  * Launched [Regional Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) into **General Availability**.



**November 07, 2016**

  * Added new `asia-northeast1` region. `asia-northeast1` contains Broadwell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.

  * Launched new IAM role, `roles/compute.imageUser`, into **Beta** , which allows users to get, list, and use images from another project. For more information, read [Sharing Images Across Projects](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects).




**November 01, 2016**

  * [Customer-Supplied Encryption Keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) are now available in the following additional countries: 
    * Belgium
    * Colombia
    * Finland
    * Ireland
    * Netherlands
    * New Zealand



## October 2016

**October 26, 2016**

  * Released a security bulletin about [CVE-2016-5195](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails). See [Security Bulletins](https://docs.cloud.google.com/compute/docs/security-bulletins) for more information.



**October 17, 2016**

  * Windows Server 2016 and Windows SQL Server 2016 on Windows Server 2016 are now available as [Public Images](https://docs.cloud.google.com/compute/docs/images). You can use these images to [create Windows instances](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances).



**October 14, 2016**

  * Launched a new autoscaling feature that supports [queue-based autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-queue-based) into **Alpha**. You can request access to the feature on the [documentation](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-queue-based).



## September 2016

**September 29, 2016**

  * [SQL Server images](https://docs.cloud.google.com/compute/docs/instances/windows#sql_server) are now **generally available**. These images include Windows Server with SQL Server preinstalled. The price for SQL Server images includes the licensing cost for SQL Server. This allows you to pay for SQL Server only when you use it with pay as you go billing on a per-minute basis. See the cost for these SQL Server images on the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#sql_server_pricing).



**September 19, 2016**

  * Added support for new [preemptible CPU quotas](https://docs.cloud.google.com/compute/docs/instances/create-start-preemptible-instance#preemptible_cpu_quotas).



**September 14, 2016**

  * Launched new [Instance Group Updater](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) into **Alpha**.
  * Deprecated [previous Instance Group Updater API](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#starting_an_update). Users should transition to using the new [Instance Group Updater API](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) instead.



**September 12, 2016**

  * Instances with 3 TB of total local SSD space are **generally available**. You can create instances with eight [local SSD devices](https://docs.cloud.google.com/compute/docs/disks/local-ssd) for a total 3 TB of local SSD storage space. See [Local SSD limits](https://docs.cloud.google.com/compute/docs/disks#local_ssd_limits) for available zones and machine types.



**September 08, 2016**

  * Added new `guestOsFeatures` property into Beta, which lets you enable certain guest OS features for your images. For more information, see the documentation for [guestOsFeatures](https://docs.cloud.google.com/compute/docs/reference/beta/images#guestOsFeatures).



## August 2016

**August 16, 2016**

  * [SQL Server images](https://docs.cloud.google.com/compute/docs/instances/windows#sql_server) are now available in **Beta**. These images include Windows Server with SQL Server preinstalled. The price for SQL Server images includes the licensing cost for SQL Server. This allows you to pay for SQL Server only when you use it with pay as you go billing on a per-minute basis. See the cost for these SQL Server images on the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#sql_server_pricing).



**August 12, 2016**

  * [SSD persistent disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs) now have improved IOPS performance. Instances with 16 or more cores can achieve 20,000 IOPS, and instances with 32 vCPUs can achieve 25,000 IOPS with SSD persistent disks of a sufficient size. See the [persistent disk performance](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison) page for details.



**August 09, 2016**

  * Lowered prices of preemptible virtual machine instances for predefined and custom machine types. To see the new pricing, see the pricing table for [machine types](https://cloud.google.com/products/compute/pricing).



## July 2016

**July 21, 2016**

  * [Virtual machine sizing recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-sizing-recommendations-for-instances) are now available in **Beta**.



**July 20, 2016**

  * The `us-west1` region is now available, and offers Broadwell zones `us-west1-a` and `us-west1-b`. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.

  * [Regional managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) are now available in **Beta**. You can use regional managed instance groups to distribute instances across multiple zones in a region and improve your application availability.




**July 1, 2016**

  * Shutdown Scripts are now **generally available** to use with Compute Engine instances. Shutdown scripts allow users to execute commands, on a best-effort basis, right before an instance is terminated or restarted. For more information, see [Running Shutdown Scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).



## June 2016

**June 29, 2016**

  * Protect data on Compute Engine with your own encryption keys. [Customer-Supplied Encryption Keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) are now **generally available** for select countries. You can now also [stop an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) with a persistent disk that is encrypted with your own key. Compute Engine is able to restart your instance if you provide the key.



**June 27, 2016**

  * Released a new feature into **Beta** where you can enable interactive access to the serial console so you can more easily troubleshoot instances that are not booting properly or that are otherwise inaccessible. See [Interacting with the Serial Console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console) for more information.



**June 20, 2016**

  * Fixed a bug with how Compute Engine accounts for and computes the metric used to create CPU usage graphs shown in the [Google Cloud console](https://console.cloud.google.com/) VM Instances page and Instance Details page. These graphs should now report CPU usage numbers much closer to the CPU usage inside the guest, and should match numbers reported by guest tools like `top` and `uptime`.



**June 14, 2016**

  * The metadata server has been updated so that it only gives a 60 second advance notice before a maintenance event if you have queried for the `maintenance-event` attribute of that instance at least once since the last migration. Otherwise, Compute Engine assumes that you do not need advance notice of maintenance events and will not provide a notice 60 seconds before an imminent maintenance event. To learn more about the `maintenance-event` attribute, read the [Getting transparent maintenance notices](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#maintenanceevents) section.

  * You can now [specify an instance's internal IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#assigninternalip) at instance creation.




**June 09, 2016**

  * The Debian 7 images and Debian 7 backports images are deprecated. Use the latest [Debian 8 public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support) to create new instances or [upgrade your Debian 7 instances](https://www.debian.org/releases/jessie/) to Debian 8. If you still require Debian 7, see the [advisory](https://groups.google.com/forum/#!topic/gce-discussion/eMYFdtVvWK0) message.

  * CentOS, Debian, and RHEL images version v20160606 or newer now include a new guest environment with the following significant changes:

    * Linux guest software is installed from, and hosted in, a Google Cloud repository, and is updateable with standard package management tools such as `apt` or `yum`.
    * Images no longer contain the deprecated `gcimagebundle` tool. If you need to create image file from a Compute Engine instance, use the instructions for [Exporting an Image to Google Cloud Storage](https://docs.cloud.google.com/compute/docs/images/export-image).
    * Debian images include `unattended-upgrades` for security updates. Security updates are installed daily by default.
    * Debian images install Google Cloud CLI from a deb package hosted in a Google Cloud repository. You can update the gcloud CLI in Debian using the `apt-get update; apt-get dist-upgrade` command instead of the `gcloud components update` command.
    * Debian images automatically expand boot disk partitions up to 2 TB regardless of the boot disk size. Previously, if your disk was over 2 TB, Debian images would not expand the boot disk at all.
    * Debian images include a compiled `python-crcmod` library so that composite objects in Google Cloud Storage work correctly with `gsutil`.
  * The new Linux guest environment is published in the [GoogleCloudPlatform/compute-image-packages](https://github.com/GoogleCloudPlatform/compute-image-packages) repo on GitHub.




## May 2016

**May 11, 2016**

The following Compute Engine IAM roles are now generally available:

  * `roles/compute.networkAdmin`
  * `roles/compute.securityAdmin`
  * `roles/iam.serviceAccountUser`



For more information, read the [IAM](https://docs.cloud.google.com/compute/docs/access/iam) documentation.

## April 2016

**April 28, 2016**

  * Images can now be organized into image families for easier management and use. Image families point to the latest version of an operating system image that is not marked as deprecated. [Create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) by specifying an image family with one of the available [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support). To organize your own images into image families, [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images).



**April 21, 2016**

  * The Ubuntu 16.04 LTS [Xenial Xerus](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) image is available.



**April 5, 2016**

  * [Health checking](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) is available in **Beta** for managed instance groups. Use [health checking](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) to automatically identify and recreate failing instances in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups).



**April 4, 2016**

  * You can now attach more than 16 unique persistent disks to an instance with a [predefined machine type](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types). Total persistent disk space per instance is still limited to 64 TB. The number of disks depends on the number of vCPUs that the instance has. This feature is available in **Beta**. See [disk number limits](https://docs.cloud.google.com/compute/docs/disks#pdnumberlimits) for details.



**April 01, 2016**

  * Added support for [labeling disks, snapshots, and images](https://docs.cloud.google.com/compute/docs/label-or-tag-resources) into **Beta**.



## March 2016

**March 30, 2016**

  * [Resizeable persistent disks](https://docs.cloud.google.com/compute/docs/disks#resize_pd) are now **generally available** to all users and projects. You can increase the size of existing persistent disks even while they are attached to running VM instances.
  * Persistent disks larger than 10 TB are **generally available**. You can now [create](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk) or [resize](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#resize_pd) persistent disks to be up to 64 TB in size. Persistent disks larger than 10 TB can be attached only to [specific machine types](https://docs.cloud.google.com/compute/docs/disks#pdlimits).



**March 24, 2016**

  * Launched [virtual machine sizing recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-sizing-recommendations-for-instances) into **Alpha**.



**March 15, 2016**

  * Launched [regional managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) into **Alpha**.



**March 10, 2016**

  * Launched Compute Engine IAM roles into **Beta**. [Learn more about Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

  * Added support for [custom service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts) into **Beta**.




**March 7, 2016**

  * Updated the way that SSH keys work in project metadata and instance metadata. If you manage SSH keys manually, [use the new metadata values](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys).



## February 2016

**February 23, 2016**

  * Added a requirement that account owners who are enabled for [user accounts](https://docs.cloud.google.com/compute/docs/access/user-accounts) must also be granted permission to act as a service account before they can connect to instances that are enabled for service accounts. Read the [documentation](https://docs.cloud.google.com/compute/docs/access/user-accounts#create_a_new_user_account) for more information.



**February 17, 2016**

  * Custom machine types are now **generally available** to all projects and users. [Learn more about custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).



**February 16, 2016**

  * Released a security bulletin about [CVE-2015-7547](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html). See [Security Bulletins](https://docs.cloud.google.com/compute/docs/security-bulletins) for more information.



**February 10, 2016**

  * Launched support for [changing the machine type of a stopped instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) into **General Availability**.



**February 05, 2016**

  * [OpenSUSE Leap 42 images](https://docs.cloud.google.com/compute/docs/images) are now available to all users and projects starting with image opensuse-leap-42-1-v20160202.



## January 2016

**January 29, 2016**

  * You can now attach up to eight [local SSD devices](https://docs.cloud.google.com/compute/docs/disks/local-ssd) to each of your instances for a total of 3 TB of local SSD space per instance. Attaching more than 1.5 TB of local SSD space to a single instance is a **Beta** feature and is available only in some zones. See [Local SSD limits](https://docs.cloud.google.com/compute/docs/disks#local_ssd_limits) for details.



## December 2015

**December 17, 2015**

  * Persistent disks larger than 10 TB are in **Beta**. You can now create disks up to 64 TB in size. Persistent disks larger than 10 TB can be attached only to [specific machine types](https://docs.cloud.google.com/compute/docs/disks#increased_persistent_disk_limits).
  * You can [resize persistent disks](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#resize_pd) to provide more disk space and throughput to your instances. This feature is now available in **Beta**.



## November 2015

**November 18, 2015**

  * Launched support for [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) into **Beta**.



**November 13, 2015**

  * Updated the [resource quotas](https://docs.cloud.google.com/compute/quotas) page to reflect that quotas are now listed on the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.



**November 12, 2015**

  * Launched support for [changing the machine type of a stopped instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) into **Beta**.



## October 2015

**October 15, 2015**

  * Launched [Instance Labels](https://docs.cloud.google.com/compute/docs/label-or-tag-resources#labeling_resources) into **Beta**.
  * Added support for filtering on nested fields in the Compute Engine [Beta API](https://docs.cloud.google.com/compute/docs/reference/beta/instances/list#filter).



**October 09, 2015**

  * Added support for using [Mailgun](http://mailgun.com) to [send email](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailgun).



**October 05, 2015**

  * Updated [activity logs](https://docs.cloud.google.com/compute/docs/activity-logs) so that the log data contains a `structPayload` in JSON format instead of a `textPayload` in protobuf format. See [examples](https://docs.cloud.google.com/compute/docs/activity-logs#sample_log_entry) in the [Activity Logs documentation](https://docs.cloud.google.com/compute/docs/activity-logs) for more information.



**October 01, 2015**

  * Added new us-east1 region. us-east1 contains Haswell zones that are now available to all projects and users. See [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.



## September 2015

**September 30, 2015**

  * The [User Accounts](https://docs.cloud.google.com/compute/docs/access/user-accounts) service is now available in **Beta**. Updates include: 
    * Release of new `beta-accounts..` images that have user accounts enabled.
    * Update to [quota](https://docs.cloud.google.com/compute/docs/access/user-accounts#quotas) limits.



**September 08, 2015**

  * [Preemptible instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) are now *_Generally Available_ to all users and projects.



**September 03, 2015**

  * [32-vCPUs machine types](https://docs.cloud.google.com/compute/docs/machine-types) are now **Generally Available** to all users and projects.
  * [Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups) and [Autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler) are now **Generally Available** to all users and projects.



## July 2015

**July 28, 2015**

  * [Debian 8 images](https://docs.cloud.google.com/compute/docs/images#debian) are now available to all users and projects starting with debian-8-jessie-v20150710.
  * Protect data on Compute Engine with your own encryption keys. The [Customer-Supplied Encryption Keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) feature is now available in **Beta** for select countries.



**July 15, 2015**

  * Updated the [User Accounts API](https://docs.cloud.google.com/compute/docs/access/user-accounts/api/latest) to use a new API endpoint:
        
        https://www.googleapis.com/clouduseraccounts/alpha/...
        




**July 14, 2015**

  * [Windows images](https://docs.cloud.google.com/compute/docs/images#windows) are now generally available to all users and projects. Commands for managing Windows instances are no longer in beta.



**July 01, 2015**

  * Released new Windows images, **20150629** , that supports [service account scopes](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#tools). This removes the restriction that users must make their startup script publicly-accessible for Windows instances.
  * Added new Python and Java script that can programmatically reset a Windows password. See [Progammatically generate a username and password](https://docs.cloud.google.com/compute/docs/instances/automate-pw-generation) for more information.



## June 2015

**June 29, 2016**

  * Updated the [User Accounts service](https://docs.cloud.google.com/compute/docs/access/user-accounts#restrictions) to support the latest Ubuntu images.



**June 03, 2015**

  * Updated Windows authentication process. Windows images v20150511 and later will use the new scheme by default. `gcloud` will now generate a random password for Windows login; it is no longer possible to manually set a Windows password through `gcloud` but you can set a custom password in the instance.



## May 2015

**May 18, 2015**

  * Added preemptible instances that you can create and run at a much [lower price](https://cloud.google.com/products/compute/pricing) than normal instances. For more information about how to use these instances in your Compute Engine project, see the [preemptible instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) documentation.
  * Lowered the price of all machine types in all locations. For more information, see the [pricing page](https://cloud.google.com/products/compute/pricing).



**May 13, 2015**

  * Removed support for running `sysprep-oobe-script-*` startup scripts on Windows virtual machines. We recommend using `windows-startup-script-*` keys as replacements. For more information, see [Startup scripts](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances).



**May 08, 2015**

  * Added documentation for configuring [network time protocol (NTP)](https://docs.cloud.google.com/compute/docs/instances/configure-ntp) on virtual machine instances. Make sure you adjust your NTP settings before the upcoming leap second on June 30th, 2015**.



**May 04, 2015**

  * Updated [activity logs](https://docs.cloud.google.com/compute/docs/activity-logs) so that the format of the log data is provided in [protobuf](https://github.com/google/protobuf) rather than JSON. See [examples](https://docs.cloud.google.com/compute/docs/activity-logs#sample_log_entry) in the [Activity Logs documentation](https://docs.cloud.google.com/compute/docs/activity-logs) for more information.



## April 2015

**April 30, 2015**

  * Added new [User Accounts](https://docs.cloud.google.com/compute/docs/access/user-accounts) feature, available in **Alpha**. User accounts allow you to create Linux user accounts for your virtual machines.



**April 29, 2015**

  * Released instance [`stop()`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/stop) and [`start()`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/start) features into **General Availability**. Additionally, stopped instances no longer count towards your CPU resource quotas. See [Stopping an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance) and [Restarting a stopped instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance) for more information.
  * Upgraded us-central1-b to use [Haswell](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29) processors. All new virtual machines started in us-central1-b will use Haswell processors by default. Existing instances in us-central1-b have been upgraded from Sandy Bridge to Haswell processors. See [Zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) and [Machine Types](https://docs.cloud.google.com/compute/docs/machine-types) for a full list of available zones and processors.



**April 27, 2015**

  * Released new Ubuntu 15.04 [Vivid Vervet](https://wiki.ubuntu.com/VividVervet/ReleaseNotes) images. See [Operating Systems](https://docs.cloud.google.com/compute/docs/images#ubuntu) for more information.



**April 23, 2015**

  * Added location information about Compute Engine regions. To see specific geographic location of regions, see the [Regions & Zones](https://docs.cloud.google.com/compute/docs/regions-zones) documentation.
  * Added support for [autoscaling with multiple policies](https://docs.cloud.google.com/compute/docs/autoscaler/multiple-policies).



## March 2015

**March 30, 2015**

  * Removed europe-west1-a zone, which was deprecated on October 15, 2014.



**March 25, 2015**

  * Added [shutdown script support on Windows](https://docs.cloud.google.com/compute/docs/images#windows) for Windows images *_v20150310_ or later.



**March 19, 2015**

  * [Windows Server 2012 R2](https://docs.cloud.google.com/compute/docs/images#windows) is now available in **Beta** to all users and projects.
  * Released a security bulletin about [CVE-2015-1427](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427). See [Security Bulletins](https://docs.cloud.google.com/compute/docs/security-bulletins) for more information.



**March 13, 2015**

  * Released the RHEL 7.1 image, `rhel-7-v20150311`. For a full list of new features , see the [RHEL 7.1 Release Notes](https://access.redhat.com/documentation/Red_Hat_Enterprise_Linux/7/html/7.1_Release_Notes/index.html). To use the new image on Compute Engine, see [Using RHEL 7 images](https://docs.cloud.google.com/compute/docs/images#rhel).
  * For RHEL 7.1 images, Red Hat provides the Kubernetes package to help you manage your containers.



**March 12, 2015**

  * Added new us-central1-c zone. us-central1-c zone is a Haswell zone that is now available to all projects and users. For more information, see [Zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * Released new [Activity Logs](https://docs.cloud.google.com/compute/docs/activity-logs) feature in **Beta** as part of the [Cloud Logging service](https://docs.cloud.google.com/logging).



**March 11, 2015**

  * Added new 32-core machine types in **Beta**. For more information and pricing, see [Machine Types](https://docs.cloud.google.com/compute/docs/machine-types) and [Pricing](https://cloud.google.com/products/compute/pricing).



**March 05, 2015**

  * Released new [`moveInstance()`](https://docs.cloud.google.com/compute/docs/reference/latest/projects/moveInstance) feature that moves an instance and its attached disks to another zone. See [Moving an instance between zones](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) for more information.
  * VPN is now available in **Beta**. For more information, see the [VPN documentation](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).



## February 2015

**February 20, 2015**

  * Removed the limit on number of API requests per day for all projects. See [API rate limits](https://docs.cloud.google.com/compute/docs/api-rate-limits) for more information.



**February 19, 2015**

  * Added new europe-west1-d zone. europe-west1-d zone is a Haswell zone that is now available to all projects and users. Currently, europe-west1-d zone offers 2.3 GHz Intel Xeon E5 v3 [Haswell](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29) processors. For more information, see [Zones](https://docs.cloud.google.com/compute/docs/regions-zones) and [Machine Types](https://docs.cloud.google.com/compute/docs/machine-types).



**February 05, 2015**

  * Released new Debian 7 images **v20150127** which performs automatic resizing of boot persistent disks up to 2 TB. For more information, see [Repartition a boot persistent disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#resize_pd).



**February 04, 2015**

  * Added UUIDs to virtual machine instances that can be queried through the [dmidecode](http://www.nongnu.org/dmidecode/) tool. For more information, see [Get the UUID of a VM](https://docs.cloud.google.com/compute/docs/instances/get-uuid).



## January 2015

**January 20, 2015**

  * [Local SSDs](https://docs.cloud.google.com/compute/docs/local-ssd) are now in General Availability and can be used by all projects and users.



**January 13, 2015**

  * Released new instance [`stop()`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/stop) and [`start()`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/start) features in **Beta**. See [Stopping an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance) and [Restarting a stopped instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance) for more information.

**Note:** Currently, virtual machines with local SSDs cannot be restarted but we expect to add this functionality in the future. Additionally, during Beta, stopped virtual machines count toward your available CPU quota but we will remove this restriction before this feature is generally available. 



## December 2014

**December 23, 2014**

  * Added instructions for [Importing an AMI image](https://docs.cloud.google.com/compute/docs/images/import-existing-image#create_image_file) into Compute Engine.



**December 17, 2014**

  * [Ubuntu](https://docs.cloud.google.com/compute/docs/images#ubuntu) images are now in General Availability.



**December 10, 2014**

  * Added new Windows images alias to `gcloud compute`. You can now specify the latest version of the Windows image by providing the following flag with your instance or disk creation request:
        
        --image windows-2008-r2
        

For more information, see [Starting a new Windows virtual machine instance](https://docs.cloud.google.com/compute/docs/instances/windows#starting_a_new_windows_virtual_machine_instance).




**December 08, 2014**

  * [Windows Server 2008 R2](https://docs.cloud.google.com/compute/docs/images#windows) is now available in **Beta** to all users and projects. Additionally, we've also added support for [Microsoft license mobility](https://docs.cloud.google.com/compute/docs/instances/ms-licensing).



**December 02, 2014**

  * Added support for [local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) in all zones, _except_ `us-central1-b` and `europe-west1-a`, which are deprecated. For more information, see [Resetting an instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance) or the [`instances().reset` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/reset).



## November 2014

**November 19, 2014**

  * `gcloud` version 0.9.37 and higher now has support for local SSD flags without an additional repository download. Additionally, the command-line flags have changed for creating local SSDs. For more information, see [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd).
  * Added support for [shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript) in [Ubuntu](https://docs.cloud.google.com/compute/docs/images#ubuntu) images.



**November 13, 2014**

  * Released new shutdown script feature in **Beta** for image versions v20141007 and newer. Shutdown scripts allow users to execute commands, on a best-effort basis, right before an instance is terminated or restarted. For more information, see [Shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).



**November 04, 2014**

  * Lowered pricing for persistent SSD and persistent disk snapshots. See [Persistent disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk) for more information.
  * Lowered network pricing. See [Network pricing](https://cloud.google.com/vpc/network-pricing) for more information.
  * Autoscaler is now available in Beta and available to all users and projects. See [Autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler) for more information.



**November 03, 2014**

  * [Canonical Ubuntu images](https://docs.cloud.google.com/compute/docs/images#ubuntu) are now in [Beta](https://cloud.google.com/products). For full release notes, see the [Canonical release notes](https://wiki.ubuntu.com/Releases).



## October 2014

**October 29, 2014**

  * Added new europe-west1-c zone. europe-west1-c zone is an Ivy Bridge zone that is now available to all projects and users. See [Zones](https://docs.cloud.google.com/compute/docs/regions-zones) for more information.
  * Released new local SSDs in Beta phase. This is now available to all users and projects. See [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) for more information.



**October 15, 2014**

  * Deprecated europe-west1-a zone. `europe-west1-a` has been deprecated and will be permanently turned down on March 29th, 2015. You should move all resources to `europe-west1-b` and ensure that you are no longer using any resources in `europe-west1-a` after March 29th, 2015.

We expect that an additional zone, `europe-west1-c` will be available in two weeks, on October 31st, 2014.

For instructions on how to move your instances, see [Moving an instance between zones](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones).




**October 06, 2014**

  * Released new RHEL 7 image, `rhel-7-v20141001`. For more information, see [Operating Systems](https://docs.cloud.google.com/compute/docs/images#rhel).
  * For RHEL 7 images, updated the firewall configuration so that all traffic is allowed by default, similar to existing CentOS images.



**October 01, 2014** \+ Lowered pricing for all machine types in all locations. For more information, see the [pricing page](https://cloud.google.com/products/compute/pricing).

## September 2014

**September 29, 2014**

  * Released new images, `v20140926`, that mitigates additional vulnerabilities in the bash security bug. See [Security bulletins](https://docs.cloud.google.com/compute/docs/security-bulletins#20140924) for detailed information.



**September 19, 2014**

  * Added new `utilizationTargetType` property in the API and new `--custom-metric-utilization-target-type CUSTOM_METRIC_UTILIZATION_TARGET_TYPE` flag in `gcloud compute` that specifies how the target value should be measured, either as a `GAUGE` value or a `DELTA_PER_MINUTE` value. This property is required if you are specifying a Stackdriver Monitoring metric. For more information, see the [Autoscaler documentation](https://docs.cloud.google.com/compute/docs/autoscaler).



**September 16, 2014**

  * Updated `gcloud compute` behavior so creating a new Windows instance requires an image name and the image project. See [Starting a new Windows virtual machine](https://docs.cloud.google.com/compute/docs/instances/creating-and-starting-an-instance) for more information.



**September 04, 2014**

  * Released new [CentOS 7 image](https://docs.cloud.google.com/compute/docs/images#centos), `centos-7-v20140903`. See [Operating Systems](https://docs.cloud.google.com/compute/docs/images#centos) for more information.



## August 2014

**August 13, 2014**

  * Released [`gcloud compute`](https://docs.cloud.google.com/compute/docs/gcloud-compute) into General Availability. Major changes from the last Open Preview release are: 
    * Added new `compute/zone` and `compute/region` properties that can be used to set a default zone and region. To set the properties, run `gcloud config set compute/zone ZONE` and `gcloud config set compute/region REGION`.
    * Added support for overriding disk auto-deletion during instance deletion.
    * Updated the output of commands that mutate resources to be more human-friendly. The --format flag can be used for more verbose output.
    * Replaced all `get` subcommands with `describe` subcommands (e.g., `gcloud compute instances get` has been replaced with `gcloud compute instances describe`).
    * Renamed the `firewalls` collection to `firewall-rules`.
    * Added support to the `addresses` collection for interacting with global addresses.



**August 12, 2014**

  * The scheduled maintenance for europe-west1-a zone has been cancelled and all zones have now transitioned to using transparent maintenance. This means that virtual machines set to live migrate will no longer be taken offline for maintenance in any zone. For information on transparent maintenance and how to set your virtual machines to live migrate, see the [Setting instance scheduling options](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options) documentation.



**August 04, 2014**

  * Added new zone, `asia-east1-c`, with transparent maintenance support. `asia-east1-c` is now available to all projects and users. See the [Zones and Region](https://docs.cloud.google.com/compute/docs/regions-zones#available) documentation for more details.



## July 2014

**July 22, 2014**

  * Released new Windows images `windows-server-2008-r2-dc-v20140716` with the following updates:

    * Allows load balancing for Windows virtual machines that are not in a zone marked by a `-windows` suffix. See the [Load Balancing](https://docs.cloud.google.com/compute/docs/load-balancing) documentation for more information.
    * Fixes a bug where Windows snapshots could not start new instances.
  * Enabled support for [Windows virtual machine instances](https://docs.cloud.google.com/compute/docs/images#windows) in all zones. Windows instances are no longer limited to Windows-specific zones. For information on starting and using Windows instances, see the [Operating Systems](https://docs.cloud.google.com/compute/docs/images#windows) documentation. Existing `-windows` zones will be inaccessible starting August 15th, 2014 and it is recommended that you restart your instance using the newest Windows image in a non-Windows zone before August 15, 2014.




**July 10, 2014**

  * Added new zone, `us-central1-f`, with transparent maintenance support. `us-central1-f` is now available to all projects and users. See the [Zones and Region](https://docs.cloud.google.com/compute/docs/regions-zones#available) documentation for more details.



## June 2014

**June 25, 2014**

  * SSD persistent disks are now available in General Availability and open to all users and projects. For detailed information about SSD persistent disks, see [Types of persistent disks](https://docs.cloud.google.com/compute/docs/disks#introduction). For pricing information, see the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk).



**June 09, 2014**

  * Released new images `sles-11-sp3-v20140609` to address the [OpenSSL security bulletin (CVE-2014-0224)](https://docs.cloud.google.com/compute/docs/security-bulletins) for SUSE Linux Enterprise Server.



**June 05, 2014**

  * Released new images `v20140605` to address the [OpenSSL security bulletin (CVE-2014-0224)](https://docs.cloud.google.com/compute/docs/security-bulletins). New images include: 
    * `debian-7-wheezy-v20140605`
    * `backports-debian-7-wheezy-v20140605`
    * `centos-6-v20140605`
    * `rhel-6-v20140605`



**June 04, 2014**

  * Released new [SSD persistent disks](https://docs.cloud.google.com/compute/docs/disks#introduction) in Limited Preview. SSD persistent disks are also charged at a [different rate](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk) than standard persistent disks.
  * Added new [Usage Export](https://docs.cloud.google.com/compute/docs/usage-export) feature that lets you export daily and monthly rollup reports about your project's detailed Compute Engine usage.



## May 2014

**May 27, 2014**

  * 16 core machine types are now in General Availability. For pricing, review the [pricing page](https://cloud.google.com/products/compute/pricing).



**May 13, 2014**

  * Added new field to Image resources, named `diskSizeGb`, which shows the size of the image when it is restored to a persistent disk, in GB.



**May 05, 2014**

  * Updated default firewall rule names. Default firewall rules are automatically created with every project. These rules were previously named `default-internal` and `default-ssh`. New projects will have the same default firewalls but with the following new names:

    * `default-allow-internal` \- Allows network connections of any protocol and port between any two instances.
    * `default-allow-ssh` \- Allows TCP connections from any source to any instance on the network, over port 22.
  * Introduced new default firewall rule that will be created with each new project.

    * `default-allow-icmp` \- Allows ICMP traffic from any source to any instance on the network.



## April 2014

**April 17, 2014**

  * Updated default Compute Engine API rate limit from 50,000 requests/day to 250,000 requests/day. See [API rate limits](https://docs.cloud.google.com/compute/docs/api-rate-limits) for more information.
  * Introduced new `Metadata-Flavor: Google` header to replace the `X-Google-Metadata-Request: True` header. This also allows users to easily detect if they are running in Compute Engine by querying for the new header. For more information, see [Metadata Server](https://docs.cloud.google.com/compute/docs/metadata#default).



**April 14, 2014**

  * Introduced an Asia Pacific region (`asia-east1`) and two new supported zones, `asia-east1-a` and `asia-east1-b`.



**April 09, 2014**

  * Released new images `v20140408` to address the [OpenSSL security bulletin (CVE-2014-0160)](https://docs.cloud.google.com/compute/docs/security-bulletins). New images include: 
    * `debian-7-wheezy-v20140408`
    * `backports-debian-7-wheezy-v20140408`
    * `centos-6-v20140408`
    * `rhel-6-v20140408`



**April 07, 2014**

  * [RHEL images](https://docs.cloud.google.com/compute/docs/images#rhel) have moved to General Availability status and are open to all users and projects.

Note that there is an additional fee for using premium operating systems, including RHEL. Please review the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) for more information.

  * Added new [Red Hat Cloud Access](https://docs.cloud.google.com/compute/docs/images#rhel) feature, which allows users to use their RHEL licenses on Compute Engine virtual machine instances.

  * Removed support for v1beta16. Please transition to using [v1](https://docs.cloud.google.com/compute/docs/reference/latest) if you haven't already.




**April 02, 2014**

  * gcutil Release 1.15.0 
    * Added feature where gcutil prompts the user to set an initial Windows password in the `addinstance` command if the source image is from a Google Windows project.



## March 2014

**March 25, 2014**

  * Introduced sustained use discounts. Sustained use discounts lower the effective price of your instances as your usage goes up. When you use a virtual machine for an entire month, this amounts to an additional 30% discount. For more information, see the [pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#sustained_use).

Sustained use discounts are effective starting April 1st, 2014.

  * [Windows Server images](https://docs.cloud.google.com/compute/docs/images#windows) are now available in limited preview.

Although we do not currently charge for use, you can review the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) for the intended Windows Server image pricing.

  * [SUSE images](https://docs.cloud.google.com/compute/docs/images#suse) are now generally available and is available for all users.

Note that Compute Engine will start charging for SUSE images on April 1st, 2014. See the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) for more information.

  * Introduced new [Replica Pool service](https://docs.cloud.google.com/compute/docs/replica-pool), which allows you to create a managed pool of virtual machines based on a reusable template. For more information, see the [Replica Pool](https://docs.cloud.google.com/compute/docs/replica-pool) documentation, or the [Replica Pool API reference](https://docs.cloud.google.com/compute/docs/replica-pool/v1beta1).




**March 19, 2014**

  * [RHEL images](https://docs.cloud.google.com/compute/docs/images#rhel) are now in open preview with a new image version, `v20140318`.

RHEL images are available to all users at no extra cost until April 1,

    1. On April 1, 2014, Compute Engine will start charging for use of these images according to the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages).
  * Released new Debian, CentOS, and Debian Backports images, `v20140318`.

    * For Debian images, network time protocol (NTP) is now configured to use Google services instead of the public NTP pool.
  * Updated image packages

    * Google Daemon now syncs ssh keys immediately instead of on a per-minute intervals.
    * Improved systemd integration.
    * Fixed Google Daemon data corruption bug.
    * Startup scripts are now downloaded with curl instead of wget.
    * Removed harmless warnings.



**March 14, 2014**

  * Released gcutil 1.14.2. 
    * Fixed issue where performing `gcutil moveinstances` with instances with disks whose autoDelete status is set to true would lead to loss of user data. `gcutil moveinstances` is now compatible with Compute Engine API v1 only.



**March 10, 2014**

  * Temporarily disabled support for [Advanced Vector Extensions (AVX)](https://wikipedia.org/wiki/Advanced_Vector_Extensions). Compute Engine has disabled support for AVX due to a stability issue that we are actively investigating. We will re-enable AVX support as soon as we find and fix the root cause.



**March 06, 2014**

  * [SUSE images](https://docs.cloud.google.com/compute/docs/images#suse) are now in open preview. This means that SUSE images are available to all users at no extra cost until April 1, 2014. On April 1, 2014, Compute Engine will start charging for use of these images according to the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages).



**March 05, 2014**

  * Added ability for creating and deleting a boot persistent disk when a virtual machine instance is created or deleted. See the [Instances](https://docs.cloud.google.com/compute/docs/reference/latest/instances/insert) documentation for more information.

  * Added support for restoring persistent disk snapshots to a persistent disk of a user-specified size.

It is now possible to use the `sizeGb` parameter when restoring a snapshot. This can be used to create a persistent disk that is larger than the persistent disk snapshot. See [Restoring snapshots to a Larger Size](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#restoresnapshotlargersize) for more information.

  * Added support for setting the [auto-delete state](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#updateautodelete) of a read/write persistent disk.

  * Released gcutil 1.14.0.

    * Switched to new, single API call for creating a virtual machine instance with a boot persistent disk.
    * Added new command, `setinstancediskautodelete`, that sets the auto-delete option for persistent disks attached to virtual machine instances.
    * Added support for specifying a disk size when creating a disk using a snapshot.
    * Decreased the time spent waiting for SSH keys to propagate during initial instance creation from 120 seconds to 10 seconds.



## February 2014

**February 20, 2014**

  * Added support for [Advanced Vector Extensions (AVX)](https://wikipedia.org/wiki/Advanced_Vector_Extensions) in new virtual machine instances.
  * All virtual machine instances created after February 11, 2014 have this feature enabled. To check if your virtual machine instance has this enabled, run the following command in your virtual machine instance:
        
        $ cat /proc/cpuinfo | grep avx
        
        

If you need to update your instance to use AVX, you must delete and recreate the instance.




## December 2013

**December 17, 2013**

  * Released new Protocol Forwarding feature. [Protocol forwarding](https://docs.cloud.google.com/compute/docs/protocol-forwarding) allows you to forward traffic to a single virtual machine instance, using a target. instance. Protocol forwarding provides support for these additional features: 
    * `AH`: [IP Authentication Header](http://tools.ietf.org/html/rfc4302.html) protocol.
    * `ESP`: [IP Encapsulating Security Payload](http://www.ietf.org/rfc/rfc2406.txt) protocol.
    * `SCTP`: [Stream Control Transmission](http://www.ietf.org/rfc/rfc2960.txt) protocol.
  * Added support for new [Target Instance resources](https://docs.cloud.google.com/compute/docs/load-balancing#targetinstances), which allows for non-NAT'ed traffic to be forwarded to a single virtual machine instance.

See [Protocol forwarding](https://docs.cloud.google.com/compute/docs/protocol-forwarding) for more information.




**December 03, 2013**

  * **Compute Engine is now generally available!** Users can now feel confident using Compute Engine to support mission-critical workloads with 24/7 support and a 99.95% monthly SLA. The move to general availability also comes with a host of new features and changes, detailed below.

  * Released new v1 API. [v1beta16](https://docs.cloud.google.com/compute/docs/reference/v1beta16) is now deprecated and customers should switch to [v1](https://docs.cloud.google.com/compute/docs/reference/latest). v1beta16 will remain available until March 04, 2014 and v1beta15 will be discontinued on January 03,

    1. Changes in v1 include (but are not limited to):

       * **New support for custom kernels and removed support for Google-provided kernels**

Users can now use custom kernels with their images and no longer need to use Google-built kernels. The Kernels collection has been removed from v1 and all new images will include embedded kernel binaries as part of the image.

       * **Removed scratch boot disks from v1.**

All scratch boot disks have been deprecated and we recommend transitioning to using [persistent disks](https://docs.cloud.google.com/compute/docs/disks). In the v1 API, you cannot create a scratch boot disk.

       * **Deprecated *-d machine types.**

All `*-d` machine types have been deprecated and no longer supported. Although you can still create instances with these machine types, we do not recommend this and will eventually remove these machine types completely.

  * **New machine types** : We've added new 16-core-machine types that are now available for your instances. For more information, review [machine types](https://docs.cloud.google.com/compute/docs/machine-types) and [pricing](https://cloud.google.com/products/compute/pricing).

  * We've introduced a new **persistent disk model**. Persistent disk performance now scales linearly with the size of the disk. Additionally, we are removing I/O charges for persistent disks completely and lowering the price of persistent disk storage. For more information, review the [pricing](https://cloud.google.com/compute/disks-image-pricing) documentation.

  * Released new metadata server version v1. The following are new changes with the v1 metadata server:

    * Requests to the metadata server will now require a security header. All requests to the metadata server will require the following header:

X-Google-Metadata-Requests: True

    * Requests containing the header `X-Forwarded-For` will automatically be rejected.

  * **Released gcutil v1.12.0.**

    * Added awareness of deprecated machine types to `listmachinetypes` and the machine type prompt when creating instances.
    * Made `--persistent_boot_disk` the default setting for the `addinstance` subcommand since scratch disks were removed from the v1 API. The `--nopersistent_boot_disk` flag can only be specified using the v1beta16 API.
    * Deprecated all kernel-related subcommands and flags when using the v1 API.
    * Updated gcutil to be distributed with the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).
    * Raised the default size of persistent disks to 500GB.
    * Made v1 the default API version.
  * As part of the Compute Engine move to using **full disk operating system** images, we have made the following changes:

    * Released new `backports-debian-wheezy` image, which allows users to access new features and bug fixes from the backports kernel.
    * Deprecated Kernels collection.
    * Remove all support for kernels from the v1 API.
    * Additionally, [FreeBSD](http://www.freebsd.org/), [SELinux](http://selinuxproject.org/page/Main_Page), and [CoreOS](http://coreos.com/) images now known to be functional on Compute Engine instances with the move to full disk operation system images.
  * Introduced new **premium operating systems limited preview program**. The new premium OS limited preview program lets you use a [SUSE](https://www.suse.com/) or [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/products/enterprise-linux/) images built explicitly for Compute Engine instances. Users who are interested in the program can review the documentation and sign up for the program on the [OS page](https://docs.cloud.google.com/compute/docs/images).




## November 2013

**November 25, 2013**

  * Released new Debian 7 and CentOS 6 images, `v20131120`.

    * New images now contain embedded kernels rather than Google-built kernels. For instructions on how to upgrade you persistent disk to use an embedded kernel, review the [documentation](https://docs.cloud.google.com/compute/docs/disks#upgrade). Similarly, you can also upgrade your custom image to use an embedded kernel.
    * New images allow you to use dmidecode to determine if you are running on Compute Engine. See the [documentation](https://docs.cloud.google.com/compute/docs/instances/detect-compute-engine) for more information.
  * Deprecated the Kernel resource. Google will no longer provide custom kernels and will instead use community-provided kernels in Google-provided images.




**November 12, 2013**

  * Added new instance migration and transparent scheduled maintenance features. Compute Engine now offers transparent scheduled maintenance in `us-central1-a` and `us-central1-b`; these zones will no longer go offline for scheduled maintenance and Compute Engine will automatically move your instances out of the way of any scheduled maintenance activity. For more information, see [maintenance events](https://docs.cloud.google.com/compute/docs/regions-zones#maintenance).

  * Added new gcutil release 1.11.0.

    * Added a new subcommand, `gcutil whoami`, that prints out the email of the currently-authenticated user to standard out.
    * Added two new scope aliases: datastore and userinfo-email.
    * Added flags to `gcutil addinstance` and a new subcommand, `gcutil setscheduling`, for controlling instance scheduling parameters.
    * Disabled host key checking for commands that rely on ssh because there is no secure channel to pass the host key to the client for the first time.
  * Marked all Debian 6 images as deprecated.

  * Marked Debian 7 images older than `debian-7-wheezy-v20130926` as deprecated.




## October 2013

**October 22, 2013**

  * Deprecated us-central2-a zone. `us-central2-a` has been deprecated and will be permanently turned down by December 31st, 2013. You should move all resources to `us-central1-a` and/or `us-central1-b` (after November 11, 2013) and ensure that you are no longer using any resources in `us-central2-a` after December 31st, 2013.



**October 10, 2013**

  * Added new kernel, `gce-no-conn-track-v20130813`, and images `v20130926`. 
    * `gce-no-conn-track-v20120813` kernel is identical to `gce-v20130813 kernel` except that [connection tracking](https://wikipedia.org/wiki/Netfilter#Connection_Tracking) is no longer enabled.
    * Images `v20130926` will use the new `gce-no-conn-track` kernel. To use a kernel with connection tracking turned on, specify the `--kernel` flag with a previous kernel version, such as `gce-v20130813`.



**October 07, 2013**

  * Reduce duration of two upcoming maintenance windows for `us-central1-a` and `us-central1-b` zones. The new maintenance window durations are as follows:

    * `us-central2-a`: Oct 12, 2013 12:00:00 PM - Oct 22, 2013 10:00:00 AM
    * `us-central1-b`: Nov 2, 2013 12:00:00 PM - Nov 10, 2013 12:00:00 PM
  * Released gcutil 1.9.1.

    * Fixed a bug in which the tilde in the authentication file path was not being expanded properly.



**October 3rd, 2013**

  * Added new features to [load balancing](https://docs.cloud.google.com/compute/docs/load-balancing):

    * New [`sessionAffinity`](https://docs.cloud.google.com/compute/docs/load-balancing#sessionAffinity) feature allows users to determine the hashing method used to select backend machines that receive traffic.
    * New [`backupPools`](https://docs.cloud.google.com/compute/docs/load-balancing#backupPools) and [`failoverRatio`](https://docs.cloud.google.com/compute/docs/load-balancing#failoverRation) feature allows users to specify a backup target pool, in case a primary target pool becomes unhealthy.
  * Released new API version v1beta16. [v1beta15](https://docs.cloud.google.com/compute/docs/reference/v1beta15) is now deprecated and customers should switch to [v1beta16](https://docs.cloud.google.com/compute/docs/reference/latest). v1beta15 will remain available until **January 03, 2014**. Changes in v1beta16 include:

    * Removed zone quotas.
    * Added new [regional quotas](https://docs.cloud.google.com/compute/docs/resource-quotas).
    * Updated the [global default quotas](https://docs.cloud.google.com/compute/docs/resource-quotas) with new default limits.
    * Changed `addresses().user` field from a string to a list and renamed the field to `addresses().users`.
    * Added new [`setBackup`](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools/setBackup) method to set backup target pools for existing primary target pools.
    * Updated [TargetPools](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools) resource representation to describe backup pools, failover ratios, and session affinity.
  * Released gcutil 1.9.0.

    * Added `gcutil settargetpoolbackup` command.
    * Added new `--backup_pool` and `--failover_ratio` flags for the `gcutil addtargetpool` command.
    * Removed `usage` field from `gcutil getzone` response.
    * Added new `usage` field to `gcutil getregion` response.
    * gcutil now outputs tables thats respect the terminal width. This feature can be turned off using the `--respect_terminal_width` flag.
    * `gcutil deleteinstance` with the `--force` flag now requests users to explicitly provide `--[no]delete_boot_pd` if any of the instances have a boot disk.
  * Stopped allowing cross-project resource references, such as the ability to create a disk from a snapshot in another project. Previously, it was allowed for projects whose access control lists (ACLs) allowed it, such as situations where multiple projects were owned by one user.




## September 2013

**September 10, 2013**

  * Released gcutil 1.8.4. 
    * Fixed an issue whereby reserved IP addresses were not preserved in the `gcutil moveinstances` subcommand.
    * Bug fixed where global flags were not being displayed on `gcutil --help`.
    * Updated gcutil help text.



**September 05, 2013**

  * Added new Debian images `v20130816`. 
    * Updated images to use latest kernel.
    * Updated images to use latest gcutil too.



**September 04, 2013**

  * Removed support for v1beta14.

**(Updated 09/09/2013)** Removed support for cross-region external IP address assignment.




## August 2013

**August 26, 2013**

  * Added support for [differential snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * Added information on how to [send email](https://docs.cloud.google.com/compute/docs/sending-mail) using [SendGrid](http://sendgrid.com).
  * Added new CentOS image `v20130813` with the following updates:

    * Updated image to use the latest kernel.
    * Updated image to use the latest gcutil tool.
  * Added new kernels `v20130813` with the following updates:

    * Added multiqueue support.
    * Fixed an issue in scheduler that impacted Hadoop.
    * Added backport pvclock enlightment for softlockup detector.



**August 6th, 2013**

  * Launched new load balancing service. Compute Engine has launched a load balancing feature that lets you distribute traffic across your instances. Load balancing is especially useful for supporting heavy traffic to your instances and to provide redundancy to avoid failures. For more information, visit the [load balancing documentation](https://docs.cloud.google.com/compute/docs/load-balancing). Additionally, you can review the load balancing [reference documentation](https://docs.cloud.google.com/compute/docs/reference/latest/forwardingRules).

  * Released gcutil 1.8.3

    * Added new prompt to select a persistent or scratch boot disk when using `gcutil addinstance`.

**Caution:** Customers with scripts that programmatically create instances in gcutil will need to update their script to use the `--[no]persistent_boot_disk` flag to continue programmatically creating instances. For more information, see [`gcutil addinstance`](https://docs.cloud.google.com/compute/docs/instances#start_vm).
    * Changed naming of persistent boot disks that are created during instance creation from `boot-<instance-name>` to `<instance-name>`.

    * Added prompt to delete attached persistent disk when using `gcutil deleteinstance`.

    * Added support for [load balancing](https://docs.cloud.google.com/compute/docs/load-balancing).

  * Added source code for custom tools that Compute Engine images uses, onto [GitHub](https://github.com/GoogleCloudPlatform/compute-image-packages). The list of tools include:

    * Image Bundle - Creates an image file our of a disk attached to a virtual machine instance.
    * Google Startup Scripts - Scripts and configuration files that set up a Linux-based image to work smoothly with Compute Engine.
    * Google Daemon - A service that manages user accounts, maintains SSH login keys, and syncs public endpoint IP addresses.
  * Added new Debian and CentOS images `v20130723`, with the following updates:

    * Added latest gsutil version which addresses issues where gsutil was not working properly.
    * Fixed typo which causes erroneous startup-script-url error.



## July 2013

**July 15th, 2013**

  * Marked kernels older than `gce-v20130603` as `DEPRECATED`.
  * Marked deprecated kernels `gce-v20120912` and older as `OBSOLETE`. For a list of kernels and their deprecation states, run the following command:
        
        gcutil --project=<project-id> listkernels
        




**June 26th, 2013**

  * Added bursting for `f1-micro` instances. See [machine types](https://docs.cloud.google.com/compute/docs/machine-types) for more information.
  * Added ability to reset an instance through the API. For more information, see [Resetting an instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance) or the [`instances().reset` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/reset).
  * Released gcutil 1.8.2. 
    * Added new `gcutil resetinstance` command that allows resetting virtual machine instances.
    * Fixed region detection when releasing addresses from multiple regions.
    * Fixed aggregated resource listing with `--format=names`.
    * Fixed the usage help string for `gcutil addroute` command.



## June 2013

**June 19th, 2013**

  * Added new Debian images `v20130617`.
  * Added the following updates for Debian 6 and 7 images `v20130617`:

    * Updated gsutil to 3.31 and gcutil to 1.8.1.
    * Disable IPv6 by default via /etc/sysctl.d, for optimal user experience. Compute Engine does not currently support IPv6.
  * Added the following updates for Debian 7 image `v20130617`:

    * Upgrade pre-installed packages to Debian 7.1, incorporating security updates and miscellaneous important bug fixes. For more information, see the [Debian announcements](http://lists.debian.org/debian-announce/2013/msg00003.html).



**June 18th, 2013**

  * Added new images `v20130522` and kernels `v20130603`.
  * Patched new kernel version `gcg-3.3.8-201305211623` and `gcg-3.3.8-201305291443` to address vulnerability in previous kernels. See [Security Bulletins](https://docs.cloud.google.com/compute/docs/security_bulletins) for more information.
  * Fixed kernel warning printed on boot about virtio net multiqueue.
  * Made ext4 kernel fixes (for `xfstest`).



## May 2013

**May 21st, 2013**

  * Increased default per-project total disk quota to 1TB.
  * Updated gcutil: 
    * Updated documentation for `gcutil moveinstances` to provide a warning of possible failures during the moving process.
    * Improved error detection in the `gcutil moveinstances` command.
    * Fixed behavior where gcutil attempted to use existing persistent disk when recreating an instance with the same name and the `--persistent_boot_disk` flag.
    * Machine type prompts in gcutil now provides a description of the machine types and `gcutil listimages` will now only display the name and description of images.



**May 15th, 2013**

  * Google Compute Engine is available for open signups! We're excited to announce that Google Compute Engine is now available for open signups and anyone can sign up for the service. For signup instructions, see the [signup page](https://docs.cloud.google.com/compute/docs/signup).

  * Released new API version v1beta15. v1beta14 is now deprecated and customers should switch to v1beta15. v1beta14 will remain available until August 15, 2013 and v1beta13 will be discontinued on **May 31, 2013**. Changes in v1beta15 include:

    * **Introduced[new region scope and regional resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources).**

      * Added new *_regional resource URIs_ to access regional resources, in the form:
            
            https://www.googleapis.com/compute/v1beta15/project/<project-id>/regions/<region-name>/<resource-type>/<resource-name>
            

For example, to access [regional reserved IPs](https://docs.cloud.google.com/compute/docs/instances_and_network#reservedaddress), use the following regional URI:
            
            https://www.googleapis.com/compute/v1beta15/project/example.com:myproject/regions/example-region/addresses
            

      * Updated reserved IP addresses to a regional resource.

External static IPs are now referred to as reserved IP addresses and are no longer a global resource. Reserved IPs are now a regional resource that can be managed through the [Addresses collection](https://docs.cloud.google.com/compute/docs/reference/latest/addresses).

You can also provision, promote, and release external IP addresses through the Addresses collection, without having to manually request one. For more information, see the [Reserved Addresses documentation](https://docs.cloud.google.com/compute/docs/instances_and_network#reservedaddress).

    * **Converted machine type resources to per-zone resources.**

To use a machine type, you must now specify the zone in which that machine type lives:
          
          https://www.googleapis.com/compute/v1beta15/project/example.com:myproject/zones/example-zone/machineTypes/machineTypeName
          

    * **Changed method of creating Snapshot resources to use a custom verb on the Disk resource.**

To create a Snapshot resource, you must now make a request to the following URI:

https://www.googleapis.com/compute/v1beta15/projects/PROJECT_ID/zones/ZONE/disks/DISK/createSnapshot

Snapshots are still accessible by making requests to the Snapshot collection.

    * **Removed ability to assign an internal IP address.**

The `internalIp` field on a virtual machine instance is now read-only and you can no longer manually assign internal IPs to your instances. Compute Engine will assign internal IPs automatically.

    * **Added a number of new features.**

      * Added new [Routes](https://docs.cloud.google.com/compute/docs/reference/latest/routes) collection that lets you set up and manage a virtual machine's routing table.
      * Added ability to [reserve and release static IPs](https://docs.cloud.google.com/compute/docs/reference/latest/addresses), and to promote ephemeral IPs to static IPs.
      * Added the ability to request [aggregate lists](https://docs.cloud.google.com/compute/docs/reference/latest/instances/aggregatedList) for per-zone and per-region resources. You can request aggregate lists for the following resources:

        * Instance resources
        * Disk resources
        * Address resources
        * Machine type resources

For example, you can list instances across all zones by making a request to the following URI:
    
    https://www.googleapis.com/compute/v1beta15/project/example.com:myproject/aggregated/instances
    

    * **Introduced new[shared-core machine types](https://cloud.google.com/products/compute/pricing).**

Shared-core machine types are more cost-effective for running applications that don't require a lot of resources. New available machine types are `g1-small` and `f1-micro`.

    * **Updated maximum total persistent disk size that can be attached to a machine type.**

Standard, high-memory, and high-CPU machine types now have an updated maximum total disk size of **10 TB**. See [machine types](https://docs.cloud.google.com/compute/docs/machine-types) for more information.

  * Updated [billing model](https://cloud.google.com/products/compute/pricing) for instances. Compute Engine has updated our billing model so that instances are billed based on per-minute usage. All instances that run for **10 minutes or less** will be charged for 10 minutes of usage. After the first 10 minutes, usage is charged on a per-minute basis.

  * Added new images and kernels `v20130515`.

  * Removed Google-specific repositories from images. The only packaged repositories configured in images are now the Debian archive. Compute Engine still installs Google-specific packages at build time but removed Google- specific repositories for various reasons.

  * Removed default installation of the `apiclient` library.

  * Changed log location of startup script output to `/var/log/startupscript.log`. Also, added startup script log output to the instance's serial port console so you can also run `gcutil getserialportoutput` to retrieve startup script log information.

  * Improved instance creation and deletion time for Debian.

  * Fixed issue preventing startup script specified in metadata to be downloaded from Google Cloud Storage.

  * Removed `dist-upgrade` from starting on instance boot.

  * Removed `google_storage_download` script.

  * Released gcutil 1.8.0.

    * Added support for v1beta15 Compute Engine API. (addresses, regions, per-zone machine types, aggregated lists).
    * Added `gcutil config` command, an alias for `gcutil auth`.
    * When prompting the user to select an image, gcutil will include standard images (CentOS, Debian).
    * With v1beta15 API, gcutil will use aggregated list API call by default. Aggregated list method will aggregate all resources across all scopes in which the resource of that type exist (for example, aggregated list of instances will list instances in all zones).
    * Users can specify image from the standard project by specifying image name prefix. For example: `gcutil addinstance my-instance --image=debian-7`. 
      * When moving instances using `gcutil moveinstances`, if some of the instances depend on deprecated resources (image, kernel), gcutil will warn before it proceeds with the migration (migration would fail). New flag `--replace_deprecated` will create instances in the destination zone with dependencies on deprecated resources updated to recommended replacement resources.
    * `List` commands will display all resources by default. Number of resources listed may be limited using `--max_results` flag. `--fetch_all_pages` flag is now deprecated.
    * Improved display of images and kernels list. By default, only newest kernels/images will be displayed when listed or when user is prompted to select an image or kernel. Use `--old_images` or `--old_kernels` to list all images or kernels, respectively.
    * When listing images, the standard images (CentOS, Debian) will be listed in addition to images from the specified project. To list images in the specified project only, use `--nostandard_images` flag.
    * When prompting user to select a machine type, gcutil displays machine type description in addition to the name.
    * Removed support for v1beta13 Google Compute Engine API.
  * gcelib is no longer available and if you haven't already, we strongly encourage users to transition to the [Google APIs Python Client Library](https://github.com/google/google-api-python-client).




**May 7th, 2013**

  * Released new Debian images. Compute Engine is happy to announce that Debian images for Compute Engine are now available for your instances. To view a list of Debian images available to your project, run the following gcutil command:
        
        gcutil --project=debian-cloud listimages
        

For information about Debian images, see the [Debian wiki](http://wiki.debian.org/Cloud/GoogleComputeEngineImage).

Similarly, you can see a list of CentOS images like so:
        
        gcutil --project=centos-cloud listimages
        

  * Deprecated gcel images. gcel images are now deprecated and we encourage users to transition to either Debian or CentOS images.




## April 2013

**April 4th, 2013**

  * Compute Engine available for Role-based signups! We're excited to announce that Compute Engine is now available for users who sign up for [Role-based Support](https://cloud.google.com/support/packages) for the Google Cloud Platform! Visit the [signup page](https://docs.cloud.google.com/compute/docs/signup) to get started.
  * Console updates 
    * Added new feature to [attach a persistent disk to a running instance](https://docs.cloud.google.com/compute/docs/console#attachingdisk).
    * Added new feature to [start an instance using a boot persistent disk](https://docs.cloud.google.com/compute/docs/console#bootfrompd).
    * Migrated the ability to view REST details of a request to [Google Cloud console](https://console.cloud.google.com/).



## March 2013

**March 29th, 2013**

  * Changed service account token cache period. The metadata server no longer caches service account tokens within 5 minutes of their expiration window. If you need to ensure you always have a valid access token, you can fetch one anytime within 5 minutes of the expiration window.
  * Fixed a bug where operations created using v1beta13 could not be retrieved using v1beta14.
  * Fixed a bug where attaching persistent disks with device names may collide with scratch disks.



**March 8th, 2013**

  * Released new metadata server version v1beta1. See the [transition guide](https://docs.cloud.google.com/compute/docs/metadata#transitioning) to help transition your code away from the previous metadata version. v1beta1 changes include:

    * New metadata server URL: `http://metadata.google.internal/computeMetadata/v1beta1/`
    * New metadata tree structure where metadata now live under a `project/` or `instance/` directory.
    * New URL query parameters. 
      * [`wait_for_change`](https://docs.cloud.google.com/compute/docs/metadata#waitforchange): Perform a hanging GET request that returns when the value of the specified metadata key changes.
      * [`recursive`](https://docs.cloud.google.com/compute/docs/metadata#aggcontents): retrieve all content from underneath a directory.
      * [`alt`](https://docs.cloud.google.com/compute/docs/metadata#endpoints): specify the format of the response.
  * Updated or added new [default metadata keys](https://docs.cloud.google.com/compute/docs/metadata#default).

  * Added new feature for [attaching](https://docs.cloud.google.com/compute/docs/disks#attachdiskrunninginstance) and [detaching](https://docs.cloud.google.com/compute/docs/disks#detachdisk) persistent disks to a running instance and new API documentation for [`attachDisk`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/attachDisk) and [`detachDisk`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/detachDisk) methods.

  * Added new images and kernels `v20130225`.

  * Patched kernels 3.3x to address security vulnerability in kernels 2.6x.

  * Released new [security bulletins](https://docs.cloud.google.com/compute/docs/security_bulletins) page that lists known security issues and their associated fixes.

  * Removed `/dev/<em>&lt;disk&gt;</em>` paths; users should be referencing their disks using the [`/dev/disk/by-id/`aliases](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk).

  * Released gcutil 1.7.2.

    * Added two new commands [attachDisk](https://docs.cloud.google.com/compute/docs/disks#attachdiskrunninginstance) and [detachDisk](https://docs.cloud.google.com/compute/docs/disks#detachdisk), which can be used to attach/detach a persistent disk to and from running virtual machine instance.
    * Fixed an issue where list operations were incorrectly capped at maximum number of results of 100.
    * Improved of project's IP addresses in `gcutil getproject`.
    * Deprecation information is now printed for deprecated resources.
    * Removed support for v1beta12 Google Compute Engine API.



## February 2013

**February 19th, 2013**

  * gcelib is now deprecated. Downloads and documentation of gcelib will continue to be available for three months, until **May 15, 2013**. During that time, gcelib will work with the v1beta13 API only (it won't be upgraded to work with v1beta14). Between now and May 15, developers using gcelib are strongly encouraged to migrate their applications to use an alternative client library, such as the [Google APIs Python Client Library](https://docs.cloud.google.com/compute/docs/api/python_guide).
  * Enabled billing for persistent disk snapshots. For more information on snapshot pricing, see the [pricing page](https://docs.cloud.google.com/compute/disks-image-pricing#standard_snapshot_pricing).



**February 8th, 2013**

  * Released gcutil 1.7.0. 
    * Added a new subcommand, `gcutil moveinstances`, for moving instances (and their persistent disks) from one zone to another.
    * Added `--zone` flag to `gcutil listdisks`.
    * Fixed a bug where `gcutil addsnapshot` would crash if the `--zone` flag was not specified.
    * Added zone column to the table output of `gcutil listoperations`.
    * Increased the timeout of synchronous operations from 2 minutes to 4 minutes.



## January 2013

**January 30th, 2013**

  * Released new API version v1beta14

v1beta13 is now deprecated and customers should switch to [v1beta14](https://docs.cloud.google.com/compute/docs/reference/latest). v1beta13 will remain available until **April 30, 2013** , and v1beta12 will be discontinued **February 11, 2013**.

Changes in v1beta14 include:

    * **Introduced[per-zone and global resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource)**

      * Added new *_per-zone resource URIs_ to access per-zone resources, in the form:
            
            https://www.googleapis.com/compute/v1beta14/projects/<project-id>/zones/<zone>/<resource-type>/<resource-name>
            

For example, accessing a Disk resource requires the following per-zone URI:
            
            https://www.googleapis.com/compute/v1beta14/project/example.com:myproject/zones/some-example-zone/disks/mydisk
            

    * _Added new global resource URIs for accessing global resources, in the form:_ *
          
          https://www.googleapis.com/compute/v1beta14/projects/<project-id>/<resource-type>/<resource-name>
          

For example, accessing a Machine Type resource requires the following global URI:
          
          https://www.googleapis.com/compute/v1beta14/project/example.com:myproject/global/machineTypes/somemachinetype
          

    * **Added a number of new features**

      * Added new [`setTags`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setTags) method which allows you to update instance tags for a running instances.
      * Added new [`setMetadata`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setMetadata) method which allows you to update metadata for a running instance.
      * Added new [`deprecate`](https://docs.cloud.google.com/compute/docs/reference/latest/images/deprecate) method which allows you to set the deprecation status for an image.
      * Added new [boot from Persistent Disk](https://docs.cloud.google.com/compute/docs/disks#rootfrompd) feature which allows you to store an operating system image on a persistent disk so that it persists through the life of the instance. Multiple instances can also attach to a boot persistent disk in read-only mode.
    * **Updated existing resource properties**

      * Removed `kind` property from `instance.networkInterfaces` and `instance.serviceAccounts`.
      * Removed support for using default images and default kernels when creating an instance or an image through the API. Users must now explicitly specify an image or kernel.
      * Added new [deprecate status](https://docs.cloud.google.com/compute/docs/reference/latest/images/deprecate) to resources.
    * **Updated response codes**

      * Changed error response for inserting an existing instance from `HTTP 400` to `HTTP 409`.
      * Changed server response for accepting an asynchronous request from `HTTP 200` to `HTTP 202`.
  * Released gcutil 1.6.0.

    * Added support for v1beta14 per-zone resources.
    * Added a new subcommand, [`gcutil setinstancemetadata`](https://docs.cloud.google.com/compute/docs/metadata#updatinginstancemetadata), for updating instance metadata.
    * Added a new subcommand, [`gcutil setinstancetags`](https://docs.cloud.google.com/compute/docs/label-or-tag-resources#tags), for updating and setting instance tags.

      * Added a new subcommand, [`gcutil deprecateimage`](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#deprecating_an_image), for setting the deprecated field on an image resource.
      * Added support for specifying a [boot persistent disk](https://docs.cloud.google.com/compute/docs/disks#rootfrompd) when creating a new instance:

gcutil addinstance my-instance --disk=my-disk,boot

      * Changed the ordering of the machine type prompt when creating instances so the standard machine types show up first, followed by the highcpu and highmem machine types.




**January 24th, 2013**

  * Added new VM images `centos-6-v20130104`, `gcel-12-04-v20130104`, and `gcel-10-04-v20130104`



## December 2012

**December 14th, 2012**

  * New persistent disk snapshot feature

Added [Persistent Disk Snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) feature which allows you to create snapshots of existing persistent disks and apply them to new disks.

**Note:** Although persistent disk snapshot rates are available on the [pricing page](https://cloud.google.com/products/compute/pricing), billing for snapshots is not yet enabled. We expect to enable snapshot billing in January 2013.
  * Added new error message when querying the metadata server for a service account token that has not been authorized for that instance.

  * Added new operation types for instance restarts and shutdowns

  * Released gcutil 1.5.0.

    * Added subcommands for interacting with snapshots.



**December 6th, 2012**

  * Added new high-memory and high-CPU machine types. 
    * For instances that require more memory relative to virtual cores, use [high-memory machine types](https://docs.cloud.google.com/compute/docs/machine-types).
    * For instances that require more virtual cores relative to memory, use [high-CPU machine types](https://docs.cloud.google.com/compute/docs/machine-types).
  * Added new [diskless](https://docs.cloud.google.com/compute/docs/machine-types) machine types.
  * Lowered pricing for [standard machine types](https://cloud.google.com/products/compute/pricing).
  * Added new [European zones](https://docs.cloud.google.com/compute/docs/regions-zones). 
    * `europe-west1-a`
    * `europe-west1-b`



## November 2012

**November 9th, 2012**

  * Released gcutil 1.4.1. 
    * Added new subcommand, `gcutil getserialportoutput`, for getting the serial port output from an instance.
    * Fixed an issue where gcutil waited for instances that failed to be created.
    * Changed the zone selection feature to display maintenance window information next to the zone names.
    * Changed the display of operation resources to show the user responsible for the operation.
  * New VM images and kernel for v20121106 
    * All new images that use a Debian package manager are now named `gcel-<version>`. Current images `ubuntu-12-04-vYYYYMMDD` and `ubuntu-10-04-vYYYYMMDD` are deprecated and will remain available until Feb. 9th, 2013.
    * Updated `/etc/lsb-release` file to reflect new distribution information.
    * Added support for [SCSI](https://wikipedia.org/wiki/SCSI) disk interface; for information on how to convert your instances, see [Disks Interfaces](https://docs.cloud.google.com/compute/docs/disks#interface).
    * Added ability to clone instances in the console. It is now possible to clone an instance by visiting the instance's details page and clicking the **Clone** button.



## October 2012

**October 11th, 2012**

  * Released new API Version v1beta13. v1beta12 is now deprecated and customers should switch to v1beta13. b1Beta12 will remain available until **January 11, 2013**. Changes in v1beta13 include:

    * Removed `hostCpus` field from the machineType resource
    * Changed API nouns and verbs to use camelCase, specifically:

      * `machine-types` is now `machineTypes`
      * `add-access-config` and `delete-access-config` is now `addAccessConfig` and `deleteAccessConfig`
      * `set-common-instance-metadata` is now `setCommonInstanceMetadata`
    * Made `setCommonInstanceMetadata` an asynchronous operation, returning an operation resource to track completion of the request

    * Add serial port output API

    * Fix metadata key validation and prevent duplicate metadata keys

    * `PENDING` and `RUNNING` states of long-running operations now reflect the full lifetime of the request

    * Delete operations now guarantee that the `DONE` state is not reached until after the resource has been completely torn down

**To update your application code to v1beta13:**

    1. Change all URIs from `v1beta12` to `v1beta13`. For example:
           
           https://www.googleapis.com/compute/**v1beta13** /disks

    2. Update API nouns and verbs that have a dash to use camelCase (e.g. `machineTypes` instead of `machine-types`)

    3. Update your application code to reflect the following changes, if necessary:

       * `setCommonInstanceMetadata` now returns an Operations resource
       * New metadata keys must match the regex `[a-zA-Z0-9-_]{1,128}` and be less than 128 bytes in length. Metadata values cannot be longer than 32768 bytes

**Note:** If your metadata value exceeds 32768 bytes, consider using a [startup script](https://docs.cloud.google.com/compute/docs/howtos/startupscript)
       * Operations can take longer to complete as they now reflect the total time it takes to roll out and confirm the request

       * Delete operations only return `DONE` after the resource has been completely torn down

       * Instances have new additional `STOPPING` state, which means that the instance is currently in process of being stopped

  * Released gcutil 1.3.4.

    * Implemented batch `adddisk`. It is now possible to add multiple disks with a single call to `gcutil adddisk`.
    * Implemented batch delete operations for additional resources. It is now possible to delete multiple disks, firewalls, images, instances, networks, operations, and snapshots.
    * Added a `--format` flag for the list subcommands. The flag accepts the following values: `table`, `sparse`, `json`, `csv`, and `names`. `--format=names` allows gcutil to be used with Unix tool pipelines:
          
          gcutil listinstances --format=names | xargs gcutil deleteinstance --force
          

    * Fixed the sorting in list subcommands. Instead of sorting each page individually, gcutil now sorts all results before displaying them to the user.

    * Changed `--cache_flag_values` to not cache flags when the underlying command fails.

    * Deprecated `--project_id` in favor of `--project`. `--project_id` still works, but will produce a warning.

    * Reconfigured the version checking to take place when gcutil exits.

    * Improved documentation for firewall commands.

    * Changed the headings for `list` and `get` subcommands. The new headings use dashes instead of spaces and are in lower-case. This eliminates the need to use quotes with the `--sort_by` flag and makes the display of the headings more user-friendly.

  * Added serial console output from a VM instance to the instance details page.

  * Added support for attaching persistent disks in read-only mode as well as read/write mode.

  * Added new example gcutil commands for adding instances, disks, networks, and firewalls.

  * Added support for adding and deleting networks.

  * Fixed assorted bugs.




## September 2012

**September 18th, 2012**

  * Released gcutil 1.2.0. 
    * Added support for `gs://` URLs to the `addimage` command.
    * Implemented support for multiple flag cache files. gcutil now searches for a `.gcutil.flags` file starting in the current directory, followed by the parent directories, and the home directory until a file is found.
    * Added a check to commands dealing with metadata to warn the user of duplicate metadata keys instead of silently ignoring duplicates.
    * Fixed an issue where `listoperations` would not fetch multiple pages when encountering an operation that contains an error. 
      * Changed the way gcutil is packaged.
      * Made some of the flag descriptions and an error messages more informative.
  * New Linux VM images v20120912 
    * Added more aggressive validation for ssh keys.
    * [make](http://linux.die.net/man/1/make) package is now included by default.



**September 13th, 2012**

  * Added newline to the end of `fstab` for images created using the image bundling tool.
  * Added a warning when users try to create hostnames that are 33 characters or longer.
  * Improved error messaging when a user tries to use an IP address reserved for system purposes.
  * Added ability to add or remove networks using the Console.



**September 5th, 2012**

  * Faster asynchronous job completion.
  * Improved scalability for resource creation, updates, and monitoring.
  * [Resource quotas enabled](https://docs.cloud.google.com/compute/docs/resource-quotas) on a per-project basis, for images, firewalls, and networks.
  * Enable NAT on ICMP packets.



## June 2012

**June 28, 2012** \+ Compute Engine is available for limited preview!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
