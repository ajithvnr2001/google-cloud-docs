---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes/
title: Google Distributed Cloud (software only) for bare metal combined release notes (all minor versions) \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:39.863514+00:00
---

# Google Distributed Cloud (software only) for bare metal combined release notes (all minor versions)  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Google Distributed Cloud (software only) for bare metal combined release notes (all minor versions) Stay organized with collections  Save and categorize content based on your preferences. 

This document lists production updates to Google Distributed Cloud (software only) for bare metal (formerly known as Google Distributed Cloud Virtual, previously known as Anthos clusters on bare metal). Check this page periodically for any new announcements.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/anthos-bare-metal-release-notes.xml) directly. 

## October 22, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.1000-gke.111 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.1000-gke.111 runs on Kubernetes v1.34.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.34

Feature

The following features were introduced in 1.34.1000-gke.111:

  * Fixed an issue in clusters using bundled BGP load balancing where control plane upgrades or configuration updates could cause up to 20 seconds of API server connection failures while a control plane node restarted. After the fix, failover to a healthy control plane node completes in approximately 4 seconds. 
  * Fixed an issue where the `NodePool` controller prematurely updated `Status.ManagedFields` on partial reconciliation failures, causing removed taints and labels to remain stranded on affected nodes. 



1.34

Fixed

The following issues were fixed in 1.34.1000-gke.111:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed `BareMetalMachine` conditions during maintenance mode transitions. 
  * Fixed an issue where updating control plane configurations caused multiple API servers to restart simultaneously, leading to transient control plane unavailability. 



## October 21, 2026

1.36

Announcement

Google Distributed Cloud (software only) for bare metal 1.36.200-gke.118 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.36.200-gke.118 runs on Kubernetes v1.36.4-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.36

Feature

The following changes were added in 1.36.200-gke.118:

  * Fixed an issue in clusters using bundled BGP load balancing where control plane upgrades or configuration updates could cause up to 20 seconds of API server connection failures while a control plane node restarted. After the fix, failover to a healthy control plane node completes in approximately 4 seconds. 
  * Fixed an issue where node drain in maintenance mode did not wait for attached storage volumes to detach. 



1.36

Fixed

The following issues were fixed in 1.36.200-gke.118:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed `BareMetalMachine` conditions during maintenance mode transitions. 



## October 13, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.600-gke.141 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.600-gke.141 runs on Kubernetes v1.35.8-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.35

Fixed

The following issues were fixed in 1.35.600-gke.141:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## October 12, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.600-gke.140 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.600-gke.140 runs on Kubernetes v1.35.8-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.35

Fixed

The following issues were fixed in 1.35.600-gke.140:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Improved `containerd` resilience against state corruption if a node reboots while unpacking container images. 
  * Fixed an issue where the periodic configuration drift health check failed with a `version not supported` error while a cluster upgrade or rollback was in progress. 
  * Fixed an issue where `audit-proxy` retried audit log exports indefinitely on permanent errors, generating excessive audit logging traffic. 
  * Fixed an issue where the Kubernetes preflight health check scanned all namespaces in the admin cluster instead of the target cluster's namespace, causing cluster upgrades to fail if an unrelated cluster had stale reconciling resources. 
  * Fixed an issue where upgrading or recreating a node during maintenance mode could proceed before storage volumes finished detaching, resulting in orphaned CSI `VolumeAttachment` resources or I/O errors. After the fix, node drain verifies that `kubelet` unmounts all host volumes and that CSI `VolumeAttachment` resources detach before completing the drain. 
  * Fixed an issue where Certificate Authority (CA) rotation failed for self-managing clusters (admin, hybrid, and standalone). The failure occurs during the final phase of the rotation when attempting to move management resources back from the temporary bootstrap cluster to the self-managing cluster, which can leave the cluster in an unmanageable state. You must upgrade your clusters to version 1.35.600-gke.140 before you rotate your CAs. 
  * Fixed an issue where `BareMetalMachine` status conditions prematurely reported nodes as ready and available during maintenance mode transitions. 
  * Fixed an issue in clusters using bundled BGP load balancing where control plane upgrades or configuration updates could cause up to 20 seconds of API server connection failures while a control plane node restarted. After the fix, failover to a healthy control plane node completes in approximately 4 seconds. 
  * Fixed an issue where user clusters repeatedly alternated between `reconciling` and `running` states if the management cluster configured a different pod density configuration than the user cluster. 



## October 07, 2026

1.36

Announcement

Google Distributed Cloud (software only) for bare metal 1.36.100-gke.144 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.36.100-gke.144 runs on Kubernetes v1.36.4-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.36

Feature

The following changes were added in 1.36.100-gke.144:

  * Extended the validity period for new certificates generated for GKE Identity Service from 5 years to 10 years. 
  * Fixed an issue in clusters using bundled BGP load balancing where control plane upgrades or configuration updates could cause up to 20 seconds of API server connection failures while a control plane node restarted. After the fix, failover to a healthy control plane node completes in approximately 4 seconds. 
  * Fixed an issue where node drain in maintenance mode did not wait for attached storage volumes to detach. 
  * Added support in `bgpadvertiser` for advertising IPv6 addresses in addition to IPv4 addresses for bundled BGP control plane load balancing. 



1.36

Fixed

The following issues were fixed in 1.36.100-gke.144:

  * Link to [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) for the list of security vulnerabilities addressed in this release.
  * Fixed an issue where user clusters repeatedly alternated between `reconciling` and `running` states if the management cluster had a different pod density configuration than the user cluster. 
  * Updated `etcd` to `v3.5.33-0-gke.3` to address security vulnerabilities CVE-2026-46595 and CVE-2026-39821. 
  * Fixed an issue where updating control plane configurations could cause transient Kubernetes API server downtime. After the fix, the update process strictly verifies that each API server is healthy before restarting subsequent control plane nodes. 
  * Fixed an issue where deleting a cluster could stall indefinitely in the `terminating` state due to orphaned machine resources. 
  * Fixed an issue where worker node pool creation could stall during provisioning in environments with strict network firewall policies. The node pool controller no longer waits for all inventory machines to be ready before declaring the node pool, eliminating a provisioning deadlock. 
  * Fixed an issue where `BareMetalMachine` status conditions prematurely reported nodes as ready and available during maintenance mode transitions. 



## September 23, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.500-gke.142 is available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.500-gke.142 runs on Kubernetes v1.35.8-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.35

Fixed

The following issues were fixed in 1.35.500-gke.142:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where node drain in maintenance mode did not wait for attached storage volumes to detach. 
  * Fixed `BareMetalMachine` conditions during maintenance mode transitions. 
  * Fixed a reconciliation loop issue in `metrics-server` by checking the ConfigMap on the target cluster. 
  * Fixed an issue where the status for `Ingress` resources didn't update when using bundled ingress. 
  * Updated `etcd` to `v3.5.33-0-gke.3` to address security vulnerabilities CVE-2026-46595 and CVE-2026-39821. 
  * Fixed an issue where deleting a cluster stalled indefinitely because node pool controllers recreated machine resources during deletion. 
  * Fixed an issue where updating control plane configurations caused multiple API servers to restart simultaneously, leading to transient control plane unavailability. 
  * Fixed an issue where creating a worker node pool stalled indefinitely while waiting for node machines in the pool to become ready. 



## September 17, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.900-gke.135 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.900-gke.135 runs on Kubernetes v1.34.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.34

Fixed

The following issues were fixed in 1.34.900-gke.135:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where the status for `Ingress` resources was not updated when using bundled Ingress. 
  * Fixed an issue where user clusters repeatedly alternated between `reconciling` and `running` states if the management cluster had a different pod density configuration than the user cluster. 
  * Updated `etcd` to `v3.5.33-0-gke.3` to address security vulnerabilities CVE-2026-46595 and CVE-2026-39821. 
  * Fixed an issue where deleting a cluster could get stuck because the node pool controller attempted to recreate machine resources while cluster deletion was in progress. 



## September 15, 2026

1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.1200-gke.83 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.1200-gke.83 runs on Kubernetes v1.33.11-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.33

Fixed

The following issues were fixed in 1.33.1200-gke.83:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## August 25, 2026

1.36

Announcement

Google Distributed Cloud (software only) for bare metal 1.36.0-gke.532 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.36.0-gke.532 runs on Kubernetes v1.36.0-gke.2800.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.36

Feature

Google Distributed Cloud (software only) for bare metal includes the following feature enhancements:

  * Upgraded the Ansible version to 2.18. This version requires Python 3.8+ on target nodes. Because RHEL 8 defaults to Python 3.6, you must have Python 3.9 installed on nodes using RHEL 8.10. RHEL 8.8 is no longer supported. 
  * Updated the Kubernetes version to 1.36. 
  * Upgraded containerd from 2.1 to 2.2 
  * Containerd is required for new cluster installations and cluster migrations to Node Agent mode.
  * Added support for the layer 4 gateway controller. 
  * `bmctl backup cluster` in Node Agent mode requires at least 12 GB of free space in `/tmp` on the admin workstation and all target nodes to buffer backup archives. You can configure a custom temporary directory by setting `TMPDIR`. 
  * If you use Node Agent and receive an error that creating the backup fails to create an archive file, you might need 12 GBs of free space in the `/tmp` directory on the admin node and all target nodes. For more information, see [Can't create a backup for a Node Agent node ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore#cant-create-na-backup%7D). 
  * Removed the deprecated `anthos-metadata-agent` component that `kubestore-collector` replaced. 
  * Removed the deprecated `csi-snapshot-validation-webhook` component. Upstream Kubernetes validation is now handled natively via Common Expression Language (CEL) rules within the deployed Custom Resource Definitions (CRDs). For more information, see [Volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots). 
  * Vertical pod autoscaling is generally available. For more information, see [Configure vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/verticalpodautoscale)
  * Unified registry mirror and private registry update behavior across all cluster types while preserving configurations. 



1.36

Fixed

The following issues were fixed in 1.36.0-gke.532:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where CA certificate secrets with identical names across different namespaces stalled cluster upgrades. In this release, the system automatically prepends the target namespace prefix to all the CA certificate secret names when forwarding them to the destination namespace. The prefix makes sure each CA certificate secret name is unique so the upgrade doesn't stall. 
  * Fixed an issue where Certificate Authority (CA) rotation failed for self-managing clusters (admin, hybrid, and standalone). The failure occurs during the final phase of the rotation when attempting to move management resources back from the temporary bootstrap cluster to the self-managing cluster, which can leave the cluster in an unmanageable state. You must upgrade your clusters to version 1.33.1000-gke.59 before you rotate your CAs. 
  * Fixed an issue where the status for `Ingress` resources didn't update when using bundled ingress. 
  * Fixed an issue where rolling back a node pool failed because stale Cluster API (CAPI) bootstrap secrets retained deprecated `kubelet` flags. 
  * Updated `cluster-proportional-autoscaler` to address security vulnerabilities. 
  * Fixed an issue where `etcd-events` installation entered an infinite retry loop during machine initialization due to incomplete cleanup of the data directory after a learner promotion failure. 
  * Fixed an issue where the `NodePool` controller prematurely updated `Status.ManagedFields` on partial reconciliation failures, causing removed taints and labels to remain stranded on affected nodes. 
  * Fixed an issue where recreating a user cluster using a previously used name caused cluster provisioning to stall indefinitely in the `PROVISIONING` state because of a missing `k8s-health-check` Service account. 
  * Fixed an issue where restarting `kube-apiserver` during etcd encryption updates abruptly terminates the container, causing stale service endpoints and transient connection failures for in-cluster workloads. 
  * Fixed an issue where the installer stalled for three minutes per control plane node during certificate rotation or etcd encryption updates because of an incorrect `kube-apiserver` container termination check. 



## August 19, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.800-gke.90 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.800-gke.90 runs on Kubernetes v1.34.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.34

Fixed

The following issues were fixed in 1.34.800-gke.90:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Removed `csi-snapshot-validation-webhook`, the [Snapshot validation webhook](https://kubernetes-csi.github.io/docs/snapshot-validation-webhook.html#description) component.



## August 11, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.400-gke.81 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.400-gke.81 runs on Kubernetes v1.35.3-gke.400.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.35

Fixed

The following issues were fixed in 1.35.400-gke.81:

  * Link to [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) for the list of security vulnerabilities addressed in this release.



## August 04, 2026

1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.1100-gke.72 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.1100-gke.72 runs on Kubernetes v1.33.11-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.33

Feature

The following changes were added in 1.33.1100-gke.72:

  * Removed the deprecated `csi-snapshot-validation-webhook` component. Upstream Kubernetes validation is now handled natively via Common Expression Language (CEL) rules within the deployed Custom Resource Definitions (CRDs). For more information, see [Volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots). 



1.33

Fixed

The following issues were fixed in 1.33.1100-gke.72:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## July 24, 2026

1.32

Fixed

A release note published on [May 6, 2025](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes#May_06_2025) stated that each Keepalived instance virtual router redundancy protocol (VRRP) configuration is configured with a `nopreempt` flag to avoid elections when a non-master instance is restarted.

The `nopreempt` flag was removed in release 1.32.200 and later. For more information, see [Control plane VIP isn't moved when HAProxy is unavailable](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#keepalived-config-issue).

## July 22, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.700-gke.93 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.700-gke.93 runs on Kubernetes v1.34.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.34

Feature

The following change was added in 1.34.700-gke.93:

  * Removed the deprecated `csi-snapshot-validation-webhook` component. Upstream Kubernetes validation is now handled natively via Common Expression Language (CEL) rules within the deployed Custom Resource Definitions (CRDs). For more information, see [Volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots). 



1.34

Fixed

The following issues were fixed in 1.34.700-gke.93:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## July 20, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.300-gke.87 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.300-gke.87 runs on Kubernetes v1.35.3-gke.400.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.35

Feature

The following change was added in 1.35.300-gke.87:

  * Removed the deprecated `csi-snapshot-validation-webhook` component. Upstream Kubernetes validation is now handled natively via Common Expression Language (CEL) rules within the deployed Custom Resource Definitions (CRDs). For more information, see [Volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots). 



1.35

Fixed

The following issues were fixed in 1.35.300-gke.87:

  * Link to [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) for the list of security vulnerabilities addressed in this release.



## July 10, 2026

1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.1000-gke.59 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.1000-gke.59 runs on Kubernetes v1.33.11-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the listing of our previously-qualified [storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

1.33

Fixed

The following issues were fixed in 1.33.1000-gke.59:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where Certificate Authority (CA) rotation failed for self-managing clusters (admin, hybrid, and standalone). The failure occurs during the final phase of the rotation when attempting to move management resources back from the temporary bootstrap cluster to the self-managing cluster, which can leave the cluster in an unmanageable state. You must upgrade your clusters to version 1.33.1000-gke.59 before you rotate your CAs. 



## June 24, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.600-gke.53 is available. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Runs on Kubernetes v1.34.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.34

Fixed

The following issues were fixed in 1.34.600-gke.53:

  * Link to [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) for the list of security vulnerabilities addressed in this release.
  * Fixed an issue where Certificate Authority (CA) rotation failed for self-managing clusters (admin, hybrid, and standalone). The failure occurs during the final phase of the rotation when attempting to move management resources back from the temporary bootstrap cluster to the self-managing cluster, which can leave the cluster in an unmanageable state. You must upgrade your clusters to version 1.34.600-gke.53 before you rotate your CAs. Running a CA rotation on self-managing clusters in versions prior to 1.34.600-gke.53 triggers this issue and can disrupt your ability to manage the cluster. 
  * Fixed an issue where a transient or partial failure during node pool updates could cause node taints or labels to become permanently stuck (stranded) on worker nodes, even after you removed them from the NodePool custom resource specification. 



## June 16, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.200-gke.66 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.200-gke.66 runs on Kubernetes v1.35.3-gke.400.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.35

Fixed

The following issues were fixed in 1.35.200-gke.66:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where a transient or partial failure during node pool updates could cause node taints or labels to become permanently stuck (stranded) on worker nodes, even after you removed them from the NodePool custom resource specification. 
  * Fixed an issue where, during the machine initialization phase, the `etcd-events` pod read the stale data directory when it started and attempted to reuse the old member ID to rejoin the cluster instead of the new one. Trying to use the old member ID to rejoin the cluster resulted in an infinite retry loop and caused the cluster to reject the connection. The fix ensures the `/var/lib/etcd-events` directory is cleared upon failure, and adds retry logic to `kubeadm-reset` to improve resiliency against transient API errors. 
  * Fixed an issue where, when enabling or updating etcd encryption, the API server was terminated abruptly, causing transient connection timeouts or failures for in-cluster workloads for up to five minutes. 
  * Fixed an issue where, during control plane certificate rotation or etcd encryption updates, the installer stalled for three minutes per control plane node while waiting for the local API server to restart, causing nodes to temporarily report an Unknown status and triggering transient routing disruptions (such as 503 Service Unavailable or ImagePullBackOff errors) for workloads scheduled on those nodes.



## June 05, 2026

1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.900-gke.90 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.900-gke.90 runs on Kubernetes v1.33.11-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.33

Fixed

The following issues were fixed in 1.33.900-gke.90:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where a transient or partial failure during node pool updates could cause node taints or labels to become permanently stuck (stranded) on worker nodes, even after you removed them from the NodePool custom resource specification. 
  * Fixed an issue where, if a new control plane node failed to join a cluster during bootstrapping or scaling (associated with installer Ansible runner job failures), orphaned etcd memberships were not cleaned up, causing the existing control plane's API server to restart repeatedly (flap) and blocking subsequent retry attempts. 
  * Fixed an issue where, during control plane certificate rotation or etcd encryption updates, the installer stalled for three minutes per control plane node while waiting for the local API server to restart, causing nodes to temporarily report an Unknown status and triggering transient routing disruptions (such as 503 Service Unavailable or ImagePullBackOff errors) for workloads scheduled on those nodes. 
  * Fixed an issue where, when enabling or updating etcd encryption, the API server was terminated abruptly, causing transient connection timeouts or failures for in-cluster workloads for up to five minutes. 
  * Fixed an issue where, when recreating a user cluster with a previously used name (which commonly occurs during Terraform deployments or manual reinstalls), cluster provisioning stalled indefinitely in the provisioning state due to a missing k8s-health-check service account. The installer ensures that the service account is created, eliminating the need to manually create the service account as a workaround.



## May 27, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.500-gke.108 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.500-gke.108 runs on Kubernetes v1.34.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.34

Fixed

The following issues were fixed in 1.34.500-gke.108:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where, if a new control plane node failed to join a cluster during bootstrapping or scaling (associated with installer Ansible runner job failures), orphaned etcd memberships were not cleaned up, causing the existing control plane's API server to restart repeatedly (flap) and blocking subsequent retry attempts. 
  * Fixed an issue where, during control plane certificate rotation or etcd encryption updates, the installer stalled for three minutes per control plane node while waiting for the local API server to restart, causing nodes to temporarily report an Unknown status and triggering transient routing disruptions (such as 503 Service Unavailable or ImagePullBackOff errors) for workloads scheduled on those nodes. 
  * Fixed an issue where, when enabling or updating etcd encryption, the API server was terminated abruptly, causing transient connection timeouts or failures for in-cluster workloads for up to five minutes. 
  * Fixed an issue where, when recreating a user cluster with a previously used name (which commonly occurs during Terraform deployments or manual reinstalls), cluster provisioning stalled indefinitely in the provisioning state due to a missing k8s-health-check service account. The installer ensures that the service account is created, eliminating the need to manually create the service account as a workaround.



## May 21, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.100-gke.72 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.100-gke.72 runs on Kubernetes v1.35.3-gke.400.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.35

Fixed

The following issues were fixed in 1.35.100-gke.72:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## May 19, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.100-gke.72 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.100-gke.72 runs on Kubernetes v1.35.3-gke.400.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.35

Fixed

The following issues were fixed in 1.35.100-gke.72:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## May 18, 2026

1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.800-gke.75 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.800-gke.75 runs on Kubernetes v1.33.11-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.33

Fixed

The following issues were fixed in 1.33.800-gke.75:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## May 11, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.400-gke.88 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.400-gke.88 runs on Kubernetes v1.34.6-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.34

Announcement

The following features were added in 1.34.400-gke.88:

  * Added a periodic health check to detect stale mounts of Secrets and ConfigMaps on pods. This helps identify rare scenarios where nodes serve outdated secret data after a rotation, which can lead to authentication failures. Currently enabled for GKE Identity Service pods, the check runs on each node and compares the locally cached volume content with the live data from the API server, reporting a mismatch only after a 5-minute grace period to allow for normal update delays.



1.34

Fixed

The following issues were fixed in 1.34.400-gke.88:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where, during the machine initialization phase, the `etcd-events` pod read the stale data directory when it started and attempted to reuse the old member ID to rejoin the cluster instead of the new one. Trying to use the old member ID to rejoin the cluster resulted in an infinite retry loop and caused the cluster to reject the connection. The fix ensures the `/var/lib/etcd-events` directory is cleared upon failure, and adds retry logic to `kubeadm-reset` to improve resiliency against transient API errors. 
  * Fixed an issue where concurrent tasks on the same node failed when `containerd` restarts. After the fix, tasks are locked and run sequentially to ensure each task completes successfully before the next begins. Each lock is held for up to 20 minutes or until the task reaches success or failure. To bypass this safety mechanism, you can run tasks concurrently by adding `baremetal.cluster.gke.io/concurrent-machine-update: "true"` to your cluster. 
  * Fixed an issue where node upgrades could hang indefinitely and bypass the 20-minute maintenance timeout. This issue occurred when a node contained completed pods within a namespace that was in a `Terminating` state. Because the Kubernetes Eviction API rejects operations in terminating namespaces, the cluster controller entered an infinite retry loop. The fix updates the drain process to skip eviction for pods in terminal phases, allowing the upgrade to proceed normally.



## May 06, 2026

1.35

Announcement

Google Distributed Cloud (software only) for bare metal 1.35.0-gke.525 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.35.0-gke.525 runs on Kubernetes v1.35.2-gke.300.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.35

Announcement

The following features were added in 1.35.0-gke.525:

  * Platform update to Kubernetes 1.35: This release updates the underlying Kubernetes version to 1.35.

This release requires the use of `cgroupsv2`. Using `cgroupsv1` is no longer supported and cluster creation or upgrades will fail. A preflight check will actively block the operation if `cgroupsv1` is detected.
    * For customers using Red Hat Enterprise Linux (RHEL) 7 or 8, which default to `cgroupsv1`, you must manually configure your operating system to enable `cgroupsv2` before upgrading. For instructions, see the Red Hat knowledge base article on [enabling cgroup v2](https://access.redhat.com/articles/3735611).
    * For more information on migrating to `cgroupsv2`, see the Kubernetes documentation on [migrating to cgroupv2](https://kubernetes.io/docs/concepts/architecture/cgroups/#migrating-cgroupv2).
    * This release upgrades the container runtime, containerd, from version 2.0 to 2.1. 
  * Added a periodic health check to detect stale secret and ConfigMap mounts on Google Kubernetes Engine pods. To account for normal propagation delays, a content mismatch is only reported as an error if the data remains stale for more than 5 minutes. 

  * Upgraded the Ansible version to 2.18. This version requires Python 3.9 on target nodes. For customers using Red Hat Enterprise Linux, version 8.10 or later is required because the default Python version in earlier Red Hat 8 releases (Python 3.6) is not supported by Ansible 2.18.

  * You can use the header section of the cluster configuration file to specify registry mirrors for your clusters. This simplifies the management of registry mirrors and provides a more consistent configuration experience. For instructions on how to update or remove these settings, see the [Registry Mirror documentation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror#header_section). 

  * **Preview** Added support for EgressDSCP tagging. With this feature, you can mark IP headers with specific Differentiated Services Code Point (DSCP) values on packets leaving the cluster to prioritize network traffic. To use this feature, you must set `preview.baremetal.cluster.gke.io/traffic-selector:` to `enable` in your cluster configuration and manage traffic selection using the `EgressDSCP` and `TrafficSelector` custom resources. For more information, see [Configure EgressDSCP tagging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-egress-dscp-tagging). 

  * `bmctl` prints the Operation ID and OperationType to the console after cluster installation and upgrade operations.




1.35

Fixed

The following issues were fixed in 1.35.0-gke.525:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where node upgrades could hang indefinitely and bypass the 20-minute maintenance timeout. This issue occurred when a node contained completed pods within a namespace that was in a `Terminating` state. Because the Kubernetes Eviction API rejects operations in terminating namespaces, the cluster controller entered an infinite retry loop. The fix updates the drain process to skip eviction for pods in terminal phases, allowing the upgrade to proceed normally. 
  * Fixed an issue where concurrent tasks on the same node failed when containerd restarts. After the fix, tasks are locked and run sequentially to ensure each task completes successfully before the next begins. Each lock is held for up to 20 minutes or until the task reaches success or failure. To bypass this safety mechanismrun and run tasks concurrently, add the following annotation to your cluster: `baremetal.cluster.gke.io/concurrent-machine-update: "true"`. 
  * Fixed an issue where Metrics API operations—including `kubectl top`, Horizontal Pod Autoscaling, and Vertical Pod Autoscaling could fail with TLS verification errors during certificate authority rotation. This occurred because the leaf certificate was not immediately renewed when the certificate authority was rotated, causing a temporary mismatch between the trusted certificate authority bundle and the certificate presented by the metrics server.
  * Fixed an issue where Cluster CA rotation could hang indefinitely on self-managed clusters, with the bmctl command hanging at the "Trust CA Bundle completed in 0/X machines" stage. This occurred due to a state deadlock during the resource pivot operation (moving resources between management and bootstrap clusters). This fix resolves the deadlock, eliminating the need to manually update cluster fields or remove lock ConfigMaps to recover. 
  * Fixed an issue where temporary API server connectivity failures (such as network timeouts) caused the system to unnecessarily re-register and redeploy the GKE Connect agent. This fix prevents these temporary errors from resetting manual or system-applied customizations to the agent deployment, improving cluster stability. 
  * Fixed an issue where bmctl could fail to capture the full log for long-running operations, resulting in empty or incomplete job logs in the workspace. This occurred because a strict internal timeout stopped log streaming prematurely. The fix ensures that log streaming continues for the full duration of the operation's pod lifecycle. 
  * Fixed an issue in the monitoring component of the cluster operator where delete operations could cause the operator to crash if the resource had no annotations. The fix ensures the system properly handles resources with empty annotation maps, preventing the crash. 
  * Fixed an issue where the anet-operator could be scheduled to an unreachable node and become stuck in a Pending state, eventually causing networking to fail. This occurred due to overly permissive scheduling rules. The fix restricts scheduling to prevent the operator from running on unreachable nodes and explicitly places it on control plane nodes to ensure reliability.



## April 23, 2026

1.32

Announcement

Google Distributed Cloud (software only) for bare metal 1.32.1100-gke.84 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.1100-gke.84 runs on Kubernetes v1.32.13-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Announcement

The following features were added in 1.32.1100-gke.84:

  * Added a periodic health check to detect stale mounts of Secrets and ConfigMaps on pods. This helps identify rare scenarios where nodes serve outdated secret data after a rotation, which can lead to authentication failures. Currently enabled for GKE Identity Service pods, the check runs on each node and compares the locally cached volume content with the live data from the API server, reporting a mismatch only after a 5-minute grace period to allow for normal update delays.



1.32

Fixed

The following issues were fixed in 1.32.1100-gke.84:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where node upgrades could hang indefinitely and bypass the 20-minute maintenance timeout. This issue occurred when a node contained completed pods within a namespace that was in a `Terminating` state. Because the Kubernetes Eviction API rejects operations in terminating namespaces, the cluster controller entered an infinite retry loop. The fix updates the drain process to skip eviction for pods in terminal phases, allowing the upgrade to proceed normally. 
  * Fixed an issue where, during the machine initialization phase, the `etcd-events` pod read the stale data directory when it started and attempted to reuse the old member ID to rejoin the cluster instead of the new one. Trying to use the old member ID to rejoin the cluster resulted in an infinite retry loop and caused the cluster to reject the connection. The fix ensures the `/var/lib/etcd-events` directory is cleared upon failure, and adds retry logic to `kubeadm-reset` to improve resiliency against transient API errors. 
  * Fixed an issue where concurrent tasks on the same node failed when `containerd` restarts. After the fix, tasks are locked and run sequentially to ensure each task completes successfully before the next begins. Each lock is held for up to 20 minutes or until the task reaches success or failure. To bypass this safety mechanismrun and run tasks concurrently, add the following annotation to your cluster: `baremetal.cluster.gke.io/ concurrent-machine-update: "true"`. 
  * Fixed an issue on clusters running Kubernetes 1.31 and later where running `kubeadm-reset` during an upgrade or reset could crash and enter an infinite retry loop, blocking the operation. This occurred because the tool failed to read cluster configuration on newer Kubernetes versions.



## April 22, 2026

1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.700-gke.71 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.700-gke.71 runs on Kubernetes v1.33.5-gke.2200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.33

Announcement

The following features were added in 1.33.700-gke.71:

A health check was added to detect when secrets or config maps mounted in pods become "stale," or out-of-sync with the Kubernetes API server. This feature addresses scenarios where the Kubelet's local cache fails to update with the latest versions of configuration data. The check performs the following actions:

  * Iterates through all running pods on the node to verify their mounts.
  * Compares the local data in the Kubelet's atomic update symlink structure against the live objects and update timestamps in the API server.
  * Uses a 5-minute threshold to prevent false positives caused by normal propagation delays. A mismatch is only reported as an error if the staleness persists for more than 5 minutes.



1.33

Fixed

The following issues were fixed in 1.33.700-gke.71:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Fixed an issue where concurrent tasks on the same node failed when `containerd` restarts. After the fix, tasks are locked and run sequentially to ensure each task completes successfully before the next begins. Each lock is held for up to 20 minutes or until the task reaches success or failure. To bypass this safety mechanismrun and run tasks concurrently, add the following annotation to your cluster: `baremetal.cluster.gke.io/concurrent-machine-update: "true"`. 
  * Fixed an issue where, during the machine initialization phase, the `etcd-events` pod read the stale data directory when it started and attempted to reuse the old member ID to rejoin the cluster instead of the new one. Trying to use the old member ID to rejoin the cluster resulted in an infinite retry loop and caused the cluster to reject the connection. The fix ensures that the system clears the `/var/lib/etcd-events` directory upon failure, and adds retry logic to `kubeadm-reset` to improve resiliency against transient API errors.
  * Fixed an issue where node upgrades could hang indefinitely and bypass the 20-minute maintenance timeout. This issue occurred when a node contained completed pods within a namespace that was in a `Terminating` state. Because the Kubernetes Eviction API rejects operations in terminating namespaces, the cluster controller entered an infinite retry loop. The fix updates the drain process to skip eviction for pods in terminal phases, allowing the upgrade to proceed normally.
  * Fixed an issue where Metrics API operations—including `kubectl top`, Horizontal Pod Autoscaling, and Vertical Pod Autoscaling could fail with TLS verification errors during certificate authority rotation. This occurred because the leaf certificate was not immediately renewed when the certificate authority was rotated, causing a temporary mismatch between the trusted certificate authority bundle and the certificate presented by the metrics server.



## April 15, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.300-gke.59 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.300-gke.59 runs on Kubernetes v1.34.3-gke.400.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.34

Fixed

The following issues were fixed in 1.34.300-gke.59:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities)
  * Cluster and node pool failures are now surfaced in the `RecentFailures` field in the cluster status. This change provides a centralized location for viewing errors from both worker node pools and control plane nodes, improving the troubleshooting and debugging experience. 
  * Fixed an issue where Metrics API operations—including `kubectl top`, Horizontal Pod Autoscaling (HPA), and Vertical Pod Autoscaling (VPA)—could fail with TLS verification errors during CA rotation. 



## March 27, 2026

1.32

Fixed

The following issues were fixed in 1.32.1000-gke.57:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).
  * Cluster and node pool failures are now surfaced in the `RecentFailures` field in the cluster status. This change provides a centralized location for viewing errors from both worker node pools and control plane nodes, improving the troubleshooting and debugging experience. 
  * Fixed an issue where Metrics API operations—including `kubectl top`, Horizontal Pod Autoscaling (HPA), and Vertical Pod Autoscaling (VPA)—could fail with TLS verification errors during CA rotation. 
  * Resolved an issue where Certificate Authority (CA) rotation became stuck on self-managed clusters (admin, hybrid, or standalone). This fix resolves an internal resource synchronization error that previously prevented the rotation process from completing successfully. 



1.32

Announcement

Google Distributed Cloud (software only) for bare metal 1.32.1000-gke.57 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.1000-gke.57 runs on Kubernetes v1.32.13-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

## March 23, 2026

1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.600-gke.39 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.600-gke.39 runs on Kubernetes v1.33.5-gke.2200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.33

Fixed

The following issues were fixed in 1.33.600-gke.39:

  * Resolved an issue where Certificate Authority (CA) rotation became stuck on self-managed clusters (admin, hybrid, or standalone). This fix resolves an internal resource synchronization error that previously prevented the rotation process from completing successfully. 
  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## March 18, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.200-gke.68 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.200-gke.68 runs on Kubernetes v1.34.3-gke.400.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.34

Fixed

The following issues were fixed in 1.34.200-gke.68:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



## March 05, 2026

1.32

Fixed

The following issues were fixed in 1.32.900-gke.60:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.32

Announcement

Google Distributed Cloud (software only) for bare metal 1.32.900-gke.60 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.900-gke.60 runs on Kubernetes v1.32.11-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

## March 03, 2026

1.33

Security

The following issues were fixed in 1.33.500-gke.63:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.33

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.500-gke.63 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.500-gke.63 runs on Kubernetes v1.33.5-gke.2200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.33

Announcement

In Google Distributed Cloud (software only) for bare metal versions 1.33.0 and later, `bmctl` operations can fail to stream logs from pods to the local workspace, causing empty or incomplete logs in `bmctl-workspace/{CLUSTER NAME}/log directory`.

This issue occurred because a recent Kubernetes library upgrade introduced a required context parameter for pod log streaming. The bmctl tool was incorrectly passing a context with a 10-second timeout, causing the log streamer to terminate prematurely for pods with long lifecycles, such as Ansible runner jobs.

This issue is resolved in the following versions:

  * 1.33.500 and later
  * 1.34.100 and later
  * 1.35.0 and later



If you use an affected version and require the logs for a failed or ongoing operation, check logs using `kubectl`. If the cluster is accessible, you can manually retrieve logs directly from the relevant pods using the `kubectl logs` command.

It is recommended to upgrade to a fixed version to ensure that all `bmctl` operation logs are correctly captured in your local workspace for troubleshooting and auditing purposes

## February 13, 2026

1.34

Announcement

Google Distributed Cloud (software only) for bare metal 1.34.100-gke.93 is now available for download. To upgrade, see Upgrade clusters. Google Distributed Cloud for bare metal 1.34.100-gke.93 runs on Kubernetes v1.34.1-gke.4700.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

Feature

The following feature was added in 1.34.100-gke.93:

The `spec.taints` field in the `NodePoolClaim` resource is mutable. You can add or remove taints on existing node pools without recreating the `NodePoolClaim`. You can use this field to manage GPU nodes.

## February 05, 2026

1.32

Fixed

The following issues were fixed in 1.32.800-gke.126:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.32

Announcement

Google Distributed Cloud (software only) for bare metal 1.32.800-gke.126 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.800-gke.126 runs on Kubernetes v1.32.11-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

## February 04, 2026

Announcement

Google Distributed Cloud (software only) for bare metal 1.33.400-gke.113 is now available for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.400-gke.113 runs on Kubernetes v1.33.5-gke.1900.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

## January 30, 2026

Security

Multiple security vulnerabilities have been identified in the OpenSSL library. The most significant finding is CVE-2025-15467, a critical vulnerability that might allow for remote code execution (RCE) or denial of service (DoS) attacks via network-based vectors.

For more details, see the [GCP-2026-006 security bulletin](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2026-006-gdcbm).

## January 16, 2026

Change

Updated the [multiple network interfaces for Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/multi-nic) and [bundled load balancing with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp) features to support admin clusters for version 1.34 or higher. Admin cluster support for these features has also been added to the GKE On-Prem API, so you can specify these features with clients like [Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_admin_cluster).

## December 11, 2025

1.34

Announcement

Google Distributed Cloud for bare metal 1.34.0-gke.566 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.34.0-gke.566 runs on Kubernetes v1.34.1-gke.2900.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.34

Feature

The following features were added in 1.34.0-gke.566:

  * **Preview** : Vertical Pod autoscaling can now be configured to use your Prometheus instance as a persistent history provider for long-term CPU and memory usage data.

  * **Preview** : Added support for horizontal Pod autoscaling that uses custom metrics from your Prometheus server to scale your applications, eliminating the operational burden of manually deploying and managing the adapter, its configuration, and RBAC. The automated solution handles the entire lifecycle, making it simpler to scale applications based on the metrics that matter most to your business.

  * **Preview** : Added support for fast failover for the egress NAT gateway running in high availability. This feature improves both the reliability and throughput of egress traffic.

  * **GA** : Added support for skip minor version cluster upgrades. You can directly upgrade your cluster control plane nodes (and entire cluster if worker node pools aren't pinned at a lower version) to two minor versions above the current version. Added the [`bmctl upgrade intermediate-version`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#upgrade_intermediate-version) command to print the intermediate version for a skip minor version upgrade.

  * **Preview** : Added support for advanced networking features on admin clusters. This capability lets you specify [multiple network interfaces for Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/multi-nic) and lets you use [bundled load balancing with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp) on your version 1.34 or higher admin clusters.

This note is incorrect; see entry for [January 16, 2026](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes#January_16_2026).




1.34

Change

The following functional changes were made in 1.34.0-gke.566:

  * Enabled Ansible SSH pipelining by default to improve performance. This can be disabled by adding the annotation `preview.baremetal.cluster.gke.io/ansible-ssh-pipelining: "disable"` to the Cluster custom resource.

  * During cluster creation and update operations, NodePools validate IP address uniqueness against all existing underlay Nodes, regardless of status. Node deprovisioning is blocked until the associated Kubernetes Node is deleted, unless the `node-deletion-timeout-seconds` annotation is present on the cluster.

  * Upgraded containerd from 1.7 to 2.0.

  * Registry mirror configuration information has been migrated to the `hosts.toml` containerd config file.

  * Upgrade preflight checks now validate PodDisruptionBudgets.

  * GKE Identity Service has been migrated from a Deployment to a DaemonSet for improved reliability on control plane nodes.

  * Added support for Red Hat Enterprise Linux 9.6.

  * Removed support for Red Hat Enterprise Linux 9.2 as it is beyond the [Red Hat support window](https://access.redhat.com/support/policy/updates/errata#RHEL8_and_9_Life_Cycle).

  * Added support for the 6.14 kernel package is supported for use with Ubuntu 24.04 LTS.




1.34

Fixed

The following issues were fixed in 1.34.0-gke.566:

  * Updated the `bmctl restore` command so that it restores the Node Problem Detector systemd Service for admin clusters.

  * Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect certificates.

  * Fixed an issue where the cluster restore process leaves the Kubelet certificate files as regular files instead of symbolic links, preventing certificate rotation.




1.34

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## December 05, 2025

1.33

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.33

Fixed

The following issues were fixed in 1.33.300-gke.60:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.33

Announcement

Google Distributed Cloud for bare metal 1.33.300-gke.60 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Distributed Cloud for bare metal 1.33.300-gke.60 runs on Kubernetes v1.33.5-gke.900.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Distributed Cloud for bare metal.

## December 02, 2025

1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.32

Fixed

The following issues were fixed in 1.32.700-gke.64:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.32

Announcement

Google Distributed Cloud for bare metal 1.32.700-gke.64 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.700-gke.64 runs on Kubernetes v1.32.9-gke.700.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

## November 12, 2025

1.33

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.33

Fixed

The following issues were fixed in 1.33.200-gke.70:

  * Fixed an issue where configuring your cluster to use [Workload Identity Cluster Authentication](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/wi-cluster-auth) together with a [registry mirror](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror) caused containerd instability. To use the fix, add the `baremetal.cluster.gke.io/enable-gcr-image-credential-refresh: "false"` cluster annotation.

  * Fixed a timeout issue for the `kubeadm` API server health check that runs during bootstrap cluster creation. The timeout issue blocked some cluster operations, such as restoring a cluster.

  * This patch release doesn't include new [fixes for specific, externally-cited vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.33

Announcement

Google Distributed Cloud for bare metal 1.33.200-gke.70 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Distributed Cloud for bare metal 1.33.200-gke.70 runs on Kubernetes v1.33.-gke.900.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Distributed Cloud for bare metal.

1.31

Announcement

Google Distributed Cloud for bare metal 1.31.1100-gke.40 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Distributed Cloud for bare metal 1.31.1100-gke.40 runs on Kubernetes v1.31.12-gke.600.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Distributed Cloud for bare metal.

1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## October 29, 2025

1.32

Announcement

Google Distributed Cloud for bare metal 1.32.600-gke.53 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.600-gke.53 runs on Kubernetes v1.32.9-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.32

Fixed

The following issues were fixed in 1.32.600-gke.53:

  * Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect certificates.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




## October 15, 2025

1.31

Fixed

The following issues were fixed in 1.31.1000-gke.44:

  * Fixed an issue where the cluster restore process leaves the Kubelet certificate files as regular files instead of symbolic links, preventing certificate rotation.

  * Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect certificates.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.31

Announcement

Google Distributed Cloud for bare metal 1.31.1000-gke.44 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Distributed Cloud for bare metal 1.31.1000-gke.44 runs on Kubernetes v1.31.12-gke.600.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Distributed Cloud for bare metal.

1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## October 02, 2025

1.33

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.33

Announcement

Google Distributed Cloud for bare metal 1.33.100-gke.89 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Distributed Cloud for bare metal 1.33.100-gke.89 runs on Kubernetes v1.33.4-gke.900.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Distributed Cloud for bare metal.

1.33

Fixed

The following issues were fixed in 1.33.100-gke.89:

  * Fixed an issue where the cluster restore process leaves the Kubelet certificate files as regular files instead of symbolic links, preventing certificate rotation.

  * Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect certificates.

  * This patch release doesn't include new [fixes for specific, externally-cited vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




## September 24, 2025

1.32

Announcement

Google Distributed Cloud for bare metal 1.32.500-gke.48 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.500-gke.48 runs on Kubernetes v1.32.8-gke.500.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Fixed

The following issues were fixed in 1.32.500-gke.48:

  * Fixed an issue where the cluster restore process leaves the Kubelet certificate files as regular files instead of symbolic links, preventing certificate rotation.

  * This patch release doesn't include new [fixes for specific, externally-cited vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## September 15, 2025

1.31

Announcement

Google Distributed Cloud for bare metal 1.31.900-gke.38 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.900-gke.38 runs on Kubernetes v1.31.10-gke.300.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Fixed

The following issues were fixed in 1.31.900-gke.38:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## September 02, 2025

1.33

Announcement

Google Distributed Cloud for bare metal 1.33.0-gke.799 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.33.0-gke.799 runs on Kubernetes v1.33.2-gke.700.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.33

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.33

Feature

The following features were added in 1.33.0-gke.799:

  * **GA** : Introduced an Envoy sidecar into the GKE Identity Service to increase security, reliability, and performance.

  * **GA** : Added support for the Ubuntu 24.04 LTS operating system with Linux kernel versions, such as 6.8 and 6.11. Support for Linux kernel 6.14 is explicitly excluded.

  * **GA** : Added the ability to override the cluster-level pod density setting for individual node pools.

  * **Preview** : Added Node Agent to give you the ability to transition from using Ansible over SSH for cluster operations to a more secure, agent-based model. Added [`bmctl nodeagent`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent) commands to provide a straightforward and reliable process of migrating existing clusters to use Node Agent.

  * **Preview** : Added a bundled version of the [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html#about-the-nvidia-gpu-operator) (version 25.3.1). The bundled operator is an open-source solution for managing the NVIDIA software components needed to provision and manage GPU devices.

  * **Preview** : Added Dynamic Resource Allocation, a Kubernetes API that lets you request and share generic resources, such as GPUs, among pods and containers. When enabled, this capability helps you run AI workloads by dynamically and precisely allocating the GPU resources within your bare metal clusters, improving resource utilization and performance for demanding workloads.

  * **Preview** : Added vertical Pod autoscaling, which lets you analyze and set CPU and memory resources required by Pods. Instead of having to set up-to-date CPU requests and limits and memory requests and limits for the containers in your Pods, you can configure vertical Pod autoscaling to provide recommended values for CPU and memory requests and limits that you can use to manually update your Pods, or you can configure vertical Pod autoscaling to automatically update the values.

  * **Preview** : Added support for skip minor version cluster upgrades. You can directly upgrade your cluster control plane nodes (and entire cluster if worker node pools aren't pinned at a lower version) to two minor versions above the current version. Added the [`bmctl upgrade intermediate-version`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#upgrade_intermediate-version) to print the intermediate version for a skip minor version upgrade.

  * Surface failures from node pool status to the `RecentFailures` field in cluster status.

  * Surface failures from failed preflight checks triggered by the cluster controller to the `RecentFailures` field in cluster status.




1.33

Fixed

The following issues were fixed in 1.33.0-gke.799:

  * Fixed an issue where restoring a cluster that has a node with a GPU causes instability of pods on the nodes.

  * Fixed an issue that caused the Ansible playbook for handling Cloud Audit Logging to fail and not complete.

  * Fixed an issue that caused nodes to get stuck in maintenance mode. Health checks have been updated so that the network check job skips connectivity checks for nodes that are in maintenance mode.

  * Fixed an issue where the CronJob for periodic health checks wasn't updating after configuration changes.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.33

Change

The following functional changes were made in 1.33.0-gke.799:

  * Changed logging behavior so that kubeadm logs show up in the journald of the node machine where kubeadm runs.

  * To help prevent stale ARP cache issues, `iptables-persistent` is installed in Debian nodes.

  * Cluster manifests are deployed using a Kubernetes job, allowing the cluster operator to be more responsive to cluster events.

  * Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters. If the upgrade version information for a user cluster doesn't comply with the version skew rules, the upgrade is halted.

  * Updated health checks and upgrade preflight checks to inspect for kubeadm certificate expiration.

  * Updated etcd version to 3.5.21.

  * Removed support for Red Hat Enterprise Linux 8.8 as it is beyond the [Red Hat support window](https://access.redhat.com/support/policy/updates/errata#RHEL8_and_9_Life_Cycle).

  * Removed support for Ubuntu 20.04 LTS as it has reached the end of [standard security maintenance in May 2025](https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle).

  * Upgraded `ansible-core` to 2.16.4 to support Python 3.12.

  * Increased the RSA key size for Cluster API certifications to 4096 bits for improved security.




## August 28, 2025

1.32

Announcement

Google Distributed Cloud for bare metal 1.32.400-gke.68 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.400-gke.68 runs on Kubernetes v1.32.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Fixed

The following issues were fixed in 1.32.400-gke.68:

  * Fixed an issue that caused the Ansible playbook for handling Customer-Acquired Licenses (CAL) to fail and not complete.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## August 13, 2025

1.31

Announcement

Google Distributed Cloud for bare metal 1.31.800-gke.32 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.800-gke.32 runs on Kubernetes v1.31.10-gke.300.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Fixed

The following issues were fixed in 1.31.800-gke.32:

  * Fixed an issue where the CronJob for periodic health checks wasn't updating after configuration changes.

  * Fixed an issue that caused the Ansible playbook for handling Customer-Acquired Licenses (CAL) to fail and not complete.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## August 12, 2025

1.30 

Announcement

Google Distributed Cloud for bare metal 1.30.1200-gke.63 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.1200-gke.63 runs on Kubernetes v1.30.12-gke.1200. This is the final patch for the 1.30 minor release.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Change

The following functional change was made in 1.30.1200-gke.63:

  * Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters. If the upgrade version information for a user cluster doesn't comply with the version skew rules, the upgrade is halted.



1.30 

Fixed

The following issues were fixed in 1.30.1200-gke.63:

  * Fixed an issue where the CronJob for periodic health checks wasn't updating after configuration changes.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




## August 08, 2025

1.32

Announcement

Google Distributed Cloud for bare metal 1.32.300-gke.85 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.300-gke.85 runs on Kubernetes v1.32.4-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Change

The following functional change was made in 1.32.300-gke.85:

  * Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters. If the upgrade version information for a user cluster doesn't comply with the version skew rules, the upgrade is halted.



1.32

Fixed

The following issues were fixed in 1.32.300-gke.85:

  * Fixed a [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#keepalived-config-issue) where Keepalived failover is blocked when the corresponding HAProxy instance is unreachable. This issue prevented the control plane VIP from being made available on a new, healthy node.

  * Fixed an issue where the CronJob for periodic health checks wasn't updating after configuration changes.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 22, 2025

1.31

Announcement

Google Distributed Cloud for bare metal 1.31.700-gke.72 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.700-gke.72 runs on Kubernetes v1.31.10-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Change

The following functional changes were made in 1.31.700-gke.72:

  * Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters.



1.31

Fixed

The following issues were fixed in 1.31.700-gke.72:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 21, 2025

1.30 

Announcement

Google Distributed Cloud for bare metal 1.30.1100-gke.67 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.1100-gke.67 runs on Kubernetes v1.30.12-gke.800.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Fixed

The following issues were fixed in 1.30.1100-gke.67:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 17, 2025

1.32

Announcement

Google Distributed Cloud for bare metal 1.32.200-gke.104 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.200-gke.104 runs on Kubernetes v1.32.4-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Fixed

The following issues were fixed in 1.32.200-gke.104:

  * Fixed a [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#keepalived-config-issue) where Keepalived failover is blocked when the corresponding HAProxy instance is unreachable. This issue prevented the control plane VIP from being made available on a new, healthy node.

  * Fixed an issue that caused nodes to get stuck in maintenance mode. Health checks have been updated so that the network check job skips connectivity checks for nodes that are in maintenance mode.

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## June 23, 2025

1.31

Announcement

Google Distributed Cloud for bare metal 1.31.600-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.600-gke.85 runs on Kubernetes v1.31.8-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Fixed

The following issues were fixed in 1.31.600-gke.85:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## June 10, 2025

1.30 

Announcement

Google Distributed Cloud for bare metal 1.30.1000-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.1000-gke.85 runs on Kubernetes v1.30.12-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Fixed

The following issues were fixed in 1.30.1000-gke.85:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## June 04, 2025

1.32

Announcement

Google Distributed Cloud for bare metal 1.32.100-gke.106 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.100-gke.106 runs on Kubernetes v1.32.4-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Change

Introduced an Envoy sidecar into the GKE Identity Service to increase security, reliability, and performance.

1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## May 22, 2025

1.31

Announcement

### Release 1.31.500-gke.68

Google Distributed Cloud for bare metal 1.31.500-gke.68 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.500-gke.68 runs on Kubernetes v1.31.7-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Change

The following functional changes were made in 1.31.500-gke.68:

  * Upgraded etcd to v3.4.33-0-gke.3.



1.31

Fixed

The following issues were fixed in 1.31.500-gke.68:

  * Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).



1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## May 16, 2025

1.30 

Announcement

### Release 1.30.900-gke.57

Google Distributed Cloud for bare metal 1.30.900-gke.57 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.900-gke.57 runs on Kubernetes v1.30.11-gke.700.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Change

The following functional change was made in 1.30.900-gke.57:

  * Upgraded etcd to v3.4.33-0-gke.3.



1.30 

Fixed

The following issues are fixed in 1.30.900-gke.57:

  * Fixed an issue where network interfaces are being leaked, preventing namespace deletion. 

  * The 1.30.900-gke.57 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).




1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## May 06, 2025

1.32

Announcement

### Release 1.32.0-gke.1087

Google Distributed Cloud for bare metal 1.32.0-gke.1087 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.0-gke.1087 runs on Kubernetes v1.32.3-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.32

Announcement

Version 1.29 end of life: In accordance with the [Version Support Policy](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#version-support), version 1.29 (all patch releases) of Google Distributed Cloud for bare metal has reached its end of life and is no longer supported.

1.32

Feature

  * **GA:** Added support for new diagnosis utility for [GKE Identity Service](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/identity-manage) that provides diagnostics information related to the login flow. This makes it easier to troubleshoot login and OIDC configuration issues. For more information, see [GKE Identity Service diagnostic utility](https://cloud.google.com/kubernetes-engine/enterprise/identity/setup/anthos-v2-diagnostic-utility).

  * **GA:** For high availability control planes, Google Distributed Cloud automatically configures the Keepalived virtual router redundancy protocol (VRRP) configuration to make failover behaviour deterministic and prevent interleaving of ARP replies with different MAC addresses:

    * By default, each Keepalived instance is configured with a different `priority` value.
    * Each Keepalived instance is configured with `nopreempt` to avoid elections when a non-master instance is restarted.

The configuration in this note has been revised. See the release notes entry for [July 24, 2026](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes#July_24_2026).

  * **GA:** Added support for a new field, `controlPlane.loadBalancer.keepalivedVRRPGARPMasterRepeat`, in the cluster configuration file that maps to the `vrrp_garp_master_repeat` setting for Keepalived. This field specifies the number of gratuitous ARP (GARP) messages to send at a time after a control plane node transitions to the role of the master server. The default value is `5`.

  * **GA:** Added a new `controlPlane.loadBalancer.mode`, field for Layer 2 load balancing. This field lets you separate control plane load balancing from data plane load balancing:

    * At cluster creation, if you set `controlPlane.loadBalancer.mode` to `bundled` and `loadBalancer.nodePoolSpec` is configured, the control plane load balancer runs in the control plane node pool and the data plane load balancer runs in the load balancer node pool.
    * For an existing cluster where `controlPlane.loadBalancer.mode` isn't set and `loadBalancer.nodePoolSpec` isn't specified, both the control plane load balancer and the data plane load balancer run in the control plane node pool. You can migrate the data plane load balancer to a load balancer node pool by updating the cluster spec to specify a load balancer node pool (`loadBalancer.nodePoolSpec`) and to add `controlPlane.loadBalancer.mode` set to `bundled`.



1.32

Fixed

  * Fixed an issue that resulted in an excessive creation of periodic `kube-proxy-cleanup` jobs on cluster nodes with high pod utilization.

  * Fixed an issue that caused cluster creation to fail because kubelet restarted before required static pods are running.

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#control-plane-upgrade-failure-due-to-missing-super-admin.conf-file) where node upgrades failed due to a missing super-admin.conf file.

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#immutable-field-error-when-updating-user-clusters-with-bmctl-version-1.30.x) where the `bmctl update cluster` command fails for user clusters that were created with the `cloudOperationsServiceAccountKeyPath` setting in the header section of the cluster configuration file.

  * Fixed an issue where prompting during `bmctl update cluster` prevented use of automation. You can now use the --quiet flag to skip prompting.

  * Fixed an issue where node machines didn't update when the registry mirror hosts field was updated.




The 1.32.0-gke.1086 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.32

Change

  * Upgraded etcd to v3.4.33-0-gke.3.

  * Upgraded containerd to version 1.7.

  * Upgraded the SR-IOV operator, `sriov-network-operator`, to version 1.4.

  * Added `Compress=yes` to `/etc/systemd/journald.conf` to ensure that objects larger than 512 bytes are compressed before they are written to the file system.

  * Added new, [default periodic health checks](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/healthchecks#health-what-default) to ensure that Kubernetes cluster resources are configured correctly and functioning properly.

  * Added more namespaces to the default snapshot scenarios.

  * Added preflight check for kernel `fsnotify` settings for Red Hat Enterprise Linux (RHEL) 8.x.

  * Removed the leading timestamp from the `bmctl version` response. Temporarily, we've provided `-t` and `--timestamps` flags to revert to the old format.

  * Added a check for the `FailedCgroupRemoval` node condition to the node problem detector (NPD) to look for orphan container processes on nodes. By default, a new plugin for NPD automatically fixes this condition on the node.

  * Updated the cluster delete process to delete worker node pools prior to removing any control plane nodes. This change applies to supported cluster deletion flows, including `bmctl`, the Google Cloud CLI, and the Google Cloud console.

  * Updated the log entries in the `backup.log` file created by the `bmctl backup` command to improve readability.

  * Updated the cluster upgrade operation to keep only the three latest `kubeadm` backups of etcd and configuration information for a node. Previously, `kubeadm` kept node backups for every attempted upgrade.

  * Added the kubelet config, CPU Manager state, and Memory Manager state to node snapshots.




1.32

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## April 25, 2025

1.31

Announcement

### Release 1.31.400-gke.110

Google Distributed Cloud (software only) for VMware 1.31.400-gke.110 is now available for [download](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/downloads). To upgrade, see [Upgrade a cluster or a node pool](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/upgrading). Google Distributed Cloud 1.31.400-gke.110 runs on Kubernetes v1.31.7-gke.800.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

1.31

Change

The following functional change was made in 1.31.400-gke.110:

  * Updated the cluster upgrade operation to keep only the three latest `kubeadm` backups of etcd and configuration information for a node. Previously, `kubeadm` kept node backups for every attempted upgrade.

  * Upgraded etcd to v3.4.33-0-gke.3.




1.31

Fixed

The 1.31.400-gke.110 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.31

Fixed

The following fixes were made in 1.31.400-gke.110:

  * Fixed an issue where network interfaces were being leaked, preventing namespace deletion.

  * Fixed an issue that resulted in an excessive creation of periodic `kube-proxy-cleanup` jobs on cluster nodes with high pod utilization.

  * Fixed an issue that caused cluster creation to fail because kubelet restarted before required static pods are running.

  * Fixed an issue that allowed `bmctl reset` to run in situations where the reset resulted in the loss of quorum for control plane nodes. To run the command without enforcing the quorum, use the newly added `--bypass-quorum-check` flag.




1.31

Change

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## April 14, 2025

1.30 

Announcement

### Release 1.30.800-gke.66

Google Distributed Cloud for bare metal 1.30.800-gke.66 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.800-gke.66 runs on Kubernetes v1.30.11-gke.500.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Change

The following functional change was made in 1.30.800-gke.66:

  * Updated the cluster upgrade operation to keep only the three latest `kubeadm` backups of etcd and configuration information for a node. Previously, `kubeadm` kept node backups for every attempted upgrade.



1.30 

Fixed

The 1.30.800-gke.66 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.30 

Fixed

The following issues are fixed in 1.30.800-gke.66:

  * Fixed an issue that resulted in an excessive creation of periodic `kube-proxy-cleanup` jobs on cluster nodes with high pod utilization.

  * Fixed an issue that caused cluster creation to fail because kubelet restarted before required static pods are running.

  * Fixed an issue that allowed `bmctl reset` to run in situations where the reset resulted in the loss of quorum for control plane nodes. To run the command without enforcing the quorum, use the newly added `--bypass-quorum-check` flag.




1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## March 28, 2025

1.29

Announcement

### Release 1.29.1200-gke.98

Google Distributed Cloud for bare metal 1.29.1200-gke.98 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.1200-gke.98 runs on Kubernetes v1.29.13-gke.500. This is the final patch for the 1.29 minor release.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Change

Updated the cluster upgrade operation to keep only the three latest `kubeadm` backups of etcd and configuration information for a node. Previously, `kubeadm` kept node backups for every attempted upgrade.

1.29

Fixed

Fixed an issue that caused cluster creation to fail because kubelet restarted before required static pods are running.

1.29

Fixed

The 1.29.1200-gke.98 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.29

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## March 25, 2025

1.31

Breaking

Since release 1.30.0-gke.1930, the `featureGates.enableGMPForSystemMetrics` field in the `stackdriver` custom resource is always on and can't be disabled. It has been enabled by default since 1.16. If you've manually turned this feature off, upgrading clusters to version 1.30 means a breaking change in the format of some system metrics. For information on this feature, see [Use Google Cloud Managed Service for Prometheus for selected system components](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#using-managed-service-for-prometheus).

1.30 

Breaking

Since release 1.30.0-gke.1930, the `featureGates.enableGMPForSystemMetrics` field in the `stackdriver` custom resource is always on and can't be disabled. It has been enabled by default since 1.16. If you've manually turned this feature off, upgrading clusters to version 1.30 means a breaking change in the format of some system metrics. For information on this feature, see [Use Google Cloud Managed Service for Prometheus for selected system components](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#using-managed-service-for-prometheus).

## March 18, 2025

1.31

Announcement

### Release 1.31.300-gke.81

Google Distributed Cloud for bare metal 1.31.300-gke.81 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.300-gke.81 runs on Kubernetes v1.31.5-gke.700.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Fixed

The 1.31.300-gke.81 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

## March 13, 2025

1.30 

Announcement

### Release 1.30.700-gke.56

Google Distributed Cloud for bare metal 1.30.700-gke.56 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.700-gke.56 runs on Kubernetes v1.30.9-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Fixed

The following issue is fixed in 1.30.700-gke.56:

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#control-plane-upgrade-failure-due-to-missing-super-admin.conf-file) where node upgrades failed due to missing `super-admin.conf` file.



1.30 

Fixed

The 1.30.700-gke.56 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## March 05, 2025

1.31

Security

### Security bulletin

The Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy.

For more details, see the [GCP-2025-009 security bulletin](https://cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-009).

1.30 

Security

### Security bulletin

The Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy.

For more details, see the [GCP-2025-009 security bulletin](https://cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-009).

1.29

Security

### Security bulletin

The Envoy project recently announced several new security vulnerabilities ([CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269), [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270), and [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)) that could allow an attacker to crash Envoy.

For more details, see the [GCP-2025-009 security bulletin](https://cloud.google.com/kubernetes-engine/security-bulletins#gcp-2025-009).

## February 27, 2025

1.31

Announcement

The initial patch releases for 1.30.500, 1.30.600, and 1.31.200 contained a [known issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#control-plane-upgrade-failure-due-to-missing-super-admin.conf-file) that blocked cluster upgrades. This issue is fixed in the following updated patches:

  * 1.31.200-gke.59
  * 1.30.600-gke.69
  * 1.30.500-gke.127



The release notes and related documentation have been updated to reflect the updated patch version information.

1.31

Announcement

### Release 1.31.200-gke.59

Google Distributed Cloud for bare metal 1.31.200-gke.59 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.200-gke.59 runs on Kubernetes v1.31.5-gke.300.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Announcement

### Release 1.30.600-gke.69

Google Distributed Cloud for bare metal 1.30.600-gke.69 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.600-gke.69 runs on Kubernetes v1.30.9-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Announcement

The initial patch releases for 1.30.500, 1.30.600, and 1.31.200 contained a [known issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#control-plane-upgrade-failure-due-to-missing-super-admin.conf-file) that blocked cluster upgrades. This issue is fixed in the following updated patches:

  * 1.31.200-gke.59
  * 1.30.600-gke.69
  * 1.30.500-gke.127



The release notes and related documentation have been updated to reflect the updated patch version information.

1.29

Announcement

### Release 1.29.1100-gke.84

Google Distributed Cloud for bare metal 1.29.1100-gke.84 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.1100-gke.84 runs on Kubernetes v1.29.13-gke.500.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Fixed

The following issue is fixed in 1.31.200-gke.69:

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#control-plane-upgrade-failure-due-to-missing-super-admin.conf-file) where node upgrades failed due to missing `super-admin.conf` file.



1.30 

Fixed

The following issues are fixed in 1.30.600-gke.69:

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#control-plane-upgrade-failure-due-to-missing-super-admin.conf-file) where node upgrades failed due to missing `super-admin.conf` file.

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#immutable-field-error-when-updating-user-clusters-with-bmctl-version-1.30.x) where `bmctl update cluster`command fails for user clusters that were created with the`cloudOperationsServiceAccountKeyPath` setting in the header section of the cluster configuration file.




1.30 

Fixed

The 1.30.600-gke.69 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.30 

Change

The following functional change was made in 1.30.600-gke.69:

  * Cluster deletion now deletes worker node pools prior to deleting any control plane node pools.



1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.29

Fixed

The 1.29.1100-gke.84 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.31

Fixed

The 1.31.200-gke.59 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.30 

Announcement

### Release 1.30.500-gke.127

Google Distributed Cloud for bare metal 1.30.500-gke.127 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.500-gke.127 runs on Kubernetes 1.30. 

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.30 

Fixed

The following issues are fixed in 1.30.500-gke.127:

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#control-plane-upgrade-failure-due-to-missing-super-admin.conf-file) where node upgrades failed due to missing `super-admin.conf` file.

  * Fixed an issue where prompting during `bmctl update cluster` prevented use of automation. You can now use the `--quiet` flag to skip prompting.

  * Fixed an issue where node machines didn't update when the registry mirror `hosts` field was updated.




1.30 

Fixed

The 1.30.500-gke.127 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## February 19, 2025

1.30 

Announcement

### Release 1.30.600-gke.68

Google Distributed Cloud for bare metal 1.30.600-gke.68 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.600-gke.68 runs on Kubernetes v1.30.9-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Change

The following functional change was made in 1.30.600-gke.68:

  * Cluster deletion now deletes worker node pools prior to deleting any control plane node pools.



1.30 

Fixed

The following issue is fixed in 1.30.600-gke.68:

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#immutable-field-error-when-updating-user-clusters-with-bmctl-version-1.30.x) where `bmctl update cluster`command fails for user clusters that were created with the`cloudOperationsServiceAccountKeyPath` setting in the header section of the cluster configuration file.



1.30 

Fixed

The 1.30.600-gke.68 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## February 13, 2025

1.31

Announcement

### Release 1.31.200-gke.58

Google Distributed Cloud for bare metal 1.31.200-gke.58 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.200-gke.58 runs on Kubernetes v1.31.5-gke.300.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Fixed

The 1.31.200-gke.58 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## February 05, 2025

1.31

Announcement

### Release 1.31.100-gke.136

Google Distributed Cloud for bare metal 1.31.100-gke.136 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.100-gke.136 runs on Kubernetes 1.31.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Announcement

### Release 1.30.500-gke.126

Google Distributed Cloud for bare metal 1.30.500-gke.126 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.500-gke.126 runs on Kubernetes 1.30. 

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Announcement

### Release 1.29.1000-gke.93

Google Distributed Cloud for bare metal 1.29.1000-gke.93 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.1000-gke.93 runs on Kubernetes 1.29.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Fixed

The following issues are fixed in 1.30.500-gke.126:

  * Fixed an issue where prompting during `bmctl update cluster` prevented use of automation. You can now use the `--quiet` flag to skip prompting.

  * Fixed an issue where node machines didn't update when the registry mirror `hosts` field was updated.




1.29

Change

The following functional change was made in 1.29.1000-gke.93:

  * Cluster deletion now deletes worker node pools prior to deleting any control plane node pools.



1.31

Feature

The following feature is available in 1.31.100-gke.136:

  * **GA:** Added [`bmctl configure projects`](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#configure_projects) command to automatically configure IAM policy bindings for [workload identity cluster authentication](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/keyless). Creates required service accounts and enables required APIs.



1.31

Fixed

The following issues are fixed in 1.31.100-gke.136:

  * Fixed [an issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#immutable-field-error-when-updating-user-clusters-with-bmctl-version-1.30.x) where `bmctl update cluster`command fails for user clusters that were created with the`cloudOperationsServiceAccountKeyPath` setting in the header section of the cluster configuration file.

  * Fixed an issue where prompting during `bmctl update cluster` prevented use of automation. You can now use the `--quiet` flag to skip prompting.

  * Fixed an issue where node machines didn't update when the registry mirror `hosts` field was updated.




1.31

Fixed

The 1.31.100-gke.136 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.31

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.31

Change

The following functional change was made in 1.31.100-gke.136:

  * Cluster deletion now deletes worker node pools prior to deleting any control plane node pools.



1.29

Fixed

The 1.29.1000-gke.93 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.30 

Fixed

The 1.30.500-gke.126 release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.29

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.30 

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## January 24, 2025

1.28

Announcement

### Release 1.28.1400-gke.79

Google Distributed Cloud for bare metal 1.28.1400-gke.79 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.1400-gke.79 runs on Kubernetes 1.28. This is the final patch for the 1.28 minor release.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Fixed

This release includes many vulnerability fixes. For a list of all vulnerabilities fixed in this release, see [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

1.28

Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## January 07, 2025

1.31

Announcement

The original 1.31.0-gke.889 release notes _stated incorrectly_ that the GKE Identity Service allows TLS 1.1 and higher connections, by default. Here is the correct change description:

  * GKE Identity Service now requires that all HTTPS connections use transport layer security (TLS) 1.2 or 1.3. For versions 1.31.0 and higher, TLS 1.1 is disabled by default, however it can be re-enabled if needed.

If you require support for TLS 1.1, reach out to [Cloud Customer Care](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for assistance.




The 1.31.0-gke.889 release notes have been updated to reflect the correct default behavior.

1.29

Announcement

### Release 1.29.900-gke.180

Google Distributed Cloud for bare metal 1.29.900-gke.180 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.900-gke.180 runs on Kubernetes 1.29.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Change

Added support for configuring the GKE Identity Service to enforce a minimum transport layer security (TLS) version of 1.2 for HTTPS connections. By default, the GKE Identity Service allows TLS 1.1 and higher connections. If you require enforcement for a minimum of TLS 1.2, reach out to [Cloud Customer Care](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for assistance.

1.29

Fixed

Fixed an issue where the registry mirror reachability check fails for a single unreachable registry mirror. Now the reachability check applies to configured registry mirrors only, instead of all registry mirrors.

1.29

Fixed

The following container image security vulnerabilities have been fixed in 1.29.900-gke.180:

  * High-severity container vulnerabilities:

[CVE-2015-20107](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-20107), [CVE-2020-10735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10735), [CVE-2020-16156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-16156), [CVE-2021-3737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3737), [CVE-2022-0934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0934), [CVE-2022-1304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1304), [CVE-2022-45061](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45061), [CVE-2022-48733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48733), [CVE-2023-3676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3676), [CVE-2023-3955](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3955), [CVE-2023-5528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5528), [CVE-2023-24329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24329), [CVE-2023-39325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39325), [CVE-2024-6232](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6232), [CVE-2024-7592](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7592), [CVE-2024-0793](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0793), [CVE-2024-38577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38577), [CVE-2024-41011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41011), [CVE-2024-42228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42228), [CVE-2024-42280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42280), [CVE-2024-42284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42284), [CVE-2024-42285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42285), [CVE-2024-42301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42301), [CVE-2024-42302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42302), [CVE-2024-42313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42313), [CVE-2024-43839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43839), [CVE-2024-43858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43858), [CVE-2024-43882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43882), [CVE-2024-44974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44974), [CVE-2024-44987](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44987), [CVE-2024-44998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44998), [CVE-2024-44999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44999), [CVE-2024-46673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46673), [CVE-2024-46674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46674), [CVE-2024-46722](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46722), [CVE-2024-46723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46723), [CVE-2024-46724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46724), [CVE-2024-46725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46725), [CVE-2024-46731](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46731), [CVE-2024-46738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46738), [CVE-2024-46740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46740), [CVE-2024-46743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46743), [CVE-2024-46744](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46744), [CVE-2024-46747](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46747), [CVE-2024-46756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46756), [CVE-2024-46757](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46757), [CVE-2024-46758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46758), [CVE-2024-46759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46759), [CVE-2024-46782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46782), [CVE-2024-46798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46798), [CVE-2024-46800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46800), [CVE-2024-46804](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46804), [CVE-2024-46814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46814), [CVE-2024-46815](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46815), [CVE-2024-46818](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46818), [CVE-2024-46828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46828), [CVE-2024-46844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46844), [GHSA-m425-mq94-257g](https://github.com/advisories/GHSA-m425-mq94-257g)

  * Medium-severity container vulnerabilities:

[CVE-2021-3669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3669), [CVE-2021-3733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3733), [CVE-2021-4189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4189), [CVE-2023-2431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2431), [CVE-2023-27043](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27043), [CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727), [CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728), [CVE-2023-31083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31083), [CVE-2023-3978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3978), [CVE-2023-40217](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40217), [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487), [CVE-2023-52889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52889), [CVE-2024-29018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29018), [CVE-2024-41098](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41098), [CVE-2024-42114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42114), [CVE-2024-42246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42246), [CVE-2024-42259](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42259), [CVE-2024-42272](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42272), [CVE-2024-42283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42283), [CVE-2024-42286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42286), [CVE-2024-42287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42287), [CVE-2024-42288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42288), [CVE-2024-42289](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42289), [CVE-2024-42297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42297), [CVE-2024-42309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42309), [CVE-2024-42310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42310), [CVE-2024-42311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42311), [CVE-2024-43828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43828), [CVE-2024-43829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43829), [CVE-2024-43834](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43834), [CVE-2024-43835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43835), [CVE-2024-43846](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43846), [CVE-2024-43849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43849), [CVE-2024-43853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43853), [CVE-2024-43854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43854), [CVE-2024-43856](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43856), [CVE-2024-43860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43860), [CVE-2024-43861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43861), [CVE-2024-43871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43871), [CVE-2024-43884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43884), [CVE-2024-43889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43889), [CVE-2024-43890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43890), [CVE-2024-43892](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43892), [CVE-2024-43893](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43893), [CVE-2024-43894](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43894), [CVE-2024-43905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43905), [CVE-2024-43907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43907), [CVE-2024-43908](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43908), [CVE-2024-43914](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43914), [CVE-2024-44935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44935), [CVE-2024-44944](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44944), [CVE-2024-44946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44946), [CVE-2024-44947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44947), [CVE-2024-44954](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44954), [CVE-2024-44960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44960), [CVE-2024-44965](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44965), [CVE-2024-44968](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44968), [CVE-2024-44971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44971), [CVE-2024-44988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44988), [CVE-2024-44989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44989), [CVE-2024-44990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44990), [CVE-2024-44995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44995), [CVE-2024-45003](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45003), [CVE-2024-45006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45006), [CVE-2024-45016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45016), [CVE-2024-45018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45018), [CVE-2024-45021](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45021), [CVE-2024-45025](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45025), [CVE-2024-45028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45028), [CVE-2024-46675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46675), [CVE-2024-46676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46676), [CVE-2024-46677](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46677), [CVE-2024-46679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46679), [CVE-2024-46685](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46685), [CVE-2024-46689](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46689), [CVE-2024-46702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46702), [CVE-2024-46707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46707), [CVE-2024-46714](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46714), [CVE-2024-46719](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46719), [CVE-2024-46721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46721), [CVE-2024-46737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46737), [CVE-2024-46739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46739), [CVE-2024-46750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46750), [CVE-2024-46755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46755), [CVE-2024-46763](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46763), [CVE-2024-46771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46771), [CVE-2024-46777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46777), [CVE-2024-46780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46780), [CVE-2024-46781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46781), [CVE-2024-46783](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46783), [CVE-2024-46791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46791), [CVE-2024-46817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46817), [CVE-2024-46819](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46819), [CVE-2024-46822](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46822), [CVE-2024-46829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46829), [CVE-2024-46840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46840), [CVE-2024-47663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47663), [GHSA-jq35-85cj-fj4p](https://github.com/advisories/GHSA-jq35-85cj-fj4p), [GHSA-r4pg-vg54-wxx4](https://github.com/advisories/GHSA-r4pg-vg54-wxx4)

  * Low-severity container vulnerabilities:

[CVE-2018-7738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-7738), [CVE-2021-3426](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3426), [CVE-2021-28861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28861), [CVE-2021-29921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29921), [CVE-2021-36084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36084), [CVE-2021-36085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36085), [CVE-2021-36086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36086), [CVE-2021-36087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36087), [CVE-2022-42919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42919), [CVE-2023-6597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6597), [CVE-2023-28450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28450), [CVE-2023-50387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50387), [CVE-2023-50868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50868), [CVE-2024-0397](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0397), [CVE-2024-4032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4032), [CVE-2024-8088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8088), [CVE-2024-8508](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8508), [CVE-2024-8775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8775), [CVE-2024-9287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9287), [CVE-2024-9902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9902), [CVE-2024-11168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11168), [CVE-2024-43841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43841), [CVE-2024-52533](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-52533)




1.29

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## December 18, 2024

1.31

Announcement

### Release 1.31.0-gke.889

Google Distributed Cloud for bare metal 1.31.0-gke.889 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.0-gke.889 runs on Kubernetes 1.31.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.31

Announcement

**Version 1.28 end of life** : In accordance with the [Version Support Policy](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#version-support), version 1.28 (all patch releases) of Google Distributed Cloud for bare metal has reached its end of life and is no longer supported.

1.31

Change

**Functionality changes:**

  * (Edited: January 7, 2025) GKE Identity Service now requires that all HTTPS connections use transport layer security (TLS) 1.2 or 1.3. For versions 1.31.0 and higher, TLS 1.1 is disabled by default, however it can be re-enabled if needed.

If you require support for TLS 1.1, reach out to [Cloud Customer Care](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for assistance.

  * Updated the `bmctl push images` command to check for the existence of an image digest to determine whether or not to push an image.

  * Increased priority for `cert-manager` pods to system-cluster-critical to prevent premature eviction under control plane node resource pressure.

  * Updated the logic for parsing the cluster configuration file for newer clusters to validate that the `anthosBareMetalVersion` value follows the full `x.y.z-gke.n` semantic versioning scheme, including the GKE patch version.

  * Updated the snapshot capability to collect the following information:

    * Details for all custom resources
    * Additional debugging information for clusters
  * Add a health check to check that the `ifnode-problem-detector` systemd service is running on the node.

  * Updated the `bmctl update` command to identify differences (if any) between the preview feature annotations in the cluster configuration file and the annotations in the deployed Cluster resource.

  * Added a `--num-of-parallel-threads` flag to the snapshot command (`bmctl check cluster --snapshot`) so that you can specify the number of threads to use to create a snapshot. The default number of threads for snapshot creation is 10.




1.31

Fixed

**Fixes:**

  * Fixed an issue where the registry mirror reachability check fails for a single unreachable registry mirror. Now the reachability check applies to configured registry mirrors only, instead of all registry mirrors.

  * Fixed the [issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#non-root-users-cant-run-bmctl-restore-to-restore-quorum) where non-root users can't run `bmctl restore` to restore quorum.

  * Fixed the issue that caused the `cplb-update` healthcheck job to run every 7 days, instead when needed only.

  * Fixed an issue where CronJob specs for periodic health checks weren't updated to reflect cluster annotation changes.

  * Fixed an issue where the control plane VIP might become unavailable because Keepalived didn't check correctly that the VIP is on a node with a responsive HAProxy.

  * Fixed the issue where, due to a misconfigured client, `bmctl update` misjudges clusters about whether they're self-managed.

  * Fixed Cloud Audit Logging failure due to allowlisting issue with multiple project IDs.




The following container image security vulnerabilities have been fixed in 1.31.0-gke.889: 

  * Critical container vulnerabilities:

    * [CVE-2022-36227](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36227)
    * [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)
    * [CVE-2024-41110](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41110)
    * [CVE-2024-45490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45490)
    * [CVE-2024-45491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45491)
    * [CVE-2024-45492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45492)
  * High-severity container vulnerabilities:

    * [CVE-2020-22218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-22218)
    * [CVE-2021-3583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3583)
    * [CVE-2022-1304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1304)
    * [CVE-2022-3697](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3697)
    * [CVE-2022-48733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48733)
    * [CVE-2023-3676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3676)
    * [CVE-2023-3955](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3955)
    * [CVE-2023-4237](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4237)
    * [CVE-2023-5528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5528)
    * [CVE-2023-5764](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5764)
    * [CVE-2023-7104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7104)
    * [CVE-2023-39325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39325)
    * [CVE-2023-47038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47038)
    * [CVE-2023-47108](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47108)
    * [CVE-2023-49083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49083)
    * [CVE-2023-52425](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52425)
    * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)
    * [CVE-2024-0567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0567)
    * [CVE-2024-0743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0743)
    * [CVE-2024-0793](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0793)
    * [CVE-2024-5321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5321)
    * [CVE-2024-6609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6609)
    * [CVE-2024-7348](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7348)
    * [CVE-2024-10220](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-10220)
    * [CVE-2024-20696](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20696)
    * [CVE-2024-37370](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37370)
    * [CVE-2024-38577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38577)
    * [CVE-2024-39487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39487)
    * [CVE-2024-41011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41011)
    * [CVE-2024-41040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41040)
    * [CVE-2024-41046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41046)
    * [CVE-2024-41049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41049)
    * [CVE-2024-41059](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41059)
    * [CVE-2024-41070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41070)
    * [CVE-2024-42104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42104)
    * [CVE-2024-42148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42148)
    * [CVE-2024-42228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42228)
    * [CVE-2024-42280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42280)
    * [CVE-2024-42284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42284)
    * [CVE-2024-42285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42285)
    * [CVE-2024-42301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42301)
    * [CVE-2024-42302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42302)
    * [CVE-2024-42313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42313)
    * [CVE-2024-43839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43839)
    * [CVE-2024-43858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43858)
    * [CVE-2024-43882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43882)
    * [CVE-2024-44974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44974)
    * [CVE-2024-44987](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44987)
    * [CVE-2024-44998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44998)
    * [CVE-2024-44999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44999)
    * [CVE-2024-46673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46673)
    * [CVE-2024-46674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46674)
    * [CVE-2024-46722](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46722)
    * [CVE-2024-46723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46723)
    * [CVE-2024-46724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46724)
    * [CVE-2024-46725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46725)
    * [CVE-2024-46731](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46731)
    * [CVE-2024-46738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46738)
    * [CVE-2024-46740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46740)
    * [CVE-2024-46743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46743)
    * [CVE-2024-46744](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46744)
    * [CVE-2024-46747](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46747)
    * [CVE-2024-46756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46756)
    * [CVE-2024-46757](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46757)
    * [CVE-2024-46758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46758)
    * [CVE-2024-46759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46759)
    * [CVE-2024-46782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46782)
    * [CVE-2024-46798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46798)
    * [CVE-2024-46800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46800)
    * [CVE-2024-46804](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46804)
    * [CVE-2024-46814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46814)
    * [CVE-2024-46815](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46815)
    * [CVE-2024-46818](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46818)
    * [CVE-2024-46828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46828)
    * [CVE-2024-46844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46844)
    * [GHSA-87m9-rv8p-rgmg](https://github.com/advisories/GHSA-87m9-rv8p-rgmg)
    * [GHSA-m425-mq94-257g](https://github.com/advisories/GHSA-m425-mq94-257g)
  * Medium-severity container vulnerabilities:

    * [CVE-2016-3709](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3709)
    * [CVE-2021-3620](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3620)
    * [CVE-2021-3669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3669)
    * [CVE-2021-36976](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36976)
    * [CVE-2022-26280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-26280)
    * [CVE-2023-2431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2431)
    * [CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)
    * [CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)
    * [CVE-2023-3978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3978)
    * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)
    * [CVE-2023-23931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23931)
    * [CVE-2023-31083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31083)
    * [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)
    * [CVE-2023-5115](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5115)
    * [CVE-2023-52889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52889)
    * [CVE-2024-0690](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0690)
    * [CVE-2024-6104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6104)
    * [CVE-2024-7264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7264)
    * [CVE-2024-8096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8096)
    * [CVE-2024-24557](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24557)
    * [CVE-2024-29018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29018)
    * [CVE-2024-36901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36901)
    * [CVE-2024-36938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36938)
    * [CVE-2024-41009](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41009)
    * [CVE-2024-41012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41012)
    * [CVE-2024-41055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41055)
    * [CVE-2024-41063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41063)
    * [CVE-2024-41064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41064)
    * [CVE-2024-41098](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41098)
    * [CVE-2024-42101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42101)
    * [CVE-2024-42102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42102)
    * [CVE-2024-42114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42114)
    * [CVE-2024-42131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42131)
    * [CVE-2024-42137](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42137)
    * [CVE-2024-42152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42152)
    * [CVE-2024-42153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42153)
    * [CVE-2024-42154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42154)
    * [CVE-2024-42157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42157)
    * [CVE-2024-42161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42161)
    * [CVE-2024-42223](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42223)
    * [CVE-2024-42224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42224)
    * [CVE-2024-42229](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42229)
    * [CVE-2024-42232](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42232)
    * [CVE-2024-42236](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42236)
    * [CVE-2024-42244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42244)
    * [CVE-2024-42246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42246)
    * [CVE-2024-42247](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42247)
    * [CVE-2024-42259](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42259)
    * [CVE-2024-42272](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42272)
    * [CVE-2024-42283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42283)
    * [CVE-2024-42286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42286)
    * [CVE-2024-42287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42287)
    * [CVE-2024-42288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42288)
    * [CVE-2024-42289](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42289)
    * [CVE-2024-42297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42297)
    * [CVE-2024-42309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42309)
    * [CVE-2024-42310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42310)
    * [CVE-2024-42311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42311)
    * [CVE-2024-43828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43828)
    * [CVE-2024-43829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43829)
    * [CVE-2024-43834](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43834)
    * [CVE-2024-43835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43835)
    * [CVE-2024-43846](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43846)
    * [CVE-2024-43849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43849)
    * [CVE-2024-43853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43853)
    * [CVE-2024-43854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43854)
    * [CVE-2024-43856](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43856)
    * [CVE-2024-43860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43860)
    * [CVE-2024-43861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43861)
    * [CVE-2024-43871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43871)
    * [CVE-2024-43884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43884)
    * [CVE-2024-43889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43889)
    * [CVE-2024-43890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43890)
    * [CVE-2024-43892](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43892)
    * [CVE-2024-43893](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43893)
    * [CVE-2024-43894](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43894)
    * [CVE-2024-43905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43905)
    * [CVE-2024-43907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43907)
    * [CVE-2024-43908](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43908)
    * [CVE-2024-43914](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43914)
    * [CVE-2024-44935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44935)
    * [CVE-2024-44944](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44944)
    * [CVE-2024-44946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44946)
    * [CVE-2024-44947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44947)
    * [CVE-2024-44954](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44954)
    * [CVE-2024-44960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44960)
    * [CVE-2024-44965](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44965)
    * [CVE-2024-44968](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44968)
    * [CVE-2024-44971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44971)
    * [CVE-2024-44988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44988)
    * [CVE-2024-44989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44989)
    * [CVE-2024-44990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44990)
    * [CVE-2024-44995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44995)
    * [CVE-2024-45003](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45003)
    * [CVE-2024-45006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45006)
    * [CVE-2024-45016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45016)
    * [CVE-2024-45018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45018)
    * [CVE-2024-45021](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45021)
    * [CVE-2024-45025](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45025)
    * [CVE-2024-45028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45028)
    * [CVE-2024-46675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46675)
    * [CVE-2024-46676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46676)
    * [CVE-2024-46677](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46677)
    * [CVE-2024-46679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46679)
    * [CVE-2024-46685](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46685)
    * [CVE-2024-46689](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46689)
    * [CVE-2024-46702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46702)
    * [CVE-2024-46707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46707)
    * [CVE-2024-46714](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46714)
    * [CVE-2024-46719](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46719)
    * [CVE-2024-46721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46721)
    * [CVE-2024-46737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46737)
    * [CVE-2024-46739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46739)
    * [CVE-2024-46750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46750)
    * [CVE-2024-46755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46755)
    * [CVE-2024-46763](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46763)
    * [CVE-2024-46771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46771)
    * [CVE-2024-46777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46777)
    * [CVE-2024-46780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46780)
    * [CVE-2024-46781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46781)
    * [CVE-2024-46783](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46783)
    * [CVE-2024-46791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46791)
    * [CVE-2024-46817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46817)
    * [CVE-2024-46819](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46819)
    * [CVE-2024-46822](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46822)
    * [CVE-2024-46829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46829)
    * [CVE-2024-46840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46840)
    * [CVE-2024-47663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47663)
    * [GHSA-jq35-85cj-fj4p](https://github.com/advisories/GHSA-jq35-85cj-fj4p)
    * [GHSA-mh55-gqvf-xfwm](https://github.com/advisories/GHSA-mh55-gqvf-xfwm)
  * Low-severity container vulnerabilities:

    * [CVE-2021-36690](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36690)
    * [CVE-2022-2309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2309)
    * [CVE-2022-48303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48303)
    * [CVE-2024-3177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3177)
    * [CVE-2024-41007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41007)
    * [CVE-2024-43167](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43167)
    * [CVE-2024-43168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43168)
    * [CVE-2024-43841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43841)



1.31

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## December 11, 2024

1.28

Announcement

### Release 1.28.1300-gke.59

Google Distributed Cloud for bare metal 1.28.1300-gke.59 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.1300-gke.59 runs on Kubernetes 1.28.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.1300-gke.59: 

  * High-severity container vulnerabilities:

    * [CVE-2015-20107](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-20107)

    * [CVE-2020-10735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10735)

    * [CVE-2021-3737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3737)

    * [CVE-2022-0934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0934)

    * [CVE-2022-45061](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45061)

    * [CVE-2022-48733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48733)

    * [CVE-2023-24329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24329)

    * [CVE-2024-0743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0743)

    * [CVE-2024-6232](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6232)

    * [CVE-2024-6609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6609)

    * [CVE-2024-7592](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7592)

    * [CVE-2024-38577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38577)

    * [CVE-2024-41011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41011)

    * [CVE-2024-42228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42228)

    * [CVE-2024-42280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42280)

    * [CVE-2024-42284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42284)

    * [CVE-2024-42285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42285)

    * [CVE-2024-42301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42301)

    * [CVE-2024-42302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42302)

    * [CVE-2024-42313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42313)

    * [CVE-2024-43839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43839)

    * [CVE-2024-43858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43858)

    * [CVE-2024-43882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43882)

    * [CVE-2024-44974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44974)

    * [CVE-2024-44987](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44987)

    * [CVE-2024-44998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44998)

    * [CVE-2024-44999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44999)

    * [CVE-2024-46673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46673)

    * [CVE-2024-46674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46674)

    * [CVE-2024-46722](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46722)

    * [CVE-2024-46723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46723)

    * [CVE-2024-46724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46724)

    * [CVE-2024-46725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46725)

    * [CVE-2024-46731](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46731)

    * [CVE-2024-46738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46738)

    * [CVE-2024-46740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46740)

    * [CVE-2024-46743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46743)

    * [CVE-2024-46744](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46744)

    * [CVE-2024-46747](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46747)

    * [CVE-2024-46756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46756)

    * [CVE-2024-46757](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46757)

    * [CVE-2024-46758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46758)

    * [CVE-2024-46759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46759)

    * [CVE-2024-46782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46782)

    * [CVE-2024-46798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46798)

    * [CVE-2024-46800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46800)

    * [CVE-2024-46804](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46804)

    * [CVE-2024-46814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46814)

    * [CVE-2024-46815](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46815)

    * [CVE-2024-46818](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46818)

    * [CVE-2024-46828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46828)

    * [CVE-2024-46844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46844)

  * Medium-severity container vulnerabilities:

    * [CVE-2021-3669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3669)

    * [CVE-2021-3733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3733)

    * [CVE-2021-4189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4189)

    * [CVE-2023-27043](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27043)

    * [CVE-2023-31083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31083)

    * [CVE-2023-40217](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40217)

    * [CVE-2023-52889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52889)

    * [CVE-2024-41098](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41098)

    * [CVE-2024-42114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42114)

    * [CVE-2024-42246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42246)

    * [CVE-2024-42259](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42259)

    * [CVE-2024-42272](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42272)

    * [CVE-2024-42283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42283)

    * [CVE-2024-42286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42286)

    * [CVE-2024-42287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42287)

    * [CVE-2024-42288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42288)

    * [CVE-2024-42289](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42289)

    * [CVE-2024-42297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42297)

    * [CVE-2024-42309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42309)

    * [CVE-2024-42310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42310)

    * [CVE-2024-42311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42311)

    * [CVE-2024-43828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43828)

    * [CVE-2024-43829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43829)

    * [CVE-2024-43834](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43834)

    * [CVE-2024-43835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43835)

    * [CVE-2024-43846](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43846)

    * [CVE-2024-43849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43849)

    * [CVE-2024-43853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43853)

    * [CVE-2024-43854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43854)

    * [CVE-2024-43856](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43856)

    * [CVE-2024-43860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43860)

    * [CVE-2024-43861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43861)

    * [CVE-2024-43871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43871)

    * [CVE-2024-43884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43884)

    * [CVE-2024-43889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43889)

    * [CVE-2024-43890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43890)

    * [CVE-2024-43892](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43892)

    * [CVE-2024-43893](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43893)

    * [CVE-2024-43894](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43894)

    * [CVE-2024-43905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43905)

    * [CVE-2024-43907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43907)

    * [CVE-2024-43908](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43908)

    * [CVE-2024-43914](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43914)

    * [CVE-2024-44935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44935)

    * [CVE-2024-44944](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44944)

    * [CVE-2024-44946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44946)

    * [CVE-2024-44947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44947)

    * [CVE-2024-44954](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44954)

    * [CVE-2024-44960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44960)

    * [CVE-2024-44965](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44965)

    * [CVE-2024-44968](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44968)

    * [CVE-2024-44971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44971)

    * [CVE-2024-44988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44988)

    * [CVE-2024-44989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44989)

    * [CVE-2024-44990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44990)

    * [CVE-2024-44995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44995)

    * [CVE-2024-45003](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45003)

    * [CVE-2024-45006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45006)

    * [CVE-2024-45016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45016)

    * [CVE-2024-45018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45018)

    * [CVE-2024-45021](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45021)

    * [CVE-2024-45025](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45025)

    * [CVE-2024-45028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45028)

    * [CVE-2024-46675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46675)

    * [CVE-2024-46676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46676)

    * [CVE-2024-46677](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46677)

    * [CVE-2024-46679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46679)

    * [CVE-2024-46685](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46685)

    * [CVE-2024-46689](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46689)

    * [CVE-2024-46702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46702)

    * [CVE-2024-46707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46707)

    * [CVE-2024-46714](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46714)

    * [CVE-2024-46719](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46719)

    * [CVE-2024-46721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46721)

    * [CVE-2024-46737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46737)

    * [CVE-2024-46739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46739)

    * [CVE-2024-46750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46750)

    * [CVE-2024-46755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46755)

    * [CVE-2024-46763](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46763)

    * [CVE-2024-46771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46771)

    * [CVE-2024-46777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46777)

    * [CVE-2024-46780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46780)

    * [CVE-2024-46781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46781)

    * [CVE-2024-46783](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46783)

    * [CVE-2024-46791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46791)

    * [CVE-2024-46817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46817)

    * [CVE-2024-46819](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46819)

    * [CVE-2024-46822](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46822)

    * [CVE-2024-46829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46829)

    * [CVE-2024-46840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46840)

    * [CVE-2024-47663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47663)

  * Low-severity container vulnerabilities:

    * [CVE-2021-3426](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3426)

    * [CVE-2021-28861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28861)

    * [CVE-2021-29921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29921)

    * [CVE-2022-42919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42919)

    * [CVE-2023-6597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6597)

    * [CVE-2023-28450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28450)

    * [CVE-2023-50387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50387)

    * [CVE-2023-50868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50868)

    * [CVE-2024-0397](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0397)

    * [CVE-2024-4032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4032)

    * [CVE-2024-8088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8088)

    * [CVE-2024-8508](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8508)

    * [CVE-2024-8775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8775)

    * [CVE-2024-9287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9287)

    * [CVE-2024-9902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9902)

    * [CVE-2024-11168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11168)

    * [CVE-2024-43841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43841)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## December 10, 2024

1.30 

Announcement

### Release 1.30.400-gke.133

Google Distributed Cloud for bare metal 1.30.400-gke.133 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.400-gke.133 runs on Kubernetes 1.30.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Change

**Functionality changes:**

  * Updated snapshots to include new information, including: kubelet config, CPU manager state, and memory manager state.

  * Updated the `bmctl push images` command to check for the existence of an image digest to determine whether or not to push an image.

  * Added support for configuring the GKE Identity Service to enforce a minimum transport layer security (TLS) version of 1.2 for HTTPS connections. By default, the GKE Identity Service allows TLS 1.1 and higher connections. If you require enforcement for a minimum of TLS 1.2, reach out to [Cloud Customer Care](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for assistance.




1.30 

Fixed

**Fixes:**

  * Fixed the [issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#non-root-users-cant-run-bmctl-restore-to-restore-quorum) where non-root users can't run `bmctl restore` to restore quorum.

  * Fixed an issue where CronJob specs for periodic health checks weren't updated to reflect cluster annotation changes.

  * Fixed an [issue that blocked **user cluster** create and upgrade operations](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#user-cluster-creation-or-upgrade-operations-might-not-succeed) to patch versions 1.30.100, 1.30.200, or 1.30.300. This issue applies only when `kubectl` or a GKE On-Prem API client (console, gcloud CLI, or Terraform) is used for user cluster creation and upgrades.




1.30 

Fixed

The following container image security vulnerabilities have been fixed in 1.30.400-gke.133: 

  * Critical container vulnerabilities: 
    * [CVE-2022-36227](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36227)
    * [CVE-2024-45491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45491)
    * [CVE-2024-45492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45492)
  * High-severity container vulnerabilities: 
    * [CVE-2020-16156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-16156)
    * [CVE-2021-33194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33194)
    * [CVE-2022-1304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1304)
    * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)
    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)
    * [CVE-2022-48733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48733)
    * [CVE-2023-3676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3676)
    * [CVE-2023-3955](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3955)
    * [CVE-2023-5528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5528)
    * [CVE-2023-7104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7104)
    * [CVE-2023-39325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39325)
    * [CVE-2023-49083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49083)
    * [CVE-2023-52425](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52425)
    * [CVE-2024-0743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0743)
    * [CVE-2024-0793](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0793)
    * [CVE-2024-6609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6609)
    * [CVE-2024-20696](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-20696)
    * [CVE-2024-38577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38577)
    * [CVE-2024-41011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41011)
    * [CVE-2024-42228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42228)
    * [CVE-2024-42280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42280)
    * [CVE-2024-42284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42284)
    * [CVE-2024-42285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42285)
    * [CVE-2024-42301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42301)
    * [CVE-2024-42302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42302)
    * [CVE-2024-42313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42313)
    * [CVE-2024-43839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43839)
    * [CVE-2024-43858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43858)
    * [CVE-2024-43882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43882)
    * [CVE-2024-44974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44974)
    * [CVE-2024-44987](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44987)
    * [CVE-2024-44998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44998)
    * [CVE-2024-44999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44999)
    * [CVE-2024-45490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45490)
    * [CVE-2024-46673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46673)
    * [CVE-2024-46674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46674)
    * [CVE-2024-46722](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46722)
    * [CVE-2024-46723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46723)
    * [CVE-2024-46724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46724)
    * [CVE-2024-46725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46725)
    * [CVE-2024-46731](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46731)
    * [CVE-2024-46738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46738)
    * [CVE-2024-46740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46740)
    * [CVE-2024-46743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46743)
    * [CVE-2024-46744](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46744)
    * [CVE-2024-46747](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46747)
    * [CVE-2024-46756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46756)
    * [CVE-2024-46757](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46757)
    * [CVE-2024-46758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46758)
    * [CVE-2024-46759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46759)
    * [CVE-2024-46782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46782)
    * [CVE-2024-46798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46798)
    * [CVE-2024-46800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46800)
    * [CVE-2024-46804](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46804)
    * [CVE-2024-46814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46814)
    * [CVE-2024-46815](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46815)
    * [CVE-2024-46818](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46818)
    * [CVE-2024-46828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46828)
    * [CVE-2024-46844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46844)
    * [GHSA-m425-mq94-257g](https://github.com/advisories/GHSA-m425-mq94-257g)
  * Medium-severity container vulnerabilities: 
    * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)
    * [CVE-2021-3669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3669)
    * [CVE-2021-36976](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36976)
    * [CVE-2022-26280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-26280)
    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)
    * [CVE-2023-2431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2431)
    * [CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)
    * [CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)
    * [CVE-2023-3978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3978)
    * [CVE-2023-23931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23931)
    * [CVE-2023-31083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31083)
    * [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)
    * [CVE-2023-52889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52889)
    * [CVE-2024-24557](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24557)
    * [CVE-2024-29018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29018)
    * [CVE-2024-41098](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41098)
    * [CVE-2024-42114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42114)
    * [CVE-2024-42246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42246)
    * [CVE-2024-42259](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42259)
    * [CVE-2024-42272](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42272)
    * [CVE-2024-42283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42283)
    * [CVE-2024-42286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42286)
    * [CVE-2024-42287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42287)
    * [CVE-2024-42288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42288)
    * [CVE-2024-42289](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42289)
    * [CVE-2024-42297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42297)
    * [CVE-2024-42309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42309)
    * [CVE-2024-42310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42310)
    * [CVE-2024-42311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42311)
    * [CVE-2024-43828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43828)
    * [CVE-2024-43829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43829)
    * [CVE-2024-43834](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43834)
    * [CVE-2024-43835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43835)
    * [CVE-2024-43846](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43846)
    * [CVE-2024-43849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43849)
    * [CVE-2024-43853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43853)
    * [CVE-2024-43854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43854)
    * [CVE-2024-43856](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43856)
    * [CVE-2024-43860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43860)
    * [CVE-2024-43861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43861)
    * [CVE-2024-43871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43871)
    * [CVE-2024-43884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43884)
    * [CVE-2024-43889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43889)
    * [CVE-2024-43890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43890)
    * [CVE-2024-43892](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43892)
    * [CVE-2024-43893](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43893)
    * [CVE-2024-43894](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43894)
    * [CVE-2024-43905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43905)
    * [CVE-2024-43907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43907)
    * [CVE-2024-43908](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43908)
    * [CVE-2024-43914](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43914)
    * [CVE-2024-44935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44935)
    * [CVE-2024-44944](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44944)
    * [CVE-2024-44946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44946)
    * [CVE-2024-44947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44947)
    * [CVE-2024-44954](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44954)
    * [CVE-2024-44960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44960)
    * [CVE-2024-44965](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44965)
    * [CVE-2024-44968](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44968)
    * [CVE-2024-44971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44971)
    * [CVE-2024-44988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44988)
    * [CVE-2024-44989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44989)
    * [CVE-2024-44990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44990)
    * [CVE-2024-44995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44995)
    * [CVE-2024-45003](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45003)
    * [CVE-2024-45006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45006)
    * [CVE-2024-45016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45016)
    * [CVE-2024-45018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45018)
    * [CVE-2024-45021](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45021)
    * [CVE-2024-45025](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45025)
    * [CVE-2024-45028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45028)
    * [CVE-2024-46675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46675)
    * [CVE-2024-46676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46676)
    * [CVE-2024-46677](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46677)
    * [CVE-2024-46679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46679)
    * [CVE-2024-46685](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46685)
    * [CVE-2024-46689](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46689)
    * [CVE-2024-46702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46702)
    * [CVE-2024-46707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46707)
    * [CVE-2024-46714](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46714)
    * [CVE-2024-46719](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46719)
    * [CVE-2024-46721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46721)
    * [CVE-2024-46737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46737)
    * [CVE-2024-46739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46739)
    * [CVE-2024-46750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46750)
    * [CVE-2024-46755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46755)
    * [CVE-2024-46763](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46763)
    * [CVE-2024-46771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46771)
    * [CVE-2024-46777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46777)
    * [CVE-2024-46780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46780)
    * [CVE-2024-46781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46781)
    * [CVE-2024-46783](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46783)
    * [CVE-2024-46791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46791)
    * [CVE-2024-46817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46817)
    * [CVE-2024-46819](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46819)
    * [CVE-2024-46822](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46822)
    * [CVE-2024-46829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46829)
    * [CVE-2024-46840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46840)
    * [CVE-2024-47663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47663)
    * [GHSA-jq35-85cj-fj4p](https://github.com/advisories/GHSA-jq35-85cj-fj4p)
  * Low-severity container vulnerabilities: 
    * [CVE-2024-3177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3177)
    * [CVE-2021-36084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36084)
    * [CVE-2021-36085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36085)
    * [CVE-2021-36086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36086)
    * [CVE-2021-36087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36087)
    * [CVE-2021-36690](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36690)
    * [CVE-2024-43841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43841)



1.30 

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## November 22, 2024

1.30 

Announcement

### Release 1.30.300-gke.84

Google Distributed Cloud for bare metal 1.30.300-gke.84 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.300-gke.84 runs on Kubernetes 1.30.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Fixed

**Fixes:**

  * Fixed an issue where the control plane VIP might become unavailable because Keepalived didn't check correctly that the VIP is on a node with a responsive HAProxy.

  * Fixed an issue where the registry mirror reachability check fails for a single unreachable registry mirror. Now the reachability check applies to configured registry mirrors only, instead of all registry mirrors.




1.30 

Fixed

The following container image security vulnerabilities have been fixed in 1.30.300-gke.84: 

  * Low-severity container vulnerabilities:

    * [CVE-2024-43167](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43167)

    * [CVE-2024-43168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43168)




1.30 

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## November 21, 2024

1.29

Announcement

### Release 1.29.800-gke.111

Google Distributed Cloud for bare metal 1.29.800-gke.111 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.800-gke.111 runs on Kubernetes 1.29.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Change

**Functionality changes:**

  * Added support for configuring the GKE Identity Service to enforce a minimum transport layer security (TLS) version of 1.2 for HTTPS connections. By default, the GKE Identity Service allows TLS 1.1 and higher connections. If you require enforcement for a minimum of TLS 1.2, reach out to [Cloud Customer Care](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for assistance.



1.29

Fixed

**Fixes:**

  * Fixed the [issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#non-root-users-cant-run-bmctl-restore-to-restore-quorum) where non-root users can't run `bmctl restore` to restore quorum.



1.29

Fixed

The following container image security vulnerabilities have been fixed in 1.29.800-gke.111:

  * High-severity container vulnerabilities:

    * [CVE-2023-49083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49083)

    * [CVE-2024-0743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0743)

    * [CVE-2024-6609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6609)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-23931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23931)

    * [CVE-2024-50096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-50096)

    * [CVE-2024-50099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-50099)




1.29

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## November 07, 2024

1.28

Announcement

### Release 1.28.1200-gke.83

Google Distributed Cloud for bare metal 1.28.1200-gke.83 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.1200-gke.83 runs on Kubernetes 1.28.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Fixed

**Fixes:**

  * Fixed an issue where the registry mirror reachability check fails for a single unreachable registry mirror. Now the reachability check applies to configured registry mirrors only, instead of all registry mirrors.

  * Fixed the [issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#non-root-users-cant-run-bmctl-restore-to-restore-quorum) where non-root users can't run `bmctl restore` to restore quorum.




1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.1200-gke.83: 

  * High-severity container vulnerabilities:

    * [CVE-2021-33194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33194)

    * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)

    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)

  * Medium-severity container vulnerabilities:

    * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-23931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23931)

  * Low-severity container vulnerabilities:

    * [CVE-2023-49083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49083)



1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## October 24, 2024

1.29

Announcement

### Release 1.29.700-gke.113

Google Distributed Cloud for bare metal 1.29.700-gke.113 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.700-gke.113 runs on Kubernetes 1.29.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Fixed

**Fixes:**

  * Fixed an issue where the control plane VIP might become unavailable because Keepalived didn't check correctly that the VIP is on a node with a responsive HAProxy.
  * Fixed an issue where `bmctl restore` fails due to etcd containers not starting correctly.
  * Fixed an issue where the registry mirror reachability check fails for a single unreachable registry mirror. Now the reachability check applies to configured registry mirrors only, instead of all registry mirrors.



1.29

Fixed

The following container image security vulnerabilities have been fixed in 1.29.700-gke.113: 

  * Medium-severity container vulnerabilities:

    * [CVE-2024-7264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7264)
  * Low-severity container vulnerabilities:

    * [CVE-2024-43167](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43167)

    * [CVE-2024-43168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43168)

    * [GHSA-xr7q-jx4m-x55m](https://github.com/advisories/GHSA-xr7q-jx4m-x55m)




1.29

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## October 17, 2024

1.28

Announcement

### Release 1.28.1100-gke.94

Google Distributed Cloud for bare metal 1.28.1100-gke.94 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.1100-gke.94 runs on Kubernetes 1.28.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Fixed

Fixed an issue where the control plane VIP might become unavailable because Keepalived didn't check correctly that the VIP is on a node with a responsive HAProxy.

1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.1100-gke.94: 

  * High-severity container vulnerabilities:

    * [CVE-2024-39487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39487)

    * [CVE-2024-41040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41040)

    * [CVE-2024-41046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41046)

    * [CVE-2024-41049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41049)

    * [CVE-2024-41059](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41059)

    * [CVE-2024-41070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41070)

    * [CVE-2024-42104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42104)

    * [CVE-2024-42148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42148)

  * Medium-severity container vulnerabilities:

    * [CVE-2016-3709](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3709)

    * [CVE-2024-7264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7264)

    * [CVE-2024-36901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36901)

    * [CVE-2024-36938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36938)

    * [CVE-2024-41009](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41009)

    * [CVE-2024-41012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41012)

    * [CVE-2024-41055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41055)

    * [CVE-2024-41063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41063)

    * [CVE-2024-41064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41064)

    * [CVE-2024-42101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42101)

    * [CVE-2024-42102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42102)

    * [CVE-2024-42131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42131)

    * [CVE-2024-42137](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42137)

    * [CVE-2024-42152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42152)

    * [CVE-2024-42153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42153)

    * [CVE-2024-42154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42154)

    * [CVE-2024-42157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42157)

    * [CVE-2024-42161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42161)

    * [CVE-2024-42223](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42223)

    * [CVE-2024-42224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42224)

    * [CVE-2024-42229](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42229)

    * [CVE-2024-42232](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42232)

    * [CVE-2024-42236](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42236)

    * [CVE-2024-42244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42244)

    * [CVE-2024-42247](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42247)

  * Low-severity container vulnerabilities:

    * [CVE-2022-2309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2309)

    * [CVE-2024-41007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41007)

    * [GHSA-xr7q-jx4m-x55m](https://github.com/advisories/GHSA-xr7q-jx4m-x55m)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## October 10, 2024

1.30 

Announcement

### Release 1.30.200-gke.101

Google Distributed Cloud for bare metal 1.30.200-gke.101 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.200-gke.101 runs on Kubernetes 1.30.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Change

Updated the `bmctl update` command to identify differences (if any) between the preview feature annotations in the cluster configuration file and the annotations in the deployed Cluster resource.

1.30 

Fixed

**Fixes:**

  * Fixed an issue where the control plane VIP might become unavailable because Keepalived didn't check correctly that the VIP is on a node with a responsive HAProxy.

  * Fixed Cloud Audit Logging failure due to allowlisting issue with multiple project IDs.




1.30 

Fixed

The following container image security vulnerabilities have been fixed in 1.30.200-gke.101: 

  * Critical container vulnerabilities:

    * [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)
  * High-severity container vulnerabilities:

    * [CVE-2023-47038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47038)

    * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)

    * [CVE-2024-0567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0567)

    * [CVE-2024-37370](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37370)

    * [CVE-2024-39487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39487)

    * [CVE-2024-41040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41040)

    * [CVE-2024-41046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41046)

    * [CVE-2024-41049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41049)

    * [CVE-2024-41059](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41059)

    * [CVE-2024-41070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41070)

    * [CVE-2024-42104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42104)

    * [CVE-2024-42148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42148)

  * Medium-severity container vulnerabilities:

    * [CVE-2016-3709](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3709)

    * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)

    * [CVE-2024-36901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36901)

    * [CVE-2024-36938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36938)

    * [CVE-2024-41009](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41009)

    * [CVE-2024-41012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41012)

    * [CVE-2024-41055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41055)

    * [CVE-2024-41063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41063)

    * [CVE-2024-41064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41064)

    * [CVE-2024-42101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42101)

    * [CVE-2024-42102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42102)

    * [CVE-2024-42131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42131)

    * [CVE-2024-42137](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42137)

    * [CVE-2024-42152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42152)

    * [CVE-2024-42153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42153)

    * [CVE-2024-42154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42154)

    * [CVE-2024-42157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42157)

    * [CVE-2024-42161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42161)

    * [CVE-2024-42223](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42223)

    * [CVE-2024-42224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42224)

    * [CVE-2024-42229](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42229)

    * [CVE-2024-42232](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42232)

    * [CVE-2024-42236](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42236)

    * [CVE-2024-42244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42244)

    * [CVE-2024-42247](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42247)

    * [CVE-2024-7264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7264)

  * Low-severity container vulnerabilities:

    * [CVE-2022-2309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2309)

    * [CVE-2022-48303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48303)

    * [CVE-2024-41007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41007)




1.30 

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## October 01, 2024

1.29

Announcement

### Release 1.29.600-gke.108

Google Distributed Cloud for bare metal 1.29.600-gke.108 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.600-gke.108 runs on Kubernetes 1.29.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Fixed

**Fixes:**

  * Fixed Cloud Audit Logging failure due to allowlisting issue with multiple project IDs.



1.29

Fixed

The following container image security vulnerabilities have been fixed in 1.29.600-gke.108: 

  * Critical container vulnerabilities:

    * [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)

    * [CVE-2024-42154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42154)

  * High-severity container vulnerabilities:

    * [CVE-2020-22218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-22218)

    * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)

    * [CVE-2024-0567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0567)

    * [CVE-2024-37370](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37370)

    * [CVE-2024-39487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39487)

    * [CVE-2024-41040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41040)

    * [CVE-2024-41046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41046)

    * [CVE-2024-41049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41049)

    * [CVE-2024-41059](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41059)

    * [CVE-2024-41070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41070)

    * [CVE-2024-42104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42104)

    * [CVE-2024-42148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42148)

    * [CVE-2024-42161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42161)

    * [CVE-2024-42224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42224)

  * Medium-severity container vulnerabilities:

    * [CVE-2016-3709](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3709)

    * [CVE-2024-36901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36901)

    * [CVE-2024-36938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36938)

    * [CVE-2024-41009](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41009)

    * [CVE-2024-41012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41012)

    * [CVE-2024-41055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41055)

    * [CVE-2024-41063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41063)

    * [CVE-2024-41064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41064)

    * [CVE-2024-42101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42101)

    * [CVE-2024-42102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42102)

    * [CVE-2024-42131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42131)

    * [CVE-2024-42137](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42137)

    * [CVE-2024-42152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42152)

    * [CVE-2024-42153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42153)

    * [CVE-2024-42157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42157)

    * [CVE-2024-42223](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42223)

    * [CVE-2024-42229](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42229)

    * [CVE-2024-42232](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42232)

    * [CVE-2024-42236](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42236)

    * [CVE-2024-42244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42244)

    * [CVE-2024-42247](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42247)

  * Low-severity container vulnerabilities:

    * [CVE-2022-2309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2309)

    * [CVE-2024-41007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41007)




1.29

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## September 25, 2024

1.30 

Announcement

### Release 1.30.100-gke.96

Google Distributed Cloud for bare metal 1.30.100-gke.96 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.100-gke.96 runs on Kubernetes 1.30.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Change

**Functionality changes:**

  * Added `--skip-preflight` flag to the `bmctl upgrade` command to prevent preflight checks from running during an upgrade.



1.30 

Fixed

The following container image security vulnerabilities have been fixed in 1.30.100-gke.96: 

  * High-severity container vulnerabilities:

    * [CVE-2020-22218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-22218)

    * [CVE-2024-7348](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7348)

    * [GHSA-87m9-rv8p-rgmg](https://github.com/advisories/GHSA-87m9-rv8p-rgmg)

  * Medium-severity container vulnerabilities:

    * [CVE-2024-6104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6104)

    * [GHSA-mh55-gqvf-xfwm](https://github.com/advisories/GHSA-mh55-gqvf-xfwm)




1.30 

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## September 23, 2024

1.28

Announcement

### Release 1.28.1000-gke.60

Google Distributed Cloud for bare metal 1.28.1000-gke.60 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.1000-gke.60 runs on Kubernetes 1.28.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Fixed

**Fixes:**

  * Fixed Cloud Audit Logging failure due to allowlisting issue with multiple project IDs.



1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.1000-gke.60: 

  * Critical container vulnerabilities:

    * [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)
  * High-severity container vulnerabilities:

    * [CVE-2020-22218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-22218)

    * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)

    * [CVE-2024-0567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0567)

    * [CVE-2024-37370](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37370)

    * [GHSA-87m9-rv8p-rgmg](https://github.com/advisories/GHSA-87m9-rv8p-rgmg)

  * Medium-severity container vulnerabilities:

    * [CVE-2024-6104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6104)

    * [GHSA-mh55-gqvf-xfwm](https://github.com/advisories/GHSA-mh55-gqvf-xfwm)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## September 12, 2024

1.29

Announcement

### Release 1.29.500-gke.163

Google Distributed Cloud for bare metal 1.29.500-gke.163 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.500-gke.163 runs on Kubernetes v1.29.7-gke.1200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Fixed

The following container image security vulnerabilities have been fixed in 1.29.500-gke.163: 

  * High-severity container vulnerabilities:

    * [CVE-2024-7348](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7348)
    * [GHSA-87m9-rv8p-rgmg](https://github.com/advisories/GHSA-87m9-rv8p-rgmg)
    * [CVE-2023-47038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47038)
  * Medium-severity container vulnerabilities:

    * [CVE-2024-6104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6104)
    * [GHSA-mh55-gqvf-xfwm](https://github.com/advisories/GHSA-mh55-gqvf-xfwm)
    * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)
  * Low-severity container vulnerabilities:

    * [CVE-2022-48303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48303)



1.29

Issue

**Known issues** :

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## August 29, 2024

1.30 

Announcement

### Release 1.30.0-gke.1930

Google Distributed Cloud for bare metal 1.30.0-gke.1930 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.0-gke.1930 runs on Kubernetes 1.30.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Announcement

### Release 1.28.900-gke.112

Google Distributed Cloud for bare metal 1.28.900-gke.112 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.900-gke.112 runs on Kubernetes 1.28.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.30 

Announcement

**Version 1.16 end of life** : In accordance with the [Version Support Policy](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#version-support), version 1.16 (all patch releases) of Google Distributed Cloud for bare metal has reached its end of life and is no longer supported.

1.28

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.28.900-gke.112: 

  * High-severity container vulnerabilities:

    * [CVE-2019-16884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16884)

    * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)

    * [CVE-2021-33194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33194)

    * [CVE-2021-38561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38561)

    * [CVE-2021-43565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43565)

    * [CVE-2021-43816](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43816)

    * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)

    * [CVE-2022-27191](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27191)

    * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)

    * [CVE-2022-32149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32149)

    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)

    * [CVE-2022-43945](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43945)

    * [CVE-2023-47038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47038)

    * [CVE-2024-7348](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7348)

    * [CVE-2024-36971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36971)

    * [CVE-2024-36978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36978)

    * [CVE-2024-38583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38583)

    * [CVE-2024-39480](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39480)

    * [CVE-2024-39495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39495)

    * [CVE-2024-40902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40902)

    * [CVE-2024-41000](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41000)

    * [CVE-2024-41087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41087)

    * [CVE-2024-41092](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41092)

    * [CVE-2024-42093](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42093)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-19921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19921)

    * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)

    * [CVE-2021-32760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32760)

    * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)

    * [CVE-2021-43784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43784)

    * [CVE-2022-23471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23471)

    * [CVE-2022-29162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29162)

    * [CVE-2022-29526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29526)

    * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)

    * [CVE-2023-25153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25153)

    * [CVE-2023-25173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25173)

    * [CVE-2023-28642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28642)

    * [CVE-2023-48795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)

    * [CVE-2024-27019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27019)

    * [CVE-2024-36288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36288)

    * [CVE-2024-37370](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37370)

    * [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)

    * [CVE-2024-38662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38662)

    * [CVE-2024-38780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38780)

    * [CVE-2024-39292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39292)

    * [CVE-2024-39475](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39475)

    * [CVE-2024-39476](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39476)

    * [CVE-2024-39482](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39482)

    * [CVE-2024-39484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39484)

    * [CVE-2024-39489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39489)

    * [CVE-2024-39493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39493)

    * [CVE-2024-40960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40960)

    * [CVE-2024-40961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40961)

    * [CVE-2024-40995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40995)

    * [CVE-2024-41006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41006)

    * [CVE-2024-41089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41089)

    * [CVE-2024-41095](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41095)

    * [CVE-2024-41097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41097)

    * [CVE-2024-42070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42070)

    * [CVE-2024-42076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42076)

    * [CVE-2024-42077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42077)

    * [CVE-2024-42082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42082)

    * [CVE-2024-42090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42090)

    * [GHSA-7ww5-4wqc-m92c](https://github.com/advisories/GHSA-7ww5-4wqc-m92c)

  * Low-severity container vulnerabilities:

    * [CVE-2022-48303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48303)

    * [CVE-2023-25809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25809)

    * [CVE-2024-2511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2511)

    * [CVE-2024-4741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4741)

    * [CVE-2024-5535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5535)

    * [GHSA-5j5w-g665-5m35](https://github.com/advisories/GHSA-5j5w-g665-5m35)

    * [GHSA-77vh-xpmg-72qh](https://github.com/advisories/GHSA-77vh-xpmg-72qh)

    * [GHSA-c9cp-9c75-9v8c](https://github.com/advisories/GHSA-c9cp-9c75-9v8c)




1.30 

Feature

**New and updated features:**

  * **Preview:** Added support for keyless mode for clusters. This feature uses short-lived tokens and Workload Identity Federation for your cluster and workload credentials, instead of the default long-lived service account keys and Kubernetes Secrets. This feature provides improved security and reduces credential maintenance.

  * **Preview:** Added support for Custom Scheduler Configuration for pods to automatically spread workloads across cluster nodes for increased reliability.

  * **GA:** Added support for admin and hybrid clusters to manage multiple versions of user clusters concurrently.

  * **GA:** Added support for [node-level private registry configuration](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-node-private-reg) for workload images. 

  * **GA:** Updated the `bmctl update` command to display the difference between the specs in the YAML cluster configuration file and the deployed Cluster resource. The diff covers the specs for both the Cluster resource and the NodePool resource.

  * **GA:** Added support for rolling back [select node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#select_np_up).

  * **GA:** Added support for specifying a session duration for Identity Service-issued tokens. You can set a session duration between 15 and 1440 minutes (24 hours). Shorter sessions provide better security (at the cost of more frequent reauthentication). Longer sessions reduce the frequency for reauthentication (at the cost of reduced security). 

  * **Preview:** Updated the `gcloud beta container fleet memberships get-credentials command` to use a connect gateway preview feature that lets you run the `kubectl attach`, `cp`, and `exec` commands. For more information, see [Limitations](https://cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#limitations).




1.30 

Fixed

**Fixes:**

  * Fixed an issue where old, inoperable WebHook resources caused problems with cluster upgrades.

  * Fixed an issue where upgraded clusters didn't get label updates that match the labels applied for newly created clusters, for a given version.

  * Fixed an issue where service accounts created by using the `--create-service-accounts` flag with the `bmctl create config` command don't have enough permissions.

  * Fixed an issue where the kubelet doesn't honor shortened, 1-second grace period for pod deletion during eviction-based draining.




1.30 

Change

**Functionality changes:**

  * Updated the node pool upgrade behavior. Version 1.30 and higher clusters, support all node pool versions from the preceding two minor versions. The `preview.baremetal.cluster.gke.io/two-minor-version-node-pool: enable` annotation isn't required when upgrading clusters from version 1.29 to version 1.30.

  * Updated the `bmctl version` command to return the metadata image digest in the response. To print only the metadata image digest only, specify the new `--option` value `metadata-digest`.

  * Deprecated the `spec.gkeVersion` field in the `Machine` custom resource. Starting with version 1.30.0, the `spec.gkeVersion` field is set to empty. For accurate version information, use `anthosBareMetalVersion` (GDC for bare metal version) in the `Cluster` resource spec or `gkeVersion` (Kubernetes version) in the `Cluster` resource status.

  * Updated Kubernetes audit logging to include request and response payloads from the Kubernetes API server for bare metal custom resources, such as `Cluster`, `NodePool`, `BareMetalMachine`, and `BareMetalCluster`.

  * Updated registry mirror support to allow you to specify a port for host addresses.

  * Updated the networking preflight check to verify that either the `ip_tables` or the `nf_tables` kernel module is available for loading, instead of being explicitly loaded.

  * Updated the `stackdriver` custom resource to remove the feature gate for using Managed Service for Prometheus for system metrics `featureGates.GMPForSystemMetrics`. This feature gate has defaulted to on (`true`) since version 1.16. If you have manually disabled using Managed Service for Prometheus for system metrics, upgrading to version 1.30 might be a breaking change for some system metrics formats. **The field name in this note is incorrect, it should be`enableGMPForSystemMetrics`, instead of `GMPForSystemMetrics`; see updated entry for March 25, 2025.**

  * Added checks to validate the SSH client certificate file type before saving the certificate as a Secret.

  * Updated GKE Identity Service custom resource definition to change the description for `IdentityServiceOptions` and improve formatting.

  * Added preflight checks for available disk space in specific directories:

    * During cluster creation, the following directories are checked:

      * `/` (the root directory) has at least 4 GiB of free space

      * `/var/log/fluent-bit-buffers` has at least 12 GiB of free space

      * `/var/opt/buffered-metrics` has at least 10016 MiB of free space

    * During a cluster upgrade, the following directory is checked:

      * `/` (the root directory) has at least 2 GiB of free space
  * **GA:** Adopted the GKE audit policy, instead of the previous unpopulated policy.




1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.30 

Fixed

The following container image security vulnerabilities have been fixed in 1.30.0-gke.1930: 

  * High-severity container vulnerabilities:

    * [CVE-2019-16884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16884)

    * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)

    * [CVE-2021-33194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33194)

    * [CVE-2021-38561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38561)

    * [CVE-2021-43565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43565)

    * [CVE-2021-43816](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43816)

    * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)

    * [CVE-2022-27191](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27191)

    * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)

    * [CVE-2022-32149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32149)

    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)

    * [CVE-2022-43945](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43945)

    * [CVE-2022-48655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48655)

    * [CVE-2023-6270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6270)

    * [CVE-2023-39323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39323)

    * [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)

    * [CVE-2023-45287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45287)

    * [CVE-2023-52434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52434)

    * [CVE-2023-52447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52447)

    * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)

    * [CVE-2024-0841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0841)

    * [CVE-2024-0985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0985)

    * [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626)

    * [CVE-2024-26581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26581)

    * [CVE-2024-26593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26593)

    * [CVE-2024-26882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26882)

    * [CVE-2024-26883](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26883)

    * [CVE-2024-26884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26884)

    * [CVE-2024-26885](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26885)

    * [CVE-2024-26898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26898)

    * [CVE-2024-26907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26907)

    * [CVE-2024-26934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26934)

    * [CVE-2024-27020](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27020)

    * [CVE-2024-36971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36971)

    * [CVE-2024-36978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36978)

    * [CVE-2024-38583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38583)

    * [CVE-2024-39480](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39480)

    * [CVE-2024-39495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39495)

    * [CVE-2024-40902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40902)

    * [CVE-2024-41000](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41000)

    * [CVE-2024-41087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41087)

    * [CVE-2024-41092](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41092)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-19921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19921)

    * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)

    * [CVE-2021-32760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32760)

    * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)

    * [CVE-2021-43784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43784)

    * [CVE-2022-23471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23471)

    * [CVE-2022-29162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29162)

    * [CVE-2022-29526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29526)

    * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)

    * [CVE-2022-38096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38096)

    * [CVE-2022-40735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40735)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-7042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7042)

    * [CVE-2023-25153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25153)

    * [CVE-2023-25173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25173)

    * [CVE-2023-28642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28642)

    * [CVE-2023-39318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39318)

    * [CVE-2023-39319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39319)

    * [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)

    * [CVE-2023-47233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47233)

    * [CVE-2023-48795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)

    * [CVE-2023-52429](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52429)

    * [CVE-2023-52435](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52435)

    * [CVE-2023-52458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52458)

    * [CVE-2024-0340](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0340)

    * [CVE-2024-0607](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0607)

    * [CVE-2024-2961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2961)

    * [CVE-2024-22099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22099)

    * [CVE-2024-23849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23849)

    * [CVE-2024-23850](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23850)

    * [CVE-2024-23851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23851)

    * [CVE-2024-24857](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24857)

    * [CVE-2024-24858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24858)

    * [CVE-2024-24861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24861)

    * [CVE-2024-25739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25739)

    * [CVE-2024-26600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26600)

    * [CVE-2024-26601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26601)

    * [CVE-2024-26602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26602)

    * [CVE-2024-26606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26606)

    * [CVE-2024-26900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26900)

    * [CVE-2024-26901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26901)

    * [CVE-2024-26903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26903)

    * [CVE-2024-26910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26910)

    * [CVE-2024-26978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26978)

    * [CVE-2024-27013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27013)

    * [CVE-2024-27019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27019)

    * [CVE-2024-28122](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28122)

    * [CVE-2024-28182](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28182)

    * [CVE-2024-33599](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33599)

    * [CVE-2024-33600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33600)

    * [CVE-2024-33601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33601)

    * [CVE-2024-33602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33602)

    * [CVE-2024-35255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35255)

    * [CVE-2024-35978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35978)

    * [CVE-2024-35982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35982)

    * [CVE-2024-35984](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35984)

    * [CVE-2024-35990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35990)

    * [CVE-2024-35997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35997)

    * [CVE-2024-36008](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36008)

    * [CVE-2024-36288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36288)

    * [CVE-2024-36902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36902)

    * [CVE-2024-37370](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37370)

    * [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)

    * [CVE-2024-38662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38662)

    * [CVE-2024-38780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38780)

    * [CVE-2024-39292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39292)

    * [CVE-2024-39475](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39475)

    * [CVE-2024-39476](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39476)

    * [CVE-2024-39482](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39482)

    * [CVE-2024-39484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39484)

    * [CVE-2024-39489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39489)

    * [CVE-2024-39493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39493)

    * [CVE-2024-40960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40960)

    * [CVE-2024-40961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40961)

    * [CVE-2024-40995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40995)

    * [CVE-2024-41006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41006)

    * [CVE-2024-41089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41089)

    * [CVE-2024-41095](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41095)

    * [CVE-2024-42070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42070)

    * [CVE-2024-42076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42076)

    * [CVE-2024-42077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42077)

    * [CVE-2024-42082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42082)

    * [GHSA-6xv5-86q9-7xr8](https://github.com/advisories/GHSA-6xv5-86q9-7xr8)

    * [GHSA-7ww5-4wqc-m92c](https://github.com/advisories/GHSA-7ww5-4wqc-m92c)

  * Low-severity container vulnerabilities:

    * [CVE-2021-4440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4440)

    * [CVE-2023-5363](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5363)

    * [CVE-2023-6246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6246)

    * [CVE-2023-6779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6779)

    * [CVE-2023-6780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6780)

    * [CVE-2023-25809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25809)

    * [CVE-2024-2511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2511)

    * [CVE-2024-4741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4741)

    * [CVE-2024-5535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5535)

    * [GHSA-5j5w-g665-5m35](https://github.com/advisories/GHSA-5j5w-g665-5m35)

    * [GHSA-77vh-xpmg-72qh](https://github.com/advisories/GHSA-77vh-xpmg-72qh)

    * [GHSA-c9cp-9c75-9v8c](https://github.com/advisories/GHSA-c9cp-9c75-9v8c)




1.30 

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## August 26, 2024

1.16

Announcement

### Release 1.16.12

Google Distributed Cloud for bare metal 1.16.12 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.12 runs on Kubernetes 1.27.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.12: 

  * High-severity container vulnerabilities:

    * [CVE-2019-16884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16884)

    * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)

    * [CVE-2021-33194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33194)

    * [CVE-2021-38561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38561)

    * [CVE-2021-43565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43565)

    * [CVE-2021-43816](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43816)

    * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)

    * [CVE-2022-27191](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27191)

    * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)

    * [CVE-2022-32149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32149)

    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)

    * [CVE-2022-43945](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43945)

    * [CVE-2023-47038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47038)

    * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)

    * [CVE-2024-0567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0567)

    * [CVE-2024-7348](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7348)

    * [CVE-2024-36971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36971)

    * [CVE-2024-36978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36978)

    * [CVE-2024-38583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38583)

    * [CVE-2024-39480](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39480)

    * [CVE-2024-39495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39495)

    * [CVE-2024-40902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40902)

    * [CVE-2024-41087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41087)

    * [CVE-2024-41092](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41092)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-19921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19921)

    * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)

    * [CVE-2021-32760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32760)

    * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)

    * [CVE-2021-43784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43784)

    * [CVE-2022-23471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23471)

    * [CVE-2022-29162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29162)

    * [CVE-2022-29526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29526)

    * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)

    * [CVE-2023-25153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25153)

    * [CVE-2023-25173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25173)

    * [CVE-2023-28642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28642)

    * [CVE-2023-48795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)

    * [CVE-2024-27019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27019)

    * [CVE-2024-36288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36288)

    * [CVE-2024-38662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38662)

    * [CVE-2024-38780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38780)

    * [CVE-2024-39292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39292)

    * [CVE-2024-39475](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39475)

    * [CVE-2024-39476](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39476)

    * [CVE-2024-39482](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39482)

    * [CVE-2024-39484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39484)

    * [CVE-2024-39489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39489)

    * [CVE-2024-39493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39493)

    * [CVE-2024-41089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41089)

    * [CVE-2024-41095](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41095)

    * [CVE-2024-42070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42070)

    * [CVE-2024-42076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42076)

    * [CVE-2024-42077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42077)

    * [CVE-2024-42082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42082)

    * [GHSA-7ww5-4wqc-m92c](https://github.com/advisories/GHSA-7ww5-4wqc-m92c)

  * Low-severity container vulnerabilities:

    * [CVE-2022-27943](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27943)

    * [CVE-2022-48303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48303)

    * [CVE-2023-25809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25809)

    * [GHSA-5j5w-g665-5m35](https://github.com/advisories/GHSA-5j5w-g665-5m35)

    * [GHSA-77vh-xpmg-72qh](https://github.com/advisories/GHSA-77vh-xpmg-72qh)

    * [GHSA-c9cp-9c75-9v8c](https://github.com/advisories/GHSA-c9cp-9c75-9v8c)

    * [GHSA-xr7q-jx4m-x55m](https://github.com/advisories/GHSA-xr7q-jx4m-x55m)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## August 08, 2024

1.29

Announcement

### Release 1.29.400-gke.86

Google Distributed Cloud for bare metal 1.29.400-gke.86 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.400-gke.86 runs on Kubernetes 1.29.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Feature

  * **GA** : Added support in version 1.29.400-gke.86 and higher for Red Hat Enterprise Linux (RHEL) version 9.2. For more information, see [Select your operating system](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs#1.29).



1.29

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.29.400-gke.86: 

Fixed the following vulnerabilities:

  * High-severity container vulnerabilities:

    * [CVE-2019-16884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16884)

    * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)

    * [CVE-2021-33194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33194)

    * [CVE-2021-38561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38561)

    * [CVE-2021-43565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43565)

    * [CVE-2021-43816](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43816)

    * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)

    * [CVE-2022-27191](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27191)

    * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)

    * [CVE-2022-32149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32149)

    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)

    * [CVE-2022-43945](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43945)

    * [CVE-2024-36971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36971)

    * [CVE-2024-38583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38583)

    * [CVE-2024-39480](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39480)

    * [CVE-2024-39495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39495)

    * [CVE-2024-40902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40902)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-19921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19921)

    * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)

    * [CVE-2021-32760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32760)

    * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)

    * [CVE-2021-43784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43784)

    * [CVE-2022-23471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23471)

    * [CVE-2022-29162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29162)

    * [CVE-2022-29526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29526)

    * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)

    * [CVE-2022-40735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40735)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-25153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25153)

    * [CVE-2023-25173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25173)

    * [CVE-2023-28642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28642)

    * [CVE-2023-48795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)

    * [CVE-2024-27019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27019)

    * [CVE-2024-36288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36288)

    * [CVE-2024-38662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38662)

    * [CVE-2024-38780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38780)

    * [CVE-2024-39292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39292)

    * [CVE-2024-39475](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39475)

    * [CVE-2024-39476](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39476)

    * [CVE-2024-39482](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39482)

    * [CVE-2024-39484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39484)

    * [CVE-2024-39489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39489)

    * [CVE-2024-39493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39493)

    * [CVE-2024-42070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42070)

    * [CVE-2024-42076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42076)

    * [CVE-2024-42077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42077)

    * [CVE-2024-42082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42082)

    * [GHSA-7ww5-4wqc-m92c](https://github.com/advisories/GHSA-7ww5-4wqc-m92c)

  * Low-severity container vulnerabilities:

    * [CVE-2023-25809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25809)

    * [GHSA-5j5w-g665-5m35](https://github.com/advisories/GHSA-5j5w-g665-5m35)

    * [GHSA-77vh-xpmg-72qh](https://github.com/advisories/GHSA-77vh-xpmg-72qh)

    * [GHSA-c9cp-9c75-9v8c](https://github.com/advisories/GHSA-c9cp-9c75-9v8c)




1.29

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## August 01, 2024

1.28

Announcement

### Release 1.28.800-gke.111

Google Distributed Cloud for bare metal 1.28.800-gke.111 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.800-gke.111 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Change

**Functionality changes:**

  * Updated Kubernetes audit logging to include request and response payloads from the Kubernetes API server for bare metal custom resources, including the following: `Cluster`, `NodePool`, `BareMetalMachine` and `BareMetalCluster`.



1.28

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.28.800-gke.111: 

  * Medium-severity container vulnerabilities:

    * [CVE-2024-33599](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33599)

    * [CVE-2024-33600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33600)

    * [CVE-2024-33601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33601)

    * [CVE-2024-33602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33602)

    * [CVE-2024-35255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35255)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 25, 2024

1.29

Announcement

### Release 1.29.300-gke.185

Google Distributed Cloud for bare metal 1.29.300-gke.185 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.300-gke.185 runs on Kubernetes 1.29.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.16

Announcement

### Release 1.16.11

Google Distributed Cloud for bare metal 1.16.11 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.11 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Change

**Functionality changes:**

  * Updated registry mirror support to allow you to specify a port for host addresses.

  * Updated Kubernetes audit logging to include request and response payloads from the Kubernetes API server for bare metal custom resources, such as `Cluster`, `NodePool`, `BareMetalMachine`, and `BareMetalCluster`.




1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.11: 

  * High-severity container vulnerabilities:

    * [CVE-2020-22218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-22218)
  * Medium-severity container vulnerabilities:

    * [CVE-2024-35255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35255)



1.29

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.29.300-gke.185: 

  * High-severity container vulnerabilities:

    * [CVE-2022-48655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48655)
  * Medium-severity container vulnerabilities:

    * [CVE-2024-26900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26900)

    * [CVE-2024-28122](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28122)

    * [CVE-2024-35255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35255)

    * [CVE-2024-36902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36902)

  * Low-severity container vulnerabilities:

    * [CVE-2021-4440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4440)



1.16

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

1.29

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 09, 2024

1.28

Announcement

### Release 1.28.700-gke.150

Google Distributed Cloud for bare metal 1.28.700-gke.150 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.700-gke.150 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Fixed

**Fixes:**

  * Fixed an issue where upgraded clusters didn't get label updates that match the labels applied for newly created clusters, for a given version.



1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.700-gke.150: 

  * High-severity container vulnerabilities:

    * [CVE-2022-48655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48655)

    * [CVE-2024-0985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0985)

  * Medium-severity container vulnerabilities:

    * [CVE-2024-26900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26900)

    * [CVE-2024-28122](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28122)

    * [CVE-2024-36902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36902)

    * [GHSA-6xv5-86q9-7xr8](https://github.com/advisories/GHSA-6xv5-86q9-7xr8)

  * Low-severity container vulnerabilities:

    * [CVE-2021-4440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4440)



1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 03, 2024

1.29

Security

### Security bulletin (all minor versions)

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that can be used to obtain access to a remote shell, enabling attackers to gain root access. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts. This vulnerability has a Critical severity.

For mitigation steps and more details, see the [GCP-2024-040](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040) security bulletin.

1.28

Security

### Security bulletin (all minor versions)

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that can be used to obtain access to a remote shell, enabling attackers to gain root access. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts. This vulnerability has a Critical severity.

For mitigation steps and more details, see the [GCP-2024-040](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040) security bulletin.

1.16

Security

### Security bulletin (all minor versions)

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that can be used to obtain access to a remote shell, enabling attackers to gain root access. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts. This vulnerability has a Critical severity.

For mitigation steps and more details, see the [GCP-2024-040](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040) security bulletin.

## July 01, 2024

1.16

Announcement

### Release 1.16.10

Google Distributed Cloud for bare metal 1.16.10 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.10 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.16

Fixed

**Fixes:**

  * Fixed an issue where upgraded clusters didn't get label updates that match the labels applied for newly created clusters, for a given version.



1.16

Change

The following container image security vulnerabilities have been fixed in 1.16.10: 

  * High-severity container vulnerabilities:

    * [CVE-2023-6270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6270)

    * [CVE-2023-52434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52434)

    * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)

    * [CVE-2024-0985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0985)

    * [CVE-2024-26882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26882)

    * [CVE-2024-26883](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26883)

    * [CVE-2024-26884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26884)

    * [CVE-2024-26898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26898)

    * [CVE-2024-26907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26907)

    * [CVE-2024-26934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26934)

    * [CVE-2024-27020](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27020)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-7042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7042)

    * [CVE-2023-47233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47233)

    * [CVE-2023-52429](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52429)

    * [CVE-2023-52435](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52435)

    * [CVE-2023-52458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52458)

    * [CVE-2024-0340](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0340)

    * [CVE-2024-0607](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0607)

    * [CVE-2024-22099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22099)

    * [CVE-2024-23849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23849)

    * [CVE-2024-23851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23851)

    * [CVE-2024-24857](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24857)

    * [CVE-2024-24858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24858)

    * [CVE-2024-24861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24861)

    * [CVE-2024-25739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25739)

    * [CVE-2024-26600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26600)

    * [CVE-2024-26602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26602)

    * [CVE-2024-26606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26606)

    * [CVE-2024-26901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26901)

    * [CVE-2024-26903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26903)

    * [CVE-2024-26910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26910)

    * [CVE-2024-27013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27013)

    * [CVE-2024-28122](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28122)

    * [CVE-2024-28182](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28182)

    * [CVE-2024-32473](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32473)

    * [CVE-2024-35978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35978)

    * [CVE-2024-35982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35982)

    * [CVE-2024-35984](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35984)

    * [CVE-2024-35997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35997)

    * [CVE-2024-36902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36902)

    * [GHSA-6xv5-86q9-7xr8](https://github.com/advisories/GHSA-6xv5-86q9-7xr8)

  * Low-severity container vulnerabilities:

    * [CVE-2021-4440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4440)

    * [CVE-2022-38096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38096)

    * [CVE-2022-48655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48655)

    * [CVE-2023-52447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52447)

    * [CVE-2023-52489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52489)

    * [CVE-2023-52492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52492)

    * [CVE-2023-52493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52493)

    * [CVE-2023-52497](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52497)

    * [CVE-2023-52616](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52616)

    * [CVE-2023-52627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52627)

    * [CVE-2023-52637](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52637)

    * [CVE-2023-52672](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52672)

    * [CVE-2024-0841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0841)

    * [CVE-2024-23850](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23850)

    * [CVE-2024-26581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26581)

    * [CVE-2024-26593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26593)

    * [CVE-2024-26601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26601)

    * [CVE-2024-26610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26610)

    * [CVE-2024-26627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26627)

    * [CVE-2024-26643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26643)

    * [CVE-2024-26665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26665)

    * [CVE-2024-26673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26673)

    * [CVE-2024-26684](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26684)

    * [CVE-2024-26688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26688)

    * [CVE-2024-26695](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26695)

    * [CVE-2024-26698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26698)

    * [CVE-2024-26702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26702)

    * [CVE-2024-26707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26707)

    * [CVE-2024-26712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26712)

    * [CVE-2024-26727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26727)

    * [CVE-2024-26748](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26748)

    * [CVE-2024-26749](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26749)

    * [CVE-2024-26753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26753)

    * [CVE-2024-26781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26781)

    * [CVE-2024-26782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26782)

    * [CVE-2024-26787](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26787)

    * [CVE-2024-26788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26788)

    * [CVE-2024-26790](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26790)

    * [CVE-2024-26795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26795)

    * [CVE-2024-26808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26808)

    * [CVE-2024-26809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26809)

    * [CVE-2024-26814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26814)

    * [CVE-2024-26833](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26833)

    * [CVE-2024-26835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26835)

    * [CVE-2024-26848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26848)

    * [CVE-2024-26855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26855)

    * [CVE-2024-26861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26861)

    * [CVE-2024-26862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26862)

    * [CVE-2024-26870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26870)

    * [CVE-2024-26877](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26877)

    * [CVE-2024-26885](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26885)

    * [CVE-2024-26891](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26891)

    * [CVE-2024-26895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26895)

    * [CVE-2024-26897](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26897)

    * [CVE-2024-26900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26900)

    * [CVE-2024-26924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26924)

    * [CVE-2024-26925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26925)

    * [CVE-2024-26926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26926)

    * [CVE-2024-26935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26935)

    * [CVE-2024-26937](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26937)

    * [CVE-2024-26950](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26950)

    * [CVE-2024-26951](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26951)

    * [CVE-2024-26970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26970)

    * [CVE-2024-26978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26978)

    * [CVE-2024-26988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26988)

    * [CVE-2024-27030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27030)

    * [CVE-2024-27038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27038)

    * [CVE-2024-27044](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27044)

    * [CVE-2024-27045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27045)

    * [CVE-2024-27047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27047)

    * [CVE-2024-27052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27052)

    * [CVE-2024-27053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27053)

    * [CVE-2024-27065](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27065)

    * [CVE-2024-27076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27076)

    * [CVE-2024-27414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27414)

    * [CVE-2024-27417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27417)

    * [CVE-2024-27431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27431)

    * [CVE-2024-35785](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35785)

    * [CVE-2024-35796](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35796)

    * [CVE-2024-35813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35813)

    * [CVE-2024-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35829)

    * [CVE-2024-35833](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35833)

    * [CVE-2024-35845](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35845)

    * [CVE-2024-35848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35848)

    * [CVE-2024-35852](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35852)

    * [CVE-2024-35853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35853)

    * [CVE-2024-35854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35854)

    * [CVE-2024-35855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35855)

    * [CVE-2024-35879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35879)

    * [CVE-2024-35884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35884)

    * [CVE-2024-35895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35895)

    * [CVE-2024-35897](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35897)

    * [CVE-2024-35899](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35899)

    * [CVE-2024-35900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35900)

    * [CVE-2024-35905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35905)

    * [CVE-2024-35958](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35958)

    * [CVE-2024-35962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35962)

    * [CVE-2024-35983](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35983)

    * [CVE-2024-35988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35988)

    * [CVE-2024-35990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35990)

    * [CVE-2024-35996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35996)

    * [CVE-2024-36005](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36005)

    * [CVE-2024-36006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36006)

    * [CVE-2024-36007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36007)

    * [CVE-2024-36008](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36008)

    * [CVE-2024-36031](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36031)

    * [CVE-2024-36889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36889)

    * [CVE-2024-36929](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36929)

    * [CVE-2024-36957](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36957)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## June 27, 2024

1.29

Announcement

### Release 1.29.200-gke.243

Google Distributed Cloud for bare metal 1.29.200-gke.243 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.29.200-gke.243 runs on Kubernetes 1.29.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.29

Change

**Functionality changes:**

  * Updated registry mirror support to allow you to specify a port for host addresses.

  * Updated the networking preflight check to verify that either the `ip_tables` or the `nf_tables` kernel module is available for loading, instead of being explicitly loaded.

  * Added support for Red Hat Enterprise Linux 8.10 for Google Distributed Cloud software version 1.29.200-gke.243 and higher.




1.29

Fixed

The following container image security vulnerabilities have been fixed in 1.29.200-gke.243 

  * High-severity container vulnerabilities:

    * [CVE-2023-6270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6270)

    * [CVE-2023-39323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39323)

    * [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)

    * [CVE-2023-45287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45287)

    * [CVE-2023-52434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52434)

    * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)

    * [CVE-2024-0985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0985)

    * [CVE-2024-26882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26882)

    * [CVE-2024-26883](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26883)

    * [CVE-2024-26884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26884)

    * [CVE-2024-26898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26898)

    * [CVE-2024-26907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26907)

    * [CVE-2024-26934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26934)

    * [CVE-2024-27020](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27020)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-7042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7042)

    * [CVE-2023-39318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39318)

    * [CVE-2023-39319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39319)

    * [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)

    * [CVE-2023-47233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47233)

    * [CVE-2023-52429](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52429)

    * [CVE-2023-52435](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52435)

    * [CVE-2023-52458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52458)

    * [CVE-2024-0340](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0340)

    * [CVE-2024-0607](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0607)

    * [CVE-2024-22099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22099)

    * [CVE-2024-23849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23849)

    * [CVE-2024-23851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23851)

    * [CVE-2024-24857](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24857)

    * [CVE-2024-24858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24858)

    * [CVE-2024-24861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24861)

    * [CVE-2024-25739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25739)

    * [CVE-2024-26600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26600)

    * [CVE-2024-26602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26602)

    * [CVE-2024-26606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26606)

    * [CVE-2024-26901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26901)

    * [CVE-2024-26903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26903)

    * [CVE-2024-26910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26910)

    * [CVE-2024-27013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27013)

    * [CVE-2024-33599](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33599)

    * [CVE-2024-33600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33600)

    * [CVE-2024-33601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33601)

    * [CVE-2024-33602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33602)

    * [CVE-2024-35978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35978)

    * [CVE-2024-35982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35982)

    * [CVE-2024-35984](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35984)

    * [CVE-2024-35997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35997)

    * [GHSA-6xv5-86q9-7xr8](https://github.com/advisories/GHSA-6xv5-86q9-7xr8)

  * Low-severity container vulnerabilities:

    * [CVE-2022-38096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38096)

    * [CVE-2023-5363](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5363)

    * [CVE-2023-6246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6246)

    * [CVE-2023-6779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6779)

    * [CVE-2023-6780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6780)

    * [CVE-2023-52447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52447)

    * [CVE-2023-52489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52489)

    * [CVE-2023-52492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52492)

    * [CVE-2023-52493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52493)

    * [CVE-2023-52497](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52497)

    * [CVE-2023-52616](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52616)

    * [CVE-2023-52627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52627)

    * [CVE-2023-52637](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52637)

    * [CVE-2023-52672](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52672)

    * [CVE-2024-0841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0841)

    * [CVE-2024-23850](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23850)

    * [CVE-2024-26581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26581)

    * [CVE-2024-26593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26593)

    * [CVE-2024-26601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26601)

    * [CVE-2024-26610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26610)

    * [CVE-2024-26627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26627)

    * [CVE-2024-26643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26643)

    * [CVE-2024-26665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26665)

    * [CVE-2024-26673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26673)

    * [CVE-2024-26684](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26684)

    * [CVE-2024-26688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26688)

    * [CVE-2024-26695](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26695)

    * [CVE-2024-26698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26698)

    * [CVE-2024-26702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26702)

    * [CVE-2024-26707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26707)

    * [CVE-2024-26712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26712)

    * [CVE-2024-26727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26727)

    * [CVE-2024-26748](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26748)

    * [CVE-2024-26749](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26749)

    * [CVE-2024-26753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26753)

    * [CVE-2024-26781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26781)

    * [CVE-2024-26782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26782)

    * [CVE-2024-26787](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26787)

    * [CVE-2024-26788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26788)

    * [CVE-2024-26790](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26790)

    * [CVE-2024-26795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26795)

    * [CVE-2024-26808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26808)

    * [CVE-2024-26809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26809)

    * [CVE-2024-26814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26814)

    * [CVE-2024-26833](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26833)

    * [CVE-2024-26835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26835)

    * [CVE-2024-26848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26848)

    * [CVE-2024-26855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26855)

    * [CVE-2024-26861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26861)

    * [CVE-2024-26862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26862)

    * [CVE-2024-26870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26870)

    * [CVE-2024-26877](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26877)

    * [CVE-2024-26885](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26885)

    * [CVE-2024-26891](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26891)

    * [CVE-2024-26895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26895)

    * [CVE-2024-26897](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26897)

    * [CVE-2024-26924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26924)

    * [CVE-2024-26925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26925)

    * [CVE-2024-26926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26926)

    * [CVE-2024-26935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26935)

    * [CVE-2024-26937](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26937)

    * [CVE-2024-26950](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26950)

    * [CVE-2024-26951](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26951)

    * [CVE-2024-26970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26970)

    * [CVE-2024-26978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26978)

    * [CVE-2024-26988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26988)

    * [CVE-2024-27030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27030)

    * [CVE-2024-27038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27038)

    * [CVE-2024-27044](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27044)

    * [CVE-2024-27045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27045)

    * [CVE-2024-27047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27047)

    * [CVE-2024-27052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27052)

    * [CVE-2024-27053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27053)

    * [CVE-2024-27065](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27065)

    * [CVE-2024-27076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27076)

    * [CVE-2024-27414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27414)

    * [CVE-2024-27417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27417)

    * [CVE-2024-27431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27431)

    * [CVE-2024-35785](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35785)

    * [CVE-2024-35796](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35796)

    * [CVE-2024-35813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35813)

    * [CVE-2024-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35829)

    * [CVE-2024-35833](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35833)

    * [CVE-2024-35845](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35845)

    * [CVE-2024-35852](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35852)

    * [CVE-2024-35853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35853)

    * [CVE-2024-35854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35854)

    * [CVE-2024-35855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35855)

    * [CVE-2024-35879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35879)

    * [CVE-2024-35884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35884)

    * [CVE-2024-35895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35895)

    * [CVE-2024-35897](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35897)

    * [CVE-2024-35899](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35899)

    * [CVE-2024-35900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35900)

    * [CVE-2024-35905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35905)

    * [CVE-2024-35958](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35958)

    * [CVE-2024-35962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35962)

    * [CVE-2024-35983](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35983)

    * [CVE-2024-35988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35988)

    * [CVE-2024-35990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35990)

    * [CVE-2024-35996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35996)

    * [CVE-2024-36005](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36005)

    * [CVE-2024-36006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36006)

    * [CVE-2024-36007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36007)

    * [CVE-2024-36008](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36008)




1.29

Fixed

**Fixes:**

  * Fixed an issue where upgraded clusters didn't get label updates that match the labels applied for newly created clusters, for a given version.

  * Fixed an issue where service accounts created by using the `--create-service-accounts` flag with the `bmctl create config` command don't have enough permissions.




1.29

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## June 06, 2024

1.28

Announcement

### Release 1.28.600-gke.163

Google Distributed Cloud for bare metal 1.28.600-gke.163 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Google Distributed Cloud for bare metal 1.28.600-gke.163 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) page to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

1.28

Change

**Functionality changes:**

  * Updated preflight checks add a check for networking kernel modules (`ip_tables` or `np_tables`) and remove the `iptables` package check.

  * Added checks to validate the SSH client certificate file type before saving the certificate as a Secret.

  * Added support for Red Hat Enterprise Linux 8.10 for Google Distributed Cloud software version 1.28.600-gke.163 and higher.

  * Removed support for Red Hat Enterprise Linux 8.9 as it is beyond the [Red Hat support window](https://access.redhat.com/support/policy/updates/errata#RHEL8_and_9_Life_Cycle).




1.28

Fixed

Fixed an issue where the kubelet doesn't honor shortened, 1-second grace period for pod deletion during eviction-based draining.

1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.600-gke.163: 

  * High-severity container vulnerabilities:

    * [CVE-2023-39323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39323)

    * [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-39318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39318)

    * [CVE-2023-39319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39319)

    * [CVE-2024-2961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2961)

    * [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)

    * [CVE-2024-28182](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28182)

  * Low-severity container vulnerabilities:

    * [CVE-2023-5363](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5363)

    * [CVE-2023-6246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6246)

    * [CVE-2023-6779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6779)

    * [CVE-2023-6780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6780)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## May 28, 2024

1.29

Security

### Security bulletin (all minor versions)

A new vulnerability ([CVE-2024-4323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4323)) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected.

Google Distributed Cloud software doesn't use a vulnerable version of Fluent Bit and is unaffected.

For more information, see the [GCP-2024-031](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-031) security bulletin.

1.28

Security

### Security bulletin (all minor versions)

A new vulnerability ([CVE-2024-4323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4323)) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected.

Google Distributed Cloud software doesn't use a vulnerable version of Fluent Bit and is unaffected.

For more information, see the [GCP-2024-031](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-031) security bulletin.

1.16

Security

### Security bulletin (all minor versions)

A new vulnerability ([CVE-2024-4323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4323)) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected.

Google Distributed Cloud software doesn't use a vulnerable version of Fluent Bit and is unaffected.

For more information, see the [GCP-2024-031](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-031) security bulletin.

1.16

Announcement

### Release 1.16.9

Google Distributed Cloud for bare metal 1.16.9 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.9 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud software.

1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.9: 

  * High-severity container vulnerabilities:

    * [CVE-2023-39323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39323)

    * [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-39318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39318)

    * [CVE-2023-39319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39319)

    * [CVE-2024-2961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2961)

    * [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)

    * [CVE-2024-28085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28085)

  * Low-severity container vulnerabilities:

    * [CVE-2023-5363](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5363)

    * [CVE-2023-6246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6246)

    * [CVE-2023-6779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6779)

    * [CVE-2023-6780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6780)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## May 15, 2024

1.29

Announcement

### Release 1.29.100-gke.251

GKE on Bare Metal 1.29.100-gke.251 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). GKE on Bare Metal 1.29.100-gke.251 runs on Kubernetes 1.29.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.29

Breaking

  * Added new API and IAM role requirements for Cloud Monitoring:

    * You must enable the `kubernetesmetadata.googleapis.com` API for your project and grant the `roles/kubernetesmetadata.publisher` IAM role to the Logging and Monitoring service account (`anthos-baremetal-cloud-ops`, when created automatically). Clusters use this API as an endpoint to send Kubernetes metadata to Google Cloud. The metadata is vital for cluster monitoring, debugging, and recovery. If you [install your clusters behind a proxy](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/proxy), add `kubernetesmetadata.googleapis.com` to the list of allowed connections.

    * Due to changes in the way service accounts are checked, you must also grant the following IAM roles to the Logging and Monitoring service account:

      * `roles/monitoring.viewer`

      * `roles/serviceusage.serviceUsageViewer`

These API and IAM role requirements apply to both creating new 1.29 clusters and upgrading existing clusters to 1.29.




1.29

Change

**Functionality changes:**

  * Added checks to validate the SSH client certificate file type before saving the certificate as a Secret.

  * Deprecated the `spec.gkeVersion` field in `Machine` and `BareMetalMachine` custom resources. After GKE on Bare Metal release 1.30, the value of `gkeVersion` isn't guaranteed to be reliable.

  * Added preflight checks for available disk space in specific directories:

    * During cluster creation, the following directories are checked:

      * `/` (the root directory) has at least 4 GiB of free space

      * `/var/log/fluent-bit-buffers` has at least 12 GiB of free space

      * `/var/opt/buffered-metrics` has at least 10016 MiB of free space

    * During a cluster upgrade, the following directory is checked:

      * `/` (the root directory) has at least 2 GiB of free space



1.29

Fixed

The following container image security vulnerabilities have been fixed in 1.29.100-gke.251: 

  * Medium-severity container vulnerabilities:

    * [CVE-2024-2961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2961)

    * [CVE-2024-28182](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28182)




1.29

Fixed

**Fixes:**

  * Fixed an issue where the kubelet doesn't honor shortened, 1-second grace period for pod deletion during eviction-based draining.



1.29

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## May 02, 2024

1.28

Announcement

### Release 1.28.500-gke.120

GKE on Bare Metal 1.28.500-gke.120 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). GKE on Bare Metal 1.28.500-gke.120 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.500-gke.120: 

  * Critical container vulnerabilities:

    * [CVE-2021-38297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38297)

    * [CVE-2022-23806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23806)

    * [CVE-2023-24538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24538)

    * [CVE-2023-24540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24540)

    * [CVE-2023-29402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29402)

    * [CVE-2023-29404](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29404)

    * [CVE-2023-29405](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29405)

  * High-severity container vulnerabilities:

    * [CVE-2020-29652](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29652)

    * [CVE-2021-29923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29923)

    * [CVE-2021-33195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33195)

    * [CVE-2021-33196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33196)

    * [CVE-2021-33198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33198)

    * [CVE-2021-39293](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39293)

    * [CVE-2021-41771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41771)

    * [CVE-2021-41772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41772)

    * [CVE-2021-44716](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44716)

    * [CVE-2022-2879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2879)

    * [CVE-2022-2880](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2880)

    * [CVE-2022-21698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21698)

    * [CVE-2022-23772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23772)

    * [CVE-2022-23773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23773)

    * [CVE-2022-24675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24675)

    * [CVE-2022-24921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24921)

    * [CVE-2022-28131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28131)

    * [CVE-2022-28327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28327)

    * [CVE-2022-30580](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30580)

    * [CVE-2022-30630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30630)

    * [CVE-2022-30631](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30631)

    * [CVE-2022-30632](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30632)

    * [CVE-2022-30633](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30633)

    * [CVE-2022-30635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30635)

    * [CVE-2022-32189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32189)

    * [CVE-2022-41715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41715)

    * [CVE-2022-41724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41724)

    * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)

    * [CVE-2023-24534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24534)

    * [CVE-2023-24536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24536)

    * [CVE-2023-24537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24537)

    * [CVE-2023-24539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24539)

    * [CVE-2023-29400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29400)

    * [CVE-2023-29403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29403)

    * [CVE-2023-45287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45287)

  * Medium-severity container vulnerabilities:

    * [CVE-2020-29509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29509)

    * [CVE-2020-29511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29511)

    * [CVE-2021-33197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33197)

    * [CVE-2021-34558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34558)

    * [CVE-2021-36221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36221)

    * [CVE-2022-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1705)

    * [CVE-2022-1962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1962)

    * [CVE-2022-32148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32148)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-24532](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24532)

    * [CVE-2023-29406](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29406)

    * [CVE-2023-29409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29409)

    * [CVE-2024-26908](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26908)

    * [CVE-2024-28085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28085)

  * Low-severity container vulnerabilities:

    * [CVE-2022-30629](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30629)

    * [CVE-2023-52630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52630)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## April 29, 2024

1.29

Announcement

### Release 1.29.0-gke.1449

GKE on Bare Metal 1.29.0-gke.1449 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). GKE on Bare Metal 1.29.0-gke.1449 runs on Kubernetes 1.29.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.29

Breaking

  * Added new API and IAM role requirements for Cloud Monitoring:

    * You must enable the `kubernetesmetadata.googleapis.com` API for your project and grant the `roles/kubernetesmetadata.publisher` IAM role to the Logging and Monitoring service account (`anthos-baremetal-cloud-ops`, when created automatically). Clusters use this API as an endpoint to send Kubernetes metadata to Google Cloud. The metadata is vital for cluster monitoring, debugging, and recovery. If you [install your clusters behind a proxy](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/proxy), add `kubernetesmetadata.googleapis.com` to the list of allowed connections.

    * Due to changes in the way service accounts are checked, you must also grant the following IAM roles to the Logging and Monitoring service account:

      * `roles/monitoring.viewer`

      * `roles/serviceusage.serviceUsageViewer`

These API and IAM role requirements apply to both creating new 1.29 clusters and upgrading existing clusters to 1.29.




1.29

Announcement

**Version 1.15 end of life** : In accordance with the [Version Support Policy](https://cloud.google.com//anthos/docs/support/getting-support#version_support_policy), version 1.15 (all patch releases) of GKE on Bare Metal has reached its end of life and is no longer supported.

1.29

Fixed

**Fixes:**

  * Fixed an issue where the kubelet doesn't honor shortened, 1-second grace period for pod deletion during eviction-based draining.

  * Fixed a cluster upgrade issue where the `lifecycle-controller-deployer` Pod was unable to migrate existing GKE on Bare Metal resources to the latest API version. This issue blocked upgrades to earlier version 1.28 releases.

  * Fixed an issue with configuring a proxy for your cluster that required you to manually set `HTTPS_PROXY` and `NO_PROXY` environment variables on the admin workstation.

  * Fixed an issue where upgrades are blocked because `cluster-operator` can't delete stale, failing preflight check resources.

  * Fixed an issue where the network check ConfigMap wasn't updated when nodes were added or removed.




1.29

Feature

  * **GA** : Support [GKE Identity Service v2 capability](https://cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access#alternativeuserloginaccess) for an improved security flow when you authenticate with third-party identity solutions.

The GA offering of GKE Identity Service v2 has the following requirements and restrictions:

    * GKE Identity Service v2 now requires ports `11001` and `11002` on the control plane load balancer nodes, instead of `8443` and `8444`. Ensure these ports are open and available before you upgrade a cluster to version 1.29.0-gke.1449 and higher. If the ports aren't open, upgrade preflight checks fail.

    * GKE Identity Service v2 requires version 1.5.1 or higher of the Anthos Auth gcloud CLI component. If necessary, update the Anthos Auth component (`gcloud components update anthos-auth`). If you use the Google Cloud SDK, updating the SDK (`gcloud components update`) to version 474.0.0 or later also updates the Anthos Auth component to the required version.

    * GKE Identity Service v2 doesn't work with GKE on Bare Metal clusters with the following configurations:

      * Clusters with a single control plane node only.

      * Clusters that use control plane nodes for load balancing. That is, clusters that aren't configured with either a separate load balancing node pool or manual load balancing.

  * **GA** : Added support for skews of up to two minor versions for [selective node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade-lifecycle#np_version_rules).

  * **GA** : Added capability to [pause and resume cluster upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#pause_resume).

  * **GA** : Maintenance mode now uses eviction-based draining for nodes, instead of taint-based draining. Eviction-based draining uses the Eviction API, which honors Pod Disruption Budgets (PDBs). Draining nodes this way provides better protection against workload disruptions.

  * **Preview** : Added support for node-level private registry configuration for workload images.

  * **Preview** : Added support for rolling back [select node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#select_np_up).

  * **Preview** : Added support for admin and hybrid clusters to manage multiple versions user clusters concurrently.

  * **Preview** : Added support for using an intermediate Certificate Authority (CA) as the cluster root CA.

  * **Preview** : Added support to route workload logs to a third-party custom Kafka destination. This capability isn't enabled by default. You enable this capability in the cluster `stackdriver` resource spec by adding the `unmanagedKafkaOutputConfig` section. This section lets you specify the IP addresses of Kafka message brokers (`brokers`), topic names (`topics`), and keys to map the topics to partitions (`topicKeys`).

  * Improved command-line interface errors and [error documentation](https://cloud.google.com/distributed-cloud/docs/reference/gke-error-ref).




1.29

Change

**Functionality changes:**

  * GKE Identity Service v2 now sends extra parameters (`extraParams`) to your OIDC provider.

  * Extra node viewing permissions are added for accounts specified with the `spec.clusterSecurity.authorization.clusterViewer.gcpAccounts` field in the Cluster resource.

  * Added `Status.Available` field to `BareMetalMachine` resources to indicate whether the machine is available.

  * Updated preflight checks add a check for networking kernel modules (`ip_tables` or `np_tables`) and remove the `iptables` package check.

  * The Google plugin for the GKE Identity Service now caches the public keys based on `max-age` in `cache-control` header.




1.29

Fixed

The following container image security vulnerabilities have been fixed in version 1.29.0-gke.1449: 

  * Critical container vulnerabilities:

    * [CVE-2021-38297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38297)

    * [CVE-2022-23806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23806)

    * [CVE-2023-24538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24538)

    * [CVE-2023-24540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24540)

    * [CVE-2023-25775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25775)

    * [CVE-2023-29402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29402)

    * [CVE-2023-29404](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29404)

    * [CVE-2023-29405](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29405)

  * High-severity container vulnerabilities:

    * [CVE-2020-29652](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29652)

    * [CVE-2021-29923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29923)

    * [CVE-2021-33195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33195)

    * [CVE-2021-33196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33196)

    * [CVE-2021-33198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33198)

    * [CVE-2021-39293](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39293)

    * [CVE-2021-41771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41771)

    * [CVE-2021-41772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41772)

    * [CVE-2021-44716](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44716)

    * [CVE-2022-2879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2879)

    * [CVE-2022-2880](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2880)

    * [CVE-2022-21698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21698)

    * [CVE-2022-23772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23772)

    * [CVE-2022-23773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23773)

    * [CVE-2022-24675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24675)

    * [CVE-2022-24921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24921)

    * [CVE-2022-28131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28131)

    * [CVE-2022-28327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28327)

    * [CVE-2022-28948](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28948)

    * [CVE-2022-30580](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30580)

    * [CVE-2022-30630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30630)

    * [CVE-2022-30631](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30631)

    * [CVE-2022-30632](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30632)

    * [CVE-2022-30633](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30633)

    * [CVE-2022-30635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30635)

    * [CVE-2022-32189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32189)

    * [CVE-2022-41715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41715)

    * [CVE-2022-41724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41724)

    * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)

    * [CVE-2023-5717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5717)

    * [CVE-2023-6040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6040)

    * [CVE-2023-6356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6356)

    * [CVE-2023-6536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6536)

    * [CVE-2023-6606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6606)

    * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)

    * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)

    * [CVE-2023-24534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24534)

    * [CVE-2023-24536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24536)

    * [CVE-2023-24537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24537)

    * [CVE-2023-24539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24539)

    * [CVE-2023-29400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29400)

    * [CVE-2023-29403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29403)

    * [CVE-2023-29499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29499)

    * [CVE-2023-35827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35827)

    * [CVE-2023-46838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46838)

    * [CVE-2023-51780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51780)

    * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)

    * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)

    * [CVE-2023-52436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52436)

    * [CVE-2023-52439](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52439)

    * [CVE-2023-52444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52444)

    * [CVE-2023-52445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52445)

    * [CVE-2023-52451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52451)

    * [CVE-2023-52464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52464)

    * [CVE-2023-52469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52469)

    * [CVE-2024-1086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1086)

    * [CVE-2024-26586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26586)

    * [CVE-2024-26597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26597)

    * [CVE-2024-26598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26598)

  * Medium-severity container vulnerabilities:

    * [CVE-2020-29509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29509)

    * [CVE-2020-29511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29511)

    * [CVE-2021-33197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33197)

    * [CVE-2021-34558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34558)

    * [CVE-2021-36221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36221)

    * [CVE-2021-44879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44879)

    * [CVE-2022-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1705)

    * [CVE-2022-1962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1962)

    * [CVE-2022-32148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32148)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)

    * [CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)

    * [CVE-2023-6004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6004)

    * [CVE-2023-6121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6121)

    * [CVE-2023-6915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6915)

    * [CVE-2023-6918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6918)

    * [CVE-2023-24532](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24532)

    * [CVE-2023-29406](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29406)

    * [CVE-2023-29409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29409)

    * [CVE-2023-32611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32611)

    * [CVE-2023-32665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32665)

    * [CVE-2023-34324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34324)

    * [CVE-2023-39198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39198)

    * [CVE-2023-39804](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39804)

    * [CVE-2023-45863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45863)

    * [CVE-2023-46218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46218)

    * [CVE-2023-46343](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46343)

    * [CVE-2023-49290](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49290)

    * [CVE-2023-52443](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52443)

    * [CVE-2023-52449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52449)

    * [CVE-2023-52470](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52470)

    * [CVE-2024-21664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21664)

    * [CVE-2024-28085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28085)

    * [GHSA-2c7c-3mj9-8fqh](https://github.com/advisories/GHSA-2c7c-3mj9-8fqh)

  * Low-severity container vulnerabilities:

    * [CVE-2021-25743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25743)

    * [CVE-2022-30629](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30629)

    * [CVE-2023-26604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26604)

    * [CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)

    * [CVE-2023-5178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5178)

    * [CVE-2023-5197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5197)

    * [CVE-2023-6531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6531)

    * [CVE-2023-6817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6817)

    * [CVE-2023-46813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46813)

    * [CVE-2023-46862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46862)

    * [CVE-2023-52438](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52438)

    * [CVE-2023-52448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52448)

    * [CVE-2023-52454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52454)

    * [CVE-2023-52456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52456)

    * [CVE-2023-52457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52457)

    * [CVE-2023-52462](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52462)

    * [CVE-2023-52463](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52463)

    * [CVE-2023-52467](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52467)

    * [CVE-2023-52503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52503)

    * [CVE-2023-52513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52513)

    * [CVE-2023-52524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52524)

    * [CVE-2023-52564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52564)

    * [CVE-2023-52573](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52573)

    * [CVE-2023-52575](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52575)

    * [CVE-2024-0193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0193)

    * [CVE-2024-0641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0641)

    * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)

    * [CVE-2024-24860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24860)




1.29

Issue

**Known issues:**

  * Clusters that use bundled load balancing with BGP might have [performance degradation as the total number of Services of type `LoadBalancer` approaches 2,000](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues#perf-degrad-bgp-lb). 



For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## April 25, 2024

1.16

Announcement

### Release 1.16.8

GKE on Bare Metal 1.16.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.8 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.8: 

  * Critical container vulnerabilities:

    * [CVE-2021-38297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38297)

    * [CVE-2022-23806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23806)

    * [CVE-2023-24538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24538)

    * [CVE-2023-24540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24540)

    * [CVE-2023-29402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29402)

    * [CVE-2023-29404](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29404)

    * [CVE-2023-29405](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29405)

  * High-severity container vulnerabilities:

    * [CVE-2020-29652](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29652)

    * [CVE-2021-29923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29923)

    * [CVE-2021-33195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33195)

    * [CVE-2021-33196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33196)

    * [CVE-2021-33198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33198)

    * [CVE-2021-39293](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39293)

    * [CVE-2021-41771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41771)

    * [CVE-2021-41772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41772)

    * [CVE-2021-44716](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44716)

    * [CVE-2022-2879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2879)

    * [CVE-2022-2880](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2880)

    * [CVE-2022-21698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21698)

    * [CVE-2022-23772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23772)

    * [CVE-2022-23773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23773)

    * [CVE-2022-24675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24675)

    * [CVE-2022-24921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24921)

    * [CVE-2022-28131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28131)

    * [CVE-2022-28327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28327)

    * [CVE-2022-30580](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30580)

    * [CVE-2022-30630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30630)

    * [CVE-2022-30631](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30631)

    * [CVE-2022-30632](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30632)

    * [CVE-2022-30633](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30633)

    * [CVE-2022-30635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30635)

    * [CVE-2022-32189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32189)

    * [CVE-2022-41715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41715)

    * [CVE-2022-41724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41724)

    * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)

    * [CVE-2023-6040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6040)

    * [CVE-2023-6356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6356)

    * [CVE-2023-6536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6536)

    * [CVE-2023-6606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6606)

    * [CVE-2023-24534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24534)

    * [CVE-2023-24536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24536)

    * [CVE-2023-24537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24537)

    * [CVE-2023-24539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24539)

    * [CVE-2023-29400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29400)

    * [CVE-2023-29403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29403)

    * [CVE-2023-45287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45287)

    * [CVE-2023-46838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46838)

    * [CVE-2023-52436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52436)

    * [CVE-2023-52439](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52439)

    * [CVE-2023-52444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52444)

    * [CVE-2023-52445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52445)

    * [CVE-2023-52451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52451)

    * [CVE-2023-52464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52464)

    * [CVE-2023-52469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52469)

    * [CVE-2024-1086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1086)

    * [CVE-2024-26586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26586)

    * [CVE-2024-26597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26597)

    * [CVE-2024-26598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26598)

  * Medium-severity container vulnerabilities:

    * [CVE-2020-29509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29509)

    * [CVE-2020-29511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29511)

    * [CVE-2021-33197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33197)

    * [CVE-2021-34558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34558)

    * [CVE-2021-36221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36221)

    * [CVE-2022-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1705)

    * [CVE-2022-1962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1962)

    * [CVE-2022-32148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32148)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-6915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6915)

    * [CVE-2023-24532](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24532)

    * [CVE-2023-29406](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29406)

    * [CVE-2023-29409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29409)

    * [CVE-2023-39198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39198)

    * [CVE-2023-52443](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52443)

    * [CVE-2023-52449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52449)

    * [CVE-2023-52470](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52470)

  * Low-severity container vulnerabilities:

    * [CVE-2022-30629](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30629)

    * [CVE-2023-52438](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52438)

    * [CVE-2023-52448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52448)

    * [CVE-2023-52454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52454)

    * [CVE-2023-52456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52456)

    * [CVE-2023-52457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52457)

    * [CVE-2023-52462](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52462)

    * [CVE-2023-52463](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52463)

    * [CVE-2023-52467](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52467)

    * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)

    * [CVE-2024-24860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24860)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## April 08, 2024

1.28

Announcement

### Release 1.28.400-gke.77

GKE on Bare Metal 1.28.400-gke.77 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/how-to/upgrade). GKE on Bare Metal 1.28.400-gke.77 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Announcement

### Release 1.16.7

GKE on Bare Metal 1.16.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.7 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.28

Change

**Functionality changes:**

  * Updated preflight checks to add a check for networking kernel modules.
  * Updated preflight checks to remove the check for `iptables` package availability.



1.16

Fixed

**Fixes:**

  * Fixed an issue with configuring a proxy for your cluster that required you to manually set `HTTPS_PROXY` and `NO_PROXY` environment variables on the admin workstation.



1.28

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.28.400-gke.77:

  * High-severity container vulnerabilities:

    * [CVE-2023-6040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6040)

    * [CVE-2023-6356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6356)

    * [CVE-2023-6536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6536)

    * [CVE-2023-6606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6606)

    * [CVE-2023-46838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46838)

    * [CVE-2023-52439](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52439)

    * [CVE-2023-52444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52444)

    * [CVE-2023-52445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52445)

    * [CVE-2023-52451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52451)

    * [CVE-2024-1086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1086)

    * [CVE-2024-26586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26586)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-6915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6915)

    * [CVE-2023-39198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39198)

    * [CVE-2023-46218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46218)

    * [CVE-2023-52443](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52443)

    * [CVE-2023-52449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52449)

  * Low-severity container vulnerabilities:

    * [CVE-2023-52438](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52438)

    * [CVE-2023-52448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52448)

    * [CVE-2023-52454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52454)

    * [CVE-2023-52456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52456)

    * [CVE-2023-52457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52457)

    * [CVE-2023-52462](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52462)

    * [CVE-2023-52463](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52463)

    * [CVE-2023-52467](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52467)

    * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)

    * [CVE-2024-24860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24860)




1.28

Fixed

**Fixes:**

  * Fixed a cluster upgrade issue where the `lifecycle-controller-deployer` Pod was unable to migrate existing GKE on Bare Metal resources to the latest API version. This issue blocked upgrades to earlier version 1.28 releases.



1.16

Fixed

The following container image security vulnerabilities have been fixed in 1.16.7: 

  * High-severity container vulnerabilities:

    * [CVE-2022-28948](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28948)

    * [CVE-2023-29499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29499)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-6004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6004)

    * [CVE-2023-6918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6918)

    * [CVE-2023-32611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32611)

    * [CVE-2023-32665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32665)

    * [CVE-2023-46218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46218)

    * [CVE-2023-49290](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49290)

    * [CVE-2024-21664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21664)

    * [GHSA-2c7c-3mj9-8fqh](https://github.com/advisories/GHSA-2c7c-3mj9-8fqh)

  * Low-severity container vulnerabilities:

    * [CVE-2021-25743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25743)



1.28

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/troubleshooting/known-issues) in the Troubleshooting section.

1.16

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## April 03, 2024

1.28

Security

A Denial-of-Service (DoS) vulnerability ([CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. For more information, see the [GCP-2024-022 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-022).

1.16

Security

A Denial-of-Service (DoS) vulnerability ([CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. For more information, see the [GCP-2024-022 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-022).

1.15

Security

A Denial-of-Service (DoS) vulnerability ([CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. For more information, see the [GCP-2024-022 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-022).

## March 21, 2024

1.28

Announcement

### Release 1.28.300-gke.131

GKE on Bare Metal 1.28.300-gke.131 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/how-to/upgrade). GKE on Bare Metal 1.28.300-gke.131 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Announcement

### Release 1.15.11

GKE on Bare Metal 1.15.11 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). GKE on Bare Metal 1.15.11 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.28

Change

**Functionality changes:**

  * Updated preflight checks to add a check for networking kernel modules.

  * Updated preflight checks to remove the check for `iptables` package availability.

  * Increased the default memory limit for `node-exporter`.




1.15

Fixed

The following container image security vulnerabilities have been fixed in 1.15.11: 

  * Medium-severity container vulnerabilities:

    * [CVE-2023-46218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46218)

    * [CVE-2023-49290](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49290)

    * [CVE-2024-21664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21664)

    * [GHSA-2c7c-3mj9-8fqh](https://github.com/advisories/GHSA-2c7c-3mj9-8fqh)

  * Low-severity container vulnerabilities:

    * [CVE-2021-25743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25743)



1.28

Fixed

**Fixes:**

  * Fixed an issue with configuring a proxy for your cluster that required you to manually set `HTTPS_PROXY` and `NO_PROXY` environment variables on the admin workstation.



1.15

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

1.28

Fixed

The following container image security vulnerabilities have been fixed in 1.28.300-gke.131: 

  * High-severity container vulnerabilities:

    * [CVE-2022-28948](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28948)

    * [CVE-2023-29499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29499)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)

    * [CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)

    * [CVE-2023-32611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32611)

    * [CVE-2023-32665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32665)

    * [CVE-2023-49290](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49290)

    * [CVE-2024-21664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21664)

    * [GHSA-2c7c-3mj9-8fqh](https://github.com/advisories/GHSA-2c7c-3mj9-8fqh)

  * Low-severity container vulnerabilities:

    * [CVE-2021-25743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25743)

    * [CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/troubleshooting/known-issues) in the Troubleshooting section.

## March 04, 2024

1.28

Announcement

### Release 1.28.200-gke.118

GKE on Bare Metal 1.28.200-gke.118 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/how-to/upgrade). GKE on Bare Metal 1.28.200-gke.118 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Announcement

### Release 1.15.10

GKE on Bare Metal 1.15.10 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). GKE on Bare Metal 1.15.10 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.28

Fixed

**Fixes:**

  * Fixed an issue where upgrades are blocked because `cluster-operator` can't delete stale, failing preflight check resources.



1.28

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.28.200-gke.118: 

  * Critical container vulnerabilities:

    * [CVE-2023-25775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25775)
  * High-severity container vulnerabilities:

    * [CVE-2023-5717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5717)

    * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)

    * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)

    * [CVE-2023-35827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35827)

    * [CVE-2023-51780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51780)

    * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)

    * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)

    * [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-6004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6004)

    * [CVE-2023-6121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6121)

    * [CVE-2023-6918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6918)

    * [CVE-2021-44879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44879)

    * [CVE-2023-34324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34324)

    * [CVE-2023-45863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45863)

    * [CVE-2023-46343](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46343)

  * Low-severity container vulnerabilities:

    * [CVE-2023-5178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5178)

    * [CVE-2023-5197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5197)

    * [CVE-2023-6531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6531)

    * [CVE-2023-6817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6817)

    * [CVE-2023-46813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46813)

    * [CVE-2023-46862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46862)

    * [CVE-2024-0193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0193)

    * [CVE-2024-0641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0641)




1.15

Feature

GKE on Bare Metal version 1.15.10 and later has been qualified on and supports Red Hat Enterprise Linux (RHEL) version 8.9.

1.15

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.15.10: 

  * High-severity container vulnerabilities:

    * [CVE-2023-29499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29499)

    * [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-6004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6004)

    * [CVE-2023-6918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6918)

    * [CVE-2023-32611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32611)

    * [CVE-2023-32665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32665)

    * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/troubleshooting/known-issues) in the Troubleshooting section.

1.15

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## February 20, 2024

1.16

Feature

### Release 1.16.6

GKE on Bare Metal 1.16.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.6 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.6: 

  * High-severity container vulnerabilities:

    * [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626)
  * Medium-severity container vulnerabilities:

    * [CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)

    * [CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)

  * Low-severity container vulnerabilities:

    * [CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)

    * [CVE-2023-4527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4527)

    * [CVE-2023-4911](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4911)




1.16

Fixed

**Fixes:**

  * Fixed an issue where upgrades are blocked because `cluster-operator` can't delete stale, failing preflight check resources.

  * Cleaned up stale `etcd-events` membership to enhance control plane initialization reliability in the event of a node join failure.




1.16

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## February 01, 2024

1.15

Feature

### Release 1.15.9

GKE on Bare Metal 1.15.9 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). GKE on Bare Metal 1.15.9 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.15.9: 

  * Critical container vulnerabilities:

    * [CVE-2023-25775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25775)
  * High-severity container vulnerabilities:

    * [CVE-2021-41617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41617)

    * [CVE-2023-5717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5717)

    * [CVE-2023-5869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5869)

    * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)

    * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)

    * [CVE-2023-27533](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27533)

    * [CVE-2023-29491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491)

    * [CVE-2023-35827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35827)

    * [CVE-2023-39417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39417)

    * [CVE-2023-51780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51780)

    * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)

    * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)

  * Medium-severity container vulnerabilities:

    * [CVE-2021-44879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44879)

    * [CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)

    * [CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)

    * [CVE-2023-5870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5870)

    * [CVE-2023-6121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6121)

    * [CVE-2023-25165](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25165)

    * [CVE-2023-27535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27535)

    * [CVE-2023-27536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536)

    * [CVE-2023-27538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27538)

    * [CVE-2023-28321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321)

    * [CVE-2023-34324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34324)

    * [CVE-2023-36054](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36054)

    * [CVE-2023-45863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45863)

    * [CVE-2023-46218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46218)

    * [CVE-2023-46343](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46343)

    * [CVE-2023-51385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51385)

    * [CVE-2023-5868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5868)

    * [CVE-2024-0584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0584)

  * Low-severity container vulnerabilities:

    * [CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)

    * [CVE-2023-4527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4527)

    * [CVE-2023-4911](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4911)

    * [CVE-2023-5178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5178)

    * [CVE-2023-5197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5197)

    * [CVE-2023-6531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6531)

    * [CVE-2023-6817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6817)

    * [CVE-2023-27534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27534)

    * [CVE-2023-28322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28322)

    * [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)

    * [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)

    * [CVE-2023-46813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46813)

    * [CVE-2023-46862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46862)

    * [CVE-2024-0193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0193)

    * [CVE-2024-0641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0641)




1.15

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## January 31, 2024

1.9

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.8

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.7

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.6

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.28

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.28

Feature

### Release 1.28.100-gke.146

GKE on Bare Metal 1.28.100-gke.146 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/how-to/upgrade). GKE on Bare Metal 1.28.100-gke.146 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.15

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.14

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.13

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.12

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.11

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.10 

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

1.28

Fixed

**Fixes:**

Fixed a rootless permission issue on file `/var/lib/audit.log` in 1.28.100, which might block control plane node upgrades.

The following container image security vulnerabilities have been fixed in 1.28.100-gke.146: 

  * Critical container vulnerabilities:

    * [CVE-2023-39320](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39320)
  * High-severity container vulnerabilities:

    * [CVE-2021-41617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41617)

    * [CVE-2023-5869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5869)

    * [CVE-2023-27533](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27533)

    * [CVE-2023-29491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491)

    * [CVE-2023-39321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39321)

    * [CVE-2023-39322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39322)

    * [CVE-2023-39417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39417)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-5156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5156)

    * [CVE-2023-5868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5868)

    * [CVE-2023-5870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5870)

    * [CVE-2023-25165](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25165)

    * [CVE-2023-27535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27535)

    * [CVE-2023-27536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536)

    * [CVE-2023-27538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27538)

    * [CVE-2023-28321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321)

    * [CVE-2023-36054](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36054)

    * [CVE-2023-51385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51385)

    * [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq)

  * Low-severity container vulnerabilities:

    * [CVE-2022-48522](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48522)

    * [CVE-2023-4527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4527)

    * [CVE-2023-4911](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4911)

    * [CVE-2023-27534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27534)

    * [CVE-2023-28322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28322)

    * [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)

    * [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)




1.28

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/troubleshooting/known-issues) in the Troubleshooting section.

## January 30, 2024

1.16

Feature

### Release 1.16.5

GKE on Bare Metal 1.16.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.5 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.5: 

  * Critical container vulnerabilities:

    * [CVE-2023-25775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25775)
  * High-severity container vulnerabilities:

    * [CVE-2021-3121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3121)

    * [CVE-2021-41617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41617)

    * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)

    * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

    * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)

    * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)

    * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)

    * [CVE-2023-0464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464)

    * [CVE-2023-5717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5717)

    * [CVE-2023-5869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5869)

    * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)

    * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)

    * [CVE-2023-27533](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27533)

    * [CVE-2023-29491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491)

    * [CVE-2023-35827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35827)

    * [CVE-2023-39417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39417)

    * [CVE-2023-51780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51780)

    * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)

    * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)

  * Medium-severity container vulnerabilities:

    * [CVE-2020-8565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8565)

    * [CVE-2021-44879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44879)

    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)

    * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)

    * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)

    * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

    * [CVE-2023-0465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465)

    * [CVE-2023-0466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466)

    * [CVE-2023-2650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650)

    * [CVE-2023-5868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5868)

    * [CVE-2023-5870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5870)

    * [CVE-2023-6121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6121)

    * [CVE-2023-25165](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25165)

    * [CVE-2023-27535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27535)

    * [CVE-2023-27536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536)

    * [CVE-2023-27538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27538)

    * [CVE-2023-28321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321)

    * [CVE-2023-34324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34324)

    * [CVE-2023-36054](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36054)

    * [CVE-2023-45863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45863)

    * [CVE-2023-46343](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46343)

    * [CVE-2023-51385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51385)

    * [CVE-2024-0584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0584)

  * Low-severity container vulnerabilities:

    * [CVE-2023-5178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5178)

    * [CVE-2023-5197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5197)

    * [CVE-2023-6531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6531)

    * [CVE-2023-6817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6817)

    * [CVE-2023-27534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27534)

    * [CVE-2023-28322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28322)

    * [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)

    * [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)

    * [CVE-2023-46813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46813)

    * [CVE-2023-46862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46862)

    * [CVE-2024-0193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0193)

    * [CVE-2024-0641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0641)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## December 15, 2023

1.28

Feature

### Release 1.28.0-gke.435

GKE on Bare Metal 1.28.0-gke.435 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/how-to/upgrade). GKE on Bare Metal 1.28.0-gke.435 runs on Kubernetes 1.28.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Feature

### Release 1.16.4

GKE on Bare Metal 1.16.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.4 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.28

Announcement

**Version alignment**

For easier identification of the Kubernetes version for a given release, we are aligning Anthos clusters on bare metal version numbering with GKE version numbering. This change starts with this minor release, which is version 1.28. The version alignment is for major and minor versions only, patch versions are product specific. In addition to this version alignment, the Anthos clusters on bare metal release versions will follow the [GKE semantic versioning scheme](https://cloud.google.com/kubernetes-engine/versioning#versioning_scheme) (x.y.z-gke.N), including the addition of a GKE patch version (-gke.N). Unlike GKE, however, the patch version (z) increments by 100.

**Example version numbers for Anthos clusters on bare metal:**

  * Minor release: 1.28.0-gke.435
  * Initial patch release: 1.28.100-gke.27
  * Second patch release: 1.28.200-gke.19



This change affects numbering only. Upgrades from 1.16 to 1.28 follow the same process as upgrades between prior minor releases. However, downloads, upgrades, and cluster creation for 1.28 and higher versions require the fully qualified version number, including the GKE patch version.

1.28

Announcement

**Version 1.14 end of life** : In accordance with the Anthos Version Support Policy, version 1.14 (all patch releases) of Anthos clusters on bare metal has reached its end of life and is no longer supported.

1.16

Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

1.16

Change

**Functionality changes:**

  * Changed upgrade preflight checks behavior to skip kubeadm job creation check to improve upgrade reliability.



1.28

Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.28.0-gke.435, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

1.28

Feature

  * **Preview** : Added support for Red Hat Enterprise Linux (RHEL) version 9.2. For more information, see [Select your operating system](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs).

  * **Preview** : Added support for skews of up to two minor versions for [selective node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade-lifecycle#np_version_rules).

  * **Preview** : Added capability to [pause and resume cluster upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#pause_resume).

  * **GA** : Added support for [using custom cluster certificate authorities (CAs)](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/custom-cluster-ca) to enable secure authentication and encryption between cluster components.

  * **GA** : Added support for using [`gkeConnect.location`](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/cluster-config-ref#gkeconnect-location) to specify regional membership for fleets.

  * **GA** : Added support for using [`controlPlane.apiServerCertExtraSANs`](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/cluster-config-ref#controlplane-apiservercertextrasans) to specify extra subject alternative name (SAN) entries for the Kubernetes API server certificate.

  * **GA** : Added support for [enabling Direct Server Return (DSR) load balancing](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/lb-network-mode) for clusters. In GA, DSR load balancing is enabled with the `clusterNetwork.forwardMode` field in the cluster configuration file.

  * **GA** : Added support for multiple BGP load balancer (`BGPLoadBalancer`) resources and BGP Community. Multiple BGP load balancer resources provide more flexibility to define which peers advertise specific load balancer nodes and Services. BGP Community support helps you to distinguish routes coming from BGP load balancers from other routes in your network.

  * **Preview** : Added GKE Identity Service v2 capability for an improved security flow when you authenticate with third-party identity solutions.

**Warning:** GKE Identity Service v2 requires ports 8443 and 8444 on the control plane load balancer nodes. Ensure these ports are open and available before you upgrade a cluster to version 1.28.0-gke.435 and higher. If the ports aren't open, upgrade preflight checks fail.



1.28

Change

**Functionality changes:**

  * Configured the local volume provisioner DaemonSet to tolerate all taints.

  * Updated the SRIOV operator. 

  * To improve logging system integration, updated audit logging to always write a local Kubernetes audit log file, even when Cloud Audit Logging is enabled. 

  * Changed upgrade preflight checks behavior to skip kubeadm job creation check to improve upgrade reliability.

  * Updated Dataplane V2 to use Cilium v1.13.

  * Added preflight check for control planes running RHEL 9.2 or Ubuntu 22.04 to check the `fs.inotify` kernel settings.

**Note:** Preflight check updates for new features or capabilities aren't an indication that a given feature or capability is supported. Added support for new features and capabilities are called out separately in release notes with their corresponding support phase (Preview or GA).
  * Removed hardcoded timeout value for `bmctl backup` operation.

  * Updated certificate management to propagate `private-registry-certs` Secret changes to all machines.

  * Added support for SSH client certificates in `bmctl backup` and `bmctl restore` commands.

  * Added the optional `userClaim` field to the ClientConfig custom resource definition bundled with Anthos clusters on bare metal. This change improves support for Azure AD integrations with Anthos Identity Service. 

  * Updated constraint on NodePool `spec.upgradeStrategy.concurrentNodes` to be the smaller of either 15 nodes or 50% of the size of the node pool.




1.16

Fixed

**Fixes:**

  * Fixed an issue where the network check ConfigMap wasn't being updated when nodes were added or removed.

  * Fixed an issue where excessive `stackdriver-operator` reconciliations resulted in high CPU usage.




1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.4: 

  * Medium-severity container vulnerabilities:

    * [CVE-2021-3507](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3507)

    * [CVE-2021-3930](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3930)

    * [CVE-2021-20196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20196)

    * [CVE-2022-0216](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0216)

    * [CVE-2023-0330](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0330)

    * [CVE-2023-3180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3180)

    * [CVE-2023-34969](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34969)

    * [CVE-2023-41913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41913)

    * [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq)

  * Low-severity container vulnerabilities:

    * [CVE-2017-16516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-16516)

    * [CVE-2020-14394](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14394)

    * [CVE-2021-20203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20203)

    * [CVE-2022-24795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24795)

    * [CVE-2023-1544](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1544)

    * [CVE-2023-3301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3301)

    * [CVE-2023-3354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3354)

    * [CVE-2023-33460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33460)




1.28

Fixed

The following container image security vulnerabilities have been fixed in version 1.28.0-gke-435:

  * Critical container vulnerabilities:

    * [CVE-2022-1996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1996)

    * [CVE-2023-38408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38408)

    * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)

  * High-severity container vulnerabilities:

    * [CVE-2017-11468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-11468)

    * [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253)

    * [CVE-2019-13509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13509)

    * [CVE-2020-7919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7919)

    * [CVE-2020-8558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8558)

    * [CVE-2020-9283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9283)

    * [CVE-2021-3121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3121)

    * [CVE-2020-16845](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-16845)

    * [CVE-2020-28362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28362)

    * [CVE-2020-28366](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28366)

    * [CVE-2020-28367](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28367)

    * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

    * [CVE-2021-27918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27918)

    * [CVE-2022-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39189)

    * [CVE-2022-41721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41721)

    * [CVE-2023-1380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1380)

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2007)

    * [CVE-2023-2124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2124)

    * [CVE-2023-2253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2253)

    * [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)

    * [CVE-2023-3111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3111)

    * [CVE-2023-3268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3268)

    * [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)

    * [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)

    * [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)

    * [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)

    * [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4206)

    * [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4207)

    * [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4208)

    * [CVE-2023-4244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4244)

    * [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622)

    * [CVE-2023-4623](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4623)

    * [CVE-2023-4921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4921)

    * [CVE-2023-21255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21255)

    * [CVE-2023-27561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27561)

    * [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840)

    * [CVE-2023-29002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29002)

    * [CVE-2023-34319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34319)

    * [CVE-2023-35001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35001)

    * [CVE-2023-35788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35788)

    * [CVE-2023-40283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40283)

    * [CVE-2023-42753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42753)

    * [GHSA-74fp-r6jw-h4mp](https://github.com/advisories/GHSA-74fp-r6jw-h4mp)

  * Medium-severity container vulnerabilities:

    * [CVE-2015-3627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3627)

    * [CVE-2019-11250](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11250)

    * [CVE-2019-11251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11251)

    * [CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254)

    * [CVE-2019-19794](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19794)

    * [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554)

    * [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)

    * [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561)

    * [CVE-2020-8564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8564)

    * [CVE-2020-8565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8565)

    * [CVE-2020-8569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8569)

    * [CVE-2020-8911](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8911)

    * [CVE-2020-14039](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14039)

    * [CVE-2020-14040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14040)

    * [CVE-2020-15586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15586)

    * [CVE-2020-21047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-21047)

    * [CVE-2020-24553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-24553)

    * [CVE-2020-29510](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29510)

    * [CVE-2021-3114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3114)

    * [CVE-2021-3507](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3507)

    * [CVE-2021-3930](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3930)

    * [CVE-2021-20196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20196)

    * [CVE-2021-20329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20329)

    * [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735)

    * [CVE-2021-25736](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25736)

    * [CVE-2022-0216](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0216)

    * [CVE-2022-2582](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2582)

    * [CVE-2022-4269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4269)

    * [CVE-2022-40982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40982)

    * [CVE-2022-46146](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-46146)

    * [CVE-2023-0330](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0330)

    * [CVE-2023-1206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1206)

    * [CVE-2023-2002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2002)

    * [CVE-2023-2269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2269)

    * [CVE-2023-3180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3180)

    * [CVE-2023-3212](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3212)

    * [CVE-2023-3338](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3338)

    * [CVE-2023-3772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3772)

    * [CVE-2023-3863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3863)

    * [CVE-2023-4132](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4132)

    * [CVE-2023-4194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4194)

    * [CVE-2023-4273](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4273)

    * [CVE-2023-20569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20569)

    * [CVE-2023-20593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20593)

    * [CVE-2023-27593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27593)

    * [CVE-2023-27594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27594)

    * [CVE-2023-27595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27595)

    * [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841)

    * [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842)

    * [CVE-2023-30851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30851)

    * [CVE-2023-31084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31084)

    * [CVE-2023-37453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-37453)

    * [CVE-2023-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39189)

    * [CVE-2023-39192](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39192)

    * [CVE-2023-39193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39193)

    * [CVE-2023-39194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39194)

    * [CVE-2023-39347](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39347)

    * [CVE-2023-40577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40577)

    * [CVE-2023-41333](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41333)

    * [CVE-2023-41913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41913)

    * [CVE-2023-42754](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42754)

    * [CVE-2023-42755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42755)

    * [GHSA-2w8w-qhg4-f78j](https://github.com/advisories/GHSA-2w8w-qhg4-f78j)

    * [GHSA-76wf-9vgp-pj7w](https://github.com/advisories/GHSA-76wf-9vgp-pj7w)

  * Low-severity container vulnerabilities:

    * [CVE-2017-16516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-16516)

    * [CVE-2020-8562](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8562)

    * [CVE-2020-8912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8912)

    * [CVE-2020-14394](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14394)

    * [CVE-2021-20203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20203)

    * [CVE-2021-25740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25740)

    * [CVE-2021-32292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32292)

    * [CVE-2022-24795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24795)

    * [CVE-2022-45886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45886)

    * [CVE-2022-45887](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45887)

    * [CVE-2022-45919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45919)

    * [CVE-2022-48554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48554)

    * [CVE-2023-1544](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1544)

    * [CVE-2023-2156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2156)

    * [CVE-2023-2898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2898)

    * [CVE-2023-3141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3141)

    * [CVE-2023-3301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3301)

    * [CVE-2023-3354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3354)

    * [CVE-2023-3389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3389)

    * [CVE-2023-3610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3610)

    * [CVE-2023-3773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3773)

    * [CVE-2023-3777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3777)

    * [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)

    * [CVE-2023-4147](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4147)

    * [CVE-2023-6176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6176)

    * [CVE-2023-21400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21400)

    * [CVE-2023-31248](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31248)

    * [CVE-2023-33460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33460)

    * [CVE-2023-34242](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34242)

    * [CVE-2023-34256](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34256)

    * [CVE-2023-35823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35823)

    * [CVE-2023-35824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35824)

    * [CVE-2023-35828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35828)

    * [CVE-2023-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35829)

    * [CVE-2023-41332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41332)

    * [CVE-2023-42756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42756)

    * [GHSA-qq97-vm5h-rrhg](https://github.com/advisories/GHSA-qq97-vm5h-rrhg)




1.28

Fixed

**Fixes:**

  * Fixed an issue where the `node-problem-detector` `systemd` service doesn't restart after the node reboots.

  * Fixed an issue where `CoreDNS` Pods can get stuck in an unready state.

  * Fixed an issue that caused application metrics to be unavailable in Anthos clusters on bare metal versions 1.16.0 and 1.16.1.

  * Fixed a memory leak in Dataplane V2.

  * Fixed an issue that caused file and directory permissions to be set incorrectly after backing up and restoring a cluster.

  * Added direct dependencies on systemd, containerd, and kubelet over their mount point folders in `/var/lib/`.

  * Fixed an issue that blocked upgrades to version 1.16 for clusters that have secure computing mode (`seccomp`) disabled.

  * Fixed an issue where etcd blocked upgrades due to an incorrect initial-cluster-state.

  * Fixed an issue that sometimes resulted in the upgrade process starting before either all pods have been drained or the draining period has elapsed.

  * Fixed an issue that resulted in the etcd-events memory request (`resources.requests.memory`) being set incorrectly.




1.16

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

1.28

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.28/troubleshooting/known-issues) in the Troubleshooting section.

## December 13, 2023

1.15

Feature

### Release 1.15.8

GKE on Bare Metal 1.15.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). GKE on Bare Metal 1.15.8 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Change

**Functionality changes:**

  * Changed upgrade preflight checks behavior to skip kubeadm job creation check to improve upgrade reliability.



1.15

Fixed

**Fixes:**

  * Fixed an issue where the network check ConfigMap wasn't being updated when nodes were added or removed.



1.15

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.15.8: 

  * High-severity container vulnerabilities:

    * [CVE-2022-41721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41721)
  * Medium-severity container vulnerabilities:

    * [CVE-2021-3507](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3507)

    * [CVE-2021-3930](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3930)

    * [CVE-2021-20196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20196)

    * [CVE-2022-0216](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0216)

    * [CVE-2023-0330](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0330)

    * [CVE-2023-3180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3180)

    * [CVE-2023-34969](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34969)

    * [CVE-2023-41913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41913)

    * [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq)

  * Low-severity container vulnerabilities:

    * [CVE-2017-16516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-16516)

    * [CVE-2020-14394](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14394)

    * [CVE-2021-20203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20203)

    * [CVE-2022-24795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24795)

    * [CVE-2023-1544](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1544)

    * [CVE-2023-3301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3301)

    * [CVE-2023-3354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3354)

    * [CVE-2023-33460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33460)




1.15

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## November 28, 2023

1.16

Feature

### Release 1.16.3

GKE on Bare Metal 1.16.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.3 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

1.16

Change

**Functionality changes:**

  * Increased the certificate time to live (TTL) for `metrics-providers-ca` and `stackdriver-prometheus-scrape` for third-party monitoring.



1.16

Fixed

**Fixes:**

  * Fixed an issue where `CoreDNS` Pods can get stuck in an unready state.

  * Fixed an issue that caused application metrics to be unavailable in Anthos clusters on bare metal versions 1.16.0 and 1.16.1.




1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.3: 

  * Critical container vulnerabilities:

    * [CVE-2023-38408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38408)

    * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)

  * High-severity container vulnerabilities:

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-4244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4244)

    * [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622)

    * [CVE-2023-4623](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4623)

    * [CVE-2023-4921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4921)

    * [CVE-2023-42753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42753)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-3772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3772)

    * [CVE-2023-37453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-37453)

    * [CVE-2023-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39189)

    * [CVE-2023-39192](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39192)

    * [CVE-2023-39193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39193)

    * [CVE-2023-39194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39194)

    * [CVE-2023-42754](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42754)

    * [CVE-2023-42755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42755)

  * Low-severity container vulnerabilities:

    * [CVE-2023-3773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3773)

    * [CVE-2023-6176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6176)

    * [CVE-2023-42756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42756)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## November 21, 2023

1.14

Feature

### Release 1.14.11

Anthos clusters on bare metal 1.14.11 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.11 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.14.11: 

  * Critical container vulnerabilities:

    * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)
  * High-severity container vulnerabilities:

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-4244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4244)

    * [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622)

    * [CVE-2023-4623](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4623)

    * [CVE-2023-4921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4921)

    * [CVE-2023-42753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42753)

  * Medium-severity container vulnerabilities:

    * [CVE-2021-3507](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3507)

    * [CVE-2021-3930](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3930)

    * [CVE-2021-20196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20196)

    * [CVE-2022-0216](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0216)

    * [CVE-2023-0330](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0330)

    * [CVE-2023-3180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3180)

    * [CVE-2023-3772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3772)

    * [CVE-2023-34969](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34969)

    * [CVE-2023-37453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-37453)

    * [CVE-2023-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39189)

    * [CVE-2023-39192](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39192)

    * [CVE-2023-39193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39193)

    * [CVE-2023-39194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39194)

    * [CVE-2023-42754](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42754)

    * [CVE-2023-42755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42755)

  * Low-severity container vulnerabilities:

    * [CVE-2017-16516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-16516)

    * [CVE-2020-14394](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14394)

    * [CVE-2021-20203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20203)

    * [CVE-2022-24795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24795)

    * [CVE-2023-1544](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1544)

    * [CVE-2023-3301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3301)

    * [CVE-2023-3354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3354)

    * [CVE-2023-3773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3773)

    * [CVE-2023-6176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6176)

    * [CVE-2023-33460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33460)

    * [CVE-2023-42756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42756)




1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## November 20, 2023

1.15

Feature

### Release 1.15.7

Anthos clusters on bare metal 1.15.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). Anthos clusters on bare metal 1.15.7 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Fixed

Fixed an issue where CoreDNS Pods can get stuck in an unready state.

1.15

Fixed

The following container image security vulnerabilities have been fixed in 1.15.7: 

  * Critical container vulnerabilities:

    * [CVE-2023-38408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38408)

    * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)

  * High-severity container vulnerabilities:

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-4244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4244)

    * [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622)

    * [CVE-2023-4623](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4623)

    * [CVE-2023-4921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4921)

    * [CVE-2023-42753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42753)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-3772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3772)

    * [CVE-2023-37453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-37453)

    * [CVE-2023-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39189)

    * [CVE-2023-39192](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39192)

    * [CVE-2023-39193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39193)

    * [CVE-2023-39194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39194)

    * [CVE-2023-42754](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42754)

    * [CVE-2023-42755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42755)

  * Low-severity container vulnerabilities:

    * [CVE-2023-3773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3773)

    * [CVE-2023-42756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42756)




1.15

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## November 06, 2023

1.14

Feature

### Release 1.14.10

Anthos clusters on bare metal 1.14.10 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.10 runs on Kubernetes 1.25.

1.14

Change

**Functionality changes:**

  * Added `NODEPOOL-NAME`, `NODEPOOL-NAMESPACE`, and `STATUS` columns for the `InventoryMachine` resource to improve troubleshooting. 

  * Removed hardcoded timeout value for the `bmctl backup` operation.




1.14

Fixed

**Fixes:**

  * Fixed an issue where `CoreDNS` Pods can get stuck in an unready state.

  * Fixed a memory leak in Dataplane V2.




1.14

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in version 1.14.10: 

  * Critical container vulnerabilities:

    * [CVE-2023-38408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38408)
  * High-severity container vulnerabilities:

    * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

    * [CVE-2021-25741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741)

    * [CVE-2022-3064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3064)

    * [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-11250](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11250)

    * [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554)

    * [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561)

    * [CVE-2020-21047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-21047)

    * [CVE-2021-4235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4235)

    * [CVE-2021-25736](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25736)

    * [CVE-2022-46146](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-46146)

    * [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841)

    * [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842)

    * [CVE-2023-39347](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39347)

    * [CVE-2023-41333](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41333)

  * Low-severity container vulnerabilities:

    * [CVE-2021-25740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25740)

    * [CVE-2021-32292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32292)

    * [CVE-2023-34242](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34242)

    * [CVE-2023-41332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41332)

    * [GHSA-qq97-vm5h-rrhg](https://github.com/advisories/GHSA-qq97-vm5h-rrhg)




1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## October 30, 2023

1.16

Feature

### Release 1.16.2

Anthos clusters on bare metal 1.16.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). Anthos clusters on bare metal 1.16.2 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Feature

### Release 1.15.6

GKE on Bare Metal 1.15.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). GKE on Bare Metal 1.15.6 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

1.16

Change

**Functionality changes:**

  * Increased the certificate time to live (TTL) for `metrics-providers-ca` and `stackdriver-prometheus-scrape` for third-party monitoring.

  * Removed hardcoded timeout value for the `bmctl backup` operation.




1.15

Change

**Functionality changes:**

  * Removed hardcoded timeout value for the `bmctl backup` operation.



1.16

Fixed

**Fixes:**

  * Fixed the `spec.featureGates.annotationBasedApplicationMetrics` feature gate in the stackdriver custom resource to enable collection of annotation-based workload metrics. This function is broken in Anthos clusters on bare metal versions 1.16.0 and 1.16.1.

  * Fixed a memory leak in Dataplane V2.

  * Fixed an issue where garbage collection deleted Source Network Address Translation (SNAT) entries for long-lived egress NAT connections, causing connection resets.

  * Fixed an issue that caused file and directory permissions to be set incorrectly after backing up and restoring a cluster.

  * Added direct dependencies on systemd, containerd, and kubelet over their mount point folders in `/var/lib/`.

  * Fixed an issue where etcd blocked upgrades due to an incorrect initial-cluster-state.

  * Fixed an issue that blocked upgrades to version 1.16 for clusters that have secure computing mode (`seccomp`) disabled.




1.15

Fixed

**Fixes:**

  * Fixed a memory leak in Dataplane V2.

  * Added direct dependencies on systemd, containerd, and kubelet over their mount point folders in `/var/lib/`.




1.16

Fixed

The following container image security vulnerabilities have been fixed in release 1.16.2: 

  * High-severity container vulnerabilities:

    * [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253)

    * [CVE-2020-7919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7919)

    * [CVE-2020-8558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8558)

    * [CVE-2020-9283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9283)

    * [CVE-2021-25741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741)

    * [CVE-2021-27918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27918)

    * [CVE-2022-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39189)

    * [CVE-2022-41721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41721)

    * [CVE-2023-1380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1380)

    * [CVE-2023-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2007)

    * [CVE-2023-2124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2124)

    * [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)

    * [CVE-2023-3111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3111)

    * [CVE-2023-3268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3268)

    * [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)

    * [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)

    * [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)

    * [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)

    * [CVE-2023-4128](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4128)

    * [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4206)

    * [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4207)

    * [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4208)

    * [CVE-2023-21255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21255)

    * [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840)

    * [CVE-2023-34319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34319)

    * [CVE-2023-35001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35001)

    * [CVE-2023-35788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35788)

    * [CVE-2023-40283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40283)

    * [GHSA-74fp-r6jw-h4mp](https://github.com/advisories/GHSA-74fp-r6jw-h4mp)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-11250](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11250)

    * [CVE-2019-11251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11251)

    * [CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254)

    * [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554)

    * [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)

    * [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561)

    * [CVE-2020-8564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8564)

    * [CVE-2020-8911](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8911)

    * [CVE-2020-14040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14040)

    * [CVE-2020-21047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-21047)

    * [CVE-2021-3114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3114)

    * [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735)

    * [CVE-2022-2582](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2582)

    * [CVE-2022-4269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4269)

    * [CVE-2022-40982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40982)

    * [CVE-2022-46146](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-46146)

    * [CVE-2023-1206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1206)

    * [CVE-2023-2002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2002)

    * [CVE-2023-2269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2269)

    * [CVE-2023-3212](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3212)

    * [CVE-2023-3338](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3338)

    * [CVE-2023-3863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3863)

    * [CVE-2023-4132](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4132)

    * [CVE-2023-4194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4194)

    * [CVE-2023-4273](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4273)

    * [CVE-2023-20569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20569)

    * [CVE-2023-20593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20593)

    * [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841)

    * [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842)

    * [CVE-2023-31084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31084)

    * [CVE-2023-40577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40577)

    * [CVE-2023-41333](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41333)

    * [GHSA-2w8w-qhg4-f78j](https://github.com/advisories/GHSA-2w8w-qhg4-f78j)

    * [GHSA-76wf-9vgp-pj7w](https://github.com/advisories/GHSA-76wf-9vgp-pj7w)

    * [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq)

  * Low-severity container vulnerabilities:

    * [CVE-2020-8562](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8562)

    * [CVE-2020-8912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8912)

    * [CVE-2021-25740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25740)

    * [CVE-2021-32292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32292)

    * [CVE-2022-45886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45886)

    * [CVE-2022-45887](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45887)

    * [CVE-2022-45919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45919)

    * [CVE-2022-48554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48554)

    * [CVE-2023-2156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2156)

    * [CVE-2023-2898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2898)

    * [CVE-2023-3141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3141)

    * [CVE-2023-3389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3389)

    * [CVE-2023-3610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3610)

    * [CVE-2023-3777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3777)

    * [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)

    * [CVE-2023-4147](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4147)

    * [CVE-2023-21400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21400)

    * [CVE-2023-31248](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31248)

    * [CVE-2023-34242](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34242)

    * [CVE-2023-34256](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34256)

    * [CVE-2023-35823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35823)

    * [CVE-2023-35824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35824)

    * [CVE-2023-35828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35828)

    * [CVE-2023-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35829)

    * [CVE-2023-41332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41332)

    * [GHSA-qq97-vm5h-rrhg](https://github.com/advisories/GHSA-qq97-vm5h-rrhg)




1.15

Fixed

**Fixes:**

Fixed the following vulnerabilities:

  * Critical container vulnerabilities:

    * [CVE-2022-1996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1996)
  * High-severity container vulnerabilities:

    * [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253)

    * [CVE-2020-8558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8558)

    * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

    * [CVE-2021-25741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741)

    * [CVE-2022-3064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3064)

    * [CVE-2022-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39189)

    * [CVE-2023-1380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1380)

    * [CVE-2023-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2007)

    * [CVE-2023-2124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2124)

    * [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)

    * [CVE-2023-3111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3111)

    * [CVE-2023-3268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3268)

    * [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)

    * [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)

    * [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)

    * [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)

    * [CVE-2023-4128](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4128)

    * [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4206)

    * [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4207)

    * [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4208)

    * [CVE-2023-21255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21255)

    * [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840)

    * [CVE-2023-34319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34319)

    * [CVE-2023-35001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35001)

    * [CVE-2023-35788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35788)

    * [CVE-2023-40283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40283)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-11250](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11250)

    * [CVE-2019-11251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11251)

    * [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554)

    * [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)

    * [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561)

    * [CVE-2020-8564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8564)

    * [CVE-2020-21047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-21047)

    * [CVE-2021-4235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4235)

    * [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735)

    * [CVE-2022-4269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4269)

    * [CVE-2022-40982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40982)

    * [CVE-2022-46146](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-46146)

    * [CVE-2023-1206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1206)

    * [CVE-2023-2002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2002)

    * [CVE-2023-2269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2269)

    * [CVE-2023-3212](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3212)

    * [CVE-2023-3338](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3338)

    * [CVE-2023-3863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3863)

    * [CVE-2023-4132](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4132)

    * [CVE-2023-4194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4194)

    * [CVE-2023-4273](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4273)

    * [CVE-2023-20569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20569)

    * [CVE-2023-20593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20593)

    * [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841)

    * [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842)

    * [CVE-2023-31084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31084)

    * [CVE-2023-41333](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41333)

  * Low-severity container vulnerabilities:

    * [CVE-2020-8562](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8562)

    * [CVE-2021-25740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25740)

    * [CVE-2021-32292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32292)

    * [CVE-2022-45886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45886)

    * [CVE-2022-45887](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45887)

    * [CVE-2022-45919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45919)

    * [CVE-2023-2156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2156)

    * [CVE-2023-2898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2898)

    * [CVE-2023-3141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3141)

    * [CVE-2023-3389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3389)

    * [CVE-2023-3610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3610)

    * [CVE-2023-3777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3777)

    * [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)

    * [CVE-2023-4147](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4147)

    * [CVE-2023-21400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21400)

    * [CVE-2023-31248](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31248)

    * [CVE-2023-34242](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34242)

    * [CVE-2023-34256](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34256)

    * [CVE-2023-35823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35823)

    * [CVE-2023-35824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35824)

    * [CVE-2023-35828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35828)

    * [CVE-2023-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35829)

    * [CVE-2023-41332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41332)

    * [GHSA-qq97-vm5h-rrhg](https://github.com/advisories/GHSA-qq97-vm5h-rrhg)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

1.15

Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## September 29, 2023

1.14

Feature

### Release 1.14.9

Anthos clusters on bare metal 1.14.9 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.9 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

Fixed an issue to prevent cluster upgrades from starting on a node before either all Pods have been drained or the Pod draining timeout has been reached.

1.14

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in version 1.14.9: 

  * High-severity container vulnerabilities:

    * [CVE-2019-13509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13509)

    * [CVE-2020-8558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8558)

    * [CVE-2022-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39189)

    * [CVE-2023-1380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1380)

    * [CVE-2023-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2007)

    * [CVE-2023-2124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2124)

    * [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)

    * [CVE-2023-3111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3111)

    * [CVE-2023-3268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3268)

    * [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)

    * [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)

    * [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)

    * [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)

    * [CVE-2023-4128](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4128)

    * [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4206)

    * [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4207)

    * [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4208)

    * [CVE-2023-21255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21255)

    * [CVE-2023-27561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27561)

    * [CVE-2023-29002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29002)

    * [CVE-2023-34319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34319)

    * [CVE-2023-35001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35001)

    * [CVE-2023-35788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35788)

    * [CVE-2023-40283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40283)

  * Medium-severity container vulnerabilities:

    * [CVE-2015-3627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3627)

    * [CVE-2019-11251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11251)

    * [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)

    * [CVE-2020-8564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8564)

    * [CVE-2020-8569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8569)

    * [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735)

    * [CVE-2022-4269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4269)

    * [CVE-2022-40982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40982)

    * [CVE-2023-1206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1206)

    * [CVE-2023-2002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2002)

    * [CVE-2023-2269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2269)

    * [CVE-2023-3212](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3212)

    * [CVE-2023-3338](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3338)

    * [CVE-2023-3863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3863)

    * [CVE-2023-4132](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4132)

    * [CVE-2023-4194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4194)

    * [CVE-2023-4273](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4273)

    * [CVE-2023-20569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20569)

    * [CVE-2023-20593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20593)

    * [CVE-2023-27593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27593)

    * [CVE-2023-27594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27594)

    * [CVE-2023-27595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27595)

    * [CVE-2023-30851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30851)

    * [CVE-2023-31084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31084)

  * Low-severity container vulnerabilities:

    * [CVE-2020-8562](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8562)

    * [CVE-2022-48554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48554)

    * [CVE-2023-2156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2156)

    * [CVE-2023-2898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2898)

    * [CVE-2023-3141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3141)

    * [CVE-2023-3389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3389)

    * [CVE-2023-3610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3610)

    * [CVE-2023-3777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3777)

    * [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)

    * [CVE-2023-4147](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4147)

    * [CVE-2023-21400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21400)

    * [CVE-2023-31248](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31248)

    * [CVE-2023-34256](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34256)

    * [CVE-2023-35823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35823)

    * [CVE-2023-35824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35824)

    * [CVE-2023-35828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35828)

    * [CVE-2023-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35829)




1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## September 25, 2023

1.15

Feature

### Release 1.15.5

Anthos clusters on bare metal 1.15.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). Anthos clusters on bare metal 1.15.5 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Fixed

Fixed an issue to prevent cluster upgrades from starting on a node before either all Pods have been drained or the Pod draining timeout has been reached.

1.15

Fixed

The following container image security vulnerabilities have been fixed in 1.15.5: 

  * High-severity container vulnerabilities:

    * [CVE-2019-13509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13509)

    * [CVE-2023-27561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27561)

    * [CVE-2023-29002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29002)

  * Medium-severity container vulnerabilities:

    * [CVE-2015-3627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3627)

    * [CVE-2020-8569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8569)

    * [CVE-2022-48554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48554)

    * [CVE-2023-27593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27593)

    * [CVE-2023-27594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27594)

    * [CVE-2023-27595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27595)

    * [CVE-2023-30851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30851)




1.15

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## September 21, 2023

1.16

Feature

### Release 1.16.1

Anthos clusters on bare metal 1.16.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). Anthos clusters on bare metal 1.16 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

1.16

Change

**Functionality changes:**

  * Added the optional `userClaim` field to the ClientConfig custom resource definition bundled with Anthos clusters on bare metal. This change improves support for Azure AD integrations with Anthos Identity Service.

  * Updated constraint on NodePool `spec.upgradeStrategy.concurrentNodes` to be the smaller of either 15 nodes or 50% of the size of the node pool.




1.16

Fixed

**Fixes:**

  * Fixed an issue where etcd blocked upgrades due to an incorrect initial-cluster-state.

  * Fixed an issue that blocked upgrades to version 1.16 for clusters that have secure computing mode (`seccomp`) disabled.

  * Fixed an issue to prevent cluster upgrades from starting on a node before either all Pods have been drained or the Pod draining timeout has been reached.

  * Fixed an issue where the memory resource requests value wasn't set properly for `etcd-events`.




1.16

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.1: 

  * Critical container vulnerabilities:

    * [CVE-2022-1996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1996)
  * High-severity container vulnerabilities:

    * [CVE-2017-11468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-11468)

    * [CVE-2019-13509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13509)

    * [CVE-2020-16845](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-16845)

    * [CVE-2020-28362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28362)

    * [CVE-2020-28366](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28366)

    * [CVE-2020-28367](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28367)

    * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

    * [CVE-2023-27561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27561)

    * [CVE-2023-29002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29002)

  * Medium-severity container vulnerabilities:

    * [CVE-2015-3627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3627)

    * [CVE-2019-19794](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19794)

    * [CVE-2020-8569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8569)

    * [CVE-2020-14039](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14039)

    * [CVE-2020-15586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15586)

    * [CVE-2020-24553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-24553)

    * [CVE-2020-29510](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29510)

    * [CVE-2021-20329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20329)

    * [CVE-2023-27593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27593)

    * [CVE-2023-27594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27594)

    * [CVE-2023-27595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27595)

    * [CVE-2023-30851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30851)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## August 25, 2023

1.16

Announcement

**Version 1.13 end of life:** In accordance with the [Anthos Version Support Policy](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support), version 1.13 (all patch releases) of Anthos clusters on bare metal has reached its end of life and is no longer supported.

Red Hat Enterprise Linux (RHEL) 8 minor versions 8.2, 8.3, 8.4, and 8.5 have reached their [end of life](https://access.redhat.com/support/policy/updates/errata). Please ensure you're using a supported version of your operating system.

1.16

Feature

### Release 1.16.0

Anthos clusters on bare metal 1.16.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). Anthos clusters on bare metal 1.16.0 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.16

Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

1.16

Feature

**Cluster lifecycle:**

  * Upgraded to Kubernetes version 1.27.4.

  * Added support for Red Hat Enterprise Linux (RHEL) version 8.8.

  * **GA:** Added support for [parallel upgrades of worker node pools](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#cw-strategy).

  * **GA:** Added support to [upgrade specific worker node pools separately from the rest of the cluster](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up).

  * **GA:** Added a [separate instance of etcd](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/limits#etcd_performance) for the `etcd-events` object. This new etcd instance is always on and requires [ports 2382 and 2383 to be open on control plane nodes](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs#control_plane_nodes) for inbound TCP traffic. If these ports aren't opened, cluster creation and cluster upgrades are blocked.

  * **GA:** Updated preflight checks for cluster installation and upgrades to use changes from the latest Anthos clusters on bare metal patch version to address known issues and provide more useful checks.

  * **GA:** Support enrolling admin and user clusters in the Anthos On-Prem API automatically to enable cluster lifecycle management from the Google Cloud CLI, the Google Cloud console, and Terraform when the Anthos On-Prem API is enabled. If needed, you have the option to disable enrollment. For more information, see the description for the [`gkeOnPremAPI`](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#gkeonpremapi) field in the cluster configuration file.

  * **GA:** Added ability to configure kubelet image pull settings for node pools. For more information, see [Configure kubelet image pull settings](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-clusters#kubelet-config).

  * Added new health check to detect any unsupported drift in the custom resources managed by Anthos clusters on bare metal. Unsupported resource changes can lead to cluster problems.

  * Added a new flag, `--target-cluster-name`, that is supported by the `bmctl register bootstrap` command.




**Networking:**

  * **GA:** Added support for Services of type LoadBalancer to use `externalTrafficPolicy=Local` with [bundled load balancing with BGP](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp).

  * **Preview:** Added support for enabling Direct Server Return (DSR) load balancing for clusters configured with flat-mode networking. DSR load balancing is enabled with an annotation, `preview.baremetal.cluster.gke.io/dpv2-lbmode-dsr: enable`.

  * **Preview:** Upgraded wherabouts to v0.6.1-gke.1 to support dual-stack networking.

  * Added support for multiple BGP load balancer (`BGPLoadBalancer`) resources and BGP Community. Multiple BGP load balancer resources provide more flexibility to define which peers advertise specific load balancer nodes and Services. BGP Community support helps you to distinguish routes coming from BGP load balancers from other routes in your network.




**Observability:**

**Important:** As part of the following change, many metrics have shifted monitored resource types from Kubernetes Container ([`k8s_container`](https://cloud.google.com/monitoring/api/resources#tag_k8s_container)) to Prometheus Target ([`prometheus_target`](https://cloud.google.com/monitoring/api/resources#tag_prometheus_target)). In some cases, this resource change can cause existing dashboards to stop working properly until they are adjusted to use the metrics for the `prometheus_target` resource.

  * **GA:** Added [support for system metrics](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/log-monitoring#using-managed-service-for-prometheus) when you use Google Cloud Managed Service for Prometheus.



**Security and Identity:**

  * **GA:** Added support for Binary Authorization, a service on Google Cloud that provides software supply-chain security for container-based applications. For more information, see [Set up Binary Authorization policy enforcement](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/binary-authorization-policy).

  * **GA:** Added support for [VPC Service Controls](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/hardening-your-cluster#vpc-sc), which provides additional security for your clusters to help mitigate the risk of data exfiltration.

  * **Preview:** Added support for [using custom cluster certificate authorities (CAs)](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/custom-cluster-ca) to enable secure authentication and encryption between cluster components.

  * **Preview:** Added support for configuring the Subject Alternative Names (SANs) of the kubeadm generated certificate for the kube-apiserver.

  * Added support to run keepalived as a non-root user.




1.16

Change

**Functionality changes:**

  * Updated constraint on NodePool `spec.upgradeStrategy.concurrentNodes` to be the smaller of 15 nodes or 50% of the size of the node pool.

  * Replaced legacy method of enabling application logging in the cluster configuration file with two fields, `enableCloudLoggingForApplications` and `enableGMPForApplications`, in the stackdriver custom resource.

The `spec.clusterOperations.enableApplication` field in the cluster configuration file has no effect on version 1.16.0 and higher clusters. This field populated the `enableStackdriverForApplications` field in the stackdriver custom resource, which enabled annotation based workload metric collection. If you need this capability, use the `annotationBasedApplicationMetrics` feature gate in the stackdriver custom resource as shown in the following sample to keep the same behavior:
        
        kind:stackdriver
        spec:
          enableCloudLoggingForApplications: true
          featureGates:
             annotationBasedApplicationMetrics: true
        

**Caution:** The annotation-based workload metrics collection enabled by the `annotationBasedApplicationMetrics` feature gate collects metrics for objects that have the `prometheus.io/scrape` annotation. Many software systems with open source origin may use this annotation. Be aware of this dependency so that you aren't surprised by metrics charges in Cloud Monitoring.
  * Added optional `ksmNodePodMetricsOnly` feature gate in the stackdriver custom resource to reduce the number of metrics from kube-state-metrics. Reducing the number of metrics makes monitoring pipeline more stable in large scale clusters.

  * Audit logs are compressed on the wire for Cloud Audit Logs consumption, reducing egress bandwidth by approximately 60%.

  * Upgraded local volume provisioner to v2.5.0.

  * Upgraded snapshot controller to v5.0.1.

  * Deprecated v1beta1 volume snapshot custom resources. Anthos clusters on bare metal will stop serving v1beta1 resources in a future release.

  * Removed resource request limits on edge profile workloads.

  * Added preflight check to make sure control plane and load balancer nodes aren't under maintenance before an upgrade.

  * Updated the cluster snapshot capability so that information can be captured for the target cluster even when the cluster custom resource is missing or unavailable.

  * Improved `bmctl` error reporting for failures during the creation of a bootstrap cluster.

  * Added support for using the `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds` cluster annotation to specify the maximum node draining duration, in seconds. By default, a 20-minute (1200 seconds) timeout is enforced. When the timeout elapses, all pods are stopped and the node is put into maintenance mode. For example to change the timeout to 10 minutes, add the annotation `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds: "600"` to your cluster.

  * Updated `bmctl check cluster` to create a HealthCheck custom resource in the admin cluster if it's healthy.




1.16

Fixed

**Fixes:**

  * Fixed an issue where the apiserver could become unresponsive during a cluster upgrade for clusters with a single control plane node.

  * Fixed an issue where cluster installations or upgrades fail when the cluster name has more than 45 characters.

  * Fixed an issue where the control plane VIP wasn't reachable during cluster installation on Red Hat Enterprise Linux.

  * Fixed an issue where audit logs were duplicated into the offline buffer even when they are sent to Cloud Audit Logs successfully.

  * Fixed an issue where node-specific labels set on the node pool were sometimes overwritten.

  * Updated [`avoidBuggyIPs`](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#loadbalancer-addresspools-avoidbuggyips) and [`manualAssign`](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#loadbalancer-addresspools-manualassign) fields in load balancer address pools (`spec.loadBalancers.addressPools`) to allow changes at any time.

  * Fixed an issue where containerd didn't restart when there was a version mismatch. This issue caused an inconsistent containerd version within the cluster. 

  * Fixed an issue that caused the logging agent to use continuously increasing amounts of memory.

  * Fixed preflight check so that it no longer ignores the `no_proxy` setting. 

  * Fixed Anthos Identity Service annotation needed for exporting metrics. 

  * Fixed an issue that caused the `bmctl restore` command to stop responding for clusters with manually configured load balancers.

  * Fixed an issue that prevented Anthos clusters on bare metal from restoring a high-availability quorum for nodes that use `/var/lib/etcd` as a mountpoint. 

  * Fixed an issue that caused health checks to report failure when they find a Pod with a status of `TaintToleration` even when the replicaset for the Pod has sufficient Pods running.

  * Fixed an issue that caused conflicts with third-party Ansible automation. 

  * Fixed a cluster upgrade issue that prevented some control plane nodes from rejoining a cluster configured for high availability.




1.16

Fixed

The following container image security vulnerabilities have been fixed: 

  * Critical container vulnerabilities:

    * [CVE-2022-29155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29155)

    * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

    * [CVE-2023-0464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464)

    * [CVE-2023-0465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465)

    * [CVE-2023-0466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466)

    * [CVE-2023-2283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2283)

    * [CVE-2023-2650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650)

  * High-severity container vulnerabilities:

    * [CVE-2019-19906](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19906)

    * [CVE-2020-8032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8032)

    * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)

    * [CVE-2022-4904](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4904)

    * [CVE-2022-24407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407)

    * [CVE-2022-29154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29154)

    * [CVE-2022-32190](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32190)

    * [CVE-2023-0045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0045)

    * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)

    * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)

    * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)

    * [CVE-2023-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0386)

    * [CVE-2023-0461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0461)

    * [CVE-2023-1077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1077)

    * [CVE-2023-1078](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1078)

    * [CVE-2023-1118](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1118)

    * [CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281)

    * [CVE-2023-1670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1670)

    * [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-2454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2454)

    * [CVE-2023-3567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3567)

    * [CVE-2023-23559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23559)

    * [CVE-2023-28466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28466)

    * [CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)

    * [CVE-2023-32233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32233)

  * Medium-severity container vulnerabilities:

    * [CVE-2018-1099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1099)

    * [CVE-2019-9511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9511)

    * [CVE-2019-9513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9513)

    * [CVE-2020-11080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11080)

    * [CVE-2020-13844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13844)

    * [CVE-2021-3468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3468)

    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)

    * [CVE-2022-3707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3707)

    * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)

    * [CVE-2022-4129](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4129)

    * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)

    * [CVE-2022-4382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4382)

    * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

    * [CVE-2022-23524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23524)

    * [CVE-2022-23525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23525)

    * [CVE-2022-23526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23526)

    * [CVE-2022-36055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36055)

    * [CVE-2023-0458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0458)

    * [CVE-2023-0459](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0459)

    * [CVE-2023-1073](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1073)

    * [CVE-2023-1074](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1074)

    * [CVE-2023-1076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1076)

    * [CVE-2023-1079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1079)

    * [CVE-2023-1667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1667)

    * [CVE-2023-1855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1855)

    * [CVE-2023-1859](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1859)

    * [CVE-2023-1990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1990)

    * [CVE-2023-1998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1998)

    * [CVE-2023-2162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2162)

    * [CVE-2023-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2194)

    * [CVE-2023-2455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2455)

    * [CVE-2023-2985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2985)

    * [CVE-2023-3161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3161)

    * [CVE-2023-3220](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3220)

    * [CVE-2023-3358](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3358)

    * [CVE-2023-23916](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23916)

    * [CVE-2023-26545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26545)

    * [CVE-2023-28328](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28328)

    * [CVE-2023-28484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28484)

    * [CVE-2023-29469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29469)

    * [CVE-2023-30456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30456)

    * [CVE-2023-32269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32269)

    * [CVE-2023-33203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33203)

    * [CVE-2023-33288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33288)

  * Low-severity container vulnerabilities:

    * [CVE-2009-5155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-5155)

    * [CVE-2015-8985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-8985)

    * [CVE-2019-17594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17594)

    * [CVE-2019-17595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17595)

    * [CVE-2021-3468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3468)

    * [CVE-2022-2196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2196)

    * [CVE-2022-3424](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3424)

    * [CVE-2022-4379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4379)

    * [CVE-2023-1513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1513)

    * [CVE-2023-1611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1611)

    * [CVE-2023-1872](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1872)

    * [CVE-2023-2163](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2163)

    * [CVE-2023-21102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21102)

    * [CVE-2023-22998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22998)

    * [CVE-2023-23004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23004)

    * [CVE-2023-25012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25012)

    * [CVE-2023-30772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30772)




1.16

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## August 22, 2023

1.14

Feature

### Release 1.14.8

Anthos clusters on bare metal 1.14.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.8 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * High-severity container vulnerabilities:

    * [CVE-2017-11468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-11468)
  * Medium-severity container vulnerabilities:

    * [CVE-2019-9511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9511)

    * [CVE-2019-9513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9513)

    * [CVE-2020-11080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11080)

    * [CVE-2020-13844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13844)

  * Low-severity container vulnerabilities:

    * [CVE-2009-5155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-5155)

    * [CVE-2015-8985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-8985)




1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## August 16, 2023

1.15

Feature

### Release 1.15.4

Anthos clusters on bare metal 1.15.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). Anthos clusters on bare metal 1.15.4 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Change

**Functionality changes:**

  * Audit logs are compressed on the wire for Cloud Audit Logs consumption, reducing egress bandwidth by approximately 60%.

  * Upgraded local volume provisioner to v2.5.0.

  * Upgraded snapshot controller to v5.0.1.

  * Deprecated v1beta1 volume snapshot custom resources. Anthos clusters on bare metal will stop serving v1beta1 resources in a future release.




1.15

Fixed

**Fixes:**

  * Fixed an issue for clusters configured with manual load balancing where CA rotation reported that there were no (`0`) control plane nodes.



1.15

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * High-severity container vulnerabilities: 
    * [CVE-2017-11468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-11468)
    * [CVE-2023-0464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464)
    * [CVE-2023-2650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650)
  * Medium-severity container vulnerabilities: 
    * [CVE-2019-9511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9511)
    * [CVE-2019-9513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9513)
    * [CVE-2020-11080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11080)
    * [CVE-2020-13844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13844)
    * [CVE-2022-23524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23524)
    * [CVE-2022-23525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23525)
    * [CVE-2022-23526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23526)
    * [CVE-2022-36055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36055)
    * [CVE-2023-0465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465)
    * [CVE-2023-0466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466)
  * Low-severity container vulnerabilities: 
    * [CVE-2015-8985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-8985)
    * [CVE-2009-5155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-5155)



1.15

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## August 01, 2023

1.13

Feature

### Release 1.13.10

Anthos clusters on bare metal 1.13.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.10 runs on Kubernetes 1.24.

1.13

Change

**Functionality changes:**

  * Upgraded local volume provisioner to v2.5.0.

  * Upgraded snapshot controller to v5.0.1.

  * Deprecated v1beta1 volume snapshot custom resources. Anthos clusters on bare metal will stop serving v1beta1 resources in a future release.




1.13

Fixed

**Fixes:**

  * Fixed an issue where the apiserver could become unresponsive during a cluster upgrade for clusters with a single control plane node.

  * Fixed an issue where audit logs were duplicated into the offline buffer even when they are sent to Cloud Audit Logs successfully.




1.13

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2009-5155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-5155)

  * [CVE-2015-8985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-8985)

  * [CVE-2019-9511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9511)

  * [CVE-2019-9513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9513)

  * [CVE-2020-11080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11080)

  * [CVE-2020-13844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13844)

  * [CVE-2022-23524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23524)

  * [CVE-2022-23525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23525)

  * [CVE-2022-23526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23526)

  * [CVE-2022-36055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36055)

  * [CVE-2023-0464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464)

  * [CVE-2023-0465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465)

  * [CVE-2023-0466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466)

  * [CVE-2023-1667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1667)

  * [CVE-2023-2283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2283)

  * [CVE-2023-2454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2454)

  * [CVE-2023-2455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2455)

  * [CVE-2023-2650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650)




1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## July 25, 2023

1.14

Feature

FEATURE

### Release 1.14.7

Anthos clusters on bare metal 1.14.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.7 runs on Kubernetes 1.25.

1.14

Change

**Functionality changes:**

  * Audit logs are compressed on the wire for Cloud Audit Logs consumption, reducing egress bandwidth by approximately 60%.

  * Upgraded local volume provisioner to v2.5.0.

  * Upgraded snapshot controller to v5.0.1.

  * Deprecated v1beta1 volume snapshot custom resources. Anthos clusters on bare metal will stop serving v1beta1 resources in a future release.




1.14

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2022-23524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23524)

  * [CVE-2022-23525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23525)

  * [CVE-2022-23526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23526)

  * [CVE-2022-36055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36055)

  * [CVE-2023-0464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464)

  * [CVE-2023-0465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465)

  * [CVE-2023-0466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466)

  * [CVE-2023-1667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1667)

  * [CVE-2023-2283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2283)

  * [CVE-2023-2650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650)




1.14

Fixed

**Fixes:**

  * Fixed an issue where the smart default didn't work for `gke-metrics-agent`.

  * Fixed an issue where the apiserver could become responsive during a cluster upgrade for clusters with a single control plane node.

  * Fixed an issue where audit logs were duplicated into the offline buffer even when they are sent to Cloud Audit Logs successfully.




1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## July 20, 2023

1.15

Feature

### Release 1.15.3

Anthos clusters on bare metal 1.15.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). Anthos clusters on bare metal 1.15.3 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Feature

Anthos clusters on bare metal 1.15.3 supports adding the [`gkeOnPremAPI` section](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/cluster-config-ref#gkeonpremapi) to your admin and user cluster configuration files to [enroll the clusters in the Anthos On-Prem API](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/enroll-cluster). Enrolling the clusters in the Anthos On-Prem API lets you [upgrade admin and user clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade-on-prem-api) using the Google Cloud console or the Google Cloud CLI.

1.15

Fixed

**Fixes:**

  * Fixed an issue where the apiserver could become responsive during a cluster upgrade for clusters with a single control plane node.

  * Fixed an issue where cluster installations or upgrades fail when the cluster name has more than 45 characters.

  * Fixed an issue where node-specific labels set on the node pool were sometimes overwritten.

  * Fixed an issue where audit logs were duplicated into the offline buffer even when they are sent to Cloud Audit Logs successfully.




1.15

Fixed

The following container image security vulnerabilities have been fixed: 

  * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)

  * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

  * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

  * [CVE-2023-1667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1667)

  * [CVE-2023-2283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2283)

  * [CVE-2023-2454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2454)

  * [CVE-2023-2455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2455)




1.15

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## June 29, 2023

1.13

Feature

### Release 1.13.9

Anthos clusters on bare metal 1.13.9 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.9 runs on Kubernetes 1.24.

1.13

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2019-17594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17594)

  * [CVE-2019-17595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17595)

  * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

  * [CVE-2021-36222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36222)

  * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)

  * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)

  * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)

  * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)

  * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

  * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)

  * [CVE-2022-29178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29178)

  * [CVE-2022-29179](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29179)

  * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

  * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)

  * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)

  * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)




1.13

Issue

ISSUE Known issues:

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## June 27, 2023

1.9

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.8

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.7

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.6

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.15

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.14

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.13

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.12

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.11

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

1.10 

Security

### Security bulletin (all minor versions)

A number of vulnerabilities have been discovered in Envoy, which is used in Anthos Service Mesh (ASM). These were reported separately as [GCP-2023-002](https://cloud.google.com/support/bulletins#gcp-2023-002).

For more information, see the [GCP-2023-016](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-016) security bulletin.

## June 23, 2023

1.14

Feature

### Release 1.14.6

Anthos clusters on bare metal 1.14.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.6 runs on Kubernetes 1.25.

1.14

Change

**Functionality changes:**

  * Upgraded etcd version to v3.4.26-0-gke.0.



1.14

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2019-17594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17594)

  * [CVE-2019-17595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17595)

  * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

  * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)

  * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

  * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

  * [CVE-2022-32190](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32190)

  * [CVE-2023-2454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2454)

  * [CVE-2023-2455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2455)




1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## June 22, 2023

1.15

Feature

### Release 1.15.2

Anthos clusters on bare metal 1.15.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). Anthos clusters on bare metal 1.15.2 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Fixed

**Fixes:**

  * Fixed an issue where containerd didn't restart when there was a version mismatch. This issue caused an inconsistent containerd version within the cluster.

  * Fixed an issue where the `spec.proxy.noProxy` value wasn't used in the Google Cloud connectivity preflight check (`bmctl check gcp`).

  * Fixed an issue that caused the logging agent to use continuously increasing amounts of memory. The following container image security vulnerabilities have been fixed: 

    * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

    * [CVE-2022-32190](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32190)

    * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)

    * [CVE-2023-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0386)

    * [CVE-2023-27561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27561)

    * [CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)

    * [CVE-2023-32233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32233)




1.15

Change

**Functionality changes:**

  * Added preflight check to make sure control plane and load balancer nodes aren't in maintenance mode before an upgrade.

  * Upgraded etcd version to v3.4.26-0-gke.0.




1.15

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## June 16, 2023

1.9

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.8

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.7

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.6

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.15

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.14

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.13

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.12

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.11

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

1.10 

Security

### Security bulletin (all minor versions)

Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook ([CVE-2023-2727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2727)) or the ServiceAccount admission plugin ([CVE-2023-2728](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2728)).

For more information, see the [GCP-2023-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2023-014) security bulletin.

## June 01, 2023

1.13

Feature

### Release 1.13.8

Anthos clusters on bare metal 1.13.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.8 runs on Kubernetes 1.24.

1.13

Fixed

**Fixes:**

  * Fixed an issue that prevented Anthos clusters on bare metal from restoring a high-availability quorum for nodes that use `/var/lib/etcd` as a mountpoint.

  * Fixed an upgrade race condition between a node and the CNI, which could trigger two worker nodes to upgrade simultaneously.

  * The following container image security vulnerabilities have been fixed:

    * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

    * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)

    * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)

    * [CVE-2023-0045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0045)

    * [CVE-2023-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0386)

    * [CVE-2023-0461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0461)

    * [CVE-2023-1077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1077)

    * [CVE-2023-1078](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1078)

    * [CVE-2023-1118](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1118)

    * [CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281)

    * [CVE-2023-1670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1670)

    * [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-23559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23559)

    * [CVE-2023-28466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28466)

    * [CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)

    * [CVE-2023-32233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32233)




1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## May 31, 2023

1.15

Feature

### Release 1.15.1

Anthos clusters on bare metal 1.15.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). Anthos clusters on bare metal 1.15.1 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Change

**Functionality changes:**

  * Updated the cluster snapshot capability so that information can be captured for the target cluster even when the cluster custom resource is missing or unavailable.

  * Improved `bmctl` error reporting for failures during the creation of a bootstrap cluster.

  * Added support for using the `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds` cluster annotation to specify the maximum node draining duration, in seconds. By default, a 20-minute (1200 seconds) timeout is enforced. When the timeout elapses, all pods are stopped and the node is put into maintenance mode. For example to change the timeout to 10 minutes, add the annotation `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds: "600"` to your cluster.

  * Added `node_pool_name` to the [`anthos_baremetal_node_os_count`](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/metrics-anthos#anthos/anthos_baremetal_node_os_count) metric.




1.15

Fixed

**Fixes:**

  * Fixed an issue that caused the `bmctl restore` command to stop responding for clusters with manually configured load balancers.

  * Fixed an issue that caused health checks to report failure when they find a Pod with a status of `TaintToleration` even when the replicaset for the Pod has sufficient Pods running.

  * Fixed an issue that prevented Anthos clusters on bare metal from restoring a high-availability quorum for nodes that use `/var/lib/etcd` as a mountpoint.

  * Fixed an issue that caused conflicts with third-party Ansible automation.

  * Fixed an issue where invalid [kubelet image pull settings](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-clusters#kubelet-config), such as negative values, resulted in update job failures. Unchecked job failures generate an excessive accumulation of kubelet configuration backup files.

  * Fixed a cluster upgrade issue that prevented some control plane nodes from rejoining a cluster configured for high availability.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2018-1099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1099)
    * [CVE-2019-19906](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19906)
    * [CVE-2020-8032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8032)
    * [CVE-2021-3468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3468)
    * [CVE-2021-43784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43784)
    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)
    * [CVE-2022-2196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2196)
    * [CVE-2022-3424](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3424)
    * [CVE-2022-3707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3707)
    * [CVE-2022-4129](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4129)
    * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)
    * [CVE-2022-4379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4379)
    * [CVE-2022-4382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4382)
    * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)
    * [CVE-2022-4904](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4904)
    * [CVE-2022-24407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407)
    * [CVE-2022-29162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29162)
    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)
    * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)
    * [CVE-2023-0045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0045)
    * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
    * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)
    * [CVE-2023-0458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0458)
    * [CVE-2023-0461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0461)
    * [CVE-2023-1073](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1073)
    * [CVE-2023-1074](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1074)
    * [CVE-2023-1076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1076)
    * [CVE-2023-1077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1077)
    * [CVE-2023-1078](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1078)
    * [CVE-2023-1079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1079)
    * [CVE-2023-1118](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1118)
    * [CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281)
    * [CVE-2023-1513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1513)
    * [CVE-2023-1611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1611)
    * [CVE-2023-1670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1670)
    * [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)
    * [CVE-2023-1855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1855)
    * [CVE-2023-1872](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1872)
    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)
    * [CVE-2023-1990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1990)
    * [CVE-2023-1998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1998)
    * [CVE-2023-2162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2162)
    * [CVE-2023-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2194)
    * [CVE-2023-21102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21102)
    * [CVE-2023-22998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22998)
    * [CVE-2023-23004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23004)
    * [CVE-2023-23559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23559)
    * [CVE-2023-25012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25012)
    * [CVE-2023-26545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26545)
    * [CVE-2023-27487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27487)
    * [CVE-2023-27488](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27488)
    * [CVE-2023-27491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27491)
    * [CVE-2023-27492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27492)
    * [CVE-2023-27493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27493)
    * [CVE-2023-27496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27496)
    * [CVE-2023-28328](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28328)
    * [CVE-2023-28466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28466)
    * [CVE-2023-28484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28484)
    * [CVE-2023-29469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29469)
    * [CVE-2023-30456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30456)
    * [CVE-2023-30772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30772)
    * [CVE-2023-32269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32269)



1.15

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

## May 24, 2023

1.14

Feature

### Release 1.14.5

Anthos clusters on bare metal 1.14.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.5 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

  * Fixed an issue that caused a continuous increase in memory usage for `stackdriver-log-forwarder` Pods.
  * Fixed an issue that caused the `bmctl restore` command to stop responding for clusters with manually configured load balancers.
  * Fixed an issue that caused preflight checks to fail for clusters configured with `spec.proxy.noProxy` settings.
  * Fixed an upgrade issue where adding `upgradeStrategy.parallelUpgrade.concurrentNodes` to the NodePool spec (for a parallel upgrade) caused the upgrade operation to fail.
  * Fixed an issue that caused conflicts with third-party Ansible automation. 
  * Fixed an issue that prevented Anthos clusters on bare metal from restoring a high-availability quorum for nodes that use `/var/lib/etcd` as a mountpoint.
  * Fixed a cluster upgrade issue that prevented some control plane nodes from rejoining a cluster configured for high availability.
  * Fixed an upgrade race condition between a node and the CNI, which could result in two worker nodes to upgrade simultaneously.
  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)
    * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)
    * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)
    * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)
    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)
    * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)
    * [CVE-2023-0045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0045)
    * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
    * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)
    * [CVE-2023-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0386)
    * [CVE-2023-0461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0461)
    * [CVE-2023-1077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1077)
    * [CVE-2023-1078](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1078)
    * [CVE-2023-1118](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1118)
    * [CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281)
    * [CVE-2023-1670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1670)
    * [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)
    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)
    * [CVE-2023-23559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23559)
    * [CVE-2023-27487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27487)
    * [CVE-2023-27488](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27488)
    * [CVE-2023-27491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27491)
    * [CVE-2023-27492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27492)
    * [CVE-2023-27493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27493)
    * [CVE-2023-27496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27496)
    * [CVE-2023-28466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28466)
    * [CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)
    * [CVE-2023-32233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32233)



1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## May 10, 2023

1.9

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.8

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.7

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.6

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.15

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.14

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.13

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.12

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.11

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

1.10 

Deprecated

### CentOS Linux 8 Support Deprecated

CentOS Linux 8 reached its end of life (EOL) on December 31st, 2021. We strongly recommend that you migrate to one of the other [supported operating systems](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/os-reqs) from Anthos clusters on bare metal. All support for CentOS is removed from Anthos clusters for bare metal release 1.17 (December 2023) and subsequent releases.

## April 27, 2023

1.15

Feature

### Release 1.15.0

Anthos clusters on bare metal 1.15.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/upgrade). Anthos clusters on bare metal 1.15.0 runs on Kubernetes 1.26.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

1.15

Announcement

**Version 1.12 end of life:** In accordance with the [Anthos Version Support Policy](https://cloud.google.com/anthos/docs/support/getting-support#version_support_policy), version 1.12 (all patch releases) of Anthos clusters on bare metal has reached its end of life and is no longer supported.

1.15

Feature

**Cluster lifecycle:**

  * Upgraded from Kubernetes version 1.25 to version 1.26. 
  * **GA:** Set in-place upgrade (without bootstrap cluster) as the [default upgrade method](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade) for self-managed clusters. 
  * **GA:** Added support for configuring worker node pools for [parallel node upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#parallel_upgrades) to significantly reduce upgrade times. Added a `minimumAvailableNodes` field to specify a minimum number of nodes to keep available for workloads throughout the upgrade.
  * **Preview:** Added support for [parallel upgrades of worker node pools](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#cw-strategy).
  * Added support for Red Hat Enterprise Linux (RHEL) version 8.7. 
  * Added support for Ubuntu 22.04 LTS.
  * **GA:** Added support for increasing the number of IP addresses for Services after cluster creation. For more information, see [Increase service network range](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-clusters#increase_service_network_range).
  * **Preview:** Added ability to configure kubelet image pull settings for node pools. For more information, see [Configure kubelet image pull settings](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-clusters#kubelet-config). 
  * Streamlined the [snapshot uploading and sharing](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/bmctl-snapshot#method_1_create_default_snapshot_and_automatically_upload_to_bucket) process.
  * **GA:** Added support of Control group v2 (cgroup v2).
  * **Preview:** Added a separate instance of etcd for the `etcd-events` object.
  * Updated `cert-manager` to version 1.17.2.
  * Updated automated API enablement when you run `bmctl create config` with the `--enable-apis` flag. The following APIs are added to the enablement list: 
    * Enable `storage.googleapis.com` as a required API.
    * Enable `gkeonprem.googleapis.com` as a recommended API.
  * Added a new field `status.failures` to the NodePool custom resource to aggregate failures across machines in the NodePool.
  * Added a new condition type `PreflightCheckSuccessful` to the NodePool custom resource. This condition type summarizes the preflight check status across machines in the NodePool.



**Networking:**

  * Added support for ClusterDNS to specify order for `upstreamNameServers` with an `orderPolicy`. Allowed values for `orderPolicy` are `random`, `round_robin`, or `sequential`. The default value is `random`.



**Observability:**

  * Added support for filtering application logs. This feature can reduce application logging billing and network traffic from the cluster to Cloud Logging. For more information, see [Filter application logs](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/application-logging-monitoring#filter_application_logs).
  * **GA:** Fully managed Cloud Monitoring Integration dashboards:

    * In the next Anthos release (version 1.16), the following dashboards in Cloud Monitoring Sample Library are unavailable: 
      * Anthos cluster control plane uptime
      * Anthos cluster node status
      * Anthos cluster pod status
      * Anthos utilization metering
      * GKE on-prem node status
      * GKE on-prem control plane uptime
      * GKE on-prem pod status
      * GKE on-prem vSphere vm health status
    * In the next Anthos release (version 1.16), the following customized dashboards aren't created when you create a new cluster: 
      * Anthos cluster control plane uptime
      * Anthos cluster pod status
      * Anthos cluster node status
      * Anthos cluster VM status
    * An added **Anthos** integration page is available from the Cloud Monitoring **Integration** page. The **Anthos** integration includes descriptions and previews for the predefined Anthos dashboards: 
      * Anthos Cluster Control Plane Uptime
      * Anthos Cluster Node Status
      * Anthos Cluster Pod Status
      * Anthos Cluster KubeVirt VM Status
      * Anthos Cluster Utilization Metering

For more information, see [Use predefined dashboards](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/reference/predefined-dashboards).

  * **Preview:** Added [support for system metrics](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/log-monitoring#using-managed-service-for-prometheus) when you use Google Cloud Managed Service for Prometheus. 




**Security and Identity:**

  * **Preview:** Added support for Binary Authorization, a service on Google Cloud that provides software supply-chain security for container-based applications. For more information, see [Binary Authorization for Anthos clusters overview](https://cloud.google.com/binary-authorization/docs/overview-on-prem).
  * **Preview:** Added support for VPC Service Controls, which provides additional security for your clusters to help mitigate the risk of data exfiltration. 
  * Improved security by disabling port 10255, the kubelet read-only port, by default. For more information, see [Disable kubelet read-only port](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/how-to/hardening-your-cluster#kubelet-ro) in Hardening your cluster's security.



1.15

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/troubleshooting/known-issues) in the Troubleshooting section.

1.15

Fixed

**Fixes:**

  * Fixed an issue that caused the `bmctl reset nodes` command to fail if the `bmctl-workspace` directory was empty.
  * Fixed an intermittent issue that caused the `bmctl upgrade cluster` command to indicate that the operation was complete before the cluster was in a ready state.



1.15

Change

**Functionality changes:**

  * Replacing taints and labels. Clusters created and upgraded to Anthos clusters on bare metal version 1.15.0 and higher have `node-role.kubernetes.io/control-plane:*` taints and `node-role.kubernetes.io/control-plane` labels. These new taints and labels replace the `node-role.kubernetes.io/master` label and `node-role.kubernetes.io/master:*` taints on new and upgraded control plane nodes.



**Networking changes:**

  * Replaced the anetd CNI plugin for the bootstrap cluster with [kindnet](https://github.com/aojea/kindnet).
  * Increased eBPF map limit to 512 K to allow for more load balancer Services.
  * Upgraded CoreDNS to version 1.9.4.



**Anthos VM Runtime:**

  * Moved the Anthos VM Runtime release notes to a [separate page](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.15/vm-runtime/release-notes) in the Anthos VM Runtime documentation section.



## April 25, 2023

1.13

Feature

### Release 1.13.7

Anthos clusters on bare metal 1.13.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.7 runs on Kubernetes 1.24.

1.13

Fixed

**Fixes:**

The following container image security vulnerability has been fixed: 

  * [CVE-2022-23824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23824)
  * [CVE-2022-42331](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42331)
  * [CVE-2022-42332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42332)
  * [CVE-2022-42333](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42333)
  * [CVE-2022-42334](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42334)



1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## April 19, 2023

1.14

Feature

### Release 1.14.4

Anthos clusters on bare metal 1.14.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.4 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-3711](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3711)
  * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)
  * [CVE-2021-40528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40528)
  * [CVE-2022-23824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23824)
  * [CVE-2022-42331](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42331)
  * [CVE-2022-42332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42332)
  * [CVE-2022-42333](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42333)
  * [CVE-2022-42334](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42334)
  * [CVE-2022-48303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48303)
  * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)
  * [CVE-2023-23916](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23916)



1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## April 12, 2023

1.9

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.8

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.7

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.6

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.14

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.13

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.12

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.11

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

1.10 

Announcement

### Kubernetes image registry redirect

As of March 21, 2023, traffic to `k8s.gcr.io` is redirected to `registry.k8s.io`, following the [community announcement](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/). This change is happening gradually to reduce disruption, and should be transparent for most Anthos clusters.

To check for edge cases and mitigate potential impact to your clusters, follow the step-by-step guidance in [k8s.gcr.io Redirect to registry.k8s.io - What You Need to Know](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/#how-can-i-check-if-i-am-impacted).

## March 31, 2023

1.14

Feature

**Cluster lifecycle improvements 1.13.1 and later**

Starting with Anthos clusters on bare metal release 1.13.1, you can use the Google Cloud console or the gcloud CLI to create admin clusters. For more information, see the documentation for your version of Anthos clusters on bare metal:

  * 1.13: [Create an admin cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/installing/creating-clusters/create-admin-cluster-api)

  * 1.14: [Create an admin cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-admin-cluster-api)




1.13

Feature

**Cluster lifecycle improvements 1.13.1 and later**

Starting with Anthos clusters on bare metal release 1.13.1, you can use the Google Cloud console or the gcloud CLI to create admin clusters. For more information, see the documentation for your version of Anthos clusters on bare metal:

  * 1.13: [Create an admin cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/installing/creating-clusters/create-admin-cluster-api)

  * 1.14: [Create an admin cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-admin-cluster-api)




## March 28, 2023

1.12

Feature

### Release 1.12.9

Anthos clusters on bare metal 1.12.9 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.9 runs on Kubernetes 1.23.

1.12

Fixed

**FIxes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-41990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41990)
  * [CVE-2021-41991](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41991)
  * [CVE-2021-45079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45079)
  * [CVE-2022-40617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40617)
  * [CVE-2023-23916](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23916)



1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## March 24, 2023

1.14

Feature

### Release 1.14.3

Anthos clusters on bare metal 1.14.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade). Anthos clusters on bare metal 1.14.3 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

  * Improved maintenance mode operation by ignoring non-running pods on nodes.
  * Updated etcd version to version 3.4.21-0-gke.1 to resolve an issue that could lead to watch starvation and non-operational watch for resources.
  * Updated kubernetes version to 1.25.6-gke.1000 to honor exponential backoff in job controller.
  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-3449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3449)
    * [CVE-2021-41990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41990)
    * [CVE-2021-41991](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41991)
    * [CVE-2021-45079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45079)
    * [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778)
    * [CVE-2022-1292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1292)
    * [CVE-2022-2068](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2068)
    * [CVE-2022-40617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40617)



1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/troubleshooting/known-issues) in the Troubleshooting section.

## March 21, 2023

1.13

Feature

### Release 1.13.6

Anthos clusters on bare metal 1.13.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.6 runs on Kubernetes 1.24.

1.13

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-3449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3449)
  * [CVE-2021-3711](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3711)
  * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)
  * [CVE-2021-40528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40528)
  * [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778)
  * [CVE-2022-1292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1292)
  * [CVE-2022-2068](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2068)
  * [CVE-2022-45142](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45142)
  * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
  * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)



1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## March 09, 2023

1.14

Feature

**Cluster lifecycle improvements 1.13.1 and later**

Starting with Anthos clusters on bare metal release 1.13.1, you can use the Google Cloud console or the gcloud CLI to upgrade admin and user clusters managed by the Anthos On-Prem API. If your cluster is at version 1.13.0 or lower, you must use `bmctl` to upgrade the cluster.

For more information about using the console or the gcloud CLI for upgrades, see the documentation for your version of Anthos clusters on bare metal:

  * 1.13: [Upgrade an admin or user cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade-on-prem-api)

  * 1.14: [Upgrade an admin or user cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade-on-prem-api)




1.13

Feature

**Cluster lifecycle improvements 1.13.1 and later**

Starting with Anthos clusters on bare metal release 1.13.1, you can use the Google Cloud console or the gcloud CLI to upgrade admin and user clusters managed by the Anthos On-Prem API. If your cluster is at version 1.13.0 or lower, you must use `bmctl` to upgrade the cluster.

For more information about using the console or the gcloud CLI for upgrades, see the documentation for your version of Anthos clusters on bare metal:

  * 1.13: [Upgrade an admin or user cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade-on-prem-api)

  * 1.14: [Upgrade an admin or user cluster using Anthos On-Prem API clients](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade-on-prem-api)




## March 02, 2023

1.12

Feature

### Release 1.12.8

Anthos clusters on bare metal 1.12.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.8 runs on Kubernetes 1.23.

1.12

Fixed

**Fixes:**

  * Updated Anthos Identity Service to better handle concurrent authentication webhook requests.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2018-20217](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20217)
    * [CVE-2022-2873](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2873)
    * [CVE-2022-3545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3545)
    * [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
    * [CVE-2022-36280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36280)
    * [CVE-2022-41218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41218)
    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)
    * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)
    * [CVE-2022-45934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45934)
    * [CVE-2022-47929](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47929)
    * [CVE-2023-23454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23454)
    * [CVE-2023-23455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23455)



1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## March 01, 2023

1.14

Feature

### Release 1.14.2

Anthos clusters on bare metal 1.14.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.14.2 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

  * Updated Anthos Identity Service to better handle concurrent authentication webhook requests.
  * Updated `stackdriver-operator` to set CPU and memory resource limits.
  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2018-20217](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20217)
    * [CVE-2022-2873](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2873)
    * [CVE-2022-3545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3545)
    * [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
    * [CVE-2022-36280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36280)
    * [CVE-2022-41218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41218)
    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)
    * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)
    * [CVE-2022-43552](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43552)
    * [CVE-2022-45934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45934)
    * [CVE-2022-47629](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47629)
    * [CVE-2022-47929](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47929)
    * [CVE-2023-23454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23454)
    * [CVE-2023-23455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23455)



1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## February 23, 2023

1.13

Feature

### Release 1.13.5

Anthos clusters on bare metal 1.13.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.5 runs on Kubernetes 1.24.

1.13

Fixed

**Fixes:**

  * Updated Anthos Identity service to better handle concurrent authentication webhook requests.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2018-20217](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20217)
    * [CVE-2022-2873](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2873)
    * [CVE-2022-3545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3545)
    * [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
    * [CVE-2022-36280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36280)
    * [CVE-2022-41218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41218)
    * [CVE-2022-43552](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43552)
    * [CVE-2022-45934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45934)
    * [CVE-2022-47929](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47929)
    * [CVE-2023-23454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23454)
    * [CVE-2023-23455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23455)



1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## February 07, 2023

1.12

Feature

### Release 1.12.7

Anthos clusters on bare metal 1.12.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.7 runs on Kubernetes 1.23.

1.12

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-3759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3759)
  * [CVE-2021-46848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46848)
  * [CVE-2022-3169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3169)
  * [CVE-2022-3524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3524)
  * [CVE-2022-3542](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3542)
  * [CVE-2022-3564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3564)
  * [CVE-2022-3565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3565)
  * [CVE-2022-3594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3594)
  * [CVE-2022-3640](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3640)
  * [CVE-2022-41849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41849)
  * [CVE-2022-41850](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41850)
  * [CVE-2022-42895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42895)
  * [CVE-2022-42896](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42896)
  * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)
  * [CVE-2022-43552](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43552)



1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## January 27, 2023

1.14

Issue

### 1.14.0 Upgrade problem

Control plane nodes for Anthos clusters on bare metal use [Kubernetes taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to prevent workload pods from being scheduled on them. When you upgrade version 1.13 Anthos clusters to version 1.14.0, the control plane nodes lose required taints. We recommend that you skip upgrading to version 1.14.0 and upgrade to version 1.14.1 directly.

This problem doesn't cause upgrade failures, but pods that aren't supposed to run on the control plane nodes may start doing so. These workload pods can overwhelm control plane nodes and lead to cluster instability. This issue has security implications, as well. We strongly recommend that you not upgrade your clusters to version 1.14.0, but upgrade instead to a subsequent release version with the fix.

For more information about the issue, including workaround instructions, see the [Clusters upgraded to 1.14.0 lose master taints](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues#master-taints) known issue.

1.14

Feature

### Release 1.14.1

Anthos clusters on bare metal 1.14.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.14.1 runs on Kubernetes 1.25.

1.14

Fixed

**Fixes:**

  * Fixed an issue with the anthos-cluster-operator that caused CertificateSigningRequest (CSR) events to be missed during reconciliation steps. The lack of signing resulted in Istio crashlooping.
  * Fixed an issue that prevented the Pod CIDR for nodes from being adjusted from the default /24 mask size to account for the maxPodsPerNode cluster setting. 
  * Fixed an [issue](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues#master-taints) that removed taints from control plane nodes when upgrading clusters to version 1.14.0.
  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-3759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3759)
    * [CVE-2021-46848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46848)
    * [CVE-2022-3169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3169)
    * [CVE-2022-3524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3524)
    * [CVE-2022-3564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3564)
    * [CVE-2022-3565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3565)
    * [CVE-2022-3594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3594)
    * [CVE-2022-3640](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3640)
    * [CVE-2022-3643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3643)
    * [CVE-2022-40303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40303)
    * [CVE-2022-40304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40304)
    * [CVE-2022-41849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41849)
    * [CVE-2022-41850](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41850)
    * [CVE-2022-42328](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42328)
    * [CVE-2022-42329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42329)
    * [CVE-2022-42895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42895)
    * [CVE-2022-42896](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42896)
    * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)
    * [CVE-2022-44638](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44638)
    * [CVE-2022-47518](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47518)
    * [CVE-2022-47519](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47519)
    * [CVE-2022-47520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47520)
    * [CVE-2022-47521](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47521)



1.14

Change

**Functionality changes:**

  * Changed the behavior for periodic health checks during upgrades. Now, during the upgrade process, existing periodic health checks continue to run in the admin cluster. Once the cluster is upgraded to the next version, the previous version periodic health checks are replaced with periodic health checks for the new version.
  * Lowered the priority of health check jobs to minimize contention for resources.
  * Changed the etcd history compaction interval from the default of 5 minutes to 2.5 minutes. This value is set in the `kube-apiserver.yaml` file.



1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## January 26, 2023

1.13

Feature

### Release 1.13.4

Anthos clusters on bare metal 1.13.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.4 runs on Kubernetes 1.24.

1.13

Fixed

Fixed an issue with the `anthos-cluster-operator` that caused CertificateSigningRequest (CSR) events to be missed during reconciliation steps. The lack of signing resulted in Istio crashlooping.

1.13

Fixed

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-3759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3759)
  * [CVE-2021-4037](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4037)
  * [CVE-2021-46848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46848)
  * [CVE-2022-1184](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1184)
  * [CVE-2022-20421](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20421)
  * [CVE-2022-2978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2978)
  * [CVE-2022-3169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3169)
  * [CVE-2022-3176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3176)
  * [CVE-2022-3524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3524)
  * [CVE-2022-3564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3564)
  * [CVE-2022-3565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3565)
  * [CVE-2022-3586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3586)
  * [CVE-2022-3594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3594)
  * [CVE-2022-3621](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3621)
  * [CVE-2022-3640](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3640)
  * [CVE-2022-3643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3643)
  * [CVE-2022-3646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3646)
  * [CVE-2022-3903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3903)
  * [CVE-2022-39188](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39188)
  * [CVE-2022-40303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40303)
  * [CVE-2022-40304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40304)
  * [CVE-2022-40307](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40307)
  * [CVE-2022-41849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41849)
  * [CVE-2022-41850](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41850)
  * [CVE-2022-41916](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41916)
  * [CVE-2022-42010](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42010)
  * [CVE-2022-42011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42011)
  * [CVE-2022-42012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42012)
  * [CVE-2022-42328](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42328)
  * [CVE-2022-42329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42329)
  * [CVE-2022-42895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42895)
  * [CVE-2022-42896](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42896)
  * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)
  * [CVE-2022-43680](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43680)
  * [CVE-2022-43750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43750)
  * [CVE-2022-44638](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44638)
  * [CVE-2022-47518](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47518)
  * [CVE-2022-47519](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47519)
  * [CVE-2022-47520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47520)
  * [CVE-2022-47521](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47521)



1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## December 21, 2022

1.14

Announcement

Anthos clusters on bare metal release 1.14.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). Note that Anthos clusters on bare metal version 1.14.0 runs on Kubernetes 1.25. Multiple [deprecated APIs are deleted in Kubernetes 1.25](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-25). Before you upgrade version 1.13 Anthos clusters to version 1.14, [check to see if you are affected by the Kubernetes API deletions](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/deleted-apis-kubernetes-1_25).

If you aren't affected by the API deletions, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade) in the 1.14 documentation for upgrade instructions.

1.13

Announcement

Anthos clusters on bare metal release 1.14.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/downloads). Note that Anthos clusters on bare metal version 1.14.0 runs on Kubernetes 1.25. Multiple [deprecated APIs are deleted in Kubernetes 1.25](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-25). Before you upgrade version 1.13 Anthos clusters to version 1.14, [check to see if you are affected by the Kubernetes API deletions](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/deleted-apis-kubernetes-1_25).

If you aren't affected by the API deletions, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.14/how-to/upgrade) in the 1.14 documentation for upgrade instructions.

## December 19, 2022

1.13

Feature

**Release 1.13.3**

Anthos clusters on bare metal 1.13.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/how-to/upgrade). Anthos clusters on bare metal 1.13.3 runs on Kubernetes 1.24.

1.13

Fixed

The following container image security vulnerabilities have been fixed:

  * [CVE-2022-35737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-35737)
  * [CVE-2022-42311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42311)
  * [CVE-2022-33745](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33745)
  * [CVE-2022-42309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42309)
  * [CVE-2022-42320](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42320)
  * [CVE-2022-42323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42323)
  * [CVE-2022-33748](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33748)
  * [CVE-2022-42321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42321)
  * [CVE-2022-33746](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33746)
  * [CVE-2022-42310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42310)
  * [CVE-2022-42316](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42316)
  * [CVE-2022-42322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42322)
  * [CVE-2022-42319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42319)
  * [CVE-2022-42325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42325)
  * [CVE-2022-42315](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42315)
  * [CVE-2022-42324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42324)
  * [CVE-2022-42314](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42314)
  * [CVE-2022-42317](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42317)
  * [CVE-2022-42312](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42312)
  * [CVE-2022-42318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42318)
  * [CVE-2022-42313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42313)
  * [CVE-2022-42326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42326)



1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.13/troubleshooting/known-issues) in the Troubleshooting section.

## December 14, 2022

1.12

Feature

**Release 1.12.6**

Anthos clusters on bare metal 1.12.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.6 runs on Kubernetes 1.23.

1.12

Fixed

The following container image security vulnerabilities have been fixed: 

  * [CVE-2022-44638](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44638)

  * [CVE-2022-23491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23491)

  * [CVE-2022-41916](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41916)

  * [CVE-2022-35737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-35737)




1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## December 13, 2022

1.14

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

1.14

Feature

**Improved cluster lifecycle functionalities:**

  * Upgraded from Kubernetes version 1.24 to 1.25.

  * Enabled customers to run the latest health and preflight checks by running the command `bmctl check cluster –check-image-version=latest`. Setting the `check-image-version` flag to 'latest' ensures that clusters are examined for more recent issues, including issues discovered after a release.

  * **Preview:** Added support of Control group v2 (cgroup v2).

  * **GA:** Added automatic reservation of CPU and memory resources on cluster nodes so that system daemons have the resources they require.

  * Optimized the consumption of resources by components such as `cluster-operator`, `cap-manager`, `preflight-check operator`, and `lifecycle-controllers-manager`.

  * **GA:** Enabled automatic and periodic health checks on all clusters.




**Networking:**

  * **Preview:** Added support for turning on kube-proxy-free mode for cluster objects. WARNING: This operation is not reversible. Once enabled, it cannot be disabled.

  * Changed behavior of Dataplane V2 so that it drops a packet if no service backends are available. Previously, the packet was passed to the kernel stack.

  * Enabled automatic API rate limit adjustments in Dataplane V2.




**Observability:**

  * Added severity level to container logs.

  * Enabled collection of uptime and other Kubernetes resource metrics from the kubelet summary API.

  * Enabled Stackdriver log forwarder in the bootstrap cluster. This log forwarder publishes bootstrap container logs to Cloud Logging.




**Security and Identity:**

  * **GA:** Added feature enabling cluster administrators to configure RBAC policies based on Azure Active Directory (AD) groups. Groups information for users belonging to more than 200 groups can now be retrieved.

  * **GA:** Added secure computing mode (seccomp) support. Running containers with a seccomp profile improves the security of a cluster because it restricts the system calls that containers are allowed to make to the kernel.

  * Added annotation in the cluster configuration file which allows customers to disable the kubelet read-only port. After disabling the read-only port, customers have to change their cluster configurations so that workloads use the kubelet secure port.




**VM Runtime:**

  * **GA:** Added support for guest OS booting of UEFI. Previously, only BIOS was supported.

  * **Preview:** Enabled [Terraform scripting](https://www.terraform.io/) to create VMs on an Anthos cluster. For more information, including usage instructions, an input reference, and examples, see the [terraform-google-anthos-vm](https://github.com/GoogleCloudPlatform/terraform-google-anthos-vm) GitHub repository.

  * **Preview:** Add support for non-uniform memory access (NUMA) awareness. When enabled, all communication within the VM is local to the NUMA node, thus avoiding the performance cost of data transactions with remote memory locations.

  * **Preview:** Enabled multicast traffic for VMs.

  * Added Anthos VM Runtime preflight checks to validate hardware accelerator configuration.

  * Enabled configuration of storage's volume mode (block or filesystem) and access modes, such as RWO and RWX.

  * Enabled means to configure the storage class of a scratch space. A scratch space is sometimes required when importing or uploading a VM disk image.

  * Added support for configuring `cloud-init`, using `virtctl`.

  * Enabled ability to disable auto-installation of the guest agent binary. After the initial guest agent installation, you can set the `autoInstallGuestAgent` flag to `false` so that the binary doesn't mount in subsequent restarts.

  * Enabled the support of multiple network interfaces, by default, for all clusters.

  * Improved security for creating a VM with `kubectl virt create`. If an initial password is specified, it is now stored in a secret and not as a VM annotation.

  * Reduced the permissions of the network controller.

  * Changed default to always use Asynchronous IO mode (AIO) in order to reduce QEMU memory pressure.

  * Added VM creation and disk provisioning times to Prometheus metrics.

  * Added support for the Tesla T4 GPU.

  * Enabled reset of GPU card to its original status when GPU functionality is disabled.

  * Enabled ability to disable Anthos VM Runtime when it's in the enabling state and custom resource definitions haven't yet been installed.

  * Added the following command, which allows you to display the VM screen: `kubectll virt vnc --screenshot VM_NAME`.

  * Fixed the IP address update for Windows guest VMs.

  * Resolved the [MacVTap](https://virt.kernelnewbies.org/MacVTap) interface creation failure which occurred when the name of the interface was too long.

  * Fixed attaching VM disk using SATA driver.

  * Fixed issue so that setting `disableCDIUploadProxyVIP` to true correctly disables the `cdi-uploadproxy` service.

  * Fixed issue so that specifying a `PersistentVolumeClaim` (PVC) with an empty underlying `PersistentVolume` (PV) correctly creates the underlying empty disk format (raw or qcow2).

  * Enforced VM names to follow the standard [RFC1123](https://www.rfc-editor.org/rfc/rfc1123) format.

  * Fixed issue so that ISO image is correctly imported from a Cloud Storage bucket.

  * Fixed benign crash looping of the NVIDIA device plugin and the Multi-Instance GPU (MIG) manager when all GPU cards are allocated to a VM.

  * Fixed issue so that `virt-launcher` Pod can be created when advanced compute is enabled.




1.14

Feature

### Release 1.14.0

Anthos clusters on bare metal 1.14.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.14.0 runs on Kubernetes 1.25.

## December 09, 2022

1.12

Feature

### Release 1.12.5

Anthos clusters on bare metal 1.12.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.5 runs on Kubernetes 1.23.

1.12

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2019-25013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-25013)
  * [CVE-2021-3326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3326)
  * [CVE-2021-3999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3999)
  * [CVE-2021-4037](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4037)
  * [CVE-2021-33574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33574)
  * [CVE-2021-35942](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35942)
  * [CVE-2022-1184](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1184)
  * [CVE-2022-1586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1586)
  * [CVE-2022-1587](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1587)
  * [CVE-2022-2663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2663)
  * [CVE-2022-3061](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3061)
  * [CVE-2022-3176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3176)
  * [CVE-2022-3303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3303)
  * [CVE-2022-3586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3586)
  * [CVE-2022-3621](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3621)
  * [CVE-2022-3646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3646)
  * [CVE-2022-3649](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3649)
  * [CVE-2022-20421](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20421)
  * [CVE-2022-23218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23218)
  * [CVE-2022-23219](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23219)
  * [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
  * [CVE-2022-33745](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33745)
  * [CVE-2022-33746](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33746)
  * [CVE-2022-33748](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33748)
  * [CVE-2022-34903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-34903)
  * [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)
  * [CVE-2022-39188](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39188)
  * [CVE-2022-40307](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40307)
  * [CVE-2022-42309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42309)
  * [CVE-2022-42310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42310)
  * [CVE-2022-42311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42311)
  * [CVE-2022-42312](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42312)
  * [CVE-2022-42313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42313)
  * [CVE-2022-42314](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42314)
  * [CVE-2022-42315](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42315)
  * [CVE-2022-42316](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42316)
  * [CVE-2022-42317](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42317)
  * [CVE-2022-42318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42318)
  * [CVE-2022-42319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42319)
  * [CVE-2022-42320](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42320)
  * [CVE-2022-42321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42321)
  * [CVE-2022-42322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42322)
  * [CVE-2022-42323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42323)
  * [CVE-2022-42324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42324)
  * [CVE-2022-42325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42325)
  * [CVE-2022-42326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42326)
  * [CVE-2022-43680](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43680)
  * [CVE-2022-43750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43750)



1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## November 22, 2022

1.13

Feature

### Release 1.13.2

Anthos clusters on bare metal 1.13.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.13.2 runs on Kubernetes 1.24.

1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

1.13

Fixed

**Fixes:**

  * Ensured the `kubeadmconfig` Secret is deleted when a Cluster API node is removed.
  * Added preflight check command (`bmctl check preflight`) that you can use when upgrading version 1.13 and higher clusters.
  * Updated the commands `bmctl check preflight` and `bmctl create cluster` so that they fail if worker or control-plane nodes have docker credentials in `/root/.docker/config.json`. (Anthos clusters on bare metal version 1.13 and higher can no longer use Docker Engine as a container runtime. All clusters must use the default container runtime `containerd`). 
  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2022-1586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1586)
    * [CVE-2022-1587](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1587)
    * [CVE-2022-3116](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3116)
    * [CVE-2021-3999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3999)
    * [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)
    * [CVE-2022-41715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41715)



## November 18, 2022

1.11

Feature

### Release 1.11.8

Anthos clusters on bare metal 1.11.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/upgrade). Anthos clusters on bare metal 1.11.8 runs on Kubernetes 1.22.

1.11

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed:

  * [CVE-2019-25013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-25013)
  * [CVE-2020-16156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-16156)
  * [CVE-2021-3326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3326)
  * [CVE-2021-3999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3999)
  * [CVE-2021-4037](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4037)
  * [CVE-2021-33574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33574)
  * [CVE-2021-35942](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35942)
  * [CVE-2022-1184](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1184)
  * [CVE-2022-1586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1586)
  * [CVE-2022-1587](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1587)
  * [CVE-2022-2663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2663)
  * [CVE-2022-3061](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3061)
  * [CVE-2022-3116](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3116)
  * [CVE-2022-3176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3176)
  * [CVE-2022-3303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3303)
  * [CVE-2022-3586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3586)
  * [CVE-2022-3621](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3621)
  * [CVE-2022-3646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3646)
  * [CVE-2022-3649](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3649)
  * [CVE-2022-20421](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20421)
  * [CVE-2022-23218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23218)
  * [CVE-2022-23219](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23219)
  * [CVE-2022-33745](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33745)
  * [CVE-2022-33746](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33746)
  * [CVE-2022-33748](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-33748)
  * [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)
  * [CVE-2022-39188](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39188)
  * [CVE-2022-40307](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40307)
  * [CVE-2022-42309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42309)
  * [CVE-2022-42310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42310)
  * [CVE-2022-42311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42311)
  * [CVE-2022-42312](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42312)
  * [CVE-2022-42313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42313)
  * [CVE-2022-42314](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42314)
  * [CVE-2022-42315](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42315)
  * [CVE-2022-42316](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42316)
  * [CVE-2022-42317](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42317)
  * [CVE-2022-42318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42318)
  * [CVE-2022-42319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42319)
  * [CVE-2022-42320](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42320)
  * [CVE-2022-42321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42321)
  * [CVE-2022-42322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42322)
  * [CVE-2022-42323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42323)
  * [CVE-2022-42324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42324)
  * [CVE-2022-42325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42325)
  * [CVE-2022-42326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42326)
  * [CVE-2022-43750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43750)



1.11

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues) in the Troubleshooting section.

## November 08, 2022

1.12

Feature

### Release 1.12.4

Anthos clusters on bare metal 1.12.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.4 runs on Kubernetes 1.23.

1.12

Fixed

**Fixes:**

  * Increased the CPU limit for the `metrics-server` Pod to prevent it from frequently restarting.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2022-40674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40674)
    * [CVE-2022-3172](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3172)
    * [CVE-2022-39278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39278)
    * [CVE-2022-2509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2509)
    * [CVE-2022-1679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1679)
    * [CVE-2022-20422](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20422)
    * [CVE-2022-3028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3028)
    * [CVE-2022-2153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2153)
    * [CVE-2022-42703](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42703)
    * [CVE-2022-2526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2526)
    * [CVE-2020-35525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-35525)



1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## November 07, 2022

1.13

Security

### Security bulletin (1.11, 1.12, and 1.13)

A security vulnerability, [CVE-2022-39278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39278), has been discovered in Istio, which is used in Anthos Service Mesh, that allows a malicious attacker to crash the control plane.

For instructions and more details, see the [Anthos clusters on bare metal security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-023).

1.12

Security

### Security bulletin (1.11, 1.12, and 1.13)

A security vulnerability, [CVE-2022-39278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39278), has been discovered in Istio, which is used in Anthos Service Mesh, that allows a malicious attacker to crash the control plane.

For instructions and more details, see the [Anthos clusters on bare metal security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-023).

1.11

Security

### Security bulletin (1.11, 1.12, and 1.13)

A security vulnerability, [CVE-2022-39278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39278), has been discovered in Istio, which is used in Anthos Service Mesh, that allows a malicious attacker to crash the control plane.

For instructions and more details, see the [Anthos clusters on bare metal security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-023).

## November 01, 2022

1.13

Feature

**Cluster lifecycle improvements in 1.13 and later**

**Preview** : You can use the Google Cloud console to [create user clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-user-cluster-api), [delete user clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/reset-nodes), and to [add and remove node pools from a user cluster](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/add-remove-node-pools). To explore the new feature, try out the tutorial [Create an Anthos on bare metal user cluster on Compute Engine VMs using the console](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/try/admin-user-gce-vms).

## October 31, 2022

1.13

Feature

### Release 1.13.1

Anthos clusters on bare metal 1.13.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.13.1 runs on Kubernetes 1.24.

1.13

Fixed

**Fixes:**

  * Increased the CPU limit for the `metrics-server` Pod to prevent it from frequently restarting.
  * Updated the command `bmctl enable/disable vmruntime` to block the CLI and periodically show the status of VMRuntime. The CLI remains blocked until the command has finished and VMRuntime's ready status is true, or until a default period of 10 mins has expired.
  * Removed deprecated `IPv6DualStack` `featureGate` field that blocks clusters from upgrading to Anthos clusters on bare metal version 1.13.0.
  * Fixed the `no path ID mapping for prefix` error that sometimes occurred when `bgpd` updated `bgpsession`.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)
    * [CVE-2021-22924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22924)
    * [CVE-2021-22946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22946)
    * [CVE-2021-22947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22947)
    * [CVE-2021-23840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23840)
    * [CVE-2021-23841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23841)
    * [CVE-2021-3999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3999)
    * [CVE-2021-43618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43618)
    * [CVE-2021-46828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46828)
    * [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778)
    * [CVE-2022-1292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1292)
    * [CVE-2022-1586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1586)
    * [CVE-2022-1587](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1587)
    * [CVE-2022-1664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1664)
    * [CVE-2022-1679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1679)
    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)
    * [CVE-2022-2257](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2257)
    * [CVE-2022-2509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2509)
    * [CVE-2022-2509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2509)
    * [CVE-2022-2526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2526)
    * [CVE-2022-27776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27776)
    * [CVE-2022-27781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27781)
    * [CVE-2022-27782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27782)
    * [CVE-2022-3172](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3172)
    * [CVE-2022-32206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32206)
    * [CVE-2022-32208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32208)
    * [CVE-2022-34903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-34903)
    * [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)
    * [CVE-2022-39278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39278)
    * [CVE-2022-40674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40674)



1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## October 28, 2022

1.11

Feature

Anthos clusters on bare metal 1.11.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/upgrade). Anthos clusters on bare metal 1.11.7 runs on Kubernetes 1.22.

1.11

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed:

  * [CVE-2022-40674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40674)
  * [CVE-2022-2509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2509)
  * [CVE-2021-46828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46828)
  * [CVE-2022-3172](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3172)
  * [CVE-2022-39278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39278)
  * [CVE-2020-35527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-35527)
  * [CVE-2021-20223](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20223)
  * [CVE-2020-35525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-35525)
  * [CVE-2022-40617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40617)
  * [CVE-2022-2526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2526)



1.11

Issue

**Known issues:** For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues) in the Troubleshooting section.

## October 05, 2022

1.12

Feature

### Release 1.12.3

Anthos clusters on bare metal 1.12.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.3 runs on Kubernetes 1.23.

1.12

Fixed

**Fixes:**

  * Updated the container image to resolve a YAML text/template vulnerability.

  * The following container image security vulnerabilities have been fixed:

    * [CVE-2022-34903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-34903)
    * [CVE-2022-1798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1798)
    * [CVE-2019-8457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-8457)
    * [CVE-2021-45346](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45346)
    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)
    * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)
    * [CVE-2021-30560](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30560)
    * [CVE-2021-3750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3750)
    * [CVE-2022-1050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1050)
    * [CVE-2020-16156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-16156)
    * [CVE-2022-1587](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1587)
    * [CVE-2021-33560](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33560)
    * [CVE-2022-35414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-35414)
    * [CVE-2022-1586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1586)



1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## September 29, 2022

1.13

Feature

### Release 1.13.0

Anthos clusters on bare metal 1.13.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.13.0 runs on Kubernetes 1.24.

1.13

Announcement

The [dockershim](https://kubernetes.io/blog/2022/05/03/dockershim-historical-context/) component in Kubernetes enables cluster nodes to use the Docker Engine container runtime. However, Kubernetes 1.24 removed the dockershim component. Since Anthos clusters on bare metal version 1.13 runs on Kubernetes 1.24, version 1.13 and higher clusters can no longer use Docker Engine as a container runtime. All clusters must use the default container runtime containerd.

1.13

Feature

**Improved cluster lifecycle functionalities:**

  * Upgraded from Kubernetes version 1.23 to 1.24:

    * Reverted some of the changes Kubernetes and the `kubeadm` tool made to certain labels and taints on control plane nodes. Changes were reverted so that older versions of Anthos clusters on bare metal remain supported. As a result, control plane nodes have the following labels and taints:

      * `node-role.kubernetes.io/master` label
      * `node-role.kubernetes.io/control-plane` label
      * `node-role.kubernetes.io/master:NoSchedule` taint
    * Upgraded from `kubeadm.k8s.io/v1beta2` to `kubeadm.k8s.io/v1beta3` since the former is deprecated.

    * Stopped automatic generation of Secret API objects containing service account tokens for every Service Account. For more information, see the `LegacyServiceAccountTokenNoAutoGeneration` section of the [upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#urgent-upgrade-notes).

  * **Breaking change:** Version 1.12 clusters that use Docker Engine can upgrade to 1.13 only if the new container runtime is specified as `containerd`. Blocked the creation of new 1.13 clusters that use Docker Engine as the container runtime.

  * **Preview:** Added feature so that upgrades of an admin/hybrid/standalone cluster can proceed without a bootstrap cluster. Management of Anthos clusters on bare metal is now fully conformant to the [Kubernetes Resource Model](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md).

  * Added support of Red Hat Enterprise Linux (RHEL) 8.6.

  * Removed an erroneous `CustomResourceDefinition` (`app.k8s.io.Application`) from inclusion in the cluster creation process.

  * Fixed vulnerability to YAML injection by switching to [safetext/yamltemplate](https://github.com/google/safetext).

  * **GA:** Added support for installing Anthos clusters on bare metal, using your own registry service, instead of `gcr.io`. For instructions and additional information, see [Use a registry mirror to create clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/registry-mirror).

  * Eliminated false error messaging when the `bmctl create cluster` is run. The message erroneously reported an `Invalid value` in the `spec.labels` field of NodePool specifications.

  * Added a webhook check to prevent worker node pools from being added to an Admin cluster inadvertently.

  * Added feature so that resetting a user cluster doesn't require the cluster configuration file.

  * Reduced `containerd` disk usage by having `containerd` store just the uncompressed layers of an image rather than both the compressed and uncompressed layers.

  * Upgraded `containerd` to version 1.6.6.




**Networking:**

  * **GA:** Enabled Dynamic Flat IP with Border Gateway Protocol (BGP) support. This feature lets you configure flat mode using BGP in clusters by leveraging Network Gateway Group and BGP. In this mode the Pod's IP address is visible and routable without masquerading across multiple subdomains. Currently supports advertising IPv4 and IPv6 routes over IPv4 sessions.

  * **GA:** Added BGP-based Load Balancer support for IPv6. Added ability to disable the Bundled Ingress feature. Customers should disable this feature if they are using full Anthos Service Mesh (ASM) instead. (Bundled Ingress is unnecessary when full ASM is installed).




**Observability:**

  * **Preview:** Added support of multi-line parsing for Go and Java logs.

  * **GA:** Added support for Google Cloud Managed Service for Prometheus (GMP) for application metrics.

  * Refined `kube-state-metrics` so that only core metrics are collected by default.




**Security:**

  * **GA:** Added Google Groups support for Connect Gateway.

  * Switched distroless base image for Node Problem Detector.

  * Changed `anet-operator/cilium-operator` to run as non-root container.

  * Secured communication between `metrics-server` and `api-server` using the Transport Layer Security (TLS) protocol.




**VM Runtime:**

  * Fixed a memory leak in `libvirt-go`, which caused unbounded memory growth and risked crashing long-running VMs.

  * Provided guaranteed compute support so that customers can get [Guaranteed Quality of Service (QoS)](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/#create-a-pod-that-gets-assigned-a-qos-class-of-guaranteed)for the VM when needed.

  * **Preview:** Enabled Anthos VM to be allocated dedicated host cores. Each VM virtual core can be pinned to a dedicated host core.

  * Separated GPU installation and deletion logic. If only the container GPU workload is needed, customers can enable the GPU without having to enable VM Runtime.

  * Added support for the T4 GPU card.

  * Enabled automatic use of the `VirtualMachineDisk` name as the disk serial number. This change makes it easier for customers to identify the disk in the VM.

  * Enabled KubeVM `cloud-init` API and startup script API.

  * Added new CLI command (`Virtctl`) for resetting Windows VM password.

  * Fixed the following container image security vulnerability: [CVE-2022-1798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1798)

  * Added feature that stops NVIDIA device plugins from crashing if a GPU card hasn't been allocated to a container.

  * Added support for automatic VM restarts after a configuration update. Previously, customers needed to stop the VM, apply the change, and then re-start the VM. To use the feature, set the `autoRestartOnConfigurationChange` flag to true in the `VirtualMachine` custom resource.

  * Improved the Kubernetes audit log of VM operations so that it contains detailed VM configuration and update information.

  * Fixed flooding of logs with cluster events that arise when a VM encounters disk I/O errors.

  * Added KubeVM roles. By binding with these roles, customers are granted permission to resources that manage VMs.




1.13

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## September 26, 2022

1.11

Feature

### Release 1.11.6

Anthos clusters on bare metal 1.11.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/upgrade). Anthos clusters on bare metal 1.11.6 runs on Kubernetes 1.22.

1.11

Fixed

**Fixes:**

  * Updated the container image to resolve a yaml text/template vulnerability.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2022-2526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2526)
    * [CVE-2022-1798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1798)



1.11

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues) in the Troubleshooting section.

## August 30, 2022

1.11

Feature

### Release 1.11.5

Anthos clusters on bare metal 1.11.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/upgrade). Anthos clusters on bare metal 1.11.5 runs on Kubernetes 1.22.

1.11

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues) in the Troubleshooting section.

1.11

Fixed

**Fixes:**

  * Increased the default storage size limit of `etcd` to 6 GiB.

  * The following container image security vulnerabilities have been fixed:

    * [CVE-2022-1664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1664)



## August 25, 2022

1.12

Feature

### Release 1.12.2

Anthos clusters on bare metal 1.12.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/upgrade). Anthos clusters on bare metal 1.12.2 runs on Kubernetes 1.23.

1.12

Fixed

**Fixes:**

  * Added caching for the Cloud Audit Logging feature status to avoid unnecessary checks and improve performance.
  * Increased the etcd default DB size to 6GiB by default to address `NO_SPACE_ALARM` in high-scale clusters.
  * Fixed a `libseccomp` package incompatibility issue. 
  * Fixed an issue with the machine-reset job getting stuck.
  * Fixed an issue that caused continuous, unneeded cluster reconciliation operations.
  * Fixed an issue that prevented the node problem detector from running after a cluster upgrade.



The following container image security vulnerabilities have been fixed: 

  * [CVE-2022-1664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1664)
  * [CVE-2022-2068](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2068)



1.12

Feature

**Features:**

  * Added `–use-disk` flag to `bmctl backup cluster` command to use the disk instead of the in-memory buffer to back up a cluster. Use this option when available RAM is limited on your admin workstation.
  * Added `--quiet` flag to `bmctl check cluster -- snapshot` command to suppress logging to the console during the snapshot creation.



1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues) in the Troubleshooting section.

## August 23, 2022

1.12

Feature

### Anthos VM Runtime

Anthos VM Runtime is Generally Available (GA). Some features and capabilities are available for [Preview](https://cloud.google.com/products#product-launch-stages) only, as indicated in the following descriptions:

  * Upgraded Kubevirt to version 0.49.
  * Upgraded Containerized Data Importer (CDI) to version 1.43.0. 
  * Added `bmctl` command to [enable or disable Anthos VM Runtime](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/enable-disable) on user clusters.
  * Added automatic upgrade of Anthos VM Runtime when upgrading Anthos clusters on bare metal.
  * **Preview:** Added ability to [configure an eviction policy](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/eviction-policy) that controls how VMs automatically migrate to other hosts during maintenance events.
  * **Preview:** Added non-disruptive upgrading of VM runtime during live migration (that is, when VMs are unobtrusively migrated from one node to another).



**VM APIs:**

  * Simplified [VM Compute API](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/compute-configurations).
  * Added ability to [create and manage disk resources for VMs that use Anthos VM Runtime](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/create-manage-disks).
  * Added ability to [schedule VMs](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/schedule-vms) using standard Kubernetes scheduling primitives.
  * **Preview:** Added ability to [use GPUs in VMs](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/use-gpu).
  * Added more access management capabilities to VM Guest Environment.
  * **Preview:** Added support for guest OS booting of UEFI. Previously, only BIOS was supported.



**Observability:**

  * Integrated VM telemetry and console logs into Google Cloud console. Telemetry information and log data are critical for monitoring the status of VMs and for troubleshooting problems with your cluster VMs.
  * Added VM CPU and memory metrics to [Cloud Monitoring](https://cloud.google.com/monitoring/docs). These metrics can be viewed in the [Anthos clusters VM status dashboard](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/vm-workloads#vm_telemetry).
  * Added ability to [view console logs for VMs that use Anthos VM Runtime](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/view-console-logs).
  * Added logs that audit VM pods.



**Guest OS support:**

Added support for the following guest OS versions running on a Virtual Machine:

  * Windows Server 2019
  * Windows Server 2016
  * Windows 10
  * Red Hat Enterprise Linux (RHEL) 8
  * RHEL 7
  * CentOS 8
  * CentOS 7
  * Ubuntu 20.04 
  * Ubuntu 18.04



**VM networking features:**

  * IPAMv4: Static IP Allocation for VM interfaces.
  * IP and MAC Stickiness for VM interfaces.
  * IPAMv4: DHCP for VM interfaces.
  * VLAN tagging support for VM Interfaces.
  * Multi-NIC for VM interfaces through native Dataplane V2 support (macvtap + Dataplane V2).
  * Static routes and DNS configurations at per-network basis.
  * NetworkPolicy enforcement at per-network basis.
  * Validating admission webhooks for Network and NetworkInterface object.
  * Network Mutation, allow the mutations of Gateway, DNS and the customized network routes in the network custom resource. The parent interface for the VM and the VLAN ID are not mutable. VMs that were already running before the network configuration change need to be restarted to pick up the change.
  * Added command to restart all VMs in a network.
  * Graceful IP release for VMs:

    * During VM migration, the IP isn't released.
    * IP addresses are released for VMs that are deleted or stopped.

For more information on networking, see [Create and use virtual networks for Anthos VM Runtime](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/vm-runtime/create-networks).




1.10 

Feature

### Release 1.10.8

Anthos clusters on bare metal 1.10.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/upgrade). Anthos clusters on bare metal 1.10.8 runs on Kubernetes 1.21.

1.12

Issue

VM Runtime issues:

  * When kubevirt is configured, customers should ensure that TOR switches have MAC learning enabled.

  * If you choose to manually run a DHCP `ipconfig /renew` command in a Windows VM, you should first perform a DHCP release, using the`ipconfig /release` command. In other words, the sequence for manually performing a DHCP renewal in a Windows environment is the following:
        
        ipconfig /release
        ipconfig /renew
        




1.10 

Fixed

**Fixes**

The following container image security vulnerability has been fixed: 

  * [CVE-2022-1664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1664)



1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/troubleshooting/known-issues) in the Troubleshooting section.

## August 04, 2022

1.11

Feature

### Release 1.11.4

Anthos clusters on bare metal 1.11.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/upgrade). Anthos clusters on bare metal 1.11.4 runs on Kubernetes 1.22.

1.11

Fixed

**Fixes:**

  * Fixed issue in which cluster restores failed when `/var/lib/etcd` is a mount point.
  * Fixed issue in which attempts to skip minor versions when upgrading weren't blocked. For details about the upgrade policy, see [Minor version upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#minor_version_upgrades).



The following container image security vulnerabilities have been fixed: 

  * [CVE-2020-26137](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26137)
  * [CVE-2022-1271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1271)
  * [CVE-2022-2068](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2068)
  * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)



1.11

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues) in the Troubleshooting section.

## August 03, 2022

1.12

Feature

### Release 1.12.1

Anthos clusters on bare metal 1.12.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.12.1 runs on Kubernetes 1.23.

1.12

Change

**Functionality changes:**

  * Increased default memory limits for `coredns`, `metallb-controller`, `metallb-speaker`, `metrics-server`, `anthos-cluster-operator`, and `cap-controller-manager`.

  * Modified the dashboards `Anthos cluster pod status` and `Anthos cluster node status`. Specifically, the following changes were made:

    * Replaced `cadvisor` resource metrics with summary API resource metrics.
    * Added `cpu`, `memory`, and `volume` utilization metrics.

If you have already installed these dashboards in a project, you need to download the JSON files `Anthos-cluster-pod-status.json` and `Anthos-cluster-node-status.json` from the Dashboards for Anthos GitHub repository. You then need to import these JSON files into Cloud Monitoring. For details, see [Install sample dashboards](https://cloud.google.com/monitoring/dashboards/dashboard-templates).




1.12

Issue

Known issues:

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

Release 1.12.1 ships with `containerd` version 1.5.13, which requires `libseccomp` version 2.5 or higher. If your system doesn't have `libseccomp` version 2.5 or higher installed, update it in advance of upgrading existing clusters to version 1.12.1. Otherwise, you may see errors in `cplb-update` Pods for load balancer nodes such as:
    
    
    runc did not terminate successfully: runc: symbol lookup error: runc:
    undefined symbol: seccomp_notify_respond
    

To install the latest version of `libseccomp` in Ubuntu, run the following command:
    
    
    sudo apt-get install  libseccomp-dev
    

To install the latest version of `libseccomp` in CentOS or RHEL, run the following command:
    
    
    sudo dnf -y install libseccomp-devel
    

1.12

Fixed

**Fixes:**

  * Fixed issue in which nodes drained or cordoned by `kubectl` were mistakenly marked as schedulable.
  * Fixed issue in which cluster controller and autoscaler conflicted with each other in the scaling of `istiod`, `coredns`, and `istio-ingress` Pods.
  * Fixed issue in which the wrong data type was used in health check log messages, resulting in panic messages.
  * Fixed issue in which cluster restores failed when `/var/lib/etcd` is a mount point.
  * Fixed issue in which attempts to skip minor versions when upgrading weren't blocked. For details about the upgrade policy, see [Minor version upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade#minor_version_upgrades).
  * Fixed issue in which an external VIP Service of type LoadBalancer would not respond when flat IP mode was enabled.



The following container image security vulnerabilities have been fixed: 

  * [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)
  * [CVE-2020-26137](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26137)
  * [CVE-2021-4160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4160)
  * [CVE-2021-33574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33574)
  * [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778)
  * [CVE-2022-1271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1271)
  * [CVE-2022-1292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1292)
  * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)
  * [CVE-2022-23218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23218)
  * [CVE-2022-23219](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23219)
  * [CVE-2022-29824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29824)
  * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)
  * [CVE-2022-32206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32206)
  * [CVE-2022-32208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32208)



## August 01, 2022

1.10 

Feature

### Release 1.10.7

Anthos clusters on bare metal 1.10.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/upgrade). Anthos clusters on bare metal 1.10.7 runs on Kubernetes 1.21.

1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/troubleshooting/known-issues) in the Troubleshooting section.

1.10 

Fixed

  * Fixed a `CrashLoopBackOff` error generated by `gke-metrics-agent` when application metrics are enabled (that is, when `enableStackdriverForApplications=true`).

  * The following container image security vulnerabilities have been fixed:

    * [CVE-2022-2068](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2068)

    * [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)

    * [CVE-2022-1292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1292)

    * [CVE-2022-1271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1271)

    * [CVE-2022-32208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32208)

    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)

    * [CVE-2022-32206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32206)

    * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)




## July 07, 2022

1.10 

Feature

### Release 1.10.6

Anthos clusters on bare metal 1.10.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/upgrade). Anthos clusters on bare metal 1.10.6 runs on Kubernetes 1.21.

1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/troubleshooting/known-issues) in the Troubleshooting section.

1.10 

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed:

  * [CVE-2022-1292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1292)

  * [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)

  * [CVE-2021-43618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43618)

  * [CVE-2021-4160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4160)

  * [CVE-2022-29824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29824)

  * [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778)

  * [CVE-2021-33574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33574)

  * [CVE-2022-23219](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23219)

  * [CVE-2022-23218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23218)

  * [CVE-2022-27782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27782)

  * [CVE-2022-29155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29155)




## June 29, 2022

1.12

Feature

### Release 1.12.0

Anthos clusters on bare metal 1.12.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.12.0 runs on Kubernetes 1.23.

1.12

Announcement

The [dockershim](https://kubernetes.io/blog/2022/05/03/dockershim-historical-context/) component in Kubernetes enables cluster nodes to use the Docker Engine container runtime. However, Kubernetes 1.24 removed the dockershim component. Starting from Anthos clusters on bare metal 1.12.0, you will not be able to create new clusters that use the Docker Engine container runtime. All new clusters should use the default container runtime `containerd`.

1.12

Feature

**Improved cluster lifecycle functionalities:**

  * Upgraded Anthos clusters on bare metal to use Kubernetes version 1.23. 

  * Upgraded container runtime to `containerd` 1.5.

  * Updated preflight check to forward default SSH key if no key is provided.

  * Added support for new `GCPAccounts` field in the cluster configuration file. This field enables the assignment of a `cluster-admin` role to end-users.

  * Added labels to control plane, control plane load balancer, and load balancer node pools, so that these different node pools can be distinguished from each other.

  * Added nodepool reference label to nodes so that worker nodes can be listed in the UI.




**Observability:**

  * **GA:** Added Summary API metrics. These metrics are scraped from the Kubernetes [Summary API](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-metrics-pipeline/#summary-api-source) and provide CPU, memory, and storage metrics for Pods, containers, and Nodes.

  * Added separate flags to enable logging and monitoring for user applications separately: `EnableCloudLoggingForApplications` and `EnableGMPForApplications`. The legacy flag `EnableStackdriverForApplications` will be deprecated and removed in future releases.

  * **Preview:** Added [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus) to collect application metrics and monitor cluster health.

  * Upgraded GKE Metrics Agent (gke-metrics-agent) from version 1.1.0 to 1.8.3. This tool scrapes metrics from each cluster node and publishes them in [Cloud Monitoring](https://cloud.google.com/monitoring/docs).

  * Added the following resource utilization metrics. For more information about these and other metrics, see [View Anthos clusters on bare metal metrics](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/metrics-anthos):

    * `container/cpu/request_utilization`
    * `container/cpu/limit_utilization`
    * `container/memory/request_utilization`
    * `container/memory/limit_utilization`
    * `node/cpu/allocatable_utilization`
    * `node/memory/allocatable_utilization`
    * `pod/volume/utilization`
  * Added sample dashboards for monitoring cluster health to [Cloud Monitoring sample dashboards](https://cloud.google.com/monitoring/dashboards/dashboard-templates). Customers can install these dashboards with one click. 

  * Scoped down the RBAC permissions of `stackdriver-operator`, a component that performs logging and monitoring.




**Security:**

  * AIS CA deprecation. AIS certs are now signed by cluster CA.

  * Changed `ca-rotation` container image so that it uses a distroless rather than a Debian-based image.

  * RBAC permissions of the `cluster-operator` component have been eliminated or reduced to address elevated permissions.

  * **GA:** Anthos Identity Service [LDAP authentication support](https://cloud.google.com/anthos/identity#ldap).




**Networking:**

  * **Preview:** Enabled creation of IPv6 and Dual Stack LoadBalancer services. Border Gateway Protocol (BGP) is used for Dualstack clusters. Advertising IPv4 and IPv6 routes over IPv4 sessions is supported.

  * **Preview:** Added [Network Connectivity Gateway](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/network-connectivity-gateway) feature support to provide HA VPN between Google Cloud and an on-premises Anthos cluster.




1.12

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## June 23, 2022

1.11

Feature

### Release 1.11.3

Anthos clusters on bare metal 1.11.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/upgrade). Anthos clusters on bare metal 1.11.3 runs on Kubernetes 1.22.

1.11

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed:

  * [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)

  * [CVE-2021-27782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27782)

  * [CVE-2021-4160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4160)

  * [CVE-2021-43618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43618)

  * [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778)

  * [CVE-2022-1292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1292)

  * [CVE-2022-29155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29155)

  * [CVE-2022-29824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29824)




1.11

Issue

Known issues:

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues) in the Troubleshooting section.

## June 09, 2022

1.9

Feature

### Release 1.9.8

Anthos clusters on bare metal 1.9.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade). Anthos clusters on bare metal 1.9.8 runs on Kubernetes 1.21.

1.9

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2022-1271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1271)

    * [CVE-2022-22576](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22576)

    * [CVE-2022-24769](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24769)

    * [CVE-2022-27774](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27774)




1.9

Issue

Known issues:

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/troubleshooting/known-issues) in the Troubleshooting section.

## June 02, 2022

1.10 

Feature

### Release 1.10.5

Anthos clusters on bare metal 1.10.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/upgrade). Anthos clusters on bare metal 1.10.5 runs on Kubernetes 1.21.

1.10 

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2022-1271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1271)
  * [CVE-2022-22576](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22576)
  * [CVE-2022-27774](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27774)
  * [CVE-2022-24769](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24769)



1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/troubleshooting/known-issues) in the Troubleshooting section.

## May 26, 2022

1.11

Feature

### Release 1.11.2

Anthos clusters on bare metal 1.11.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.11.2 runs on Kubernetes 1.22.

1.11

Announcement

If you have Anthos VM Runtime enabled for your Anthos clusters on bare metal, you must disable it before upgrading clusters to version 1.11.2 or higher. If this step is not completed, your cluster upgrade will fail. You can [re-enable](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/vm-workloads#enable_anthos_vm_runtime) Anthos VM Runtime after the upgrade is complete.

1.11

Announcement

Starting with Anthos clusters on bare metal release 1.11.2, you can enable or disable Anthos VM Runtime by updating the `VMRuntime` custom resource only. The legacy `spec.kubevirt` settings in the cluster configuration are no longer supported. The `VMRuntime` custom resource is installed by default on version 1.10 and later hybrid, standalone, and user clusters. The `VMRuntime` custom resource can't be applied to admin clusters.

1.11

Fixed

**Fixes:**

  * Fixed cluster custom resource status reporting for pending reconciliations.

  * Fixed a `bmctl check cluster` command issue that caused the user cluster kubeconfig Secret to be overwritten.

  * Fixed an issue with manifest installation when `last-applied-config` is broken that caused upgrades to fail.

  * Fixed an issue to ensure that the 20-minute timeout for node draining is enforced during cluster upgrades. This timeout provides ample time for nodes to drain, but ensures that upgrades can always proceed.




1.11

Announcement

Starting with Anthos clusters on bare metal release 1.11.2, the Anthos VM Runtime API version has changed from `v1alpha1` to `v1`. This version change doesn't affect the `VMRuntime` custom resource, but most other resources are affected.

1.11

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

1.11

Change

**Functionality changes:**

  * The `containerd` runtime has been upgraded to 1.5.11-gke.0 to address [CVE-2022-24769](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24769)

  * Added a preflight check that disallows Ubuntu 18.04 distributions with 4.15.x Linux kernels.




## May 04, 2022

1.10 

Feature

### Release 1.10.4

Anthos clusters on bare metal 1.10.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/downloads). To upgrade, see [Upgrade Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/upgrade). Anthos clusters on bare metal 1.10.4 runs on Kubernetes 1.21.

1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/troubleshooting/known-issues) in the Troubleshooting section.

1.10 

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed:

    * [CVE-2021-3999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3999)
    * [CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)
    * [CVE-2021-45960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45960)
    * [CVE-2021-46143](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46143)
    * [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055)
    * [CVE-2022-22822](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22822)
    * [CVE-2022-22824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22824)
    * [CVE-2022-22825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22825)
    * [CVE-2022-22826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22826)
    * [CVE-2022-22827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22827)
    * [CVE-2022-23852](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23852)
    * [CVE-2022-25236](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-25236)
    * [CVE-2022-25315](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-25315)
    * [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666)
  * Role-based access control (RBAC) fixes:

    * Set `AutomountServiceAccountToken` field for Node Problem Detector jobs and `etcd-defrag` Daemonsets to false.

    * Set `capi-kubeadm-bootstrap-controller-manager` to use a dedicated service account.

    * Scoped down `configmap/(get, list, watch)` permissions to `metallb-config` resource name.

    * Scoped down `configmap/get` permission to `core-dns-autoscaler` resource name.

    * Removed `services.update` permission for the MetalLB `kube-system:controller` role.

    * anetd

      * Removed Cilium service account and replaced it with the account used by `kubelet`.

      * Removed pod and node access from Cilium cluster role.

      * Added Cilium cluster role to the `kubelet` service account.

      * Removed `pods/(delete)` role from `cilium-operator` cluster role.

      * Scoped down leases permissions in `cilium-operator` cluster role to `cilium-operator-resource-lock` resource name and `kube-controller-manager` resource name.




## May 02, 2022

1.11

Feature

### Release 1.11.1

Anthos clusters on bare metal 1.11.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.11.1 runs on Kubernetes 1.22.

1.11

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

1.11

Fixed

**Fixes:**

  * Resolved cluster installation issue in which cluster status is prematurely declared ready, resulting in a "Failed to wait for applied resources" error.

  * Added validation that a cluster's `kubeconfig` secret data is correct.

  * Added feature so that `bmctl` outputs line numbers of relevant yaml when a parsing error occurs.

  * Removed the misleading log "Waiting for pod to finish" on pods such as `anetd` that aren't meant to finish.

  * Added automatic inclusion of a control plane's virtual IP address to the cluster `NO_PROXY` list.

  * Role-based access control fixes:

    * Set `AutomountServiceAccountToken` field for Node Problem Detector jobs to false.

    * Set `capi-kubeadm-bootstrap-controller-manager` to use a dedicated service account.

    * Scoped down `deployment/(update,patch)` permissions to the `metrics-server` resource name.

    * Scoped down `configmap/(get, list, watch)` permissions to `metallb-config` resource name.

    * anetd:

    * Removed Cilium service account and replaced it with the account used by `kubelet`.

    * Removed pod and node access from Cilium cluster role.

    * Added Cilium cluster role to the `kubelet` service account.

    * Removed `pods/(delete)` role from `cilium-operator` cluster role.

    * Scoped down leases permissions in `cilium-operator` cluster role to `cilium-operator-resource-lock` resource name and `kube-controller-manager` resource name.

  * The following container image security vulnerabilities have been fixed:

    * [CVE-2021-3999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3999)



## April 27, 2022

1.9

Feature

### Release 1.9.7

Anthos clusters on bare metal 1.9.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade). Anthos clusters on bare metal 1.9.7 runs on Kubernetes 1.21.

1.9

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/troubleshooting/known-issues) in the Troubleshooting section.

1.9

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-3999](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3999)
    * [CVE-2022-24407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407)



## April 26, 2022

1.9

Security

### Security bulletin (all minor versions)

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect Linux operating systems supported by Anthos clusters on bare metal. For instructions and more details, see the [GCP-2022-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-014) security bulletin.

1.8

Security

### Security bulletin (all minor versions)

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect Linux operating systems supported by Anthos clusters on bare metal. For instructions and more details, see the [GCP-2022-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-014) security bulletin.

1.7

Security

### Security bulletin (all minor versions)

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect Linux operating systems supported by Anthos clusters on bare metal. For instructions and more details, see the [GCP-2022-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-014) security bulletin.

1.6

Security

### Security bulletin (all minor versions)

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect Linux operating systems supported by Anthos clusters on bare metal. For instructions and more details, see the [GCP-2022-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-014) security bulletin.

1.11

Security

### Security bulletin (all minor versions)

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect Linux operating systems supported by Anthos clusters on bare metal. For instructions and more details, see the [GCP-2022-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-014) security bulletin.

1.10 

Security

### Security bulletin (all minor versions)

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect Linux operating systems supported by Anthos clusters on bare metal. For instructions and more details, see the [GCP-2022-014](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-014) security bulletin.

## April 12, 2022

1.9

Security

### Security bulletin (1.8, 1.9, and 1.10)

A security vulnerability, [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648), has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host.

For more information, see the [GCP-2022-013](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-013) security bulletin.

1.8

Security

### Security bulletin (1.8, 1.9, and 1.10)

A security vulnerability, [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648), has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host.

For more information, see the [GCP-2022-013](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-013) security bulletin.

1.10 

Security

### Security bulletin (1.8, 1.9, and 1.10)

A security vulnerability, [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648), has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host.

For more information, see the [GCP-2022-013](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-013) security bulletin.

## March 31, 2022

1.11

Feature

### Release 1.11.0

Anthos clusters on bare metal 1.11.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/downloads). To upgrade, see [Upgrade Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/upgrade). Anthos clusters on bare metal 1.11.0 runs on Kubernetes 1.22.

1.10 

Feature

### Release 1.10.3

Anthos clusters on bare metal 1.10.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/downloads). To upgrade, see [Upgrade Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/upgrade). Anthos clusters on bare metal 1.10.3 runs on Kubernetes 1.21.

1.11

Announcement

Kubernetes 1.22 has deprecated certain APIs, and a list of these deprecated APIs can be found in [Kubernetes 1.22 deprecated APIs](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/reference/deprecated-apis-kubernetes-1_22). In their manifests and API clients, customers need to replace references to the deprecated APIs with references to the newer API calls. For more information, see [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#migrate-to-non-deprecated-apis).

1.11

Announcement

The structure of the Anthos clusters on bare metal documentation is substantially different from previous versions. For details, see [New documentation structure](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/concepts/about-bare-metal#toc-update).

1.11

Announcement

On January 31, 2022, CentOS 8 reached its end of life (EOL). As a result of the EOL, yum repositories stopped working for CentOS, which causes cluster creation and cluster upgrade operations to fail. For a workaround and more information, see [Cluster creation or upgrades fail on CentOS](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues#centos-eol).

1.11

Announcement

Containerd is the default runtime in Anthos clusters on bare metal. Support for Docker as a container runtime on Kubernetes nodes will be removed from Anthos clusters on bare metal starting with version 1.13.0. If you use a node image based on Docker container runtime, please migrate your workloads to a Containerd node image as soon as possible. For more details, see [Containerd node images](https://cloud.google.com/kubernetes-engine/docs/concepts/using-containerd#migrating).

1.11

Feature

**Improved cluster lifecycle functionalities:**

  * Upgraded Anthos clusters on bare metal to use Kubernetes version 1.22.

  * Updated `cert-manager` to version 1.5.4.

  * Added error messaging in the `bmctl` command line interface to better surface cluster installation or upgrade failure.

  * Incorporated audit logs into `bmctl` snapshots.

  * Added ability for registry mirror users to customize `containerd` configuration and have it automatically mirror public registry hosts other than `gcr.io`.

  * Changed `bmctl update` command so that it extracts manifests before updating a cluster.

  * Added feature so that a cluster `kubeconfig` file automatically renews when the cluster is upgraded and the kubeconfig `Secret` is renewed whenever cluster reconciliation takes place.

  * Added support for Red Hat Enterprise Linux (RHEL) and CentOS 8.5.

  * Added warning to `bmctl` command that `docker containerRuntime` will not be supported in version 1.13 of Anthos cluster on bare metal.

  * Added support for specifying CIDR blocks in the `NoProxy` section of the cluster's configuration file.

  * Added Service CIDR to `NoProxy` section of a cluster configuration file by default in order to fix a multinic in proxy environment issue.

  * Fixed a multi-NIC in proxy environment issue. Whenever the `NO_PROXY` environment variable is set, it includes the Service CIDR from the cluster specification.




**Networking:**

  * **GA:** Added egress Network Address Translation (NAT) gateway capability to provide persistent, deterministic routing for egress traffic from clusters. For more information, see [Configure an egress NAT gateway for external communication](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/egress-nat).

  * **GA:** Added option for [BGP bundled load balancer](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/how-to/lb-bundled-bgp) which advertises Load Balancer (LB) Virtual IP addresses (VIPs) to the network using the Border Gateway Protocol (BGP). This feature supports topologies across multiple subnets and can provide greater load-balancing bandwidth than bundled Layer 2 mode.

  * **GA:** Enabled SR-IOV. This feature allows you to configure Virtual Functions (VFs) on the supported devices on the nodes of their cluster. It also allows you to define the kernel module you want to bind to the VF.

  * **GA:** Enabled IPv4/IPv6 dual-stack support. Clusters can be deployed in a dual-stack network in which IPv4 and IPv6 addresses are assigned to both nodes and pods. By default, IPv4 is in island mode and IPv6 is in flat mode (a simplified network topology).

  * **GA:** Enabled static flat network (without BGP). This feature lets you configure a flat mode network for IPv4 addresses. A pod's IPv4 address is visible and routable within the same Layer 2 domain, without having to masquerade as the node's IP address.

  * **Preview:** Enabled Dynamic Flat IP with Border Gateway Protocol (BGP) support. This feature lets you configure flat mode using BGP in clusters with the help of Anthos Network Gateway and BGP. In this mode, the pod's IP address is visible and routable without masquerading across multiple subdomains. Currently supports advertising IPv4 and IPv6 routes over IPv4 sessions.

  * Fixed issue in which new MAC addresses of re-imaged nodes weren't updated.




**Observability:**

  * **GA:** Enabled collection of multiple network interfaces (multinic) logs from clusters. Logs are collected as system logs and are sent to Cloud Logging without charge to the customer.

  * **Preview:** Added [Summary API](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-metrics-pipeline/#summary-api-source) metrics. These metrics provide CPU, memory, and storage statistics about pods, containers, and nodes.

  * Updated fluent-bit (`stackdriver-log-forwarder`) cri parser to avoid matching time fields multiple times.

  * Upgraded `kube-state-metrics` from version 1.9 to 2.4. This service generates metrics about Kubernetes API objects such as deployments, nodes, and pods.

  * Upgraded [Metric Server](https://github.com/kubernetes-sigs/metrics-server) from version 0.3.6 to 0.4.5. Metrics Server retrieves metrics from kubelets and exposes them through the Kubernetes Metrics API.




**Security:**

  * **Preview:** Added secure computing mode (`seccomp`) support. Running containers with a `seccomp` profile improves the security of a cluster because it restricts the system calls that containers are allowed to make to the kernel.

  * Added ability to disable rootless mode for system containers. Since version 1.10.0, Kubernetes control planes and Anthos clusters on bare metal system containers run as non-root containers by default.

  * Fixed CA rotation issues by increasing the `ca-rotation` timeout for admin clusters. While verifying that a static pod has been restarted after manifest update, the current hash is retrieved before the manifest changes are applied.




1.10 

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2022-24407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407)
    * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)



1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.10/troubleshooting/known-issues) in the Troubleshooting section.

1.11

Issue

**Known issues:**

  * Deprecated metrics 

Several Anthos metrics have been deprecated and, starting with this release, data is no longer collected for these deprecated metrics. If you use these metrics in any of your alerting policies, there won't be any data to trigger the alerting condition. For more information, including instructions to migrate to updated replacement metrics, see [Deprecated metrics affects Cloud Monitoring dashboard](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues#metr-depr) in Known Issues.




For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.11/troubleshooting/known-issues) in the Troubleshooting section.

## March 23, 2022

1.9

Feature

### Release 1.9.6

Anthos clusters on bare metal 1.9.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade). Anthos clusters on bare metal 1.9.6 runs on Kubernetes 1.21.

1.9

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend that you upgrade to the highest patch version to ensure that you have the latest security fixes. Always review the release notes before upgrading so that you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/troubleshooting/known-issues) in the Troubleshooting section.

1.9

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-43824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43824)
    * [CVE-2021-43825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43825)
    * [CVE-2021-43826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43826)
    * [CVE-2021-21654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21654)
    * [CVE-2021-21655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21655)
    * [CVE-2021-23606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23606)
    * [CVE-2021-21657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21657)
    * [CVE-2021-21656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21656)
    * [CVE-2021-23635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23635)
    * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)
    * [CVE-2021-45960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45960)
    * [CVE-2021-3996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3996)
    * [CVE-2021-3995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3995)
    * [CVE-2021-45960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45960)
    * [CVE-2022-22823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22823)
    * [CVE-2022-22824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22824)
    * [CVE-2022-22822](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22822)
    * [CVE-2022-23852](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23852)
    * [CVE-2022-23990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23990)
    * [CVE-2021-43618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43618)
    * [CVE-2022-22825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22825)
    * [CVE-2022-22827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22827)
    * [CVE-2021-46143](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46143)
    * [CVE-2022-22826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22826)



## March 14, 2022

1.8

Feature

### Release 1.8.9

Anthos clusters on bare metal 1.8.9 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.9 runs on Kubernetes 1.20.

1.8

Issue

**Known issues:**

When upgrading Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend that you upgrade to the highest patch version to ensure that you have the latest security fixes. Always review the release notes before upgrading so that you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

1.8

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-43824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43824)
    * [CVE-2021-43825](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43825)
    * [CVE-2021-43826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43826)
    * [CVE-2021-21654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21654)
    * [CVE-2021-21655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21655)
    * [CVE-2021-23606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23606)
    * [CVE-2021-21657](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21657)
    * [CVE-2021-21656](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21656)
    * [CVE-2021-23635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23635)



## February 28, 2022

1.9

Feature

### Release 1.9.5

Anthos clusters on bare metal 1.9.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade). Anthos clusters on bare metal 1.9.5 runs on Kubernetes 1.21.

1.9

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend that you upgrade to the highest patch version to ensure that you have the latest security fixes. Always review the release notes before upgrading so that you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/troubleshooting/known-issues) in the Troubleshooting section.

1.9

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-3997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3997)
    * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)
    * [CVE-2021-45079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45079)



## February 25, 2022

1.9

Security

### Security bulletin (1.8, 1.9, and 1.10)

Envoy recently released multiple security vulnerability fixes. The vulnerabilities affect Anthos clusters on bare metal, because Envoy is used for [Metrics Server](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#metrics_server).

For instructions and more details, see the [GCP-2022-008](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-008) security bulletin.

1.8

Security

### Security bulletin (1.8, 1.9, and 1.10)

Envoy recently released multiple security vulnerability fixes. The vulnerabilities affect Anthos clusters on bare metal, because Envoy is used for [Metrics Server](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#metrics_server).

For instructions and more details, see the [GCP-2022-008](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-008) security bulletin.

1.10 

Security

### Security bulletin (1.8, 1.9, and 1.10)

Envoy recently released multiple security vulnerability fixes. The vulnerabilities affect Anthos clusters on bare metal, because Envoy is used for [Metrics Server](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#metrics_server).

For instructions and more details, see the [GCP-2022-008](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-008) security bulletin.

1.10 

Feature

### Release 1.10.2

Anthos clusters on bare metal 1.10.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.10.2 runs on Kubernetes 1.21.

1.10 

Change

**Functionality changes:**

  * A preflight check now verifies whether your node machine has [enough disk space](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/install-prereq#node_machine_prerequisites) before starting an install.

  * Updated the `bmctl check cluster --snapshot` command so that snapshots now capture information about pods in cluster namespaces.

  * Updated the `bmctl check cluster --snapshot` command so that snapshots now capture information about cluster API machines and `kubeadmin` Secrets.




1.10 

Fixed

**Fixes:**

  * Fixed issue in which the edge profile's request to reserve resources is lost during the upgrade process.

  * Fixed `bmctl upgrade` command so that the log file `upgrade-cluster.log` is generated in the `bmctl-workspace/cluster/logs` directory.

  * Fixed issue in which the non-root login didn't have the proper permissions to perform `bmctl backup` or `bmctl restore`.

  * Fixed a Node Problem Detector service that sometimes failed to run on nodes after a cluster installation or upgrade.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)
    * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)
    * [CVE-2021-3997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3997)



1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## February 04, 2022

1.9

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2021-4034](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034), has been discovered in `pkexec`, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions, such as rebooting the system, installing packages, restarting services, as governed by a policy.

For instructions and more details, see the [GCP-2022-004 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-004).

1.8

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2021-4034](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034), has been discovered in `pkexec`, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions, such as rebooting the system, installing packages, restarting services, as governed by a policy.

For instructions and more details, see the [GCP-2022-004 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-004).

1.7

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2021-4034](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034), has been discovered in `pkexec`, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions, such as rebooting the system, installing packages, restarting services, as governed by a policy.

For instructions and more details, see the [GCP-2022-004 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-004).

1.6

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2021-4034](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034), has been discovered in `pkexec`, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions, such as rebooting the system, installing packages, restarting services, as governed by a policy.

For instructions and more details, see the [GCP-2022-004 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-004).

1.10 

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2021-4034](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034), has been discovered in `pkexec`, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions, such as rebooting the system, installing packages, restarting services, as governed by a policy.

For instructions and more details, see the [GCP-2022-004 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-004).

## February 01, 2022

1.8

Feature

### Release 1.8.8

Anthos clusters on bare metal 1.8.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.8 runs on Kubernetes 1.20.

1.8

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

1.8

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-3733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3733)
    * [CVE-2021-3737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3737)
    * [CVE-2021-3997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3997)



## January 27, 2022

1.9

Feature

### Release 1.9.4

Anthos clusters on bare metal 1.9.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/downloads). To upgrade, see [Upgrade Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade). Anthos clusters on bare metal 1.9.4 runs on Kubernetes 1.21.

1.10 

Feature

### Release 1.10.1

Anthos clusters on bare metal 1.10.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.10.1 runs on Kubernetes 1.21.

1.9

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/troubleshooting/known-issues) in the Troubleshooting section.

1.9

Fixed

**Fixes:**

  * The following container image security vulnerabilities have been fixed: 
    * [CVE-2021-3733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3733)
    * [CVE-2021-3737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3737)
    * [CVE-2021-3997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3997)



1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

1.10 

Fixed

**Fixes:**

  * Fixed PreflightCheck to allow the `preflightCheck.Spec.ConfigYAML` field to be empty.

  * Fixed PreflightCheck to allow an existing GKE Hub membership, if the cluster already exists. 

  * Fixed issue that blocked access to external Virtual IP addresses of Services, such as a Load Balancer, when Flat IPv4 is enabled.

  * Fixed issue in which the use of `–nodes/` and `–node-ssh-key` flags when taking an admin-less snapshot of a cluster resulted in an empty snapshot.

  * Fixed issue that caused installation of version 1.10.0 clusters to fail when the `umask` setting for the `root` user on the target machine wasn't `0022`. For more information, see [Failure on systems with restrictive umask setting](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues#failure_on_systems_with_restrictive_umask_setting).

  * Fixed issue in which BGP load balancer preflight checks failed if the Kubernetes interface had a period ('.') in the name. (For example, VLAN interfaces often have names such as `eth0.1`).

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2021-3733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3733)
    * [CVE-2021-3737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3737)
    * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)
    * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)



## December 22, 2021

1.9

Fixed

**Fixes:**

  * Fixed an issue in which cluster creation fails if a cluster has more than one control plane node, and the `HTTPS_PROXY` environment variable has been defined on one or more of the control plane nodes.

  * Upgraded Kubernetes version from 1.21.4 to 1.21.5 to address an error in which pods become stuck in the `ContainerCreating` state because `libcontainer` mistakenly throws a "unit already exists" error.

  * The following container image security vulnerability has been fixed: 

    * [CVE-2020-21913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-21913)



1.9

Feature

### Release 1.9.3

Anthos clusters on bare metal 1.9.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade). Anthos clusters on bare metal 1.9.3 runs on Kubernetes 1.21.

1.9

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.9/troubleshooting/known-issues) in the Troubleshooting section.

## December 14, 2021

1.8

Feature

### Release 1.8.7

Anthos clusters on bare metal 1.8.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.7 runs on Kubernetes 1.20.

1.8

Fixed

**Fixes:**

The following container image security vulnerability has been fixed: 

  * [CVE-2020-21913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-21913)



1.8

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

## December 10, 2021

1.10 

Feature

### Release 1.10.0

Anthos clusters on bare metal 1.10.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.10.0 runs on Kubernetes 1.21.

1.10 

Breaking

**Breaking changes:**

The gateway capability used by the egress NAT gateway and Bundled load balancing with BGP [Preview](https://cloud.google.com/products#product-launch-stages) features have changed in this release. The `NetworkGatewayGroup` custom resource replaces `AnthosNetworkGateway` and the capability is enabled with a new `advancedNetworking` field in the cluster configuration file, instead of an annotation. These changes affect the ability to upgrade clusters that use earlier versions of the features. 

Anthos clusters on bare metal blocks cluster upgrades from version 1.9 to version 1.10 for clusters that use either of these two advanced networking features. You can upgrade a version 1.9 admin cluster that is managing 1.9 user clusters that use these features to version 1.10, but object reconciliation breaks for the `AnthosNetworkGateway` custom resource. Object reconciliation is the mechanism whereby admin clusters automatically copy/restore objects on managed user clusters when the objects have been defined alongside the cluster configuration. Any `AnthosNetworkGateway` custom resources are still functional and can be modified with `kubectl`.

To bring a version 1.9 cluster that uses either advanced networking Preview feature up to version 1.10, [reset or delete the cluster](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/reset-clusters) and create a new 1.10 cluster. 

Preview features and products are subject to change and are provided for testing and evaluation purposes only. Do not use Preview features on your production clusters.

1.10 

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

1.10 

Feature

**Improved cluster lifecycle functionalities:**

  * **GA:** Enabled Node Problem Detector to run by default on all nodes. You can check if a problem was detected on a node by running the `kubectl describe` command for the node. Then look for `NodeConditions` or `Events` reported by Node Problem Detector.

  * **GA:** Added `bmctl backup cluster` and `bmctl restore cluster` commands to facilitate disaster recovery for clusters.

  * **Preview:** Added the ability to reset individual nodes using the SSH key.

  * Updated the `bmctl check cluster` command so that the snapshot of a cluster includes the cluster's YAML file and logs that are in the `bmctl-workspace` directory.

  * Added a new status field `cluster.gkeHubRegistrationStatus`. The command `kubectl get cluster` now shows information about the cluster's membership to GKE Hub.




**Networking:**

  * **Preview:** Enabled Anthos multi-cluster connectivity to provide Anthos clusters a way to connect to another Anthos cluster in the same data center (intra-site, cluster-to-cluster). Pods in connected clusters can reach each other over pod IP addresses without using native address translation (NAT) in between.

  * **Preview:** Enabled IPv4/IPv6 dual stack support. Customers can deploy clusters in a dual-stack network, where IPv4 and IPv6 addresses can be assigned to both nodes and pods.

  * **Preview:** Enabled "flat mode" (a simplified network topology) for IPv4 , where the pod's IPv4 address is visible and routable without masquerading as node IP within the same Layer 2 domain.

  * **Preview:** Enabled SR-IOV. This feature lets you configure Virtual Functions (VFs) on the supported devices on the nodes of their cluster. This feature also lets you define the kernel module you want to bind to the VF.




**Observability:**

  * **GA:** Added ability to show severity level of an issue in Cloud Logging. Severity level is extracted from `containerd` and `kubelet` node logs.

  * **GA:** Changed collection of application metrics to use a more scalable monitoring pipeline based on OpenTelemetry. This change significantly reduces the amount of resources required to collect metrics.




**Security:**

  * **GA:** Enhanced the capability to rotate cluster certificate authorities (CAs). Updates include support for all cluster types, rotation of front-proxy and `etcd` CAs, and changes to the `bmctl` command syntax.

  * **Preview:** Enabled installation of Anthos clusters on bare metal using a short-lived Google Service Account token instead of using Google Service Account keys.

  * Enabled Kubernetes control plane and most Anthos system containers to run as non-root users. For details, see [Don't run containers as root user](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/hardening-your-cluster#dont_run_containers_as_root_user).




**VM Runtime:**

  * **Preview:** Supported enabling or disabling Anthos VM Runtime on user clusters.

  * **Preview:** Enabled Anthos VM Runtime to support QEMU Copy On Write (QCOW2) format, which is a storage format for virtual disks on virtual machines. Some benefits of virtual disk capabilities are independent thin provisioning, better compression, and encryption at rest. 

  * **Preview:** Enabled `VMRuntime` custom resource and the `Network` custom resource, which let you create VMs on either the node network with a static IP address or the default pod network.

  * **Preview:** Enabled VM pods audit logs for VM runtime resources.

  * **Preview:** Expanded guest OS versions that can run on the virtual machine. We support Windows Server 2019, 2016, Windows 10, Red Hat Enterprise Linux (RHEL) 8, Centos 8, and Ubuntu 20.04 as guest OS.

  * **Preview:** Enabled virtual machine high availability to provide greater uptime for virtual machines instances (VMIs) by automatically detecting and recovering from a range of host machine failures.




1.10 

Fixed

**Fixed cluster lifecycle functionalities:**

  * Outputs from all `bmctl` commands except `bmctl version` are now written to log files.

  * Fixed strict mode for decoding the cluster YAML file. Extraneous information in the cluster YAML file now results in an error.

  * Fixed preflight check so that it no longer ignores the `no_proxy` setting.

  * Binaries in cluster provision no longer run from `/tmp`, which is often mounted with `noexec` options. This change fixes a preflight check "permission denied" error.

  * Switched the default server-side `containerRuntime` value from `docker` to `containerd`.




**Observability:**

  * Increased the priority of the `kube-state-metrics` service to keep it from being stuck in a pending state. This service generates metrics about Kubernetes API objects such as deployments, nodes, and pods.

  * Upgraded metrics-server to version 0.3.6 to fix a missing metrics issue that occurs when a duplicated pod name is present.




1.10 

Change

**Functionality changes:**

  * Enabled use of `ADMIN_KUBECONFIG` environment variable to reduce the number of `bmctl` command flags.

  * The cluster reconciliation process now checks for differences in the GKEHub membership before attempting to update it. If the GKEHub membership needs to be changed, the cluster is unregistered and then re-registered.

  * The `advancedNetworking` field in the cluster configuration file replaces the deprecated `baremetal.cluster.gke.io/enable-anthos-network-gateway` annotation for enabling advanced networking capabilities.

  * The `NetworkGatewayGroup` custom resource replaces the `AnthosNetworkGateway` custom resource.




## December 09, 2021

1.7

Feature

### Release 1.7.7

Anthos clusters on bare metal 1.7.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos clusters on bare metal 1.7.7 runs on Kubernetes 1.19.

1.7

Fixed

**Fixes:**

  * The 1.7.6 release has a [known issue](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues#upgrade-block) that blocks upgrades of 1.7.5 clusters. The 1.7.7 release allows you to upgrade from all earlier versions to get the latest security fixes.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)
    * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)
    * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)



1.7

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

## November 29, 2021

1.8

Feature

### Release 1.8.6

Anthos clusters on bare metal 1.8.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.6 runs on Kubernetes 1.20.

1.8

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)

  * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)

  * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)




1.8

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

## November 15, 2021

1.9

Feature

### Release 1.9.2

Anthos clusters on bare metal 1.9.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.9.2 runs on Kubernetes 1.21.

1.7

Feature

### Release 1.7.6

Anthos clusters on bare metal 1.7.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos clusters on bare metal 1.7.6 runs on Kubernetes 1.19.

1.9

Fixed

**Fixes:**

  * Updated preflight checks to use strict mode for decoding YAML to catch issues with indentation and misplaced fields in the cluster configuration file.

  * Fixed an issue that caused `containerRuntime` to default to `docker`, instead of `containerd` in certain uncommon situations.

  * Fixed an issue where `node_filesystem` metrics report incorrect size in Cloud Monitoring for mount-points other than root.

  * Fixed an issue that caused communication failures between Cloud Logging metadata agent and the Cloud Monitoring API when the root certificate authority (CA) on the host node isn't set up properly.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)
    * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)
    * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)
    * [CVE-2021-41990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41990)
    * [CVE-2021-41991](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41991)



1.9

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

1.7

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)

  * [CVE-2021-37750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37750)

  * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)




1.7

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

## October 29, 2021

1.9

Security

### Security bulletin (all minor versions)

The security community recently disclosed a new security vulnerability [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465) found in `runc` that has the potential to allow full access to a node filesystem.

For more information, see the [GCP-2021-011](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-011) security bulletin.

1.8

Security

### Security bulletin (all minor versions)

The security community recently disclosed a new security vulnerability [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465) found in `runc` that has the potential to allow full access to a node filesystem.

For more information, see the [GCP-2021-011](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-011) security bulletin.

1.7

Security

### Security bulletin (all minor versions)

The security community recently disclosed a new security vulnerability [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465) found in `runc` that has the potential to allow full access to a node filesystem.

For more information, see the [GCP-2021-011](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-011) security bulletin.

1.6

Security

### Security bulletin (all minor versions)

The security community recently disclosed a new security vulnerability [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465) found in `runc` that has the potential to allow full access to a node filesystem.

For more information, see the [GCP-2021-011](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-011) security bulletin.

## October 26, 2021

1.9

Feature

### Release 1.9.1

Anthos clusters on bare metal 1.9.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.9.1 runs on Kubernetes 1.21.

1.9

Fixed

**Fixes:**

  * Fixed `bmctl` to eliminate stack trace from error output.

  * The following container image security vulnerabilities have been fixed: 

    * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)
    * [CVE-2021-22946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22946)
    * [CVE-2021-22947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22947)
    * [CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)
    * [CVE-2021-40528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40528)



1.9

Change

**Functionality changes:**

  * Updated the `bmctl reset cluster` command to prevent you from resetting an admin cluster if the admin cluster is managing user clusters.
  * Updated the `bmctl create cluster` command to block you from enabling the Anthos VM Runtime for admin clusters.



1.9

Issue

**Known issues:**

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## October 21, 2021

1.9

Security

### Security bulletin (all minor versions)

A security issue was discovered in the Kubernetes ingress-nginx controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. For more information, see the [GCP-2021-024](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-024) security bulletin.

1.8

Security

### Security bulletin (all minor versions)

A security issue was discovered in the Kubernetes ingress-nginx controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. For more information, see the [GCP-2021-024](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-024) security bulletin.

1.8

Feature

### Release 1.8.5

Anthos clusters on bare metal 1.8.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.5 runs on Kubernetes 1.20.

1.7

Security

### Security bulletin (all minor versions)

A security issue was discovered in the Kubernetes ingress-nginx controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. For more information, see the [GCP-2021-024](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-024) security bulletin.

1.6

Security

### Security bulletin (all minor versions)

A security issue was discovered in the Kubernetes ingress-nginx controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. For more information, see the [GCP-2021-024](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-024) security bulletin.

1.8

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)
  * [CVE-2021-22946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22946)
  * [CVE-2021-22947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22947)
  * [CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)
  * [CVE-2021-40528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40528)



1.8

Issue

Known issues:

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

## October 19, 2021

1.7

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: 

  * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)
  * [CVE-2021-22946](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22946)
  * [CVE-2021-22947](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22947)
  * [CVE-2021-40528](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-40528)



1.7

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

1.7

Feature

### Release 1.7.5

Anthos clusters on bare metal 1.7.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos clusters on bare metal 1.7.5 runs on Kubernetes 1.19.

## October 04, 2021

1.9

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

For more information, see the [GCP-2021-021](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-021) security bulletin.

1.8

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

For more information, see the [GCP-2021-021](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-021) security bulletin.

1.7

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

For more information, see the [GCP-2021-021](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-021) security bulletin.

1.6

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server.

For more information, see the [GCP-2021-021](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-021) security bulletin.

## September 28, 2021

1.9

Feature

### Release 1.9.0

Anthos clusters on bare metal 1.9.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Anthos clusters on bare metal 1.9.0 runs on Kubernetes 1.21.

1.9

Feature

**Improved cluster lifecycle functionalities:**

  * **Preview:** Added ability to reset individual nodes with the `bmctl reset node` command. To give access to the needed cluster configuration file, use the command with the `-c` flag.

  * **Preview:** Added ability to recover from HA control plane quorum loss with`bmctl restore --control-plane-node` command.

  * Added `bmctl create ksa` command to create a Kubernetes Service Account (KSA) and generate a bearer token. To log in to the registered cluster, you can [use the token in Cloud Console **Kubernetes Engine** > **Clusters**](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/anthos-ui#logging_in_to_anthos_clusters_in_the_google_cloud_console).

  * **Preview:** Added `bmctl backup cluster` and `bmctl restore cluster` commands to [facilitate disaster recovery for clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/bmctl-backup-restore). 




**Introduced new troubleshooting capabilities:**

  * Updated the `bmctl check cluster --snapshot` command to support uploading cluster diagnostic snapshots to a Cloud Storage bucket for review by Cloud Customer Care.

  * Provided [access to bootstrap cluster logs](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/create-upgrade) to help troubleshoot cluster creation or upgrade problems.

  * **Preview:** Added support for [Node Problem Detector](https://github.com/kubernetes/node-problem-detector) service on nodes for quick detection of common node problems.




**Enhanced monitoring and logging:**

  * **GA:** Cloud Audit Logs capability is now generally available and enabled by default. Audit logs are useful for investigating suspicious API requests and for collecting statistics. For more information, see [Use Audit Logging](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/audit-logging).

  * Switched to new open telemetry-based metrics agents to improve reliability, ability to scale, and resource usage.




**Improved networking capabilities:**

  * **GA:** The [multi-NIC capability](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/multi-nic) to provide additional interfaces to your pods is now generally available. 

  * **Preview:** Added the single root I/O virtualization (SR-IOV) [container network interface (CNI) plugin](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/multi-nic#supported_cni_plugins) for multi-NIC.

  * Added support to configure cluster Domain Name System (DNS) provider options, such as upstream nameservers, with the new `ClusterDNS` custom resource definition.




**Enhanced security:**

  * SELinux is now always enabled in the container runtime for CentOS and RHEL. 

  * **Preview:** Enhanced the capability to [rotate cluster certificate authorities (CAs)](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/ca-rotation). Updates include support for all cluster types, rotation of front-proxy and etcd CAs, and changes to the `bmctl` command syntax. 

  * **Preview:** Added Okta group support for authentication in [Anthos Identity Service](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/identity-manage).




1.9

Change

**Functionality changes:**

  * Changed [default container runtime to containerd](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/runtime), `containerRuntime: containerd` for new clusters. Customers can still choose Docker as the container runtime.
  * **Preview:** Updated `bmctl` command, `bmctl reset nodes --force`, to support force removal of control plane nodes with etcd membership cleanup.

  * Added checks for cluster updates to verify access to cluster machines if changes to `loginUser` or `sshKeyPrivatePath` are detected. If the checks pass, Anthos clusters on bare metal saves the secret in the cluster.

  * Added new Anthos cluster control plane uptime dashboard in Cloud Monitoring with new metric `kubernetes.io/anthos/container/uptime` for component availability.

  * Added new alerts for control plane components availability with new metric `kubernetes.io/anthos/container/uptime` to replace deprecated alerts with metric `kubernetes.io/anthos/up`.




1.9

Fixed

**Fixes:**

  * Added missing registry mirror package required for Cloud Audit Logs to the Registry Mirror.

  * Fixed issue with containerd not finding `crictl` due to `/usr/local/bin` not being in the SSH user's PATH.

  * Fixed flapping node readiness issues caused by an unhealthy Pod Lifecycle Event Generator (PLEG).

  * Fixed kernel support issue for Ubuntu 18.04 and 18.04.1 that prevented the `anetd` networking controller from working properly. Anthos clusters on bare metal release 1.9.0 works with all kernels supplied with supported distributions.




1.9

Issue

**Known issues:**

  * [Control group v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) (cgroup v2) is not officially supported in Anthos clusters on bare metal release 1.9.0 and later. The presence of `/sys/fs/cgroup/cgroup.controllers` indicates that your system uses cgroup v2.

  * Anthos Service Mesh v1.10 is incompatible with Anthos clusters on bare metal release 1.9.0 running on Red Hat Enterprise Linux (RHEL) when SELinux is enabled. If you want to use Anthos Service Mesh, you must disable SELinux or set it to permissive mode on the host.




For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## September 21, 2021

1.8

Feature

### Release 1.8.4

Anthos clusters on bare metal 1.8.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/downloads#184). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.4 runs on Kubernetes 1.20.

1.8

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed: \- [CVE-2021-3711](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3711) \- [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712) \- [CVE-2021-20305](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20305) \- [CVE-2021-33560](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33560)

1.8

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see Anthos clusters on bare metal [known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

## September 20, 2021

1.7

Feature

### Release 1.7.4

Anthos clusters on bare metal release 1.7.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/downloads#174). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos clusters on bare metal 1.7.4 runs on Kubernetes 1.19.

1.8

Security

### Security bulletin (1.7 and 1.8)

A security issue was discovered in Kubernetes, [CVE-2021-25741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741), where a user may be able to create a container with subpath volume mounts to access files and directories outside of the volume, including on the host filesystem. This vulnerability affects all clusters created or upgraded with Anthos clusters on bare metal 1.7.x and 1.8.x releases, specifically 1.7.3 and earlier and 1.8.2 and earlier.

To fix this vulnerability, upgrade your Anthos clusters to version 1.7.4 or 1.8.3. For more information, see the [GCP-2021-018](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-018) security bulletin.

1.7

Security

### Security bulletin (1.7 and 1.8)

A security issue was discovered in Kubernetes, [CVE-2021-25741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741), where a user may be able to create a container with subpath volume mounts to access files and directories outside of the volume, including on the host filesystem. This vulnerability affects all clusters created or upgraded with Anthos clusters on bare metal 1.7.x and 1.8.x releases, specifically 1.7.3 and earlier and 1.8.2 and earlier.

To fix this vulnerability, upgrade your Anthos clusters to version 1.7.4 or 1.8.3. For more information, see the [GCP-2021-018](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-018) security bulletin.

1.7

Fixed

**Fixes:**

  * Fixed vulnerability [CVE-2021-25741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741) that might allow users to create a container with subpath volume mounts to access files and directories outside of the volume, including on the host filesystem. This vulnerability affects all clusters created or upgraded with Anthos clusters on bare metal release 1.7.0. For more information, see the [GCP-2021-018](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-018) security bulletin.

  * Updated the Kubernetes patch version to address the following container image security vulnerabilities: 

    * [CVE-2021-3711](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3711)
    * [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712)
    * [CVE-2021-20305](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20305)
    * [CVE-2021-33560](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33560)
    * [CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)



1.7

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

## August 27, 2021

1.8

Feature

### Release 1.8.3

Anthos clusters on bare metal 1.8.3 is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.3 runs on Kubernetes 1.20.

1.8

Breaking

**Breaking changes:**

In Anthos clusters on bare metal release 1.8.0, we added a kernel version requirement for Ubuntu 18.04. We required a Linux kernel version of 4.17.0 or later. Anthos clusters on bare metal release 1.8.3 again supports all Linux kernel versions that ship with Ubuntu 18.04 and 20.04 distributions. As a result of this change, however, the [egress NAT gateway](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/egress-nat) feature that was provided for Preview in release 1.8.0 does not work with Anthos clusters on bare metal release 1.8.3.

1.8

Feature

**Features:**

  * **Preview:** Anthos Identity Service now works with Anthos clusters on bare metal to support LDAP authentication methods in addition to OIDC. You can use AIS with Microsoft Active Directory without the need for provisioning Active Directory Federation Services. For more information, see [Setting up Anthos Identity Service with LDAP](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap).

  * **Preview:** Anthos Metadata Agent replaces Stackdriver Metadata Collector and collects more accurate and usable metadata for Kubernetes resources. When you [configure logging and monitoring](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/log-monitoring), you need to enable the [Config Monitoring for Ops API](https://console.cloud.google.com/apis/api/opsconfigmonitoring.googleapis.com/overview) and grant the `opsconfigmonitoring.resourceMetadata.writer` IAM role to your logging-monitoring service account. If Anthos clusters on bare metal is [installed behind a proxy](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/installing/proxy), your proxy server must also allow connections to `opsconfigmonitoring.googleapis.com`.

  * Added preflight checks to verify that specific APIs are enabled for your Google Cloud project. Preflight checks return an error if any of the following APIs aren't enabled for your project:

    * `anthos.googleapis.com`
    * `anthosaudit.googleapis.com`
    * `anthosgke.googleapis.com`
    * `cloudresourcemanager.googleapis.com`
    * `gkeconnect.googleapis.com`
    * `gkehub.googleapis.com`
    * `iam.googleapis.com`
    * `opsconfigmonitoring.googleapis.com`
    * `logging.googleapis.com`
    * `monitoring.googleapis.com`
    * `stackdriver.googleapis.com`

To enable these APIs when you create a cluster configuration file, use the `--enable-apis` flag with the `bmctl create config` command. For an example that uses the `--enable-apis` flag, see [Create an admin cluster config with bmctl](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/installing/creating-clusters/admin-cluster-creation#create_an_admin_cluster_config_with_bmctl).

  * Added preflight checks for the following machine requirements:

    * Minimum supported Linux kernel version
    * Minimum required CPU
    * Minimum required RAM



1.8

Change

**Changes:**

  * The Kubevirt version used for [working with VM-based workloads](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/vm-workloads) is now v0.43.0-gke.3.
  * The bootstrap cluster is deleted when a cluster upgrade completes without errors.



For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

1.8

Fixed

**Fixes:**

  * Fixed the following container image security vulnerabilities: 
    * [CVE-2021-3520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3520)
    * [CVE-2021-20305](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20305)
    * [CVE-2021-22924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22924)
    * [CVE-2021-22925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22925)
    * [CVE-2021-31535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31535)
    * [CVE-2021-33560](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33560)
    * [CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)
  * Fixed cluster creation and cluster update failures for nodes running CentOS or Red Hat Enterprise Linux (RHEL) with both SELinux and Cloud Audit Logs enabled.
  * Fixed Transmission Control Protocol (TCP) connection leakage issue.
  * Fixed an issue that prevented cert-manager from issuing ACME certificates over HTTP due to `ImagePullBackOff` errors.



## August 16, 2021

1.7

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

1.7

Feature

### Release 1.7.3

Anthos clusters on bare metal 1.7.3 is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos clusters on bare metal 1.7.3 runs on Kubernetes 1.19.

1.7

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed:

  * [CVE-2021-3520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3520)
  * [CVE-2021-20305](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20305)
  * [CVE-2021-22924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22924)
  * [CVE-2021-22925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22925)
  * [CVE-2021-31535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31535)
  * [CVE-2021-33560](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33560)
  * [CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)



## August 13, 2021

1.6

Feature

### Release 1.6.4

Anthos clusters on bare metal 1.6.4 is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/how-to/upgrade). Anthos clusters on bare metal 1.6.4 runs on Kubernetes 1.18.

1.6

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed:

  * [CVE-2021-3520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3520)
  * [CVE-2021-20305](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20305)
  * [CVE-2021-22924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22924)
  * [CVE-2021-22925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22925)
  * [CVE-2021-31535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31535)
  * [CVE-2021-33560](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33560)
  * [CVE-2021-33910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33910)



1.6

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/troubleshooting/known-issues) in the Troubleshooting section.

## July 29, 2021

1.8

Feature

**Features:**

  * **Preview:** Added capability to rotate cluster certificate authorities (CAs) for user clusters. For instructions on using the `bmctl cluster credentials` command to rotate cluster CAs, see [Rotate user cluster certificate authority](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/ca-rotation).

  * **Preview:** Added support for AppArmor with Anthos clusters on bare metal. You don't need to disable AppArmor on Ubuntu as a prerequisite for installation. When you create new 1.8.2 clusters or upgrade clusters to version 1.8.2, you can enable AppArmor either before or after you upgrade.




1.8

Feature

### Release 1.8.2

Anthos clusters on bare metal 1.8.2 is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.2 runs on Kubernetes 1.20.

1.8

Change

**Functionality changes:**

  * Expanded snapshots to include resource usage metrics to improve troubleshooting and support. Added metrics include the output of `ip neigh`, `kubectl top nodes`, and `kubectl top pods` commands.



For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

1.8

Fixed

**Fixes:**

  * Fixed [CVE-2021-3520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3520) vulnerability related to a flaw in lz4, which provides support for [LZ4](https://en.wikipedia.org/wiki/LZ4_\(compression_algorithm\)) a lossless compression algorithm. The flaw impacts availability, but has potential to impact confidentiality and integrity as well.

  * Fixed `bmctl` operation failures that occur for some Ubuntu 20.04 LTS distributions with a more recent Linux kernel, including Ubuntu 20.04 LTS images on the 5.8 kernel. For more information about this issue and a workaround, see [Ubuntu 20.04 LTS and bmctl](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues#ubuntu_2004_lts_and_bmctl).

  * Fixed OpenStack support for user clusters. In prior releases, cluster creation fails for user type clusters when the `baremetal.cluster.gke.io/external-cloud-provider: "true"` annotation is added to the cluster configuration file.

  * Fixed PATH environment issues for executing commands as a non-root user. For more information, see [Known Issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues).

  * Fixed an issue that caused user cluster resets (`bmctl reset cluster`) to get stuck while deleting namespaces.

  * Fixed out-of-memory (OOM) conditions related to Connect Agent memory usage that resulted in pod failures.

  * Fixed issue that blocked snapshots for clusters configured for passwordless `SUDO` capability for machine login (`nodeAccess.loginUser: <login user name>`).

  * Fixed issue that blocked some 1.7.x version admin, hybrid, or standalone clusters from upgrading to the 1.8 minor release. This issue affected some clusters that were updated by applying changes from an updated cluster configuration file.

  * Fixed Address Resolution Protocol (ARP) table issue for high-availability (HA) deployments that blocked upgrades from completing.




## July 02, 2021

1.8

Feature

### Release 1.8.1

Anthos clusters on bare metal **release 1.8.1** is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos on bare metal 1.8.1 runs on Kubernetes 1.20.

1.8

Fixed

**Fixes:**

Fixed [CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824) that could expose private keys and certificates from Kubernetes secrets through the `credentialName` field when using `Gateway` or `DestinationRule`. This vulnerability affects all clusters created or upgraded with Anthos clusters on bare metal release 1.8.0. For more information, see the [GCP-2021-012](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-012) security bulletin.

For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

## June 30, 2021

1.8

Security

### Security bulletin (1.8)

The Istio project recently [announced](https://istio.io/latest/news/security/istio-security-2021-007/) a security vulnerability ([CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824)) where credentials specified in the `credentialName` field for `Gateway` or `DestinationRule` can be accessed from different namespaces. This vulnerability affects all clusters created or upgraded with Anthos clusters on bare metal release 1.8.0. For more information, see the [GCP-2021-012](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-012) security bulletin.

## June 21, 2021

1.8

Feature

### Release 1.8.0

Anthos clusters on bare metal **release 1.8.0** is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade). Anthos clusters on bare metal 1.8.0 runs on Kubernetes 1.20.

1.8

Feature

**Extended installation support:**

  * Provided support to [use containerd as the container runtime](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/installing/runtime) as GA for Anthos clusters on bare metal release 1.8.0. Cluster upgrades to 1.8.0 are blocked for 1.7.x clusters that are configured to use the preview containerd capability. For more information, see [Upgrading 1.7.x clusters that use containerd](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues#containerd-upgrade) in Known Issues.
  * **Preview:** Improved virtual machine (VM) management capability. Anthos VM Runtime uses KubeVirt to orchestrate VMs on clusters, allowing you to work with your VM-based apps and workloads in a uniform development environment. Anthos VM Runtime has worked with Anthos clusters on bare metal as a preview feature since November 2020 and we have continued to enhance its capability. For more information, see [Working with VM-based workloads](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/vm-workloads).
  * Added edge profile support for standalone clusters. The edge profile is recommended for edge devices with limited resources. Add `profile: edge` to the cluster config file when you create a standalone cluster to produce a cluster that has significantly reduced system resource requirements. The edge profile is only available for standalone clusters, it is ignored for other cluster types. For more information, see [Creating standalone clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/installing/creating-clusters/standalone-cluster-creation).
  * Added support to specify provider ID for Nodes (`controlPlane.nodePoolSpec.nodes.providerID`) to support deploying on OpenStack using Load Balancing as a Service (LBaaS) resources. For more information, see [Configure your clusters to use OpenStack](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/installing/openstack).
  * **Preview:** Added support for installing Anthos clusters on bare metal, using your own registry service, instead of `gcr.io`. For instructions and additional information, see [Installing Anthos Bare Metal using registry mirror](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/installing/registry-mirror).



**Improved upgrade:**

  * Enabled support for upgrading non-SELinux clusters to SELinux. For more information, see [Enable SELinux](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/upgrade#enable-selinux) in Upgrading Anthos clusters on bare metal.
  * Cluster upgrades are not blocked by excessive Node draining durations. During a cluster upgrade, if the draining process takes longer than 20 minutes for any specific Node, the upgrade process will carry on without waiting for draining to complete.



**Updated user cluster lifecycle management:**

  * Added `bmctl` improvements for resetting user cluster and adding additional preflight checks to confirm machine and network readiness for cluster creation:



**Enhanced monitoring and logging:**

  * **Preview:** Added Cloud Audit Logging capability, which enables audit logs to be written to [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit) in your Google project. Audit logs are useful for investigating suspicious API requests and for collecting statistics. For more information, see [Enable Audit Logging](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/audit-logging).



**Introduced new networking capabilities in preview:**

  * **Preview:** Added multi-NIC capability to provide additional interfaces to your Pods. 
  * **Preview:** Added egress NAT gateway capability to provide persistent, deterministic routing for the egress traffic from your clusters. For more information, see [Configure an egress NAT gateway for external communication](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/egress-nat).
  * **Preview:** Added option for BGP bundled load balancer for Layer-3 (L3) topologies. This feature can be used with user clusters and admin clusters.



**Enhanced security:**

  * Workload Identity is GA. The Connect Agent Service Account Key is no longer required during installation. Connect Agent uses Workload Identity to authenticate to Google Cloud instead of an exported Google Cloud Service Account Key. 



**Expanded support for newer versions of operating systems:**

  * Added support for installing Anthos clusters on bare metal on Red Hat Enterprise Linux (RHEL) 8.4, and CentOS 8.4



1.8

Issue

**Known issues:**

  * If a Node is out of reach, Anthos clusters on bare metal can't start the draining process, which may impact the cluster upgrade process. For more information, see [Node draining can't start when Node is out of reach](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues#node-drain).
  * Upgrading from 1.7.x clusters that use containerd as the container runtime to 1.8.0 is blocked. For more information, see [Upgrading 1.7.x clusters that use containerd](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues#containerd-upgrade).
  * When running Anthos clusters on bare metal with firewalld enabled on either CentOS or Red Hat Enterprise Linux (RHEL), changes to firewalld can remove the Cilium `iptables` chains on the host network. The loss of the Cilium iptables chains causes the Pod on the Node to lose network connectivity outside of the Node. for more information, see [Modifying firewalld will erase Cilium `iptable` chains](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues#firewalld-mod).



For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.8/troubleshooting/known-issues) in the Troubleshooting section.

1.8

Fixed

**Fixes:**

  * Resolved, as part of the GA support for using containerd as the container runtime, incorrect cgroup driver use. Newly created 1.8.0 clusters that are configured to use containerd will use the correct `systemd` cgroup driver.
  * Fixed issue that prevented usage metrics for the containerd process from being collected by Cloud Logging. This fix applies to newly created 1.8.0 clusters only.



1.8

Change

**Functionality changes:**

  * Added `--workspace-dir` flag to `bmctl` to allow changing the path and name of the workspace directory from the default `bmctl-workspace`. The workspace directory contains the configuration and log files generated by `bmctl`. When using the `bmctl` command, pass in a `--workspace-dir` flag to specify a non-default workspace directory location. If the directory does not exist, `bmctl` will create it for you.
  * Moved away from `iptables`-based NodePort and masquerade handling to eBPF-based management. NodePort and masquerade handling are now applied to the _Node IP_ and _default gateway_ interfaces only.



## June 02, 2021

1.7

Feature

### Release 1.7.2

Anthos clusters on bare metal **release 1.7.2** is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos clusters on bare metal 1.7.2 runs on Kubernetes 1.19.

1.7

Fixed

**Fixes:**

  * Fixed [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735) that could allow node updates to bypass a Validating Admission Webhook. For more details, open the **Anthos clusters on bare metal** tab of the [GCP-2021-003](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-003) security bulletin.
  * Resolved the `bmctl snapshot` command failure when the user creates a custom cluster namespace omitting "cluster-" prefix from the cluster config file. The prefix is no longer required for a custom cluster namespace.
  * Added webhook blocks to prevent users from modifying control plane node pool and load balancer node pool resources directly. Control plane and load balancer node pools for Anthos clusters on bare metal are specified in the cluster resource, using the `spec.controlPlane.nodePoolSpec` and `spec.LoadBalancer.nodePoolSpec` sections of the cluster config file respectively.
  * Fixed the cluster upgrade command, `bmctl upgrade cluster`, to prevent it from interfering with user-installed Anthos Service Mesh (ASM).



1.7

Change

**Functionality changes:**

  * Updated the `bmctl check snapshot` command so that it includes certificate signing requests in the snapshot.
  * Changed the upgrade process to prevent node drain issues from blocking upgrades. The upgrade process triggers a node drain. Now, if the node drain takes longer than 20 minutes, the upgrade process carries on to completion even when the draining hasn't completed. In this case, the upgrade output reports the incomplete node drain. Excessive drain times signal a problematic with pods. You may need to restart problem pods.
  * Updated cluster creation process, `bmctl create cluster`, to display logged errors directly on the command line. Prior to this release, detailed error messages were only available in the log files.



1.7

Issue

**Known issues:**

  * Node logs from nodes with a dot (".") in their name are not exported to Cloud Logging. For workaround instructions, see [Node logs aren't exported to Cloud Logging](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues#node_logs_arent_exported_to) in Anthos clusters on bare metal known issues.



For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

## May 17, 2021

1.6

Issue

**Known issues:**

When you upgrade Anthos clusters on bare metal from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version to ensure you have the latest security fixes. Always review the release notes before upgrading so you're aware of what has changed, including security fixes and known issues. Upgrading to a lower release version isn't supported.

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/troubleshooting/known-issues) in the Troubleshooting section.

1.6

Feature

### Release 1.6.3

Anthos clusters on bare metal **release 1.6.3** is now available. To upgrade, see [Upgrading Anthos clusters on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/how-to/upgrade). Anthos clusters on bare metal 1.6.3 runs on Kubernetes 1.18.

1.6

Fixed

**Fixed:**

  * Fixed [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735) that could allow node updates to bypass a Validating Admission Webhook. For more details, open the **Anthos clusters on bare metal** tab of the [GCP-2021-003](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-003) security bulletin. 
  * Fixed [CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682), and [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258). For more details, open the **Anthos clusters on bare metal** tab of the [GCP-2021-004](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-004) security bulletin.



## May 06, 2021

1.7

Security

### Security bulletin (1.6 and 1.7)

The Envoy and Istio projects recently [announced](https://istio.io/latest/news/security/istio-security-2021-003) several new security vulnerabilities ([CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682), and [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258)) that could allow an attacker to crash Envoy.

For more information, see the [GCP-2021-004](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-004) security bulletin.

1.6

Security

### Security bulletin (1.6 and 1.7)

The Envoy and Istio projects recently [announced](https://istio.io/latest/news/security/istio-security-2021-003) several new security vulnerabilities ([CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682), and [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258)) that could allow an attacker to crash Envoy.

For more information, see the [GCP-2021-004](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-004) security bulletin.

## April 30, 2021

1.7

Feature

### Release 1.7.1

Anthos clusters on bare metal **release 1.7.1** is now available. To upgrade, see [Upgrading Anthos clusters on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos clusters on bare metal 1.7.1 runs on Kubernetes 1.19.

1.7

Fixed

**Fixes:**

  * **(Updated May 12, 2021)** Fixed [CVE-2021-28683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28683), [CVE-2021-28682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28682), [CVE-2021-29258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29258). For more details, see the [GCP-2021-004](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-004) security bulletin.
  * Fixed potential stuck upgrade from 1.6.x to 1.7.0. The bug was caused by a rare race condition when the coredns configmap failed to be backed up and restored during the upgrade.
  * Fixed potential missing GKE connect agent during installation due to a rare race condition.
  * Fixed issue that prevented automatic updates to the control plane load balancer config when adding/removing node(s) from the control plane node pool.
  * Addressed problem with syncing NodePool taints and labels that resulted in deletion of pre-existing items. Syncs will now append, update, or delete items that are added by taints and labels themselves only.



1.7

Change

**Functionality changes:**

  * Customers can now take cluster snapshots regardless of whether the admin cluster control plane is running. This is helpful for diagnosing installation issues.
  * Deploying Anthos clusters on bare metal with SELinux is now fully supported on supported versions of Redhat Enterprise Linux. This applies for new installations of Anthos clusters on bare metal cases only.
  * User cluster creation with `bmctl` supports credential inheritance from the admin cluster by default. Credential overrides for the user cluster can be specified in the config file during cluster creation.



1.7

Issue

**Known issues:**

  * Upgrading the container runtime from containerd to Docker will fail in Anthos clusters on bare metal release 1.7.1. This operation is not supported while the containerd runtime option is in preview.
  * `bmctl snapshot` command fails when the user creates a custom cluster namespace omitting `cluster-` prefix from the cluster config file. To avoid this issue, the cluster namespace should follow the `cluster-$CLUSTER_NAME` naming convention.



For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

## April 20, 2021

1.7

Security

### Security bulletin (1.6 and 1.7)

The Kubernetes project recently [announced](https://groups.google.com/forum/#!topic/kubernetes-security-announce/FKAGqT4jx9Y) a new security vulnerability, [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735), that could allow node updates to bypass a Validating Admission Webhook. For more details, see the [GCP-2021-003 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-003).

1.6

Security

### Security bulletin (1.6 and 1.7)

The Kubernetes project recently [announced](https://groups.google.com/forum/#!topic/kubernetes-security-announce/FKAGqT4jx9Y) a new security vulnerability, [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735), that could allow node updates to bypass a Validating Admission Webhook. For more details, see the [GCP-2021-003 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-003).

## March 25, 2021

1.7

Feature

### Release 1.7.0

Anthos clusters on bare metal **release 1.7.0** is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade). Anthos on bare metal 1.7.0 runs on Kubernetes 1.19.

**Extended installation support:**

  * Added requirement for Anthos clusters on bare metal connectivity with Google Cloud for install and upgrade operations. As of 1.7.0 preflight checks will check for connectivity to Google Cloud, enabled APIs, and permissions for service accounts. Existing clusters need to be registered in Google Cloud before upgrading. The connectivity checks are not overridable by the `--force` flag. For details, see the [cluster creation](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/installing/creating-clusters/create-clusters-overview) and [cluster upgrade](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/upgrade) documentation.

  * Added support for installing Anthos clusters on bare metal on OpenStack. For configuration instructions, see [Configure your clusters to use OpenStack](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/installing/openstack). 

  * Added support for installing Anthos clusters on bare metal, using a private package repository instead of the default Docker APT repository. For instructions and additional information, see [Use a private package repository server](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/installing/package-server).

  * Removed installation prerequisite for setting Security-Enhanced Linux (SELinux) operational mode to be permissive. The related preflight check has been removed, as well.

  * Removed installation prerequisite for disabling firewalld . The related preflight check has also been removed. For information on configuring ports to use firewalld with Anthos clusters on bare metal, see [Configuring firewalld ports](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/concepts/network-reqs#configuring_firewalld_ports) on the Network requirements page.

  * Updated requirements for installing behind a proxy server and removed restriction on system-wide proxy configurations. For a detailed list of prerequisites, see [Installing behind a proxy](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/installing/proxy).




**Improved upgrade:**

  * Updated cluster upgrade routines to ensure worker node failures do not block cluster upgrades, providing a more consistent user experience. Control plane node failures will still block cluster upgrades. 

  * Added `bmctl` support for running upgrade preflight checks. `bmctl check preflight` will run upgrade preflight checks if users specify the `--kubeconfig` flag. For example:  
`bmctl check preflight --kubeconfig bmctl-workspace/cluster1/cluster1-kubeconfig`




**Updated user cluster lifecycle management:**

  * Added support in `bmctl` for user cluster creation and upgrade functions.

  * Improved resource handling. Anthos clusters on bare metal now reconciles node pool taints and labels to nodes unless the node has a `baremetal.cluster.gke.io/label-taint-no-sync` annotation. 




**Enhanced monitoring and logging:**

  * **Preview:** Added out-of-the-box alerts for critical cluster metrics and events. For information on working with alerting policies and getting notified, see [Creating alerting policies](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/how-to/alerting-policies-creating).

  * Added support for collecting ansible job logs in admin and hybrid clusters by default.




**Expanded support for newer versions of operating systems:**

  * Added support for installing Anthos clusters on bare metal on Red Hat Enterprise Linux (RHEL) 8.3 and CentOS 8.3.



1.7

Issue

**Known issues:**

  * Under rare circumstances, `bmctl upgrade` may become stuck at the `Moving resources to upgraded cluster` stage after finishing upgrading all nodes in the cluster. The issue does not affect cluster operation, but the final step needs to be finished. 

If `bmctl` does not move forward after 30 minutes in this state, re-run the `bmctl upgrade` command to complete the upgrade. 

The issue is captured in the `upgrade-cluster.log` file located in `.../bmctl-workspace/<cluster name>/log/upgrade-cluster-<timestamp>`. The following log entry shows how the failure is reported:

`Operation failed, retrying with backoff. Cause: error creating "baremetal.cluster.gke.io/v1, Kind=Cluster" <cluster name>: Internal error occurred: failed calling webhook "vcluster.kb.io": Post "https://webhook-service.kube-system.svc:443/validate-baremetal-cluster-gke-io-v1-cluster? timeout=30s": net/http: TLS handshake timeout`




For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/troubleshooting/known-issues) in the Troubleshooting section.

1.7

Change

**Functionality changes:**

  * Added support for configuring the number of pods per node. New clusters can be configured to run up to 250 pods per node. For more information about configuring nodes, see [Pod networking](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.7/concepts/network-reqs#pod_networking). You can find additional information for configuring pods in the cluster creation documentation.
  * **Preview:** Added support to use containerd as the container runtime. Anthos clusters on bare metal 1.6.x supports only Docker for container runtime (dockershim). In 1.7.0, Kubelet can be configured to use either Docker or containerd, using the new `containerRuntime` cluster config field. You must upgrade existing clusters to 1.7.0 to add or update the `containerRuntime` field.
  * Added support for more load balancer `addressPool` entries under `cluster.spec.loadBalancer.addressPools`. For existing `addressPools`, users can use `cluster.spec.loadBalancer.AddressPools[].manualAssign` specify additional `addressPool` entries.



## February 26, 2021

1.6

Feature

### Release 1.6.2

Anthos clusters on bare metal **release 1.6.2** is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/how-to/upgrade). Anthos on bare metal 1.6.2 runs on Kubernetes 1.18.

1.6

Fixed

**Fixes:**

  * Updated custom resource API to reject changes to Cluster and NodePool configuration fields that are not currently supported. For a list of supported mutable fields, see [Configuration](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/troubleshooting/known-issues#configuration) in Known Issues. 
  * Updated `bmctl` to allow creating or upgrading Anthos clusters on bare metal to the current `bmctl` version (1.6.2) only. For more information about version restrictions, see [Installation](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/troubleshooting/known-issues#161_version_of_bmctl_cannot_install_160_clusters) in Known Issues.
  * Fixed an issue that caused the automatic reset of bare metal machines to fail after deleting the user cluster.
  * Added preflight check to verify that [control group v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html), or cgroup v2 for short, is not in use on the cluster machine. Anthos on bare betal 1.6.x is incompatible with cgroup v2. For more information, see [Control group v2 incompatibility](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/troubleshooting/known-issues#control_group_v2_incompatibility) in Known Issues.
  * Updated `csi-snapshot-validation-webhook` to support certification rotation. For more information about certificate rotation, see [Security](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/troubleshooting/known-issues#security) in Known Issues.
  * Fixed an issue to prevent constant patching for `snapshot.storage.k8s.io` CRDs.
  * Fixed a Certificate Signing Request (CSR) issue with `kubelet` to ensure fully qualified domain name(FQDN) hostnames are supported. 



For information about the latest known issues, see [Anthos on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/troubleshooting/known-issues) in the Troubleshooting section.

## January 29, 2021

1.6

Feature

### Release 1.6.1

Anthos clusters on bare metal **release 1.6.1** is now available. To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.6/how-to/upgrade). Anthos on bare metal 1.6.1 runs on Kubernetes 1.18.6-gke.6600.

1.6

Change

**Functionality changes:**

  * Added upgrade support from 1.6.0. Users are able to upgrade existing Anthos bare metal cluster from 1.6.0 to 1.6.1.
  * Improved upgrade preflight check. Added preflight check before cluster upgrade to validate current cluster status, machine health and other issues before proceeding to upgrade.
  * Added support for deleting mounts and data from the anthos-system StorageClass during `bmctl reset`.
  * Relaxed the requirement for an odd number of control plane node pools to allow customers to add and remove nodes for maintenance or replacement.
  * Added support to force removing a broken worker node through annotation on the operator machine.
  * Added etcddefrag pod to control-plane nodes, which are responsible for monitoring etcd's database size and defragmenting the database as needed. This helps reclaim etcd database size and recover etcd when its disk space is exceeded.
  * Enabled kubelet server TLS certification auto-rotation. Kubelet on each node sends out CSR when nearing serving certificate expiration. A controller running inside the admin cluster validates and approves the CSR for user clusters.
  * Added proxy support to connect to the OIDC provider. This allows overriding the cluster proxy configuration with a different proxy.
  * Added `bmctl update cluster` for updating standalone clusters.



1.6

Fixed

**Fixes:**

  * Fixed bug causing cluster deletion stall problem because of pods refusing to evacuate, or dead nodes.



## November 30, 2020

1.6

Feature

### Release 1.6.0

**Anthos on bare metal is generally available**

Anthos on bare metal is a deployment option to run Anthos on physical or virtual servers, deployed on an operating system provided by you, without a hypervisor layer. Anthos on bare metal ships with built-in networking, lifecycle management, diagnostics, health checks, logging, and monitoring. Anthos on bare metal supports CentOS, Red Hat Enterprise Linux (RHEL), and Ubuntu—all validated by Google. With Anthos on bare metal, you can use your company's standard hardware and operating system images, taking advantage of existing investments, which are automatically checked and validated against Anthos infrastructure requirements. 

Anthos on bare metal is available today, with either subscription or pay-as-you-go [pricing](https://cloud.google.com/anthos/pricing). Anthos on bare metal lets you leverage existing investments in hardware, OS, and networking infrastructure. The minimum system requirement to run Anthos on bare metal is 2 nodes with a minimum total of 4 cores, 32 GB RAM, and 128 GB of disk space with no specialized hardware. The setup lets you run Anthos on bare metal on almost any infrastructure.

Anthos on bare metal uses a "bring your own operating system" model. It runs atop physical or virtual instances, and supports Red Hat Enterprise Linux 8.1/8.2, CentOS 8.1/8.2, or Ubuntu 18.04/20.04 LTS. Anthos provides overlay networking and L4/L7 load balancing. You can also integrate with your own load balancer such as F5 and Citrix. For storage, you can deploy persistent workloads using [CSI integration](https://kubernetes-csi.github.io/docs/drivers.html) with your existing infrastructure.

You can deploy Anthos on bare metal using one of the following deployment models:

  * **A standalone model** lets you manage every cluster independently. This is a good choice when running in an edge location or if you want your clusters to be administered independent of one another. 
  * **The multiple-cluster model** lets central IT teams manage a fleet of clusters from a centralized cluster, called the admin cluster. This is more suitable if you want to build automation or tooling, or if you want to delegate the lifecycle of clusters to individual teams without sharing sensitive credentials such as SSH keys or Google Cloud service account details.



Like with all Anthos environments, a bare metal cluster has a thin, secure connection back to Google Cloud called [Connect](https://cloud.google.com/anthos/multicluster-management/connect/overview). After it's installed in your clusters, you can centrally view, configure, and monitor your clusters from the Google Cloud Console. 

Anthos on bare metal, which is part of the Anthos 1.6 release, provides the following features and capabilities:

  * Kubernetes 1.18
  * Ubuntu/RHEL/CentOS support
  * Standalone and multiple-cluster architecture
  * In-place upgrades (minor and major)
  * Overlay networking, Ingress (L7), integrated load balancing (L4, L2-Mode) 
  * Manual load balancing (F5, Citrix)
  * Installs behind proxy support
  * Preflight and health checks
  * Node maintenance mode
  * Cloud Monitoring and Cloud Logging
  * ACM, ASM, identity, hub or connect, billing, and pay-as-you-go
  * NVIDIA GPU support
  * Scales to 500 nodes
  * Virtual machine management (Kubevirt) preview



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
