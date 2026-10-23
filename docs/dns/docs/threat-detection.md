---
url: https://docs.cloud.google.com/dns/docs/threat-detection/
title: Advanced threat detection with DNS Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:47.151892+00:00
---

# Advanced threat detection with DNS Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Advanced threat detection with DNS Armor Stay organized with collections  Save and categorize content based on your preferences. 

DNS Armor, powered by [Infoblox](https://www.infoblox.com/threat-intel), is a fully-managed service that provides DNS-layer security for your Google Cloud workloads with no further software installation required. Its advanced threat detector is designed to detect malicious activity at the earliest point in the attack chain—the DNS query—without adding operational complexity or performance overhead. Threat checking is supported for Compute Engine and GKE instances.

DNS Armor allows for the processing and analysis of DNS queries directly within your existing cloud infrastructure. This removes the need to redirect sensitive traffic to a third-party proxy.

After a threat is detected, you can gain actionable insights into DNS threats through Cloud Logging.

## How DNS Armor works

When you enable a DNS threat detector for a project, DNS Armor securely sends your internet-bound DNS query logs to the dedicated deployment of the Infoblox threat engine within Google Cloud. This engine uses a combination of threat intelligence feeds and AI-based behavioral analysis to identify threats.

Any suspicious or malicious activity that's detected will automatically generate a DNS Armor threat log, which is then sent back to your project and written to Cloud Logging for you to view and act upon.

With DNS Armor's advanced threat detection, you can detect threats, such as the following:

  * **DNS Tunneling for Data Exfiltration** : DNS queries that are structured to secretly carry data out of your network, often bypassing traditional firewalls.
  * **Malware Command & Control (C2)**: DNS communication from a compromised workload that is attempting to contact an attacker's server for instructions.
  * **Domain Generation Algorithms (DGA)** : DNS queries to random-looking, machine-generated domains that malware creates to find and connect with its command and control servers.
  * **Fast Flux** : DNS queries to domains that rapidly change their associated IP addresses, a technique used to make malicious infrastructure harder to track and block.
  * **Zero-Day DNS** : DNS queries to newly registered domains that attackers use for malicious activities before those domains develop a known bad reputation.
  * **Malware Distribution** : DNS queries to malicious and high-risk domains, owned by threat actors, that are known to host or distribute malware or could host or distribute malware in the future.
  * **Lookalike Domains** : DNS queries to domains already known to be malicious that are intentionally misspelled or formatted to appear like legitimate, trusted brands.
  * **Exploit Kits** : DNS queries to websites that attempt to automatically exploit vulnerabilities in cloud workloads to install malware.
  * **Advanced Persistent Threats (APT)** : DNS queries to domains associated with targeted, long-term attack campaigns, often conducted by sophisticated groups for espionage or data theft.



## Threat detector operation

The advanced threat detector is a globally configured service available at the project level, but operates independently in each region (see [DNS Armor Locations](https://docs.cloud.google.com/dns/docs/threat-detector-locations) for the list of supported regions). However, the DNS threat detector configuration is identical regardless of the local region that threats are analyzed in. It can be enabled for all VPC networks in a project with the ability to exclude up to 100 specific networks.

Detection engines are deployed regionally and receive DNS traffic from the same region. For example, DNS traffic from a client in `us-central1` is forwarded to a detection engine deployed in `us-central1`.

A single domain name can match multiple threat categories. In this case, you'll see multiple threat events for the same DNS query.

DNS Armor is independent of query resolution. Threat analysis is performed asynchronously after query resolution, which adds no additional latency to the actual DNS resolution path in the workload. Enabling or disabling standard VPC Flow Logs or DNS query logs also won't impact the operation of DNS Armor.

**Note:** DNS Armor detects queries to domains that are known or suspected to be malicious, or are considered lookalikes to popular domains. DNS Armor isn't a proactive brand-protection or typo-squatting detection service.

### Threat checking for CNAME chains

Threat checking for DNS CNAME chains is also available with DNS Armor. The query will be in-scope if the first name in the query resolution is a public CNAME record.

If a domain in a CNAME chain triggers a threat finding, a single threat log entry is generated for the query. The `dnsQuery.queryName` field contains the initial domain queried by your workload, and the `threatInfo.threatIndicator` field contains the specific domain in the chain that triggered the detection.

### Threat detector exclusions

The following are excluded from DNS Armor inspection:

  * **VPC exclusion** : the VPC network is in the DNS Armor exclusion list.
  * **Unsupported workloads and configurations** : 
    * **Serverless** : Cloud Run, Cloud Run functions, and App Engine standard environments are unsupported.
    * **Bypassing Cloud DNS resolver** : queries from workloads configured to bypass Cloud DNS (169.254.169.254) and send queries directly to another DNS server or service, such as `8.8.8.8` are unsupported.
    * **DNS-based hub-and-spoke designs** : if spoke VPC networks are associated with DNS peering zones (such as a root `.` zone) to forward all queries, including internet-bound queries, to a central hub VPC network, those queries are not inspected. This is because the queries match a peering zone at the source and are treated as internal traffic in both the hub and spoke VPC.
  * **Non-internet path resolution** : 
    * **Internal VPC resolution** : 
      * **Compute Engine internal DNS** : queries for default [internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns)
      * **Cloud DNS private zones** : queries for records within Cloud DNS private managed zones, which includes zones integrated with [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview).
    * **Hybrid environments** : DNS traffic between a VPC network and private networks connected with Cloud VPN or Cloud Interconnect using Cloud DNS server policies or forwarding zones: 
      * Outbound or inbound queries from the VPC to and from hybrid environments.



#### Query exclusions

The following top-level domains (TLDs) are natively excluded by Cloud DNS and don't incur charges:

  * `.internal`
  * `.local` ([RFC 6762](https://datatracker.ietf.org/doc/html/rfc6762))



[RFC 2606](https://datatracker.ietf.org/doc/html/rfc2606) TLDs are also natively excluded and won't incur charges:

  * `.test`
  * `.example`
  * `.invalid`
  * `.localhost`

**Note:** Queries for random, non-existent TLDs (e.g. `.fbc`, `.localdomain`) recurse to the internet, and therefore are inspected by DNS Armor.

## Limitations

DNS Armor has the following limits.

  * **Private DNS resolution** : DNS Armor inspects only internet-bound DNS traffic.

  * **Serverless workloads (Cloud Run)** : DNS Armor doesn't inspect DNS queries from serverless workloads.

  * **Inbound forwarding** : DNS Armor doesn't inspect queries sent to Cloud DNS inbound forwarding endpoints.

  * **DNS peering zones** : DNS Armor doesn't inspect queries (even internet-bound queries) that traverse DNS peering connections.

  * **Secure Web Proxy** : DNS Armor doesn't inspect DNS queries made by Secure Web Proxy.




## Billing impact

You are charged based on how many internet-bound DNS queries your workloads produce and have threat analysis performed on them. For a list of exclusions, see Threat detector exclusions.

DNS Armor also impacts your Cloud Logging bill, as threat findings are written to your project's Cloud Logging account. For more information, see [Pricing for Google Cloud Observability: Cloud Logging](https://cloud.google.com/stackdriver/pricing).

For more information about estimating DNS Armor query volume and cost optimization, see [DNS Armor cost estimation and optimization](https://docs.cloud.google.com/dns/docs/armor-optimization).

For more information on general Cloud DNS pricing, see [Cloud DNS pricing](https://cloud.google.com/dns/pricing).

## Other security options

In addition to DNS Armor, another available security option is Google Security Operations. This service must be manually configured in your project.

Google Security Operations is a service that normalizes, indexes, correlates, and analyzes security and network telemetry data. For more information, see [Google SecOps documentation](https://docs.cloud.google.com/chronicle/docs).

## What's next

  * [Create and manage a threat detector](https://docs.cloud.google.com/dns/docs/create-threat-detector)
  * [View threats](https://docs.cloud.google.com/dns/docs/view-threat-logs)
  * [Troubleshoot common issues](https://docs.cloud.google.com/dns/docs/troubleshooting#threat-detection)
  * [Codelab tutorial](https://codelabs.developers.google.com/dns-armor-getting-started#0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
