---
url: https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview/
title: Outbound Endpoints overview \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:42:42.813680+00:00
---

# Outbound Endpoints overview  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Outbound Endpoints overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides an overview of Cloud DNS Outbound Endpoints. Outbound Endpoints can be attached to forwarding zones or server policies to enable direct DNS query forwarding from VPC networks to external and on-premises DNS resolvers by using private IP addresses. Using Outbound Endpoints provides granular control over outbound DNS traffic and enhances your ability to unblock Hybrid and Multi-cloud DNS resolution use cases.

To learn how to create, update, and associate Outbound Endpoints with forwarding zones or server policies, see [Create and update Outbound Endpoints](https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints).

## Outbound Endpoints capabilities

Outbound Endpoints let you control the source IP addresses for outbound DNS traffic, enabling VPC network specific behavior by assigning a unique egress range for each network. The unique egress range overcomes the routing limitations of the [existing fixed forwarding proxy range](https://cloud.google.com/blog/products/networking/cloud-forwarding-peering-and-zones).

GKE clusters automatically inherit Outbound Endpoints when querying external destinations with the host VPC network. If the host VPC network is authorized for a standard global Cloud DNS forwarding zone or server policy configured with Outbound Endpoints, pods using VPC DNS resolution automatically route outbound queries through regional Outbound Endpoints without requiring cluster-level modifications or zonal forwarding zones.

To learn more about migrating your existing DNS forwarding setup to Outbound Endpoints, see [Migrate an existing Cloud DNS forwarding setup to Outbound Endpoints](https://docs.cloud.google.com/dns/docs/migrate-existing-dns-setup).

## Outbound Endpoints architecture and query routing

An Outbound Endpoint is created within a specific VPC network and uses that network's [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) for its source IP address.

When you attach Outbound Endpoints to your forwarding zones or server policy, Cloud DNS first attempts to route DNS queries through the highest-ranked Outbound Endpoint by using the existing target ranking algorithm. If that endpoint is unhealthy, Cloud DNS tries the next highest-ranked endpoint. The geographically closest Outbound Endpoint is preferred but not guaranteed.

The ranking algorithm for destination servers is automatically performed and is based on the existing forwarding zones failover pattern - [lowest latency and error rate IP selection](https://docs.cloud.google.com/dns/docs/zones/zones-overview#fz-target-selection). The following factors increase the ranking of a forwarding target:

  * Higher number of successful DNS responses processed by the forwarding target. Successful DNS responses also include `NXDOMAIN` responses.
  * Lower latency for communicating with the forwarding target.
  * Shorter geographic distance to the Outbound Endpoint. If success and latency data are unavailable, the closest target is preferred.



For protection against regional outages, you can configure Outbound Endpoints in at least two regions where you run compute workloads. This approach provides Cloud DNS a regional failover target and maintains minimal query latency. If your hybrid connectivity is only provisioned in select regions, endpoints in other compute regions can still route through those connections to reach your on-premises resolvers.

Even if the highest ranked endpoint is in a different region, Cloud DNS continues to route queries to that endpoint. For example, if an endpoint in Region A becomes unavailable, traffic is automatically routed to a healthy endpoint in Region B. When the endpoint in Region A is healthy again, the ranking algorithm will detect its improved performance and start preferring it again for upcoming queries.

You can have up to 10 Outbound Endpoints per project per region but you can request a quota increase in the Google Cloud console if needed. There can be up to 100 Outbound Endpoints attached to a forwarding zone or server policy.

### Route queries to regional on-premises resolvers

Cloud DNS doesn't guarantee that traffic is sent to the endpoint in the same region as the originating VM, but you can use [Geolocation routing policies](https://docs.cloud.google.com/dns/docs/routing-policies-overview#geolocation-policy) to route traffic to the nearest target name server. Although Cloud DNS preferentially routes traffic towards the Outbound Endpoint in the region closest to the originating query and target name server, the target name server's region and Outbound Endpoint region aren't tightly coupled. Regardless of location, Cloud DNS chooses the endpoint that historically has provided the lowest latency.

The following provides a high-level overview of what you need to do to route queries to regional on-premises resolvers:

  * **Create a zone with a geolocation policy** : Create a new Cloud DNS private zone for an FQDN you control (for example, `onprem-resolvers.example.com`) authorized for your VPC network. In this zone, create `A` records for your on-premises DNS server IPs and apply a Geolocation routing policy. Configure the policy to return resolver IPs for queries sourced from that specific region. For example, return European resolver IPs for queries sourced from European Google Cloud regions.
  * **Use the FQDN as the forwarding target** : In your forwarding zone, use the FQDN you just created (`onprem-resolvers.example.com`) as the destination DNS server.
  * **Configure Outbound Endpoints** : Associate your regional Outbound Endpoints (for example, one in a US region and one in a European region) with this forwarding zone.



When a VM in one region makes a query, the system follows a two-step routing process:

  * **Endpoint selection** : Cloud DNS evaluates the list of Outbound Endpoints associated with the forwarding zone and selects the best endpoint (for example, an endpoint in Europe is likely chosen for a query from a VM in Europe).
  * **Destination resolution** : The selected Outbound Endpoint resolves the destination FQDN (`onprem-resolvers.example.com`). As the Outbound Endpoint is a regional resource located in the specified region, the Geolocation policy identifies the query's source as that region and returns the specific IP address you have configured for that region. The Outbound Endpoint then forwards the original query to the target DNS server IP.



For more information, see the [Cloud DNS FQDN outbound DNS forwarding tutorial](https://codelabs.developers.google.com/codelabs/cloud-dns-fqdn-outbound-forwarding#1).

### Forwarding from a region without a local endpoint in a single VPC network

A Google Cloud VPC network is a global resource that can contain subnets in multiple regions. If a VM makes a query from a region where you haven't configured an Outbound Endpoint, forwarding will still succeed. The query will be routed across regions to the highest-ranked available Outbound Endpoint which exists within the same VPC network and is configured in the forwarding zone or server policy.

### Forwarding from multiple VPC networks in the same region with source IP isolation

If you need to forward queries from multiple VPC networks in the same region and require the on-premises resolver to see a distinct source IP address for each VPC network, follow these steps:

  1. **Create an Outbound Endpoint in each VPC network** : For more information, see [Create an Outbound Endpoint](https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints#create-outbound-endpoint).
  2. **Create a forwarding zone or server policy in each VPC network** : Authorize the forwarding zone or server policy for only that VPC network and only use that VPC network's Outbound Endpoint.



This action results in VMs in each VPC network sending queries through the Outbound Endpoint in their VPC network. Each endpoint forwards the query to the on-premises resolver. The on-premises network sees the source IP address of each VPC network's proxy-only subnet, allowing it to apply different configurations for each network's traffic.

### Unified forwarding across different VPC networks (Hub-and-Spoke)

You can configure a forwarding zone or server policy to use an Outbound Endpoint in a different, centralized VPC network (the hub). Network connectivity isn't necessary between the hub network and the VPC network where the query originates (the spoke) as Cloud DNS handles the query forwarding internally.

You must configure network connectivity between the Outbound Endpoint and the forwarding targets in your forwarding zone or server policy. Connectivity can be established using Cloud Interconnect or Cloud VPN to reach on-premises resolvers. VPC Network Peering can be used to reach forwarding targets in another VPC network.

  1. Create an Outbound Endpoint in the hub VPC network.
  2. Create a forwarding zone or server policy in the spoke VPC network and configure it to use the hub network's Outbound Endpoint.



The VMs in the spoke VPC networks send queries through the Outbound Endpoint in the hub VPC network. The endpoint forwards the query to the on-premises resolver.

#### Shared VPC support

Outbound Endpoints support Shared VPC deployments. The endpoint and its associated proxy-only subnet are created centrally in the host project. Service projects can then create private forwarding zones or server policies and bind them cross-project to the centralized Outbound Endpoint in the host project (requiring `dns.outboundEndpoints.bindPrivateDNSZone` or `dns.outboundEndpoints.bindPrivateDNSPolicy` on the host project).

### Manage network resources associated with Outbound Endpoints

Cloud DNS Outbound Endpoints enforce strict lifecycle dependencies with their underlying VPC networks and subnets to help protect production DNS traffic from accidental infrastructure changes like deletions or modifications.

#### Delete proxy-only subnet or VPC network when in use by an Outbound Endpoint

A proxy-only subnet or VPC network actively in use by an Outbound Endpoint is protected from deletion to prevent outages. Attempting to delete these resources results in an error. If you want to delete these resources, you must follow these steps in the exact order:

  1. **Update Cloud DNS configuration** : Edit any forwarding zones or server policies that use the Outbound Endpoint and remove it from the configuration so it is no longer in use.
  2. **Delete the Outbound Endpoint** : After the endpoint is no longer in use, you can delete it. This action releases the dependency on the proxy-only subnet.
  3. **Delete the proxy-only subnet** : After confirming no other resources are using it, delete the proxy-only subnet.
  4. **Delete the VPC network** : Once all other VPC dependencies are removed, you can delete the VPC network.



#### Subnet modification

You can't directly modify a proxy-only subnet when an Outbound Endpoint is actively using it. This restriction prevents you from editing key properties, such as the IP address range, which helps avoid service outages. To modify the subnet, you must follow [existing guidelines](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#proxy_only_subnet_change) and first migrate to a new subnet.

Do the following to modify a subnet that is being used by an Outbound Endpoint:

  1. **Create a backup subnet** : Create a new proxy-only subnet in the same VPC network and region. You must set this subnet's role to `BACKUP` during creation.
  2. **Activate the new subnet** : Update the new subnet's role to `ACTIVE`. Doing so automatically sets the original subnet to the `BACKUP` role and starts draining active connections from it.
  3. **Wait for draining** : Allow time for the connection draining process to complete.
  4. **Delete the old subnet** : You can now delete the original subnet once it's in the `BACKUP` role and has no active connections.



## Dedicated source IP predictability for on-premises firewalls

If your on-premises DNS firewalls require a dedicated and predictable source IP address range isolated to DNS traffic, we recommend that you apply the following architecture:

  * **Deploy in a dedicated egress VPC network** : Create a dedicated VPC network with a regular subnet (for the Outbound Endpoint IP address) and a regional proxy-only subnet reserved exclusively for Cloud DNS (`--purpose=REGIONAL_MANAGED_PROXY` and `--role=ACTIVE`).
  * **Isolate your application VPC networks:** Do not peer or route your application VPC networks to this dedicated egress network. Cloud DNS routes queries internally within the Google Cloud infrastructure, so direct network connectivity between these VPC networks is not required.
  * **Connect the dedicated egress VPC network to external forwarding targets** : Configure connectivity only between the dedicated egress VPC network and your external or on-premises target name servers. Establish this path by using the following: 
    * **VPC network peering to an existing transit VPC** : This is the recommended approach and the most cost effective. If your organization already has a central transit VPC network with Cloud Interconnect or Cloud VPN to on-premises, peer the dedicated DNS VPC network to that transit hub. This approach avoids provisioning redundant hybrid circuits and minimizes costs.
    * **Direct hybrid connectivity** : Dedicated Interconnect, Cross-Cloud Interconnect, or Cloud VPN that terminates directly in the dedicated DNS VPC network.



## Limitations

Outbound Endpoints have the following limitations:

  * **Source IP and subnet sharing limited to resources in the same region** : Outbound Endpoints allocate source IP ranges from the regional proxy-only subnet of the VPC network they are attached to. In standard deployments, this proxy-only subnet can be shared with other regional resources like Regional Application Load Balancers.

  * **Direct peering to proxy-only subnets isn't supported** : You can't directly peer with a proxy-only subnet. Network connectivity to external name servers must be established through standard VPC routing like Cloud Interconnect, Cloud VPN, or VPC Network Peering.

  * **IPv4 support only** : The source IP address of an Outbound Endpoint is IPv4-only, and queries can only be forwarded to IPv4 targets or FQDN forwarding targets on forwarding zones that resolve to IPv4 addresses.

  * **Binding Outbound Endpoints to a network across projects is unsupported** : Creating an Outbound Endpoint in a service project attached to a host project's shared VPC network is not supported. Outbound Endpoints must reside in the same project as the VPC network and subnet they attach to.

  * **Limited to private targets** : Outbound Endpoints only support forwarding to [private targets](https://docs.cloud.google.com/dns/docs/zones/zones-overview#fz-targets) and can't be used as an egress proxy or static source IP anchor for public internet DNS traffic. Queries to public internet targets resolve directly through Google's distributed anycast edge to minimize latency and avoid Cloud NAT dependencies.

  * **Regional scope** : Outbound Endpoints are regional resources. You must create endpoints in each region you intend to use them in.

  * **Single forwarding mechanism only** : Your forwarding mechanism (either the default `35.199.192.0/19` range or Outbound Endpoints) is configured at the forwarding zone or server policy level. However, you can't use both methods simultaneously for the same zone or policy.




## What's next

  * For more information on Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
  * For information on creating or updating Outbound Endpoints, see [Create or update Outbound Endpoints](https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints).
  * For troubleshooting information, see [Troubleshoot Cloud DNS Outbound Endpoints](https://docs.cloud.google.com/dns/docs/troubleshooting#outbound-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
