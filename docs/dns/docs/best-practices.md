---
url: https://docs.cloud.google.com/dns/docs/best-practices/
title: Best practices for Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:39.959724+00:00
---

# Best practices for Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Best practices for Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

This document provides best practices for private zones, DNS forwarding, and reference architectures for hybrid DNS.

It's easier for both humans and applications to use the Domain Name System (DNS) to address applications and services because using a name is easier to remember and more flexible than using IP addresses. In a hybrid environment that consists of on-premises and one or more cloud platforms, DNS records for internal resources often need to be accessed across environments. Traditionally, on-premises DNS records are manually administered by using an authoritative DNS server, such as `BIND` in UNIX/Linux environments or Active Directory in Microsoft Windows environments.

This document describes best practices for forwarding private DNS requests between environments to make sure that services can be addressed from both on-premises environments and within Google Cloud.

## General principles

### Learn about DNS concepts on Google Cloud

When you use DNS on Google Cloud, it's important to understand the different systems and services available in Google Cloud for DNS resolution and domain names:

  * [Internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns) is a service that automatically creates DNS names for virtual machines and internal load balancers on [Compute Engine](https://docs.cloud.google.com/compute/docs). 
  * [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) is a service providing low latency and high availability DNS zone serving. It can act as an authoritative DNS server for public zones that are visible to the internet, or for private zones that are visible only within your network. 
  * [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview) is a highly available, hardened service that runs Microsoft Active Directory, including a domain controller. 
  * [Public DNS](https://developers.google.com/speed/public-dns/) is a Google service that is not part of Google Cloud that acts as an open, recursive DNS resolver.
  * [Cloud Domains](https://docs.cloud.google.com/domains/docs) is a domain registrar for buying, transferring, and managing domains within Google Cloud. Cloud Domains lets you interact with the domain registration system through an API. 



### Identify stakeholders, tools, and processes

When you think about building a strategy for DNS in a hybrid environment, it's important to familiarize yourself with your current architecture and contact all stakeholders. Do the following:

  * Identify and contact the administrator of your organization's corporate DNS servers. Ask them for information about the configurations that are required to map your on-premises configuration to a suitable architecture on Google Cloud. For information about methods for accessing Google Cloud DNS records, see Use conditional forwarding for accessing DNS records from on-premises.
  * Familiarize yourself with the current DNS software and identify the domain names that are used privately within your organization.
  * Identify contacts on the networking team who can make sure that traffic to Cloud DNS servers is correctly routed.
  * Familiarize yourself with your hybrid connectivity strategy and with hybrid and multicloud patterns and practices.



### Create a consistent naming standard

Create a naming standard that is consistent throughout your organization. For example, assume that your organization uses `example.com` as its second-level domain name and the domain for public resources (for example, `www.example.com`). Where the public zones are hosted is irrelevant for the purposes of this document because the scope is to migrate private zones.

For naming corporate resources on-premises, you can choose from the following patterns:

  * **You can have different domain names for on-premises servers and for Google Cloud.** This pattern uses a separate domain for your different environments—for example, `corp.example.com` for your on-premises servers and `gcp.example.com` for all resources on Google Cloud. If you use other public cloud environments, they can each have a separate subdomain. This is the preferred pattern, because you can forward requests between environments.

You can also use separate domain names such as `example.com` and `example.cloud`.

  * **You can have the Google Cloud domain as a subdomain of the domain that contains on-premises servers.** Using the `example.com` domain, on-premises could use `corp.example.com`, and Google Cloud could use `gcp.corp.example.com`. This is a common pattern when most of the resources remain on-premises.

  * **You can have the on-premises domain as a subdomain of the domain that contains Google Cloud records.** Using the `example.com` domain, Google Cloud could use `corp.example.com` and on-premises could use `dc.corp.example.com`. This is an uncommon pattern, but it might be used for digital organizations that have only a small footprint on-premises.

  * **You can use the same domain for Google Cloud and for on-premises.** In this case, both Google Cloud and on-premises use resources that use the `corp.example.com` domain. Avoid this pattern because it makes managing records in a hybrid environment much harder; it's possible only when you use a single authoritative DNS system.




The rest of this page uses the following domain names:

  * `example.com` as a domain name for your public records, regardless of where they're hosted.
  * `corp.example.com` as a zone hosted by your on-premises DNS server. This zone hosts records of your on-premises resources.
  * `gcp.example.com` as a Cloud DNS private managed zone that hosts records for your Google Cloud resources.



Figure 1 illustrates a domain name setup that is consistent across both your on-premises network and Google Cloud.

[ ![FIgure 1. Consistent domain name setup across your organization.](https://docs.cloud.google.com/static/dns/images/example-domain-name-setup.svg)](https://docs.cloud.google.com/static/dns/images/example-domain-name-setup.svg) **Figure 1.** Domain name setup is consistent across the organization.

For naming resources within your Virtual Private Cloud (VPC) network, you can follow guidelines such as the ones in the solutions guide [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/solutions/best-practices-vpc-design).

### Choose where DNS resolution is performed

In a hybrid environment, DNS resolution can be performed in different locations. You can do the following:

  * Use a hybrid approach with two authoritative DNS systems.
  * Keep DNS resolution on-premises.
  * Move all DNS resolution to Cloud DNS.



We recommend the hybrid approach, so this document focuses on that approach. However, for completeness, this document briefly describes the alternative approaches.

#### Use a hybrid approach with two authoritative DNS systems

We recommend using a hybrid approach with two authoritative DNS systems. In this approach:

  * Authoritative DNS resolution for your private Google Cloud environment is done by Cloud DNS.
  * Authoritative DNS resolution for on-premises resources is hosted by existing DNS servers on-premises.



Figure 2 shows this arrangement.

[ ![Figure 2. A hybrid DNS architecture that uses both Cloud DNS
    and on-premises DNS servers to provide authoritative DNS resolution.](https://docs.cloud.google.com/static/dns/images/hybrid-with-two-dns.svg)](https://docs.cloud.google.com/static/dns/images/hybrid-with-two-dns.svg) **Figure 2.** A hybrid DNS architecture that uses both Cloud DNS and on-premises DNS servers provides authoritative DNS resolution.

The scenario shown in figure 2 is the preferred use case. The following details are covered later on this page:

  * How to set up forwarding between environments using private zones and DNS forwarding.
  * How to configure firewalls and routing.
  * Reference architectures that show how to use one or multiple VPC networks.



#### Keep DNS resolution on-premises

An alternative approach is to continue using your existing on-premises DNS server for authoritatively hosting all internal domain names. In that case, you can use an alternative name server to forward all requests from Google Cloud through outbound DNS forwarding.

This approach has the following advantages:

  * You make fewer changes in business processes.
  * You can continue to use your existing tools.
  * You can use deny lists to filter individual DNS requests on-premises.



However, it has the following disadvantages:

  * DNS requests from Google Cloud have higher latency.
  * Your system relies on connectivity to on-premises environments for DNS operations.
  * You might find it difficult to integrate highly flexible environments such as autoscaled instance groups.
  * The system might not be compatible with products such as Managed Service for Apache Spark because those products rely on reverse resolution of Google Cloud instance names.



#### Move all DNS resolution to Cloud DNS

Another approach is to migrate to Cloud DNS as an authoritative service for all domain resolution. You can then use private zones and [inbound DNS forwarding](https://docs.cloud.google.com/dns/docs/policies#create-in) to migrate your existing on-premises name resolution to Cloud DNS.

This approach has the following advantages:

  * You don't need to maintain a high availability DNS service on-premises.
  * Your system can use Cloud DNS to take advantage of centralized [logging and monitoring](https://docs.cloud.google.com/dns/docs/monitoring).



However, it has the following disadvantages:

  * DNS requests from on-premises have higher latency.
  * Your system requires a reliable connection to your VPC network for name resolution.



## Best practices for Cloud DNS private zones

Private zones host DNS records that are visible only inside your organization. Public zones on Cloud DNS are not covered in this document. Public zones cover the organization's public records, such as DNS records for the public website, and they're not as relevant in a hybrid setup.

### Use automation to manage private zones in the Shared VPC host project

If you use Shared VPC networks within your organization, you must host all the private zones on Cloud DNS within the host project. All service projects automatically can access the records in private zones attached to the Shared VPC network. Alternatively, you can set up the zone in a service project using [cross-project binding](https://docs.cloud.google.com/dns/docs/zones/cross-project-binding).

Figure 3 shows how private zones are hosted in a Shared VPC network.

[ ![Figure 3. Private zones hosted in a Shared VPC network \(click to enlarge\).](https://docs.cloud.google.com/static/dns/images/private-zones-hosted-in-shared-vpc-network.svg)](https://docs.cloud.google.com/static/dns/images/private-zones-hosted-in-shared-vpc-network.svg) **Figure 3.** This setup shows how private zones are attached to a Shared VPC.

If you want teams to set their own DNS records, we recommend that you automate DNS record creation. For example, you can create a web application or an internal API where users set their own DNS records under specific subdomains. The app verifies that the records comply with your organization rules.

Alternatively, you can put your DNS configuration in a code repository such as [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories) in the form of [Terraform](https://www.terraform.io/) or [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs) descriptors and accept pull requests from teams.

In both cases, a service account with the IAM [DNS Administrator](https://docs.cloud.google.com/dns/docs/access-control#roles) role in the host project can automatically deploy the changes after they've been approved.

### Set IAM roles using the principle of least privilege

Use the [security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) to give the right to change DNS records only to those in your organization who need to perform this task. Avoid using [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) because they might give access to resources beyond those that the user requires. Cloud DNS offers [roles and permissions](https://docs.cloud.google.com/dns/docs/access-control#permissions_and_roles) that allow you to give read and write access that is specific to DNS.

If it's important to separate the ability to create private DNS zones from the ability to create public zones, use the `dns.networks.bindPrivateDNSZone` permission.

## Best practices for DNS forwarding zones and server policies

Cloud DNS offers [DNS forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones) and [DNS server policies](https://docs.cloud.google.com/dns/docs/server-policies-overview) to allow lookups of DNS names between your on-premises and Google Cloud environment. You have multiple options for configuring DNS forwarding. The following section lists best practices for hybrid DNS setup. These best practices are illustrated in the Reference architectures for hybrid DNS.

**Note:** DNS forwarding cannot be used to forward between different Google Cloud environments, regardless of which way they are interconnected. For that use case, use [DNS peering](https://docs.cloud.google.com/dns/docs/zones#peering-zones).

### Use forwarding zones to query on-premises servers

To make sure that you can query DNS records in your on-premises environment, set up a forwarding zone for the domain that you're using on-premises for your corporate resources (such as _corp.example.com_). This approach is preferred over using a [DNS policy that enables an alternative name server](https://docs.cloud.google.com/dns/docs/policies#firewall-rules). It preserves access to Compute Engine internal DNS names, and external IP addresses are still resolved without an extra hop through an on-premises name server.

The traffic flow that uses this setup is shown in the Reference architectures for hybrid DNS.

Use alternative name servers only if all DNS traffic needs to be monitored or filtered on-premises, and if [private DNS logging](https://docs.cloud.google.com/dns/docs/monitoring) can't meet your requirements.

**Note:** Cloud DNS does not automatically synchronize with on-premises name servers. On-premises name servers must be available to respond to outbound-forwarded queries. As described in [DNS forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones), Cloud DNS caches results of outbound-forwarded queries for up to 60 seconds, or for the duration of their TTL. Google Cloud does not sync or cache on-premises records; requests are forwarded as they come in. Therefore it's critical for on-premises DNS servers to be available and reachable so that on-premises domains can be resolved.

### Use DNS server policies to allow queries from on-premises

To allow on-premises hosts to query DNS records that are hosted in Cloud DNS private zones (for example, _gcp.example.com_), [create a DNS server policy using inbound DNS forwarding](https://docs.cloud.google.com/dns/docs/policies#create-in). Inbound DNS forwarding allows your system to query all private zones in the project as well as internal DNS IP addresses and peered zones.

The traffic flow that uses this setup is shown in the Reference architectures for hybrid DNS.

### Open Google Cloud and on-premises firewalls to allow DNS traffic

Make sure that DNS traffic is not filtered anywhere inside your VPC network or on-premises environment by doing the following:

  * **Ensure that your on-premises firewall passes queries from Cloud DNS.** Cloud DNS sends queries from the IP address range `35.199.192.0/19`. DNS uses UDP port 53 or TCP port 53, depending on the size of the request or response.

  * **Ensure that your DNS server does not block queries.** If your on-premises DNS server accepts requests only from specific IP addresses, make sure that the IP address range `35.199.192.0/19` is included.

  * **Ensure that traffic can flow from on-premises to your forwarding IP addresses.** In Cloud Router instances, add a custom advertised route for the IP address range `35.199.192.0/19` in your VPC network to the on-premises environment.




### Use conditional forwarding for accessing DNS records from on-premises

With Cloud DNS, to access private records hosted on corporate DNS servers on-premises, you can only use [forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones). However, depending on what DNS server software you use, you might have multiple options for accessing the DNS records in Google Cloud from on-premises. In each case, access to the records happens by using [inbound DNS forwarding](https://docs.cloud.google.com/dns/docs/policies#create-in):

  * **Conditional forwarding**. Using conditional forwarding means that your corporate DNS server forwards requests for specific zones or subdomains to the forwarding IP addresses on Google Cloud. We recommend this approach because it is the least complex and lets you centrally monitor all DNS requests on the corporate DNS servers.

  * **Delegation**. If your private zone on Google Cloud is a subdomain of the zone that you use on-premises, you can also delegate this subdomain to the Google Cloud name server by setting NS entries within your zone. When you use this setup, clients can talk to the forwarding IP addresses on Google Cloud directly, so make sure that the firewall passes these requests.

  * **Zone transfers**. Cloud DNS doesn't support zone transfers, so you cannot use zone transfers to synchronize DNS records with your on-premises DNS servers.




### Use DNS peering to configure outbound forwarding for multiple VPC networks

To configure outbound forwarding to the same DNS servers for multiple VPC networks, you must use DNS peering. Configuring outbound forwarding for multiple VPC networks independently or through VPC Network Peering is unsupported for the following reasons:

  * Google Cloud accepts responses from your DNS servers only if they're routed to the VPC network from which the query originated. However, queries from any VPC network have the same IP address range `35.199.192.0/19` as source. Therefore, responses can't be routed correctly unless you have separate environments on-premises.
  * Outbound forwarding can't traverse a VPC Network Peering connection. For example, if VPC network A is configured with Cloud VPN or Cloud Interconnect, VPC network B can't use its VPC Network Peering connection to VPC network A to send DNS queries to your on-premises DNS servers.

[ ![Figure 4. A problem occurs when multiple VPC forwarding
    traffic outside of their networks.](https://docs.cloud.google.com/static/dns/images/issues-with-multiple-vpcs-outbound-forwarding.svg)](https://docs.cloud.google.com/static/dns/images/issues-with-multiple-vpcs-outbound-forwarding.svg) **Figure 4.** Problem with having multiple VPC networks doing outbound forwarding.

We recommend that you designate a single VPC network to query on-premises name servers by using outbound forwarding. Then, additional VPC networks can query the on-premises name servers by targeting the designated VPC network with a DNS peering zone. Their queries would then be forwarded to on-premises name servers according to the [name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order) of the designated VPC network. This setup is shown in the Reference architectures for hybrid DNS.

### Understand the difference between DNS peering and VPC Network Peering

[VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) is not the same as DNS peering. VPC Network Peering allows virtual machine (VM) instances in multiple projects to reach each other, but it does not change name resolution. Resources in each VPC network still follow their own resolution order.

In contrast, through DNS peering, you can allow requests to be forwarded for specific zones to another VPC network. This lets you forward requests to different Google Cloud environments, regardless of whether the VPC networks are interconnected.

VPC Network Peering and DNS peering are also set up differently. For VPC Network Peering, both VPC networks need to set up a peering relationship to the other VPC network. The peering is then automatically bidirectional.

DNS peering unidirectionally forwards DNS requests and does not require a bidirectional relationship between VPC networks. A VPC network referred to as the DNS _consumer_ network performs lookups for a Cloud DNS peering zone in another VPC network, which is referred to as the DNS _producer_ network. Users with the IAM permission `dns.networks.targetWithPeeringZone` on the producer network's project can establish DNS peering between consumer and producer networks. To set up DNS peering from a consumer VPC network, you require the DNS peer role for the producer VPC network's host project.

### If you use auto-generated names, use DNS peering for internal zones

If you use the auto-generated names for VMs that the internal DNS service creates, you can use DNS peering to forward the `projectname.internal` zones to other projects. As shown in figure 5, you can group all `.internal` zones in a hub project to make them accessible from your on-premises network.

[ ![Figure 5. DNS peering is used to organize all .internal zones into
    a hub.](https://docs.cloud.google.com/static/dns/images/dns-peering-in-a-mesh.svg)](https://docs.cloud.google.com/static/dns/images/dns-peering-in-a-mesh.svg) **Figure 5.** DNS peering is used to organize all `.internal` zones into a hub.

### If you have problems, follow the troubleshooting guide

The [Cloud DNS troubleshooting guide](https://docs.cloud.google.com/dns/docs/troubleshooting) provides instructions for resolving common errors that you might encounter when you set up Cloud DNS.

## Reference architectures for hybrid DNS

This section provides some reference architectures for common scenarios that use Cloud DNS private zones in a hybrid environment. In each case both on-premises resources and Google Cloud resources records and zones are managed within the environment. All records are available for querying both from on-premises and Google Cloud hosts.

Use the reference architecture that maps to your VPC network design:

  * **Hybrid architecture using a single Shared VPC network:** Uses a single VPC network connected to or from on-premises environments.

  * **Hybrid architecture using multiple separate VPC networks:** Connects multiple VPC networks to on-premises environments through different VPN tunnels or VLAN attachments and shares the same DNS infrastructure on-premises.

  * **Hybrid architecture using a hub VPC network connected to spoke VPC networks:** Uses VPC Network Peering to have a hub VPC network connected to multiple independent spoke VPC networks.




In each case, the on-premises environment is connected to the Google Cloud VPC networks by one or multiple Cloud VPN tunnels or Dedicated Interconnect or Partner Interconnect connections. It is irrelevant which connection method is used to each VPC network.

### Hybrid architecture using a single Shared VPC network

The most common use case is a single Shared VPC network connected to the on-premises environment as shown in figure 6.

[ ![Figure 6. A hybrid architecture uses a single Shared VPC network to connect to an on-premises network.](https://docs.cloud.google.com/static/dns/images/hybrid-arch-using-a-single-shared-vpc-network.svg)](https://docs.cloud.google.com/static/dns/images/hybrid-arch-using-a-single-shared-vpc-network.svg) **Figure 6.** A hybrid architecture uses a single Shared VPC network to connect to an on-premises network.

To set up this architecture:

  1. Set up your on-premises DNS servers as authoritative for `corp.example.com`.
  2. Configure an authoritative private zone (for example, `gcp.example.com`) on Cloud DNS in the host project of the Shared VPC network, and set up all records for resources in that zone.
  3. Set a DNS server policy on the host project for the Shared VPC network to allow inbound DNS forwarding.
  4. Set a DNS forwarding zone that forwards `corp.example.com` to the on-premises DNS servers. The Shared VPC network needs to be authorized to query the forwarding zone.
  5. Set up forwarding to `gcp.example.com` on your on-premises DNS servers, pointing at an inbound forwarder IP address in the Shared VPC network.
  6. Make sure that DNS traffic is allowed on your on-premises firewall.
  7. In Cloud Router instances, add a custom advertised route for the range `35.199.192.0/19` to the on-premises environment.



### Hybrid architecture using multiple separate VPC networks

Another option for hybrid architectures is to have multiple separate VPC networks. These VPC networks in your Google Cloud environment are not connected to each other through VPC Network Peering. All VPC networks use separate Cloud VPN tunnels or [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) to connect to your on-premises environments.

As shown in figure 7, a typical use case for this architecture is when you have separate production and development environments that do not communicate with each other, but they share DNS servers.

[ ![Figure 7. A hybrid architecture can use multiple separate
    VPC networks.](https://docs.cloud.google.com/static/dns/images/hybrid-arch-using-multiple-vpc-networks.svg)](https://docs.cloud.google.com/static/dns/images/hybrid-arch-using-multiple-vpc-networks.svg) **Figure 7.** A hybrid architecture can use multiple separate VPC networks.

To set up this architecture:

  1. Set up your on-premises DNS servers as authoritative for `corp.example.com`.
  2. Configure a private zone (for example, `prod.gcp.example.com`) on Cloud DNS in the host project of the production Shared VPC network, and set up all records for resources in that zone.
  3. Configure a private zone (for example, `dev.gcp.example.com`) on Cloud DNS in the host project of the development Shared VPC network, and set up all records for resources in that zone.
  4. Set a DNS server policy on the host project for the production Shared VPC network and allow inbound DNS forwarding.
  5. In the production Shared VPC network, set a DNS zone to forward `corp.example.com` to the on-premises DNS servers.
  6. Set a DNS peering zone from the development Shared VPC network to the production Shared VPC network for `prod.gcp.example.com`.
  7. Set a DNS peering zone from the production Shared VPC network to the development Shared VPC network for `dev.gcp.example.com`.
  8. Set up inbound forwarding by delegating the resolution of `gcp.example.com.` to the Cloud DNS inbound forwarding virtual IP addresses on your on-premises name servers.
  9. Make sure that the firewall allows DNS traffic on both on-premises and Google Cloud firewalls.
  10. In Cloud Router instances, add a custom advertised route for the IP address range `35.199.192.0/19` in the production Shared VPC network to the on-premises environment.



### Hybrid architecture using a hub VPC network connected to spoke VPC networks

Another option is to use Cloud Interconnect or Cloud VPN to connect the on-premises infrastructure to a hub VPC network. As shown in figure 8, you can use VPC Network Peering to peer a VPC network with several spoke VPC networks. Each spoke VPC network hosts its own private zones on Cloud DNS. Custom routes on VPC Network Peering, along with [custom route](https://docs.cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes) advertisement on Cloud Router, allow full route exchange and connectivity between on-premises and all spoke VPC networks. DNS peering runs in parallel with VPC Network Peering connections to allow name resolution between environments.

The following diagram shows this architecture.

[ ![Figure 8. A hybrid architecture can use a hub VPC
    network connected to spoke VPC networks by using VPC Network Peering.](https://docs.cloud.google.com/static/dns/images/hybrid-arch-using-hub-vpc-to-spoke-vpc.svg)](https://docs.cloud.google.com/static/dns/images/hybrid-arch-using-hub-vpc-to-spoke-vpc.svg) **Figure 8.** A hybrid architecture can use a hub VPC network connected to spoke VPC networks. 

To set up this architecture:

  1. Set up your on-premises DNS servers as authoritative for `corp.example.com`.
  2. Configure a private zone (for example, `projectX.gcp.example.com`) on Cloud DNS for each spoke VPC network, and set up all records for resources in that zone.
  3. Set a DNS server policy on the hub project for the hub VPC network to allow inbound DNS forwarding.
  4. In the hub VPC network, create a private DNS zone for `corp.example.com` and configure outbound forwarding to the on-premises DNS servers.
  5. Set a DNS peering zone from the hub VPC network to each spoke VPC network for `projectX.gcp.example.com`.
  6. Set a DNS peering zone from each spoke VPC network to the hub VPC network for `example.com`.
  7. Set up forwarding to `gcp.example.com` on your on-premises DNS servers to point at an inbound forwarder IP address in the hub VPC network.
  8. Make sure that the firewall allows DNS traffic on both on-premises and Google Cloud firewalls.
  9. In Cloud Router instances, add a custom advertised route for the IP address range `35.199.192.0/19` in the hub VPC network to the on-premises environment.
  10. (Optional) If you also use the automatically generated internal DNS names, peer each spoke project zone (for example, `spoke-project-x.internal`) with the hub project, and forward all queries for `.internal` from on-premises.

**Note:** When you use Cloud VPN instead of VPC Network Peering between Google Cloud environments with this architecture, make sure that there is a VM or VPN tunnel in the hub project in every region used in the spoke projects. This ensures that all VMs can query records through DNS peering.

## Multi-provider public DNS using Cloud DNS

As a foundational component of application networking, reliable DNS is key to ensuring that your applications or services are available for your users. You can improve the availability and resiliency of your applications and services by configuring multiple DNS providers. When multiple DNS providers are configured, your application or service can be available to your users even if there is an outage with one of the DNS providers. You can also simplify the deployment and migration of hybrid applications that have dependencies across on-premises and cloud environments with a multi-provider DNS configuration.

Google Cloud offers an open source solution based on [octoDNS](https://github.com/octodns/octodns) to help you set up and operate an environment with multiple DNS providers. The multi-provider DNS solution leverages Cloud DNS as one of your DNS providers in an active-active (recommended) or active-passive configuration to ensure a highly available DNS architecture. After you have deployed the solution, octoDNS performs one-time as well as ongoing sync between your current DNS zones and managed DNS zones hosted in Cloud DNS. When individual DNS records are updated, the changes are propagated to corresponding DNS zones hosted in Cloud DNS without requiring any changes to your CI/CD pipelines.

**Important:** To achieve active-active configuration and reliability, you must update the NS records at your registrar to include Cloud DNS name servers.

  * To configure Cloud DNS in a multi-provider public DNS configuration, see [multi-provider-dns-with-clouddns](https://github.com/GoogleCloudPlatform/multi-provider-dns-with-clouddns).



## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To find guidance about how to approach and implement a hybrid setup that uses Google Cloud, see the [Hybrid and multi-cloud patterns and practices](https://docs.cloud.google.com/solutions/hybrid-and-multi-cloud-patterns-and-practices) solutions guide.
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
