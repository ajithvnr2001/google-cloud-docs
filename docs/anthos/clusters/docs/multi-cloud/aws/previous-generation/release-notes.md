---
url: https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/release-notes/
title: GKE on AWS release notes \u00a0|\u00a0 Anthos clusters on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:14.964247+00:00
---

# GKE on AWS release notes  |  Anthos clusters on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/release-notes/

The product described by this documentation, Anthos Clusters on AWS (previous generation), is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/previous-generation/turndown-announcement). All new installs must use the current generation product, [Anthos clusters on AWS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/previous-generation/current-docs-link). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Anthos clusters on AWS (previous generation) ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/previous-generation)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/previous-generation/resources)



Send feedback 

#  GKE on AWS release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to GKE on AWS. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gkeonaws-release-notes.xml) directly. 

## January 26, 2023

Announcement

Anthos clusters on AWS (previous generation) aws-1.14.1-gke.0 is now available.

Feature

You can now launch clusters with the following Kubernetes versions:

  * 1.23.15-gke.2000
  * 1.24.9-gke.2100
  * 1.25.5-gke.2100



Security

This release fixes the following vulnerabilities:

  * [CVE-2022-23471](https://nvd.nist.gov/vuln/detail/CVE-2022-23471)



Feature

Upgraded to containerd 1.6.12.

## December 21, 2022

Security

A new vulnerability (CVE-2022-2602) has been discovered in the io_uring subsystem in the Linux kernel that can allow an attacker to potentially execute arbitrary code. For more information, see the [GCP-2022-2025 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-025).

## December 13, 2022

Announcement

Anthos clusters on AWS (previous generation) aws-1.14.0-gke.2 is now available.

Security

This release fixes the following vulnerabilities:

  * [CVE-2022-43680](https://nvd.nist.gov/vuln/detail/CVE-2022-43680)
  * [CVE-2022-43680](https://nvd.nist.gov/vuln/detail/CVE-2022-43680)
  * [CVE-2022-37434](https://nvd.nist.gov/vuln/detail/CVE-2022-37434)
  * [CVE-2022-37434](https://nvd.nist.gov/vuln/detail/CVE-2022-37434)
  * [CVE-2022-23218](https://nvd.nist.gov/vuln/detail/CVE-2022-23218)
  * [CVE-2021-33574](https://nvd.nist.gov/vuln/detail/CVE-2021-33574)
  * [CVE-2022-23219](https://nvd.nist.gov/vuln/detail/CVE-2022-23219)
  * [CVE-2019-25013](https://nvd.nist.gov/vuln/detail/CVE-2019-25013)
  * [CVE-2021-3999](https://nvd.nist.gov/vuln/detail/CVE-2021-3999)
  * [CVE-2020-10029](https://nvd.nist.gov/vuln/detail/CVE-2020-10029)
  * [CVE-2021-27645](https://nvd.nist.gov/vuln/detail/CVE-2021-27645)
  * [CVE-2019-19126](https://nvd.nist.gov/vuln/detail/CVE-2019-19126)
  * [CVE-2020-1752](https://nvd.nist.gov/vuln/detail/CVE-2020-1752)
  * [CVE-2016-10228](https://nvd.nist.gov/vuln/detail/CVE-2016-10228)
  * [CVE-2020-6096](https://nvd.nist.gov/vuln/detail/CVE-2020-6096)
  * [CVE-2020-27618](https://nvd.nist.gov/vuln/detail/CVE-2020-27618)
  * [CVE-2021-35942](https://nvd.nist.gov/vuln/detail/CVE-2021-35942)
  * [CVE-2021-3326](https://nvd.nist.gov/vuln/detail/CVE-2021-3326)



Deprecated

Kubernetes version 1.25 deprecates several APIs. See the [Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) for details.

Feature

You can now launch clusters with the following Kubernetes versions:

  * 1.23.13-gke.2000
  * 1.24.7-gke.2000
  * 1.25.3-gke.1900



## November 10, 2022

Security

Two new vulnerabilities ([CVE-2022-2585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2585) and [CVE-2022-2588](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2588)) have been discovered in the Linux kernel that can lead to a full container break out to root on the node.

For more information, see the [GCP-2022-024 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-024).

## October 31, 2022

Announcement

Anthos clusters on AWS (previous generation) aws-1.13.1-gke.1 is now available.

Feature

You can now launch clusters with the following Kubernetes versions:

  * 1.22.15-gke.1400
  * 1.23.12-gke.1400
  * 1.24.6-gke.1300



Security

This release fixes the following vulnerabilities:

  * [CVE-2021-3999](https://nvd.nist.gov/vuln/detail/CVE-2021-3999)
  * [CVE-2022-40674](https://nvd.nist.gov/vuln/detail/CVE-2022-40674)
  * [CVE-2021-46828](https://nvd.nist.gov/vuln/detail/CVE-2021-46828)
  * [CVE-2022-2526](https://nvd.nist.gov/vuln/detail/CVE-2022-2526)
  * [CVE-2022-1587](https://nvd.nist.gov/vuln/detail/CVE-2022-1587)
  * [CVE-2022-1586](https://nvd.nist.gov/vuln/detail/CVE-2022-1586)
  * [CVE-2022-37434](https://nvd.nist.gov/vuln/detail/CVE-2022-37434)
  * [CVE-2022-2509](https://nvd.nist.gov/vuln/detail/CVE-2022-2509)
  * [CVE-2022-3176](https://nvd.nist.gov/vuln/detail/CVE-2022-3176)
  * [CVE-2022-2602](https://nvd.nist.gov/vuln/detail/CVE-2022-2602)
  * [CVE-2022-2585](https://nvd.nist.gov/vuln/detail/CVE-2022-2585)



## October 28, 2022

Security

A new vulnerability, [CVE-2022-3176](https://nvd.nist.gov/vuln/detail/CVE-2022-3176), has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve full container breakout to root on the node.

For instructions and more details, see the [Anthos clusters on AWS security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-021-anthosaws).

## October 03, 2022

Announcement

Anthos clusters on AWS (previous generation) aws-1.13.0-gke.5 is now available.

Feature

You can now launch clusters with the following Kubernetes versions:

  * 1.22.15-gke.300
  * 1.23.12-gke.300
  * 1.24.6-gke.200



Security

This release fixes the following vulnerabilities:

  * [CVE-2022-1292](https://nvd.nist.gov/vuln/detail/CVE-2022-1292)
  * [CVE-2022-1586](https://nvd.nist.gov/vuln/detail/CVE-2022-1586)
  * [CVE-2022-2097](https://nvd.nist.gov/vuln/detail/CVE-2022-2097)
  * [CVE-2022-2068](https://nvd.nist.gov/vuln/detail/CVE-2022-2068)
  * [CVE-2022-34903](https://nvd.nist.gov/vuln/detail/CVE-2022-34903)
  * [CVE-2022-37434](https://nvd.nist.gov/vuln/detail/CVE-2022-37434)



Issue

If you use the deprecated `ubuntuRepositoryMirror: 'packages.cloud.google.com'` field in the AWSManagementService resource and are upgrading your node pool, you must upgrade only to the 1.22.15-gke.300 or 1.23.12-gke.300 versions included in this release. Upgrading to any other node pool version will cause your upgrade to hang. If your node pool is already hanging in the upgrading state, you need to delete and re-create the node pool. If you aren't using this field, this issue doesn't affect you and you can upgrade to any supported version.

## August 25, 2022

Announcement

Anthos clusters on AWS (previous generation) aws-1.12.2-gke.1 is now available.

Feature

You can now launch clusters with the following Kubernetes versions:

  * 1.21.14-gke.2900
  * 1.22.12-gke.1100
  * 1.23.9-gke.800



Security

This release fixes the following vulnerabilities:

  * [CVE-2022-29901](https://nvd.nist.gov/vuln/detail/CVE-2022-29901)
  * [CVE-2022-28693](https://nvd.nist.gov/vuln/detail/CVE-2022-28693)
  * [CVE-2022-29900](https://nvd.nist.gov/vuln/detail/CVE-2022-29900)
  * [CVE-2022-23825](https://nvd.nist.gov/vuln/detail/CVE-2022-23825)
  * [CVE-2020-29361](https://nvd.nist.gov/vuln/detail/CVE-2020-29361)
  * [CVE-2020-27350](https://nvd.nist.gov/vuln/detail/CVE-2020-27350)
  * [CVE-2021-20232](https://nvd.nist.gov/vuln/detail/CVE-2021-20232)
  * [CVE-2022-34903](https://nvd.nist.gov/vuln/detail/CVE-2022-34903)
  * [CVE-2020-24659](https://nvd.nist.gov/vuln/detail/CVE-2020-24659)
  * [CVE-2021-20305](https://nvd.nist.gov/vuln/detail/CVE-2021-20305)
  * [CVE-2021-43618](https://nvd.nist.gov/vuln/detail/CVE-2021-43618)
  * [CVE-2021-3580](https://nvd.nist.gov/vuln/detail/CVE-2021-3580)
  * [CVE-2021-20231](https://nvd.nist.gov/vuln/detail/CVE-2021-20231)
  * [CVE-2021-3520](https://nvd.nist.gov/vuln/detail/CVE-2021-3520)
  * [CVE-2020-29363](https://nvd.nist.gov/vuln/detail/CVE-2020-29363)
  * [CVE-2020-29362](https://nvd.nist.gov/vuln/detail/CVE-2020-29362)
  * [CVE-2022-1664](https://nvd.nist.gov/vuln/detail/CVE-2022-1664)
  * [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910)
  * [CVE-2018-25032](https://nvd.nist.gov/vuln/detail/CVE-2018-25032)



## August 08, 2022

Announcement

Anthos clusters on AWS (previous generation) aws-1.12.1-gke.0 is now available.

Feature

You can now launch clusters with the following Kubernetes versions:

  * 1.23.8-gke.2000
  * 1.22.12-gke.300
  * 1.21.14-gke.2100



Security

This release fixes the following vulnerabilities:

  * [CVE-2022-1292](https://nvd.nist.gov/vuln/detail/CVE-2022-1292)
  * [CVE-2022-2068](https://nvd.nist.gov/vuln/detail/CVE-2022-2068)
  * [CVE-2022-1271](https://nvd.nist.gov/vuln/detail/CVE-2022-1271)
  * [CVE-2018-25032](https://nvd.nist.gov/vuln/detail/CVE-2018-25032)
  * [CVE-2022-1271](https://nvd.nist.gov/vuln/detail/CVE-2022-1271)
  * [CVE-2022-31030](https://nvd.nist.gov/vuln/detail/CVE-2022-31030)
  * [CVE-2022-2327](https://nvd.nist.gov/vuln/detail/CVE-2022-2327)



## August 01, 2022

Security

A new vulnerability (CVE-2022-2327) has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve a full container breakout to root on the node.  
For more information, see the [GCP-2022-018 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-018).

## July 07, 2022

Announcement

Anthos clusters on AWS (previous generation) aws-1.12.0-gke.0 is now available.

Announcement

This release note has been updated to mark the actual date of release, July 7, 2022. Previously, the release date was mentioned as June 24th.

Feature

You can now launch clusters with the following Kubernetes versions:

  * 1.23.7-gke.1500
  * 1.22.10-gke.1500
  * 1.21.13-gke.1600



Feature

You can now launch Kubernetes 1.23 clusters.

Deprecated

Kubernetes 1.20 clusters are no longer supported. This version no longer supports creation or maintenance of Kubernetes 1.19 clusters.

Security

This release fixes the following vulnerabilities:

  * [CVE-2022-1292](https://nvd.nist.gov/vuln/detail/CVE-2022-1292).   
Note: this vulnerability is fixed in 1.23 clusters. It is still present in 1.21 and 1.22 clusters.
  * [CVE-2022-29581](https://nvd.nist.gov/vuln/detail/CVE-2022-29581)
  * [CVE-2022-29582](https://nvd.nist.gov/vuln/detail/CVE-2022-29582)
  * [CVE-2022-1116](https://nvd.nist.gov/vuln/detail/CVE-2022-1116)
  * [CVE-2021-4160](https://nvd.nist.gov/vuln/detail/CVE-2021-4160)
  * [CVE-2022-0778](https://nvd.nist.gov/vuln/detail/CVE-2022-0778)
  * [CVE-2021-43618](https://nvd.nist.gov/vuln/detail/CVE-2021-43618)



## June 23, 2022

Security

Three new memory corruption vulnerabilities (CVE-2022-29581, CVE-2022-29582, CVE-2022-1116) have been discovered in the Linux kernel. These vulnerabilities allow an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. For more information, refer to the [GCP-2022-016 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-016).

## June 01, 2022

Change

Anthos Clusters on AWS aws-1.11.1-gke.7 (previous generation) is now available. Clusters in this release support the following Kubernetes versions:

  * 1.22.9-gke.800
  * 1.21.12-gke.1000
  * 1.20.15-gke.7500



Security

This release fixes the following CVEs:

  * [CVE-2022-24769](https://nvd.nist.gov/vuln/detail/CVE-2022-24769)
  * [CVE-2022-1292](https://nvd.nist.gov/vuln/detail/CVE-2022-1292)
  * [CVE-2022-25235](https://nvd.nist.gov/vuln/detail/CVE-2022-25235)
  * [CVE-2022-25236](https://nvd.nist.gov/vuln/detail/CVE-2022-25236)
  * [CVE-2022-25315](https://nvd.nist.gov/vuln/detail/CVE-2022-25315)
  * [CVE-2022-23852](https://nvd.nist.gov/vuln/detail/CVE-2022-23852)
  * [CVE-2021-4160](https://nvd.nist.gov/vuln/detail/CVE-2021-4160)
  * [CVE-2022-25313](https://nvd.nist.gov/vuln/detail/CVE-2022-25313)
  * [CVE-2022-24407](https://nvd.nist.gov/vuln/detail/CVE-2022-24407)
  * [CVE-2022-23219](https://nvd.nist.gov/vuln/detail/CVE-2022-23219)
  * [CVE-2022-23218](https://nvd.nist.gov/vuln/detail/CVE-2022-23218)
  * [CVE-2021-3999](https://access.redhat.com/security/cve/cve-2021-3999)



## May 02, 2022

Announcement

Anthos Clusters on AWS aws-1.11.0-gke.6 (previous generation) is now available. Clusters in this release support the following Kubernetes versions:

  * 1.22.8-gke.1300
  * 1.21.11-gke.1100
  * 1.20.15-gke.5200



Change

This release removes unneeded permissions from the `coredns-autoscaler`, `calico-typha`, and `konnectivity-agent-autoscaler` components.

Fixed

This release fixes the following CVEs:

  * [CVE-2022-0492](https://nvd.nist.gov/vuln/detail/CVE-2022-0492)
  * [CVE-2022-1055](https://nvd.nist.gov/vuln/detail/CVE-2022-1055)



Fixed

The issue announced in the April 19th release note regarding the creation of 1.22 clusters has been resolved. You can now create 1.22 clusters.

## April 26, 2022

Security

Two security vulnerabilities, [CVE-2022-1055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1055) and [CVE-2022-27666](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27666) have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all GKE node operating systems (Container-Optimized OS and Ubuntu). For instructions and more details, see the [GCP-2022-014 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-014).

## April 19, 2022

Announcement

An issue has been discovered in Anthos clusters on AWS (previous generation). Do not launch Kubernetes 1.22 clusters at this time. 

The Anthos clusters on AWS (previous generation) release `1.11.0-gke.1` has been removed. We are working on a fix.

## April 12, 2022

Security

A security vulnerability, CVE-2022-23648, has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host.

For more information, see the [GCP-2022-013 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-013).

## April 07, 2022

Security

A security vulnerability, [CVE-2022-0847](https://nvd.nist.gov/vuln/detail/CVE-2022-0847), has been discovered in the Linux kernel version 5.8 and later that can potentially escalate container privileges to root. This vulnerability affects Anthos Clusters on AWS (previous generation) running Kubernetes version v1.19, v1.20 or v1.21 on Ubuntu.

For more information, see the [GCP-2022-012 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-012).

## April 05, 2022

Announcement

Anthos Clusters on AWS aws-1.11.0-gke.1 (previous generation) is now available. Clusters in this release support the following Kubernetes versions:

  * 1.22.8-gke.300
  * 1.21.11-gke.100
  * 1.20.15-gke.2200



Change

To use an Application Load Balancer (ALBs) with version 1.22 clusters, you need to upgrade your [ALB controller configuration](https://cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/how-to/loadbalancer-alb#configure_your_cluster).

Announcement

This version adds support for Kubernetes 1.22 clusters. 

Because Kubernetes 1.22 replaces some `v1beta` APIs with `v1` APIs, your workloads might need to be updated to use 1.22. For more information, see Kubernetes 1.22 [Deprecated APIs](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22).

Issue

The workload identity webhook is not supported on cluster versions 1.22 and later. Before you upgrade your clusters to version 1.22, you should modify any workloads that depend on the webhook to configure their credentials without it.

Deprecated

This version no longer supports creation or maintenance of Kubernetes 1.18 clusters.

Security

This release includes fixes for the following CVEs:

  * [CVE-2021-22600](https://nvd.nist.gov/vuln/detail/CVE-2021-22600)
  * [CVE-2022-23648](https://nvd.nist.gov/vuln/detail/CVE-2022-23648)
  * [CVE-2021-3177](https://nvd.nist.gov/vuln/detail/CVE-2021-3177)
  * [CVE-2019-15165](https://nvd.nist.gov/vuln/detail/CVE-2019-15165)
  * [CVE-2021-3521](https://nvd.nist.gov/vuln/detail/CVE-2021-3521)
  * [CVE-2021-4122](https://nvd.nist.gov/vuln/detail/CVE-2021-4122)



## February 24, 2022

Announcement

Anthos Clusters on AWS aws-1.10.2-gke.0 (previous generation) is now available. Clusters in this release support the following Kubernetes versions:

  * 1.21.9-gke.1900
  * 1.20.15-gke.1900
  * 1.19.16-gke.7700



Security

This release includes fixes for the following CVEs:

  * [CVE-2021-45960](https://nvd.nist.gov/vuln/detail/CVE-2021-45960)
  * [CVE-2022-22827](https://nvd.nist.gov/vuln/detail/CVE-2022-22827)
  * [CVE-2022-22825](https://nvd.nist.gov/vuln/detail/CVE-2022-22825)
  * [CVE-2021-46143](https://nvd.nist.gov/vuln/detail/CVE-2021-46143)
  * [CVE-2022-22826](https://nvd.nist.gov/vuln/detail/CVE-2022-22826)
  * [CVE-2022-23852](https://nvd.nist.gov/vuln/detail/CVE-2022-23852)
  * [CVE-2022-23990](https://nvd.nist.gov/vuln/detail/CVE-2022-23990)
  * [CVE-2022-22824](https://nvd.nist.gov/vuln/detail/CVE-2022-22824)
  * [CVE-2022-22822](https://nvd.nist.gov/vuln/detail/CVE-2022-22822)
  * [CVE-2022-22823](https://nvd.nist.gov/vuln/detail/CVE-2022-22823)



## February 04, 2022

Security

A security vulnerability, [CVE-2021-4034](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034), has been discovered in pkexec, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions such as rebooting the system, installing packages, restarting services etc, as governed by a policy.

Anthos clusters on AWS is unaffected. 

For instructions and more details, see the [GCP-2022-004 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-004).

## January 27, 2022

Announcement

Anthos Clusters on AWS aws-1.10.1-gke.0 (previous generation) is now available. Clusters in this release support the following Kubernetes versions:

  * 1.21.8-gke.2000
  * 1.20.14-gke.2000
  * 1.19.16-gke.5300



Security

This release includes fixes for the following CVEs:

  * [CVE-2018-20482](https://nvd.nist.gov/vuln/detail/CVE-2018-20482)
  * [CVE-2018-20673](https://nvd.nist.gov/vuln/detail/CVE-2018-20673)
  * [CVE-2019-20838](https://nvd.nist.gov/vuln/detail/CVE-2019-20838)
  * [CVE-2019-17594](https://nvd.nist.gov/vuln/detail/CVE-2019-17594)
  * [CVE-2019-17595](https://nvd.nist.gov/vuln/detail/CVE-2019-17595)
  * [CVE-2020-14155](https://nvd.nist.gov/vuln/detail/CVE-2020-14155)
  * [CVE-2021-20266](https://nvd.nist.gov/vuln/detail/CVE-2021-20266)
  * [CVE-2021-23840](https://nvd.nist.gov/vuln/detail/CVE-2021-23840)
  * [CVE-2021-23841](https://nvd.nist.gov/vuln/detail/CVE-2021-23841)
  * [CVE-2021-27645](https://nvd.nist.gov/vuln/detail/CVE-2021-27645)
  * [CVE-2021-33574](https://nvd.nist.gov/vuln/detail/CVE-2021-33574)
  * [CVE-2021-35942](https://nvd.nist.gov/vuln/detail/CVE-2021-35942)
  * [CVE-2021-42574](https://nvd.nist.gov/vuln/detail/CVE-2021-42574)
  * [CVE-2021-43618](https://nvd.nist.gov/vuln/detail/CVE-2021-43618)
  * [CVE-2022-0185 ](https://nvd.nist.gov/vuln/detail/CVE-2022-0185)



Change

The release note from December 14 has been updated to clarify which service account no longer needs the ServiceUsageViewer role. The ServiceUsageViewer role is now required for the user that runs the `anthos-gke` command-line tool.

## December 14, 2021

Announcement

Anthos Clusters on AWS aws-1.10.0-gke.5 (previous generation) is now available.

Anthos clusters on AWS aws-1.10.0-gke.5 (previous generation) clusters run the following Kubernetes versions:

  * 1.19.16-gke.1000
  * 1.20.12-gke.1000
  * 1.21.6-gke.1000



Deprecated

Kubernetes 1.18 is no longer supported. You can no longer launch Kubernetes 1.17 clusters. Your existing 1.17 clusters will continue to run.

Feature

This release supports creating instances in the `c5a`, `c5ad`, `i3en`, `m5a`, `m5ad`, `r5a`, `r5ad`, and `t3a` families.

Security

This release fixes the following security issues:

  * [CVE-2021-3733](https://nvd.nist.gov/vuln/detail/CVE-2021-3733)
  * [CVE-2021-3737](https://nvd.nist.gov/vuln/detail/CVE-2021-3737)
  * [CVE-2021-3711](https://nvd.nist.gov/vuln/detail/CVE-2021-3711)



Fixed

This release fixes an earlier issue with 1.21 clusters that use both OIDC and an HTTP proxy.

Issue

To install Anthos Service Mesh, follow the steps in [Connecting to your cluster](https://cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/how-to/connecting-to-a-cluster) before starting your Anthos Service Mesh installation.

Change

Updated: The management service account no longer needs the ServiceUsageViewer role to install Anthos clusters on AWS. For more information, see [Prerequisites](https://cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/how-to/prerequisites#permissions_for_anthos-gke_command-line_tool).

## December 02, 2021

Issue

If your cluster uses both a proxy and OIDC authentication, do not upgrade to version 1.21.4 or 1.21.5. If you encounter an issue during an upgrade, contact support for assistance.

## October 29, 2021

Announcement

Anthos Clusters on AWS aws-1.9.1-gke.0 is now available.

Anthos clusters on AWS aws-1.9.1-gke.0 clusters run the following Kubernetes versions:

  * 1.18.20-gke.8300
  * 1.19.15-gke.1600
  * 1.20.11-gke.1600
  * 1.21.5-gke.1600



Fixed

Release aws-1.9.1-gke.0 fixes an issue in release 1.9.0 in which authorization with AWS IAM assumed roles failed.

Fixed

Release aws-1.9.1-gke.0 of Anthos Clusters on AWS fixes the following security issues:

  * [CVE-2021-38160](https://nvd.nist.gov/vuln/detail/CVE-2021-38160)
  * [CVE-2021-3612](https://nvd.nist.gov/vuln/detail/CVE-2021-3612)
  * [CVE-2021-37576](https://nvd.nist.gov/vuln/detail/CVE-2021-37576)
  * [CVE-2018-5729](https://nvd.nist.gov/vuln/detail/CVE-2018-5729)
  * [CVE-2018-5730](https://nvd.nist.gov/vuln/detail/CVE-2018-5730)
  * [CVE-2020-16119](https://nvd.nist.gov/vuln/detail/CVE-2020-16119)
  * [CVE-2021-20305](https://nvd.nist.gov/vuln/detail/CVE-2021-20305)
  * [CVE-2021-22543](https://nvd.nist.gov/vuln/detail/CVE-2021-22543)
  * [CVE-2021-33624](https://nvd.nist.gov/vuln/detail/CVE-2021-33624)
  * [CVE-2021-33910](https://nvd.nist.gov/vuln/detail/CVE-2021-33910)
  * [CVE-2021-3580](https://nvd.nist.gov/vuln/detail/CVE-2021-3580)
  * [CVE-2021-3653](https://nvd.nist.gov/vuln/detail/CVE-2021-3653)
  * [CVE-2021-3712](https://nvd.nist.gov/vuln/detail/CVE-2021-3712)
  * [CVE-2021-37159](https://nvd.nist.gov/vuln/detail/CVE-2021-37159)
  * [CVE-2021-37750](https://nvd.nist.gov/vuln/detail/CVE-2021-37750)
  * [CVE-2021-40490](https://nvd.nist.gov/vuln/detail/CVE-2021-40490)
  * [CVE-2021-42008](https://nvd.nist.gov/vuln/detail/CVE-2021-42008)



For more information, click on the CVE or search for details at https://nvd.nist.gov.

## October 25, 2021

Security

A security issue was discovered in the Kubernetes ingress-nginx controller, [CVE-2021-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25742). Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces. For more information, see the [GCP-2021-024 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-024).

Security

The security community recently disclosed a new security vulnerability [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465) found in `runc` that has the potential to allow full access to a node filesystem.

For more information, see the [GCP-2021-011 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-011).

## September 30, 2021

Change

Anthos Clusters on AWS aws-1.9.0-gke.2 is now available.

Anthos clusters on AWS aws-1.9.0-gke.2 clusters run the following Kubernetes versions:

  * 1.18.20-gke.6300
  * 1.19.14-gke.2200
  * 1.20.10-gke.2000
  * 1.21.4-gke.2100



Feature

[Anthos Identity Service](https://cloud.google.com/anthos/identity/) is available on Kubernetes clusters version 1.21 and above.

Feature

Kubernetes 1.21 clusters now support the Kubernetes Konnectivity tool for communication between nodes and the control plane. When you launch a 1.21 cluster, you must allow connections between control plane nodes and node pool nodes on port 8132.

Deprecated

The VolumeSnapshot resource API version `v1beta1` is deprecated in Kubernetes 1.21 clusters. Use API version `v1` for 1.21 clusters and above. All previously persisted VolumeSnapshot objects remain functional.

Security

A security vulnerability, [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561), has been discovered in Kubernetes where certain webhooks can be made to redirect `kube-apiserver` requests to private networks of that API server. For more information, see the [GCP-2021-021 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-021).

Feature

You can now specify a Cloud Storage Bucket name where Anthos clusters on AWS stores configuration data.

Feature

You can now launch node pools with AWS R5 instances.

Feature

You can now launch Kubernetes 1.21 clusters.

Feature

You can now update the OIDC configuration on a running cluster.

Deprecated

You cannot create new 1.16 clusters. Existing 1.16 clusters continue to function.

Change

Error messages when upgrading or downgrading your clusters have been clarified.

## September 15, 2021

Security

A security issue was discovered in Kubernetes, CVE-2021-25741, where a user may be able to create a container with subpath volume mounts to access files & directories outside of the volume, including on the host filesystem. For more information, see the [GCP-2021-018 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2021-018).

## September 01, 2021

Announcement

Anthos clusters on AWS aws-1.8.2-gke.2 is now available.

Anthos clusters on AWS aws-1.8.2-gke.2 clusters run the following Kubernetes versions:

  * 1.17.17-gke.15800
  * 1.18.20-gke.4800
  * 1.19.14-gke.600
  * 1.20.10-gke.600



Security

The supported versions also offer the latest patches and updates for security vulnerabilities, exposures, and issues impacting Anthos clusters on AWS 1.8.

## July 29, 2021

Announcement

Anthos clusters on AWS aws-1.8.1-gke.1 is now available.

Anthos clusters on AWS aws-1.8.1-gke.1 clusters run the following Kubernetes versions:

  * 1.17.17-gke.13600
  * 1.18.20-gke.2600
  * 1.19.13-gke.300
  * 1.20.9-gke.300



Security

This release contains fixes for the following security vulnerabilities:

  * [CVE-2021-33560](https://nvd.nist.gov/vuln/detail/CVE-2021-33560)
  * [CVE-2021-20232](https://nvd.nist.gov/vuln/detail/CVE-2021-20232)
  * [CVE-2021-20231](https://nvd.nist.gov/vuln/detail/CVE-2021-20231)
  * [CVE-2020-24659](https://nvd.nist.gov/vuln/detail/CVE-2020-24659)
  * [CVE-2021-20305](https://nvd.nist.gov/vuln/detail/CVE-2021-20305)
  * [CVE-2021-3580](https://nvd.nist.gov/vuln/detail/CVE-2021-3580)
  * [CVE-2021-3520](https://nvd.nist.gov/vuln/detail/CVE-2021-3520)
  * [CVE-2021-20271](https://nvd.nist.gov/vuln/detail/CVE-2021-20271)



Change

Anthos clusters on AWS now requires `kubectl` version 1.17 or higher and `terraform` version v0.14.3 or higher.

## July 07, 2021

Announcement

Anthos clusters on AWS aws-1.8.0-gke.8 is now available.

Anthos clusters on AWS aws-1.8.0-gke.8 clusters run the following Kubernetes versions:

  * 1.17.17-gke.11000
  * 1.18.19-gke.2300
  * 1.19.11-gke.2300
  * 1.20.7-gke.2400



Fixed

This release fixes an issue mentioned in the entry on July 2, 2021. We recommend all customers upgrade to 1.8.0-gke.8.

Change

When you upgrade or update a user cluster, the [Connect agent](https://cloud.google.com/anthos/multicluster-management/connect/overview#agent) is automatically updated to the latest version.

## July 02, 2021

Issue

An issue has been discovered with Anthos clusters on AWS 1.8.0. When you complete an upgrade to your management service to 1.8.0, the management service automatically performs a rolling update of all node pools.

A fix for this issue is being developed. A new build will be published when the fix is available.

## July 01, 2021

Change

Anthos clusters on AWS aws-1.8.0-gke.7 is now available.

Anthos clusters on AWS aws-1.8.0-gke.7 clusters run the following Kubernetes versions:

  * 1.17.17-gke.11000
  * 1.18.19-gke.2300
  * 1.19.11-gke.2300
  * 1.20.7-gke.2400



Feature

You can now launch Kubernetes 1.20 clusters.

Change

Anthos clusters on AWS now supports Cloud Logging and Cloud Monitoring of user cluster control planes. For more information, see [Configuring logging and monitoring](https://cloud.google.com/anthos/clusters/docs/aws/how-to/logging-and-monitoring#and_on_control_plane_nodes).

Feature

You can now modify proxy settings on a running cluster. For more information, see [Changing Cluster Proxy Settings](https://cloud.google.com/anthos/clusters/docs/aws/how-to/changing-proxy-settings)

Feature

You can now update the security groups associated with user clusters and node pools. For more information, see [Updating a user cluster](https://cloud.google.com/anthos/clusters/docs/aws/how-to/update-cluster)

Feature

[Workload identity](https://cloud.google.com/anthos/clusters/docs/aws/how-to/workload-identity-gcp) to authenticate to Google Cloud services from your user clusters is now available. Using workload identity is supported on user clusters running version 1.20 and higher.

## June 03, 2021

Change

Anthos clusters on AWS 1.7.2-gke.0 is now available.

Anthos clusters on AWS 1.7.2-gke.0 clusters run the following Kubernetes versions:

  * 1.16.15-gke.18500
  * 1.17.17-gke.8200
  * 1.18.18-gke.1500
  * 1.19.10-gke.1500



Security

The Anthos clusters on AWS 1.7.2-gke.0 release addresses the following vulnerabilities:

  * [CVE-2020-29361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29361)
  * [CVE-2020-1971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1971)
  * [CVE-2020-29362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29362)
  * [CVE-2020-29362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29362)
  * [CVE-2021-23841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23841)
  * [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735)



## April 30, 2021

Change

Anthos clusters on AWS 1.7.1-gke.1 is now available.

Anthos clusters on AWS 1.7.1-gke.1 clusters run the following Kubernetes versions:

  * 1.16.15-gke.17300
  * 1.17.17-gke.7000
  * 1.18.18-gke.300
  * 1.19.9-gke.900



Security

The Anthos clusters on AWS 1.7.1-gke.1 patch release addresses the following security vulnerabilities:

  * [CVE-2020-29361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29361)
  * [CVE-2020-29362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29362)
  * [CVE-2021-24031](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-24031)
  * [CVE-2021-23336](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23336)
  * [CVE-2021-3449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3449)
  * [CVE-2021-3450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3450)
  * [CVE-2020-1971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1971)
  * [CVE-2021-23841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23841)
  * [CVE-2021-23840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23840)



## April 20, 2021

Security

The Kubernetes project recently [announced](https://groups.google.com/forum/#!topic/kubernetes-security-announce/FKAGqT4jx9Y) a new security vulnerability, [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735), that could allow node updates to bypass a Validating Admission Webhook. For more details, see the [GCP-2021-003 security bulletin](https://cloud.google.com/anthos/clusters/docs/aws/security-bulletins#gcp-2021-003).

## April 06, 2021

Change

Anthos clusters on AWS 1.7.0-gke.12 is now available.

Anthos clusters on AWS 1.7.0-gke.12 clusters run the following Kubernetes versions:

  * 1.16.15-gke.8100
  * 1.17.13-gke.2800
  * 1.18.12-gke.1800
  * 1.19.8-gke.1000



To upgrade your clusters, perform the following steps:

  * [Upgrade your Management](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#mgmt) service to 1.7.0-gke.12.
  * [Upgrade your user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#user-clusters) to a supported Kubernetes version.



Fixed

This release fixes an issue mentioned in the entry on April 2, 2021. We recommend all customers running 1.7.0-gke.11 upgrade to 1.7.0-gke.12.

## April 02, 2021

Issue

An issue has been discovered with Anthos clusters on AWS 1.7.0.

If you use a [HTTP proxy](https://cloud.google.com/anthos/clusters/docs/aws/how-to/using-a-proxy), do not upgrade to 1.7.0.

If you do not use a HTTP proxy, you can upgrade to 1.7.0.

A fix for this issue is being developed.

## March 31, 2021

Announcement

Anthos clusters on AWS 1.7.0-gke.11 is now available.

**This note is updated. For more information, see entry on April 2, 2021.**

Anthos clusters on AWS 1.7.0-gke.11 clusters run the following Kubernetes versions:

  * 1.16.15-gke.8100
  * 1.17.13-gke.2800
  * 1.18.12-gke.1800
  * 1.19.8-gke.1000



To upgrade your clusters, perform the following steps:

  * [Upgrade your Management](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#mgmt) service to 1.7.0-gke.11.
  * [Upgrade your user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#user-clusters) to a supported Kubernetes version.



Feature

Anthos clusters on AWS now supports Kubernetes 1.19.

Feature

Anthos clusters on AWS now supports exporting logs and metrics from an Anthos clusters on AWS user cluster to Cloud Logging and Cloud Monitoring.

For more information, see [Configuring logging and monitoring for Anthos clusters on AWS](https://cloud.google.com/anthos/clusters/docs/aws/how-to/logging-and-monitoring)

Feature

Anthos clusters on AWS now supports CMK encryption for component volumes. For more information, see [Using CMK to encrypt volumes](https://cloud.google.com/anthos/clusters/docs/aws/how-to/using-cmk).

Feature

[Workload identity](https://cloud.google.com/anthos/clusters/docs/aws/how-to/workload-identity-cluster) in user clusters is now generally available.

Feature

Anthos clusters on AWS now supports `gp3` EBS volume types. You can configure `gp3` volumes on your [management service](https://cloud.google.com/anthos/clusters/docs/aws/reference/awsmanagementservice), [AWSCluster](https://cloud.google.com/anthos/clusters/docs/aws/reference/awscluster), and [AWSNodePools](https://cloud.google.com/anthos/clusters/docs/aws/reference/awsnodepools).

## February 25, 2021

Announcement

Anthos clusters on AWS 1.6.2-gke.0 is now available.

Anthos clusters on AWS 1.6.2-gke.0 clusters run the following Kubernetes versions:

  * 1.16.15-gke.5302
  * 1.17.9-gke.6402
  * 1.18.10-gke.902



To upgrade your clusters, perform the following steps:

  * [Upgrade your Management](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#mgmt) service to 1.6.2-gke.0.
  * [Upgrade your user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#user-clusters) to a supported Kubernetes version.



Fixed

This release fixes an issue where the management service fails to start when provided with a KMS alias.

Fixed

Bug fixes and security improvements.

## February 03, 2021

Change

GKE on AWS 1.6.1-gke.2 is now available.

GKE on AWS 1.6.1-gke.2 clusters run the following Kubernetes versions:

  * 1.16.15-gke.5301
  * 1.17.9-gke.6401
  * 1.18.10-gke.901



To upgrade your clusters, perform the following steps:

  * [Upgrade your Management](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#mgmt) service to 1.6.1-gke.2.
  * [Upgrade your user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster) to a supported Kubernetes version.



Feature

[Snapshots](https://cloud.google.com/anthos/gke/docs/aws/troubleshooting#snapshots) now collect AWS EFS logs from user cluster nodes.

Fixed

Bug fixes and performance improvements.

## December 17, 2020

Announcement

GKE on AWS 1.6.0-gke.3 is now available.

GKE on AWS 1.6.0-gke.3 clusters run the following Kubernetes versions:

  * 1.16.15-gke.5300
  * 1.17.9-gke.6400
  * 1.18.10-gke.900



To upgrade your clusters, perform the following steps:

  1. [Upgrade your Management service](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading) to 1.6.0-gke.1.
  2. [Upgrade your user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading#user-clusters) to a supported Kubernetes version.



Feature

GKE on AWS now supports Kubernetes 1.18. 

The Kubernetes 1.18 version includes CoreDNS 1.7.1 and Cluster Autoscaler 1.18.

Feature

GKE on AWS now supports [mounting AWS Elastic File System file systems](https://cloud.google.com/anthos/gke/docs/aws/how-to/using-efs) without having to install a driver.

Security

Cluster state synchronizations between the management service and S3 now use HTTPS.

Change

You can now use custom DNS hostnames in your VPC by setting [`enableDnsHostnames` to `false`](https://cloud.google.com/anthos/gke/docs/aws/troubleshooting#tls_errors_when_connecting_to_your_cluster)

Change

You can now specify an AWS KMS alias in your [`anthos-gke.yaml`](https://cloud.google.com/anthos/gke/docs/aws/how-to/installing-management#configure) instead of a KMS ARN.

## November 02, 2020

Change

Anthos GKE on AWS 1.5.1-gke.1 is now available and clusters run on 1.16.15-gke.701 and v1.17.9-gke.2801. To upgrade your clusters, perform the following steps:

Upgrade your [Management service](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-management) to 1.5.1-gke.1. Upgrade your [user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster) to 1.16.15-gke.701 or v1.17.9-gke.2801

Feature

You can now use [Private Google Access](https://cloud.google.com/vpc/docs/private-access-options#pga) to provision images for your GKE on AWS environment. For more information, see [`spec.ubuntuRepositoryMirror`](https://cloud.google.com/anthos/gke/docs/aws/reference/awsmanagementservice#specubunturepositorymirror) in the AWSManagementService resource.

Change

Bug fixes and performance improvements.

## October 12, 2020

Feature

GKE on AWS 1.5.0 supports [volume snapshots](https://cloud.google.com/anthos/gke/docs/aws/concepts/storage#using_volume_snapshots).

## October 02, 2020

Change

Anthos GKE on-AWS 1.5.0-gke.6 is now available and clusters run on 1.16.15-gke.700 and v1.17.9-gke.2800. To upgrade your clusters, perform the following steps:

  1. [Upgrade your Management service](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-management) to 1.5.0-gke.6.
  2. [Upgrade your user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster) to 1.16.15-gke.700 or v1.17.9-gke.2800



Feature

Workload identity (preview) lets you bind Kubernetes service accounts to AWS IAM accounts with specific permissions. Workload identity blocks unwanted access to cloud resources with AWS IAM permissions. With workload identity, you can assign different IAM roles to each workload. Fine grained permissions control allows you to follow the principle of least privilege. For more details, see [Creating a user cluster with workload identity](https://cloud.google.com/anthos/gke/docs/aws/how-to/workload-identity-cluster#applying_credentials_without_the_webhook)

Feature

You can now route traffic from the GKE on AWS management service and Connect through an HTTP/HTTPS proxy. For more details, see [Using a proxy with GKE on AWS](https://cloud.google.com/anthos/gke/docs/aws/how-to/using-a-proxy)

Feature

Improved installation experience

  * This version enables installation and upgrade by using any Google Cloud–authenticated service account. You no longer need to be on the allowlist to access GKE on AWS components..

  * Additional preflight checks enforce enablement of required Google Cloud APIs. See [Google Cloud requirements](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites#gcp_requirements) for more information.




Fixed

When creating multiple multiple management clusters, users may have seen name collisions with S3 bucket. Now, you can specify a [custom name](https://cloud.google.com/anthos/gke/docs/aws/reference/awsmanagementservice) for your S3 bucket to avoid naming conflicts.

## September 17, 2020

Change

GKE on AWS 1.4.3-gke.7 is now available. GKE on AWS 1.4.3-gke.7 clusters run on Kubernetes 1.16.13-gke.1402. 

To Upgrade:

  1. Upgrade your [Management service](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-management) to 1.4.3-gke.7.
  2. Upgrade your [user clusters](https://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster) to to 1.16.13-gke.1402.



Fixed

A vulnerability, described in [CVE-2020-14386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14386), was recently discovered in the Linux kernel. The vulnerability may allow container escape to obtain root privileges on the host node.

All GKE on AWS nodes are affected.

To fix this vulnerability, upgrade your management service and user clusters to this patched version. The following GKE on AWS version contains the fix for this vulnerability:

  * GKE on AWS 1.4.3



For more information, see the [Security Bulletin](https://cloud.google.com/anthos/gke/docs/aws/security-bulletins#gcp-2020-012)

## August 27, 2020

Change

GKE on AWS 1.4.2-gke.1 is released. This release includes Kubernetes version 1.16.13-gke.1401.

Fixed

This release includes bug fixes and security improvements. We recommend you update your clusters to this version.

To upgrade your clusters, perform the following steps:

  1. Upgrade your [management service](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-management) to aws-1.4.2-gke.1.
  2. Upgrade your [user cluster's](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster) AWSCluster and AWSNodePools to 1.16.13-gke.1401.



Fixed

  * Fixed Perl version to fix security vulnerability [CVE-2020-10878](https://nvd.nist.gov/vuln/detail/CVE-2020-10878)
  * Removed a dependency on Musl to fix security vulnerability [CVE-2019-14697](https://nvd.nist.gov/vuln/detail/CVE-2019-14697)



## August 04, 2020

Fixed

Anthos GKE on AWS 1.4.1-gke.17 is released. This release fixes a memory leak that causes clusters to become unresponsive.

To upgrade your clusters, perform the following steps:

  1. Restart your [control plane instances](https://cloud.google.com/anthos/gke/docs/aws/troubleshooting#rebooting_your_control_plane).
  2. Upgrade your [management service](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-management) to aws-1.4.1-gke.17.
  3. Upgrade your [user cluster's](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster) AWSCluster and AWSNodePools to 1.16.9-gke.15.



Change

Use version 1.16.9-gke.15 for creating new clusters.

## August 03, 2020

Issue

Anthos GKE on AWS 1.4.1-gke.15 clusters will experience a memory leak that results in an unresponsive cluster. A fix for this issue is in development.

If you are planning to deploy an Anthos GKE on AWS cluster, wait until the fix is ready.

## July 24, 2020

Change

Anthos GKE on AWS is now generally available.

Change

Clusters support in-place upgrades, with the ability to upgrade the control plane and node pools separately.

Change

With Anthos Config Management enterprises can set policies on their AWS workloads and with Anthos Service Mesh, they can monitor, manage, and secure them.

Change

Anthos can be deployed within existing AWS VPCs, leveraging existing security groups to secure those clusters. Customers can ingress traffic using NLB and ALBs. Additionally Anthos on AWS supports AWS IAM and OIDC. This makes deploying Anthos easy, eliminates the need to provision new accounts, and minimizes configuration of the environment.

Change

Clusters have been validated to support up to 200 nodes and 6000 pods.

Change

Allows the number of nodes to be scaled dynamically based on traffic volume to increase utilization and reduce cost, and improve performance

Change

Clusters can be deployed in a high availability (HA) configuration, where control plane instances and node pools are spread across multiple availability zones.

Change

Kubernetes settings (flags and sysctl settings) have been updated to match GKE.

Breaking

Upgrades from beta versions are not supported. To install Anthos GKE on AWS, you must remove your user and management clusters, then reinstall them.

## May 29, 2020

Change

A new build of Anthos GKE on AWS has been released. This build removes the need to check AWS IAM privileges when creating a management cluster. **You don't need to update** if you have not encountered this issue.

To install this build, download the `anthos-gke` tool by running the following command:

`gsutil cp gs://gke-multi-cloud-release/bin/aws-0.2.1-gke.8/anthos-gke .`

Then, recreate your [Terraform configuration](https://cloud.google.com/anthos/gke/docs/aws/how-to/installing-management) and continue with your installation.

## May 07, 2020

Breaking

To upgrade your Anthos GKE on AWS clusters, you need to [uninstall](https://cloud.google.com/anthos/gke/docs/aws/how-to/uninstalling) all your management and user clusters. You also need to download the new version of the [`anthos-gke`](https://cloud.google.com/anthos/gke/docs/aws/downloads#anthos-gke_cli_tool) cli tool.

Change

Anthos GKE on AWS now supports [auto-scaling](https://cloud.google.com/anthos/gke/docs/aws/how-to/scaling-user-cluster). You can enable auto-scaling by changing settings in your AWSNodePools, or scale your clusters manually by adding new AWSNodePools.

Change

Built-in EBS StorageClass names have been changed to `standard-rwo` and `premium-rwo`. If you declare the [`singlewriter-standard` or `singlewriter-premium`](https://cloud.google.com/anthos/gke/docs/aws/concepts/storage.md) StorageClasses with your workloads, you must update your workloads when upgrading.

Change

Anthos GKE on AWS now support for Application-layer secrets encryption with AWS KMS by passing a KMS key ARN to your [AWSCluster](https://cloud.google.com/anthos/gke/docs/aws/reference/awscluster#speccontrolplane).

## April 02, 2020

Feature

Initial beta release of Anthos GKE on AWS

Change

The release improves upon earlier releases with:

  * **Improved reliability** : User clusters are now deployed in a high availability (HA) fashion, where both control plane instances as well as node pools can be placed across multiple availability zones. AWS Auto Scaling groups are also now used for resiliency.

  * **Improved security** : Control plane instances for different user clusters are now isolated in separate security groups. Instance Metadata Service Version 2 (IMDSv2) is enabled to protect against SSRF attacks, and sensitive fields in EC2 metadata are now encrypted.

  * **Easier to deploy** : The installation process for the management layer has been simplified and performs additional validation checks. It uses Terraform modules for flexible integration into different AWS environments, and customers can now leverage existing security groups and IAM resources to secure clusters. Documentation has been improved and expanded.

  * **Future-proof storage stack** : We're now using the [EBS CSI driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) to manage all AWS EBS volumes. The legacy, in-tree Kubernetes EBS driver has been removed entirely, and all upcoming storage features, such as snapshots, will be provided using CSI.

  * **Updated Kubernetes version** : User clusters are now based on Kubernetes 1.15 and have passed open-source Kubernetes conformance tests.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
