---
url: https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config/
title: Access external services using private services access \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:15:16.470722+00:00
---

# Access external services using private services access  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Access external services using private services access Stay organized with collections  Save and categorize content based on your preferences. 

When your Looker (Google Cloud core) instance uses [private services access](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip) and is configured with private or hybrid connections, you can connect your instance to external services and resources. You can configure these connections for secure and reliable integration with data sources and applications beyond your instance's VPC network.

## Connect to other VPCs using private services access

To use internal IPs to connect to services in other VPCs that are hosted by either Google or third parties, you can use [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).

During Looker (Google Cloud core) [instance creation](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip#before_you_create_a_instance), you created a private services access connection to connect your VPC to the Looker (Google Cloud core) service. You can also [update the IP allocation](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modifying-connection) of an existing private services access connection without disrupting traffic.

To set up a private services access connection:

  1. [Allocate an internal IP range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) in your VPC network.
  2. [Set up the private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#creating-connection) between your VPC network and service producer's network, using the allocated IP range. This private connection establishes a [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) connection between your VPC and the other network.



Private connections are a one-to-one relationship between your VPC network and a service producer. If a single service producer offers multiple services, you only need one private connection for all of the producer's services.

## Connect to on-premises resources or third-party services using private services access

If your instance was created to use private services access, with either private connections or hybrid connections, you can use either of the following two options to connect Looker (Google Cloud core) instances to on-premises resources or third-party services:

  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)
  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview), specifically HA VPN, and [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



With either method, you will need to do the following:

  * Configure a [dynamic route](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) in your Looker (Google Cloud core) VPC for each on-premises resource.
  * Set up a [custom advertised route](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) of the Looker (Google Cloud core) [private services access subnet](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#about_the_service_producers_subnet) on all Cloud Routers that are deployed in the Looker (Google Cloud core) VPC.
  * Update your on-premises firewalls to allow traffic with the Looker (Google Cloud core) subnet.
  * Configure [DNS forwarding](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods), which will let Looker (Google Cloud core) connect to any on-premises resources.
  * Configure [DNS Peering](https://docs.cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains) with the Service Networking Google Managed VPC for the Looker (Google Cloud core) instance to resolve the private hostnames.



### Cloud Interconnect and Cloud Router

The following network diagram shows how Cloud Interconnect and Cloud Router interact with the Looker (Google Cloud core) service to connect to an on-premises network:

  1. Private services access connects the Looker (Google Cloud core) service with the VPC over internal IP addresses using VPC peering.
  2. Cloud Router uses Border Gateway Protocol (BGP) to advertise the IP prefixes and program dynamic routes based on the BGP advertisements it receives from a peer. Cloud Interconnect is used to connect to the on-premises network.



![](https://docs.cloud.google.com/static/looker/docs/images/looker-private-network-2316.png)

### Cloud VPN and Cloud Router

For a walkthrough of how to create a private and public IP Looker (Google Cloud core) instance and connect it to an on-premises database using Cloud VPN and Cloud Router, see the [Connect Looker Cloud over hybrid networking](https://codelabs.developers.google.com/codelabs/looker-hybrid-networking) codelab.

## What's next?

  * [Connect Looker Cloud over hybrid networking](https://codelabs.developers.google.com/codelabs/looker-hybrid-networking)
  * [Connecting Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)
  * [Prepare your Looker (Google Cloud core) instance for users](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * For an example of how to manually install [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) content, see the Looker Community article, [Installing the Looker API Explorer on a Looker (Google Cloud core) instance on a private IP network](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Installing-the-Looker-API-Explorer-on-a-Looker-Google-Cloud-core/ta-p/722671).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
