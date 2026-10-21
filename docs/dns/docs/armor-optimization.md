---
url: https://docs.cloud.google.com/dns/docs/armor-optimization/
title: DNS Armor cost estimation and optimization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:59.462416+00:00
---

# DNS Armor cost estimation and optimization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/armor-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  DNS Armor cost estimation and optimization Stay organized with collections  Save and categorize content based on your preferences. 

This document provides some basic information about estimating DNS Armor costs. It also provides some methods for you to optimize your costs when using DNS Armor.

For general Cloud DNS pricing information, see [Cloud DNS pricing](https://cloud.google.com/dns/pricing).

More information about DNS Armor pricing can be found at [Advanced threat detection pricing](https://cloud.google.com/dns/pricing?e=48754805#dns-armor-advanced-threat-detection-pricing).

## Cost estimation

You can use the `dns.googleapis.com/query/response_count` metric filtered to `target_type=external` and `source_type==gce-vm` to estimate your costs.

**Caution:** The `dns.googleapis.com/query/response_count` metric might not be entirely accurate because it includes queries that are [excluded](https://docs.cloud.google.com/dns/docs/threat-detection#exclusions). Use this metric only for a very high-level cost estimation.

## Cost optimization

To reduce your DNS Armor costs, you can configure the following resources to exclude their traffic from threat inspection.

### Excluding Google APIs and services

By default, queries to `googleapis.com` are recursed to the internet, which means that these queries are considered to be `external` queries, and therefore in-scope to be processed by DNS Armor. To avoid this scenario, capture this traffic in a Cloud DNS private zone and route it to [Google's internal virtual IP addresses (VIPs)](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). Doing so marks these queries as `internal` and the queries will bypass DNS Armor inspection.

To exclude the API calls from DNS Armor processing, configure Private Google Access or Private Service Connect for Google APIs. For more information, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) and [About accessing Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints).

### Excluding your own domains

DNS Armor treats queries from internal workloads to public domains as external traffic, which results in processing by the threat detector. To avoid this, make sure your company domain is resolved privately using private managed zones, peering zones, or forwarding zones. As long as Cloud DNS does not recurse the queries to the internet, DNS Armor won't process the queries.

#### Private managed zone

Use this option if you want to maintain a complete and separate copy of your internal DNS zones in Cloud DNS (often referred to as "split-brain" or "split-horizon" DNS).

For example. if you create a Cloud DNS private zone for `example.com` and populate it with your DNS records, you can then attach the zone to your VPC network. This approach means when a workload queries `api.example.com`, Cloud DNS will check the attached private zone first, finds the internal record, and answers immediately. The query never leaves the VPC and is tagged as `internal`, which helps the query avoid DNS Armor processing.

#### Cloud DNS response policies

Use this option if you only need to resolve a few specific hostnames (such as `api.example.com` or `db.example.com`) to internal IP addresses, but you want the rest of your domain to continue resolving publicly over the internet.

For example. you can create a response policy rule for `api.example.com` that returns your internal IP address and attach it to your VPC. This intercepts your high-volume trusted queries and answers them locally. Queries from other domains (like `www.example.com`) will still resolve publicly and be processed by DNS Armor.

#### Forwarding zone

Use this method if you operate on-premises DNS servers (such as Active Directory, InfoBlox, or BIND) that are authoritative for your internal DNS zones, and are connected to Google Cloud using Cloud VPN or Dedicated Interconnect.

For example, you can create a Cloud DNS forwarding zone for `example.com` and configure it to directly point to the internal IP addresses (typically [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) addresses) of your on-premises DNS servers. This method sends the query across your private network to your internal servers. Because the destination is a private IP address, the query is tagged as `forwarding-zone` and isn't subject to processing by DNS Armor.

For more information, see [Use forwarding zones to query on-premises servers](https://docs.cloud.google.com/dns/docs/best-practices#use_forwarding_zones_to_query_on-premises_servers).

#### Custom DNS servers on Compute Engine VMs

If you run your own DNS servers (e.g. BIND, Active Directory, dnsmasq) on Google Cloud VMs, your DNS Armor usage depends on the routing topology you use.

  * **Cloud DNS forwarding to your VM.** Corporate queries sent using a Cloud DNS forwarding zone to your custom DNS VM's internal IP address will be considered internal and therefore won't be processed by DNS Armor.
  * **Workloads directly querying your VM.** If your workloads are configured to bypass Cloud DNS and directly query your custom DNS VM, Cloud DNS doesn't process the initial request so the queries aren't processed by DNS Armor at the workload level.
  * **Your VM forwards to Cloud DNS.** If you route all your company's internet DNS traffic through a central DNS server VM, which then forwards to Cloud DNS, the platform sees only the queries coming from that single source. The VM makes low-to-medium volume environments less expensive because DNS Armor bills based on `GREATEST(Workloads, Queries / 150)` and this method drops the Workloads baseline to 1.

**Note:** Extreme high volume environments are unlikely to see significant cost savings as you'll be billed on the volume of queries.



### Private zones resolution

Charges can arise from queries to domains that should be resolved internally, but are inadvertently leaked to the internet and therefore are resolved using public DNS and processed by DNS Armor.

To optimize your costs in this instance, handle the resolution for these domains internally within your VPC. You can either use Cloud DNS private zones or forwarding zones to direct these queries to your internal resolvers. Doing this helps ensure the queries are no longer marked as internet-bound and therefore won't be inspected by DNS Armor.

## What's next

  * For more information about DNS Armor, see [Advanced threat detection](https://docs.cloud.google.com/dns/docs/threat-detection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
