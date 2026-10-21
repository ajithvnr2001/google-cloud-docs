---
url: https://docs.cloud.google.com/vpc/docs/quota/
title: Quotas and limits \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:15:56.515794+00:00
---

# Quotas and limits  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Resources ](https://docs.cloud.google.com/vpc/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This document lists the quotas and limits that apply to Virtual Private Cloud (VPC) networking.

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on VPC resources. System limits can't be changed. 

## Quotas

To change a quota, see requesting additional quota.

### Per project

This table highlights important global quotas for VPC resources in each project. For other quotas, see the [**Quotas** page](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console.

To monitor per-project quotas using Cloud Monitoring, set up monitoring for the metric `serviceruntime.googleapis.com/quota/allocation/usage` on the `Consumer Quota` resource type. Set additional label filters (`service`, `quota_metric`) to get to the quota type. For information about monitoring quota metrics, including finding limit names and metric names, see [Use quota metrics](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics). Each quota has a limit and a usage value.

**Note:** You can request an increase for a per-project quota's limit by using the Google Cloud console. If the edit option is not available for a quota, [file a support case](https://cloud.google.com/support-hub) to ask if the quota's limit can be increased.Quota | Description  
---|---  
**Network bandwidth**  
[**GCE VM to internet egress bandwidth Mbps**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/vm_to_internet_egress_bandwidth) | Total egress bandwidth from Google Cloud VMs in one region to [destinations outside of a VPC network](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out-dest-e) (using the default internet gateway). This quota's usage is charged to the project that contains the Compute Engine VMs that emit the packets. Excludes traffic sent to Google APIs and services by using [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). Excludes traffic sent to Google APIs and services from [VMs with external IP addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip).   
[**Inter-region network egress bandwidth (Mbps) from Compute instances**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/inter_region_egress_bandwidth) | Total egress bandwidth from Google Cloud VMs in one region to [destinations that are routable within a VPC network](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out-dest-i) (using next hops that are not the default internet gateway). This quota's usage is charged to the project that contains the Compute Engine VMs that emit the packets.   
**Shared VPC**  
[**Shared VPC service projects per host project**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/xpn_service_projects) | Number of Shared VPC service projects that can be attached to a Shared VPC host project. In addition to this quota, see Shared VPC project limits.  
**General**  
[**Networks**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/networks) | Includes the `default` network, which you can remove.  
[**Policy-based routes**](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/per-project-policy-based-routes) | The number of policy-based routes that you can create in your project.  
[**Routers**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/routers) | The number of Cloud Routers that you can create within your project, in any network and region. Networks also have a _limit_ on the number of Cloud Routers in any given _region_. For details, see [Cloud Router quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas).  
[**Packet Mirrorings**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/packet_mirrorings) | The number of Packet Mirroring policies that you can create in your project, in any network and region.  
**Load balancer and protocol forwarding rules**  
See [Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/quotas#forwarding_rules) in the load balancing quotas documentation.  
**Internal IP addresses**  
[**Internal IP addresses**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/internal_addresses) | The number of static regional internal IPv4 addresses that you can reserve in each region in your project.  
[**Regional static internal IPv6 address ranges**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_static_internal_ipv6_address_ranges) | The number of static regional internal IPv6 address ranges that you can reserve in each region in your project.  
[**Static global internal IPv4 addresses**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_internal_addresses) | The number of static global internal IPv4 address ranges that you can reserve in your project, such as [allocated IPv4 address ranges](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) for private services access and IPv4 addresses reserved for [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#ip-address-requirements) that are used to access global Google APIs. For IP address ranges, each range is a contiguous internal IP address range.  
[**Internal ranges**](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/per-project-internal-ranges) | The number of internal range resources that you can reserve in your project.  
**External IP addresses**  
[**Static IP addresses**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_static_addresses) | The number of static regional external IPv4 addresses that you can reserve in each region in your project.  
[**Regional static external IPv6 address ranges**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_static_external_ipv6_address_ranges) | The number of static regional external IPv6 address ranges that you can reserve in each region in your project.  
[**Static IP addresses global**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_static_addresses) | The number of static global external IP addresses that you can reserve in your project.  
[**In-use IP addresses**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_in_use_addresses) | The number of static and ephemeral regional external IP addresses that you can use in your project simultaneously.  
[**In-use IP addresses global**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_in_use_addresses) | The number of static and ephemeral global external IP addresses that you can use in your project simultaneously.  
[**Address move requests per minute**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/address_move_requests) | The system limit for the global number of address move requests that you can make per minute.  
[**Address move requests per minute per region**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/address_move_requests_per_region) | The system limit for the number of address move requests that you can make per minute per region.  
**Bring your own IP (BYOIP)**  
[ **Static BYOIP IP addresses**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_static_byoip_addresses) | The number of [bring your own IP ](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) regional external IP addresses that you can reserve in each region in your project.

  * Limit name: `STATIC-BYOIP-ADDRESSES-per-project-region`
  * Metric: compute.googleapis.com/regional_static_byoip_addresses

  
[ **Static BYOIP IP addresses global**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_static_byoip_addresses) | The number of [bring your own IP ](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) global external IP addresses that you can create in your project.

  * Limit name: `STATIC-BYOIP-ADDRESSES-per-project`
  * Metric: compute.googleapis.com/global_static_byoip_addresses

  
[**Public advertised prefixes**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/public_advertised_prefixes) | The number of public advertised prefixes (PAPs) that you can create in your project.

  * Limit name: `PUBLIC-ADVERTISED-PREFIXES-per-project`
  * Metric: compute.googleapis.com/public_advertised_prefixes

  
[ **Public V2 advertised prefixes create requests per minute**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=regional_v2_public_advertised_prefixes_create_requests) | The number of create requests for regional public advertised prefixes that you can make per minute. This quota applies to both v1 and v2 public advertised prefixes.

  * Limit name: `PublicAdvertisedPrefixV2CreateRequestsPerMinutePerProject`
  * Metric: compute.googleapis.com/regional_v2_public_advertised_prefixes_create_requests

  
[ **Public V2 advertised prefixes delete requests per minute**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=regional_v2_public_advertised_prefixes_delete_requests) | The number of delete requests for regional public advertised prefixes that you can make per minute. This quota applies to both v1 and v2 public advertised prefixes.

  * Limit name: `PublicAdvertisedPrefixV2DeleteRequestsPerMinutePerProject`
  * Metric: compute.googleapis.com/regional_v2_public_advertised_prefixes_delete_requests

  
[ **Public V2 advertised prefixes announce requests per minute**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=regional_v2_public_advertised_prefixes_announce_requests) | The number of announce requests that you can make per minute for regional public advertised prefixes.

  * Limit name: `PublicAdvertisedPrefixV2AnnounceRequestsPerMinutePerProject`
  * Metric: compute.googleapis.com/regional_v2_public_advertised_prefixes_announce_requests

  
[ **Regional public delegated prefixes**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_public_delegated_prefixes) | The number of regional public delegated prefixes (PDPs) that you can create in each region.

  * Limit name: `PUBLIC-DELEGATED-PREFIXES-per-project-region`
  * Metric: compute.googleapis.com/regional_public_delegated_prefixes

  
[**Global public delegated prefixes**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_public_delegated_prefixes) | The number of global public delegated prefixes that you can create.

  * Limit name: `PUBLIC-DELEGATED-PREFIXES-per-project`
  * Metric: compute.googleapis.com/global_public_delegated_prefixes

  
[ **Regional public delegated prefixes create requests per minute per region**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_public_delegated_prefixes_create_requests_per_region) | The number of create requests for regional public delegated prefixes that you can make per minute per region.

  * Limit name: `PublicDelegatedPrefixCreateRequestsPerMinPerProjectPerRegion`
  * Metric: compute.googleapis.com/regional_public_delegated_prefixes_create_requests_per_region

  
[ **Regional public delegated prefixes delete requests per minute per region**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_public_delegated_prefixes_delete_requests_per_region) | The number of delete requests for regional public delegated prefixes that you can make per minute per region.

  * Limit name: `PublicDelegatedPrefixDeleteRequestsPerMinPerProjectPerRegion`
  * Metric: compute.googleapis.com/regional_public_delegated_prefixes_create_requests_per_region

  
[ **Regional public delegated prefixes announce requests per minute per region**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_public_delegated_prefixes_announce_requests_per_region) | The number of announce requests that you can make per minute per region for regional public delegated prefixes. This quota does not apply to withdraw requests.

  * Limit name: `PublicDelegatedPrefixAnnounceRequestsPerMinPerProjectPerRegion`
  * Metric: compute.googleapis.com/regional_public_delegated_prefixes_announce_requests_per_region

  
[ **Public delegated prefix with variable prefix length**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_variable_prefix_length_public_delegated_prefixes) | The number of regional IPv6 public delegated prefixes that you can create, per project per region.

  * Limit name: `VARIABLE-IPV6-PUBLIC-DELEGATED-PREFIXES-per-project-region`
  * Metric: compute.googleapis.com/regional_variable_prefix_length_public_delegated_prefixes

  
**Private Service Connect**  
[**PSC internal LB forwarding rules**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/psc_internal_lb_forwarding_rules) | The maximum number of Private Service Connect endpoints (forwarding rules) that a service consumer can create to connect to producer services. This quota is per region, per project. Quota name:  
`PSC-INTERNAL-LB-FORWARDING-RULES-per-project-region`  
[**Number of Regional Endpoints per project per region**](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-regional-endpoints) |  The maximum number of Private Service Connect endpoints that a service consumer can create to connect to regional endpoints. This quota is per region, per project. Quota name:  
`RegionalPerProjectRegionalEndpoints`  
[**PSC global GAPI routes per route table**](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/psc_global_gapi_routes_per_route_table) |  The maximum number of Private Service Connect endpoints for global Google APIs that can be propagated to VPC spokes that attach to the same Network Connectivity Center hub ([Preview](https://cloud.google.com/products#product-launch-stages)). Each endpoint that is propagated counts once towards this maximum, regardless of the number of VPC spokes that the endpoint is propagated to. Quota name:  
`PerProjectPerHubPerRouteTablePscGlobalGoogleApiRoutes`  
[**Service attachments**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/service_attachments) | The maximum number of Private Service Connect service attachments that a service producer can create. This quota is per region, per project. Quota name:  
`SERVICE-ATTACHMENTS-per-project-region`  
[**Network attachments**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/network_attachments) | The maximum number of network attachments that a Private Service Connect consumer can create. This quota is per region, per project. Quota name:  
`NETWORK-ATTACHMENTS-per-project-region`  
[**Service Connection Policies per project per region**](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-service-connection-policies) | The maximum number of service connection policies that a service consumer can create. This quota is per region, per project. Quota name:  
`RegionalPerProjectServiceConnectionPolicies`  
[**Service Connection Maps per project per region**](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-service-connection-maps) | The maximum number of service connection maps that a service producer can create. This quota is per region, per project. Quota name:  
`RegionalPerProjectServiceConnectionMaps`  
**Composite Health**  
[**Regional health aggregation policies**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_health_aggregation_policies) | The maximum number of health aggregation policies that you can create in each region of your project. Quota name:  
`REGIONAL-HEALTH-AGGREGATION-POLICIES-per-project-region`  
[**Regional health sources**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_health_sources) | The maximum number of health sources that you can create in each region of your project. Quota name:  
`REGIONAL-HEALTH-SOURCES-per-project-region`  
[**Regional composite health checks**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_composite_health_checks) | The maximum number of composite health checks that you can create in each region of your project. Quota name:  
`REGIONAL-COMPOSITE-HEALTH-CHECKS-per-project-region`  
  
### Per network

This table highlights important network quotas. For other quotas, see the [**Quotas** page](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console.

Information on monitoring the available metrics using Cloud Monitoring is available at [Use quota metrics](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics). Each quota has a limit and a usage value.

**Note:** You can request an increase for a per-network quota's limit by using the Google Cloud console. If the edit option is not available for a quota, [file a support case](https://cloud.google.com/support-hub) to ask if the quota's limit can be increased.

A per-network quota usually has a corresponding per-peering group quota applicable when VPC Network Peering is used. Per-peering group quotas have the concept of an effective limit.

Quota | Description  
---|---  
**Instances & alias IP ranges**  
[**Instances per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/instances_per_vpc_network) | The total number of VM network interfaces (NICs) in the VPC network. Quota name:  
`INSTANCES_PER_NETWORK_GLOBAL` Available metrics:

  * compute.googleapis.com/quota/instances_per_vpc_network/limit
  * compute.googleapis.com/quota/instances_per_vpc_network/usage
  * compute.googleapis.com/quota/instances_per_vpc_network/exceeded

  
[ **IP aliases per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/ip_aliases_per_vpc_network) | The total number of [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) used by VM network interfaces (NICs) in the VPC network. This quota counts the number of alias IP ranges without regard to each range's size (subnet mask). In addition to this quota, there is a limit on the number of alias IP ranges per network interface.  Quota name:  
`ALIASES_PER_NETWORK_GLOBAL` Available metrics:

  * compute.googleapis.com/quota/ip_aliases_per_vpc_network/limit
  * compute.googleapis.com/quota/ip_aliases_per_vpc_network/usage
  * compute.googleapis.com/quota/ip_aliases_per_vpc_network/exceeded

  
**Subnet IP address ranges**  
[**Subnetwork ranges per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/subnet_ranges_per_vpc_network) | The total number of [subnet IP address ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges) used by subnets in the VPC network. Includes primary IPv4 address ranges, secondary IPv4 address ranges, and IPv6 address ranges. Quota name:  
`SUBNET_RANGES_PER_NETWORK` Available metrics:

  * compute.googleapis.com/quota/subnet_ranges_per_vpc_network/limit
  * compute.googleapis.com/quota/subnet_ranges_per_vpc_network/usage
  * compute.googleapis.com/quota/subnet_ranges_per_vpc_network/exceeded

  
[**Subnetwork ranges per peering group**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/subnet_ranges_per_peering_group) | From the perspective of a VPC network, the total number of [ subnet IP address ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges) used by subnets local to the VPC network and in its directly connected peers. Includes primary IPv4 address ranges, secondary IPv4 address ranges, and IPv6 address ranges. Quota name:  
`SUBNET_RANGES_PEERING_GROUP` Available metrics:

  * compute.googleapis.com/quota/subnet_ranges_per_peering_group/limit
  * compute.googleapis.com/quota/subnet_ranges_per_peering_group/usage

  
**VPC Network Peering**  
[**Peerings per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/peerings_per_vpc_network) | From the perspective of a VPC network, the total number of other VPC networks it can connect to by using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). Quota name:  
`PEERINGS_PER_NETWORK` Available metrics:

  * compute.googleapis.com/quota/peerings_per_network/limit
  * compute.googleapis.com/quota/peerings_per_network/usage
  * compute.googleapis.com/quota/peerings_per_network/exceeded

  
**Static and dynamic routes**  
[**Static routes per network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/static_routes_per_vpc_network) | From the perspective of all regions of a VPC network, the total number of [static routes](https://docs.cloud.google.com/vpc/docs/static-routes) local to the VPC network. This quota applies to the aggregate of IPv4 and IPv6 static routes.  Quota name:  
`STATIC_ROUTES_PER_NETWORK` Available metrics:

  * compute.googleapis.com/quota/static_routes_per_vpc_network/limit
  * compute.googleapis.com/quota/static_routes_per_vpc_network/usage
  * compute.googleapis.com/quota/static_routes_per_vpc_network/exceeded

  
[**Static routes per peering group**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/static_routes_per_peering_group) | From the perspective of all regions of a VPC network, the total number of [static routes](https://docs.cloud.google.com/vpc/docs/static-routes) local to the VPC network and in its directly connected peers. This quota applies to the aggregate of IPv4 and IPv6 static routes.  Quota name:  
`STATIC_ROUTES_PER_PEERING_GROUP` Available metrics:

  * compute.googleapis.com/quota/static_routes_per_peering_group/limit
  * compute.googleapis.com/quota/static_routes_per_peering_group/usage

  
[**Dynamic routes per region per peering group**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/dynamic_routes_per_region_per_peering_group) | From the perspective of _each region_ in a VPC network, the total number of [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) local to the VPC network and in its directly connected peers. This quota applies to the aggregate of IPv4 and IPv6 dynamic routes. Quota name:  
`DYNAMIC_ROUTES_PER_REGION_PER_PEERING_GROUP` Available metrics:

  * compute.googleapis.com/quota/dynamic_routes_per_region_per_peering_group/limit
  * compute.googleapis.com/quota/dynamic_routes_per_region_per_peering_group/usage

If the number of dynamic routes exceeds this limit, Google Cloud adjusts how it imports dynamic routes according to the following rules:

  * Google Cloud _only drops peering dynamic routes_. Google Cloud uses an internal algorithm when dropping peering dynamic routes; you can't predict _which_ peering dynamic routes are dropped.
  * Subject to [Cloud Router limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits), Google Cloud never drops local dynamic routes (those routes learned by Cloud Router that are local to the VPC network itself).
  * If a peering connection causes this limit to be exceeded, Google Cloud still lets you create the peering connection without a warning.

  
**Load balancer and protocol forwarding rules**  
See [Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/quotas#forwarding_rules) in the load balancing quotas documentation.  
**Private Service Connect**  
[ **PSC Google APIs forwarding rules per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=psc_google_apis_forwarding_rules_per_vpc_network) | The maximum number of Private Service Connect endpoints (forwarding rules) that can be used to access global Google APIs. This quota applies to the _total_ number of forwarding rules used to access global Google APIs in all regions. This quota can't be increased. See per project for additional important details about how many global internal addresses you can create. Quota name:  
`PSC_GOOGLE_APIS_FORWARDING_RULES_PER_NETWORK` Available metrics:

  * compute.googleapis.com/quota/psc_google_apis_forwarding_rules_per_vpc_network/limit
  * compute.googleapis.com/quota/psc_google_apis_forwarding_rules_per_vpc_network/usage
  * compute.googleapis.com/quota/psc_google_apis_forwarding_rules_per_vpc_network/exceeded

  
[ **PSC propagated connections per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=psc_propagated_connections_per_vpc_network) |  The maximum number of Private Service Connect [propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) for published services and regional Google APIs that can exist in a consumer's [VPC network](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-spokes).  This quota can't be increased.  Quota name: `PSC_PROPAGATED_CONNECTIONS_PER_VPC_NETWORK` Available metrics:

  * compute.googleapis.com/quota/psc_propagated_connections_per_vpc_network/limit
  * compute.googleapis.com/quota/psc_propagated_connections_per_vpc_network/usage
  * compute.googleapis.com/quota/psc_propagated_connections_per_vpc_network/exceeded

  
[**PSC ILB consumer forwarding rules per producer VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=psc_ilb_consumer_forwarding_rules_per_producer_vpc_network) |  The maximum number of Private Service Connect [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) and [propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) that can access a service producer VPC network.  This quota applies to the _total_ number of endpoints and propagated connections that access services in all regions of the service producer VPC network.  Endpoints contribute to this quota until they are deleted, even if the associated service attachment is deleted or configured to reject the connection. Propagated connections contribute to this quota until the associated endpoint is deleted, even if connection propagation is disabled on the hub or the propagated connection's spoke is deleted.  Quota name:  
`PSC_ILB_CONSUMER_FORWARDING_RULES_PER_PRODUCER_NETWORK` Available metrics:

  * compute.googleapis.com/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/limit
  * compute.googleapis.com/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/usage
  * compute.googleapis.com/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/exceeded

  
  
### Deprecated quotas

Google Cloud no longer enforces the following quotas:

  * [Subnetworks](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/subnetworks): The Subnetwork ranges per VPC network quota is the replacement.

  * [Routes](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/routes): The Static routes per network quota is the replacement.

  * [Instances per peering group](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/instances_per_peering_group): Instead, Google Cloud enforces the Instances per VPC network quota in each VPC network.

  * [IP aliases per peering group](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/ip_aliases_per_peering_group): Instead, Google Cloud enforces the IP aliases per VPC network quota in each VPC network.




## Limits

Limits can't generally be increased unless specifically noted.

### Shared VPC limits

The number of service projects that can be attached to a host project is a configurable per-project quota. In addition to that quota, the following limits apply to [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

Item | Limit | Notes  
---|---|---  
Number of Shared VPC host projects in a single organization | 100 | To request an update to this limit, [file a support case](https://cloud.google.com/support-hub).  
Number of host projects to which a service project can attach | 1 | This limit can't be increased.  
  
### Per network

The following limits apply to VPC networks. These limits are enforced by using quotas internally. When per-network limits are exceeded, you see `QUOTA_EXCEEDED` errors with the internal quota names.

Item | Limit | Notes  
---|---|---  
**Subnet IP ranges**  
Primary IP ranges per subnet | 1 | IPv4-only and dual-stack subnets must have exactly one primary IPv4 range (CIDR block). This limit can't be increased. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).  
Maximum number of secondary IP ranges per subnet | 170 | IPv4-only and dual-stack subnets can optionally have subnet secondary IPv4 address ranges. This limit can't be increased. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).  
**Routes**  
Maximum number of network tags per route | 256 | The maximum number of network tags that you can associate with a static route. This limit can't be increased.  
  
### IP address limits

Item | Limit | Notes  
---|---|---  
Public delegated prefixes per public advertised prefix  |  10  |  The number of public delegated prefixes (PDPs) that you can create from a public advertised prefix (PAP).   
Allocated IP address ranges per private connection  |  5,000  |  The maximum number of IP address ranges that you can associate with a [private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).   
  
### Per instance

The following limits apply to VM instances. Unless otherwise noted, these limits _can't_ be increased. For _quotas_ relevant to VMs, see [Compute Engine quotas](https://docs.cloud.google.com/compute/quotas#understanding_quotas).

Item | Limit | Notes  
---|---|---  
Maximum Transmission Unit (MTU) | Between 1,300 bytes and 8,896 bytes (inclusive). Common values include 1460 bytes (default), 1500 bytes (standard Ethernet), and 8896 bytes (jumbo frames). | For more information, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).  
Maximum number of network interfaces | Depends on the machine type of the VM | See [Maximum number of network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces).  
Maximum number of alias IP ranges per network interface | 150 | The number of alias IP ranges that you can assign to a network interface as long as you don't exceed the quota for the total number of assigned alias IP ranges in the VPC network. Google Cloud does _not_ consider the _size_ of the alias IP range's netmask. For example, an individual `/24` range is a single alias IP range and an individual `/23` range is also a single alias IP range.  
Network interfaces per VPC network | 1 | Each network interface must be connected to a unique VPC network. An instance can only have one network interface in a given VPC network.  
Maximum duration for idle TCP connections | 10 minutes | VPC networks automatically drop idle TCP connections after ten minutes. You can't change this limit, but you can use [TCP keepalives](https://en.wikipedia.org/wiki/Keepalive) to prevent connections to instances from becoming idle. For details, see [ Compute Engine tips and troubleshooting](https://docs.cloud.google.com/compute/docs/troubleshooting#communicatewithinternet).  
Maximum egress data rate to an internal IP address destination | Depends on the machine type of the VM  | See [ Egress to internal IP address destinations](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out-dest-i) and [machine types](https://docs.cloud.google.com/compute/docs/machine-types) in the Compute Engine documentation.   
Maximum egress data rate to an external IP address destination | all flows: about 7 Gbps (gigabits per second) sustained or 25 Gbps with per VM Tier_1 networking performance single flow: 3 Gbps sustained | See [ Egress to external IP address destinations](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out-dest-e) in the Compute Engine documentation.   
Maximum ingress data rate to an internal IP address destination | No artificial limit | See [ Ingress to internal IP address destinations](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-in-dest-i) in the Compute Engine documentation.   
Maximum ingress data rate to an external IP address destination | no more than 30 Gbps no more than 1,800,000 packets per second | See [ Ingress to external IP address destinations](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-in-dest-e) in the Compute Engine documentation.   
  
### Connection logging limits

The maximum number of connections that can be logged per VM instance depends on its [machine type](https://docs.cloud.google.com/compute/docs/machine-types). Connection logging limits are expressed as the maximum number of connections that can be logged in a five-second interval.

**Important:** Firewall log entries are created on a best effort basis according to the following table. It is possible for entries to not be logged during periods of heavy traffic, even if the maximum number of logged connections for a machine type has not been reached.Instance machine type | Maximum number of connections logged in a 5-second interval  
---|---  
f1-micro | 100 connections  
g1-small | 250 connections  
Machine types with 1–8 vCPUs | 500 connections per vCPU  
Machine types with more than 8 vCPUs | 4,000 (500×8) connections  
  
### Hybrid connectivity

Use the following links to find quotas and limits for Cloud VPN, Cloud Interconnect, and Cloud Router:

  * [Cloud VPN quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas)
  * [Cloud Interconnect quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas)
  * [Cloud Router quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas)



## Effective limits for per-peering group quotas

Each per-peering group quota has the concept of an _effective limit_. This section describes how the quota's effective limit is calculated. The effective limit is always greater than or equal to the value of the per-peering group quota's limit.

Most per-peering group quotas have a corresponding network quota—for example, `SUBNET_RANGES_PER_PEERING_GROUP` and `SUBNET_RANGES_PER_NETWORK`. The effective limit calculation described in this section applies to all per-peering group quotas, even those that don't have a corresponding per-network quota.

A per-peering group quota's effective limit is calculated in the following way:

  * **Step 1**. Select a VPC network. When VPC Network Peering is used, each network has its own peering group. A network's peering group consists of the VPC network itself and all other VPC networks that are directly connected to it through VPC Network Peering. Effective limit calculations are repeated for each per-peering group quota _on a network by network basis_.

  * **Step 2**. For the selected VPC network, find the _greater_ of these limits:

    * the limit for the per-peering group quota
    * the limit for the corresponding per-network quota

If no corresponding per-network quota exists, use the per-peering group quota's limit.

  * **Step 3**. Create a list consisting of the _greater_ of these two limits in each peer network:

    * the limit for the per-peering group quota
    * the limit for the corresponding per-network quota

If no corresponding per-network quota exists, use the per-peering group quota's limit.

  * **Step 4**. Find the _smallest value_ from the list created by Step 3.

  * **Step 5**. Take the _greater_ of the two values from Step 2 and Step 4. This number is the _effective limit_ for the per-peering group quota from the perspective of the selected VPC network.




### Effective limits example

Suppose that you have four VPC networks, `network-a`, `network-b`, `network-c`, and `network-d`. Because there are four VPC networks, there are also four peering groups, one from the perspective of each network.

Suppose the network peering connections are as follows:

  * `network-a` is peered with `network-b`, and `network-b` is peered with `network-a`
  * `network-a` is peered with `network-c`, and `network-c` is peered with `network-a`
  * `network-c` is peered with `network-d`, and `network-d` is peered with `network-c`



Suppose the limits for two corresponding quotas are set as follows:

Network | Limit for `INTERNAL_FORWARDING_RULES_PER_PEERING_GROUP` | Limit for `INTERNAL_FORWARDING_RULES_PER_NETWORK`  
---|---|---  
`network-a` | 500 | 600  
`network-b` | 350 | 300  
`network-c` | 300 | 300  
`network-d` | 400 | 300  
  
The effective limits for each `INTERNAL_FORWARDING_RULES_PER_PEERING_GROUP` quota are as follows:

  * Peering group for `network-a`—direct peers are `network-b` and `network-c`.

    1. In `network-a`: `max(500,600) = 600`
    2. List of maxima for direct peers: 
       * `network-b`: `max(350,300) = 350`
       * `network-c`: `max(300,300) = 300`
    3. Minimum of the list of direct peers: `min(350,300) = 300`
    4. Effective limit for `INTERNAL_FORWARDING_RULES_PER_PEERING_GROUP` in `network-a`: `max(600,300) = 600`
  * Peering group for `network-b`—one direct peer, `network-a`.

    1. In `network-b`: `max(350,300) = 350`
    2. List of maxima for direct peers: 
       * `network-a`: `max(500,600) = 600`
    3. Minimum of the list of direct peers: `min(600) = 600`
    4. Effective limit for `INTERNAL_FORWARDING_RULES_PER_PEERING_GROUP` in `network-b`: `max(350,600) = 600`
  * Peering group for `network-c`—direct peers are `network-a` and `network-d`.

    1. In `network-c`: `max(300,300) = 300`
    2. List of maxima for direct peers: 
       * `network-a`: `max(500,600) = 600`
       * `network-d`: `max(400,300) = 400`
    3. Minimum of the list of direct peers: `min(600,400) = 400`
    4. Effective limit for `INTERNAL_FORWARDING_RULES_PER_PEERING_GROUP` in `network-c`: `max(300,400) = 400`
  * Peering group for `network-d`—one direct peer, `network-c`.

    1. In `network-d`: `max(400,300) = 400`
    2. List of maxima for direct peers: 
       * `network-c`: `max(300,300) = 300`
    3. Minimum of the list of direct peers: `min(300) = 300`
    4. Effective limit for `INTERNAL_FORWARDING_RULES_PER_PEERING_GROUP` in `network-d`: `max(400,300) = 400`



## Manage quotas

Virtual Private Cloud enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

All projects start with the same quotas, which you can change by requesting additional quota. Some quotas might increase automatically based on your use of a product.

### Permissions

To view quotas or request quota increases, Identity and Access Management (IAM) principals need one of the following roles. 

Task | Required role  
---|---  
Check quotas for a project | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaViewer`)

  
Modify quotas, request additional quota | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaAdmin`)
  * A custom role with the `serviceusage.quotas.update` permission

  
  
### Check your quota

### Console

  1. In the Google Cloud console, go to the **Quotas** page. 

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. To search for the quota that you want to update, use the **Filter table**. If you don't know the name of the quota, use the links on this page instead.



### gcloud

Using the Google Cloud CLI, run the following command to check your quotas. Replace `PROJECT_ID` with your own project ID.
    
    
        gcloud compute project-info describe --project PROJECT_ID

To check your used quota in a region, run the following command:
    
    
        gcloud compute regions describe example-region
        

### Errors when exceeding your quota

If you exceed a quota with a `gcloud` command, `gcloud` outputs a `quota exceeded` error message and returns with the exit code `1`.

If you exceed a quota with an API request, Google Cloud returns the following HTTP status code: `413 Request Entity Too Large`. 

### Request additional quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

### Resource availability

Each quota represents a maximum number for a particular type of resource that you can create, if that resource is available. It's important to note that quotas _don't_ guarantee resource availability. Even if you have available quota, you can't create a new resource if it is not available.

For example, you might have sufficient quota to create a new regional, external IP address in a given region. However, that is not possible if there are no available external IP addresses in that region. Zonal resource availability can also affect your ability to create a new resource.

Situations where resources are unavailable in an entire region are rare. However, resources within a zone can be depleted from time to time, typically without impact to the service level agreement (SLA) for the type of resource. For more information, review the relevant SLA for the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
