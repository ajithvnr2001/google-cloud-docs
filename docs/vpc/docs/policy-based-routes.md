---
url: https://docs.cloud.google.com/vpc/docs/policy-based-routes/
title: Policy-based routes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.929977+00:00
---

# Policy-based routes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/policy-based-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Policy-based routes

This document provides an overview of Policy-based Routing.

Policy-based routes let you select a next hop based on more than a packet's destination IP address. You can match traffic by protocol and source IP address as well. Matching traffic is redirected to an internal passthrough Network Load Balancer. This can help you insert appliances such as firewalls into the path of network traffic.

## Specifications

  * When you [create a policy-based route](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#create), you select which resources the policy-based route applies to. The route can apply to: 
    * All VM instances, Cloud Interconnect VLAN attachments, and Cloud VPN tunnels that are in the same VPC network as the route
    * Only VM instances that are in the same VPC network as the route and identified by [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags)
    * Only VLAN attachments that are in a specific region of the same VPC network as the route. You can't create a policy-based route that only applies to a single VLAN attachment or Cloud VPN tunnel
  * The next hop of a policy-based route must be a valid [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal). This internal passthrough Network Load Balancer must either be in the same VPC network as the policy-based route or in a VPC network that is connected to the route's VPC network through [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  * The backend VM instances of the next hop internal passthrough Network Load Balancer must have [IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#create-vm-canipforward) enabled.
  * Policy-based routes are evaluated before subnet routes, static routes, and dynamic routes, but after [special routing paths](https://docs.cloud.google.com/vpc/docs/routes#special_return_paths). For more information, see the [Policy-based routes](https://docs.cloud.google.com/vpc/docs/routes#check-for-pbrs) step in the routing order.
  * If two or more policy-based routes have the same priority, and a packet's characteristics match at least two of those policy-based routes, Google Cloud selects a single policy-based route by using an internal algorithm. The selected policy-based route might not be the most specific match for the packet's characteristics because policy-based routes don't use longest-prefix matching. Make sure that all policy-based routes in the same VPC network have unique priorities.
  * A policy-based route can apply to either IPv4 or IPv6 traffic.
  * You can create a single rule for one-way traffic or multiple rules to handle bidirectional traffic.



## Limitations

  * Policy-based routes are not exchanged between VPC networks that are connected through [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  * Policy-based routes are not exchanged between [Network Connectivity Center spokes and hubs](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview).
  * Policy-based routes don't support matching traffic based on port.
  * It is not possible to update a policy-based route after it is created. If you want to update a route, [delete the route](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#delete) and then create a new one.
  * The internal passthrough Network Load Balancer forwarding rule must have a dedicated IP address that's not used by any other internal passthrough Network Load Balancer. Using a shared IP address (IP address purpose set to `SHARED_LOADBALANCER_VIP`) is not supported.
  * Policy-based routes can interfere with communication between the GKE control plane and nodes. For more information, see [Use policy-based routes with GKE](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#pbr-with-gke).
  * Policy-based routes can't route packets to Private Service Connect endpoints or backends. 
    * For information about using policy-based routes in VPC networks with endpoints or backends that access published services, see [Policy-based routes and Private Service Connect for published services](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#pbr-with-psc).
    * For information about using policy-based routes in VPC networks with endpoints or backends that access Google APIs and services, see [Policy-based routes and accessing Google APIs and services](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#pbr-with-pga-psc-apis).
  * Only VLAN attachments that use [Dataplane v2](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#dataplaneVersion) can use policy-based routes. To inspect your VLAN attachment to check what version it uses, see the instructions for [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-vlans#dataplane) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/viewing-vlans#dataplane).



## Skipping other policy-based routes

You can create a policy-based route that skips other policy-based routes by using the Google Cloud CLI or sending an API request. For the gcloud CLI, use the `--next-hop-other-routes=DEFAULT_ROUTING` flag. For an API request, include `"nextHopOtherRoutes": "DEFAULT_ROUTING"` with the request body.

If a policy-based route of this type matches a packet's characteristics and has a higher priority than other matching policy-based routes, Google Cloud ignores the other policy-based routes and proceeds to the _most specific destination_ step of the [VPC routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).

For example, consider a policy-based route that uses a next hop internal passthrough Network Load Balancer. This policy-based route has a source range of `0.0.0.0/0` and a network tag of `compute-vm`.

To skip evaluation of the first policy-based route when packet sources match a specific IP address range, create a higher-priority policy-based route that is configured to skip other policy-based routes. Set the source IP address range for this higher-priority policy-based route to the source IP address range of the systems that need to skip policy-based routing.

## Quota

There is a limit for how many policy-based routes you can create in a single project. For more information, see the per-project [quotas](https://docs.cloud.google.com/vpc/docs/quota#policy-based-routes-quota) in the VPC documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
