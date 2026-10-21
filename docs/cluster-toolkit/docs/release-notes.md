---
url: https://docs.cloud.google.com/cluster-toolkit/docs/release-notes/
title: Cluster Toolkit release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:43.372404+00:00
---

# Cluster Toolkit release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Resources ](https://docs.cloud.google.com/cluster-toolkit/docs/release-notes)



Send feedback 

#  Cluster Toolkit release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cluster Toolkit. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 13, 2026

v1.106.0

Feature

Cluster Toolkit v1.106.0 is available. This release adds support for flexible managed instance groups on [static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes), multiple network interfaces (multi-NIC) for Google Cloud Managed Lustre instances, and parallelism controls for Terraform to accelerate cluster deployment and teardown.

This release also introduces the `cloud-build` community module to build container images with Cloud Build.

Additionally, this release adds preflight checks for storage profiles when you [submit jobs](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit) and cleans up gateways when you [cancel jobs](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-cancel).

This update also scopes the `--main-only` flag in the [`gcluster job logs` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-logs) to the main Pod and its default container.

For more information, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6467).

## October 02, 2026

v1.105.0

Feature

Cluster Toolkit v1.105.0 is available. This release adds support for Slurm on Cloud TPU 7x and optional support for managed instance groups (MIGs) on static compute nodes that use A4X machine types.

This release also adds storage profiles and volume attributes for [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) in job submissions, and unifies Google Kubernetes Engine (GKE) blueprints for GPU and Cloud TPU workloads to support dynamic consumption options.

Additionally, this release adds the `repository_name` variable to override repository names and fixes the output for the registry URL in the Artifact Registry module.

This update also introduces the `pre-existing-project` community module and resolves an HTTP 400 error when Slurm checks the deletion status of virtual machines (VMs).

For more information, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6407).

## September 22, 2026

v1.104.0

Feature

Cluster Toolkit v1.104.0 is available. This release adds agent skills to let you debug Kueue workloads on Google Kubernetes Engine (GKE) and migrate from the Accelerated Processing Kit (XPK).

It also adds optional support for managed instance groups on [static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes) and [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) on Slurm nodesets and login nodes.

Additionally, `gcluster` now validates [placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview), [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview), and queues when you submit GKE jobs.

This update also runs the Lustre Networking (LNet) setup script only when Lustre is enabled and prevents LNet errors from causing deployments to fail. For more information, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6355).

## September 11, 2026

Security

Google addressed multiple security vulnerabilities in Slurm that affect Cluster Toolkit. For more information, see the [security bulletin](https://docs.cloud.google.com/cluster-toolkit/docs/security-bulletins#gcp-2026-062).

## September 07, 2026

v1.103.0

Feature

Cluster Toolkit version v1.103.0 is available. This release simplifies the `gcluster` job configuration workflow, adds dynamic catalog fallback for system node pools, increases the maximum system node pool limit to 150 nodes, and replaces deprecated `e2` instances with `n2d` across daily tests and configurations. This release also upgrades Slurm to version 25.11.8 to address multiple security vulnerabilities. For more information about the vulnerabilities, see the [security bulletin](https://docs.cloud.google.com/cluster-toolkit/docs/security-bulletins#gcp-2026-062) and the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6280).

Security

Google addressed a security vulnerability (CVE-2026-65107) in the Slurm `sbcast` tool that affects Cluster Toolkit. For more information, see the [security bulletin](https://docs.cloud.google.com/cluster-toolkit/docs/security-bulletins#gcp-2026-060).

## August 27, 2026

v1.102.0

Feature

Cluster Toolkit version v1.102.0 is available. This release enables Multi-Tier Checkpointing (MTC) when you create GKE clusters, and adds support for Flex unified volumes to NetApp Volumes modules. This release also updates Slurm blueprints to use OS image families, enables Distributed Resilient Architecture Network (DRANET) in example blueprints for A3 Ultra, A4, Cloud TPU v7x, and Cloud TPU v6e, and updates the Go toolchain to version 1.26. In addition, this release consolidates the lifecycle and queue management for Kueue, validates authorized CIDR ranges in GKE blueprints, enables `gcluster` job submission with VM boot disk fixes, and lets you disable Private Google Access for IPv6. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/tag/v1.102.0).

## August 20, 2026

v1.101.0

Feature

Cluster Toolkit version v1.101.0 is available. This release adds support for [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) storage pools to the `vm-instance` module, GKE node pools, and storage. The update also optimizes dependency management to improve the user experience, and updates Cloud TPU v4 and TPU v5p shorthand mappings to use TensorCore counts. For more information, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6180).

## August 13, 2026

v1.100.0

Feature

Cluster Toolkit v1.100.0 is available. This release adds the `--gke-namespace` flag to enable namespace-aware operations, enables `sauth` by default in the Slurm module, and removes topology labels from the `nodeLabels` resources in Kueue `ResourceFlavor` objects. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6136).

## August 06, 2026

v1.99.0

Feature

Cluster Toolkit v1.99.0 is available. This release adds built-in Prometheus OpenMetrics telemetry for Slurm version 25.11 and later, promotes toolkit telemetry to production, and enhances Slurm resilience to capacity constraints and quota errors. This version also enables Multi-Tier Checkpointing (MTC) at the job submission stage and adds GKE TPU v4 and v5p examples. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6087).

## July 22, 2026

v1.98.0

Feature

Cluster Toolkit v1.98.0 is available. This release enables Multi-Tier Checkpointing (MTC) for Pathways workloads and adds support for expedited requeue and start-only health checks for Slurm version 25.11. It also optimizes daily maintenance window and exclusion start times, and extends static node count tracking to support complex mappings and zone multipliers. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/6000).

## July 13, 2026

v1.97.0

Feature

Cluster Toolkit v1.97.0 is available. This release integrates cluster health checks into the toolkit, adds support for collecting static node counts from blueprints, and enforces strict Google Kubernetes Engine node auto-provisioning (NAP) accelerator validation. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5945).

## July 02, 2026

v1.96.0

Feature

Cluster Toolkit v1.96.0 is available. This release adds support for G4 Confidential VMs with Blackwell GPUs and customer-managed encryption keys (CMEK) for storage. This version also introduces warnings for GKE version vulnerabilities and support for the `--env` flag in the `gcluster job submit` command to set custom environment variables. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5889).

## June 25, 2026

v1.95.0

Feature

Cluster Toolkit v1.95.0 is available. This release introduces Slurm high availability controller support using managed instance groups (MIGs). This version also implements Google Kubernetes Engine node auto-provisioning (NAP) and unified compute consumption options for the `gcluster job submit` command. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5852).

## June 18, 2026

v1.94.0

Feature

Cluster Toolkit v1.94.0 is available. This release provides reservation subblock support in the `nodeset` module for Slurm. This version also adds `network_policy` as a variable in the `gke-cluster` module and loosens strict Terraform version constraints across core and community modules. By moving to a minimum version requirement, you can use newer versions of Terraform while maintaining compatibility. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5804).

## June 11, 2026

v1.93.0

Feature

Cluster Toolkit v1.93.0 is available. This release introduces example blueprints for GKE H4D deployments that use the [flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms), a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) and integrated [Google Cloud ML Diagnostics](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/overview). This version also adds a Slurm high availability controller script and upgrades Slurm images from Rocky Linux 8 to Rocky Linux 9. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5770).

## June 04, 2026

v1.92.0

Feature

Cluster Toolkit version 1.92.0 is available. This release introduces support for [ML Diagnostics](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/overview) on TPU machine types and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) on GKE clusters. The release also adds an optional infrastructure setup for inference gateways and compact placement for Slurm clusters by using the Dynamic Workload Scheduler (DWS) flex-start provisioning model. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5744).

## May 14, 2026

v1.91.0

Feature

Cluster Toolkit v1.91.0 is available. This release introduces support for parallel containers on TPU 7x machines. This version also adds [Telemetry data collection options](https://docs.cloud.google.com/cluster-toolkit/docs/overview#privacy), which let Google collect usage statistics. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5665).

## May 06, 2026

v1.90.0

Feature

Cluster Toolkit v1.90.0 is available. This release adds an experimental capability to submit jobs that you can use with the `gcluster job` command. This version also adds support for regional AI zones in Slurm by using the `locationPolicy.zones` resource. Additionally, this release updates examples for GKE TPU, exposes outputs for accelerator topology and slice controllers, and fixes several Slurm issues. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/pull/5603).

## April 30, 2026

v1.89.0

Feature

Cluster Toolkit v1.89.0 is available. This release lets you configure virtual machines (VMs) dynamically for Slurm and manage secondary NICs by using the Networking Dynamic Resource Allocation (DRA) driver. This release also updates the GKE A3 Mega blueprint to align with integration tests and ensure stability. This version also adds support to use Fractional G4 GPU instances in Slurm. For details, see the [Release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5576).

## April 16, 2026

v1.88.0

Feature

Cluster Toolkit version v1.88.0 is available. This release adds dynamic machine configurations by using the Compute Engine API. This release also refactors the naming convention for Helm releases within the `kubectl-apply` module, which helps to improve the predictability and maintainability of deployed resources. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5506).

## April 13, 2026

v1.87.0

Feature

Cluster Toolkit version v1.87.0 is available. This release adds Kueue support for GKE A4X-Max and introduces support for Customer Managed Encryption Keys (CMEK) in Google Cloud Managed Lustre. This release also migrates the `install_asapd_lite` module to Helm and updates the Google Kubernetes Engine A3 High blueprint. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5469).

## April 02, 2026

v1.86.0

Feature

Cluster Toolkit version v1.86.0 is available. This release implements and configures the Google Container Filesystem (GCFS) to stream images at the cluster level for Google Kubernetes Engine. This release also migrates the `kubectl_apply_manifest` module to Helm and upgrades the command-line interface (DCGMI) for the NVIDIA Data Center GPU Manager (DCGM).

For more information about version v1.86.0, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5447).

## March 25, 2026

v1.85.0

Feature

Cluster Toolkit version v1.85.0 is available. This release updates the `cloud_dns_config` setting in the `gke-cluster` module to default to `KUBE_DNS` (CoreDNS). This version also adds Google Cloud Managed Lustre integration for Google Kubernetes Engine with the A4X Max machine type.

For more information about this release and other minor changes, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5397).

## March 12, 2026

v1.84.0

Feature

Cluster Toolkit version v1.84.0 is available. This release adds disk type validation in specific zones, updates GKE versioning for GPU direct configurations, and fixes an issue with NCCL test scripts on A3 High instances. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5348).

## March 05, 2026

v1.83.0

Feature

Cluster Toolkit version v1.83.0 is available. This release introduces early conditional and required validations, adds support for A4X-Max Bare Metal on GKE and Slurm, and enables Dynamic Workload Scheduler Queued Provisioning for TPU v6e and 7x. It also includes several module migrations to Helm and pins Terraform to version 1.12.2. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5312).

## February 12, 2026

v1.82.0

Feature

Cluster Toolkit version v1.82.0 is available. This release adds an A4X JBVM blueprint that is designed to provision and deploy a group of virtual machines (VMs) for machine learning (ML) workloads. This release includes a ZIP archive of binaries to the release that improves the install process. This release removes Terraform validation for machine types. The API validation now handles this Terraform validation because custom machine types are not supported.

For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5233).

## February 05, 2026

v1.81.0

Feature

Cluster Toolkit version v1.81.0 is available. This release adds support for the Dynamic Workload Scheduler (DWS) Flex-start provisioning model on TPU 7x and TPU v6e resources. This release also updates Slurm cluster blueprints to use the Cloud Storage FUSE profile feature for AI/ML Cloud Storage bucket mounts.

For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5195).

## January 28, 2026

v1.80.0

Feature

Cluster Toolkit version v1.80.0 is available. This release adds support for IPv6 and the Infrastructure Data-Plane Function (IDPF). This version makes the H4D blueprint more concise by refactoring the `vpc` and `multivpc` modules to support more variables. Additionally, this release integrates the Report and Replace (R&R) API with Slurm, which lets you report faulty nodes for repair or replacement.

For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5145).

## January 21, 2026

v1.79.0

Feature

Cluster Toolkit version v1.79.0 is available. This release enables Dynamic Workload Scheduler Flex-start provisioning for G4 instances.

For more information about this release and other minor changes, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5125).

## January 14, 2026

v1.78.0

Feature

Cluster Toolkit version v1.78.0 is available. This release adds a deprecation notice for the Parallelstore module. This version also adds support for gIB versions v1.1.1 and v1.1.0 for the Arm64-based architecture.

For more information about this release and other minor changes, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5105).

## January 07, 2026

v1.77.0

Feature

Cluster Toolkit version v1.77.0 is available. This release introduces a robust destroy process to help ensure that you can reliably delete resources from the Cluster Toolkit. This version also adds an automated Google Cloud resource cleanup script and integrates a Cloud Build pipeline to let you remove resources that are no longer required.

For more information about this release and other minor changes, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5075).

## December 18, 2025

v1.76.0

Feature

Cluster Toolkit version v1.76.0 is available. This release introduces an example NCCL test script for Slurm on GKE and makes the `wait` parameter for Kueue installation configurable, and adds a `wait` parameter for Kueue in the [examples/gke-g4/gke-g4.yaml](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-g4/gke-g4.yaml) blueprint. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/5016).

## December 10, 2025

v1.75.0

Feature

Cluster Toolkit version v1.75.0 is available. This release graduates the `cloud-storage-bucket` module to the core collection of modules and adds integration tests for TPU v6e and TPU 7x. This version also enables Spot VM testing for A3 Ultra instances and provides ML dependencies and dual NIC guidance for G4 machines. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4975).

## December 04, 2025

v1.74.0

Feature

Cluster Toolkit version v1.74.0 is available. This release adds support for Google Cloud NetApp Volumes and introduces new blueprint files for TPU 7x instances. This release also adds a `force_conflicts` flag that you can use when you apply manifests using the `kubectl` command. This release also updates the `nccl-tcpxo-installer`, `nri-device-injector`, and `nccl-test` values for `a3-megagpu-8g` machines. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4934).

## November 19, 2025

v1.73.0

Feature

Cluster Toolkit version v1.73.0 is available. This release adds support for the [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) and adds a new blueprint for [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) machines that automates the process of building a custom image with a TCPx-patched kernel for enhanced network performance. This version also includes an initial blueprint for [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) and parameterized the gIB NCCL RDMA plugin installer in the `gke-a4x.yaml` blueprint. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4857).

## November 13, 2025

v1.72.0

Feature

Cluster Toolkit version v1.72.0 is available. This release adds support for Google Cloud Managed Lustre as an optional storage solution for the `gke-tpu-v6-advanced` blueprint. This release also adds four example blueprints to support the deployment of Sycomp storage. In addition, this release makes improvements to the `gke-node-pool` module and `a4xhigh-slurm-blueprint.yaml` blueprint. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4841).

## November 03, 2025

v1.71.0

Feature

Cluster Toolkit version v1.71.0 is available. This release includes a fix for a munge mount on login failure due to slow controller Slurm v6 setup, and adds Managed Lustre support in the `gke-a4x` blueprint. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4810).

## October 24, 2025

v1.70.0

Feature

Cluster Toolkit version v1.70.0 is available. This release adds automated TPU support and Cloud Storage FUSE mounts in the TPU v6 blueprint and refactors the H4D blueprint. This version also includes breaking changes, such as removing support for the `maintenance_interval` field for reservations created by [Technical Account Managers (TAMs)](https://cloud.google.com/tam) and migrating Jobset from static manifests to a Helm chart. For a complete list of changes, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4783).

## October 21, 2025

v1.69.0

Feature

Cluster Toolkit version v1.69.0 is available. This release adds NUMA-aware scheduling in GKE clusters for G4 machines and adds a new module that provides mount scripts for WEKA filesystems. This version also includes PSA updates and adds a GKE sample for running the `nvidia-bug-report` shell script. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4772).

## October 10, 2025

v1.68.0

Feature

Cluster Toolkit version v1.68.0 is available. This release lets you download the NVIDIA Collective Communications Library (NCCL) software packages `libnccl2` and `libnccl-dev` for A3U and A4H machine types. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4756).

This release supports the generally available, open-source IBM Spectrum Symphony HostFactory connectors for Google Compute Engine and Google Kubernetes Engine, which you can deploy through Cluster Toolkit to extend your on-premises cluster or run entirely within Google Cloud. For information, see [Run IBM Spectrum Symphony workloads](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony).

## September 19, 2025

v1.67.0

Feature

Cluster Toolkit version v1.67.0 is available. This release adds support for aarch64-based architecture. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4674).

## September 15, 2025

v1.66.0

Feature

Cluster Toolkit version v1.66.0 is available. This release lets you use Cloud Storage FUSE for H4D machine types and sets the default cluster availability to zonal. For more information about this release, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4655).

## September 09, 2025

v1.65.0

Feature

Cluster Toolkit version v1.65.0 is available. This release expands support for Managed Lustre on A4X instances and provides an improved GPU network wait solution for A-family machine types. This version also deprecates Debian-based blueprints for A3 Mega GPUs. For a complete list of changes, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4632).

## September 01, 2025

v1.64.0

Feature

Cluster Toolkit version v1.64.0 is available. This release integrates GKE Managed Lustre, which provides high-performance, scalable storage for your GKE clusters. The storage for A3 Ultra machine types now uses basic SSD for improved performance. This version also improves support for alternative services for private service access. For details about these changes and other updates, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4589).

## August 26, 2025

v1.63.0

Feature

Cluster Toolkit version v1.63.0 is available. This release upgrades Slurm image versions to the `6-11` iteration, for example, `slurm-gcp-6-11-hpc-rocky-linux-8`. This version migrates Dynamic Workload Scheduler (DWS) Flex-start to regional managed instance groups (MIGs). This version also includes breaking changes, for example, updating the file storage for A3 Ultra machine types to basic HDD. For a complete list of new features, improvements, and bug fixes, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4570).

## August 14, 2025

v1.62.0

Feature

Cluster Toolkit version v1.62.0 is available. This release adds new blueprints for A4X instances and adds a community scheduler module for Slinky (Slurm on Kubernetes). For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4514).

## August 04, 2025

v1.61.0

Change

Cluster Toolkit version v1.61.0 is available. This release adds a namespace for GKE modules and optimizes Cloud Storage FUSE configurations for A3 Ultra and A4 blueprints. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4484).

## July 22, 2025

v1.59.0

Change

Cluster Toolkit version v1.59.0 is available. This release adds a configurable number of IP addresses per NAT for A-family blueprints and fixes an issue with additional disks for login nodes. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4432).

## July 15, 2025

v1.58.0

Feature

Cluster Toolkit version v1.58.0 is available. This release adds a new blueprint for deploying GKE clusters with H4D instances and deprecates blueprints for deploying Parallelstore. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4400).

## June 30, 2025

v1.57.0

Feature

Cluster Toolkit version v1.57.0 is available. This release integrates Cluster Health Scripts (CHS) with GKE blueprints for A3 Mega, A3 Ultra, and A4 instances. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4337).

## June 23, 2025

v1.56.0

Change

Cluster Toolkit version v1.56.0 is available. This release improves SlurmGCP Resume functionality and includes several bug fixes. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4308).

## June 16, 2025

v1.55.0

Feature

Cluster Toolkit version v1.55.0 is available. This release adds a new blueprint for a high-throughput AlphaFold 3 execution environment and aligns Cloud Storage FUSE configurations with best practices. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4283).

## June 10, 2025

v1.54.0

Change

Cluster Toolkit version v1.54.0 is available. This release adds Managed Lustre support for non-default ports in GKE and adds a network blocking script for A3 High instances. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4261).

## June 05, 2025

v1.53.0

Change

Cluster Toolkit version v1.53.0 is available. This release standardizes the A3 Mega Slurm solution on Ubuntu and adds a new GKE blueprint for A4X instances. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4242).

## May 22, 2025

v1.52.0

Breaking

Cluster Toolkit version v1.52.0 is available. This release improves CloudSQL support with database flags and query insights, and adds several bug fixes. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4181).

## May 13, 2025

v1.51.0

Feature

Cluster Toolkit version v1.51.0 is available. This release adds GPU health-check epilogs for A3 High and A3 Mega Slurm blueprints and adds a new GKE TPU v6e example. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4111).

## May 05, 2025

v1.50.0

Feature

Cluster Toolkit version v1.50.0 is available. This release adds new blueprints for Managed Lustre attached to VMs and Slurm clusters. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4061).

## April 24, 2025

v1.49.0

Feature

Cluster Toolkit version v1.49.0 is available. This release adds TPU support to the GKE nodepool module and adds support for Managed Lustre. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/3997).

## April 01, 2025

v1.48.0

Feature

Cluster Toolkit version v1.48.0 is available. This release updates the GKE nodepool module to support multiple nodepools and adds automatic GPU health checks for Slurm. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/3864).

## February 27, 2025

v1.47.0

Feature

Cluster Toolkit version v1.47.0 is available. This release adds support for the A4 machine family in GKE and Slurm blueprints and adds Dynamic Workload Scheduler Flex support for GKE. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/3731).

## February 07, 2025

v1.46.0

Feature

Cluster Toolkit version v1.46.0 is available. This release officially supports Kueue as the workload scheduler for A3U and adds new blueprints for A3U, H4D VMs, and Slurm. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/3650).

## January 15, 2025

v1.45.0

Change

Cluster Toolkit version v1.45.0 is available. This release updates A3 Ultra GKE blueprints to newer versions of Kueue and Jobset, and adds support for cluster deletion protection. For details, see the [release announcement on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/3541).

For information about previous releases of Cluster Toolkit, see the [Announcements page on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/categories/announcements).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
