---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-overview/
title: About Cloud DNS \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:08.930691+00:00
---

# About Cloud DNS  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  About Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

This overview page explains how you can manage DNS records using Cloud DNS in Google Distributed Cloud (GDC) air-gapped. Cloud DNS provides a highly-reliable, scalable way to manage DNS records, through a command line interface and a Kubernetes-based API. Learn how Cloud DNS works in GDC, including the distinctions between public and private DNS zones.

The intended audience for this document is platform administrators and application operators responsible for network administration and managing DNS for their organization. This document assumes you have a basic understanding of essential networking and DNS concepts.

## Zone types for Cloud DNS

A DNS zone is a specific portion of the DNS namespace that you are responsible for. GDC offers two types of managed DNS zones:

  * **Public DNS zones:** These zones are visible and accessible from anywhere in your network. Public zones are used for services that you want to be reachable by users outside of your GDC.
  * **Private DNS zones:** These zones are only accessible from within your default customer Virtual Private Cloud (VPC) in GDC. Private zones are ideal for internal services and applications that must not be exposed to the external network.



## Create DNS records within zones

Within a DNS zone, you create DNS records. Each record associates a domain name or subdomain with a specific value, such as an IP address, another domain name, or text information. Different types of DNS records serve different purposes, such as directing traffic, defining mail servers, and verifying ownership. You can configure the following record types:

  * **Address (A) record:** maps a domain name to one or more IPv4 addresses. This record is the most fundamental record type for pointing a domain to a server.
  * **Canonical Name (CNAME) record:** creates an alias of one domain name to another canonical (authoritative) domain name. This record type is useful for redirecting traffic or simplifying DNS management.
  * **Text (TXT) record:** lets you associate arbitrary text with a domain name. These records are often used for verification purposes or to store information like Sender Policy Framework (SPF) records for email authentication.
  * **Pointer (PTR) record:** maps an IP address back to a domain name, also known as reverse DNS lookup. This record is often used for email server reputation and logging analysis.
  * **Mail Exchanger (MX) record:** specifies the mail servers responsible for accepting email for a domain. This is essential for setting up email services.



The [ResourceRecordSet API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/global-networking-v1#resourcerecordset) in GDC lets you create and manage DNS records within a DNS zone. This API lets you specify the details of a set of identical DNS records that share the same name, type, and TTL (Time-To-Live).

## DNS operations

You can use the gdcloud CLI or the Kubernetes API in GDC to create DNS zones and create DNS records. These interfaces let you define the state of your DNS zones, including their name, description, and visibility. The API provides the following:

  * **DNS zone creation and management:** Define and configure DNS zones such as domain name, description, public or private visibility.
  * **Zone management:** List, update, and delete managed DNS zones.
  * **Distributed deployment and replication:** Replicate DNS zones across GDC air-gapped zones for high availability and global distribution.
  * **Status monitoring:** Track overall zone health, deployment progress, and individual replica status.



For the full reference documentation for DNS zones in GDC, see [gdcloud dns managed-zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-dns-managed-zones) and [ManagedDNSZone](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/global-networking-v1#manageddnszone).

## What's next

  * [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
