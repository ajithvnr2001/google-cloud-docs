---
url: https://docs.cloud.google.com/firewall/docs/release-notes/
title: Cloud NGFW release notes \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:47:48.875675+00:00
---

# Cloud NGFW release notes  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Resources ](https://docs.cloud.google.com/firewall/docs/resources)



Send feedback 

#  Cloud NGFW release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Cloud Next Generation Firewall (Cloud NGFW).

To view Cloud NGFW announcements prior to April 2023, see the [Virtual Private Cloud (VPC) release notes](https://docs.cloud.google.com/vpc/docs/release-notes). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloud-firewall-release-notes.xml) directly. 

## September 22, 2026

v1

Feature

You can now use Cloud NGFW Enterprise advanced threat prevention with cross-region internal Application Load Balancers ([Preview](https://cloud.google.com/products#product-launch-stages)).

You can configure global network firewall policies with security profile groups to inspect incoming traffic targeting load balancer forwarding rules. This integration supports intrusion detection and prevention service and Advanced malware sandbox (WildFire) to protect workloads and backends.

For more information, see [Supported load balancers](https://docs.cloud.google.com/firewall/docs/about-firewalls#ngfw-load-balancers). This feature is available in **Preview**.

## August 17, 2026

v1

Feature

Support for the Advanced malware sandbox (WildFire) service is now restored. You can now use Advanced malware sandbox to perform deep inspection of network-routed file transfers and block zero-day malware before it reaches your workloads. Advanced malware sandbox is available in the Cloud Next Generation Firewall Enterprise tier.

For more information, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire) and [Configure Advanced malware sandbox in your network](https://docs.cloud.google.com/firewall/docs/configure-wildfire). This feature is available in **Preview**.

## July 30, 2026

v1

Announcement

The limits for the following Cloud NGFW resources have been updated:

  * Security profile groups with threat prevention per project: 35
  * Security profile groups with URL filtering per project: 35
  * Firewall endpoint associations per organization-level firewall endpoint: 50
  * Firewall endpoint associations per project-level firewall endpoint: 50



For more information, see [Quotas and limits](https://docs.cloud.google.com/firewall/docs/quotas).

## July 27, 2026

v1

Breaking

Enabling Advanced malware sandbox (WildFire) in an existing firewall endpoint can cause a temporary data plane outage. As a result, the Advanced malware sandbox feature is temporarily removed.

## July 20, 2026

v1

Feature

You can now use the Advanced malware sandbox (WildFire) service to protect your network against unknown, novel malware, and file-based threats. Advanced malware sandbox integrates dynamic machine learning (ML) and cloud-based behavioral sandboxing to perform deep inspection of network-routed file transfers and block zero-day malware before it reaches your workloads. Advanced malware sandbox is available in the Cloud Firewall Enterprise tier.

For more information, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire) and [Configure Advanced malware sandbox in your network](https://docs.cloud.google.com/firewall/docs/configure-wildfire). This feature is available in **Preview**.

## June 30, 2026

v1

Feature

You can now create and configure project-level resources for application layer inspection in Cloud NGFW, including project-level firewall endpoints, security profile groups, and security profiles. For more information, see [Organization-level and project-level resources](https://docs.cloud.google.com/firewall/docs/about-app-layer-inspection#org-project-resources), [Firewall endpoints overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints), [Security profile groups overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups), and [Security profiles overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles). This feature is available in **General Availability**.

v1

Feature

To restrict traffic to the managed Envoy proxies in a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets), you can configure global network firewall policies and regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers. For more information, see [Use global network firewall policies to protect Envoy-based load balancers](https://docs.cloud.google.com/firewall/docs/global-network-app-lb) and [Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers](https://docs.cloud.google.com/firewall/docs/regional-network-app-lb). This feature is available in **General Availability**.

## May 15, 2026

v1

Issue

Due to a known issue, the limit of firewall endpoint associations per organization-level firewall endpoint is restricted to 15. To track the planned increase of the limit to 50 or to request a limit increase, contact [Support](https://docs.cloud.google.com/firewall/docs/getting-support).

## May 04, 2026

v1

Feature

You can now create and configure the following organization-level Cloud NGFW resources within a Google Cloud project:

  * Security profiles
  * Security profile groups
  * Firewall endpoints
  * Firewall endpoint associations



For more information, see [Security profile overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles), [Security profile group overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups), and [Firewall endpoint overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints). This feature is available in **Public preview**.

## March 24, 2026

v1

Feature

You can use the URL filtering service to filter your workload traffic by using domain and Server Name Indication (SNI) information available in the egress HTTP(S) messages. For more information, see [URL filtering service overview](https://docs.cloud.google.com/firewall/docs/about-url-filtering). This feature is available in **General Availability**.

## March 23, 2026

v1

Feature

Secure tags with a `purpose-data` attribute specifying a VPC network or an organization now support VPC networks that are connected using VPC Network Peering. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview). This feature is available in **General Availability**.

## February 25, 2026

v1

Feature

You can use network contexts to meet your security goals by using fewer firewall policy rules more efficiently. For more information, see [Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts). This feature is available in **General Availability**.

## February 19, 2026

v1

Feature

Cloud NGFW now supports regional system firewall policies. Regional system firewall policies are read-only policies that internal Google services, such as Google Kubernetes Engine, use to secure their operations within a VPC network. For more information, see [Regional system firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#regional-system-firewall-policies). This feature is available in **General Availability**.

## January 13, 2026

v1

Feature

You can now create regional firewall policies that apply to managed Envoy proxies used by internal Application Load Balancers and internal proxy Network Load Balancers. For more information, see [Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers](https://docs.cloud.google.com/firewall/docs/regional-network-app-lb). This feature is available in **Preview**.

## November 17, 2025

v1

Feature

You can create a Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) Virtual Private Cloud (VPC) network and configure firewall rules that apply to the network. For more information, see [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce). This feature is available in **General Availability**.

## November 13, 2025

v1

Feature

You can create a firewall endpoint that supports jumbo frames up to 8,500 bytes in size. For more information, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size). This feature is available in **General Availability**.

## September 23, 2025

v1

Feature

You can use the URL filtering service to filter your workload traffic by using domain and Server Name Indication (SNI) information available in the egress HTTP(S) messages. For more information, see [URL filtering service overview](https://docs.cloud.google.com/firewall/docs/about-url-filtering). This feature is available in **Preview**.

## August 04, 2025

v1

Feature

You can create a secure tag at the organization level and bind its value to all virtual machine (VM) instances across that organization. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview). This feature is available in **General Availability**.

## July 25, 2025

v1

Feature

You can create a Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) Virtual Private Cloud (VPC) network and configure firewall rules that apply to the network. For more information, see [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce). This feature is available in **Preview**.

## June 23, 2025

v1

Feature

You can create a secure tag at the organization level and bind its value to all virtual machine (VM) instances across that organization, instead of applying tags to instances within a specific network. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview). This feature is available in **Preview**.

## April 24, 2025

v1

Feature

You can use a single request to batch update all the firewall policy rules for hierarchical and network firewall policies. For more information, see [Overview of batch update to firewall policy rules](https://docs.cloud.google.com/firewall/docs/batch-update-overview). This feature is available in **General Availability**.

## December 13, 2024

v1

Feature

You can use network contexts to meet your security goals by using fewer firewall policy rules more efficiently. This feature is available in **Preview**. For more information, see [Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts).

## August 28, 2024

v1

Feature

You can use custom constraints to provide more granular and customizable control over specific fields for firewall policy resources. For more information, see [Manage firewall policy resources by using custom constraints](https://docs.cloud.google.com/firewall/docs/custom-constraints-fw-policy). This feature is available in **General Availability**.

## April 08, 2024

v1

Announcement

Starting **April 9, 2024** , you will be charged for the Cloud NGFW Enterprise feature—[intrusion prevention service](https://cloud.google.com/firewall/docs/about-intrusion-prevention). For more information about billing, see [Cloud NGFW pricing](https://docs.cloud.google.com/firewall/pricing).

v1

Announcement

Cloud Firewall in Google Cloud is now Cloud Next Generation Firewall (NGFW). For more information, see [Cloud NGFW](https://docs.cloud.google.com/security/products/firewall).

v1

Feature

Cloud NGFW Enterprise, including the [intrusion prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention), is available in **General Availability**. Use intrusion prevention service to safeguard your workload traffic from threats such as malware, spyware, and command-and-control attacks.

## September 30, 2023

v1

Announcement

Starting **September 30, 2023** , you will be charged for the Cloud Firewall Standard feature—[fully qualified domain name (FQDN) objects](https://cloud.google.com/firewall/docs/fqdn-objects-overview). For more information about billing, see [Cloud Firewall pricing](https://docs.cloud.google.com/firewall/pricing).

## September 27, 2023

v1

Feature

You can use [fully qualified domain name (FQDN) objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview) in firewall policy rules to filter incoming or outgoing traffic from specific domain names. This feature is available in General Availability.

## September 08, 2023

v1

Announcement

Starting **September 8, 2023** , you will be charged for the following Cloud Firewall Standard features:

  * [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview)
  * [Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview)



For more information about billing, see [Cloud Firewall pricing](https://cloud.google.com/firewall/pricing).

## August 29, 2023

v1

Feature

You can use [intrusion prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) to safeguard your workload traffic from threats such as malware, spyware, and command-and-control attacks. This feature is available in **Preview**.

## June 30, 2023

v1

Feature

You can use custom constraints to provide more granular and customizable control over specific fields for VPC firewall rule resources. For more information, see [Manage firewall resources by using custom constraints](https://docs.cloud.google.com/firewall/docs/custom-constraints). This feature is available in **Preview**.

## June 26, 2023

v1

Feature

[Address groups](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies) are a logical collection of either IPv4 address ranges or IPv6 address ranges in CIDR format. You can use address groups to define consistent sources or destinations referenced across multiple rules in the same or different firewall policies. This feature is available in **General Availability**.

## June 05, 2023

v1

Feature

Use [Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview) to secure your network by allowing or blocking traffic based on threat intelligence data. This feature is available in **General Availability**.

v1

Feature

Use [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview) in firewall policy rules to filter external IPv4 and external IPv6 traffic based on specific geographic locations or regions. This feature is available in **General Availability**.

## April 28, 2023

v1

Feature

**General Availability:** You can specify the [source IP ranges for egress firewall rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-src) and the [destination IP ranges for ingress firewall rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
