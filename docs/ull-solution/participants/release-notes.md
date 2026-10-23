---
url: https://docs.cloud.google.com/ull-solution/participants/release-notes/
title: ULL Solution release notes \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:17.732057+00:00
---

# ULL Solution release notes  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)
  * [ Resources ](https://docs.cloud.google.com/ull-solution/participants/release-notes)



Send feedback 

#  ULL Solution release notes Stay organized with collections  Save and categorize content based on your preferences. 

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page documents production updates to Ultra Low Latency (ULL) Solution. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 14, 2026

Feature

U4S instances support [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput) (`hyperdisk-throughput`) block storage. For more information, see [Supported disk types for U4S instances](https://docs.cloud.google.com/ull-solution/participants/u4-machines#u4s-disks).

## October 08, 2026

Feature

You can filter mirrored traffic by the primary IP address ranges of the capture point. For more information, see [Create a ULL Packet Mirroring collector filter rule](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull#create-ull-pm-collector-filter-rule).

## October 05, 2026

Feature

Information about ULL unicast packet loss is available in Flow Analyzer. For more information, see [Analyze traffic flows with Flow Analyzer](https://docs.cloud.google.com/ull-solution/participants/view-flow-logs#analyze-flows).

## September 30, 2026

Feature

**Preview** : Ultra Low Latency (ULL) Packet Mirroring is available for exchange participants. You can clone traffic from your ULL VPC networks and forward it to collector instances for analysis without affecting latency or performance. For more information, see [Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull).

## August 12, 2026

Announcement

**General Availability with allowlist** : Ultra Low Latency (ULL) Solution

[ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) with allowlist in private zones `us-south1-d` and `us-south1-e` for approved exchange participants.

For more information about the services included in ULL Solution, see the following:

Feature

**ULL VPC networks** : ULL Virtual Private Cloud (VPC) networks provide support for ultra-low latency unicast and multicast traffic for market trading applications, respecting strict latency, jitter, and multicast variance targets. Connectivity between exchange operators and participants is managed through Network Connectivity Center (NCC), which uses a hub and spoke model. For more information, see [About participant ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/participant-ull-network-profile).

Feature

**Firewall for ULL VPC networks** : Firewall rules in regional network firewall policies are supported for ULL VPC networks through the `ULL_POLICY` firewall policy type. For more information, see [Firewall for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/firewall/overview).

Feature

**Compute Engine U4 machine family** : U4 is Google Cloud's ULL network-optimized machine family designed to support the core workloads of financial exchange ecosystems. U4C bare metal instances run on 5th generation (Emerald Rapids) Intel Xeon processors and provide ULL connectivity for exchange participants. U4S virtual machine (VM) instances run on 6th generation (Granite Rapids) Intel Xeon processors and provide support for adjacent workloads. For more information, see [U4 Ultra Low Latency (ULL) machine family](https://docs.cloud.google.com/ull-solution/participants/u4-machines).

Google Cloud provides public Red Hat Enterprise Linux (RHEL) and Rocky Linux operating system (OS) images for use with U4 instances. These images support the required functionality for ULL Solution. For more information, see [Operating system support for U4 machine types](https://docs.cloud.google.com/ull-solution/participants/u4-machines#u4-os-images).

Feature

**Guest networking and Onload** : You can use Onload, a high-performance user-space network stack, to optimize the performance of trading applications that run on U4 instances. Using Onload with ULL Solution includes flow steering support for unicast and multicast traffic. For procedures for using Onload on the supported public OS images, including setup, busy polling configuration, and performance optimization, see [Work with Onload](https://docs.cloud.google.com/ull-solution/participants/use-onload).

Feature

**Time synchronization** : The Firefly protocol provides nanosecond-level time synchronization for U4 instances, including both U4C bare metal instances and U4S VM instances. You can configure accurate time for an instance by synchronizing the system clock of the instance to the physical NIC clock of its host server. Additionally, you can monitor the accuracy of this time synchronization through Cloud Monitoring. For more information, see [Configure accurate time for U4 Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/configure-time-sync).

Feature

**ULL Multicast** : ULL Multicast provides a hardware-based multicast service for applications with strict latency and multicast variance requirements. It relies on infrastructure directly in the physical network fabric to replicate and distribute traffic. After ULL Multicast is configured, U4C instance network interfaces attached to ULL VPC networks can join and leave multicast groups by using IGMPv2. For more information, see the [ULL Multicast overview](https://docs.cloud.google.com/ull-solution/participants/multicast-overview).

Feature

**Observability** : ULL Solution includes the following observability features:

  * **VPC Flow Logs** : Provides visibility into bandwidth, network latency, network packet loss, and instance packet loss. For more information, see [VPC Flow Logs records for ULL traffic](https://docs.cloud.google.com/ull-solution/participants/view-flow-logs#ull-records).
  * **Flow Analyzer** : All of the information in VPC Flow Logs records for ULL traffic is available in Flow Analyzer, except for ULL unicast packet loss. For more information, see [Analyze traffic flows with Flow Analyzer](https://docs.cloud.google.com/ull-solution/participants/view-flow-logs#analyze-flows).
  * **Group membership event logs** : You can monitor multicast group membership events, such as IGMP join and leave requests. For more information, see [View group membership event logs for ULL Multicast](https://docs.cloud.google.com/ull-solution/participants/view-membership-logs).



Feature

**Dual-zone design and maintenance schedule** : ULL Solution uses a dual-zone design to help ensure that regular maintenance and testing can be performed without interrupting market trading. The _production zone_ is the active environment for live trading. The _maintenance zone_ is the inactive environment for updates, repairs, and testing. Information about the maintenance schedule is available through the Google Cloud API. For more information, see [Maintenance in ULL Solution private zones](https://docs.cloud.google.com/ull-solution/participants/zone-maintenance).

Feature

**Cloud Multicast in ULL Solution private zones** : Cloud Multicast is supported for use in ULL Solution private zones, including with U4S instances and the `nic0` (non-ULL) interface of U4C instances. Cloud Multicast is a multicast service based on software-defined networking that uses multicast infrastructure in a tenant project and network managed by Google to replicate and distribute traffic. For more information, see [Comparison of ULL Multicast and Cloud Multicast](https://docs.cloud.google.com/ull-solution/participants/multicast-overview#comparison) and the [Cloud Multicast](https://docs.cloud.google.com/vpc/docs/multicast/overview) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
