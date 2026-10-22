---
url: https://docs.cloud.google.com/network-security-integration/docs/release-notes/
title: Network Security Integration release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:16.909248+00:00
---

# Network Security Integration release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Resources ](https://docs.cloud.google.com/network-security-integration/docs/resources)



Send feedback 

#  Network Security Integration release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Network Security Integration. 

Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/network-security-integration-release-notes.xml) directly. 

## August 20, 2026

Feature

Network Security Integration in-band integration now supports the direct internet egress deployment model. In this model, the network security appliance in the producer VPC network inspects outbound traffic and sends it directly to the internet through its external network interface. The appliance then sends the internet response packet directly to the consumer VM using GENEVE, bypassing the return hop to the consumer VPC network.

For more information, see [Direct internet egress](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview#direct-internet-egress).

## June 30, 2026

Feature

The broker mode for out-of-band Network Security Integration (also known as packet broker) is now available in **General Availability (GA) with allowlist**. Broker mode lets you mirror GENEVE-encapsulated network packets from a consumer network to multiple producer networks for analysis, and adds additional GENEVE metadata (such as timestamp and network stable ID). This feature is not available to all users. To access this feature, contact your Google account team.

For more information, see [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#oob-modes) and [Understand GENEVE format](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve).

Feature

Project-level security profiles and security profile groups for Network Security Integration are now available in **General Availability (GA)**.

For more information, see [Security profiles overview](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview) and [Security profile groups overview](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview).

## May 04, 2026

Feature

You can now enable zonal affinity for your Network Security Integration in-band integration deployments and configure zonal interception with regional backends. For more information, see [Zonal affinity](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview#zonal-affinity).

## January 14, 2026

Feature

You can now integrate your network security appliances directly in the network traffic path for inspection and identify any threats before the traffic reaches its destination. For more information, see [In-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview). This feature is available in **General Availability**.

## June 05, 2025

Change

Network Security integration now retains 396 bytes for the GENEVE encapsulation overhead. Consumer networks must use the maximum transmission unit (MTU) size of 8500 bytes or less. Producer networks must use an MTU at least 396 bytes more than the consumer network. For more information, see [GENEVE encapsulation and MTU requirements](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve#geneve-mtu).

## March 11, 2025

Feature

[Network Security Integration](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview), including the Out-of-band integration, is available in **General Availability**.

Use out-of-band integration service to analyze your workloads' network traffic at scale. For more information, see [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview).

## October 30, 2024

Feature

You can use Packet Mirroring, an "out-of-band" Network Security Integration, to analyze your workloads' network traffic at scale. This feature is available in Preview. For more information, see [Network Security Integration overview](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview).

Announcement

For Preview, Network Security Integration resources are available free of charge. For other Google Cloud resources, see the product-specific pricing documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
