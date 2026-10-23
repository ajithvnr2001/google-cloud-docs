---
url: https://docs.cloud.google.com/vpc/docs/ipv6-support/
title: IPv6 support in Google Cloud \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:11.408296+00:00
---

# IPv6 support in Google Cloud  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/ipv6-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IPv6 support in Google Cloud

This document describes which services in Google Cloud include support for IPv6.

IPv6 has a much larger address space than IPv4, with 128 bits per address. IPv6 has many more addresses available than IPv4 does, which helps mitigate the growing shortage of IPv4 addresses.

IPv6 support is widely available in Google Cloud through dual-stack (IPv4 and IPv6) and IPv6-only compute and networking services. You can deploy dual-stack and IPv6-only subnets, which lets you deploy IPv6 workloads.

You can control IPv6 configurations by using organization policy constraints as described in the [organization policy constraints](https://docs.cloud.google.com/vpc/docs/vpc#org-policies) section of the VPC networks overview.

## Core compute and networking services

The following table summarizes support for IPv6 in core compute and networking services in Google Cloud.

If a service has an IP stack type configuration option, the table lists the supported stack types. The IPv6-only stack type is available for some services where marked in the table. If a service doesn't have a stack type configuration option, the table lists not applicable (N/A).

For more information about a given service, see the corresponding documentation.

Service | IPv6 support | Supported stack types | Documentation  
---|---|---|---  
Compute  
Compute Engine instances1 |  | Dual-stack,  
IPv6-only | 

  * [Compute Engine IP addresses overview](https://docs.cloud.google.com/compute/docs/ip-addresses)
  * [Configuring IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address)

  
Compute Engine instance templates |  | Dual-stack,  
IPv6-only  
Compute Engine managed instance groups (MIGs)2 |  | Dual-stack,  
IPv6-only | 

  * [MIGs IPv6 overview](https://docs.cloud.google.com/compute/docs/instance-groups#network)
  * [Basic scenarios for creating MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#ipv6)

  
Dynamic Network Interfaces (NICs) |  | Dual-stack,  
IPv6-only | 

  * [Multiple network interfaces overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)
  * [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)

  
Google Kubernetes Engine (GKE) nodes and pods |  | Dual-stack | 

  * [GKE IPv6 overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network)
  * [Use an IPv4 and IPv6 dual-stack network to create a dual-stack cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#dual-stack)

  
Cloud Run services and jobs (internal IPv6) |   
| Dual-stack | 

  * [Set up dual-stack services and jobs](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet)

  
Networking  
VPC networks  
Subnets |  | Dual-stack,  
IPv6-only | 

  * [Subnets IPv6 overview](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges)
  * [Add a subnet with an IPv6 address range](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules)

  
VPC Network Peering3 |  | Dual-stack | 

  * [VPC Network Peering overview](https://docs.cloud.google.com/vpc/docs/vpc-peering)
  * [Use VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering)

  
Static IP address reservation |  | N/A | 

  * [IP addresses overview](https://docs.cloud.google.com/vpc/docs/ip-addresses)
  * [Reserve a static internal IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip)
  * [Reserve a static external IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static)

  
Static routes |  | N/A | 

  * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes)
  * [Add an IPv6 static route](https://docs.cloud.google.com/vpc/docs/using-routes#adding_and_removing_routes)

  
Policy-based routes  |  | N/A | 

  * [Policy-based routes overview](https://docs.cloud.google.com/vpc/docs/policy-based-routes)
  * [Create a policy-based route for IPv6 traffic](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#create)

  
Network security  
Cloud Next Generation Firewall |  | N/A | 

  * [Firewall policy rules overview](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details)
  * [VPC firewall rules overview](https://docs.cloud.google.com/firewall/docs/firewalls)

  
Packet Mirroring  |  | N/A | 

  * [Packet Mirroring overview](https://docs.cloud.google.com/vpc/docs/packet-mirroring)
  * [Mirror IPv6 traffic](https://docs.cloud.google.com/vpc/docs/using-packet-mirroring)

  
Network Connectivity  
Cloud Router |  | N/A | 

  * [Cloud Router IP protocols support](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#ip-protocols)
  * [Establish IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp#ipv6_bgp_sessions)
  * [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp)

  
Network Connectivity Center |  | N/A | 

  * You can configure VPC spokes to exchange only IPv4 subnet ranges, both IPv4 and IPv6 subnet ranges, or only IPv6 subnet ranges. See: 
    * [IP addressing](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#ip_addressing)
    * [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke)

  
Dedicated Interconnect VLAN attachments3 |  | Dual-stack | 

  * [Dedicated Interconnect IPv6 overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#ipv6-support)
  * [Create dual-stack VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)

  
Partner Interconnect VLAN attachments3 |  | Dual-stack | 

  * [Partner Interconnect IPv6 overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#ipv6-support)
  * [Create dual-stack VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)

  
HA VPN |  | Dual-stack,  
IPv6-only | 

  * [HA VPN IPv6 overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ipv6-support)
  * [Migrate to an IPv6 HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/migrate-ha-vpn-ipv6)

  
Classic VPN |  | N/A |   
DNS  
Cloud DNS4 |  | N/A | 

  * IPv6 DNS record support: 
    * [DNS records overview](https://docs.cloud.google.com/dns/docs/records-overview)
    * [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records)
  * DNS64 synthesizes IPv6 addresses for IPv4 destinations: 
    * [DNS64 overview](https://docs.cloud.google.com/dns/docs/overview#dns64-overview)
    * [Configure DNS64](https://docs.cloud.google.com/dns/docs/configure-dns64)
To reach IPv4 destinations, configure both DNS64 and NAT64. 

  
NAT  
Cloud NAT 5 |  | N/A | 

  * By using DNS64 and NAT64, IPv6-only instances can reach IPv4 destinations on the internet and in VPC or on-premises networks. See: 
    * [NAT64 in Public NAT](https://docs.cloud.google.com/nat/docs/public-nat#nat64)
    * [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64)
    * [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation)
    * [Set up and manage network address translation with Private NAT](https://docs.cloud.google.com/nat/docs/set-up-private-nat)
    * [Configure IPv6-only subnets and instances with DNS64 and NAT64](https://docs.cloud.google.com/vpc/docs/connect-ipv6-to-ipv4) (tutorial)

  
Cloud Load Balancing  
Global external Application Load Balancer |  | Dual-stack | 

  * End-to-end dual-stack support. See: 
    * [IPv6 for Application Load Balancers and proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ipv6)
    * [Convert Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-global-ext-https-dualstack)
    * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-global-ext-proxy-dualstack)

  
Global external proxy Network Load Balancer |  | Dual-stack  
Regional external Application Load Balancer |  | Dual-stack | 

  * Dual-stack backends are supported but load balancers can't terminate IPv6 connections from clients. See: 
    * [IPv6 for Application Load Balancers and proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ipv6)
    * [Convert Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-global-ext-https-dualstack)
    * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-global-ext-proxy-dualstack)

  
Regional internal Application Load Balancer |  | Dual-stack  
Cross-region internal Application Load Balancer |  | Dual-stack  
Regional external proxy Network Load Balancer |  | Dual-stack  
Regional internal proxy Network Load Balancer |  | Dual-stack  
Cross-region internal proxy Network Load Balancer |  | Dual-stack  
Classic Application Load Balancer |  | N/A | 

  * Load balancers can terminate IPv6 connections from clients but backends with IPv6 addresses aren't supported. See [IPv6 for Application Load Balancers and proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ipv6).

  
Classic proxy Network Load Balancer |  | N/A  
Regional external passthrough Network Load Balancer6 |  | Dual-stack,  
IPv6-only | 

  * End-to-end dual-stack or IPv6-only support. See [Backend service-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).

  
Global external passthrough Network Load Balancer |  | Dual-stack,  
IPv6-only | 

  * End-to-end dual-stack or IPv6-only support. See [Global external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture).

  
Internal passthrough Network Load Balancer6 |  | Dual-stack,  
IPv6-only | 

  * End-to-end dual-stack or IPv6-only support. See [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal).

  
Private access for services  
Private Service Connect published services |  | N/A | 

  * [Published services overview](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#ip-version-translation)
  * [Publish IPv6 services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

  
Private Service Connect endpoints for published services |  | N/A | 

  * [Accessing published services through endpoints overview](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#ip-version-translation)
  * [Access IPv4 and IPv6 published services through IPv6 endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services)

  
Private Service Connect interfaces |  | Dual-stack,  
IPv6-only | 

  * [Private Service Connect interfaces overview](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#specifications)
  * [Create a Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#create)
  * [Create a network attachment with a subnet that has an IPv6 address range](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-subnet)

  
Private Service Connect backends |  | N/A |   
  
1 See the following limitations: 

  * IPv6-only instances support only Debian, Red Hat, and Ubuntu [operating systems](https://docs.cloud.google.com/compute/docs/images/os-details).
  * IPv6-only instances don't support Compute Engine [Internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns).



2 See the limitations for including instances with IPv6 addresses in MIGs in [Basic scenarios for creating MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#ipv6). 

3 VPC Network Peering and Cloud Interconnect VLAN attachments themselves can only be configured as dual-stack and not IPv6-only. However, when configured as dual-stack they are compatible with IPv6-only resources such as subnets and instances. 

4 Cloud DNS doesn't support IPv6 for inbound forwarding. 

5 For NAT64, Cloud NAT supports second generation or earlier VM instances and M3 VM instances. For more information, see [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). 

6 IPv6-only support is limited to instance group backends and protocol forwarding with IPv6-only target instances. 

## Application services

The following table summarizes support for IPv6 in commonly used Google APIs and services.

For services that support private IPv6 access, private access from IPv6 clients is supported by [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

For more information, see Additional details about application services and IPv6.

Service | Public IPv6 access | Private IPv6 access  
---|---|---  
[AlloyDB for PostgreSQL API](https://docs.cloud.google.com/alloydb/docs/reference/rest) |  |   
[AlloyDB for PostgreSQL instances](https://docs.cloud.google.com/alloydb/docs/connection-overview)1 |  |   
[Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/service-apis-overview) |  |   
[BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/rest) |  |   
[Dataflow](https://docs.cloud.google.com/dataflow/docs/reference/rest) |  |   
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/reference/rest) |  |   
[Cloud Deploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest) |  |   
[Firestore](https://docs.cloud.google.com/firestore/docs/reference/rest) |  |   
[Cloud Identity](https://docs.cloud.google.com/identity/docs/reference/rest) |  |   
[Cloud Logging](https://docs.cloud.google.com/logging/docs/reference/v2/rest) |  |   
[Memorystore for Memcached API](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest) |  |   
[Memorystore for Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/connect-memcached-instance)1 |  |   
[Memorystore for Redis API](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest) |  |   
[Memorystore for Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance)1 |  |   
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/api/ref_v3/rest) |  |   
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/reference/rest) |  |   
[Spanner](https://docs.cloud.google.com/spanner/docs/reference/rest) |  |   
[Cloud SQL Admin API for MySQL](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest) |  |   
[Cloud SQL for MySQL instances](https://docs.cloud.google.com/sql/docs/mysql/connect-overview)1 |  |   
[Cloud SQL Admin API for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest) |  |   
[Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/connect-overview)1 |  |   
[Cloud SQL Admin API for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest) |  |   
[Cloud SQL for SQL Server instances](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview)1 |  |   
[Cloud Storage](https://docs.cloud.google.com/storage/docs/json_api/v1) |  |   
[Cloud Tasks](https://docs.cloud.google.com/tasks/docs/reference/rest) |  |   
[Cloud Trace](https://docs.cloud.google.com/trace/docs/reference) |  |   
[Workflows](https://docs.cloud.google.com/workflows/docs/reference/rest) |  |   
[Container Registry / Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/reference/rest) |  |   
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/reference/rest) |  |   
  
1 Some products have an administrative API that runs on Google's production infrastructure and can be accessed by IPv6 clients, but the API creates VPC-hosted resources that can't be accessed by IPv6 clients. For example, Memorystore for Memcached has an administrative API at `memcache.googleapis.com`. Using this API lets you perform some administrative tasks for your Memorystore for Memcached instances, but you must use [private services access](https://docs.cloud.google.com/memorystore/docs/memcached/networking#private_services_access) to access the Memorystore for Memcached instances. 

### Additional details about application services and IPv6

There are two varieties of Google APIs and services:

  * Services that run on Google's production infrastructure, including all `*.googleapis.com` service endpoints.
  * Services that run in VPC networks that are run by Google (also known as _VPC-hosted services_), such as Cloud SQL and Filestore.



Most services that run on Google's production infrastructure support access by clients with IPv6 addresses:

  * Public access from IPv6 clients is supported.

  * Private access from IPv6 clients is supported through the following methods:

    * [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). For more information, including supported services, see [Domain options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options).

    * [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints) for [regional Google APIs](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints). This type of endpoint can be configured with either an IPv4 or IPv6 address—you must configure an IPv6 address to let IPv6 clients use it.

However, you can't use [Private Service Connect endpoints for global Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) to access services from IPv6 clients. This type of endpoint can be configured with an IPv4 address only.




For more information about services that run on Google's infrastructure, see the [Google APIs Explorer](https://developers.google.com/apis-explorer).

For VPC-hosted services, support for access by IPv6 clients depends on the [private access option](https://docs.cloud.google.com/vpc/docs/private-access-options) that you use:

  * You can create IPv6 Private Service Connect endpoints to let clients with IPv6 addresses [access published services](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints).
  * Private services access doesn't support access by clients that have IPv6 addresses. For more information, see the [Supported services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services) in the private services access documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
