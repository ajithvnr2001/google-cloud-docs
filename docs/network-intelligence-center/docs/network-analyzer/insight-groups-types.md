---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types/
title: Insight groups and types \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:24.280625+00:00
---

# Insight groups and types  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Insight groups and types Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Network Analyzer insight groups and their corresponding insight types.

The results from Network Analyzer analyses are known as _insights_. An insight can include one of the following outcomes from an analysis:

  * A network failure, such as a service connectivity blockage caused by configuration issues.
  * A suboptimal configuration, such as reserved but unassigned IP addresses, or dynamic routes that overlap with static or subnet routes.
  * A preventive warning, such as IP utilization above 75 percent for a subnet range.
  * A summary of status, such as the list of reserved but unallocated IP addresses distributed by region or service projects.



## Supported insight types

In addition to the Network Analyzer pages, insights are published as the following insight types:

  * **Recommender insight types.** To request a list of insights or to list insight details, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api). To view all Recommender insight types, see [Recommender insight types](https://docs.cloud.google.com/recommender/docs/insights/insight-types).
  * **Cloud Logging insight types.** For details, see the [`analyzer_log.proto` on GitHub](https://github.com/googleapis/googleapis/blob/master/google/cloud/networkanalyzer/logging/v1/analyzer_log.proto).



Each of the following sections provides links to the Network Analyzer insight types. Each section also includes a table that shows the supported Recommender insight type and subtypes and the Cloud Logging insight types.

## VPC network insights

VPC network insights cover basic VPC network setup and configuration issues, such as issues with IP addresses, routes, firewall rules, VPC Network Peering, and Shared VPC.

### Routes with an invalid next hop

For details about this insight type, see [Insights about routes with an invalid next hop](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/route-invalid-next-hop).

For the related Recommender and Cloud Logging insight types, see the following table.

Recommender insight type and subtypes | Cloud Logging insight types  
---|---  
`google.networkanalyzer.vpcnetwork.connectivityInsight`

  * `ROUTE_NEXT_HOP_VM_IP_FORWARDING_DISABLED`
  * `ROUTE_NEXT_HOP_VM_STOPPED`
  * `ROUTE_NEXT_HOP_VM_DELETED`
  * `ROUTE_NEXT_HOP_ILB_MISCONFIGURED`
  * `ROUTE_NEXT_HOP_VPN_TUNNEL_DELETED`
  * `ROUTE_NEXT_HOP_ILB_VIP_NOT_ASSIGNED`
  * `ROUTE_NEXT_HOP_VM_WRONG_NETWORK`
  * `ROUTE_NEXT_HOP_VM_NON_PRIMARY_IP`
  * `ROUTE_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH`
  * `ROUTE_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID`

|  `ROUTE_INVALID_NEXT_HOP_VM_IP_FORWARDING_DISABLED` `ROUTE_INVALID_NEXT_HOP_VM_DELETED` `ROUTE_INVALID_NEXT_HOP_VM_STOPPED` `ROUTE_INVALID_NEXT_HOP_ILB_MISCONFIGURED` `ROUTE_INVALID_NEXT_HOP_VPN_TUNNEL_DELETED` `ROUTE_INVALID_NEXT_HOP_ILB_VIP_NOT_ASSIGNED` `ROUTE_INVALID_NEXT_HOP_VM_WRONG_NETWORK` `ROUTE_INVALID_NEXT_HOP_VM_NON_PRIMARY_IP` `ROUTE_INVALID_NEXT_HOP_VPN_TUNNEL_NOT_ESTABLISHED` `ROUTE_INVALID_NEXT_HOP_IP_NOT_ASSIGNED` `ROUTE_INVALID_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH` `ROUTE_INVALID_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID`  
  
### IP addresses

For details about this insight type, see the following:

  * [IP address utilization insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/ip-utilization)
  * [Unused IP address insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/unused-ip-address)



For the related Recommender and Cloud Logging insight types, see the following table.

Recommender insight type and subtypes | Cloud Logging insight types  
---|---  
`google.networkanalyzer.vpcnetwork.ipAddressInsight`

  * `PRIMARY_IP_RANGE_UTILIZATION_HIGH`
  * `SECONDARY_IP_RANGE_UTILIZATION_HIGH`
  * `EXTERNAL_IP_UNASSIGNED`
  * `IP_UTILIZATION_SUMMARY`
  * `PSA_IP_UTILIZATION_SUMMARY`

|  `IP_UTILIZATION_IP_ALLOCATION_RATIO_HIGH` `IP_UTILIZATION_IP_ALLOCATION_SUMMARY`  
  
## Network services insights

Network services insights cover issues that you might encounter when using load balancers and Cloud NAT.

### Load balancer

For details about this insight type, see [Load balancer insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/load-balancer).

For the related Recommender and Cloud Logging insight types, see the following table.

Recommender insight type and subtypes | Cloud Logging insight types  
---|---  
`google.networkanalyzer.networkservices.loadBalancerInsight`

  * `HEALTH_CHECK_FIREWALL_NOT_CONFIGURED`
  * `HEALTH_CHECK_FIREWALL_FULLY_BLOCKING`
  * `HEALTH_CHECK_FIREWALL_PARTIALLY_BLOCKING`
  * `HEALTH_CHECK_FIREWALL_INCONSISTENT`
  * `HEALTH_CHECK_PORT_MISMATCH`
  * `BALANCING_MODE_BREAKS_SESSION_AFFINITY`

|  `LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_FIREWALL_NOT_CONFIGURED` `LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_RANGE_BLOCKED` `LOAD_BALANCER_HEALTH_CHECK_FIREWALL_FIREWALL_CONFIG_INCONSISTENT` `LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_RANGE_PARTIALLY_BLOCKED` `LOAD_BALANCER_BEST_PRACTICES_BACKEND_SERVICE_BALANCING_MODE_BREAKS_SESSION_AFFINITY` `LOAD_BALANCER_BEST_PRACTICES_BACKEND_SERVICE_HEALTH_CHECK_PORT_MISMATCH`  
  
### Cloud NAT

For details about this insight type, see [Cloud NAT insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/cloud-nat).

## Hybrid connectivity insights

Hybrid connectivity insights cover issues related to hybrid connectivity for Cloud VPN, Cloud Interconnect, Cloud Router, BGP peering, dynamic routes, and Network Connectivity Center.

### Shadowed dynamic routes

For details about this insight type, see [Shadowed dynamic route insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/hybrid-connectivity/dynamic-route-shadowed).

For the related Recommender and Cloud Logging insight types, see the following table.

Recommender insight type and subtypes | Cloud Logging insight types  
---|---  
`google.networkanalyzer.hybridconnectivity.dynamicRouteInsight`

  * `DYNAMIC_ROUTE_FULLY_SHADOWED`
  * `NCC_DYNAMIC_ROUTE_FULLY_SHADOWED`
  * `PEERING_DYNAMIC_ROUTE_FULLY_SHADOWED`

|  `DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_SUBNET_ROUTE` `DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_PEERING_SUBNET_ROUTE` `DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_STATIC_ROUTE` `DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_PEERING_STATIC_ROUTE` `DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_NCC_SUBNET_ROUTE` `NCC_DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_SUBNET_ROUTE` `NCC_DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_PEERING_SUBNET_ROUTE` `NCC_DYNAMIC_ROUTE_SHADOWED_FULLY_SHADOWED_BY_STATIC_ROUTE`  
  
## GKE insights

Google Kubernetes Engine (GKE) insights cover networking issues that can impact the operation and connectivity for GKE. Network Analyzer detects bidirectional connectivity issues caused by configurations when a connection is initiated between a GKE node and a GKE control plane. Network Analyzer also analyzes the IP utilization of GKE pods and runs a variety of checks for best practices for GKE clusters.

### GKE connectivity

For details about this insight type, see the following:

  * [GKE node connectivity insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-node-to-control-plane)
  * [GKE on-premises to control plane connectivity insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-onprem-control-plane)
  * [GKE best practices insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-best-practices)



For the related Recommender and Cloud Logging insight types, see the following table.

Recommender insight type and subtypes | Cloud Logging insight types  
---|---  
`google.networkanalyzer.container.connectivityInsight`

  * `NODE_TO_CONTROL_PLANE_BLOCKED_BY_ROUTING_ISSUE`
  * `NODE_TO_CONTROL_PLANE_BLOCKED_BY_EGRESS_FIREWALL`
  * `CONTROL_PLANE_UNABLE_TO_ACCESS_CUSTOM_ROUTES`
  * `NEED_EXTENDED_AUTHORIZED_RANGE`
  * `PRIVATE_GOOGLE_ACCESS_DISABLED`
  * `MISSING_ROUTES_TO_GOOGLE_APIS_AND_SERVICES`

`google.networkanalyzer.container.serviceAccountInsight`

  * `NODE_SERVICE_ACCOUNT_DISABLED`
  * `NODE_SERVICE_ACCOUNT_IS_COMPUTE_ENGINE_DEFAULT`
  * `NODE_POOL_INSUFFICIENT_OAUTH_SCOPES`

|  `GKE_NODE_TO_CONTROL_PLANE_BLOCKED_BY_ROUTING_ISSUE` `GKE_NODE_TO_CONTROL_PLANE_PUBLIC_ENDPOINT_BLOCKED_BY_EGRESS_FIREWALL` `GKE_NODE_TO_CONTROL_PLANE_PRIVATE_ENDPOINT_BLOCKED_BY_EGRESS_FIREWALL`  
  
### GKE IP address utilization

For details about this insight type, see [GKE IP address utilization insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-utilization).

For the related Recommender and Cloud Logging insight types, see the following table.

Recommender insight type and subtypes | Cloud Logging insight types  
---|---  
`google.networkanalyzer.container.ipAddressInsight`

  * `POD_RANGES_ALLOCATION_RATIO_HIGH`
  * `POD_RANGES_ALLOCATION_RATIO_LIMITS_AUTOSCALING`

|  `GKE_IP_UTILIZATION_POD_RANGES_ALLOCATION_HIGH ` `GKE_IP_UTILIZATION_POD_RANGES_ALLOCATION_LIMITS_AUTOSCALING`  
  
### GKE service accounts

For details about this insight type, see [GKE node service account insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-node-service-account).

For the related Recommender and Cloud Logging insight types, see the following table.

Recommender insight type and subtypes | Cloud Logging insight types  
---|---  
`google.networkanalyzer.container.serviceAccountInsight`

  * `NODE_SERVICE_ACCOUNT_DISABLED`
  * `NODE_SERVICE_ACCOUNT_IS_COMPUTE_ENGINE_DEFAULT`
  * `NODE_SERVICE_ACCOUNT_INSUFFICIENT_OAUTH_SCOPES`

|  `GKE_NODE_SERVICE_ACCOUNT_SERVICE_ACCOUNT_DISABLED` `GKE_NODE_SERVICE_ACCOUNT_DEFAULT_SERVICE_ACCOUNT_USED` `GKE_NODE_SERVICE_ACCOUNT_BAD_OAUTH_SCOPES`  
  
### GKE IP masquerade configuration

For information about this insight type, see [GKE IP masquerade configuration insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-masq-config).

For the related Cloud Logging insight types, see the following table.

Cloud Logging insight types  
---  
`GKE_IP_MASQ_AGENT_CONFIG_MAP_NOT_COVERING_POD_CIDR` `GKE_IP_MASQ_AGENT_CUSTOM_CONFIG_NOT_COVERING_POD_CIDR`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
