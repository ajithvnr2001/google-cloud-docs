---
url: https://docs.cloud.google.com/dns/docs/special-configurations/
title: Special configurations \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:58.529367+00:00
---

# Special configurations  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/special-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Special configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes special configurations for DNS.

## DNS outbound forwarding for multiple VPC networks

If you want more than one Virtual Private Cloud (VPC) network to query an on-premises DNS server, you must create a forwarding zone in one of the networks that points to the on-premises environment. Then, in each of the other projects, create a peering zone that points to the VPC network designated to query the forwarding zone. Peering between two VPC networks is applicable within the same or different projects.

For example, you have VPC networks A, B, and C connected to on-premises through VPN tunnels or VLAN attachments. You can create a forwarding zone in VPC network A that forwards requests to the on-premises DNS server. You can then create peering zones for VPC networks B and C that point to the forwarding zone. As a result, queries for `example.com.` resolve according to the [name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order) of VPC network A.

### Example

  1. Suppose that your domain `company.com` has several VPC networks in the Google Cloud console that may or may not be [DNS peered](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones).
  2. All the VPC networks need to reach the same set of on-premises DNS servers for records in the DNS zone `corp.company.com.`.



### Configuration

  1. Designate a single VPC network for outbound DNS forwarding to on-premises name servers. Name this `core-vpc`, for example.
  2. Configure one or more VPN tunnels or VLAN attachments between `core-vpc` and your on-premises environment.
  3. Create an outbound forwarding zone in the project that contains `core-vpc` for the DNS name `corp.company.com.`. Configure the IP addresses of the on-premises name servers as the targets of the zone. Authorize `core-vpc` to query the forwarding zone.
  4. For every other VPC network, [create a DNS peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones) for the DNS name `corp.company.com.` that points to `core-vpc`.



## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview). 
  * To learn about using multi-provider public DNS, see [Best practices for Cloud DNS](https://docs.cloud.google.com/dns/docs/best-practices#multi-provider-dns). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
