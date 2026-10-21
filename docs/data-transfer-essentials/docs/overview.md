---
url: https://docs.cloud.google.com/data-transfer-essentials/docs/overview/
title: Data Transfer Essentials overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:00.830373+00:00
---

# Data Transfer Essentials overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-transfer-essentials/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Data Transfer Essentials ](https://docs.cloud.google.com/data-transfer-essentials/docs)
  * [ Guides ](https://docs.cloud.google.com/data-transfer-essentials/docs/overview)



Send feedback 

#  Data Transfer Essentials overview Stay organized with collections  Save and categorize content based on your preferences. 

Data Transfer Essentials provides cost-effective data transfer between services of the same organization that are distributed across different cloud service providers (CSPs) and connected over public internet. This page provides an overview about Data Transfer Essentials.

## When to use Data Transfer Essentials

In some architectures, services of the same organization might reside on different cloud platforms. Customers running such applications face a complex landscape of data transfer options, each with varying costs and performance trade-offs.

Data Transfer Essentials allows for cost-optimized data transfer between two services of an organization that are running on different cloud platforms. It's specifically designed for intra-organization traffic.

Data Transfer Essentials is designed for cross-cloud connectivity for essential [supported services, tiers, and regions](https://docs.cloud.google.com/data-transfer-essentials/docs/services) with external IP connectivity over the internet. For mission-critical services, other Google Cloud products, such as [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview), might be more suitable.

**Note:** Data Transfer Essentials doesn't extend to applications that serve end users—whether organizations or consumers—on other CSPs. Such traffic is charged at the data transfer rates that are applicable by default as documented in [Network Service Tiers pricing](https://cloud.google.com/network-tiers/pricing).

For more information, see [Frequently asked questions](https://docs.cloud.google.com/data-transfer-essentials/docs/faq).

## How it works

Assume that one of your applications uses two CSPs, one of which is Google Cloud and the other `Cloud service provider A`. In Google Cloud, you use a [service in a tier and region that Data Transfer Essentials supports](https://docs.cloud.google.com/data-transfer-essentials/docs/services). You connect from the Google Cloud service to the service on `Cloud service provider A` by using external IP connectivity over the internet.

Data Transfer Essentials helps you configure billing for data transferred from the Google Cloud service to the service on `Cloud service provider A`. When the Data Transfer Essentials configuration for your service is active, traffic between these resources uses Data Transfer Essentials billing rather than billing according to the default network pricing of outbound traffic to the internet for that service, region, and tier.

[ ![Billing by using Data Transfer Essentials.](https://docs.cloud.google.com/static/data-transfer-essentials/images/data-transfer-essentials-concept.svg)](https://docs.cloud.google.com/static/data-transfer-essentials/images/data-transfer-essentials-concept.svg) Data Transfer Essentials billing (click to enlarge).

## Data Transfer Essentials resources

To enable Data Transfer Essentials for your services, create the following Data Transfer Essentials resources:

  * A [configuration](https://docs.cloud.google.com/data-transfer-essentials/docs/create-resources#create-configuration) (`multicloudDataTransferConfigs`) resource.

Specifies the services for which you want to enable Data Transfer Essentials. You can create only one Data Transfer Essentials configuration per region per project. You can include only [supported services](https://docs.cloud.google.com/data-transfer-essentials/docs/services) in a configuration.

  * Associated [destination](https://docs.cloud.google.com/data-transfer-essentials/docs/create-resources#create-destination) (`multicloudDataTransferConfigs.destinations`) resources.

Specifies the external IP addresses and destination CSPs that you want to include in the configuration. You can specify only [recognized ASNs](https://docs.cloud.google.com/data-transfer-essentials/docs/asn).




## Auditing

Data Transfer Essentials is designed for intra-organization applications and not for serving third-party customers.

If a configured IP prefix doesn't meet the specified criteria, its associated endpoint is marked as invalid. If all endpoints linked to the IP prefix are considered to be invalid, the IP prefix is labeled as suspended and the traffic directed to it is billed as regular internet traffic.

Data Transfer Essentials is initially offered at no charge when used according to the guidance provided in the documentation. If Data Transfer Essentials becomes a billed service, Google will notify you in advance through [Mandatory Service Announcements (MSAs)](https://docs.cloud.google.com/docs/cloud-msa).

To ensure compliance, Google Cloud reserves the right to validate an IP address as a legitimate intra-organization CSP destination.

## SLA

No Service Level Agreement (SLA) applies to the Data Transfer Essentials service. If you use a service that supports Data Transfer Essentials, that service might offer its own SLA. For details, see the documentation for that service.

For services that require data transfer with SLA-backed performance and availability, use [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
