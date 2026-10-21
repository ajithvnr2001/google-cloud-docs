---
url: https://docs.cloud.google.com/compute/docs/release-notes/
title: Compute Engine release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:52:41.325512+00:00
---

# Compute Engine release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Compute Engine release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the latest release notes for features and updates to the Compute Engine service. The following release notes are also available for Compute Engine: 

  * [Guest environment release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes): contains feature rollouts and updates for the guest agent and other essential software required for your instances to function correctly on Compute Engine.
  * [The archive](https://docs.cloud.google.com/compute/docs/release-notes-archive): contains older release notes.



**Latest API version: v1**

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/compute-release-notes.xml) directly. 

## October 13, 2026

Feature

**Generally available** : You can query regional views of global Compute Engine project and OS image resources by using the regional read-only `projectViews` and `imageViews` endpoints. Querying regional views isolates your control-plane read requests to a specific region, helping your workloads stay available during global API disruptions. For more information, see [Use regional views for resilient control-plane reads](https://docs.cloud.google.com/compute/docs/architecture/regional-views-global-resources) and [Access global resources regionally for high availability](https://docs.cloud.google.com/compute/docs/architecture/access-global-resources-regionally).

## October 12, 2026

Feature

**Generally available** : The network-optimized C4N machine types with 375 GiB to 12,000 GiB of attached Titanium SSD are now generally available.

For more information, see [C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series) and [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd).

## October 08, 2026

Feature

**Generally available** : You can sync a Compute Engine VM's clock with its host server's clock by using `chrony` and `ptp_kvm` to achieve accuracy designed to be within 1 ms. Accurate time synchronization is supported in all standard public Google Cloud [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). For more information, see [Configure accurate time for Compute Engine VMs](https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-time-sync).

## October 06, 2026

Feature

**Generally available** : When you reserve compute resources for H4D instances through your account team, you can include a Hyperdisk pool in the same request or in a subsequent request. This option helps ensure that your high performance computing (HPC) workloads have the storage resources that they require close to your compute instances. For more information, see [Reserve capacity through your account team](https://docs.cloud.google.com/compute/docs/hpc/reserve-capacity-account-team).

## October 05, 2026

Feature

**Generally available** : Z3 machine types that have 8 to 44 vCPUs can use Hyperdisk Balanced High Availability volumes to synchronously replicate data across two zones.

For more information, see [About Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha).

Feature

**Preview** : External IPv6 addresses are now supported for [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier). For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

## October 01, 2026

Feature

**Generally available** : Expanded machine series support for sharing the same Hyperdisk volume between instances:

  * C3 bare metal instances support multi-writer mode for Hyperdisk Balanced volumes.
  * C4 instances created after May 1, 2026, support multi-writer mode for Hyperdisk Balanced, Hyperdisk Extreme, and Hyperdisk Balanced High Availability volumes.



For more information, see [Sharing a disk between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## September 30, 2026

Feature

**Generally available** : You can specify a 120-second preemption notice duration while creating Spot VMs. Use this feature for workloads on Spot VMs where you want up to an additional 120 seconds for handling preemption. If you want to migrate existing Spot VMs workloads, make sure you update your workload to handle preemption outside of a shutdown script and test preemption. For more information, see [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration) and [Create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot).

## September 29, 2026

Announcement

Interface-based versioning (IBV) for the Compute Engine API is now generally available. IBV lets you call a specific, date-based API version so you can adopt API changes on your own schedule.

For more information, see [Compute Engine API versioning](https://docs.cloud.google.com/compute/docs/api/how-tos/api-versioning-guide).

Feature

**Generally available** : Compute Engine API version `2026-09-01` is now generally available. In this version, `aggregatedList` methods return partial results by default when a scope is unreachable. The `returnPartialSuccess` query parameter is no longer available in `aggregatedList` and `list` methods.

For more information, see the [`2026-09-01` REST reference](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01).

Feature

**Preview** : Compute Engine API version `2026-10-01-preview` is now available in Preview. In this version, the `quotas` field is no longer available in responses from the `projects.get`, `regions.get`, and `regions.list` methods. To view and manage quota information, use the [Cloud Quotas API](https://docs.cloud.google.com/docs/quotas/overview).

For more information, see the [`2026-10-01-preview` REST reference](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview).

Feature

**Generally available** : You can create a standard or archive snapshot of a disk and protect the snapshot with a customer-managed encryption key (CMEK), even if the source disk isn't protected with a CMEK. If the source disk is protected with a CMEK, then you can use a different CMEK to encrypt the new snapshot.

For more information, see [Create a CMEK-encrypted snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#create_snapshot).

## September 28, 2026

Feature

**Allowlisted GA** : You can expose the host ID of a Compute Engine instance to verify its physical location in relation to other compute instances in your Google Cloud organization. Use compute instance proximity in a zone to optimize latency-sensitive workloads or improve the reliability of your applications. For more information, see [View the physical location of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).

Feature

**Generally available** : The [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4d) machine series supports Hyperdisk Throughput.

For more information, see [About Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput) and [Hyperdisk Throughput performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hdt-perf).

## September 25, 2026

Feature

**Generally available** : New X5 series with 50% larger memory instances: Breaking the previous 32TB memory limit of the X4 [memory-optimized machine type](https://docs.cloud.google.com/compute/docs/memory-optimized-machines), a new X5 series introduces massive 48TB configurations. This empowers the largest SAP HANA and RISE with SAP customers to easily scale up their mission-critical databases on a single node.

## September 24, 2026

Feature

**Preview** : To protect standard snapshots from accidental or malicious deletion, Compute Engine retains deleted snapshots in the _recycle bin_ for three days before permanently erasing the snapshots.

For more information, see [Retain deleted resources in the recycle bin](https://docs.cloud.google.com/compute/docs/disks/retain-deleted-resources).

## September 22, 2026

Deprecated

As of September 15, 2026, NVIDIA P100 (`nvidia-tesla-p100` and `nvidia-tesla-p100-vws`) GPUs have reached end of support (EOS) and are shut down. You can no longer create, launch, or access Compute Engine instances or other Google Cloud resources that use NVIDIA P100 GPUs.

For information about migrating your workloads to supported GPU alternatives such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series, see [NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos).

Deprecated

NVIDIA T4 (`nvidia-tesla-t4` and `nvidia-tesla-t4-vws`) and NVIDIA P4 (`nvidia-tesla-p4` and `nvidia-tesla-p4-vws`) GPUs are deprecated and will reach end of support (EOS) on August 1, 2027. After August 1, 2027, you won't be able to create, launch, or access Compute Engine instances or other Google Cloud resources that run NVIDIA T4 or P4 GPUs. In addition, you can no longer purchase or renew 3-year committed use discounts (CUDs) for NVIDIA T4 or P4 GPUs.

To transition your workloads to supported GPU models such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series before the EOS date, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) and [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos).

## September 17, 2026

Feature

**Generally available** : The storage-optimized Z4D machine series is generally available for Compute Engine. Powered by AMD EPYC Turin processors and Titanium offload processors, Z4D instances are purpose-built for low core usage and high storage density workloads such as:

  * SQL, NoSQL, and vector databases
  * Data analytics and data warehouses
  * Search
  * Parallel file systems for AI/ML



The Z4D machine series delivers up to 3 TB of memory and 42,000 GiB of local Titanium SSD capacity. Z4D also supports up to 400 Gbps of network bandwidth using two physical NICs. Z4D instances are available in predefined `standardlssd` and `highlssd` machine shapes.

For more information, see [Storage-optimized machine family](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series).

## September 15, 2026

Feature

**Public preview** : Network-optimized C4N machine type with 375 GiB to 12,000 GiB of attached Titanium SSD are now available in [Preview](https://cloud.google.com/products#product-launch-stages). You don't have to request allowlist approval.

For more information, see [C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series).

## September 14, 2026

Feature

**Preview** : You can create regional disks, including Hyperdisk Balanced High Availability volumes, from custom and public OS images.

For more information, see [Create and manage regional disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk).

## September 11, 2026

Feature

**Preview** : You can view Workload Manager rule findings directly on the Compute Engine **Overview** page in the Google Cloud console. The **Workload Manager findings** tile lets you identify configuration risks for your compute instances and resources against best practices for reliability and security.

For more information, see [View Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings).

## September 08, 2026

Feature

**Generally available** : You can convert a single-project reservation into a shared reservation, or a shared reservation into a single-project reservation. Modify the share type for a reservation to share your reserved resources with other projects in your Google Cloud organization, or to restrict access to only the reservation's owner project. For more information, see [Modify the share type for a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-share-type).

## August 26, 2026

Feature

**Generally available** : Red Hat Enterprise Linux (RHEL) images pre-configured with Logical Volume Manager (LVM) partitioning are available for Compute Engine in the Google Cloud console. LVM-enabled images let you manage volumes flexibly and size partitions dynamically on your boot disk.

For more information, see [Red Hat Enterprise Linux (RHEL)](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel).

Feature

**Generally available** : Red Hat Enterprise Linux (RHEL) Extended Update Support (EUS) images are available for Compute Engine in the Google Cloud console. RHEL EUS images let you lock your VMs to a specific minor version while receiving critical security updates and bug fixes for up to two years.

For more information, see [Red Hat Enterprise Linux (RHEL)](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel).

## August 21, 2026

Feature

**Generally available** : The network- and memory-optimized [M4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series) is generally available. Powered by 5th generation Intel Xeon Scalable processors (Emerald Rapids), M4N instances are purpose-built for network and block storage-intensive workloads such as:

  * High-performance vector databases
  * Retrieval-augmented generation (RAG) data layers
  * Massive in-memory context caching
  * Real-time semantic search



The M4N machine series delivers the highest I/O performance available in Compute Engine, supporting up to 400 Gbps of network bandwidth. M4N also offers leading block storage performance with Hyperdisk Extreme that scales up to 25 GiB/s of bandwidth and 1M IOPS. M4N instances are available in predefined machine shapes, ranging in size from 16 to 224 vCPUs and up to 5,952 GB of DDR5 memory.

## August 20, 2026

Feature

**Preview** : Image Builder is available in allowlist-only Preview. Image Builder is a declarative operating system (OS) image customization tool that automates the process of building, customizing, and validating custom OS images within Google Cloud by using Cloud Build. For more information about Image Builder, see [About Image Builder](https://docs.cloud.google.com/compute/docs/images/image-builder/overview).

To onboard your project and request access, fill out the [request form](https://forms.gle/4NncEhwetZDjaPx9A).

## August 19, 2026

Feature

**Preview** : Advanced Compute Images provide high-performance images to support your artificial intelligence (AI), machine learning (ML), and high-performance computing (HPC) workloads running on non-GPU instances on Google Cloud.

Advanced Compute Images optimized for CPUs provide a single source of trusted, performance-tuned OS images that remove the need for manual image building for specialized workloads. Each image version is pre-installed with the necessary drivers, network fabrics, and Slurm agents to help you run your workloads.

## August 14, 2026

Feature

**Generally available** : You can use zonal and global extension policies in VM Extension Manager to automatically install and manage extensions, such as the Ops Agent, on a fleet of VMs and to ensure consistent extension states across your project.

To improve observability of enforcement states and guest agent activities, you can [view VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs) by using Cloud Logging. These logs help you identify and troubleshoot issues with VM extensions.

For more information, see [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).

## August 12, 2026

Feature

**Generally available** : The U4 Ultra Low Latency (ULL) network-optimized machine family is generally available with allowlist for [ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview) customers. Designed for financial exchange ecosystems, the U4 machine family provides industry-specific networking capabilities and ultra-low latency unicast and multicast communication. All U4 instances leverage Google's [Titanium IPU](https://cloud.google.com/titanium).

The U4 machine family includes the following machine series:

  * **U4P machine series** : Bare metal instances powered by 5th generation Intel Xeon Scalable processors (Emerald Rapids), delivering specialized compute for exchange operators running core trading systems.
  * **U4C machine series** : Bare metal instances powered by 5th generation Intel Xeon Scalable processors (Emerald Rapids), designed for exchange participants executing latency-sensitive trading strategies.
  * **U4S machine series** : Virtual machine (VM) instances powered by 6th generation Intel Xeon Scalable processors (Granite Rapids), providing advanced flexibility and cost optimization for adjacent workloads and ecosystem services requiring close physical proximity to U4P and U4C instances.



For more information, see the [U4 machine family overview](https://docs.cloud.google.com/ull-solution/participants/u4-machines) in the ULL Solution documentation.

## August 11, 2026

Feature

**Generally available** : Compute flexible committed use discounts (CUDs) are available for G2 and G4 GPU accelerator-optimized machine series. The supported resources include vCPUs, memory, Local SSD disks, and GPUs.

Compute flexible CUDs are spend-based CUDs that apply to eligible Google Cloud spend across Compute Engine, GKE, and Cloud Run. For G2 and G4 machine series, compute flexible commitments provide the flexibility to switch between eligible machine series and regions depending on your workload needs. For GPUs that belong to these machine series, compute flexible commitments don't require attached reservations.

For more information, see [Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

Security

A vulnerability (CVE-2026-6726) in the Trusted Computing Group's TPM 2.0 reference implementation code was discovered and is being addressed. For more information, see the [GCP-2026-054 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-054).

## August 03, 2026

Feature

**Changed** : The minimum provisioned throughput for a Hyperdisk ML volume attached to more than 20 instances is 20 MiB/s per instance, reduced from 100 MiB/s.

For more information, see [Share a Hyperdisk ML volume between instances](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#hdml-ro).

## July 29, 2026

Feature

**Public preview** : you can create a machine image that includes or excludes specific non-boot disks attached to a source Compute Engine instance. For more information, see [Create a machine image from specific disks](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#specific-disk-backup). You can also create a new disk by restoring a specific individual disk from a machine image without creating a new Compute Engine instance. For more information, see [Create a disk from a machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image#create-disk-from-machine-image).

## July 28, 2026

Feature

Hyperdisk Balanced volumes on C4D instances have increased maximum throughput limits for these machine types:

  * `c4d-*-96`: 3,125 MiB/s (up from 2,800 MiB/s).
  * `c4d-*-192`: 6,250 MiB/s (up from 4,800 MiB/s).
  * `c4d-*-384`: 12,500 MiB/s (up from 10,000 MiB/s).



For detailed performance limits, see [Hyperdisk Balanced performance limits when attached to an instance](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#perf-limits).

## July 27, 2026

Feature

The maximum IOPS per GiB for Hyperdisk Balanced Storage Pools have increased from 4 IOPS per GiB. The new limits depend on the provisioning type:

  * **Standard performance** : 30 IOPS per GiB
  * **Advanced performance** : 6 IOPS per GiB



For more information, see [Limits for Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#hdsp-limits).

## July 24, 2026

Feature

You can observe real-time virtual machine (VM) distribution across zones, machine types, and instance states in your managed instance groups (MIGs) by using the **GCE MIG Instance Distribution Monitoring** dashboard in Cloud Monitoring. When your group uses location flexibility across zones, instance flexibility across machine types, or both, this visibility helps you monitor capacity allocation and diagnose runtime fallback behavior. For more information, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

## July 21, 2026

Feature

**Generally available** : You can configure a regional managed instance group (MIG) to allow a VM repair in an alternate zone when the MIG can't repair the VM in its original zone. Repairing a VM in an alternate zone can help to improve your application's resiliency and resource obtainability. For more information, see [Repair a VM in an alternate zone](https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone).

## July 20, 2026

Deprecated

Encrypting disks, snapshots, images, and machine images with customer-supplied encryption keys (CSEKs) is deprecated and will be disabled on July 20, 2027.

For more information and alternatives to CSEKs for your Compute Engine resources, see [Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine).

## July 16, 2026

Feature

Hyperdisk Balanced High Availability volumes on C4 instances have increased performance limits for several machine types. For example, an instance that uses the `c4-standard-16` machine type can reach up to 1,600 MiB/s of throughput, up from 600 MiB/s.

For detailed performance limits, see [Hyperdisk Balanced High Availability performance limits when attached to an instance](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#perf-limits).

Change

**Changed** : The following operations on the boot disk of a Compute Engine instance that has a service account attached no longer require the `iam.serviceAccounts.actAs` permission. In the following list, the boot disk of such an instance is referred to as the _source disk_.

  * Creating a standard or archive snapshot of the source disk.
  * Cloning the source disk.
  * Creating a machine image of the instance.
  * Creating a custom image of the source disk.
  * Starting asynchronous replication of the source disk to another region.
  * Creating a new disk when you create an instance, if the new disk is created from an instant snapshot of the source disk.



## July 15, 2026

Feature

**Preview** : The network-optimized C4N machine series offers machine types with 375 GiB to 12,000 GiB of attached Titanium SSD.

To use C4N machine types with attached Local SSD disks, you can [Request preview access](https://forms.gle/ehRSqssSEavKt1Fh7).

For more information, see [C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series).

## July 09, 2026

Feature

**Preview** : Advanced Compute Images provide high-performance images to support your artificial intelligence (AI), machine learning (ML), and high-performance computing (HPC) workloads on Google Cloud.

Advanced Compute Images provide a single source of trusted, performance-tuned OS images that remove the need for manual image building for specialized workloads. Each image version is pre-installed with the necessary drivers, network fabrics, and Slurm agents to help you run your workloads.

## July 08, 2026

Feature

**Generally available** : The network-optimized C4N machine series is generally available for Compute Engine and Google Kubernetes Engine (GKE) customers. Powered by 5th generation Intel Xeon Scalable processors (Emerald Rapids), C4N instances are purpose-built for network- and block storage-intensive workloads such as:

  * Network and security appliances
  * High-performance databases
  * High-scale data analytics
  * Distributed filesystems



The C4N machine series delivers the highest I/O performance available in Compute Engine, supporting up to 400 Gbps of network bandwidth and up to 95 million packets per second (Mpps) of sustained packet processing performance. C4N also offers leading block storage performance with Hyperdisk Extreme that scales up to 25 GiB/s of bandwidth and 1M IOPS. C4N instances are available in predefined machine shapes with three different vCPU to memory ratios, ranging in size from 2 to 192 vCPUs and up to 1,488 GB of DDR5 memory.

For C4N machine types with attached Local SSD disks, you can [Request preview access](https://forms.gle/ehRSqssSEavKt1Fh7).

For more information, see [C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series).

## June 26, 2026

Feature

**Generally available** : You can cancel a future reservation request in calendar mode to prevent Compute Engine from provisioning your requested resources and incurring unnecessary charges. For more information, see [Delete a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations-calendar-mode).

Feature

**Generally available** : In a managed instance group (MIG), you can use a health check to monitor your application health without triggering repairs for an unhealthy VM, if the application fails the health check. You can prevent the MIG from repairing an unhealthy VM by turning off autohealing. For more information, see [Turn off repairs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).

## June 23, 2026

Feature

**Preview** : You can use Gemini in the Google Cloud console as an AI-powered interface to evaluate hardware options, estimate deployment costs, and view recommended configurations for your Compute Engine instances. Prompting Gemini helps you reach an optimal configuration for your workload before you create or modify a compute instance. For more information, see [Design your compute infrastructure with Gemini](https://docs.cloud.google.com/compute/docs/design-with-gemini).

## June 22, 2026

Feature

**Generally available** : You can create instances all at once in a regional managed instance group (MIG) by using resize requests. For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

Feature

**Generally available** : Resource-based committed use discount (CUD) recommendations are available for GPUs, Local SSD disks, and premium operating system (OS) licenses.

CUD recommendations provide insight into any additional commitments that you can purchase to optimize the costs of the resources that you run. You can use these recommendations and purchase commitments for resource usage that isn't covered by commitments and is being charged at list prices. Google Cloud analyzes your compute instance spending trends with and without a commitment and generates CUD recommendations on a monthly basis.

For more information about how CUD recommendations are generated, what resource types are supported, and how to use recommendations to purchase commitments, see [Get recommendations for committed use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds-recommender).

## June 16, 2026

Change

For resource-based committed use discounts (CUDs), the default value of CUD scope for most Cloud Billing accounts has changed from **Project** to **Billing account**. If the CUD scope is set to **Billing account** , then resource-based CUDs from a commitment are shared across all projects in that account. If the CUD scope is set to **Project** , then resource-based CUDs from a commitment are available to only the project in which you purchased that commitment.

Depending on the Cloud Billing account's creation date and the active commitments in that account, this change applies in the following way:

  * **Cloud Billing accounts created on or after June 16, 2026** : The CUD scope is **Billing account** (CUD sharing enabled) by default.
  * **Cloud Billing accounts created before June 16, 2026** : 
    * If the account has **no active resource-based commitments** on June 16, 2026, then the CUD scope has changed to **Billing account** (CUD sharing enabled).
    * If the account has **any active resource-based commitments** on June 16, 2026, then the CUD scope remains unchanged and Google Cloud continues to use your existing configuration.



For more information, see [Share resource-based CUDs across projects](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#cud-scope-configuration).

## June 15, 2026

Feature

**Preview** : Before you create Spot VMs, you can view the following information for a specific machine type and location:

  * **You can view the real-time obtainability and estimated uptime**. This information helps you maximize your chances of successfully creating Spot VMs, as well as help ensure that your workload starts and runs efficiently.

  * **You can view historical and current preemption rate and pricing**. This information helps you compare and choose the configuration that best fits your workload needs and budget.




For more information, see [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability) and [View the preemption rate and pricing for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price).

## June 11, 2026

Feature

In an autoscaled managed instance group (MIG), you can configure the stabilization period to manage how quickly the autoscaler deletes instances after a decrease in the load. This configuration can help optimize costs or maintain extra capacity based on your workload requirements. For more information, see [Configure stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#configure_stabilization_period).

## June 09, 2026

Security

A vulnerability (CVE-2025-10263) about bypass of translation stages or GPT protections in some Arm core families was discovered and has been addressed. For more information, see the [GCP-2026-036 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-036).

## June 08, 2026

Feature

**Generally available** : The [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4d) machine series supports Hyperdisk Balanced High Availability disks.

For more information, see [About Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha) and [Performance limits for machine series](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hdbha-perf).

## June 03, 2026

Feature

**Generally available** : You can gradually create Flex-start VMs in a managed instance group (MIG) as capacity becomes available. Unlike resize requests for MIGs that wait for full capacity before creating VMs, this method might create only a portion of your requested Flex-start VMs if capacity is unavailable. The MIG creates the remaining VMs later as capacity permits. Flex-start VMs run for up to seven days and help you obtain high-demand resources, such as GPUs, at a discounted price.

For more information, see [Create a MIG that uses Flex-start VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms).

## June 01, 2026

Feature

**Generally available** : Compute Engine supports the Google's custom-developed accelerator Tensor Processing Unit (TPU), providing a converged experience across AI accelerators on Google Cloud. You can use the Compute Engine instance API and managed instance group (MIG) API to create and manage TPU VMs. You can perform standard VM configurations such as using a custom OS or configure boot disk size. Compute Engine APIs support the creation and management of TPU slices across all consumption options, enabling small-scale experimentation and large-scale training and inference workloads.

For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/compute/docs/tpus/tpu-resources-in-compute-engine).

Feature

**Generally available** : In a managed instance group (MIG), obtain the requested number of virtual machine (VM) instances all at once by using bulk mode of the target size policy. Using bulk mode helps you avoid partial VM provisioning in a MIG. Bulk mode is particularly beneficial for batch workloads, such as high performance computing (HPC) or distributed training, that require full capacity before they can start. For more information, see [About bulk mode](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode).

## May 27, 2026

Feature

**Generally available** : Two C4A bare metal machine types are generally available:

  * `c4a-standard-96-metal` with 96 vCPUs and 384 GB of DDR5 memory
  * `c4a-highmem-96-metal` with 96 vCPUs and 768 GB DDR5 memory



These two machine types support Hyperdisk Balanced, Hyperdisk Extreme, Hyperdisk Throughput, and Hyperdisk ML volume storage and up to 100 Gbps of network bandwidth.

To learn more about the C4A machine family, read [General-purpose machines](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series). To see where you can create C4A bare metal instances, read [Bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).

## May 12, 2026

Security

A vulnerability in AMD firmware (CVE-2025-61971, CVE-2025-61972, CVE-2024-36315) that could compromise SEV-SNP guests has been addressed. For more information, see the [GCP-2026-031 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-031).

Security

A vulnerability (CVE-2025-54518) about potential corruption within the micro-operation (OP) cache in Zen 2 microarchitecture processors was discovered and has been addressed. For more information, see the [GCP-2026-032 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-032).

## April 29, 2026

Feature

**Preview** : In an autoscaled managed instance group (MIG), you can monitor individual autoscaling events and view details to understand the reasons behind each autoscaling decision. For more information, see [Monitor autoscaling events](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#monitor_autoscaling_events).

## April 27, 2026

Feature

**Generally available** : Compute Engine now offers support for AI zones. To learn more, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).

## April 22, 2026

Feature

**Generally available** : The G4 accelerator-optimized machine series now supports the creation of virtual machine (VM) instances with less than one GPU attached (fractional GPUs). When you create VM instances with fractional GPUs, you can select 1/2, 1/4, or 1/8 of a G4 GPU. Fractional GPUs let you optimize costs for workloads that don't require the resources of a full GPU.

For more information, see the [G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) overview.

## April 20, 2026

Feature

**Generally available** : You can use the Compute Engine remote Model Context Protocol (MCP) server to let AI agents and AI applications manage Compute Engine resources, such as Compute Engine instances, managed instance groups, disks, and snapshots. For more information, see [Use the Compute Engine remote MCP server](https://docs.cloud.google.com/compute/docs/use-compute-engine-mcp).

## April 17, 2026

Feature

**Generally available** : You can create a Hyperdisk Balanced High Availability disk by cloning a zonal Hyperdisk Balanced or Hyperdisk Extreme disk. This lets you make your zonal workloads highly available by adding a replica of the data in another zone within the same region.

For more information, see [Create a regional disk clone from a zonal disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#create-regional-clone).

## April 16, 2026

Feature

**Generally available** : To ensure data consistency when backing up multiple disks, you can use consistency groups of instant snapshots to back up a group of disks at the same point in time.

For more information, see [About instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

Feature

**Preview** : You can specify a 120-second preemption notice duration while creating Spot VMs. Use this feature for workloads on Spot VMs where you want up to an additional 120 seconds for handling preemption. If you want to migrate existing Spot VMs workloads, make sure you update your workload to handle preemption outside of a shutdown script and test preemption. For more information, see [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration) and [Create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot).

Feature

**Generally available** : You can rotate the customer-managed encryption key (CMEK) used to encrypt a disk, standard snapshot, or archive snapshot to a new key version without downtime.

**Generally available** : You can change the CMEK used to encrypt a disk, standard snapshot, or archive snapshot to a different key without downtime.

For more information, see [Rotate the CMEK for a disk or standard snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption) and [Change the CMEK for a disk or standard snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#change-key).

## April 15, 2026

Announcement

You can view the physical location of your Compute Engine instances in a zone to understand your cluster topology. This information helps you reduce network latency between your compute instances. For more information, see [View Compute Engine instance topology](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).

Feature

**Generally available** : You can control the physical location of the Compute Engine instances in a MIG by using workload policies. Workload policies help you to, for example, place your compute instances close together to minimize network latency when running AI or ML workloads. For more information, see [About workload policies in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies).

## April 14, 2026

Security

A vulnerability (CVE-2025-54510) about AMD SEV-SNP guest memory integrity has been addressed. For more information, see the [GCP-2026-019 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-019).

Security

A vulnerability affecting AMD SEV-SNP Confidential VM instances was discovered and has been addressed. For more information, see the [GCP-2026-021 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-021).

Feature

**Generally available** : Hyperdisk ML disks are supported by the following machine series:

  * [C3 bare metal](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_disks)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4), including bare metal instances.
  * [C4A bare metal instances](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4a)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4a)



For more information, see [Hyperdisk ML overview](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml).

## April 09, 2026

Feature

**Generally available** : Hyperdisk ML disks are supported by the following machine series:

  * [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-disks)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4d)
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4)
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4d)



Hyperdisk ML offers the highest throughput of all Google Cloud Hyperdisk types, up to 2 TiB/s (2,097,152 MiB/s). For more information, see [Hyperdisk ML overview](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml).

## April 02, 2026

Feature

**Preview** : To control the use of the deprecated container startup agent, an option for deploying containers on Compute Engine instances, you can enforce the `constraints/compute.managed.disableVmsWithContainerStartupAgent` organization policy constraint. This constraint prevents the creation of Compute Engine instances that use the container startup agent and the `gce-container-declaration` metadata.

You can also enforce this organization policy in dry-run mode to identify projects that use the deprecated metadata, without blocking resource creation.

For more information, see [Prevent the creation of VMs that use the container metadata](https://docs.cloud.google.com/compute/docs/containers/prevent-konlet-vms) and [Migrate containers deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

## March 31, 2026

Feature

**Generally available** : The maximum throughput for a Hyperdisk ML disk is increased to 2,097,152 MiB/s from 1,200,000 MiB/s. Hyperdisk ML provides the highest throughput per disk for machine learning and for workloads that require high read throughput on immutable datasets.

For more information, see [About Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml).

## March 27, 2026

Security

A vulnerability (CVE-2026-23268) about CrackArmor was discovered and has been addressed. For more information, see the [GCP-2026-015 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-015).

## March 24, 2026

Feature

**Generally available** : The maximum throughput for a Hyperdisk Balanced High Availability disk is increased to 2,400 MiB/s from 1,200 MiB/s. Hyperdisk Balanced High Availability provides high availability block storage for mission-critical workloads by synchronously replicating data between two zones within a region.

For more information, see [Hyperdisk Balanced High Availability overview](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha).

## March 23, 2026

Feature

**Preview** : The instance flexibility policy of a managed instance group (MIG) lets you override the minimum CPU platform and disk definition that is specified in the MIG's instance template. With these overrides, you can select machine types that run on different CPU platforms and that have different architectures.

For more information, see [About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#overrides-for-instance-properties).

## March 19, 2026

Breaking

**Changed** : The following operations on the boot disk of a Compute Engine instance that has a service account attached require the `iam.serviceAccounts.actAs` permission on the service account. In the following list, the boot disk of such an instance is referred to as the _source disk_.

  * Creating a standard or archive snapshot of the source disk, including application consistent snapshots
  * Cloning the source disk
  * Creating a machine image of the instance
  * Creating a custom image of the source disk
  * Starting asynchronous replication of the source disk to another region
  * Creating a new disk when you create an instance, if the new disk is created from an instant snapshot of the source disk



If you already have the Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) role and the Service Account User (v1) (`roles/iam.serviceAccountUser`) role on the project, no action is required.

Otherwise, ask your administrator to grant you the `iam.serviceAccounts.actAs` permission on the service account. For instructions, see [Manage access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources).

## March 11, 2026

Issue

To address high-severity kernel vulnerabilities (including [CVE-2025-21756](https://nvd.nist.gov/vuln/detail/CVE-2025-21756) and [CVE-2025-38052](https://nvd.nist.gov/vuln/detail/CVE-2025-38052)) in Rocky Linux 8 and 9, updates are available for the Compute Engine images maintained by [CIQ](https://ciq.com/products/rocky-linux/). If your VM instances use images dated before September 2025 (version `v20250912`), you must take action to ensure you continue to receive security patches.

**How to determine if your Compute Engine VMs are affected**

You are affected if your VM instance uses a Rocky Linux image from an `-optimized-gcp` or `-optimized-gcp-nvidia` family with a version date older than `v20250912` (for example, `rocky-linux-9-optimized-gcp-v20250807`). To check your VM's source image, see View [VM instance image details](https://docs.cloud.google.com/compute/docs/instances/view-vm-image). You can view details for these image families in [Rocky Linux OS details](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux).

**Action required**

  * **If your image version is** `v20250912` **or later:** Your VM is already configured to use the newer [SIG/Cloud Next (SCN)](https://docs.ciq.com/scn/) repositories and is receiving security updates. **No action is required.**

  * **If your image version is older than** `v20250912`: Your VM is configured to use legacy [SIG/Cloud](https://sig-cloud.rocky.page/) repositories that no longer receive regular kernel updates and won't receive future security patches. While running `sudo dnf update` applies a one-time patch for the vulnerabilities listed, you **must** manually migrate the VM to the SCN repositories to receive ongoing updates by following the [CIQ migration guide](https://docs.ciq.com/scn/#migration-from-sigcloud).




## March 10, 2026

Feature

When you autoscale a managed instance group (MIG), you can monitor the configured group size and the size recommended by the autoscaler on a chart. For more information, see [Monitor group size](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#monitor_group_size).

## March 05, 2026

Issue

For Red Hat Enterprise Linux (RHEL) operating system, VM Manager provides vulnerability scanning results based on the latest minor version for each major version released. If your VM runs an earlier minor version of RHEL, you might get inaccurate results in the vulnerability reports. For more information about supported operating systems for vulnerability reports, see [supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager).

## March 04, 2026

Feature

**Generally available** : You can use managed constraints with Organization Policy Service for centralized, programmatic control of your Compute Engine resources. Managed constraints replace legacy `compute.*` constraints and are identifiable by the `compute.managed.*` prefix. They also include built-in support for safe rollout tools like Policy Simulator and dry run mode.

For more information, see [Organization policies for Compute Engine](https://docs.cloud.google.com/compute/docs/access/organization-policies) and [Managed constraints](https://docs.cloud.google.com/compute/docs/access/managed-constraints).

## March 02, 2026

Feature

**Generally available** : You can apply compact placement policies to standalone Flex-start VMs. These policies let you colocate your standalone Flex-start VMs as close to each other as possible. Applying a compact placement policy minimizes network hops and improves the performance of latency-sensitive workloads. For more information, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) and [About Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

## February 23, 2026

Feature

**Generally available** : H4D VMs, designed for high performance computing (HPC) workloads, are now generally available. Based on 5th generation AMD EPYC Turin with Cloud RDMA 200 Gbps networking, H4D VMs offer 192 cores (SMT disabled), up to 1,488 GB of memory, and 3,750 GiB of Local SSD. H4D is optimized for tightly-coupled applications that scale across multiple nodes.

For more information, see [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series).

## February 18, 2026

Feature

**Generally available** : You can use Hyperdisk Exapools for large-scale workloads, such as AI and machine learning, that require between 500 TiB and 5 EiB of block storage and more than 100 GiB/s of concurrent performance in a single zone. With Hyperdisk Exapools, you purchase storage and performance in bulk and share those resources across as many as 500,000 disks in a single project.

To use Hyperdisk Exapools with your projects, [contact your account team](https://docs.cloud.google.com/tam) to get access.

To learn more about Hyperdisk Exapools, see [Hyperdisk Exapools overview](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools).

## February 17, 2026

Deprecated

Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

Change

After March 17, 2026, when you enable Compute Engine, the Compute Engine MCP server is automatically enabled.

## February 12, 2026

Feature

**Generally available** : You can use instance flexibility to improve resource availability when creating VMs in bulk in a region. With instance flexibility, you specify one or more suitable machine types for your workload. Compute Engine then provisions VMs from the list of machine types based on capacity and quota availability.

For more information, see [About instance flexibility for VMs created in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/about-instance-flexibility-for-bulk-vms) and [Create VMs in bulk with instance flexibility](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk-with-instance-flexibility).

## February 10, 2026

Feature

**Preview** : You can use consistency groups of instant snapshots to back up a group of disks at the same point in time, ensuring data consistency across multiple disks. Consistency groups of instant snapshots offer the following benefits:

  * **Simultaneous backups** : create instant snapshots for all disks in a consistency group with a single operation.
  * **Bulk restoration** : restore multiple disks at once from a consistency group of instant snapshots.



To learn more, see [About instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

## February 09, 2026

Feature

You can autoscale a managed instance group (MIG) that has instance flexibility configured. Autoscaling lets the MIG create or delete virtual machine instances based on an increase or decrease in load. For more information, see [About instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#instance_flexibility_and_autoscaling).

## February 06, 2026

Change

Expanded coverage for compute flexible committed use discounts (CUDs) is available to all Cloud Billing accounts. All Cloud Billing accounts have been automatically migrated to the [new spend-based CUD model](https://docs.cloud.google.com/docs/cuds-multiprice) and you no longer need to opt in to benefit from the expanded coverage. For the full list of eligible SKUs across Compute Engine, GKE, and Cloud Run, see [SKU Groups - Compute Flexible CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/compute-flexible-cud-eligible-skus).

To learn more about compute flexible CUDs and how they apply to your usage, see the [compute flexible CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

## February 05, 2026

Feature

**Generally available** : You can use Hyperdisk ML with the following machine series and Cloud TPU versions:

  * C4A machine series
  * A4 machine series
  * A4X machine series
  * G4 machine series
  * TPU v5e
  * TPU v5p
  * TPU7x



For more information, see [About Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml).

## January 26, 2026

Feature

**Generally available** : The N4A machine family is powered by Google's latest custom-designed Axion processor, built on Arm Neoverse N3 compute core and powered by Titanium IPU. This machine family has between 1-64 vCPUs with up to 512 GB of memory, and supports Google Cloud Hyperdisk volume storage. It is available in `standard`, `highmem`, `highcpu`, and custom machine types. For detailed information, see [General-purpose machines](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series). See [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) to learn where you can create N4A VMs.

## January 20, 2026

Feature

**Generally available** : You can create N4, C4, M4, and M3 VM instances in Bangkok, Thailand `asia-southeast3-a,b,c`. To learn more about these machine types, see [General-purpose machines](https://docs.cloud.google.com/compute/docs/general-purpose-machines) and [Memory-optimized machines](https://docs.cloud.google.com/compute/docs/memory-optimized-machines).

## January 07, 2026

Feature

**Generally available** : You can view future resource availability before you create a future reservation request in calendar mode. This action helps increase the likelihood that Google Cloud approves your request. For more information, see [View resource future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability).

## December 22, 2025

Feature

When you autoscale a regional managed instance group (MIG), you can view the reasons why the autoscaler adds or removes VMs in your MIG. Autoscaling reasons were previously available only for zonal MIGs. For more information, see [Viewing autoscaler logs](https://docs.cloud.google.com/compute/docs/autoscaler/viewing-autoscaler-logs).

## December 19, 2025

Feature

**Public Preview** : The C4A VM family now offers a `c4a-highmem-96-metal` bare metal instance. This machine type has 96 vCPUs and 768 GB of DDR5 memory, [Titanium I/O offload processing](https://cloud.google.com/titanium), and supports Hyperdisk Balanced, Hyperdisk Extreme, and Hyperdisk ML storage volumes. This bare metal instance is offered in select [regions and zones](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#regions_zones). For more information, see [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series).

Feature

**Generally available** : The G4 accelerator-optimized machine series supports the flex-start provisioning model. When you specify the flex-start provisioning model for your G4 virtual machine (VM) instances, you receive a discount up to 50% for vCPUs, memory, and GPUs. Flex-start is ideal for fault-tolerant or temporary workloads that can benefit from lower costs by having a flexible start time. For more information, see [About Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

## December 17, 2025

Feature

**Generally available** : You can create future reservation requests in calendar mode to reserve GPU, TPU, or H4D resources for your virtual machine (VM) instances. Use these requests to obtain high-demand resources for creating VMs that you plan to run for up to 90 days, such as when you want to run model pre-training, model fine-tuning, or high performance computing (HPC) jobs. For more information, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

## December 16, 2025

Feature

Sole-tenancy is now supported for the following GPU machine types:

  * A2 Ultra, A2 Mega, and A2 High machine types. You can provision sole-tenant nodes using the following node types: 
    * `a2-ultragpu-node-96-1360-lssd`
    * `a2-megagpu-node-96-1360`
    * `a2-highgpu-node-96-680`
  * A3 Mega and A3 High machine types. You can provision sole-tenant nodes using the following node types: 
    * `a3-megagpu-node-208-1872-lssd`
    * `a3-highgpu-node-208-1872-lssd`



For more information, see [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

## December 14, 2025

Feature

Instance flexibility in regional managed instance groups (MIGs) support the `ANY` target distribution shape. Selecting this shape lets you maximize resource obtainability and the utilization of unused zonal reservations. For more information, see [About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

## December 12, 2025

Feature

The memory-optimized X4 machine series offers additional bare metal machine types with 6 TB, 8 TB, and 12 TB of memory. For more information, see [X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series).

Issue

Workloads on A4 VMs might experience interruptions due to a firmware issue for NVIDIA B200 GPUs. To help prevent the issue, we recommend resetting the GPUs on A4 VMs at least once every 60 days. For more information, see the [known issue](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/known-issues#a4-firmware).

## December 10, 2025

Feature

**Generally available** : The general purpose C4 machine series now supports the following machine types on Intel's Xeon 6 processor (Granite Rapids):

  * `c4-standard-288-lssd-metal`
  * `c4-highmem-288-lssd-metal`



To learn more, see the [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series).

For more information, see [Machine types that automatically attach Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed) and [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).

Fixed

If you clone a source disk that's encrypted with a customer-supplied encryption key or customer-managed encryption key, you must use the same key to encrypt the clone.

For more information, see [Create a clone of an encrypted source disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#encrypted-source).

Feature

**Preview** : You can use the [Compute Engine remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/compute/docs/reference/mcp) to let LLM agents manage Compute Engine resources, such as VMs and disks. This server provides a standardized interface for AI applications to securely and reliably interact with Compute Engine resources using natural language or autonomous workflows.

## December 08, 2025

Feature

**Preview** : VM Extension Manager lets you manage Compute Engine guest agent extensions on your virtual machines (VMs). You can use VM Extension Manager to install and manage extensions, such as Ops Agent and Agent for SAP, on your Compute Engine VMs at scale, without connecting to each VM.

Use VM Extension Manager to create policies that install extensions on your VMs. You can install extensions based on a specific criteria, such as VM labels, for both existing and new VMs that match the criteria. VM Extension Manager automates the lifecycle of extensions across your entire fleet of VMs and monitors their health status while they are running.

For more information, see the following:

  * [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager)
  * [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy)
  * [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions)



## November 26, 2025

Issue

C4 machine type virtual machine (VM) instances running on sole tenant nodes might encounter unexpected VM terminations due to host errors or VM creation failures. For more information, see [known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#c4-oom-errors).

## November 24, 2025

Feature

**Public Preview** : You can now access the VM metadata server using IPv6 connectivity from single-stack IPv6 VM instances. For more information, see [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

## November 19, 2025

Fixed

For the Windows operating system, gVNIC driver version 2.0.15 is available.

This version fixes the handling for highly fragmented TSO packets. Without this updated driver version, you might experience intermittent network connectivity loss on Windows VMs that use any Compute Engine machine types. The affected versions are 2.0.7 - 2.0.14.

Symptoms include ARP resolution failures and an inability to reach local subnet IPs, including the metadata server. We recommend upgrading your Windows instances to this latest version of the driver. To learn about upgrading, read the [Windows components](https://docs.cloud.google.com/compute/docs/images/guest-environment#windows-components) section of the Guest environment documentation.

## November 18, 2025

Feature

**Preview** : The general purpose C4 machine series now supports the following machine types on Intel's Xeon 6 processor (Granite Rapids):

  * `c4-standard-288-lssd-metal`
  * `c4-highmem-288-lssd-metal`



To learn more, see the [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series).

For more information, see [Machine types that automatically attach Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed) and [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).

Feature

You can autoscale a regional managed instance group (MIG) that has the target distribution shape set to `ANY` or `ANY_SINGLE_ZONE`. These shapes are particularly beneficial for batch workloads. For more information about target distribution shapes, see [Regional MIG target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).

## November 13, 2025

Feature

**Preview** : Future reservation requests in calendar mode support reserving capacity for `a3-megagpu-8g` and `a3-highgpu-8g` machine types. Use future reservation requests in calendar mode to obtain resources for running model pre-training, model fine-tuning, simulation, and inference workloads. For more information, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

## November 10, 2025

Issue

The Windows guest agent identifies administrator accounts and groups using string matching. Therefore, credential management features only function correctly when you use English language names for user accounts and groups, for example, `Administrators`. If you use non-English language names, credential management features such as generating or resetting passwords might not function as expected. For more information about managing Windows user accounts, see [Manage accounts and credentials on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials) and [Known issues for Windows VM instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-non-english-credentials).

Feature

**Generally available** : Two new features that provide better observability for Compute Engine reservations and deeper insights into their capacity usage and costs:

  * A new `consumedReservation` field in the VM instance details showing the full resource name of the consumed reservation, providing reservation consumption status on VMs and better visibility for resource management and troubleshooting.
  * Two new system labels in the BigQuery billing export for instances consuming a reservation and the unused portion of a reservation, providing more detailed cost analysis: 
    * `compute.googleapis.com/reservation_name`: the short name of the Compute Engine reservation.
    * `compute.googleapis.com/reservation_project_id`: the Project ID owning the Compute Engine reservation.



For more information, see the following:

  * [View consumption history for a given instance](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#view_consumption_for_a_given_instance).
  * [Analyze usage distribution per project for a shared reservation](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#analyze_usage_distribution_for_a_given_reservation).
  * [List all the instances consuming a reservation](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#list_all_the_instances_consuming_a_reservation).



## November 07, 2025

Feature

**Generally available** : N4D VMs are powered by the fifth generation AMD EPYC Turin processor and [Titanium I/O offload processing](https://cloud.google.com/titanium). N4D machine types have up to 96 vCPUs and up to 768 GB of DDR5 memory, and a max-boost frequency of 4.1 GHz. They are offered in predefined and custom machine types and are available in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

N4D VM instances support standard networking with up to 50 Gbps of networking bandwidth and Hyperdisk storage. For more information, see [General-purpose machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series).

## November 06, 2025

Feature

**Preview** : N4A VMs are powered by Google's next-generation Axion processor, which is built on the Arm Neoverse N3 platform. N4A includes machine types with up to 64 vCPUs and 512 GB of DDR5 memory. N4A is available as standard, high-mem, high-cpu, and custom machine types with extended memory and up to 50 Gbps of standard networking. These machine types are available in limited [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). For more information, see [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series).

To access these VMs, complete [this access request form](https://docs.google.com/forms/d/e/1FAIpQLSddzdVNnkbi5oKB3DURruA28S9MdxdKcvxwuheqojGHCldLRw/viewform), or speak to your account team.

## November 04, 2025

Feature

**Public preview** : You can configure a regional managed instance group (MIG) to repair a VM in an alternate zone when the MIG can't repair the VM in its original zone. Repairing a VM in an alternate zone can improve your application's resiliency and resource obtainability. For more information, see [Repair a VM in an alternate zone](https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone).

Feature

**Generally available** : You can verify which reservation a VM consumes and view a list of VMs that consume a reservation. For more information, see [View reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view_reservation_consumption).

## November 02, 2025

Feature

If you need to synchronize time with high accuracy and monitor its accuracy for your Compute Engine instances, you can sync your VM clock with its host server clock using `chrony` and `ptp_kvm`. This configuration provides accuracy within 1 ms for supported setups. For more information, see [Configure accurate time for Compute Engine VMs](https://docs.cloud.google.com/compute/docs/instances/time-synchronization).

## October 30, 2025

Feature

**Generally available** : Dynamic NICs let you add or remove network interfaces to or from an instance without restarting or recreating the instance.

You can also use Dynamic NICs when you need more network interfaces. The maximum number of vNICs for most machine types in Google Cloud is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

  * [Multiple network interfaces overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)
  * [Create VM instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)



## October 28, 2025

Feature

**Generally available** : You can create managed instance groups (MIGs) that consist of IPv6-only VM instances.

For more information, see [Basic scenarios for creating managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

## October 21, 2025

Feature

**Generally available** : Future reservations let you reserve capacity for a specific date up to one year in advance. For more information, see [About future reservation requests](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).

Change

As part of the consolidation of CIQ's kernel trees, the kernel `dist-tag` that supports the Rocky Linux Optimized and Accelerator images on Compute Engine is changing from `elX_ycld_next` to `elX_y_ciq`. There are no changes to Secure Boot or GPG signing keys.

For example, `6.12.0-55.32.1.el10_0cld_next.2.1` changes to `6.12.0-55.39.1.el10_0_ciq.2.1`, where `ciq` replaces the `cld_next` tag.

This change affects the Rocky Linux 8, 9, and 10 optimized and accelerator images in an upcoming kernel update over the next month. The major version 8 and 9 kernels now include FIPS 140-3 patches as part of CIQ's ongoing FIPS 140-3 validation efforts for Rocky Linux. These patches have no effect if FIPS mode is not enabled. There are no code changes to the major version 10 kernel.

You can find the kernel source tree in the CIQ [kernel-src-tree](https://github.com/ctrliq/kernel-src-tree) GitHub repository.

## October 20, 2025

Security

A vulnerability affecting AMD Zen 5 processors (Turin) is being addressed. For more information, see the [GCP-2025-058 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2025-058).

Feature

**Generally Available** : The G4 [accelerator-optimized machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) is designed for graphics-intensive workloads such as NVIDIA Omniverse simulations, video transcoding, and virtual desktops. The G4 machine series also provides a cost-effective solution for single-host inference and model tuning. The G4 machine series is now available in the following regions and zones:

  * APAC 
    * Jurong West, Singapore: `asia-southeast1-b`
  * Europe 
    * Eemshaven, Netherlands: `europe-west4-a`
  * North America 
    * Council Bluffs, Iowa: `us-central1-b`
    * Ashburn, Virginia: `us-east4-c`
    * Columbus, Ohio: `us-east5-c`



To get started with G4 machine types, see [Create a G2 or G4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series).

## October 18, 2025

Feature

**Generally Available** : You can use the Compute Engine alpha API at the project level through a self-service process. By enabling the alpha API, you can use the Google Cloud console, Google Cloud CLI, API, and Terraform to view and manage preview features. For more information, see [Use the Compute Engine alpha API](https://docs.cloud.google.com/compute/docs/reference/rest/alpha).

## October 17, 2025

Feature

**Generally Available** : You can use the Compute Engine alpha API at the project level through a self-service process. By enabling the alpha API, you can use the Google Cloud console, Google Cloud CLI, API, and Terraform to view and manage preview features. For more information, see [Use the Compute Engine alpha API](https://docs.cloud.google.com/compute/docs/reference/rest/alpha).

## October 16, 2025

Change

Starting with SUSE Linux Enterprise Server (SLES) 16, including variants for SAP, the default file system for the root partition (`/`) is [Btrfs](https://en.wikipedia.org/wiki/Btrfs), which replaces the previous default of XFS. For more information, see [File systems in SLES](https://documentation.suse.com/sles/15-SP7/html/SLES-all/cha-filesystems.html#sec-filesystems-major-btrfs-suse) in the SUSE documentation.

## October 06, 2025

Change

The Google Cloud optimized (`-optimized-gcp`) and accelerated (`optimized-gcp-nvidia-*`) versions of the Rocky Linux images include the [CIQ SIG/Cloud Next repository](https://docs.ciq.com/rlc/ciq-sig-cloud-next/), which provides a cloud-optimized kernel. The accelerated images also include the [CIQ SIG/Cloud Next Nonfree repository](https://gitlab.com/ctrl-iq-public/sig-cloud-next/next-nonfree), which provides proprietary GPU drivers for the cloud-optimized kernel.

This update applies to images created on or after September 12, 2025.

For more information about Rocky Linux OS images, see [Rocky Linux](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux) on the operating system details page.

## September 22, 2025

Feature

**Generally available** : You can create and use Flex-start VMs. Flex-start VMs are virtual machine (VM) instances that can run for up to seven days, and that use the flex-start provisioning model. This model provisions resources from a secure pool of capacity, increasing your chances of obtaining high-demand resources like GPUs. These features make Flex-start VMs suitable for short-duration workloads that can start at any time, such as the following:

  * Small model pre-training
  * Model fine-tuning
  * High performance computing (HPC) simulation
  * Batch inference



You can create standalone Flex-start VMs, or add Flex-start VMs all at once to a managed instance group (MIG) by using resize requests. Based on the machine type that your Flex-start VMs use, you get discounts for vCPUs, memory, and any attached GPUs.

For more information, see [About Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

## September 17, 2025

Change

Compute Engine enforces limits to the total baseline performance that a project's Hyperdisk Balanced and Hyperdisk Balanced High Availability disks that are in the same zone can consume at the same time. The aggregate baseline performance limit is 50 GiB/s of throughput and 500,000 IOPS, and it only applies to baseline performance. For a detailed explanation, see [Concurrent consumption limits for baseline performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#baseline_consumption_limits).

## September 15, 2025

Feature

**Generally available** : You can decrease a Compute Engine instance shutdown time by skipping the guest OS shutdown. This action speeds up an instance stop or deletion operation to release resources and quota faster. However, as abrupt guest OS shutdowns may cause data loss or corrupt file system data, we recommend that you skip a guest OS shutdown only when you delete instances, or when you stop instances which boot disks you don't plan to reuse. For more information, see [Decrease Compute Engine instances shutdown time](https://docs.cloud.google.com/compute/docs/instances/decrease-shutdown-time).

## September 12, 2025

Feature

**Preview** : H4D VMs, designed for high performance computing (HPC) workloads, are now in preview. Based on 5th generation AMD EPYC Turin with Cloud RDMA 200 Gbps networking, H4D VMs offer 192 cores (SMT disabled), up to 1,488 GB of memory, and 3,750 GiB of Local SSD. H4D is optimized for tightly-coupled applications that scale across multiple nodes and offers RDMA-enabled 200 Gbps networking.

For more information, see [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series).

## September 10, 2025

Feature

**Generally available** : The [accelerator-optimized A4X machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms), the first GPU VM to run on Arm, is available on Compute Engine. The A4X machine series has the NVIDIA GB200 Grace Blackwell Superchips attached and runs on the NVIDIA GB200 NVL72 platform. Use this machine type to run your large artificial intelligence (AI) models, machine learning (ML), and high performance computing (HPC) workloads. The A4X machine type is currently available in the `us-central1-a` zone.

## September 09, 2025

Feature

**Preview:** Eight new organization policy constraints are available to help you enforce security best practices for Compute Engine virtual machine (VM) instances.

These [managed constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints) simplify governance for common security scenarios and integrate with safe rollout tools like [dry-run](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy) and [simulation](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies), letting you test their impact before enforcement.

The new constraints are as follows:

  * `compute.managed.disableNestedVirtualization`
  * `compute.managed.disableSerialPortAccess`
  * `compute.managed.disableSerialPortLogging`
  * `compute.managed.disallowGlobalDns`
  * `compute.managed.requireOsConfig`
  * `compute.managed.requireOsLogin`
  * `compute.managed.vmCanIpForward`
  * `compute.managed.vmExternalIpAccess`



These constraints can evaluate metadata values at the [VM instance, project, or zonal level](https://docs.cloud.google.com/compute/docs/metadata/overview#metadata-directories). For more information about these managed constraints, see [Managed Constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints#managed-constraints) in the Resource Manager documentation.

Change

Hyperdisk Balanced High Availability disks are available in all regions. Hyperdisk Balanced High Availability disks synchronously replicate disk data from one zone to another. Cross-zonal replication provides data protection in the unlikely event of a zonal outage. For more information, see [About Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha).

## September 04, 2025

Feature

Hyperdisk Balanced High Availability (Hyperdisk Balanced HA) volumes attached to C3 instances have increased performance limits for several C3 machine types. The new limits for the updated machine types are as follows:

  * `c3-*-8`: 50,000 IOPS and 800 MiB/s of throughput
  * `c3-*-22`: 120,000 IOPS and 1,800 MiB/s of throughput
  * `c3-*-44`: 160,000 IOPS and 2,400 MiB/s of throughput
  * `c3-*-88`: 160,000 IOPS and 4,800 MiB/s of throughput
  * `c3-*-176`: 160,000 IOPS and 10,000 MiB/s of throughput
  * `c3-*-192`: 160,000 IOPS and 10,000 MiB/s of throughput



For more information, see [Performance limits when attached to an instance](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#perf-limits).

Feature

**Generally available** : [Windows OS images](https://docs.cloud.google.com/compute/docs/images/os-details#network-features) have been updated with a new version of the gVNIC driver. Third generation and later compute instances that use these updated Windows OS images support up to [200 Gbps networking bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table) and [Jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).

## August 28, 2025

Feature

**Generally available:** [M4 memory-optimized hypermem VMs](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_series) are now generally available. These smaller machine types expand the memory-optimized family to allow for greater flexibility in matching your specific application needs. Hypermem VMs have a GB/vCPU ratio of 15.5:1 and are offered in the following sizes:

  * m4-hypermem-16
  * m4-hypermem-32
  * m4-hypermem-64



See the [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page to learn where you can create M4 VMs.

## August 26, 2025

Feature

**Generally available** : You can create instances that use only IPv6 IP addresses. For more information, see [Create an IPv6-only instance](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance#create-vm-ipv6-only).

## August 20, 2025

Feature

You can use instant snapshots to back up Extreme Persistent Disk volumes. For more information, see [About instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

## August 14, 2025

Feature

**Public Preview** : You can now access the Compute Engine alpha API at the project level through a self-service process. By enabling the alpha API, you can use the Google Cloud console, gcloud CLI, API, and Terraform to view and manage Preview features. For more information, see [Use the Compute Engine alpha API](https://docs.cloud.google.com/compute/docs/reference/rest/alpha).

## August 13, 2025

Feature

**Generally available:** License Manager is now generally available. License Manager lets you subscribe, manage, and track your third-party license usage on Google Cloud. As an administrator, you can use License Manager to offer per-user licensing products, like Microsoft Office, to your users with no long-term commitments and no overhead of managing compliance.

For more information, see [About License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager).

## August 11, 2025

Feature

**Preview** : The [G4 accelerator-optimized machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) is designed for graphics-intensive workloads such as NVIDIA Omniverse simulations, video transcoding, and virtual desktops. The G4 machine series also provides a cost-effective solution for single-host inference and model tuning.

Powered by the 5th Generation AMD EPYC Turin CPU platform and featuring [NVIDIA RTX PRO 6000 Blackwell Server Edition](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/) GPUs, the G4 machine series offer significant performance improvements over the previous G2 machine series. For available G4 regions and zones, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).

To get started with G4 machine types, contact your Google account team.

Feature

You can attach up to 128 instances to the same Hyperdisk ML volume whose size is between 2 TiB and 16 TiB. The previous limit was 30. For more information, see [Share a disk between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## August 05, 2025

Feature

For Hyperdisk Throughput, the maximum IOPS for a single volume has increased from 600 MiB/s to 2,400 MiB/s. The maximum IOPS for a single volume has increased from 2,400 IOPS to 9,600 IOPS. Hyperdisk Throughput volumes are designed for cost-sensitive workloads, analytics workloads, and workloads that have sequential I/O and large block sizes. For more information, see [About Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput).

Feature

**Generally Available** : The storage-optimized Z3 machine series offers a bare metal (`z3-highmem-192-highlssd-metal`) machine type with 192 vCPUs, 1,536 GB of memory, and 72 TiB of Local SSD storage. 

Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. Z3 uses [Titanium](https://cloud.google.com/titanium) to deliver more compute and memory resources for your workloads by offloading network and I/O processing from the host hardware. To learn more, see [Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).

Deprecated

The Compute Engine feature that deploys containers on VMs during VM creation is deprecated. For more information about the alternative solutions for running containers on VMs and MIGs, see [Compute Engine container startup agent deprecation](https://docs.cloud.google.com/compute/docs/deprecations/container-startup-agent-on-compute).

## July 30, 2025

Feature

**Generally available** : The general purpose C4 machine series now supports the following machine types on Intel's Xeon 6 processor (Granite Rapids):

  * C4 VMs with Titanium Local SSD attached using new machine types: 
    * `c4-standard-*-lssd`
    * `c4-highmem-*-lssd`
  * New bare metal machine types: 
    * `c4-standard-288-metal`
    * `c4-highmem-288-metal`
  * C4 `standard`, `highmem`, and `highcpu` VMs with 144 and 288 vCPUs 



To learn more, see the [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series). 

For more information, about the attached Local SSD disks, see [Machine types that automatically attach Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed).

## July 25, 2025

Change

Hyperdisk Extreme is available in all regions and zones. For more information, see [About Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme).

Change

You can now resize Hyperdisk Balanced volumes twice within a 4-hour window. For more information, see [Capacity changes](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#capacity_changes).

## July 24, 2025

Feature

**Generally available** : The general-purpose C4 machine series now supports Hyperdisk Balanced High Availability. For more information, see [Supported disk types for C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4).

## July 23, 2025

Change

When a regional Persistent Disk volume is fully replicated, Compute Engine now refreshes its replica recovery checkpoint every 15 minutes. 

Learn more about [Regional Persistent Disk replica recovery checkpoints](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-replica-recovery-checkpoint) and [how to use checkpoints to recover a degraded disk](https://docs.cloud.google.com/compute/docs/disks/repd-failover#recover-repd-using-checkpoint).

## July 22, 2025

Feature

**Preview** : Multi-writer support for Hyperdisk Extreme disks. You can give up to 16 instances simultaneous read-write access to the same disk. For more information, see [Share disks between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## July 21, 2025

Feature

**Generally available** : The general-purpose C4D machine series offers the following bare metal machine types:

  * `c4d-standard-384-metal`
  * `c4d-highcpu-384-metal`
  * `c4d-highmem-384-metal`



This is the first machine series to offer AMD-based bare metal instances. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. C4D uses [Titanium](https://cloud.google.com/titanium) to deliver more compute and memory resources for your workloads by offloading network and I/O processing from the host hardware. To learn more, see [C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#c4d-metal).

## July 18, 2025

Feature

**Generally available** : You can create instant and standard snapshots from Hyperdisk volumes in multi-writer mode. You can also clone Hyperdisk volumes in multi-writer mode.

For more information, see [Share disks between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## July 15, 2025

Change

Compute flexible committed use discounts (CUDs) offer expanded coverage by supporting the following resources and services:

  * Memory-optimized M1, M2, M3, and M4 VMs
  * Compute-optimized H3 instances
  * Cloud Run services with request-based billing
  * Cloud Run Functions



To receive the expanded coverage for flexible CUDs, you must opt in to the new spend-based CUD model. Cloud Billing accounts that meet specific criteria are automatically opted into the new model. On January 21, 2026, all remaining accounts will automatically migrate to the new model. You can opt in before that date to start receiving the expanded coverage. To learn more about the new model and the opt-in details, see [Spend-based CUDs program improvements](https://docs.cloud.google.com/docs/cuds-multiprice).

To learn more about this change and how your flexible CUDs apply after you opt in, see [Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

## July 02, 2025

Feature

**Preview** : You can reserve GPU VMs that use A4 and A3 Ultra machine types by using future reservations in calendar mode. This feature lets you reserve up to 80 GPU VMs for up to 90 days to obtain capacity for the following workloads:

  * Model pre-training jobs

  * Model fine-tuning jobs

  * High performance computing (HPC) simulation workloads

  * Short-term expected increases in inference workloads




For more information, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

Feature

**Generally available** : You can create Z3 VMs using smaller machine types, ranging in size from 14 to 88 vCPUs. Also, Z3 now offers `-standardlssd` and `-highlssd` predefined machine types. These new machine types have different amounts of Local SSD capacity per vCPU.

When you use Local SSD disks with Z3 VMs, you can receive committed use discounts (CUDs) without needing to [attach reservations to your commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#committed_resources_that_require_attached_reservations).

For more information, see [Storage-optimized machines](https://docs.cloud.google.com/compute/docs/storage-optimized-machines).

Feature

**Preview** : The general purpose C4 machine series now supports the following machine types on Intel's Xeon 6 processor (Granite Rapids):

  * C4 VMs with Titanium Local SSD attached using two new machine types: 
    * `c4-standard-*-lssd`
    * `c4-highmem-*-lssd`
  * Three new bare metal machine types: 
    * `c4-standard-288-metal`
    * `c4-highcpu-288-metal`
    * `c4-highmem-288-metal`
  * C4 `standard`, `highmem`, and `highcpu` VMs with 144 and 288 vCPUs 



To learn more, see the [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series). 

For more information, about the attached Local SSD disks, see [Machine types that automatically attach Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed).

## June 30, 2025

Feature

**Generally available** : You can now modify licenses attached to your disks. Previously, licenses on disk resources were immutable. You had to delete and recreate disks, or engage our support team to change licenses.

This feature provides greater flexibility for managing your disk licenses. You can now:

  * Append, remove, replace, and view the history of license updates.
  * Perform in-place license upgrades, such as [Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu), using the `gcloud` CLI and REST.
  * [Switch from PAYG to BYOS billing](https://docs.cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos) models.
  * Review [license changes and restrictions](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions) and [append a RHEL ELS](https://docs.cloud.google.com/compute/docs/images/premium/rhel/append-els-licenses) license to a newer version.



For more information on how to manage licenses, see [Manage licenses](https://docs.cloud.google.com/compute/docs/licenses/manage).

## June 27, 2025

Feature

**Generally available** : You can specify a custom ephemeral external IPv6 address when creating an instance. For more information, see [Create instances that use IPv6 addresses](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance).

## June 13, 2025

Feature

**Generally available** : General purpose [C4D machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series), powered by the fifth generation AMD EPYC processors (Turin) and Google Titanium, are generally available.

C4D is designed to run mission-critical workloads including web app and game servers, AI inference, web serving, video streaming, and data centric applications like analytics, relational, and in-memory databases.

C4D is available in `standard`, `highmem`, and `highcpu` machine types and supports only Google Cloud Hyperdisk storage and Titanium SSD. To learn more about C4D, refer to the [C4D release blog](https://www.google.com/url?q=https://cloud.google.com/blog/products/compute/c4d-vms-unparalleled-performance-for-business-workloads). For details about where you can create C4D instances, see the [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) page.

Feature

**Preview** : Dynamic NICs let you add or remove network interfaces to or from an instance without having to restart or recreate the instance.

You can also use Dynamic NICs when you need more network interfaces. The maximum number of vNICs for most machine types in Google Cloud is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

  * [Multiple network interfaces overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)
  * [Create VM instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)



## June 11, 2025

Feature

**Preview** : The storage-optimized Z3 machine series offers a bare metal (`-metal`) machine type with 192 vCPUs. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. To learn more, see [Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).

## June 10, 2025

Security

A vulnerability (CVE-2025-2884) affecting Shielded VMs using virtual Trusted Platform Module (vTPM) was discovered and is being addressed. For more information, see the [GCP-2025-031 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2025-031).

## June 06, 2025

Change

**Generally available** : The [Security Risk Overview dashboard for Compute Engine](https://docs.cloud.google.com/compute/docs/monitor-security-risks-console) is generally available. In addition, it provides a **Top CVE findings** table that lists the most severe CVEs that affect your Compute Engine instances.

## June 04, 2025

Feature

**Preview** : OS Login now supports connections from SSH certificates in addition to SSH keys. For more information, see [Set up OS Login to require SSH certificates for SSH connections](https://docs.cloud.google.com/compute/docs/oslogin/certificates).

## June 03, 2025

Feature

**Preview** : You can enable your project to send HTTP requests to a Compute Engine feature alpha URI. This action lets you test and develop with experimental features in the alpha stage using REST. For more information, see [Use the Compute Engine API in alpha](https://docs.cloud.google.com/compute/docs/reference/rest/alpha).

## June 02, 2025

Feature

**Preview** : The general-purpose C4D machine series offers bare metal (`-metal`) machine types with 384 vCPUs. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. To learn more, see [C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).

## May 26, 2025

Feature

**Generally Available** : [A3 Ultra accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) machine types are now available in the following additional regions and zones:

APAC

  * Mumbai, India: `asia-south1-b`
  * Delhi, India: `asia-south2-c`



Europe:

  * St. Ghislain, Belgium: `europe-west1-b`
  * Eemshaven, Netherlands: `europe-west4-b`



North America:

  * Council Bluffs, Iowa: `us-central1-b`
  * Moncks Corner, South Carolina: `us-east1-d`
  * Ashburn, Virginia,: `us-east4-b`
  * The Dalles, Oregon: `us-west1-c`
  * Dallas, Texas: `us-south1-b`



For a complete list of A3 Ultra regions and zones, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).

## May 23, 2025

Feature

**Generally available** : Resource-based committed use discounts (CUDs) are available for M4 machine types that come with 6 TB of memory. Learn more about how to [purchase commitments for M4 6 TB machine types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchasecommitment).

## May 22, 2025

Feature

**Public preview** : The general-purpose C4D machine series offers Local SSD (`-lssd`) machine types with up to 12 TiB of Titanium SSD. Learn more about [C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series) and the available [C4D Local SSD machine types](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed).

## May 20, 2025

Feature

**Preview:** You can edit your instance's configuration to change the Backup and DR backup plan that is applied to that instance. Backup and DR backup plans let you create rule-based, indelible backups of your Compute Engine instances and store those backups in a secure and isolated storage locations. By changing your instance's backup plan, you can adapt your data protection strategy to match your changing operational requirements.

For more information, see [Change your instance's backup plan](https://docs.cloud.google.com/compute/docs/instances/change-backup-plan-for-instance). To learn more about Backup and DR backup plans, see [Backup and DR Service overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).

Feature

**Preview** : You can use future reservation requests in calendar mode to reserve capacity for creating VMs with TPUs attached. This feature helps you obtain and reserve high-demand resources to run generative artificial intelligence (AI), machine learning (ML), or high performance computing (HPC) workloads. 

For more information, see the following pages: 

  * [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview)

  * [Create a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode)




## May 15, 2025

Feature

**Public Preview** : You can use the flex-start provisioning model to increase your chances of obtaining GPUs for short-duration workloads. You can use flex-start with resize requests in managed instance groups (MIGs). 

For more information, see the following:

  * [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig)

  * [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models)




## May 13, 2025

Security

Google has applied fixes for a vulnerability (CVE-2024-45332) affecting the following Intel processors: CascadeLake, Ice Lake XeonSP, Ice Lake XeonD, Sapphire Rapids and Emerald Rapids. For more information, see the [GCP-2025-025 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2025-025).

## May 12, 2025

Security

A vulnerability (CVE-2024-28956) affecting Intel Cascade Lake processors and Intel Ice Lake processors was discovered and is being addressed. For more information, see the [GCP-2025-024 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2025-024).

Feature

**Public preview** : In a managed instance group (MIG), you can use a health check to monitor your application health without triggering repairs of an unhealthy VM, if the application fails the health check. You can prevent the MIG from repairing an unhealthy VM by turning off autohealing. For more information, see [Turn off repairs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).

## May 09, 2025

Feature

**Public preview:** A [Security Risk Overview dashboard for Compute Engine](https://docs.cloud.google.com/compute/docs/monitor-security-risks-console), available in the Google Cloud console, shows the top Security Command Center findings that affect your Compute Engine resources.

## April 28, 2025

Feature

**Generally available:** The [Memory-optimized machine family](https://docs.cloud.google.com/compute/docs/memory-optimized-machines) has added two new M4 machine types:

  * m4-megamem-28
  * m4-ultramem-224



The m4-megamem-28 offers 28 vCPUs with 372 GB of memory. The m4-ultramem-224 offers 224 vCPUs with 5,952 GB of memory.

Feature

**Public preview** : Resize request in a managed instance group (MIG) lets you specify the name of the VMs to create all at once. This feature helps if your orchestration mechanism or workload requires specific VM naming. For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

## April 25, 2025

Feature

**Public Preview:** License Manager lets you subscribe, manage, and track your third-party license usage on Google Cloud. As an administrator, you can use License Manager to offer per-user licensing products, like Microsoft Office, to your users with no long-term commitments and no overhead of managing compliance.

For more information, see [About License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager).

## April 22, 2025

Feature

**Public Preview** : General purpose [C4D machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series) have reached Public Preview. C4D is powered by the fifth generation AMD EPYC processor (Turin) and Google Titanium.

C4D is designed to run mission critical workloads including web app and game servers, AI inference, web serving, video streaming, and data centric applications like analytics, relational, and in-memory databases.

C4D is available in `standard`, `highmem`, and `highcpu` machine types and only supports Google Cloud Hyperdisk storage.

To learn where to create C4D instances, see the [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) page.

## April 21, 2025

Feature

**Generally available** : Compute flexible committed use discounts (CUDs) are available for the [sole-tenancy premium](https://docs.cloud.google.com/compute/sole-tenant-pricing?e=48754805&hl=en#nodes) that you pay for eligible sole-tenant node types. Flexible CUDs add flexibility to your Compute Engine spending capabilities by eliminating the need to restrict your commitments to a single project, region, or machine series.

For more information, see [Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

## April 04, 2025

Deprecated

On June 30th, 2024, CentOS 7 will reach end of support and the images marked deprecated on Google Cloud. If you use CentOS 7 images in your project, review [CentOS end of support guidance ](https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance).

Deprecated

On June, 30, 2024, Red Hat Enterprise Linux (RHEL) 7 will reach end of support and the images marked deprecated on Google Cloud. If you use RHEL 7 images in your project, review [RHEL end of support](https://docs.cloud.google.com/compute/docs/eol/rhel-eol).

## April 02, 2025

Feature

**Generally available** : You can manage OS policy assignments across projects and zones at scale in large organizations using the **OS policy orchestrator** feature in VM Manager. OS policy assignment was previously available only for zonal resources in a project. For more information, see [About OS Policy Orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/about-policy-orchestrator).

## March 31, 2025

Deprecated

Compute Engine provides the [interactive serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) for troubleshooting malfunctioning instances. The serial console SSH key endpoint is deprecated and a new serial SSH key endpoint is available. For more information, see [Serial console SSH host key endpoint deprecation](https://docs.cloud.google.com/compute/docs/deprecations/serial-console-ssh-host-key-endpoint).

## March 26, 2025

Feature

**Generally available** : You can use instant snapshots to take in-place backups of the following types of disks:

  * Hyperdisk Balanced
  * Hyperdisk Balanced High Availability
  * Hyperdisk Extreme 



Instant snapshots are ideal for rapid data restoration only within the same location as the source disk. You can use an instant snapshot to create a new disk in under a minute. For more information, see [About instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

Feature

**Generally available** : You can specify a custom ephemeral internal IPv6 address when creating an instance. For more information, see [Create instances that use IPv6 addresses](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance).

Feature

**Generally available** : Asynchronous Replication is now generally available for Hyperdisk Balanced, Hyperdisk Balanced High Availability, and Hyperdisk Extreme disks. Asynchronous Replication provides low-RPO and low-RTO block storage replication for cross-region disaster recovery. For more information, see [About Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).

## March 25, 2025

Fixed

**Resolved:** Fixed the issue that caused Persistent Disks attached to VMs with `n2d-standard-64` machine types to inconsistently reach the maximum performance limit of 100,000 IOPS.

For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#resolved_disks_attached_to_vms_with_n2d-standard-64_machine_types_dont_consistently_reach_performance_limits).

## March 24, 2025

Feature

**Generally available** : Multi-writer support for Hyperdisk Balanced High Availability disks. You can give up to 8 VMs, across two zones, simultaneous read-write access to the same disk. For more information, see [Share disks between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## March 21, 2025

Feature

**Generally available** : Resource-based committed use discounts (CUDs) are available for licenses of RHEL operating system images. You can purchase commitments with a 1-year plan for these licenses and receive up to 20% discounts over on-demand prices.

To learn how to purchase these commitments, see [Purchase commitments for licenses](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchaselicensecommitment). For pricing information, reach out to your [Technical account manager (TAM)](https://cloud.google.com/tam).

## March 19, 2025

Feature

**Preview** : You can create regionally scoped snapshots. Setting a regional scope ensures that all snapshot data and the metadata necessary to use the snapshot are co-located within the scoped region. Regionally scoped snapshots also support additional location control by letting you restrict allowed snapshot creation and restore locations.

For more information, see [Snapshot scopes](https://docs.cloud.google.com/compute/docs/disks/snapshots#snapshot-scopes).

## March 17, 2025

Feature

**Generally available** : The [A4 accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) is now generally available. A4 instances are powered by NVIDIA B200 GPUs and provide up to 3x performance of previous GPU instance types for most GPU accelerated workloads. A4 is especially recommended for ML training workloads at large scales. A4 is available in the `a4-highgpu-8g` machine type in the `us-central1-b` zone.

To create A4 instances, you must either use AI Hypercomputer to request capacity and create VMs or clusters, or use Spot VMs. For detailed instructions, see [Create an A3 Ultra or A4 VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4).

## March 14, 2025

Feature

**Generally available:** The **Create an instance** page in the Google Cloud console has a **Data protection** pane where you can specify how to back up and replicate your data. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options) and [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).

Feature

**Generally available** : Memory-optimized [M4 VMs](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_series) are now generally available. M4 3T VMs run on Intel's 5th generation Emerald Rapids CPU. They offer up to 224 vCPUs with up to 3 TB of memory. 

M4 is available in five predefined machine types. The megamem VMs have a GB/vCPU ratio of 13.29:1 and the ultramem VMs have a GB/vCPU ratio of 25.57:1.

## March 10, 2025

Feature

**Generally available** : Compute flexible committed use discounts (CUDs) are available for Local SSD disks that you attach to instances of eligible machine types. Flexible CUDs add flexibility to your Compute Engine spending capabilities by eliminating the need to restrict your commitments to a single project, region, or machine series.

For more information, see [Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

Feature

**Generally available** : Configure the host error detection time, which is the maximum amount of time Compute Engine waits to restart or terminate an instance after detecting that the instance is unresponsive. For more information, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).

## March 04, 2025

Feature

**Generally available:** Stockholm, Sweden, Europe `(europe-north2-a,b,c)` has launched with [N4, C3D highmem, C4 highmem, and E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines) machine types available in all three zones. For more information, see [Cloud locations](https://cloud.google.com/about/locations) and [VM instance pricing](https://cloud.google.com/products/compute/pricing).

## February 14, 2025

Change

Starting as soon as February 14, 2025, projects might start seeing a **Data protection** pane on the **Create an instance page** in the Google Cloud console. If you see the **Data protection** pane, it selects an option to automatically back up data by default, which is recommended to make sure you can recover your data if it's lost due to unforeseen events. The backup incurs additional costs according to either [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing) or [Compute Engine pricing for disk snapshots](https://cloud.google.com/compute/disks-image-pricing).

If desired, you can select a different backup option (or disable backups) before you finish creating an instance. You can also change which backup option your project selects by default. For more information, see [Configure the default backup setting for the console](https://docs.cloud.google.com/compute/docs/disks/default-backup).

Feature

You can [apply a Backup and DR Service backup plan during instance creation](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan). Use backup plans to centralize backup management of instances across projects and improve cyber resilience through immutable and indelible backups to backup vaults.

## January 29, 2025

Feature

**Preview:** You can now modify which machine types are recommended, so that the generated recommendations only include your preferred machine series. You can also change the metrics used to generate memory recommendations to improve the accuracy of the recommendations. For more information, see [Configure machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-machine-type-recommendations).

## January 24, 2025

Feature

**Preview** : To prevent data loss or corruption when a compute instance is stopped, you can enable graceful shutdown in the instance. This setting gives the guest OS up to one hour to finish running tasks. Gracefully shutting down an instance is helpful when, for example, your database needs time to complete active transactions, your multiplayer session needs time to end properly, or you want to cleanly shutdown a high performance computing (HPC) job. 

For more information, see the following pages:

  * [Graceful shutdown overview](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview)

  * [Enable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/enable-graceful-shutdown)

  * [View graceful shutdown in a Compute Engine instance ](https://docs.cloud.google.com/compute/docs/instances/view-graceful-shutdown)

  * [Disable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown)




## January 20, 2025

Feature

**Generally available** : Managed instance groups (MIGs) let you create pools of suspended and stopped virtual machine (VM) instances. You can manually suspend and stop VMs in a MIG to save on costs, or use suspended and stopped pools to speed up scale out operations of your MIG. For more information, see [About suspending and stopping VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig).

## January 17, 2025

Feature

Compute Engine is enabled for use with Cloud KMS Autokey.

Using keys generated by Autokey can help you consistently align with industry standards and recommended practices for data security, including the HSM protection level, separation of duties, key rotation, location, and key specificity. Keys requested using Autokey function identically to other Cloud HSM keys with the same settings.

For more information, see [About disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption). To learn more about Cloud KMS Autokey, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

## January 16, 2025

Feature

**Generally available** : Google Axion Processor-based [C4A VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) with [Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types) are now generally available. Part of our general-purpose machine family, these instances come with up to 6 TiB of Titanium SSD disks. Titanium SSD is our latest generation of Local SSD. It uses [Titanium I/O offload processing](https://cloud.google.com/titanium) and offers enhanced SSD security, performance, and management.

## January 15, 2025

Issue

The metadata server might display old `physicalHost` metadata if a VM experiences a host error. For more information, see [known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#the_metadata_server_might_display_old_physicalhost_vm_metadata).

## January 13, 2025

Fixed

**Resolved:** Fixed the issue that caused missing symlinks for Local SSD devices on C3 and C3D VMs running SUSE Linux.

For more information, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#resolved_missing_symlinks_for_local_ssd_devices_on_c3_and_c3d_vms_running_suse_linux).

## December 31, 2024

Feature

**Generally available** : The [A3 Ultra accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) is now generally available. A3 Ultra VMs are powered by NVIDIA H200 Tensor Core GPUs and support the new Titanium ML network adapter, which delivers non-blocking 3.2 Tbps of GPU-to-GPU traffic with RDMA over Converged Ethernet (RoCE). A3 Ultra VMs are ideal for foundation ML model training and serving. The A3 Ultra machine type is available in the following region and zone:

  * St. Ghislain, Belgium, Europe - `europe-west1-b`



When provisioning A3 Ultra machine types, you must use [Hypercompute Cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/hypercompute-cluster) to request capacity and create VMs or clusters. To get started see [Overview of creating VMs and clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) in the AI Hypercomputer documentation.

## December 17, 2024

Feature

**Preview** : You can create instances that use only IPv6 IP addresses. For more information, see [IP addresses](https://docs.cloud.google.com/compute/docs/networking/network-overview#ip-addresses).

## December 16, 2024

Deprecated

The [A3 Edge accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms) is no longer available in Turin, Italy: `europe-west12-b`. For a list of available regions and zones, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).

## December 11, 2024

Change

[C3 bare metal instances](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) are available in the following additional zones:

  * **c3-highcpu-192-metal** : asia-southeast1-a and c, europe-west4-c, us-east1-d, us-east4-c, us-east5-a, us-west1-a and b

  * **c3-standard-192-metal** : europe-west1-b and c, europe-west4-b and c, us-east1-d, us-east4-a, us-west1-a and b

  * **c3-highmem-192-metal** : europe-west4-c, us-east4-a and c, us-west1-a and b




## December 10, 2024

Feature

**Generally available** : Instance flexibility in a managed instance group (MIG) lets you configure multiple machine types in the group. This can improve resource availability for applications that require large-scale capacity and high-demand hardware. Support for Terraform has also been added. For more information, see [About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

## December 09, 2024

Fixed

Fixed the issue causing incorrect detection of CPU load on T2D machine series VMs in managed instance groups (MIGs). This issue affected MIG autoscaling based on CPU utilization in projects that were created before June 18, 2023.

## December 03, 2024

Feature

**Generally available** : [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks#hdb-ha) provides cross-zonal, synchronous replication for your disk data, offering the best set of options for RPO, RTO, and performance.

## November 26, 2024

Feature

**Preview:** Use the disk performance status metric to monitor the health of your Hyperdisk or Persistent Disk volumes. This metric indicates whether your disks might be affected by adverse events within Compute Engine.

To learn more, see [Monitor disk health](https://docs.cloud.google.com/compute/docs/disks/disk-health).

## November 19, 2024

Change

The documentation has been updated to clarify that future reservation requests don't support E2 machine types. To reserve VMs that use E2 machine types, use on-demand reservations instead.

For more information, see [Restrictions on creation](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#restrictions-create).

## November 18, 2024

Feature

**Generally available** : Queretaro, Mexico, North America (`northamerica-south1-a,b,c`) has launched with [E2, N4, C4, and C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines) VMs available in all three zones. For more information, see [Global Locations](https://cloud.google.com/about/locations) and [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).

## November 13, 2024

Feature

**Preview** : The OS policy orchestrator feature in VM Manager lets you manage OS policy assignments across projects and zones at scale in large organizations. OS policy assignment was previously available only for zonal resources in a project. For more information, see [About OS Policy Orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/about-policy-orchestrator).

## November 05, 2024

Feature

**Generally available** : An updated version of the gVNIC driver for Windows offers improved network performance and support for Jumbo frames. For more information, see [Update to the latest gVNIC driver for Windows](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#windows-os-upgrade).

## November 04, 2024

Feature

**Preview** : You can create GPU VMs all at once in a regional managed instance group (MIG) by using resize requests. This feature was previously available only for zonal MIGs. For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

## October 30, 2024

Feature

**Generally available** : General purpose [C4A Arm VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) on Google's custom-built Axiom processors. C4A VMs are available as predefined configurations in sizes ranging from 1 vCPU to 72 vCPUs and up to 576 GB of DDR5 memory. C4A uses Google Cloud's latest generation storage options including Hyperdisk Balanced and Hyperdisk Extreme.

C4A VMs are available in the following regions and zones:

  * Singapore - asia-southeast1-a,b,c
  * Belgium - europe-west1-b,c,d
  * Frankfurt - europe-west3-a,b,c
  * Netherlands - europe-west4-a,b,c
  * Iowa - us-central1-a,b,c
  * South Carolina - us-east1-b,c,d
  * Virginia - us-east4-a,b,c



Feature

**Generally available** : You can autoscale a regional MIG with a BALANCED target distribution shape. With the BALANCED shape, the autoscaler is aware of the capacity in each zone and creates VMs in zones that have resource availability. For more information, see [Autoscaling a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#autoscaling_a_regional_mig).

## October 25, 2024

Feature

**Generally available** : The [A3 Edge accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms) is now available. The A3 Edge machine type has NVIDIA® H100 80GB GPUs attached and provides up to 800 Gbps of network bandwidth speed depending on the region. A3 Edge VMs are ideal for inference or training ML workloads that require a single node. The A3 Edge machine type is available in the following regions and zones:

  * APAC 
    * Tokyo, Japan: `asia-northeast1-c`
    * Seoul, South Korea: `asia-northeast3-a,c`
    * Mumbai, India: `asia-south1-c`
  * Europe 
    * London, England: `europe-west2-b`
    * Frankfurt, Germany: `europe-west3-a`
    * Eemshaven, Netherlands: `europe-west4-b`
    * Milan, Italy: `europe-west8-c`
    * Paris, France: `europe-west9-c`
    * Turin, Italy: `europe-west12-b`
  * North America 
    * Toronto, Ontario: `northamerica-northeast2-c`



To get started with A3 Edge VMs, see [Create an A3 VM](https://docs.cloud.google.com/compute/docs/gpus/gpudirect).

## October 23, 2024

Feature

**Generally available** : You can extend the term lengths of your resource-based commitments beyond the preset 1 or 3 years and choose custom term lengths such as 2, 3.5, or 5.5 years. Term extensions let you tailor commitments to match your resource usage needs and keep receiving committed use discounts (CUDs) for a longer time.

For more information, see [Extend the term length of commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).

## October 16, 2024

Deprecated

**End of life:** On October 31, 2024, SLES 12 SP5 and SLES 12 SP5 for SAP are reaching end of life and the images will be deprecated on Google Cloud. If you use SLES 12 SP5 or SLES 12 SP5 for SAP images in your project, review [Long Term Service Support Pack (LTSS) options](https://docs.cloud.google.com/compute/docs/images/premium/sles-faq#ltss).

## October 15, 2024

Feature

**Generally available** : In addition to the A3 High machine type that has 8 NVIDIA H100 GPUs attached, we now have smaller machine types available that have 1, 2, or 4 NVIDIA H100 GPUs attached. These smaller machine types are ideal for workloads such as inference, simulations, and small-scale training.

To get started, review [A3 High machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms).

## October 09, 2024

Feature

**Public preview** : Instance flexibility in a managed instance group (MIG) lets you configure multiple machine types in the group. This can improve resource availability for applications that require large-scale capacity and high-demand hardware. For more information, see [About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

## October 08, 2024

Feature

**Preview** : An updated version of the gVNIC driver for Windows offers improved network performance and support for Jumbo frames. For more information, see [Update to the latest gVNIC driver for Windows](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#windows-os-test).

## September 30, 2024

Feature

**Preview:** Multi-writer support for Hyperdisk Balanced High Availability disks. You can allow up to 8 VMs simultaneous read-write access to the same disk. For more information, see [Share disks between VMs](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## September 26, 2024

Deprecated

OS Login POSIX groups support is deprecated. For more information, see [OS Login POSIX groups support deprecation](https://docs.cloud.google.com/compute/docs/deprecations/oslogin-groups).

## September 18, 2024

Change

You can create a future reservation request by reusing the properties of an existing VM. This lets you consume the auto-created reservations for the future reservation by creating VMs with properties that exactly match the reference VM's properties. For more information, see the following:

  * [Create future reservation requests for a single project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations)

  * [Create shared future reservation requests](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations)




Change

You can determine the number of running VMs and reservations that match the properties of a future reservation request. By subtracting this number from the total count specified in a future reservation request, you can determine the number of reserved VMs that an existing future reservation provisions at its start time. For more information, see [Determine the number of provisioned VMs](https://docs.cloud.google.com/compute/docs/instances/view-future-reservations#determine-provisioned-vms).

Feature

**Generally available** : Hyperdisk Balanced volumes can be [created in Confidential mode](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#encrypt_a_new_hd_confidential) and attached to [Confidential VMs](https://docs.cloud.google.com/compute/docs/about-confidential-vm).

## September 05, 2024

Feature

**Generally available:** Multi-writer support for Hyperdisk Balanced disks. Up to 8 VMs can simultaneously read from and write to the same disk. For more information, see [Share disks between VMs](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## September 02, 2024

Feature

**Generally available** : You can use the performance monitoring unit (PMU) to monitor low-level CPU events and metrics in VMs that use a C4 machine type. Using the PMU is helpful to analyze and optimize the performance of the software running on your VM when running performance-sensitive workloads, such as high-performance computing (HPC) or machine learning (ML) workloads. 

For more information, see the following pages:

  * [PMU overview](https://docs.cloud.google.com/compute/docs/pmu-overview)

  * [Enable the PMU in VMs](https://docs.cloud.google.com/compute/docs/enable-pmu-in-vms)

  * [Manage the PMU in VMs](https://docs.cloud.google.com/compute/docs/manage-pmu-in-vms)




## August 30, 2024

Feature

**Generally available** : When applying a spread placement policy to VMs, you can specify the availability domain in which to place the VMs. Specifying an availability domain lets you decide how to physically locate VMs among each other, which can increase the reliability of your workload by placing VMs in different domains, or try to limit network latency among VMs by placing them in the same domain. Viewing the availability domains of your VMs is also useful for planning, deploying, or upgrading your application, as well as developing your availability SLAs.

For more information, see [Create and apply spread placement policies to VMs](https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies).

Feature

The fleetwide and per-instance **Observability** tabs on the Compute Engine **VM instances** page now include charts for GPU metrics the from NVIDIA Management Library (NVML). To view the fleetwide GPU charts, select **Compute Engine** > **VM instances** > **Observability**. To view the GPU charts for a VM instance, select **Compute Engine** > **VM instances** , click on the name of a VM instance, and then select **Observability**. These charts are available only for VM instances with attached GPUs, with both the Ops Agent and the NVIDIA GPU driver installed. For information about configuring these VMs, see [About the `gpu` metrics](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#receiver-nvml-metrics).

## August 23, 2024

Feature

**Generally available** : Hyperdisk Storage Pools with Advanced Performance provisioning help you to manage the performance needs of your Hyperdisk Balanced and Hyperdisk Throughput disks. By creating your disks in a storage pool, you can provision your disks to handle peak performance spikes while also optimizing costs. For more information, see [Provisioning types for Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#provisioning-types).

## August 19, 2024

Feature

**Generally available** : [General purpose C4 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) on the Intel Emerald Rapids CPU. The C4 machine series offers consistently high performance with up to 192 vCPUs and 1.5 TB of DDR5 memory, and support for [Hyperdisk storage](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

C4 VMs are available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

  * Singapore - `asia-southeast1-a,b`
  * Belgium - `europe-west1-b,c`
  * Netherlands - `europe-west4-a,b,c`
  * Iowa - `us-central1-a,b,c`
  * South Carolina - `us-east1-b,c,d`
  * Virginia - `us-east4-a,b,c`



## August 01, 2024

Feature

**Generally available** : You can use instant snapshots to take in-place disk backups that can be restored to new disks in under a minute.

Instant snapshots are ideal for rapid data restoration within the same location as the source disk. For more information, see [Instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

## July 26, 2024

Change

[Persistent Disk Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) can now replicate up to 12.5 GB per minute per disk of compressed changed blocks, which is an increase from the previous maximum of 2 GB per minute. This increase helps to support scaled production databases and other demanding workloads. You can read more about PD Async Replication performance in the [documentation](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#performance). There is no action required to use the increased performance - new and existing PD Async Replication disks automatically have more headroom to replicate.

## July 16, 2024

Feature

**Generally available** : C3 bare metal machine types are available in the C3 machine series. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. With bare metal instances, you can access all the raw compute resources of the server. For more information, see the [C3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series).

## July 15, 2024

Change

**Compute flexible committed use discounts (CUDs)** —previously known as Compute Engine flexible CUDs—have been expanded to also cover your Cloud Billing account's spend across Google Kubernetes Engine (GKE) and Cloud Run. A single flexible commitment covers your eligible spend across all three services. For more information, see [Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

To learn about how flexible CUDs apply to the other services, see the following:

  * [CUDs documentation for GKE](https://docs.cloud.google.com/kubernetes-engine/cud)
  * [CUDs documentation for Cloud Run](https://docs.cloud.google.com/run/cud)



Feature

**Generally available:** You can limit the run time of VMs, which automatically stops or deletes a VM after a specific time or duration. Limiting your VMs' run times can help you optimize temporary workloads by minimizing costs and releasing quota. For more information, see [Limit the run time of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime) and [Limit the runtime of VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs).

## July 12, 2024

Feature

**Preview** : [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks#hdb-ha) provides cross-zonal, synchronous replication for your disk data, offering the best set of options for RPO, RTO, and performance.

## July 11, 2024

Change

You can only create on-demand reservations of A3 VMs if you create specifically targeted reservations. This restriction doesn't affect reservations that were created before July 11, 2024, which you can continue to consume based on their consumption type.

For more information, see the following pages:

  * [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#restrictions)

  * [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project)

  * [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared)




## July 09, 2024

Feature

**Generally available** : Hyperdisk ML, block storage designed specifically for high-performance AI workloads. Each Hyperdisk ML volume can achieve up to 1,200,000 MBps of throughput. For large-scale training and inference workloads, you can attach a single Hyperdisk ML volume to up to 2,500 VM instances. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

Feature

**Generally available** : You can create GPU VMs in a managed instance group (MIG) by using resize requests. Resize requests help you create VMs all at once and give you higher chances to obtain highly demanded resources such as GPUs.

For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

## July 01, 2024

Fixed

The issue related to creating larger (>90 vCPUs) C3D `standard-lssd` or `highmem-lssd` VM instances.

## June 18, 2024

Change

Preemptible allocation quotas also apply to some temporary GPU VMs. This behavior can help you improve quota obtainability for temporary GPU VMs while maintaining the benefits of uninterrupted run time of the standard provisioning model. For more information, see [GPU VMs and preemptible allocation quotas](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas).

Fixed

The issue related to creating C2 sole tenant nodes with more than 60 CPUs.

## June 17, 2024

Feature

**Generally available** : You can now use the **Require OS Config** organization policy constraint to automatically enable VM Manager for all new VMs in your organization, folder, or project. For more information, see [Enable VM Manager using an organization policy](https://docs.cloud.google.com/compute/docs/manage-os#enable-vmm-org-policy).

## June 14, 2024

Change

[Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) are now available for the [H3 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series).

## June 13, 2024

Feature

**Preview** : C3 bare metal machine types are available in Preview in the C3 machine series. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. With bare metal instances, you can access all the raw compute resources of the server. For more information, see the [C3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series).

## June 12, 2024

Feature

**Preview** : [General Purpose C4 VM](https://docs.cloud.google.com/compute/docs/general-purpose-machines) instances are now available in Public Preview on the [Intel Emerald Rapids CPU](https://docs.cloud.google.com/compute/docs/cpu-platforms). The C4 machine series offers consistently high performance with up to 192 vCPUs and 1.5 TB of DDR5 memory, and support for [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) storage.

Change

**Expanded Hyperdisk Balanced support for M3 and C3 machine types** : The maximum number of Hyperdisk Balanced volumes that you can use with C3 and M3 virtual machines has been increased, as follows:

  * C3 VMs with 4 or 8 vCPUs now support attaching up to 16 Hyperdisk Balanced volumes.
  * C3 VMs with 16 or more vCPUs support 32 Hyperdisk Balanced volumes.
  * M3 virtual machines support up to 32 Hyperdisk Balanced volumes, up from 2. 



For more information, see the documentation for [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_disks) and [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_disks) VMs.

## June 11, 2024

Change

**Generally available** : The [A3 Mega accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) is now available. The A3 Mega machine type has NVIDIA® H100 80GB GPUs attached and provides twice the network bandwidth speed when compared to A3 Standard. A3 Mega VMs can be used to support your large artificial intelligence (AI) models, machine learning (ML), and high performance computing (HPC) workloads. The A3 machine type is available in the following regions and zones:

  * APAC 
    * Singapore: `asia-southeast1-b`
  * Europe 
    * Netherlands: `europe-west4-b,c`
  * North America 
    * Iowa: `us-central1-a,c`
    * Virginia: `us-east4-a,b`
    * Ohio:`us-east5-a`
    * Oregon: `us-west1-a,b`
    * Nevada: `us-west4-a`



To get started with A3 Mega VMs, see [Run large-scale model training and fine-tuning](https://docs.cloud.google.com/compute/docs/gpus/overview#large-scale-ai).

Feature

C3 and C3D VMs are available in the following [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available):

C3:

  * `asia-northeast1-b` Tokyo, Japan
  * `europe-west3-b,c` Frankfurt, Germany
  * `us-west1-a,b` The Dalles, OR
  * `us-west2-a` Los Angeles, CA
  * `us-south1-a` Dallas, TX



C3D:

  * `australia-southeast1-c` Sydney, Australia
  * `europe-west3-c` Frankfurt, Germany
  * `us-west4-a` Las Vegas, NV



## June 05, 2024

Issue

You can't provision C2 sole tenant nodes with 60 vCPUs. For details, see [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues).

## June 04, 2024

Feature

You can now order and request quota for X4 bare metal instances. You create bare metal instances using a new predefined machine type for the X4 memory-optimized machine series. X4 instances can be used to host the largest production SAP HANA databases. For more information, see the [X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series).

## May 31, 2024

Issue

Creating a larger (>90 vCPUs) C3D `standard-lssd` or `highmem-lssd` VM results in an error message. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues) for the workaround. Larger C3D VMs that don't require `-lssd` are not impacted.

## May 15, 2024

Feature

**Generally Available:** Advanced maintenance control for sole-tenancy lets you control planned maintenance events for sole-tenant node groups and minimize maintenance-related disruptions. This feature is available only for sole-tenant node groups. To use this feature with your existing virtual machines, you must first move your VMs to sole-tenant node groups that have advanced maintenance control enabled.

The advanced maintenance control for sole-tenancy feature lets you:

  * Check for maintenance events scheduled for a sole-tenant node 28 days in advance.
  * Trigger maintenance immediately or schedule it for later. Note that if you trigger maintenance immediately, the maintenance takes place within 6 hours from the time you trigger the request.



For more information, see [Advanced maintenance control for sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control).

## May 08, 2024

Feature

**Preview** : You can now use the **Require OS Config** organization policy constraint to automatically enable VM Manager for all new VMs in your organization, folder, or project. For more information, see [Enable VM Manager using an organization policy](https://docs.cloud.google.com/compute/docs/manage-os#enable-vmm-org-policy).

## April 30, 2024

Deprecated

The global serial console gateway is deprecated. For more information, see [Global serial console gateway deprecation](https://docs.cloud.google.com/compute/docs/deprecations/global-serial-console).

## April 29, 2024

Breaking

Starting the week of April 29, 2024, when you limit the run time of a standalone VM or a VM in a managed instance group (MIG), the following changes take effect:

  * When you stop or suspend a VM that has a time limit, the time limit will no longer be automatically removed. Whenever you start or resume the VM, its time limit is reapplied until you update or remove the time limit. If a VM's time limit is defined as a specific time and that time has passed, you can't rerun the VM until you update or remove its time limit.

  * When a VM in a MIG reaches its time limit, the MIG deletes that VM instead of repairing it.




For more information, see [Limit the run time of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime) and [Limit the run time of VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs).

## April 26, 2024

Feature

**Generally available** : [Zonal metadata](https://docs.cloud.google.com/compute/docs/metadata/overview#zonal-metadata) (previously known as project zonal metadata) is custom metadata that you define at a zonal scope within a project and provides information about VMs in that specific zone. Zonal metadata helps you with fault isolation and provides greater reliability. By setting custom zonal metadata, you gain more control over the metadata for VMs in your project and limit the impact of any incorrect metadata updates to VMs within a specific zone.

To get started working with zonal metadata, see [Set custom zonal metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-zonal-metadata).

## April 19, 2024

Feature

[General purpose C3 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) are now available in Sydney, `(australia-southeast1-c)`.

## April 16, 2024

Feature

**Generally available** : Z3 VMs, which offer the latest compute, networking, and storage innovations in one platform with a particular focus on high density, high performing Local SSD are now available on Compute Engine. For more information, see [Storage-optimized machine family](https://docs.cloud.google.com/compute/docs/storage-optimized-machines).

Feature

**Generally available** : Hyperdisk Balanced is available with [M1 and M2 VMs](https://docs.cloud.google.com/compute/docs/memory-optimized-machines). Hyperdisk Balanced is a good fit for a wide range of use cases such as LOB applications, and medium-tier databases that don't require the performance of Hyperdisk Extreme. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

## April 09, 2024

Feature

**Generally available:** [N4 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) are generally available on the [Intel Emerald Rapids CPU](https://docs.cloud.google.com/compute/docs/cpu-platforms) with 640 GB DDR5 memory. The N4 machine series offers predefined and custom machine types with extended memory and Hyperdisk Balanced storage.

N4 VMs are available in limited [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

See [VM pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family) for cost details.

Feature

**Generally available** : You can plan ahead for VM maintenance on [M1, M2, and M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines) machine types by [viewing their maintenance schedule notifications](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event). For specific machine types within these families, you can also [trigger VM maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) ahead of schedule.

## April 08, 2024

Announcement

**Pricing change** : On January 26, 2024, [Red Hat announced a price model update](https://www.redhat.com/en/blog/red-hat-enterprise-linux-scalable-pricing-cloud-partners-announcement) on RHEL and RHEL for SAP for all Cloud providers that scales image subscription costs according to vCPU count. The new pricing model will be reflected on Compute Engine starting July 1, 2024.

For the pricing changes, see [Premium images](https://docs.cloud.google.com/compute/all-pricing#premiumimages). To learn about your options to optimize subscription costs, see the [Red Hat Enterprise Linux pricing FAQs](https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq#pricing_faqs).

Announcement

On January 26, 2024, [Red Hat announced a price model update](https://www.redhat.com/en/blog/red-hat-enterprise-linux-scalable-pricing-cloud-partners-announcement) on RHEL and RHEL for SAP for all Cloud providers that scales image subscription costs according to vCPU count. As a result, starting July 1, 2024, any active commitments for RHEL and RHEL for SAP licenses will be canceled and will not be charged for the remainder of the commitment's term duration. 

Google Cloud has notified and will issue [adjustments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#viewing_credits_and_adjustments) to affected customers.

## April 04, 2024

Feature

**Generally available** : Simplify block storage management for Compute Engine instances with Hyperdisk Storage Pools. A Hyperdisk Storage Pool is a pre-purchased collection of disk capacity, throughput, and IOPS which you can then provision to your applications as needed. By managing disks in aggregate, you can save costs while achieving expected capacity and performance growth. For more information, see [About Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools).

## April 03, 2024

Security

Compute Engine is not affected by CVE-2024-3094. For more information, see the [GCP-2024-021 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2024-021).

## March 22, 2024

Feature

**Generally available** : Disaster recovery with [Persistent Disk Async Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) has been expanded to allow you to replicate data on a disk in one region to any other region [within the same continent](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).

Also, the following performance and capacity enhancements are available:

  * Data replication change rate increased to 2 GiB/min from 250 MB/min.
  * Maximum provisioned disk size increased to 32 TB from 5 TB per disk.
  * The number of disks per project increased to 1000 from 100.
  * The number of disks per consistency group increased to 128 from 64.



## March 21, 2024

Feature

**Generally available** : In a managed instance group (MIG), you can set metadata and labels for all VMs in the group without the need to create a new instance template. For more information, see [Override instance template properties with an all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic).

Feature

**Generally available** : In a managed instance group (MIG), you can turn off repairs to inspect failed and unhealthy VMs, to implement your own repair logic, or to monitor the application health without triggering repairs by MIG. For more information, see [Turn off repairs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).

## March 18, 2024

Announcement

**Generally available** : The organization-wide [patch status dashboard](https://docs.cloud.google.com/compute/docs/os-patch-management/view-patch-summary) and organization-wide [OS policy compliance reports](https://docs.cloud.google.com/compute/docs/os-configuration-management/view-compliance#policy-summary) in VM Manager are now generally available.

## March 13, 2024

Feature

**Generally available** : You can use SSH-in-browser to connect to TPU VMs. For more information, see [Connecting to a Cloud TPU](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm#tpu-connect).

## March 12, 2024

Feature

**Generally available** : You can scale a single VM into a managed instance group (MIG), which is a group of VMs that you can manage as a single entity. A MIG can make your workload scalable and highly available using features like autoscaling, autohealing, regional (multiple zones) deployment, and automatic updating. 

For more information, see [Create a MIG from an existing VM](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm).

## March 11, 2024

Feature

**Generally available** : Hyperdisk Balanced is available with C3 and H3 VMs. Hyperdisk Balanced is a good fit for a wide range of use cases such as LOB applications, web applications, and medium-tier databases that don't require the performance of Hyperdisk Extreme. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

## February 21, 2024

Feature

**Preview** : With managed workload identities for Compute Engine, you can implement mutually authenticated and encrypted communications between any two Compute Engine VMs. Workload applications running on the configured VMs can use the X.509 credentials for per-VM mTLS. These mTLS certificates are automatically rotated and managed for you by Certificate Authority Service.

For more information, see [Authenticate workloads to other workloads over mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).

## February 15, 2024

Feature

**Preview** : You can now use SSH-in-browser to connect to VMs using security keys with OS Login. For more information, see [Enable security keys with OS Login](https://docs.cloud.google.com/compute/docs/oslogin/security-keys).

## February 13, 2024

Feature

**Generally available** : The following quotas and metrics are now available to help you monitor the usage and limits for Compute Engine concurrent operation quotas:

  * Quotas for global concurrent operations (metric - `compute.googleapis.com/global_concurrent_operations`): 
    * `Concurrent global operations per project`
    * `Concurrent global operations per project operation type`
  * Quotas for regional concurrent operations (metric: `compute.googleapis.com/regional_concurrent_operations`): 
    * `Concurrent regional operations per project`
    * `Concurrent regional operations per project operation type`



For more information, see [Concurrent operation quotas](https://docs.cloud.google.com/compute/operations-quota).

## February 08, 2024

Feature

**Generally available** : Hyperdisk Throughput is available with the following VMs:

  * A3
  * C3
  * C3D
  * G2
  * H3
  * M3



Hyperdisk Throughput support for Z3 VMs is also available in Preview.

Also, the maximum number of Hyperdisk Throughput volumes you can attach to a VM has been increased. See [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#hyperdisk-capacity) for more information. 

Hyperdisk volumes are durable network storage devices that your VMs can access, similar to Persistent Disk. Hyperdisk Throughput provides cost-effective and throughput-oriented storage with dynamically configurable capacity and throughput. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

## February 07, 2024

Feature

When you purchase a resource-based commitment for GPUs, Local SSD disks, or both, you can attach any of your existing on-demand or auto-created future reservations to that commitment. By attaching existing reservations, you can reserve resources in advance and minimize resource unavailability issues when you purchase commitments for GPU or Local SSD disk resources.

For more information, see [Purchase commitments with attached reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#purchasing_a_commitment_with_a_reservation).

## February 02, 2024

Feature

**Generally available** : You can plan ahead for VM maintenance on [C3, C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines), and [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines) [Preview](https://cloud.google.com/products#product-launch-stages) machine types by [viewing their maintenance schedule notifications](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event). For specific machine types within these families, you can also [trigger VM maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) ahead of schedule.

## January 31, 2024

Feature

**Preview** : You can create GPU VMs in a MIG by using resize requests. Resize requests help you create VMs all at once and give you higher chances to obtain highly demanded resources such as GPUs.

For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

Feature

**Generally available:** Johannesburg, South Africa `africa-south1-a,b,c` has launched with E2, N2, N2D, and T2D [general-purpose VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines) in all three zones.

## January 30, 2024

Feature

**Generally available** : [Persistent Disk Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) is available between the following region pairs:

  * `europe-west3` (Frankfurt, Germany) and `europe-west8` (Milan, Italy)
  * `europe-west3` (Frankfurt, Germany) and `europe-west10` (Berlin, Germany)
  * `us-east1` (Moncks Corner, South Carolina) and `northamerica-northeast1` (Montréal, Québec)



For the full list of available regions, see [Supported region pairs](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).

Feature

**Generally available** : Snapshot settings are centralized configuration parameters for all snapshots in a project. You can use snapshot settings to customize the default storage location for all future snapshots in your project. By enabling you to do this, snapshot settings remove the need for you to manually specify a storage location during each individual snapshot creation.

For information about how to use snapshot settings and set your project's default snapshot storage location, see the [snapshot settings documentation](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings).

Feature

**Preview** : Z3 VMs, which offer the latest compute, networking, and storage innovations in one platform with a particular focus on high density, high performing Local SSD are now in Preview. For more information, see [Storage-optimized machine family for Compute Engine](https://docs.cloud.google.com/compute/docs/storage-optimized-machines).

Feature

**Generally available** : NVIDIA L4 GPUs are now available in the following additional region and zone:

  * Zurich, Switzerland (`europe-west6-b`)



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

## January 25, 2024

Feature

**Generally available** : Hyperdisk Balanced is available with M3 VMs. Hyperdisk Balanced is a good fit for a wide range of use cases such as LOB applications, web applications, and medium-tier databases that don't require the performance of Hyperdisk Extreme. For more information, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

## January 22, 2024

Feature

**Generally available** : In the Google Cloud console, in the Observability tab on the VM instances page, you can customize the predefined dashboard to monitor specific VM metrics that you want. For more information, see [Create a customized dashboard to view specific metrics](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms#create-customized-dashboard).

## January 09, 2024

Security

Google has patched several vulnerabilities that were discovered in the TianoCore EDK II UEFI firmware used in Google Compute Engine VMs. For more information, see the [GCP-2024-001 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2024-001).

## January 08, 2024

Feature

**Generally available** : NVIDIA L4 GPUs are now available in the following additional zone:

  * Changhua County, Taiwan (`asia-east1-b`)



For more information about using GPUs on Compute Engine, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
