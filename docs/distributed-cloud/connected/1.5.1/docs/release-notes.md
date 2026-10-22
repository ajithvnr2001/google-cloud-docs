---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/release-notes/
title: Google Distributed Cloud connected, version 1.5.1 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:55.799018+00:00
---

# Google Distributed Cloud connected, version 1.5.1 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/release-notes/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)
  * [ Resources ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/resources)



Send feedback 

#  Google Distributed Cloud connected, version 1.5.1 release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for releases, features, and updates to Google Distributed Cloud.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/distributed-cloud-edge-release-notes.xml) directly. 

## September 15, 2025

Distributed Cloud connected 1.11.0

Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

  * **OS layer security mitigations:** CVE-2025-31498, CVE-2024-48615, CVE-2016-1585.

  * **GDC software-only security mitigations:** All mitigations listed in the [GDC software-only release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) up to version [1.32.100](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities#1.32) (inclusive).




The following new functionality has been introduced in this release of Google Distributed Cloud connected:

  * **Backup for VM workloads on GDC connected servers.** You can now backup and restore virtual machine workloads on your Google Distributed Cloud connected servers deployment, including scheduling. For more information, see [Back up a virtual machine](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers#back_up_a_virtual_machine).

  * **Configurable runtime class for container workloads.** As part of gVisor integration in Google Distributed Cloud connected, you can now specify the default runtime class for container workloads at both Pod and cluster level. Cluster-level runtime class selection is a preview-level feature. For more information, see [Configure the runtime class for a Pod](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/deploy#runtime-class).

  * **Island mode networking.** Google Distributed Cloud connected now supports [island mode networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network) on secondary network interfaces. For more information, see [(Optional) Configure island mode](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking#island-mode).

  * **`AppArmor` sandboxing audit logs for VM workloads.** Google Distributed Cloud connected now lets you enable audit logs for virtual machine workloads sandboxed using `AppArmor` policies. To enable audit log emission on an existing virtual machine workload, restart the corresponding virtual machine. For more information, see [View AppArmor sandboxing audit logs](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers#view_apparmor_sandboxing_audit_logs).

  * **CoreDNS resolution for secondary networks.** Google Distributed Cloud connected now supports specifying a CIDR block for use with secondary networks at both Pod and cluster level. This allows for CoreDNS resolution on secondary network interfaces. For more information, see [`Network` resource](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#Network).

  * **Access clusters through Connect Gateway.** You can now access your Google Distributed Cloud connected clusters through Connect Gateway. For more information, see [Obtain cluster credentials through Connect Gateway](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters#gateway).

  * **VNC support for accessing VM workloads through Connect Gateway.** You can now use VNC to access your virtual machine workloads through Connect Gateway.




This release of Google Distributed Cloud connected contains the following known issues:

  * **The`gvisor` runtime class is incompatible with Symcloud Storage persistent volumes in block mode.** If you set a workload that uses Symcloud Storage persistent volumes in block mode to use the `gvisor` runtime class, the workload fails. Symcloud Storage persistent volumes in filesystem mode are not affected.

  * **Cilium does not differentiate between TCP and UDP protocols.** Cilium does not differentiate between TCP and UDP protocols for services that use both protocols on the same port number and routes traffic for both protocols to the same backend pods. This can render such services non-functional. To work around this issue, use a different port for each protocol.

  * **Overlapping the Pod and cluster CIDR blocks for secondary networks causes network failure.** If you specify overlapping CIDR blocks for Pods and clusters using the `annotations.networking.gke.io/gdce-pod-cidr` and `annotations.networking.gke.io/gke-gateway-clusterip-cidr` annotations in the `Network` resource, the Google Distributed Cloud connected virtual networking subsystem might behave erratically, including loss of connectivity. Follow the guidelines in [(Optional) Configure island mode](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking#island-mode) to prevent this issue.

  * **The`anthos-multinet` container might take up to two hours to fully start.** You might intermittently experience a slower than normal startup for the `anthos-multinet` container (up to two hours). To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).




The following Google Distributed Cloud connected components have been updated:

  * **GDC software-only has been updated** to version 1.32.100. (This component was formerly known as GKE on Bare Metal and as Anthos Clusters on Bare Metal.)

  * **Kubernetes** has been updated to version 1.32.4-gke.200.




This is a minor release of Google Distributed Cloud connected (version 1.11.0). Google Distributed Cloud software updates roll out gradually across regions. The latest version might not be immediately available on your Google Distributed Cloud connected deployment.

The following issues have been resolved in this release of Google Distributed Cloud connected:

  * **Machines no longer experience intermittent connectivity loss.** Google Distributed Cloud connected machines no longer experience intermittent connectivity loss; the underlying rare condition that can occur with fleet credential management has been resolved.

  * **VNC sessions through Connect Gateway are now more resilient.** The stability of VNC sessions to virtual machine workloads through Connect Gateway has been improved.




## August 15, 2025

Distributed Cloud connected 1.10.0

The following Google Distributed Cloud connected components have been updated:

  * **EdgeOS kernel** has been updated to version 5.15.177.

  * **GDC software-only has been updated** from version 1.30.500 to version 1.31.400. (This component was formerly known as GKE on Bare Metal and as Anthos Clusters on Bare Metal.)

  * **Kubernetes** has been updated from version 1.30 to version 1.31.

  * **Symcloud Storage** has been updated from version 5.4.14 to version 5.4.16.




The following changes to existing functionality have been introduced in this release of Google Distributed Cloud connected:

  * **Reduced minimum internet connection bandwidth requirement.** The minimum internet connection bandwidth required by Google Distributed Cloud connected to function reliably has been reduced. For more information, see [Internet connection bandwidth](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/requirements#internet-bandwidth).



This release of Google Distributed Cloud connected contains the following known issues:

  * **Machines can experience intermittent connectivity loss.** Google Distributed Cloud connected machines can experience intermittent connectivity loss due to a rare condition that can occur with fleet credential management. To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **The`anthos-multinet` container might take up to two hours to fully start.** You might intermittently experience a slower than normal startup for the `anthos-multinet` container (up to two hours). To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Virtual machine workloads cannot coexist on the same virtual network with Pods that use DHCP for IP address assignment.** This is because virtual machine workloads need the `IPAMMode` parameter set to `external` to use DHCP, while Pods need the `IPAMMode` parameter set to `internal` to use DHCP. Pods with static IP address are not affected by this. This behavior is by design.




Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

  * **OS layer security mitigations:** CVE-2024-56664, CVE-2024-56658, CVE-2023-52664, CVE-2024-27010, CVE-2024-56647, CVE-2024-53091.

  * **GDC software-only security mitigations:** All mitigations listed in the [GDC software-only release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) from version [1.30.500](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities#1.30) up to version [1.31.400](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities#1.31) (inclusive).




The following issues have been resolved in this release of Google Distributed Cloud connected:

  * **Storage is now freed immediately upon cluster deletion.** After deleting a cluster, the storage used by that cluster is now freed up immediately. You no longer have to manually delete all persistent volumes in a cluster before deleting the cluster itself.

  * **Virtual machine workloads no longer fail to restart or migrate if DHCP server address changes.** If you are using DHCP to assign IP addresses to your virtual machine workloads and the IP address of your DHCP server changes, your virtual machine workloads now automatically restart and successfully complete migration.




This is a minor release of Google Distributed Cloud connected (version 1.10.0).

The following new functionality has been introduced in this release of Google Distributed Cloud connected:

  * **Pause and resume cluster software upgrades.** Software upgrades for your Google Distributed Cloud connected clusters now automatically pause when a maintenance window ends and automatically resume when the next maintenance window starts. For more information, see [Availability best practices](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/availability).

  * **VM management in Cloud Console for GDCc servers.** You can now manage virtual machine workloads running on your Google Distributed Cloud connected servers deployments through the Cloud Console. For more information, see [Manage virtual machines on Distributed Cloud connected servers](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers).

  * **Kernel memory accounting control.** You can now configure the `NodeSystemConfigUpdate` Network Function operator resource to exclude kernel-space memory from Pod memory usage calculation. For more information, see [`NodeSystemConfigUpdate` resource](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#NodeSystemConfigUpdate).

  * **Configurable per-node subnet mask size.** The `Network` Network Function operator resource now allows you to configure the subnet mask size for each node. For more information, see [`Network` resource](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#Network).

  * **Raw workload log export.** You can now access raw (unprocessed and untagged) workload logs for your Pods for export to your own log processor. For more information, see [Collect raw workload logs for external processing](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/logs-metrics#collect_raw_workload_logs_for_external_processing).




## May 19, 2025

Distributed Cloud connected 1.9.0

The following changes to existing functionality have been introduced in this release of Google Distributed Cloud connected:

  * **IPv4/IPv6 dual-stack networking GA.** This release of Google Distributed Cloud connected promotes the dual-stack IPv4/IPv6 networking feature to General Availability. For more information, see [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking#dual-stack).

  * **Configurable local storage schemas GA.** This release of Google Distributed Cloud connected promotes the configurable local storage schemas feature to General Availability. For more information, see [Configure local storage schemas](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/storage#schemas).

  * **Load balancer address pool support GA.** This release of Google Distributed Cloud connected promotes the load balancer address pool networking feature to General Availability. For more information, see [Create a cluster](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters#create).

  * **Optimized BGP peering for multi-network Pods.** The BGP peering functionality has been optimized for workload Pods using both primary and secondary network interfaces. For more information, see [Networking features](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking).

  * **Virtual machine workload support is now enabled by default on GDCc servers.** The VMRuntime virtual machine subsystem is now enabled by default on GDC connected servers deployments. You can manually disable it by modifying the `VMRuntime` custom resource. For more information, see [Enable VM Runtime on GDC support on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers#enable-anthos-vm-runtime-support).

  * **Default downtime for virtual machine workloads has changed.** The default value of the maxDowntime parameter for virtual machine workloads has been changed to 5 seconds. This lets a virtual machine workload pause for 5 seconds to complete live migration. To override this default with a value of your choice, see [Migration Policies](https://kubevirt.io/user-guide/cluster_admin/migration_policies/).

  * **Virtual machine workloads stuck in abnormal state now automatically restart.** The auto-recovery feature in the VMRuntime virtual machine subsystem now automatically restarts virtual machine workloads that have remained in an abnormal state for more than 3 minutes.




This release of Google Distributed Cloud connected contains the following known issues:

  * **Storage is not freed immediately upon cluster deletion.** After deleting a cluster, the storage used by that cluster is not freed up immediately. This is because storage clean-up is part of a garbage collection task that runs infrequently. To work around this issue, manually delete all of a cluster's persistent volumes before deleting the cluster itself.

  * **The Storage Infrastructure Cluster cannot be deleted.** On refreshed rack hardware deployments, the first cluster in a Google Distributed Cloud connected zone, also known as the Storage Infrastructure Cluster (SIC) cannot be deleted. Doing so would render Google Distributed Cloud connected storage inoperable. This is intentional behavior. Legacy Google Distributed Cloud connected rack hardware deployments and Google Distributed Cloud connected server deployments are not affected by this issue.

  * **Machines can experience intermittent connectivity loss.** Google Distributed Cloud connected machines can experience intermittent connectivity loss due to a rare condition that can occur with fleet credential management. To remedy this issue, contact Google Support.

  * **The`anthos-multinet` container might take up to two hours to fully start.** You might intermittently experience a slower than normal startup for the anthos-multinet container (up to two hours). To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Virtual machine workloads fail to restart or migrate if DHCP server address changes.** If you are using DHCP to assign IP addresses to your virtual machine workloads and the IP address of your DHCP server changes, your virtual machine workloads cannot restart or complete migration. To remedy this issue, remove the stale network interface resource from the cluster and restart the affected virtual machine workloads.

  * **Virtual machine workloads cannot coexist on the same virtual network with Pods that use DHCP for IP address assignment.** This is because virtual machine workloads need the `IPAMMode` parameter set to `external` to use DHCP, while Pods need the `IPAMMode` parameter set to `internal` to use DHCP. Pods with static IP address are not affected by this. This behavior is by design.




The following new functionality has been introduced in this release of Google Distributed Cloud connected:

  * **Workload network traffic tagging on GDCc servers.** VLAN ID tagging on the kube0 network interface is now supported on GDC connected servers. This lets you tag your GDC connected workload traffic with a specific VLAN ID. You must request this feature when ordering your GDC connected servers deployment. For more information, see [Workload network traffic tagging](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/requirements#vlan-ids).

  * **Performance-optimized Network Function operator on GDCc servers.** The Network Function operator functionality has been streamlined on GDC connected server deployments to reduce vCPU and RAM consumption. For more information, see [Network Function operator profiles](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#profiles).

  * **L2 MetalLB load balancing for secondary networks.** You can now specify an annotation in your Network resource and Pod configuration that triggers automatic configuration of L2 MetalLB load balancing on secondary Pod networks. For more information, see [Configure a secondary interface on a Pod using Distributed Cloud multi-networking](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#configure_a_secondary_interface_on_a_pod_using_multi-networking).




The following issues have been resolved in this release of Google Distributed Cloud connected:

  * **Reallocating a GPU resource from a VM to a container no longer causes an initialization error.** An NVML initialization error no longer occurs when you reallocate a GPU from a virtual machine workload to a container workload.

  * **After a network disruption, Symcloud Storage volumes no loner fail to mount or dismount.** Symcloud Storage volumes now mount and dismount reliably after network connectivity is restored after a node that uses Symcloud Storage volumes experiences a network disconnection.

  * **Virtual machines using file-based Symcloud Storage volumes no longer experience CDI import errors.** Intermittent CDI import failures no longer occur when creating a virtual machine that uses a file-based Symcloud Storage volume.

  * **You no longer have to manually copy storage secrets for corresponding buckets to the target clusters in a zone.** For Google Distributed Cloud connected zones with more than one cluster deployed on refreshed rack hardware, management of storage buckets for all clusters must be done through the first cluster in the zone, also known as the Storage Infrastructure Cluster (SIC). This is because bucket access is granted through roles to users on the SIC. When access to a bucket is granted, a secret is generated on the SIC for the associated user. Google Distributed Cloud connected now automatically synchronizes storage secrets across clusters, and you no longer have to manually copy those secrets to each target cluster.




The following Google Distributed Cloud connected components have been updated:

  * **GDC software-only** has been updated from version 1.29.800 to version 1.30.500. (This component was formerly known as GKE on Bare Metal and as Anthos Clusters on Bare Metal.)

  * **Kubernetes** has been updated from version 1.29 to version 1.30.

  * **Symcloud Storage** has been updated from version 5.4.8 to version 5.4.14-63.




Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

  * **OS layer security mitigations:** CVE-2024-53227, CVE-2024-38589, CVE-2024-56770, CVE-2024-56779, CVE-2024-56724, CVE-2024-56723, CVE-2024-56720, CVE-2024-56688, CVE-2024-56642, CVE-2024-56606, CVE-2024-35925, CVE-2024-35933, CVE-2024-35930, CVE-2024-35895, CVE-2024-35855, CVE-2024-35852, CVE-2024-35847, CVE-2024-42145, CVE-2024-53066, CVE-2024-53061, CVE-2024-53057, CVE-2024-50151, CVE-2024-50142, CVE-2024-46771, CVE-2024-50202, CVE-2024-50143, CVE-2024-50251, CVE-2024-50237, CVE-2024-50234, CVE-2024-49968, CVE-2024-43846, CVE-2024-50058, CVE-2024-47696, CVE-2024-47671, CVE-2024-47668, CVE-2024-47667, CVE-2024-47663, CVE-2024-46840, CVE-2024-46854, CVE-2024-46844, CVE-2024-46829, CVE-2024-46822, CVE-2024-46750, CVE-2024-46744, CVE-2024-40905, CVE-2024-38588, CVE-2024-46707, CVE-2021-47619

  * **GDC software-only security mitigations:** CVE-2022-36227, CVE-2024-45491, CVE-2024-45492, CVE-2020-16156, CVE-2021-33194, CVE-2022-1304, CVE-2022-27664, CVE-2022-41723, CVE-2022-48733, CVE-2023-3676, CVE-2023-3955, CVE-2023-5528, CVE-2023-7104, CVE-2023-39325, CVE-2023-49083, CVE-2023-52425, CVE-2024-0743, CVE-2024-0793, CVE-2024-6609, CVE-2024-20696, CVE-2024-38577, CVE-2024-41011, CVE-2024-42228, CVE-2024-42280, CVE-2024-42284, CVE-2024-42285, CVE-2024-42301, CVE-2024-42302, CVE-2024-42313, CVE-2024-43839, CVE-2024-43858, CVE-2024-43882, CVE-2024-44974, CVE-2024-44987, CVE-2024-44998, CVE-2024-44999, CVE-2024-45490, CVE-2024-46673, CVE-2024-46674, CVE-2024-46722, CVE-2024-46723, CVE-2024-46724, CVE-2024-46725, CVE-2024-46731, CVE-2024-46738, CVE-2024-46740, CVE-2024-46743, CVE-2024-46744, CVE-2024-46747, CVE-2024-46756, CVE-2024-46757, CVE-2024-46758, CVE-2024-46759, CVE-2024-46782, CVE-2024-46798, CVE-2024-46800, CVE-2024-46804, CVE-2024-46814, CVE-2024-46815, CVE-2024-46818, CVE-2024-46828, CVE-2024-46844, GHSA-m425-mq94-257g, CVE-2021-31525, CVE-2021-3669, CVE-2021-36976, CVE-2022-26280, CVE-2022-41717, CVE-2023-2431, CVE-2023-2727, CVE-2023-2728, CVE-2023-3978, , CVE-2023-23931, CVE-2023-31083, CVE-2023-44487, CVE-2023-52889, CVE-2024-24557, CVE-2024-29018, CVE-2024-41098, CVE-2024-42114, CVE-2024-42246, CVE-2024-42259, CVE-2024-42272, CVE-2024-42283, CVE-2024-42286, CVE-2024-42287, CVE-2024-42288, CVE-2024-42289, CVE-2024-42297, CVE-2024-42309, CVE-2024-42310, CVE-2024-42311, CVE-2024-43828, CVE-2024-43829, CVE-2024-43834, CVE-2024-43835, CVE-2024-43846, CVE-2024-43849, CVE-2024-43853, CVE-2024-43854, CVE-2024-43856, CVE-2024-43860, CVE-2024-43861, CVE-2024-43871, CVE-2024-43884, CVE-2024-43889, CVE-2024-43890, CVE-2024-43892, CVE-2024-43893, CVE-2024-43894, CVE-2024-43905, CVE-2024-43907, CVE-2024-43908, CVE-2024-43914, CVE-2024-44935, CVE-2024-44944, CVE-2024-44946, CVE-2024-44947, CVE-2024-44954, CVE-2024-44960, CVE-2024-44965, CVE-2024-44968, CVE-2024-44971, CVE-2024-44988, CVE-2024-44989, CVE-2024-44990, CVE-2024-44995, CVE-2024-45003, CVE-2024-45006, CVE-2024-45016, CVE-2024-45018, CVE-2024-45021, CVE-2024-45025, CVE-2024-45028 CVE-2024-46675, CVE-2024-46676, CVE-2024-46677, CVE-2024-46679, CVE-2024-46685, CVE-2024-46689, CVE-2024-46702, CVE-2024-46707, CVE-2024-46714, CVE-2024-46719, CVE-2024-46721, CVE-2024-46737, CVE-2024-46739, CVE-2024-46750, CVE-2024-46755, CVE-2024-46763, CVE-2024-46771, CVE-2024-46777, CVE-2024-46780, CVE-2024-46781, CVE-2024-46783, CVE-2024-46791, CVE-2024-46817, CVE-2024-46819, CVE-2024-46822, CVE-2024-46829, CVE-2024-46840, CVE-2024-47663, GHSA-jq35-85cj-fj4p, CVE-2024-43167, CVE-2024-43168, CVE-2024-3177, CVE-2021-36084, CVE-2021-36085, CVE-2021-36086, CVE-2021-36087, CVE-2021-36690, CVE-2024-43841




The following documentation updates have been implemented in this release of Google Distributed Cloud connected:

  * **Survivability mode.** We have clarified how a cluster enters survivability, what happens when a cluster enters survivability mode, and how Google supports clusters that have entered survivability mode. For more information, see [Survivability mode](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/survivability).

  * **Offline cluster credential generation.** We have updated the "Create and manage clusters" page with steps for generating offline cluster credentials. For more information, see [Obtain credentials for a cluster](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters#credentials).




This is a minor release of Google Distributed Cloud connected (version 1.9.0).

## February 21, 2025

Distributed Cloud connected 1.8.0

Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

  * **OS layer security mitigations:** CVE-2024-41087, CVE-2024-40961, CVE-2024-41000, CVE-2024-40995, CVE-2024-38588, CVE-2024-40905, CVE-2024-40959, CVE-2024-39487, CVE-2024-42131, CVE-2024-42145, CVE-2024-36901

  * **GKE on Bare Metal security mitigations:** CVE-2024-37371, CVE-2021-38297, CVE-2022-23806, CVE-2023-24538, CVE-2023-24540, CVE-2023-25775, CVE-2023-29402, CVE-2023-29404, CVE-2023-29405, CVE-2020-22218, CVE-2024-0553, CVE-2024-0567, CVE-2024-37370, GHSA-87m9-rv8p-rgmg, CVE-2024-39487, CVE-2024-41040, CVE-2024-41046, CVE-2024-41049, CVE-2024-41059, CVE-2024-41070, CVE-2024-42104, CVE-2024-42148, CVE-2023-49083, CVE-2024-0743, CVE-2024-6609, CVE-2024-46738, CVE-2024-46740, CVE-2024-46743, CVE-2024-46744, CVE-2024-46747, CVE-2024-46756, CVE-2024-46757, CVE-2024-46758, CVE-2024-46759, CVE-2024-46782, CVE-2024-46798, CVE-2024-46800, CVE-2024-46804, CVE-2024-46814, CVE-2024-46815, CVE-2024-46818, CVE-2024-46828, CVE-2024-46844, CVE-2020-29652, CVE-2021-29923, CVE-2021-33195, CVE-2021-33196, CVE-2021-33198, CVE-2021-39293, CVE-2021-41771, CVE-2021-41772, CVE-2021-44716, CVE-2022-2879, CVE-2022-2880, CVE-2022-21698, CVE-2022-23772, CVE-2022-23773, CVE-2022-24675, CVE-2022-24921, CVE-2022-28131, CVE-2022-28327, CVE-2022-28948, CVE-2022-30580, CVE-2022-30630, CVE-2022-30631, CVE-2022-30632, CVE-2022-30633, CVE-2022-30635, CVE-2022-32189, CVE-2022-41715, CVE-2022-41724, CVE-2022-41725, CVE-2023-5717, CVE-2023-6040, CVE-2023-6356, CVE-2023-6536, CVE-2023-6606, CVE-2023-6931, CVE-2023-6932, CVE-2023-24534, CVE-2023-24536, CVE-2023-24537, CVE-2023-24539, CVE-2023-29400, CVE-2023-29403, CVE-2023-29499, CVE-2023-35827, CVE-2023-46838, CVE-2023-51780, CVE-2023-51781, CVE-2023-51782, CVE-2023-52436, CVE-2023-52439, CVE-2023-52444, CVE-2023-52445, CVE-2023-52451, CVE-2023-52464, CVE-2023-52469, CVE-2024-1086, CVE-2024-26586, CVE-2024-26597, CVE-2024-26598, CVE-2023-6270, CVE-2023-39323, CVE-2023-45285, CVE-2023-45287, CVE-2023-52434, CVE-2024-0565, CVE-2024-0985, CVE-2024-26882, CVE-2024-26883, CVE-2024-26884, CVE-2024-26898, CVE-2024-26907, CVE-2024-26934, CVE-2024-27020, CVE-2022-48655, CVE-2019-16884, CVE-2021-30465, CVE-2021-33194, CVE-2021-38561, CVE-2021-43565, CVE-2021-43816, CVE-2022-23648, CVE-2022-27191, CVE-2022-27664, CVE-2022-32149, CVE-2022-41723, CVE-2022-43945, CVE-2024-36971, CVE-2024-38583, CVE-2024-39480, CVE-2024-39495, CVE-2024-40902, CVE-2024-7348, CVE-2023-47038, CVE-2024-42161, CVE-2024-42224, CVE-2024-6104, GHSA-mh55-gqvf-xfwm, CVE-2016-3709, CVE-2024-7264, CVE-2024-36901, CVE-2024-36938, CVE-2024-41009, CVE-2024-41012, CVE-2024-41055, CVE-2024-41063, CVE-2024-41064, CVE-2024-42101, CVE-2024-42102, CVE-2024-42131, CVE-2024-42137, CVE-2024-42152, CVE-2024-42153, CVE-2024-42154, CVE-2023-23931, CVE-2024-50096, CVE-2024-50099, CVE-2021-3669, CVE-2021-3733, CVE-2021-4189, CVE-2023-27043, CVE-2023-31083, CVE-2023-40217, CVE-2023-52889, CVE-2024-41098, CVE-2024-42114, CVE-2024-42246, CVE-2024-42259, CVE-2024-42272, CVE-2024-42283, CVE-2024-42286, CVE-2024-42287, CVE-2024-42288, CVE-2024-42289, CVE-2024-42297, CVE-2024-42309, CVE-2024-42310, CVE-2024-42311, CVE-2024-43828, CVE-2024-43829, CVE-2024-43834, CVE-2024-43835, CVE-2024-43846, CVE-2024-43849, CVE-2024-43853, CVE-2024-43854, CVE-2024-43856, CVE-2024-43860, CVE-2024-43861, CVE-2024-43871, CVE-2024-43884, CVE-2024-43889, CVE-2024-43890, CVE-2024-43892, CVE-2024-43893, CVE-2024-43894, CVE-2024-43905, CVE-2024-43907, CVE-2024-43908, CVE-2024-43914, CVE-2024-44935, CVE-2024-44944, CVE-2024-44946, CVE-2024-44947, CVE-2024-44954, CVE-2024-44960, CVE-2024-44965, CVE-2024-44968, CVE-2024-44971, CVE-2024-44988, CVE-2024-44989, CVE-2024-44990, CVE-2024-44995, CVE-2024-45003, CVE-2024-45006, CVE-2024-45016, CVE-2024-45018, CVE-2024-45021, CVE-2024-45025, CVE-2024-45028, CVE-2024-46675, CVE-2024-46676, CVE-2024-46677, CVE-2024-46679, CVE-2024-46685, CVE-2024-46689, CVE-2024-46702, CVE-2024-46707, CVE-2024-46714, CVE-2024-46719, CVE-2024-46721, CVE-2024-46737, CVE-2024-46739, CVE-2024-46750, CVE-2024-46755, CVE-2024-46763, CVE-2024-46771, CVE-2024-46777, CVE-2024-46780, CVE-2024-46781, CVE-2024-46783, CVE-2024-46791, CVE-2024-46817, CVE-2024-46819, CVE-2024-46822, CVE-2024-46829, CVE-2024-46840, CVE-2024-47663, CVE-2020-29509, CVE-2020-29511, CVE-2021-33197, CVE-2021-34558, CVE-2021-36221, CVE-2021-44879, CVE-2022-1705, CVE-2022-1962, CVE-2022-32148, CVE-2022-41717, CVE-2023-3446, CVE-2023-3817, CVE-2023-6004, CVE-2023-6121, CVE-2023-6915, CVE-2023-6918, CVE-2023-24532, CVE-2023-29406, CVE-2023-29409, CVE-2023-32611, CVE-2023-32665, CVE-2023-34324, CVE-2023-39198, CVE-2023-39804, CVE-2023-45863, CVE-2023-46218, CVE-2023-46343, CVE-2023-49290, CVE-2023-52443, CVE-2023-52449, CVE-2023-52470, CVE-2024-21664, CVE-2024-28085, GHSA-2c7c-3mj9-8fqh, CVE-2024-2961, CVE-2024-28182, CVE-2023-7042, CVE-2023-39318, CVE-2023-39319, CVE-2023-39326, CVE-2023-47233, CVE-2023-52429, CVE-2023-52435, CVE-2023-52458, CVE-2024-0340, CVE-2024-0607, CVE-2024-22099, CVE-2024-23849, CVE-2024-23851, CVE-2024-24857, CVE-2024-24858, CVE-2024-24861, CVE-2024-25739, CVE-2024-26600, CVE-2024-26602, CVE-2024-26606, CVE-2024-26901, CVE-2024-26903, CVE-2024-26910, CVE-2024-27013, CVE-2024-33599, CVE-2024-33600, CVE-2024-33601, CVE-2024-33602, CVE-2024-35978, CVE-2024-35982, CVE-2024-35984, CVE-2024-35997, GHSA-6xv5-86q9-7xr8, CVE-2024-26900, CVE-2024-28122, CVE-2024-35255, CVE-2024-36902, CVE-2019-19921, CVE-2021-31525, CVE-2021-32760, CVE-2021-41103, CVE-2021-43784, CVE-2022-23471, CVE-2022-29162, CVE-2022-29526, CVE-2022-31030, CVE-2022-40735, CVE-2022-41717, CVE-2023-25153, CVE-2023-25173, CVE-2023-28642, CVE-2023-48795, CVE-2024-27019, CVE-2024-36288, CVE-2024-38662, CVE-2024-38780, CVE-2024-39292, CVE-2024-39475, CVE-2024-39476, CVE-2024-39482, CVE-2024-39484, CVE-2024-39489, CVE-2024-39493, CVE-2024-42070, CVE-2024-42076, CVE-2024-42077, CVE-2024-42082, GHSA-7ww5-4wqc-m92c, CVE-2023-5981, CVE-2024-42157, CVE-2024-42223, CVE-2024-42229, CVE-2024-42232, CVE-2024-42236, CVE-2024-42244, CVE-2024-42247, CVE-2021-3426, CVE-2021-28861, CVE-2021-29921, CVE-2022-42919, CVE-2023-6597, CVE-2023-28450, CVE-2023-50387, CVE-2023-50868, CVE-2024-0397, CVE-2024-4032, CVE-2024-8088, CVE-2024-8508, CVE-2024-8775, CVE-2024-9287, CVE-2024-9902, CVE-2024-11168, CVE-2024-43841, CVE-2021-25743, CVE-2022-30629, CVE-2023-26604, CVE-2023-2975, CVE-2023-5178, CVE-2023-5197, CVE-2023-6531, CVE-2023-6817, CVE-2023-46813, CVE-2023-46862, CVE-2023-52438, CVE-2022-38096, CVE-2023-5363, CVE-2023-6246, CVE-2023-6779, CVE-2023-6780, CVE-2023-52447, CVE-2023-52489, CVE-2023-52492, CVE-2023-52493, CVE-2023-52497, CVE-2023-52616, CVE-2023-52627, CVE-2023-52637, CVE-2023-52672, CVE-2024-0841, CVE-2024-23850, CVE-2024-26581, CVE-2024-26593, CVE-2024-26601, CVE-2024-26610, CVE-2024-26627, CVE-2024-26643, CVE-2024-26665, CVE-2024-26673, CVE-2024-26684, CVE-2024-26688, CVE-2024-26695, CVE-2024-26698, CVE-2024-26702, CVE-2024-26707, CVE-2024-26712, CVE-2024-26727, CVE-2024-26748, CVE-2024-26749, CVE-2024-26753, CVE-2024-26781, CVE-2024-26782, CVE-2024-26787, CVE-2024-26788, CVE-2024-26790, CVE-2024-26795, CVE-2024-26808, CVE-2024-26809, CVE-2024-26814, CVE-2024-26833, CVE-2024-26835, CVE-2024-26848, CVE-2024-26855, CVE-2024-26861, CVE-2024-26862, CVE-2024-26870, CVE-2024-26877, CVE-2024-26885, CVE-2024-26891, CVE-2024-26895, CVE-2024-26897, CVE-2024-26924, CVE-2024-26925, CVE-2024-26926, CVE-2024-26935, CVE-2024-26937, CVE-2024-26950, CVE-2024-26951, CVE-2024-26970, CVE-2024-26978, CVE-2024-26988, CVE-2024-27030, CVE-2024-27038, CVE-2024-27044, CVE-2024-27045, CVE-2024-27047, CVE-2024-27052, CVE-2024-27053, CVE-2024-27065, CVE-2024-27076, CVE-2024-27414, CVE-2024-27417, CVE-2024-27431, CVE-2024-35785, CVE-2024-35796, CVE-2024-35813, CVE-2024-35829CVE-2023-25809, GHSA-5j5w-g665-5m35, GHSA-77vh-xpmg-72qh, GHSA-c9cp-9c75-9v8c, CVE-2022-48303, CVE-2022-2309, CVE-2024-41007, CVE-2024-43167, CVE-2024-43168, GHSA-xr7q-jx4m-x55m.




The following changes to existing functionality have been introduced in this release of Google Distributed Cloud connected:

  * **Kubernetes metadata API now required for cluster creation and upgrades.** You must enable the `kubernetesmetadata.googleapis.com` API to create Google Distributed Cloud connected clusters. This API is also required for upgrading clusters to Google Distributed Cloud connected software version 1.8.0. For more information, see [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters).

  * **Configure CMEK on existing clusters and node pools.** You can now enable and disable support for Customer-Managed Encryption Keys (CMEK) on existing Google Distributed Cloud connected clusters and node pools. For more information, see [Local storage security](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/security#storage).

  * **Improved hardware ordering process.** The ordering process for Google Distributed Cloud connected hardware has been improved. For more information, see [Order hardware](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/order).

    * The order form for Google Distributed Cloud connected hardware in the Cloud console now has feature parity with the Google Distributed Cloud Hardware Management API.
    * The Google Distributed Cloud Hardware Management API has been improved with more robust functionality.
  * **Overhauled pricing page.** The pricing page for Google Distributed Cloud connected has been overhauled to include detailed pricing information for the supported form factors and their respective regions. For more information, see [Pricing](https://cloud.google.com/distributed-cloud/edge/latest/pricing).

  * **Hardware ordering documentation has been expanded.** The "Order hardware" page has been expanded with additional information on prerequisites, enabling the Google Distributed Cloud Hardware Management API, and the actions that can be performed on an order. For more information, see [Order hardware](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/order).




The following functionality has been deprecated in this release of Google Distributed Cloud connected:

  * **Legacy GDC connected rack hardware.** The legacy GDC connected rack hardware (also known as "Config 1" and "Config 2") has reached end-of-sale and can no longer be ordered. Google continues to support your existing legacy rack deployments until the end of your contract term. For more information, contact your Google field sales representative.

  * **GPU workloads on refreshed GDC connected racks.** The refreshed Google Distributed Cloud connected rack hardware does not support GPU workloads. GPU workloads are supported on Google Distributed Cloud connected legacy rack hardware and on Google Distributed Cloud connected servers as a limited-access feature.

  * **Virtual machine workloads on refreshed GDC connected racks.** The refreshed Google Distributed Cloud connected rack hardware does not support virtual machine workloads. Virtual machine workloads are supported on Google Distributed Cloud connected legacy rack hardware and on Google Distributed Cloud connected servers.




The following new functionality has been introduced in this release of Google Distributed Cloud connected:

  * **Refreshed GDC connected rack hardware.** New GDC connected rack hardware is now available for purchase as a preview-level offering. This new offering allows you to deploy GDC connected racks as combinations of base rack pairs and up to three expansion racks for each zone. Each rack is populated by up to four compute blocks of three machines each. For more information, see [Google Distributed Cloud connected form factors](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/how-it-works#form-factors).

  * **GDC connected services platform.** Google Distributed Cloud connected now ships with a platform supporting the deployment of select Google services. For more information, see [Manage Google services](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/services).

  * **GPU workloads on GDC connected servers.** You can now deploy GPU-based workloads on Google Distributed Cloud connected servers. The machines now ship with optional NVIDIA L4 GPUs. For more information, see [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/gpu). This is a limited-access feature; contact your Google field sales representative for details.

  * **Configurable local storage schemas.** You can now configure the local storage present on GDC connected deployments with custom schemas. For more information, see [Configure local storage schemas](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/storage#schemas).

  * **Network connectivity verification tool.** Google Distributed Cloud connected now offers a tool that allows you to verify that your local network meets the connectivity requirements for Google Distributed Cloud connected. For more information, see [Validate your connectivity before ordering Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/requirements#validate_your_connectivity_before_ordering_connected).

  * **L2 load balancer virtual IP pool support.** You can now specify IPv4 and IPv6 addresses, address ranges, or subnetworks for ingress traffic for services that run behind the GDC connected L2 load balancer when the cluster is running in survivability mode. For more information, see [Layer 2 load balancing with MetalLB](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking#load-balancing-metal-lb).

  * **Terraform support for the Edge Container API.** The Google Distributed Cloud Connected Edge Container API is now supported in Terraform. See the [Terraform repository](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/edgecontainer_cluster) for details.

  * **Symcloud Storage metrics.** Certain metrics for Symcloud Storage are now available in Cloud Monitoring. For more information, see [Google Distributed Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos#anthos).




This is a minor release of Google Distributed Cloud connected (version 1.8.0).

The following issues have been resolved in this release of Google Distributed Cloud connected:

  * **Virtual machine management no longer fails after extended power or network connectivity loss.** If one or more nodes in a cluster loses power or network connectivity for an extended period of time, you can now reliably manage virtual machines scheduled on the affected nodes after power or network connectivity is restored.

  * **The Kubernetes API server no longer returns 404 errors when attempting to access virt-api endpoints**. 

  * **Cluster deletion no longer fails due to stale Symcloud Storage data.** You can now reliably delete a cluster during disaster recovery or cluster reset. Symcloud Storage now properly cleans up the corresponding Symcloud Storage volumes.

  * **Containerized Data Importer (CDI) import performance has been improved**. When creating a virtual machine that uses a block Symcloud Storage volume, the speed of importing machine images has been significantly improved.




The following Google Distributed Cloud connected components have been updated:

  * **GKE on Bare Metal** has been updated from version 1.28.700-gke.154 to version 1.29.800-gke.111. (This component was formerly known as Anthos Clusters on Bare Metal.)

  * **Kubernetes** has been updated from version 1.28.10 to version 1.29.




This release of Google Distributed Cloud connected contains the following known issues:

  * **Virtual machines using file-based Symcloud Storage volumes can experience a CDI import error**. When creating a virtual machine that uses a file-based Symcloud Storage volume, you can experience a CDI import failure. To work around this issue, add the following annotation to the corresponding Symcloud storage class config:
        
        annotations:
                cdi.kubevirt.io/enable-qemu-target-zero-option: "false"
        

  * **The Storage Infrastructure Cluster cannot be deleted.** On refreshed rack hardware deployments, the first cluster in a Google Distributed Cloud connected zone, also known as the Storage Infrastructure Cluster (SIC) cannot be deleted. Doing so would render Google Distributed Cloud connected storage inoperable. This is intentional behavior. Legacy Google Distributed Cloud connected rack hardware deployments and Google Distributed Cloud connected server deployments are not affected by this issue.

  * **You must manually copy storage secrets for corresponding buckets to the target clusters in a zone.** For Google Distributed Cloud connected zones with more than one cluster deployed on refreshed rack hardware, management of storage buckets for all clusters must be done through the first cluster in the zone, also known as the Storage Infrastructure Cluster (SIC). This is because bucket access is granted through roles to users on the SIC. When access to a bucket is granted, a secret is generated on the SIC for the associated user, and Google Distributed Cloud connected does not synchronize storage secrets across clusters. To work around this issue, you must manually copy the respective storage secrets from the "storage infrastructure cluster" to the cluster on which the corresponding storage buckets are used. Legacy Google Distributed Cloud connected rack hardware deployments and Google Distributed Cloud connected server deployments do not use a SIC and are not affected by this issue.

  * **Storage is not freed immediately upon cluster deletion.** After deleting a cluster, the storage used by that cluster is not freed up immediately. This is because storage clean-up is part of a garbage collection task that runs infrequently. To work around this issue, manually delete all of a cluster's persistent volumes before deleting the cluster itself.

  * **Machines can experience intermittent connectivity loss.** Google Distributed Cloud connected machines can experience intermittent connectivity loss due to a rare condition that can occur with fleet credential management. To remedy this issue, [contact Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **After a network disruption, Symcloud Storage volumes can fail to mount or dismount**. If a node that uses Symcloud Storage volumes experiences a network disconnection, the Symcloud Storage volumes can fail to mount or dismount after network connectivity is restored. This is caused by the `iomgr` service entering a degraded state. To work around this issue, delete the `iomgr` container on the affected node.

  * **Reallocating a GPU resource from a VM to a container can cause an initialization error**. When you reallocate a GPU from a virtual machine workload to a container workload, you might receive an NVML initialization error. To remedy this issue, [contact Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **The`anthos-multinet` container might take up to two hours to fully start.** You might intermittently experience a slower than normal startup for the `anthos-multinet` container (up to two hours). To remedy this issue, [contact Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).




## August 07, 2024

Distributed Cloud connected 1.7.1

This release of Google Distributed Cloud connected contains the following known issues:

  * **Virtual machine management can fail after a node has been powered down for an extended time.** If you power down your Google Distributed Cloud connected machines for an extended period of time, you might not be able to manage the virtual machines scheduled on the corresponding nodes after you power the machines back up, even though those virtual machine workloads continue to run. To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **The Kubernetes API server might return 404 errors when attempting to access`virt-api` endpoints.** To work around this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Storage operations hang when volume replicas are deleted from a cluster without removing the corresponding Symcloud Storage persistent volume intent.** If you delete the volume replicas for a Symcloud Storage persistent volume but do not remove the corresponding intent, TCMU devices on the worker node hang, causing storage operations to stall indefinitely. This can affect both your workload data availability as well core system functionality of Google Distributed Cloud connected. To prevent this, you must always remove a Symcloud Storage persistent volume before deleting its associated volume replicas. If you need to resolve this issue on an affected node, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Cluster deletion can fail due to stale Symcloud Storage data.** When attempting to delete a cluster during disaster recovery or cluster reset, the deletion might fail due to the corresponding Symcloud Storage volumes not having been cleaned up. To resolve this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Cluster upgrades might fail with an "`ABM upgrade timed out`" error.** Under certain conditions, if the GKE token expires while a cluster upgrade is in progress, the upgrade fails with an "`ABM upgrade timed out`" error and a missing `gkehub.memberships.update` permission is recorded in the logs. If you encounter this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Removing the`NodeSelector` node label value in the `NodeSystemConfigUpdate` resource after reconciliation does not reset the node status to default.** If you remove the node label value in the `NodeSelector` field of the `NodeSystemConfigUpdate` resource after the resource has been successfully reconciled, the node does not revert to its default configuration.




Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

  * CVE-2024-36971, CVE-2024-36901, CVE-2024-36969, CVE-2024-36902 CVE-2024-36893, CVE-2024-36897, CVE-2024-35984, CVE-2024-35997, CVE-2024-6387 (GCP-2024-040), CVE-2024-38433, CVE-2024-0172



The following new functionality has been introduced in this release of Google Distributed Cloud connected:

  * **Active backup network redundancy**. On Google Distributed Cloud connected servers, you can now opt in to active backup network redundancy mode for each Google Distributed Cloud connected zone. This mode improves resilience to network interruptions when you have a redundant network link available. To enable this feature, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Single-node configuration for GDCc servers.** You now have the option to order and deploy Google Distributed Cloud servers in single-node configurations. For more information, contact your Google field sales representative.




The following issues have been resolved in this release of Google Distributed Cloud connected:

  * **Nodes no longer get stuck in`Ready,SchedulingDisabled` state after applying configuration changes.** Applying or deleting the `NodeSystemConfigUpdate` or `SriovNetworkNodePolicy` resources no longer results in a node that's stuck in the `Ready,Scheduling Disabled` state after it reboots.

  * **Cluster software upgrades are no longer affected by GKE Identity Service (GKE IS) Pods that get stuck in a`Failed` state after a machine reboot.**

  * **Virtual machine workloads no longer temporarily go down when upgrading Google Distributed Cloud connected software.** The virtual machine workloads now remain running while a Google Distributed Cloud software upgrade completes.

  * **Changes to the`VMRuntime` resource are no longer required before upgrading to Google Distributed Cloud connected version 1.7.1 or higher.**

  * **Excessive CPU load on nodes undergoing live virtual machine migration during software upgrades has been resolved.** When completing a live virtual machine migration during a Google Distributed Cloud connected software upgrade, nodes no longer experience CPU spikes that might affect workloads running on them.

  * **Virtual machines no longer lose connectivity to each other during a live migration.** When completing a live migration of virtual machines from one node to another, the virtual machines now retain network connectivity to each other across the source and destination nodes.

  * **Virtual machines are now properly scheduled after recovery from a network partition.** When a loss of network connectivity across multiple nodes occurs and causes a stall in storage I/O operations, the virtual machine fencing logic now properly marks the affected virtual machines as failed. Such virtual machines are now properly scheduled back onto the affected nodes when network connectivity is restored.




The following Google Distributed Cloud connected components have been updated:

  * **GKE on Bare Metal** has been updated from version 1.28.500 to version 1.28.700. (This component was formerly known as Anthos Clusters on Bare Metal.)
  * **Kubernetes** has been updated from version 1.28.8 to version 1.28.10.



This is a patch release of Google Distributed Cloud connected (version 1.7.1).

## July 08, 2024

Distributed Cloud connected 1.7.0

This is a minor release of Google Distributed Cloud connected (version 1.7.0).

The following new functionality has been introduced in this release of Google Distributed Cloud connected:

  * **Customer-sourced hardware.** You now have the option to purchase the Google Distributed Cloud connected hardware from a Google-partnered System Integrator (SI) and retain full ownership instead of leasing it from Google. For more information, contact your Google field sales representative.

  * **Refreshed machine hardware.** The server machines comprising Google Distributed Cloud connected racks have been updated to a more powerful hardware configuration. For more information, see [Plan the hardware configuration](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/requirements#hardware).

  * **Flexible rack configuration.** You can now order a Google Distributed Cloud connected rack with 3, 6, 9, or 12 server machines. For more information, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **IPv4/IPv6 dual-stack networking.** Google Distributed Cloud connected now supports IPv6 networking in addition to IPv4 networking. For more information, see [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking#dual-stack).

  * **VM support on GDC connected servers.** Google Distributed Cloud connected servers now support running virtual machine workloads. For more information, see [Manage virtual machines on Distributed Cloud connected servers](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers).

  * **Pod image caching.** Google Distributed Cloud connected now supports local caching of Pod images. For more information, see [Configure a Pod for image caching](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/deploy#configure_a_pod_for_image_caching).

  * **Kafka support.** Google Distributed Cloud now supports collecting workload metrics with [Apache Kafka](https://kafka.apache.org/). For more information, see [Logs and metrics](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/logs-metrics).

  * **Cluster connection state indication.** You can now check whether a cluster is connected, disconnected, or reconnected and synchronizing with Google Cloud Platform. For more information, see [Survivability mode](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/survivability).

  * **Cluster maintenance exclusion windows.** You can now specify one or more maintenance exclusion windows for a cluster. This prevents Google from performing maintenance or software upgrades on the cluster during the specified times. For more information, see [Understand software updates and maintenance windows](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/availability#cluster-maintenance).

  * **GDC Hardware Management API.** You can now place orders for Google Distributed Cloud connected hardware programmatically using the GDC Hardware Management API. For more information, see [Google Distributed Cloud connected CLI and API reference](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/apis). This is a Preview-level feature.




The following functionality has been deprecated in this release of Google Distributed Cloud connected:

  * **Cloud control plane cluster support.** As of this release, Google Distributed Cloud connected no longer supports Cloud control plane clusters. Local control plane clusters are now the only supported cluster type.

  * **Raw block storage for virtual machine workloads.** As of this release, you can no longer provision virtual machine workloads with raw block storage. Symcloud Storage is now the only supported storage type for virtual machine workloads.




The following issues have been resolved in this release of Google Distributed Cloud connected:

  * **Symcloud Storage volume clean-up now functions correctly.** Single node failures, such as power loss or network disconnection, no longer cause rescheduling failures for virtual machines that use Symcloud Storage volumes. When a node fails, virtual machines are automatically rescheduled onto another node and then scheduled back onto the original node once that node returns to operation.

  * **Virtual machines no longer enter a stuck state when node network connections are intermittent.** Virtual machines no longer get stuck in container creation state when their network connections repeatedly disconnect and reconnect. When all three nodes in a Google Distributed Cloud connected server group regain network connectivity, the affected virtual machines are automatically rescheduled back onto their original nodes.

  * **Virtual machine restore operations now complete successfully.** Problems related to taking subsequent snapshots of virtual machines after the initial ones have been resolved. These problems caused virtual machine restore operations to fail.

  * **Virtual machine heartbeat has been tuned to increase failover resilience.** Occasionally, when a node failed, virtual machines on other nodes in the cluster would fail multiple successive heartbeats to the Kubernetes control plane that ran on the failed node. The heartbeat configuration has been tuned to mitigate this and increase failover resilience.

  * **Intermittent SR-IOV device availability on large deployments has been resolved.** SR-IOV devices are no longer intermittently unavailable on large, long-uptime deployments of Google Distributed Cloud connected after creating SR-IOV network node policies.




The following changes to existing functionality have been introduced in this release of Google Distributed Cloud connected:

  * **Bastion host GA.** The bastion host feature of Google Distributed Cloud connected is now generally available. For more information, see [Configure a bastion host](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/bastion).

  * **Worker node software upgrades are now staggered.** Google Distributed Cloud connected now upgrades worker node software in stages instead of all at once. This allows your workloads to continue running on some nodes, while others are upgrading. You have the option to specify the number of worker nodes that can go down for a software upgrade simultaneously. For more information, see [Software update staggering](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/availability#update-staggering).

  * **GPU support is now automatically enabled.** You no longer have to modify the `VMRuntime` resource to enable GPU support on Google Distributed Cloud connected. GPU support is now automatically enabled if a GPU is detected on a Google Distributed Cloud connected machine.

  * **Google Distributed Cloud connected component updates:**

    * **GKE on Bare Metal.** This component has been updated from version 1.1.6.1 to version 1.28.500.
    * **Kubernetes control plane.** This component has been updated from version 1.27.9 to version 1.28.8.
    * **Symcloud Storage.** This component has been updated from version 5.4.6 to version 5.4.8.
  * **Anthos branding has been replaced with Google Kubernetes Service branding.** Anthos features and services that Google Distributed Cloud connected relies on, such as Anthos Identity Service, have been rebranded to Google Kubernetes Service. You might still see references to the legacy branding in Google Distributed Cloud connected command output and error messages.




Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

  * CVE-2024-26934, CVE-2024-27013, CVE-2024-26884, CVE-2024-26902, CVE-2022-48659, CVE-2024-26901, CVE-2024-26910, CVE-2024-26883, CVE-2024-26898, CVE-2024-26882, CVE-2024-26908, CVE-2024-26585, CVE-2021-46904, CVE-2021-46905, CVE-2020-36775, CVE-2021-46909, CVE-2021-46906, CVE-2019-25162, CVE-2024-26606, CVE-2024-26602, CVE-2024-26600, CVE-2023-52469, CVE-2023-52470, CVE-2022-48626, CVE-2024-26597, CVE-2023-52464, CVE-2024-26598, CVE-2024-0340, CVE-2024-23849, CVE-2024-23850, CVE-2024-23851, CVE-2023-52439, CVE-2023-52435, CVE-2023-52443, CVE-2023-46343, CVE-2024-0607, CVE-2024-22705, CVE-2023-46838, CVE-2023-51782, CVE-2023-51781, CVE-2023-51780, CVE-2024-1086, CVE-2024-0584, CVE-2024-0562, CVE-2023-6915, CVE-2024-0646, CVE-2023-6040, CVE-2023-46862, CVE-2023-46813, CVE-2023-6932, CVE-2023-6931, CVE-2023-5178, CVE-2023-5717



This release of Google Distributed Cloud connected contains the following known issues:

  * **Refreshed Google Distributed Cloud connected hardware requires Google Distributed Cloud connected software version 1.7.0 or later.** The refreshed Google Distributed Cloud connected hardware does not support versions of Google Distributed Cloud connected prior to release 1.7.0.

  * **Virtual machine workloads might temporarily go down when upgrading Google Distributed Cloud connected software to release 1.7.0.** The virtual machine workloads will go back up and be healthy once the Google Distributed Cloud software upgrade completes.

  * **Cluster upgrades to software release 1.7.0 might fail with an `ABM upgrade timed out` error. Under certain conditions, if the GKE token expires while a cluster upgrade is in progress, the upgrade fails with an `ABM upgrade timed out` error and a missing `gkehub.memberships.update` permission is recorded in the logs. If you encounter this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Storage operations hang when volume replicas are deleted from a cluster without removing the corresponding Symcloud Storage persistent volume intent.** If you delete the volume replicas for a Symcloud Storage persistent volume but do not remove the corresponding intent, TCMU devices on the worker node hang, causing storage operations to stall indefinitely. This can affect both your workload data availability as well core system functionality of Google Distributed Cloud connected. To prevent this, you must always remove a Symcloud Storage persistent volume before deleting its associated volume replicas.

  * **Virtual machines might not get scheduled onto nodes after their network has been partitioned.** When you partition a network, some virtual machines using that network might not get scheduled back onto their node after the node reconnects to the network. To work around this issue, restart the affected virtual machines or contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Cluster deletion can fail due to stale Symcloud Storage data.** When attempting to delete a cluster during disaster recovery or cluster reset, the deletion might fail due to the corresponding Symcloud Storage volumes not having been cleaned up. To resolve this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Virtual machine management can fail after a node has been powered down for an extended time.** If you power down your Google Distributed Cloud connected machines for an extended period of time, you might not be able to manage the virtual machines scheduled on the corresponding nodes after you power the machines back up, even though those virtual machine workloads continue to run. To resolve this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Nodes can get stuck in`Ready,SchedulingDisabled` state after applying configuration changes.** Applying or deleting the `NodeSystemConfigUpdate` or `SriovNetworkNodePolicy` resources can result in a node that's stuck in the `Ready, Scheduling Disabled` state after it reboots. To resolve this issue, see [Troubleshoot Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/troubleshooting).

  * **The Kubernetes API server might return 404 errors when attempting to access`virt-api` endpoints.** To work around this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **Changes required to`VMRuntime` resource before upgrading to Google Distributed Cloud connected version 1.7.0.** To ensure your existing virtual machine workloads successfully upgrade to Google Distributed Cloud connected version 1.7.0, you must modify the `VMRuntime` resource before upgrading the cluster as described in [Upgrade existing virtual machines to Google Distributed Cloud connected version 1.7.0](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/virtual-machines#grace-period).

  * **The`containerd` daemon state might not be reset after deleting a cluster.** In very rare situations, cluster deletion does not reset the state of the `containerd` daemon. To resolve this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

  * **GKE Identity Service (GKE IS) Pods stuck in`Failed` state after machine reboot.** Rebooting a machine might spawn one or more GKE IS (formerly branded as Anthos IS) Pods stuck in a `Failed` state, even though the GKE IS deployment is healthy and running. This does not impact the cluster nor the GKE IS functionality. Since GKE IS Pods are deployed into a protected namespace, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support) to resolve this issue. 

  * **Cluster software upgrades might fail.** If there are GKE IS pods stuck in a `Failed` state after a machine reboot, you might experience the following behavior on the affected cluster: 

    * Automatic software upgrades never start.
    * Manually initiated software upgrades stall and enter a `Paused` state.

Workloads on the cluster continue to run and the cluster remains healthy. To resolve this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).




## March 14, 2024

1.6.1

Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

  * CVE-2023-51043, CVE-2023-51042, CVE-2024-0775, CVE-2023-6531, CVE-2023-42752, CVE-2023-44466, CVE-2023-42756, CVE-2023-5197, CVE-2023-4569, CVE-2023-4128, CVE-2023-4147, CVE-2023-4194, CVE-2023-39194, CVE-2023-39189, CVE-2023-42753, CVE-2023-4921, CVE-2023-2163, CVE-2023-3611, CVE-2023-3610, CVE-2023-4004.



The following changes have been introduced in this release of Google Distributed Cloud connected:

  * **Cloud control plane clusters can no longer be created in subsequent releases of Distributed Cloud Edge.** Distributed Cloud Edge version 1.6.1 is the last release of Distributed Cloud Edge in which you can create Cloud control plane clusters. Creation of cloud control plane clusters will be disabled in the next minor release of Distributed Cloud Edge. Existing cloud control plane clusters will continue to run workloads.

  * **Release channel requirement for specifying cluster software versions.** If you want to specify a Distributed Cloud Edge software version when creating a cluster, you must now set the cluster's release channel to `NONE`. If you do not specify a release channel or explicitly set it to `REGULAR`, the cluster automatically upgrades to the latest version of Distributed Cloud Edge software and specifying a software version is not possible.




The following new features have been introduced in this release of Google Distributed Cloud connected:

  * **Multi-rack deployments.** Distributed Cloud Edge now supports aggregating the resources of multiple Distributed Cloud Edge Racks into a single zone. You can now create clusters that span nodes across multiple Distributed Cloud Edge Racks. A single multi-rack deployment supports one Distributed Cloud Edge Base Rack and up to 10 Distributed Cloud Edge Standalone Racks. For more information, see [How Distributed Cloud Edge works](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/how-it-works).

  * **Distributed Cloud Edge Base Rack.** We are now shipping a new form factor of Distributed Cloud Edge Rack hardware, the Distributed Cloud Edge Base Rack. This form factor is a pair of existing Distributed Cloud Edge Standalone Rack hardware with the addition of four network switches that aggregate network traffic from up to 10 Distributed Cloud Edge Standalone Racks.

  * **Prometheus integration.** You can now use the Prometheus metrics solution to collect Distributed Cloud Edge metrics and workload metrics on local control plane clusters running in survivability mode. For more information, see [Collect metrics with Prometheus](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/logs-metrics#collecting_workload_metrics_with_prometheus).

  * **Node labels.** You can now assign unique labels to individual nodes when creating a node pool. For more information, see [Create a node pool](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/nodepools#create).




This is a patch release of Google Distributed Cloud connected (version 1.6.1).

This release of Google Distributed Cloud connected contains the following known issues:

  * **Nodes can get stuck in`Ready,SchedulingDisabled` state after applying configuration changes.** Applying or deleting the `NodeSystemConfigUpdate` or `SriovNetworkNodePolicy` resources can result in a node that's stuck in the `Ready, Scheduling Disabled` state after it reboots. To resolve this issue, see [Troubleshoot Distributed Cloud Edge](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/troubleshooting).

  * **Deleting clusters and node pools fails when a node is not ready.** If a node in a cluster or node pool that you want to delete is in the `NotReady` state, the deletion can fail. Contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support) to remedy this condition.

  * **Nodes using Symcloud Storage report the file system as read-only after reboot.** When multiple nodes that use Symcloud Storage reboot at once in a cluster, they can incorrectly mark the file system as read-only. Contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support) to remedy this condition.




## December 19, 2023

1.6.0

The following new features have been introduced in this release of Distributed Cloud Edge:

  * **Distributed Cloud Edge Servers.** You can now order Distributed Cloud Edge in sets of three clustered server machines without ToR switches in addition to the existing fully configured rack offering. These three-machine clusters connect directly to your local network.

  * **Configuration 8 standalone server machines.** Distributed Cloud Edge now offers a new hardware option, the Configuration 8 standalone server machine. You can order this hardware option in sets of three. Each Configuration 8 machine offers 16 processor cores (32 vCPUs), 64GB of RAM, and 1.6TB of SSD storage. The machine is housed in a half-depth 1U rackmount chassis.

  * **Symcloud Storage support for virtual machine workloads.** Distributed Cloud Edge now supports configuring virtual machine workloads with Symcloud Storage.

  * **Locally cached system images.** Distributed Cloud Edge clusters can now access system images while disconnected from Google Cloud. This allows Pods to transfer onto another node using locally cached system images.

  * **Manage clusters using the`kubectl` tool while disconnected from Google Cloud.** You can now contact Google Cloud support to request emergency credentials to authenticate to a Distributed Cloud Edge cluster and manage it using the `kubectl` command-line tool from your local network while disconnected from Google Cloud.




This is a minor release of Google Distributed Cloud Edge (version 1.6.0).

The following changes have been introduced in this release of Distributed Cloud Edge:

  * **Reduced outbound network traffic.** Distributed Cloud Edge has reduced the amount of outbound data it sends to Google Cloud. For a typical 3-machine deployment, outbound traffic bandwidth is now below 4Mbps.

  * **Nodes can now rejoin clusters after rebooting while disconnected from Google Cloud.** When creating a local control plane cluster, you can now configure it so that when a node reboots while your Distributed Cloud Edge deployment is disconnected from Google Cloud, the node rejoins its cluster after the reboot is complete and resumes running its designated workloads. For more information, see [Create a cluster](https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/clusters#create). This is a preview-level feature.




## November 03, 2023

1.5.1

This is a patch release of Google Distributed Cloud Edge (version 1.5.1).

The following issues have been resolved in this release of Distributed Cloud Edge:

  * **CVE-2022-40982 "Downfall" remediation.** The CVE-2022-40982 vulnerability, also known as "Downfall," has been patched.



The following changes have been introduced in this release of Distributed Cloud Edge:

  * **Cluster software version upgrades for local control plane clusters.** You can now trigger a software version upgrade on a local control plane cluster to a specific version of Distributed Cloud Edge software, starting with version 1.5.1. This feature is not available for Cloud control plane clusters. For instructions, see [Upgrade the software version on a local control plane cluster](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters#upgrade_the_software_version_of_a_local_control_plane_cluster).

  * **Cluster software version pinning for local control plane clusters.** You can now pin a local control plane cluster to a specific version of Distributed Cloud Edge software, starting with version 1.5.0. A cluster pinned to a specific version does not automatically upgrade when new Distributed Cloud Software becomes available. This feature is not available for Cloud control plane clusters. For instructions, see [Create a cluster](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters#create).

  * **Cluster status.** The `gcloud edge-cloud container describe` command now returns the operational status of a Distributed Cloud Edge cluster.




This release of Distributed Cloud Edge contains the following known issues:

  * **Cloud SDK version 450.0.0 or later is required.** You must upgrade your Cloud SDK to version 450.0.0 or later to create local control plane clusters with Distributed Cloud Edge software version 1.5.0. Otherwise, creating such clusters will fail.

  * **Node and machine labels are not applied when upgrading to Distributed Cloud Edge version 1.5.1.** When upgrading to Distributed Cloud Edge version 1.5.1, system-required labels might not be applied to nodes and machines within existing node pools. To work around this issue, either modify the affected node pool to update its corresponding resource definition, or delete and re-add the affected nodes. For instructions, see [Create and manage node pools](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/nodepools).




## September 07, 2023

1.5.0

This is a minor release of Google Distributed Cloud Edge (version 1.5.0).

This release of Distributed Cloud Edge contains the following known issues:

  * When creating a local control plane cluster, Distributed Cloud Edge instantiates dummy `BGPPeer` and `BGPLoadBalancer` resources. You can ignore these resources.

  * Distributed Cloud Edge does not support BGP peering to multiple VLANs within the same virtual router. You must set up a separate virtual router with a unique loopback IP addresses for each affected VLAN to allow concurrent BGP peering sessions.




The following issues have been resolved in this release of Distributed Cloud Edge:

  * When creating a Cloud control plane cluster, creating a node pool that includes nodes that were previously part of a local control plane cluster no longer fails.

  * BGP sessions now properly recover when the associated network interface goes down and then comes back up.




The following changes have been introduced in this release of Distributed Cloud Edge:

  * **Survivability mode is now generally available**. For more information, see [Distributed Cloud Edge survivability mode](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/availability#survivability-mode). After your Distributed Cloud Edge deployment has been upgraded from version 1.4.0 to version 1.5.0, you must manually delete and recreate all local control plane clusters you have created with Distributed Cloud Edge version 1.4.0 or 1.4.1. Otherwise, unexpected behavior and data loss can occur. Clusters configured to use a cloud control plane continue to run normally after upgrading Distributed Cloud Edge to version 1.5.0.

  * **Symcloud Storage integration is now generally available**. For more information, see [Configure Distributed Cloud Edge for Symcloud Storage](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/storage).

  * **Local control plane clusters now support virtual machines and GPU workloads**. For more information, see [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/virtual-machines) and [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/gpu).

  * **Loadable SCTP kernel modules**. Distributed Cloud Edge now configures the sctp kernel module as loadable. This allows you to load custom networking stacks into the kernel's user space. For more information, see [SCTP kernel modules](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking#sctp_kernel_module_support). This is a preview-level feature.




The following features have been introduced in this release of Distributed Cloud Edge:

  * **Bastion host support**. Distributed Cloud Edge now allows you to set up one or more bastion host virtual machines. The bastion host feature allows Google support engineers to connect to your Distributed Cloud Edge deployment and work with you to diagnose and resolve issues. For more information, see [Configure a bastion host](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/bastion). This is a preview-level feature.

  * **Selectable cluster software versions**. You now have the option to create a cluster running a specific version of Distributed Cloud Edge software, starting with version 1.5.0. For more information, see [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters). This is a preview-level feature.

  * **Container image registry access over secondary networks**. Distributed Cloud Edge now allows you to specify the network interface in the `spec.containerRuntimeDNSConfig` field of the `NodeSystemConfigUpdate` resource. This allows you to specify a container image registry IP/domain pair for a network interface other than the primary. For more information, see [`NodeSystemConfigUpdate` resource](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#NodeSystemConfigUpdate). This is a preview-level feature.

  * **CMEK support for local control plane nodes**. You can now configure Cloud KMS integration for storage on nodes running local control planes for Distributed Cloud Edge clusters. For more information, see [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/security#cmek).




## June 30, 2023

1.4.1

The following issues have been resolved in this release of Distributed Cloud Edge:

  * Resource utilization metrics that were previously not exported to Cloud Monitoring are now exported as expected. 
  * The status of the `kube-apiserver` mirrored Pods is no longer erroneously reported as "Pending."



This is a patch release of Google Distributed Cloud Edge (version 1.4.1).

The following changes have been introduced in this release of Distributed Cloud Edge:

  * The IP addresses of local control plane endpoints are now accessible on your local network. You must ensure that your local network's security configuration prevents external access to those IP addresses.



## May 19, 2023

1.4.0

This is a minor release of Google Distributed Cloud Edge (version 1.4.0).

The following features have been introduced in this release of Distributed Cloud Edge:

  * **Survivability mode**. Distributed Cloud Edge now allows you to create clusters with the Kubernetes control plane running locally on your Distributed Cloud Edge hardware. This improves the reliability of Distributed Cloud Edge when your connection to Google Cloud is intermittent. This is a Public Preview feature. For more information, see [Distributed Cloud Edge survivability mode](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/survivability).

  * **Symcloud Storage integration**. You can now integrate Distributed Cloud Edge with [Rakuten Symcloud Storage](https://symphony.rakuten.com/insight/datasheet/symcloud-storage), a third-party storage abstraction solution that allows Pods to access local storage on different Distributed Cloud Edge nodes. This is a Public Preview feature. For more information, see [Configure Distributed Cloud Edge for Symcloud Storage](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/storage).

  * **Enhanced rNDC security**. Distributed Cloud Edge has replaced the `bond0` interface with the `gdcenet0` interface that allows you to use the physical management network interface card for your application workloads while maintaining complete separation from Distributed Cloud Edge control and management traffic. You must manually reconfigure any existing network resources that reference the `bond0` interface to use the `gdcenet0` interface. For more information, see [Upgrade CustomNetworkInterfaceConfig resources from Distributed Cloud Edge 1.3.0 to 1.4.0](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#upgrade_customnetworkinterfaceconfig_resources_from_130_to_140) and [Upgrade NetworkAttachmentDefinition resources to Distributed Cloud Edge 1.4.0](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#upgrade_networkattachmentdefinition_resources_to_140).

  * **Cloud Router reuse for VPN connections**. When creating a VPN connection, Distributed Cloud Edge now automatically reuses any Cloud Router resource it has automatically created for a VPN connection. You can also specify a custom Cloud Router resource when creating a VPN connection. Existing VPN connections are not affected. For more information, see [Manage VPN connections](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vpn-connections).




This release of Distributed Cloud Edge contains the following known issues:

  * BGP sessions do not recover when the associated network interface goes down and then comes back up.

  * In the `CustomNetworkInterfaceConfig` resource, setting the `ifname` field to `gdcenet0` while the `masterInterface` field is also set to `gdcenet0` causes the resource to not apply to the cluster.

  * When configuring a `CustomNetworkInterfaceConfig` resource, you must explicitly set the MTU size to be no greater than the MTU size of its parent network interface. Otherwise, unpredictable behavior might result.

  * If you reboot a node running a local control plane workload for a local control plane cluster, the cluster loses its GKEConnect connection to GKEHub until the node fully starts up again. The workloads deployed on the cluster continue to run.

  * If you are creating a remote control plane plane cluster, creating a node pool using nodes that were previously part of a local control plane cluster might fail. If you encounter this issue, contact Google Support for assistance.




The following issues have been resolved in this release of Distributed Cloud Edge:

  * Distributed Cloud Edge now supports dynamic IPAM for multi-networking configurations.

  * Disabling the Anthos VM Runtime virtual machine subsystem no longer removes the `network-controller-manager` container. You can now disable the subsystem without affecting Distributed Cloud Edge networking features.




The following changes have been introduced in this release of Distributed Cloud Edge:

  * The cross-project VPN connection functionality is now generally available. For more information, see [Manage cross-project VPN connections](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vpn-connections#manage_cross-project_vpn_connections).

  * The default behavior of the `gcloud edge-cloud clusters get credentials` command has changed. The command now requires the ``gke-gcloud-auth-plugin` plugin, which replaces the legacy `in-tree-auth-plugin` plugin. For more information about the `gke-gcloud-auth-plugin` plugin, see [Important changes to Kubectl authentication are coming in GKE v1.26](https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke). You have the option to revert to the legacy `in-tree-auth-plugin` plugin by setting the `USE_GKE_CLOUD_AUTH_PLUGIN` environment flag to `false`.

  * The Kubernetes control plane has been updated to version 1.25.5-gke.1001 for all clusters.

  * The Kubernetes container daemon (`containerd`) has been updated to version 1.6.6-gke.1 for remote control plane clusters and to 1.6.12-gke.0 for survivability mode clusters.

  * The Kubernetes worker node agent (`kubelet`) has been updated to version 1.24.7.gke.1700 for remote control plane clusters and 1.25.5-gke.1001 for local control plane clusters.

  * Distributed Cloud Edge now supports the ConfigSync feature of Anthos Config Management. Distributed Cloud Edge does not support any other Anthos features.




## March 27, 2023

1.3.1

The following issues have been resolved in this release of Distributed Cloud Edge:

  * Errors in the `NodeSystemConfigUpdate` custom resource definition that shipped with Distributed Cloud Edge 1.3.0 have been corrected. The outputs of the affected status fields are now accurate.



This release of Distributed Cloud Edge contains the following known issues:

  * If you have enabled the Anthos VM Runtime virtual machine subsystem, disabling it removes the `network-controller-manager` service and its container. This renders Distributed Cloud Edge networking inoperable. To prevent this, keep the Anthos VM Runtime virtual machine subsystem enabled on your Distributed Cloud Edge deployment. If the subsystem has been disabled, re-enable it by following the steps in [Enable the Anthos VM Runtime support on Distributed Cloud Edge](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/virtual-machines#enable-anthos-vm-runtime-support) to restore Distributed Cloud Edge networking to an operable state.



This is a patch release of Google Distributed Cloud Edge (version 1.3.1).

The following changes have been introduced in this release of Distributed Cloud Edge:

  * The Kubernetes control plane has been updated to version 1.24.9-gke.2500.
  * The Kubernetes container daemon (`containerd`) has been updated to version 1.6.6-gke.1.
  * The Kubernetes worker node agent (`kubelet`) has been updated to version 1.24.7-gke.5.



## February 21, 2023

1.3.0

The following changes have been introduced in this release of Distributed Cloud Edge:

  * Getting information about a Machine resource now returns the version of the Distributed Cloud Edge cluster stack.
  * You can now connect Distributed Cloud Edge clusters to a Virtual Private Cloud network in a Cloud project other than your Distributed Cloud Edge cluster project. 
  * When creating a cross-project VPN connection, you can no longer specify a VPC project service account. Distributed Cloud Edge now uses your cluster project service account.



The following new features have been introduced in this release of Google Distributed Cloud Edge:

  * Distributed Cloud Edge now exposes the Edge Network API, which allows you to configure the networking components of Distributed Cloud Edge. For more information, see [How it works](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/how-it-works#networking) and [Distributed Cloud Edge networking features](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking).



This is a minor release of Google Distributed Cloud Edge (version 1.3.0).

## January 06, 2023

1.2.2

The following changes have been introduced in this release of Distributed Cloud Edge:

  * The NVIDIA Tesla T4 GPU driver has been updated to version 515.65.01.
  * The NVIDIA Tesla T4 GPU resource name has been changed from `nvidia.com/gpu` to `nvidia.com/gpu-pod-TESLA_T4`. If you have existing GPU-based container workloads, you must manually update their configuration to use the new resource name. For more information, see [Configure a container to use GPU resources](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/gpu#configure_a_container_to_use_gpu_resources).
  * The Kubernetes worker node agent (`kubelet`) has been updated to version 1.23.5-gke.1505.



This is a patch release of Google Distributed Cloud Edge (version 1.2.2).

## November 07, 2022

1.2.0

The following changes have been introduced in this release of Google Distributed Cloud Edge:

  * Google Distributed Cloud Edge now ships with the NVIDIA Tesla T4 GPU driver version 470.63.01.
  * The Network Function operator feature of Google Distributed Cloud Edge has been updated as follows. To learn more, see [Network Function operator](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function). 
    * The `NodeSystemConfigUpdate` resource now supports additional `sysctls` fields.
    * The `NodeSystemConfigUpdate` resource now supports fields for specifying the IP address lists and domain lists of private image registries.
    * The `CustomNetworkInterfaceConfig` resource no longer supports certain previously supported fields.
    * You can now scope both safe and unsafe `sysctls` parameters to a specific Pod or namespace using the [`tuning` Container Networking Interface (CNI) plug-in](https://www.cni.dev/plugins/current/meta/tuning/).
    * Webhook-level enforcement of valid field values is now in effect.
  * The Kubernetes control plane has been updated to version 1.23.5-gke.1505.
  * The `coredns` service has been updated to version 1.8.6-gke.0.



The following new features have been introduced in this release of Google Distributed Cloud Edge:

  * **Anthos VM Runtime replaces Kubevirt in Google Distributed Cloud Edge starting with this release.** To continue using your existing virtual machines, you must shut them down and back them up before your Distributed Cloud Edge deployment is upgraded to release 1.2.0, and then re-create them as described in [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/virtual-machines).
  * A new Google Distributed Cloud Edge hardware configuration is available. This new configuration supports GPU-based workloads that run on NVIDIA Tesla T4 GPUs in both containers and virtual machines. To order a GPU-enabled configuration, see [Order Google Distributed Cloud Edge](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/order). To learn more about running workloads on GPUs, see [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/gpu).
  * Google Distributed Cloud Edge now supports the following networking features: 
    * (Preview) Cross-project VPN Connections. To learn more, see [Manage cross-project VPN Connections](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/vpn-connections#manage_cross-project_vpn_connections).
    * (Preview) MacVLAN driver support for creating secondary network interfaces for Pods running containerized workloads. The MacVLAN driver is not supported on Pods running virtual machines. To learn more, see [Configure a secondary network interface on a Pod using the MacVLAN driver](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#configure_a_secondary_interface_on_a_pod_using_the_macvlan_driver). 
    * (Preview) Multi-network support for creating secondary network interfaces for Pods. To learn more, see [Configure a secondary network interface on a Pod using Distributed Cloud Edge multi-networking](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/network-function#configure_a_secondary_interface_on_a_pod_using_multi-networking).
    * (Preview) `ClusterDNS` resource. To learn more, see [ClusterDNS resource](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking#clusterdns_resource).



This is a minor release of Google Distributed Cloud Edge (version 1.2.0).

The following issues have been resolved in this release of Google Distributed Cloud Edge:

  * Google Distributed Cloud Edge nodes no longer become temporarily unresponsive due to excessive memory utilization.



## September 23, 2022

1.1.2

This is a patch release of Google Distributed Cloud Edge (version 1.1.2).

The following changes have been introduced in this release of Google Distributed Cloud Edge:

  * `cgroups` has been reverted to `v1` to retain compatibility with legacy workloads.
  * The Kubernetes control plane has been updated to version 1.22.8-gke.204.
  * The Kubernetes container daemon (`containerd`) has been updated to version 1.5.13-gke.0.
  * The Kubernetes worker node agent (`kubelet`) has been updated to version 1.22.8-gke.200.



## August 26, 2022

1.1.1

The following issues have been resolved in this release of Google Distributed Cloud Edge:

  * The SR-IOV interface no longer fails to start after a Google Distributed Cloud Edge worker node has been rebooted.



This is a patch release of Google Distributed Cloud Edge (version 1.1.1).

The following changes have been introduced in this release of Google Distributed Cloud Edge:

  * Google Distributed Cloud Edge worker nodes have been updated to Kubernetes 1.22.



## July 14, 2022

1.1.0

This is a minor release of Google Distributed Cloud Edge (version 1.1.0).

The following changes have been introduced in this release of Google Distributed Cloud Edge:

  * The Kubernetes control plane has been updated to version 1.22.



This release of Distributed Cloud Edge contains the following known issues:

  * Garbage collection intermittently fails to clean up terminated Pods.



The following issues have been resolved in this release of Distributed Cloud Edge:

  * The Kubernetes control plane no longer becomes intermittently unavailable during Google Distributed Cloud Edge software updates.
  * VPN connectivity between non-Anthos gateway nodes and Google Cloud Platform now works reliably.



## May 25, 2022

1.0.2

This is a patch release of Google Distributed Cloud Edge (version 1.0.2).

The following changes have been introduced in this release of of Distributed Cloud Edge:

  * Configuring a [maintenance window](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/clusters#maintenance) now controls the scheduling of software updates for the Kubernetes control plane and Kubernetes nodes.

  * You can now deploy KubeVirt virtual machines on Distributed Cloud Edge in unmanaged namespaces with support for the [Containerized Data Importer (CDI) plug-in](https://kubevirt.io/user-guide/operations/containerized_data_importer/).




The following issues have been resolved in this release of Distributed Cloud Edge:

  * Intermittent VPN connection persistence after deletion has been resolved. You no longer need to manually check whether the VPN connection and its associated resources have been successfully deleted.

  * The `localpv-shared` Persistent Volume has been eliminated. You will no longer see this Persistent Volume on the filesystem of your Distributed Cloud Edge nodes.




This release of Distributed Cloud Edge contains the following known issues:

  * The NodePort Service is not supported. This release of Distributed Cloud Edge only supports the LoadBalancer and ClusterIP Kubernetes Services.

  * The Kubernetes control planes associated with Distributed Cloud Clusters can briefly go down during Distributed Cloud Cluster software updates.

  * A large number of webhook calls might cause the Konnectivity proxy to temporarily fail.

  * The metrics agents running on Distributed Cloud Edge nodes can accumulate a backlog of events and stall, preventing the capture of further metrics.




## March 30, 2022

1.0

This is the General Availability release of Google Distributed Cloud Edge (version 1.0.0).

For information about the latest known issues, see [Known issues in this release of Distributed Cloud Edge](https://docs.cloud.google.com/distributed-cloud-edge/docs/overview#issues).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
