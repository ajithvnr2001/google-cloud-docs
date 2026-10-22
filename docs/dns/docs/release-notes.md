---
url: https://docs.cloud.google.com/dns/docs/release-notes/
title: Cloud DNS release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:32.567197+00:00
---

# Cloud DNS release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Resources ](https://docs.cloud.google.com/dns/docs/resources)



Send feedback 

#  Cloud DNS release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Cloud DNS. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/dns-release-notes.xml) directly. 

## October 12, 2026

Feature

Outbound Endpoints for Cloud DNS is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Attach Outbound Endpoints to forwarding zones or server policies to enable direct DNS query forwarding from VPC networks to external and on-premises DNS resolvers using private IP addresses. For more information, see [Outbound Endpoints overview](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview).

## March 15, 2026

Feature

The `filter` query parameter for [`resourceRecordSets.list`](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/list#query-parameters) is generally available ([GA](https://cloud.google.com/products?e=48754805#product-launch-stages)).

You can filter records to match a specified domain using the API.

## January 16, 2026

Feature

Monitoring your internet-bound DNS queries for malicious activity using DNS Armor is generally available ([GA](https://cloud.google.com/products?e=48754805#product-launch-stages)).

For more information, see [Advanced threat detection with DNS Armor](https://docs.cloud.google.com/dns/docs/threat-detection).

## September 30, 2025

Feature

[Alias records](https://cloud.google.com/dns/docs/records-overview#alias-records) are available in [GA](https://cloud.google.com/products#product-launch-stages).

This custom record type provides CNAME-like functionality at the zone apex, mapping the apex domain name to a canonical target.

## August 29, 2025

Feature

Monitoring your internet-bound DNS queries for malicious activity using advanced threat detection from DNS Armor is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Advanced threat detection overview](https://docs.cloud.google.com/dns/docs/threat-detection).

## August 26, 2025

Feature

DNS64 is available in [GA](https://cloud.google.com/products#product-launch-stages). 

DNS64 provides synthesized IPv6 addresses for IPv4 destinations. For more information, see the following:

  * [DNS64 overview](https://docs.cloud.google.com/dns/docs/overview#dns64-overview)
  * [Configure DNS64 server policies](https://docs.cloud.google.com/dns/docs/configure-dns64)



## June 30, 2025

Feature

Using a fully qualified domain name (FQDN) [forwarding target](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones) is available for outbound DNS forwarding in [GA](https://cloud.google.com/products#product-launch-stages).

## April 28, 2025

Feature

Using a fully qualified domain name (FQDN) [forwarding target](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones) is available for outbound DNS forwarding in [**Preview**](https://cloud.google.com/products#product-launch-stages).

## February 21, 2025

Feature

[Health checks for external endpoints](https://docs.cloud.google.com/dns/docs/routing-policies-overview#health-checks-internet) in Cloud DNS routing policies are now available in **[GA](https://cloud.google.com/products#product-launch-stages)**.

## January 30, 2025

Feature

[DNS64](https://docs.cloud.google.com/dns/docs/overview#dns64-overview) is now available in **[Preview](https://cloud.google.com/products/#product-launch-stages)**.

## August 08, 2024

Feature

You can now select internal proxy Network Load Balancers as a health checked target for DNS routing policies in **[Preview](https://cloud.google.com/products/#product-launch-stages)**. For more information, see [DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/routing-policies-overview).

## July 31, 2024

Feature

[Health checks for external endpoints](https://docs.cloud.google.com/dns/docs/routing-policies-overview#health-checks-internet) in Cloud DNS routing policies are now available in **[Preview](https://cloud.google.com/products/#product-launch-stages)**.

## August 14, 2023

Feature

You can now select a cross-region internal Application Load Balancer as a health checked target for DNS routing policies. For more information, see [Manage DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/zones/manage-routing-policies).

## August 07, 2023

Feature

You can now select internal Application Load Balancers as a health checked target for DNS routing policies. For more information, see [Manage DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/zones/manage-routing-policies).

## February 22, 2023

Feature

[Health checks for internal load balancers and automatic failovers](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies) in Cloud DNS routing policies are now available in **[GA](https://cloud.google.com/products/#product-launch-stages)**.

## December 14, 2022

Feature

[Zonal Cloud DNS zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#zonal_zones) are now available in **[GA](https://cloud.google.com/products/#product-launch-stages)**.

You can create private DNS zones that are scoped only to a Google Cloud zone.

Feature

Configuring [Cloud DNS scopes](https://docs.cloud.google.com/dns/docs/scopes) is now available in [**GA**](https://cloud.google.com/products/#product-launch-stages).

## December 05, 2022

Feature

[Cloud DNS per resource IAM permissions](https://docs.cloud.google.com/dns/docs/zones/iam-per-resource-zones) are available in **[GA](https://cloud.google.com/products/#product-launch-stages)**.

## August 18, 2022

Feature

[Health checks for internal load balancers and automatic failovers](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies) in Cloud DNS routing policies are now available in **[Preview](https://cloud.google.com/products/#product-launch-stages)**.

## August 16, 2022

Feature

[Alias records](https://docs.cloud.google.com/dns/docs/records-overview#alias-records) are available in **[Preview](https://cloud.google.com/products/#product-launch-stages)**.

You can now manage an alias record, which maps an alias domain name to a canonical name at the zone apex, by using Cloud DNS.

## June 13, 2022

Feature

[Cloud DNS per resource IAM permissions](https://docs.cloud.google.com/dns/docs/zones/iam-per-resource-zones) are available in **[Preview](https://cloud.google.com/products/#product-launch-stages)**.

You can now set up specific read, write, or administrator permissions for different managed zones under the same project.

## February 22, 2022

Feature

[Zonal Cloud DNS zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#zonal_zones) are now available in **[Preview](https://cloud.google.com/products/#product-launch-stages)**.

You can create private DNS zones that are scoped only to a Google Cloud zone.

## February 07, 2022

Change

This release fixes an issue in which [Audit Logs](https://docs.cloud.google.com/dns/docs/audit-logging) for `PATCH` operations on managed zones and DNS server policies were not being generated.

## January 21, 2022

Feature

[Managing routing policies](https://docs.cloud.google.com/dns/docs/zones/manage-routing-policies) in Cloud DNS is available in [**GA**](https://cloud.google.com/products/#product-launch-stages).

## November 12, 2021

Change

The type of the `vmInstanceId` field in Cloud DNS's Stackdriver Logs has been changed from a number to a string.

## November 09, 2021

Feature

[Cloud Logging](https://docs.cloud.google.com/dns/docs/monitoring#using_logging) for managed public zones in Cloud DNS is now available in [**GA**](https://cloud.google.com/products/#product-launch-stages).

## November 03, 2021

Feature

[Managing response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies) in Cloud DNS is available in [**GA**](https://cloud.google.com/products/#product-launch-stages).

## August 19, 2021

Feature

[Managing routing policies](https://docs.cloud.google.com/dns/docs/zones/manage-routing-policies) in Cloud DNS is available in [**preview**](https://cloud.google.com/products/#product-launch-stages).

## May 20, 2021

Feature

[Cloud DNS monitoring dashboard](https://docs.cloud.google.com/dns/docs/monitoring-dashboard) is available in [**GA**](https://cloud.google.com/products/#product-launch-stages).

## May 12, 2021

Feature

Configuring [Cloud DNS scopes](https://docs.cloud.google.com/dns/docs/scopes) is now available in [**Preview**](https://cloud.google.com/products/#product-launch-stages).

## March 24, 2021

Feature

The [API for updating `ResourceRecordSets` in Cloud DNS](https://docs.cloud.google.com/dns/docs/records#creating_a_resourcerecordset) is now available in [**GA**](https://cloud.google.com/products/#product-launch-stages).

## February 16, 2021

Feature

[Managing response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies) in Cloud DNS is available in [**Preview**](https://cloud.google.com/products/#product-launch-stages).

## January 11, 2021

Feature

The [API for updating `ResourceRecordSets` in Cloud DNS](https://docs.cloud.google.com/dns/docs/records#creating_a_resourcerecordset) is now available in [**Beta**](https://cloud.google.com/products/#product-launch-stages).

## May 18, 2020

Feature

[DNS forwarding to a non-RFC 1918 address](https://docs.cloud.google.com/dns/zones#creating-forwarding-zones) is available in **General Availability**.

## January 07, 2020

Feature

[Cloud DNS peering](https://docs.cloud.google.com/dns/docs/overview#dns-peering) is available in **General Availability**.

## November 19, 2019

Feature

[DNS forwarding to a non-RFC 1918 address](https://docs.cloud.google.com/dns/zones#creating-forwarding-zones) is available in **Beta**.

## October 08, 2019

Feature

[Private DNS User Facing Query Logging and Monitoring](https://docs.cloud.google.com/dns/docs/monitoring#private_dns_logging) is available in **General Availability**.

## September 24, 2019

Feature

[DNS Forwarding](https://docs.cloud.google.com/dns/zones#creating-forwarding-zones) is available in **General Availability**.

## April 05, 2019

Feature

[DNS peering](https://docs.cloud.google.com/dns/docs/overview#dns-peering) is available in **Beta**.

Feature

[Private DNS logging and monitoring](https://docs.cloud.google.com/dns/docs/monitoring) is available in **Beta**.

## March 26, 2019

Feature

[Private zones support](https://docs.cloud.google.com/dns/zones) is available in **General Availability**.

## March 12, 2019

Change

[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) service projects now support [Cloud DNS private zones](https://docs.cloud.google.com/dns/docs/overview#concepts) by default.

## December 11, 2018

Feature

[DNS forwarding](https://docs.cloud.google.com/dns/zones) is available in **Beta**.

## October 23, 2018

Feature

[Private zones support](https://docs.cloud.google.com/dns/zones) is available in **Beta**.

## May 02, 2018

Feature

[DNSSEC for Cloud DNS](https://docs.cloud.google.com/dns/dnssec) is available in **General Availability**.

## November 02, 2017

Feature

[DNSSEC for Cloud DNS](https://docs.cloud.google.com/dns/dnssec) is available in **Beta**.

## March 06, 2017

Feature

Private zones for Cloud DNS is available in **Alpha**.

## May 28, 2016

Feature

[DNSSEC for Cloud DNS](https://docs.cloud.google.com/dns/dnssec) is available in **Beta**.

## April 13, 2015

Feature

[Cloud DNS](https://docs.cloud.google.com/dns/docs) is available in **General Availability**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
