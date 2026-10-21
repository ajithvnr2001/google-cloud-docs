---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes/
title: Learned routes \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:15:40.572112+00:00
---

# Learned routes  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Learned routes

This document describes learned routes, how the dynamic routing mode of a Virtual Private Cloud network affects learned routes, and best path selection modes available in Cloud Router.

_Learned routes_ are either routes that Cloud Router receives from remote peer routers using the BGP protocol or custom learned routes that you configure on a Cloud Router:

BGP received routes
    

BGP routes learned from a remote peer. The peer router can be any of the following:

  * A physical on-premises router
  * Another Cloud Router
  * A Router appliance VM (with Network Connectivity Center)
  * A router from a different cloud provider


Custom learned routes
    

Custom learned routes are manually configured on Cloud Router to simulate routes learned from a remote peer. Custom learned routes are useful when you don't have administrator control to configure a remote peer router.

Cloud Router enforces quotas for the number of unique prefixes for dynamic routes, including the prefixes that are dynamically learned from a BGP peer or are manually configured as custom learned routes. For more information, see [Cloud Router quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#quotas).

Cloud Router doesn't re-advertise [learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#benefits) unless you use an NCC hybrid spoke with data transfer enabled.

Both types of Cloud Router learned routes are processed by a dynamic route control plane and then a VPC network control plane. The processing steps use destination prefix and route metrics to create [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) in a VPC network. For information about the differences between the dynamic route control plane and the VPC network control plane, see [How Cloud Router works](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works).

## Custom learned routes

Custom learned routes provide the same advantages as BGP-received dynamic routes. Unlike [static routes](https://docs.cloud.google.com/vpc/docs/static-routes), custom learned dynamic routes are automatically withdrawn when the BGP session for a next hop goes down.

Custom learned routes are the only way to define non-BGP routes for certain next hops, like Cloud Interconnect VLAN attachments and HA VPN tunnels.

For more information, see [Specify and manage custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes).

## Dynamic routing mode

The dynamic routing mode of a VPC network affects how received BGP routes and custom learned routes are processed by the dynamic route control plane and the VPC network control plane to create dynamic routes in the VPC network.

When using VPC Network Peering, the dynamic routing mode of the VPC network that exports custom routes controls how dynamic routes are created in peer VPC networks that import custom routes. For more information, see [Effects of the dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc-peering#interaction-dynamic-routing-mode) in the VPC Network Peering documentation.

Google Cloud VPC networks support two dynamic routing modes:

Regional dynamic routing mode
    Each region's dynamic route control plane only processes learned routes from the Cloud Router BGP tasks in its own region. The resulting dynamic routes created in a particular region of a VPC network have next hops only within that specific region.
Global dynamic routing mode
    Each region's dynamic route control plane processes learned routes from the Cloud Router BGP tasks in its own region. Each region's dynamic route control plane also sends the best path for each prefix to the dynamic route control planes in all other regions used in the VPC network. The resulting dynamic routes created in a particular region of a VPC network can have next hops in any region.

## Best path selection modes

Cloud Router offers two modes for best path selection: standard mode and legacy mode. The best path selection mode applies to all learned routes through Cloud Router in all regions of a VPC network, including custom learned routes.

Legacy is the default best path selection mode when a new VPC network is created. We recommend that you use legacy mode unless you need specific features of standard mode or use a Google Cloud feature that relies on standard mode.

NCC for site-to-site data transfers and NCC for third-party network virtual appliances or Router appliance works with either standard best path selection or legacy best path selection.

NCC [route exchange with VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes) has the following limitations for best path selection modes:

  * If a route is uniquely advertised by one VPC, both standard mode and legacy mode work as expected.

  * If the same route is advertised by multiple VPCs to the same workload VPC, then the following apply:

    * If all VPCs use legacy best path selection, then the workload VPCs apply legacy best path selection across routes from different routing VPCs.

    * If all VPCs use standard best path selection, then the workload VPCs use the best route from one of the routing VPCs based upon an internal algorithm.

    * If the routing VPCs use a mix of legacy best path selection and standard best path selection, then the workload VPCs use either the best route based on legacy best path selection _or_ one of the best standard best path selection routes based on an internal algorithm.

If you plan on advertising the same route from multiple routing VPCs, then we recommend that you select legacy best path selection for all your VPC networks.




### Legacy best path selection

This section describes how Cloud Router BGP tasks and the dynamic route control plane implement the legacy best path selection mode.

#### AS path length

In legacy best path selection mode, AS path information is only relevant within a single Cloud Router BGP task, and the dynamic route control plane doesn't use the AS path information to make best path selection decisions. When using legacy best path selection mode, don't rely on selecting the best path based on AS-path length information when different Cloud Router software tasks are involved for the same destination prefix.

BGP sessions involve multiple Cloud Router BGP tasks. For more information, see [Cloud Router BGP tasks](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works#bgp-tasks).

#### BGP task selection process

A Cloud Router BGP task receives destination prefixes from peer routers of the BGP sessions that it manages. The BGP task creates a set of unique destination prefixes from all of the BGP sessions that the BGP task manages. Then the BGP task determines at least one best next hop for each of the BGP-received unique destination prefixes using the following process:

  1. **Shortest AS path length** : the BGP task sorts the list of next hops by AS path length, from shortest AS path length to longest AS path length. After sorting, the BGP task removes all next hops that don't have the shortest AS path length from consideration.

  2. **Preferred origin type** : the BGP task prefers next hops that use the Interior Gateway Protocol (IGP) over next hops that use the Exterior Gateway Protocol (EGP), and the BGP task prefers next hops that use EGP over next hops that have an Incomplete origin type.

If at least one next hop's origin type is IGP, then the BGP task removes all next hops with EGP or Incomplete origin types from consideration.

If none of the next hops has an origin type IGP _and_ if at least one next hop's origin type is EGP, the BGP task removes all next hops with Incomplete origin types from consideration.

  3. **Smallest MED value** : The BGP task sorts next hops from smallest to largest multi-exit discriminator (MED) value. After sorting, the BGP task removes all next hops that don't have the smallest MED value from consideration.




The BGP task sends each destination prefix and its corresponding list of best next hops to the region's dynamic route control plane. In some cases the Cloud Router BGP software task might also send next hops that have been removed from consideration.

#### Dynamic route control plane processing

Each region's dynamic route control plane enforces the following quotas, which apply to unique destinations from both BGP received and custom learned routes:

  * [Unique Cloud Router dynamic route prefixes from own region per region per VPC network](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#from-own-region-limit)
  * [Unique Cloud Router dynamic route prefixes from other regions per region per VPC network](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#from-other-regions-limit)



When enforcing the Cloud Router quotas, the dynamic route control plane drops all route information associated with unique destinations that sort beyond the limit for either Cloud Router quota. For more information, see [Deterministic route dropping behavior](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#deterministic). You can identify which routes were dropped by viewing `[route_quota_events](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#route-quota-events-log)` in Cloud Logging.

After enforcing the quotas, the dynamic route control plane applies the following processing algorithm to each non-dropped unique destination prefix:

  1. The dynamic route control plane creates a list of next hops for the prefix. The list consists of:

     * Next hops and MED values for the prefix received from each Cloud Router BGP task within the VPC network in its own region.

     * Next hops and priority values for custom learned routes that use the prefix. The priority of a custom learned route is treated like a MED value.

  2. The following steps occur only when the VPC network that contains the Cloud Routers uses the global dynamic routing mode:

     * The dynamic route control plane sends only the next hops that have the lowest MED value to the dynamic route control planes in other regions. If more than one next hop has the same lowest MED value, then they're all exported to the dynamic route control planes in other regions. The information sent includes both the next hops and the lowest MED value.

     * The dynamic route control plane receives a list of next hops and MED values from dynamic route control planes in other regions. The dynamic route control plane adds each next hop to its list of next hops for the prefix. When adding each next hop, the dynamic route control plane adjusts the MED value by adding an inter-regional cost.

  3. The dynamic route control plane sorts its list of next hops for the prefix from smallest to largest received MED value.

  4. The dynamic route control plane truncates the list of routes that are sent to the VPC control plane. Typically the list of routes sent to the VPC control plane includes the routes with the lowest MED values, and, if available, the next-to-lowest MED values. However, the dynamic route control plane only guarantees that it sends the routes with the lowest MED values to the VPC control plane.




### Standard best path selection mode

The standard best path selection mode more closely adheres to [RFC 4271](https://datatracker.ietf.org/doc/html/rfc4271). It offers the following benefits over the legacy best path selection mode:

  * **Consistent AS path-based routing** : AS path information is considered over all of the routes learned on all of the Cloud Routers of the VPC network. This lets you influence traffic flow using AS path prepending.

  * **Better flexibility and customization** : you have more control over how BGP prefixes are ranked within your VPC networks, including the ability to fine-tune BGP best-path routing. Dynamic routes always have a lower VPC network route priority compared to [static routes](https://docs.cloud.google.com/vpc/docs/static-routes).




When using the standard best path selection mode, Cloud Router offers the following configuration options:

  * **Compare MED values** : you can choose either of the following options:

    * **Always compare:** the MED value for each destination prefix is compared without considering the AS that the Cloud Router learned the prefix from.

    * **Conditionally compare:** prefixes are grouped by the AS that the Cloud Router learned the prefix from. For each prefix within each AS, the hops are ranked by the MED value matching described in [RFC 4271](https://datatracker.ietf.org/doc/html/rfc4271).

  * **Add region to inter-region costs** : you can select whether inter-region costs are added to MED values.




#### BGP task selection process

A Cloud Router BGP task receives destination prefixes from peer routers of the BGP sessions that it manages. The BGP task creates a set of unique destination prefixes from all of the BGP sessions that the BGP task manages. Then the BGP task determines at least one best next hop for each of the BGP-received unique destination prefixes using the following process:

  1. **Shortest AS path length** : the BGP task sorts the list of next hops by AS path length, from shortest AS path length to longest AS path length. After sorting, the BGP task removes all next hops that don't have the shortest AS path length from consideration.

  2. **Preferred origin type** : the BGP task prefers next hops that use the Interior Gateway Protocol (IGP) over next hops that use the Exterior Gateway Protocol (EGP), and the BGP task prefers next hops that use EGP over next hops that have an Incomplete origin type.

If at least one next hop's origin type is IGP, then the BGP task removes all next hops with EGP or Incomplete origin types from consideration.

If none of the next hops has an origin type IGP _and_ if at least one next hop's origin type is EGP, the BGP task removes all next hops with Incomplete origin types from consideration.

  3. **Consider neighbor ASN** : the VPC network setting `routingConfig.bgpAlwaysCompareMed` controls this step of the algorithm as follows:

     * If `routingConfig.bgpAlwaysCompareMed` is `True`, the neighbor ASN value of each next hop isn't considered relevant. The BGP task sorts next hops from smallest to largest MED value. After sorting, the BGP task removes all next hops that don't have the smallest MED value from consideration.

     * If `routingConfig.bgpAlwaysCompareMed` is `False` or isn't set, the neighbor ASN value of each next hop is considered relevant, so the BGP task does the following:

       1. The BGP task groups the list of next hops by neighbor ASN value.

       2. Within each neighbor ASN group, the BGP task sorts the next hops from smallest to largest MED value. (The smallest-numbered MED value might be different in each neighbor ASN group.)

       3. Within each neighbor ASN group, the BGP task removes all next hops that don't have the smallest MED value from consideration.




The BGP task sends each destination prefix and its corresponding list of non-removed next hops to the region's dynamic route control plane. In some cases the Cloud Router BGP software task might also send next hops that have been removed from consideration.

#### Dynamic route control plane processing

Each region's dynamic route control plane enforces the following quotas, which apply to unique destinations from both the BGP received and custom learned routes:

  * [Unique Cloud Router dynamic route prefixes from own region per region per VPC network](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#from-own-region-limit)
  * [Unique Cloud Router dynamic route prefixes from other regions per region per VPC network](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#from-other-regions-limit)



When enforcing the Cloud Router quotas, the dynamic route control plane drops all route information associated with unique destinations that sort beyond the limit for either Cloud Router quota. For more information, see [Deterministic route dropping behavior](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#deterministic).

You can identify which routes were dropped by viewing `[route_quota_events](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#route-quota-events-log)` in Cloud Logging.

After enforcing the quotas, the dynamic route control plane applies the following processing algorithm to each non-dropped unique destination prefix:

  1. **Initial list of next hops for the prefix** : the dynamic route control plane creates an initial list of next hops for the prefix consisting of both of the following:

     * The BGP-received next hop information from BGP tasks managing Cloud Routers in the VPC network, located in the same region as the dynamic route control plane.

     * The next hop information of custom learned routes for the prefix, defined on Cloud Routers in the VPC network, and located in the same region as the dynamic route control plane. Custom learned routes have the following BGP attributes applied:

       * AS path, consisting of just the peer's ASN. That is an AS-path length of 1, and the neighbor ASN of the peer's ASN.
       * Origin, set to Incomplete.
       * MED value, where each custom learned route priority is treated like a MED value.
       * Inter-region cost set to 0.
  2. **Shortest AS path length** : the dynamic route control plane sorts the list of next hops by AS path length, from shortest AS path length to longest AS path length. The dynamic route control plane removes all next hops that don't have the shortest AS path length from consideration.

  3. **Preferred origin type** : the dynamic route control plane prefers next hops that use IGP over next hops that use the EGP, and next hops that use EGP over next hops that have an Incomplete origin type.

If at least one next hop's origin type is IGP, then the dynamic route control plane removes all next hops with EGP or Incomplete origin types from consideration.

If none of the next hops has an origin type IGP _and_ if at least one next hop's origin type is EGP, the dynamic route control plane removes from consideration all next hops with Incomplete origin types.

  4. **Consider neighbor ASN** : the VPC network setting `routingConfig.bgpAlwaysCompareMed` controls this step of the algorithm as follows:

     * If `routingConfig.bgpAlwaysCompareMed` is `True`, then the neighbor ASN value of each next hop isn't considered relevant. In this case, the dynamic route control plane sorts next hops from smallest to largest MED value. Next hops with the smallest MED have the highest _rank_. The dynamic route control plane removes all next hops except for those with the highest rank from consideration.

     * If `routingConfig.bgpAlwaysCompareMed` is `False` or isn't set, the neighbor ASN value of each next hop is considered relevant, so the dynamic route control plane does the following:

       1. The dynamic route control plane groups the list of next hops by neighbor ASN value.

       2. Within each neighbor ASN group, the dynamic route control plane sorts the next hops from smallest to largest MED value. The smallest-numbered MED value might be different in each neighbor ASN group.

       3. Within each neighbor ASN group, the dynamic route control plane removes all next hops that don't have the smallest MED value from consideration.

The next hops that have the smallest MED values _within each neighbor ASN group_ have the highest _rank_. The dynamic route control plane removes all next hops except for those with the highest rank from consideration.

  5. **Send all highest-ranked next hops to other regions** : when the dynamic routing mode of the VPC network is global, the dynamic route control plane sends the current set of highest-ranked next hops to other regions.

  6. **Receive highest-ranked hops from other regions** : when the dynamic routing mode of the VPC network is global, the dynamic route control plane receives a list of highest-ranked next hops for the prefix from the dynamic route control planes in each of the other regions. Each received next hop includes AS path length, neighbor ASN, origin type, and MED, plus the region of the dynamic route control plane that sent the next hop.

The dynamic route control plane appends the received next hops to its list of next hops for the prefix, then does the following:

     * Repeats the **Shortest AS path length** step.

     * Repeats the **Preferred origin type** step.

     * Repeats the **Consider neighbor ASN** step according to the `routingConfig.bgpInterRegionCost` setting of the VPC network:

       * If `routingConfig.bgpInterRegionCost` of the VPC network is `ADD_COST_TO_MED`, the dynamic route control plane uses adjusted MED values when repeating the **Consider neighbor ASN** step. Each adjusted MED value is the sum of the original MED value plus an inter-regional cost. Next hops in the dynamic route control plane's own region have an inter-regional cost of `0`. Next hops learned from dynamic route control planes in other regions have nonzero inter-regional costs, unique to each region pair consisting of the sending region and receiving region.

       * If the `routingConfig.bgpInterRegionCost` of the VPC network is `DEFAULT` or not set, the dynamic route control plane repeats the **Consider neighbor ASN** step using original MED values.

  7. **Remove from consideration all next hops that don't have the smallest inter-regional cost** : when the dynamic routing mode of the VPC network is global, the dynamic route control plane removes from consideration all next hops except for the next hops that have the smallest inter-regional cost.

  8. **Send next hops to the VPC control plane** : For each unique destination prefix, the dynamic route control plane sends all next hops with the highest rank and smallest inter-regional cost to the VPC control plane. These next hops create dynamic routes in the dynamic route control plane's region of the VPC network. These dynamic routes have Andromeda route priority `65536`. The `65536` priority number is purposefully chosen because it's one value larger than `65535`, the _lowest_ priority of a [static route](https://docs.cloud.google.com/vpc/docs/static-routes). Consequently, if both static and dynamic routes exist for the same destination prefix, a static route is preferred by the [routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).

In some situations, the dynamic route control plane can send next hops that have lower ranks or non-lowest inter-regional cost. These additional next hops also create dynamic routes in the dynamic route control plane's region of the VPC network, but they use lower Andromeda route priorities—for example, `65537`, `65538`.




## VPC control plane processing

Each region's VPC control plane receives candidate dynamic routes from the region's dynamic route control plane. Unless a dynamic route is dropped by the dynamic route control plane, the VPC control plane evaluates each candidate dynamic route. Evaluation results in either creating a dynamic route in the VPC network that contains the Cloud Routers or suppression of the candidate dynamic route. The following are reasons why a candidate dynamic route is suppressed:

  * The candidate dynamic route destination prefix conflicts with a local, peering, or NCC subnet route. [Hybrid subnet routing](https://docs.cloud.google.com/vpc/docs/hybrid-subnets) is an exception. For more information, see [Interactions between subnet routes and dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-dynamic-interactions).

  * The VPC control plane determines that the next hop for the candidate dynamic route isn't usable before an updated BGP state is processed by Cloud Router. For more information, see the [Disregard static and dynamic routes with unusable next hops](https://docs.cloud.google.com/vpc/docs/routes#disregard-static-dynamic-routes) step of the routing order.




### VPC control plane processing of peering dynamic routes

Each region's VPC control plane is responsible for creating [peering dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#peering-custom-routes) when both of the following conditions are true:

  * The VPC network containing the Cloud Routers exports custom routes.

  * The other VPC network imports custom routes.




For information about custom route exchange using VPC Network Peering, see [Options for exchanging dynamic routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#dynamic-route-exchange).

When creating peering dynamic routes, each region's VPC control plane independently evaluates candidate dynamic routes for each network. The following additional suppression cases apply when using VPC Network Peering:

  * **Local dynamic routes suppress candidate peering dynamic routes** : If the destination prefix of a candidate peering dynamic route exactly matches the destination prefix of a local dynamic route, the VPC control plane suppresses the conflicting candidate peering dynamic route. For more information, see the [Select only the most favorable custom route type](https://docs.cloud.google.com/vpc/docs/routes#custom-route-category-step) step of the routing order.

  * **Candidate peering dynamic routes from different peered VPC networks** : If two or more candidate peering dynamic routes with the same destination prefix are received from different peered VPC networks, the VPC control plane uses an internal algorithm to pick the network from which it imports peering dynamic routes. This internal algorithm is evaluated _before_ considering route priority. For more information, see the [Select next hops for peering custom routes from a single VPC network](https://docs.cloud.google.com/vpc/docs/routes#peering-custom-single-vpc-network) step of the routing order.

  * **Candidate peering dynamic routes suppressed by quota** : If the [dynamic routes per region per peering group quota](https://docs.cloud.google.com/vpc/docs/quota#per_network) usage exceeds its limit, the VPC control plane suppresses peering dynamic routes.




### VPC control plane processing of NCC dynamic routes

Each region's VPC control plane is responsible for creating NCC dynamic routes in VPC spokes when a hybrid spoke's export filter sends the dynamic routes to the hub. For more information, see [Spoke filters overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview).

When creating NCC dynamic routes, each region's VPC control plane independently evaluates candidate dynamic routes for each VPC spoke. The following additional suppression cases apply when using NCC:

  * **Local dynamic routes suppress candidate NCC dynamic routes** : If the destination prefix of a candidate NCC dynamic route exactly matches the destination prefix of a local dynamic route, the VPC control plane suppresses the conflicting candidate NCC dynamic route. For more information, see the [Select only the most favorable custom route type](https://docs.cloud.google.com/vpc/docs/routes#custom-route-category-step) step of the routing order.

  * **Candidate NCC dynamic routes from hybrid spokes in different routing VPC networks** : If two or more candidate NCC dynamic routes with the same destination prefix are received from hybrid spokes in different routing VPC networks, the VPC control plane selects a route candidate _after_ considering route priority. For more information, see the [Select next hops for NCC dynamic routes from a single routing VPC network](https://docs.cloud.google.com/vpc/docs/routes#ncc-dynamic-single-vpc-network) step of the routing order.

  * **Candidate NCC dynamic routes suppressed by quota** : If the [dynamic routes per region of spoke group route table quota](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-quotas) usage exceeds its limit, the NCC control plane prevents some NCC dynamic routes from being sent to the hub. Consequently, the VPC control plane is unable to import those routes into other VPC spokes.




### VPC control plane network programming

Because VPC control planes program each network separately, candidate dynamic route suppression is unique to each VPC network:

  * Suppose that a candidate dynamic route becomes a local dynamic route in the VPC network that contains the Cloud Routers that produced the candidate dynamic route. The following occurs:

    * Corresponding peering dynamic routes might be suppressed when the VPC control plane processes dynamic routes in each peered VPC network.
    * Corresponding NCC dynamic routes might be suppressed when the VPC control plane processes dynamic routes in each VPC spoke.
  * Suppose that a candidate dynamic route has been suppressed in the VPC network that contains the Cloud Routers that produced the candidate dynamic route. The following occurs:

    * Corresponding peering dynamic routes might _not_ be suppressed when the VPC control plane processes dynamic routes in each peered VPC network.
    * Corresponding NCC dynamic routes might _not_ be suppressed when the VPC control plane processes dynamic routes in each VPC spoke.



## BGP state changes

BGP-received and custom learned routes produce dynamic routes as described in Best path selection modes. Dynamic routes persist for as long as the corresponding BGP session is established. Dynamic routes are removed when a BGP session is considered down or has been terminated. The following are common examples:

  * If the peer router supports graceful restart and sends a graceful restart notification (TCP `FIN` or `RST` packet), Google Cloud removes the dynamic routes learned from the BGP session after the _peer_ router's graceful restart timer has expired. For more information, see [graceful restart timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#graceful-restart-timer).

  * If the peer router sends a BGP `CEASE` notification, Google Cloud removes the dynamic routes learned from the BGP session immediately. For more information, see [Section 4.5 of RFC 4271](https://datatracker.ietf.org/doc/html/rfc4271#section-4.5).

  * If neither of the previous notification situations apply, and the negotiated hold timer is reached, Google Cloud removes the dynamic routes learned from the BGP session. For more information, see [hold timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#hold_timer).




Planned [maintenance events for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events) result in removal of dynamic routes whose next hops are the VLAN attachments associated with a Cloud Interconnect connection during the connection's maintenance. During planned maintenance, the corresponding BGP sessions are taken down. To minimize disruptions, make sure that your Cloud Interconnect VLAN attachments and connections adhere to one of the following requirements:

  * [99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability)
  * [99.99% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability)

  * [99.9% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability)

  * [99.9% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability)




For more information about BFD, see [BFD during a failure event](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd_during_a_failure_event).

## What's next

  * To configure custom learned routes, see [Specify and manage custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes).

  * To troubleshoot issues with Cloud Router, see the following:

    * [Troubleshoot BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-sessions)

    * [Troubleshoot BGP peering](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering)

    * [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes)

    * [Troubleshoot Cloud Router log messages](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
