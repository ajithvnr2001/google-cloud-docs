---
url: https://docs.cloud.google.com/dns/docs/policies-overview/
title: DNS policies overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:32.084566+00:00
---

# DNS policies overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  DNS policies overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud DNS supports different types of policies. This page provides details about the different policy types and when you can use one or the other.

  * **Server policies** apply private DNS configuration to a Virtual Private Cloud (VPC) network (DNS forwarding, logging).
  * **Response policies** override private DNS responses based on the query name.
  * **Routing policies** steer traffic based on the query (for example, round robin, geolocation).



You can use all three policies at the same time depending on your needs.

## Server policies

Use server policies to set up hybrid deployments for DNS resolutions. You can set up an inbound server policy depending on the direction of DNS resolutions. If your workloads plan to use an on-premises DNS resolver, you can set up DNS forwarding zones by using an outbound server policy. On the other hand, if you want your on-premises workloads to resolve names on Google Cloud, you can set up an inbound server policy.

For more information, see the [Server policies overview](https://docs.cloud.google.com/dns/docs/server-policies-overview).

## Response policies

Use response policies to add custom rules that modify how DNS queries are handled within your network. The DNS resolver consults these rules during DNS lookups. Response policies let you customize DNS management within a private zone by using rules instead of records. If a rule in the response policy affects the incoming query, it is processed; otherwise, the lookup proceeds normally. Use these rules to achieve results similar to the DNS [response policy zone (RPZ)](https://wikipedia.org/wiki/Response_policy_zone) draft concept ([IETF](https://datatracker.ietf.org/doc/draft-ietf-dnsop-dns-rpz/)). For information about how to manage response policies, see [Manage response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies).

A response policy is different from an RPZ, which is an otherwise normal DNS zone with specially formatted data that causes compatible resolvers to provide different responses to queries. Response policies aren't DNS zones and are managed separately. For more information, see [Manage response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies).

## Routing policies

Use DNS routing policies for a resource record set to steer traffic based on the query and other factors, such as weighted round robin (WRR), geolocation, or failover. DNS routing policies lets you do the following:

  * Steer traffic from a geographical location to a content delivery network (CDN) provider.
  * Route your on-premises traffic to Google Cloud load balancers based on the query's source region.
  * Specify that traffic that originated from a specific continent is served by services in the same continent.
  * Route traffic to different service providers on WRR basis.
  * Onboard new services with a percentage of the total traffic.



For more information, see [DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/routing-policies-overview).

## What's next

  * [Apply DNS server policies](https://docs.cloud.google.com/dns/docs/policies)
  * [Manage response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies)
  * [Manage DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/routing-policies-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
