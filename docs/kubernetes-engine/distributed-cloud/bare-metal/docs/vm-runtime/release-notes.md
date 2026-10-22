---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/release-notes/
title: VM Runtime on GDC release notes \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:59.930858+00:00
---

# VM Runtime on GDC release notes  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  VM Runtime on GDC release notes Stay organized with collections  Save and categorize content based on your preferences. 

This document lists production updates to VM Runtime on Google Distributed Cloud. We recommend that VM Runtime on GDC developers periodically check this list for any new announcements 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/vmruntime-release-notes.xml) directly. 

## October 09, 2024

1.3

Announcement

A new release of VM Runtime on Google Distributed Cloud is available as part of the Google Distributed Cloud for bare metal 1.30.0-gke.1930 release, which is now available for download. For a more information about what's new in this release, see the [Google Distributed Cloud for bare metal 1.30.0-gke.1930 release notes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver).

1.3

Feature

Added support for the `virtctl diagnose` command to diagnose VM issues and the `virtctl snapshot` command to collect VMRuntime logs for debugging.

1.3

Feature

Added support for configuring live migration `maxDowntime` through the kubevirt migration policy. This specifies the maximum time in milliseconds that a VM is allowed to be paused at the end of a live migration. The default value is `300` (0.3 seconds). For VMs with workloads that are dirtying RAM faster than it can be copied across the network for live migration, increasing this setting can speed up live migration.

1.3

Change

Updated the live migration flow to remove the old `virt-launcher` pod after a successful live migration.

1.3

Change

Updated VM Runtime to mark a VMI as unready when the VM hits IO/sync error.

1.3

Change

Increased the `nodeMonitorGracePeriod` default value for node high availability to 55 seconds to tolerate cluster API unavailability due to etcd failover.

1.3

Change

Moved the configuration for node high availability to `spec.haPolicy` in the `vmruntime` resource.

1.3

Change

Changed the KubeVirt restore short name to `virtvmrestore` to avoid conflict with `vmrestore` that's used by VM Runtime on GDC.

1.3

Fixed

Refactored the high-availability (HA) logic to fix a corner case issue in HA.

1.3

Fixed

Fixed a networking issue on live migration.

1.3

Fixed

Disabled the VM generation check for the `autoRestartOnConfigurationChange` feature, because the check isn't accurate.

1.3

Fixed

Removed the erroneous "No disk capacity" error from the `virt-launcher` log.

## April 29, 2024

1.29

Announcement

### Release 1.29.0-gke.1449

A new release of VM Runtime on Google Distributed Cloud is available as part of the GKE on Bare Metal 1.29.0-gke.1449 release, which is now available for [download](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). For a more information about what's new in this release, see the [GKE on Bare Metal 1.29.0-gke.1449 release notes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver).

1.29

Feature

Added support for applying real-time label patching to the vm Pod by adding labels to GVM resources.

1.29

Feature

Added support for configuring the running state (`Running` or `Stopped`) of a GVM through the `runningState` field in the GVM resource spec.

1.29

Change

Reduced the CPU and memory resource request settings for the `macvtap` DaemonSet.

1.29

Change

Added `ResponseReadTimeout` for use when fetching images from an S3 repository. Now, the importer Pod disconnects and restarts when the object read can't get new data for more than 10 minutes.

1.29

Change

Added `vmruntime` preflight check result to the output of `kubectl get vmruntime`.

1.29

Change

Enabled the ability to override the pod network configuration through the `virtSpec` ConfigMap. Overrides are needed when the cluster CIDR conflicts with the default mock CIDR (`10.0.2.0/24`) used by VMs that connect to the default pod network.

1.29

Change

Changed the default VM high availability grace period from 90 seconds to 35 seconds. With this change, VMs fail over on node failure sooner than with previous releases. Included in this change is the addition of continuous retries on heartbeat failures.

1.29

Fixed

Fixed the `virt-launcher` log container termination issues that sometimes caused VM statuses of not ready.

1.29

Fixed

Fixed issues on the persistent non-volatile random access memory NVRAM feature, which caused the created PVC to get stuck in a pending state.

1.29

Fixed

Fixed the guest agent installation script.

1.29

Fixed

Fixed an issue with the `virtctl create vm` command that caused failures when `os-type` was set to `windows`.

## December 15, 2023

1.28

Feature

Anthos clusters on bare metal 1.28.0 is now available for [download](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.28/downloads). For a more information about what's new in this release, see the [Anthos clusters on bare metal 1.28 release notes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.28/release-notes-ver).

1.28

Feature

Added support for local image caching within the same namespace.

1.28

Change

Increased the memory resource limit for CDI pods when importing or cloning images.

1.28

Change

Added an error to catch attempts to create disks using a storage class (other than `local-shared`) with a storage profile that's missing access modes. In earlier versions of Anthos VM Runtime, the access mode defaults to ReadWriteOnce (RWO) for this case.

1.28

Change

Added a check to see if the network controller is ready as part of overall `VMRuntime` readiness.

1.28

Change

Added an `Enabled` column for the `VMRuntime` custom resource so that you can see whether `VMRuntime` is enabled or not without printing the whole custom resource.

1.28

Change

Removed the node patching access from the `virt-handler` DaemonSet to reduce security risk.

1.28

Change

Added `ErrorConfiguration` and `Pending` to the disk phase status.

1.28

Change

Upgraded CDI version to v1.57.0. With this upgrade, support for the qcow2 VM format is obsolete. This image format configuration is ignored silently.

1.28

Fixed

Increased the live migration Pod creation timeout to resolve cluster upgrade failures.

1.28

Fixed

Enabled live migration auto-converge, by default. This fixes an issue where live migration wouldn't finish for some VMs.

1.28

Fixed

FIxed an issue to prevent VM annotations from triggering VMs to restart when the `autoRestartOnConfigurationChange` flag is enabled.

1.28

Fixed

Fixed an issue that caused nil pointer crashes when the `KubeVirt` custom resource is missing.

1.28

Fixed

Enabled support for running a VM as a dynamic host configuration protocol (DHCP) server.

## August 25, 2023

1.16

Feature

Anthos clusters on bare metal 1.16.0 is now available for [download](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). For a more information about what's new in this release, see the [Anthos clusters on bare metal 1.16 release notes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver).

1.16

Feature

Added GPU support for Rocky Linux guest operating systems (OSes). Support is similar to what's provided for Ubuntu, but you must use the `dnf` package manager, instead of the Ubuntu `apt`.

1.16

Feature

Added support to persist states for Unified Extensible Firmware Interface (UEFI) and trusted platform module (TPM) across virtual machine (VM) restarts. This feature is enabled in the VMRuntime custom resource by setting `spec.featureGates.VMPersistentState` to `Enabled`.

1.16

Feature

Added support for inserting or ejecting CD-ROMs for live virtual machines (VMs) without interruptions. You can eject currently attached CD-ROMs and you can insert a CD-ROM into any open slot. You can also start with open slots and insert CD-ROMs at any time.

1.16

Change

Added READY column in VMRuntime custom resource to tell you if VMRuntime is ready or not without printing the whole resource manifest.

1.16

Change

Upgraded Kubevirt version from v0.58.0 to v0.59.0.

1.16

Change

Changed the default VM format from qCOW2 to RAW for file system storage. This change improves the underlying storage performance and is transparent to users.

1.16

Fixed

Fixed the issue that prevented proper detection of GPU devices when the VM is booted with UEFI.

1.16

Fixed

Fixed a network disconnect issue that occurred during VM live migration.

1.16

Fixed

Fixed the issue where a `daemon-reload` for systemd on a worker node causes an existing GPU workload to fail.

1.16

Fixed

Fixed the issue that blocked VMs from starting when secure boot and Windows guest agent are both enabled.

1.16

Fixed

Fixed the issue where cluster upgrades or credential rotation prevented new GPU workloads from running.

## April 27, 2023

1.15

Feature

**Make MIG controller resilient to K8s API server failure** This change makes the GPU MIG component more resilient to short-time controller plane failures. For example, if there is a glitch on the API server, the MIG controller will retry connecting to the server multiple times till the API server returns to be responsive or it times out.

1.15

Feature

**Change eviction behavior during cluster upgrade** VM live migration/restart is triggered after a node is put into maintenance mode instead of before as in earlier versions, and the operation is subject to the common `enteringMaintenanceWindow` timeout set by Anthos on Bare Metal. The VM will try to migrate or move to other nodes that are already upgraded in a best-effort way. Also changed the Kubevirt migration taints to soft taints to fix the single-control-node upgrade issue.

1.15

Feature

**Base image upgrade to address vulnerabilities**

1.15

Change

**Kubevirt version upgrade from v0.57.1 to[v0.58.0](https://kubevirt.io/2022/changelog-v0.58.0.html)** This most notably removes the root-user requirement on virt-launcher pods.

1.15

Fixed

**Support ABM cluster proxy**

1.15

Change

**Qemu version upgrade from 5.2 to 7.2** This upgrade changse the default Qemu machine type for VM instances. We will restart all existing VMs during upgrade to switch to the new machine type.

1.15

Feature

**HA enhancement for Robin storage class** When the Robin storage class is used, because Robin supports storage fencing, trigger Robin fencing to ensure no access to the storage from the failed node during HA failover. This allows HA to work with a block storage class with Robin.

1.15

Feature

**Support configuration of the virtio-nontransitional driver for SLES11** Expose the Kubevirt knob on the virtio-nontransitional driver to the KubeVM layer.

1.15

Feature

**Windows guest HyperV optimization** For windows guest OS on a physical server environment, automatically enable some advanced configurations for better performance.

1.15

Fixed

**Fix the OOM error for VM with large memory** This fix adds memory overhead for VMs with large memory.

1.15

Change

**Prevent multiple VMs from attaching to the same disk in non-read-only mode**

1.15

Feature

**VNC access improvement** Use tablet mode to enhance VNC experience.

1.15

Feature

**Support for virtual machine disk resize** When customers modify the size of a VM disk, the underlying persistent volume claim (PVC) and disk used by the VM are expanded if the storage provider supports it.

1.15

Change

**Guest agent V2** Previously, the guest agent connected to the control plane through the Kubernetes API server watching mechanism. In Anthos for Bare Metal 1.15, we changed the default communication mode for guest agents on Linux VMs to the push model through the vsock.

1.15

Change

**Detects generation difference between Kubevirt VM and Kubevirt VMI** This ensures that when the `autoResetartVMOnConfigurationChange` flag is enabled, VM instances will always be in sync with VM configurations irrespective of whether the changes were made before the flag enablement or not.

1.15

Feature

**Support Rocky 8 guest OS, SLES11, and Ubuntu 22.04**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
