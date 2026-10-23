---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview/
title: Spoke filters overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:20.066717+00:00
---

# Spoke filters overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Spoke filters overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes spoke filters, what the import and export spoke filters mean, supported filters for each spoke type, and provides examples for how spoke filters are used.

## Spoke filters

Network Connectivity Center has two types of spoke filters:

  * **Export filters** : Export filters control the following:

    * Which subnet routes a [VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) sends to the hub
    * Which dynamic routes a [hybrid spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid_spokes) sends to the hub
  * **Import filters** : Import filters control which subnet routes and dynamic routes a hybrid spoke imports from the hub.




The following table shows the supported spoke types for each filter.

Spoke type | Export filter | Import filter  
---|---|---  
VPC spokes   
Producer VPC spokes  |  Include export ranges (IPv4 and IPv6)  
Exclude export ranges (IPv4 and IPv6)  
|  Include import ranges  
Exclude import ranges  
  
VLAN attachment hybrid spokes   
Cloud VPN hybrid spokes  |  Include export ranges (IPv4 and IPv6)  
Exclude export ranges (IPv4 and IPv6)  
|  Include import ranges (IPv4 and IPv6)  
Exclude import ranges (IPv4 and IPv6)  
  
Router appliance hybrid spokes |  Include export ranges (IPv4 only)  
Exclude export ranges (IPv4 only)  
|  Include import ranges (IPv4 only)  
Exclude import ranges (IPv4 only)  
  
NCC Gateway spokes |  Include export ranges  
Exclude export ranges  
|  Include import ranges  
Exclude import ranges  
  
  
## Export filters

Export filters control which subnet ranges or dynamic routes a spoke sends to the NCC [hub route table](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-hub-admin#hub-route-table). Export filters are configured on a per-spoke basis.

  * **Export filters on a VPC spoke** : These filters control which subnet ranges are sent to the hub.

  * **Export filters on a hybrid spoke** : These filters control which dynamic routes are sent to the hub.




Export filters consist of both _include export ranges_ and _exclude export ranges_.

  * **Include export ranges** : Use the `--include-export-ranges` flag in the Google Cloud CLI or the `includeExportRanges` field in the API to create an include export range. The following rules apply to the include export ranges:

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR. CIDRs can be IPv4 or IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages)), except for Router appliance hybrid spokes, which support only IPv4 CIDRs.

    * In place of a CIDR, the include export ranges support the following keywords:

      * `ALL_PRIVATE_IPV4_RANGES`: This keyword includes all [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) from subnet ranges exported by a VPC spoke. This keyword can only be used in the include export ranges of a VPC spoke.

      * `ALL_IPV4_RANGES`: This keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. This keyword can be used in the include export ranges of a VPC spoke or hybrid spoke.

      * `ALL_IPV6_RANGES`: This keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR. This keyword can be used in the include export ranges of a VPC spoke or hybrid spoke, except for a Router appliance hybrid spoke.

    * If you don't specify any include export ranges, NCC uses the following defaults:

      * For a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

      * For a hybrid spoke, the default include export ranges is the same as if you had specified `ALL_IPV4_RANGES`.

  * **Exclude export ranges** : Use the `--exclude-export-ranges` flag in the Google Cloud CLI or the `excludeExportRanges` field in the API to create an exclude export range. The following rules apply to the exclude export ranges:

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR. CIDRs can be IPv4 or IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages)), except for Router appliance hybrid spokes, which support only IPv4 CIDRs.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the _include_ export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you don't specify any exclude export ranges, NCC uses an empty list as the default exclude export ranges, for both VPC spokes and hybrid spokes.




### Export filter rules for VPC spokes

For VPC spokes, the following rules control the interaction between export filters and subnet ranges in each VPC spoke:

Scenario | Example | Valid configuration | Result  
---|---|---|---  
Subnet range of a VPC network isn't wholly contained in any of the VPC spoke's include export ranges (and consequently isn't contained in any exclude export ranges) | Subnet range `10.0.0.0/16` and include export range `192.168.0.0/16` |  | The subnet range isn't sent to the hub.  
Subnet range of a VPC network intersects with, but isn't wholly contained in, one of the VPC spoke's include export ranges | Subnet range `10.0.0.0/16` and include export range `10.0.0.0/17` |  | Google Cloud prevents the following: 

  * Creating a new subnet range if an existing include export range results in this scenario
  * Creating a new include export range if an existing subnet range results in this scenario

  
Subnet range of a VPC network is wholly contained in one of the VPC spoke's include export ranges, and the subnet range doesn't intersect with any of the spoke's exclude export ranges | Subnet ranges `10.0.0.0/16` or `10.0.0.0/17`, include export ranges `10.0.0.0/16` and `192.168.0.0/16`, exclude export range `192.168.0.0/24` |  | The subnet range is sent to the hub.  
Subnet range of a VPC network is wholly contained in one of the VPC spoke's include export ranges, but the subnet range intersects with one of the spoke's exclude export ranges | Subnet range `10.0.0.0/17`, include export range `10.0.0.0/16`, exclude export range `10.0.0.0/24` |  | Google Cloud prevents the following: 

  * Creating a new subnet range if an existing include export range and an existing exclude export range result in this scenario
  * Creating a new include export range if an existing subnet range and an existing exclude export range result in this scenario
  * Creating a new exclude export range if an existing subnet range and an existing include export range result in this scenario

  
Subnet range of a VPC network is wholly contained in one of the VPC spoke's exclude export ranges (and consequently is contained in one of its include export ranges) | Subnet range `10.0.0.0/17`, include export range `10.0.0.0/8`, and exclude export range `10.0.0.0/16` |  | The subnet range isn't sent to the hub.  
  
### Export filter rules for hybrid spokes

For hybrid spokes, the following rules control the interaction between export filters and dynamic routes:

Scenario | Example | Valid configuration | Result  
---|---|---|---  
Dynamic route in a hybrid spoke isn't wholly contained in any of the hybrid spoke's include export ranges (and consequently isn't contained in any exclude export ranges) | Dynamic route `10.0.0.0/16` and include export range `192.168.0.0/16` |  | The dynamic route isn't sent to the hub.  
Dynamic route in a hybrid spoke intersects with, but isn't wholly contained in, one of the hybrid spoke's include export ranges | Dynamic route `10.0.0.0/16` and include export range `10.0.0.0/17` |  | The dynamic route isn't sent to the hub.  
Dynamic route in a hybrid spoke is wholly contained in one of the hybrid spoke's include export ranges, and the dynamic route doesn't intersect with any of the spoke's exclude export ranges | Dynamic route `10.0.0.0/16` or `10.0.0.0/17`, include export ranges `10.0.0.0/16` and `192.168.0.0/16`, exclude export range `192.168.0.0/24` |  | The dynamic route is sent to the hub.  
Dynamic route in a hybrid spoke is wholly contained in one of the hybrid spoke's include export ranges, but the dynamic route intersects with one of the spoke's exclude export ranges | Dynamic route `10.0.0.0/17`, include export range `10.0.0.0/16`, exclude export range `10.0.0.0/24` |  | The dynamic route isn't sent to the hub.  
Dynamic route in a hybrid spoke is wholly contained in one of the hybrid spoke's exclude export ranges (and consequently is contained in one of its include export ranges) | Dynamic route `10.0.0.0/17`, include export range `10.0.0.0/8`, and exclude export range `10.0.0.0/16` |  | The dynamic route isn't sent to the hub.  
  
## Import filters

Import filters control which subnet ranges or dynamic routes a hybrid spoke's [routing VPC network](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#routing-vpc) receives from the NCC hub route table. Import filters are configured for each hybrid spoke, and they support IPv4 and IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages)) address ranges (except for Router appliance spokes, which support only IPv4 address ranges). VPC spokes don't support import filters.

Import filters consist of both _include import ranges_ and _exclude import ranges_ :

  * **Include import ranges** : Use the `--include-import-ranges` flag in the Google Cloud CLI or the `includeImportRanges` field in the API to create an include import range. The following rules apply to the include import ranges:

    * The include import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include import ranges can match or contain another CIDR. CIDRs can be IPv4 or IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages)), except for Router appliance hybrid spokes, which support only IPv4 CIDRs.

    * In place of a CIDR, the include import ranges support the following keywords:

      * `ALL_IPV4_RANGES`: This keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

      * `ALL_IPV6_RANGES`: This keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR. This keyword can't be used by Router appliance hybrid spokes.

    * If you don't specify any include import ranges, NCC uses the following defaults:

      * If the hybrid spoke doesn't have [site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer) enabled, the default include import ranges is empty.

      * If the hybrid spoke has site-to-site data transfer enabled, the default include import ranges contains only the IPv4 dynamic routes learned from the hub's other hybrid spokes that have site-to-site data transfer enabled (transit dynamic routes). This default include import ranges doesn't contain any subnet ranges from the hub.

      * Google recommends that you specify an explicit set of include import ranges since the default values vary and might only apply to importing transit dynamic routes.

  * **Exclude import ranges** : Use the `--exclude-import-ranges` flag in the Google Cloud CLI or the `excludeImportRanges` field in the API to create an exclude import range. The following rules apply to the exclude import ranges:

    * The exclude import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude import ranges can match or contain another CIDR. CIDRs can be IPv4 or IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages)), except for Router appliance hybrid spokes, which support only IPv4 CIDRs.

    * Every CIDR specified in the exclude import ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the _include_ import ranges.

    * Exclude import ranges don't support keywords.

    * If you don't specify any exclude import ranges, the default `exclude import ranges` is empty.




### Hybrid spokes and NCC-imported subnet route advertisement

BGP sessions on Cloud Routers in a hybrid spoke can advertise subnet ranges received from the NCC hub route table using either of the following techniques:

  * **Using hybrid spoke import filters and Cloud Router subnet route advertisement** : This technique only supports IPv4 subnet ranges because import filters only support IPv4 ranges. To use this technique, you must do the following:

    * Configure include import ranges and exclude import ranges in hybrid spokes of a routing VPC network. For example, set the include import ranges to `[ALL_IPV4_RANGES]` and leave exclude import ranges empty.

    * Configure subnet range advertisement on BGP sessions of Cloud Routers in hybrid spokes of a routing VPC network. Cloud Router subnet range advertisement is available using either default or custom advertisement mode. For more information, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) in the Cloud Router documentation.

When using this technique, note the following:

    * **Effect of dynamic routing mode on subnet range advertisement** : The dynamic routing mode of a routing VPC network controls the subnet range advertisement of _both_ its local subnet ranges _and_ subnet ranges received from the NCC hub:

      * **Routing VPC network using regional dynamic routing mode** : BGP sessions in each hybrid spoke can only advertise local subnet ranges and NCC-imported subnet ranges that are in the same region as the hybrid spoke. The advertised MED matches the configured base priority of each BGP session.

      * **Routing VPC network using global dynamic routing mode** : BGP sessions in each hybrid spoke can advertise local subnet ranges and NCC-imported subnet ranges from any region. The advertised MED of subnet ranges in the same region as the hybrid spoke matches the configured base priority of the BGP session. The advertised MED of subnet ranges in different regions is the sum of the configured base priority of the BGP session and an inter-regional cost.

    * **Hybrid spoke import filters don't affect advertisement of local subnet ranges from the routing VPC network** : Hybrid spoke import filters can't be used to control the advertisement of _local_ subnet ranges in a routing VPC network. Advertisement of the routing VPC network's local subnet ranges depends on each BGP session's advertisement mode and the dynamic routing mode of the routing VPC network.

  * **By using Cloud Router custom advertisements** : [Cloud Router custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-custom) supports advertising custom IPv4 and IPv6 prefixes to a peer of a BGP session, either in addition to subnet route advertisement or instead of subnet route advertisement. You can add IPv4 or IPv6 CIDRs, including ones that match or contain subnet ranges in the NCC hub.

When using this technique, note the following:

    * **Effect of dynamic routing mode on Cloud Router custom advertisements** : The dynamic routing mode of a routing VPC network _doesn't_ affect custom route advertisement. The advertised MED matches the configured base priority of each BGP session.

    * **A Cloud Router custom advertisement is ignored if it exactly matches an advertised subnet route** :

      * If a BGP session's advertisement mode and the dynamic routing mode of the routing VPC network result in the advertisement of a local subnet range, the BGP session omits any custom advertisement if the custom advertisement matches the local subnet range.

      * If hybrid spoke import filters and the dynamic routing mode of the routing VPC network result in the advertisement of an NCC-imported subnet range, the BGP session omits any custom advertisement if the custom advertisement matches the NCC-imported subnet range.




The following statement applies to both techniques:

**Effect of Cloud Router outbound BGP policies** : [Outbound BGP policies](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview) apply to all advertised routes, including NCC-imported subnet routes.

### Hybrid spokes and NCC-imported dynamic route re-advertisement

BGP sessions on Cloud Routers in a hybrid spoke can re-advertise dynamic routes received from other hybrid spokes of the NCC hub route table. To use this technique, you must do the following:

  * Ensure all hybrid spokes are in the same routing VPC network. This is a [site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer) prerequisite.

  * Ensure that site-to-site data transfer is enabled in the hybrid spoke that sends the dynamic routes to the hub.

  * Ensure that site-to-site data transfer is enabled in the hybrid spoke that receives the dynamic routes from the hub. Configure include import ranges and exclude import ranges for this hybrid spoke appropriately.




The re-advertised dynamic routes are called _transit dynamic routes_. When using this technique, note the following:

  * **Effect of dynamic routing mode on transit dynamic route re-advertisement** : The dynamic routing mode of the routing VPC network that contains the hybrid spokes controls which transit dynamic routes are re-advertised:

    * **Routing VPC network using regional dynamic routing mode** : BGP sessions of Cloud Routers in a hybrid spoke with site-to-site data transfer enabled re-advertise transit dynamic routes from other hybrid spokes, with site-to-site data transfer enabled, in the same region. The advertised MED matches the configured base priority of each BGP session that does the re-advertisement.

    * **Routing VPC network using global dynamic routing mode** : BGP sessions of Cloud Routers in a hybrid spoke with site-to-site data transfer enabled re-advertise transit dynamic routes from other hybrid spokes, with site-to-site data transfer enabled, in all regions. The advertised MED of transit dynamic routes in the same region matches the configured base priority of each BGP session that does the re-advertisement. The advertised MED of transit dynamic routes in different regions matches the configured base priority and an inter-regional cost.

  * **Effect of Cloud Router advertisement mode** : Settings in the [Cloud Router advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am) don't control whether transit dynamic routes are re-advertised. Re-advertisement of transit dynamic routes is controlled exclusively by hybrid spoke settings—the site-to-site data transfer option, export filters, and import filters.




### Import filter rules for hybrid spokes

For hybrid spokes, the following rules control the interaction between import filters and routes received from the hub. Routes received from the hub can be subnet routes or transit dynamic routes.

Scenario | Example | Valid configuration | Result  
---|---|---|---  
Subnet route or transit dynamic route in the hub isn't wholly contained in any of the hybrid spoke's include import ranges (and consequently isn't contained in any exclude import ranges) | Hub subnet route or transit dynamic route `10.0.0.0/16` and include import range `192.168.0.0/16` |  | Hub subnet route or transit dynamic route isn't imported by the hybrid spoke.  
Subnet route or transit dynamic route in the hub intersects with, but isn't wholly contained in, one of the hybrid spoke's include import ranges | Hub subnet route or transit dynamic route `10.0.0.0/16` and include import range `10.0.0.0/17` |  | Hub subnet route or transit dynamic route isn't imported by the hybrid spoke.  
Subnet route or transit dynamic route in the hub is wholly contained in one of the hybrid spoke's include import ranges, and the hub route doesn't intersect with any of the spoke's exclude import ranges | Hub subnet route or transit dynamic route `10.0.0.0/16` or `10.0.0.0/17`, include import ranges `10.0.0.0/16` and `192.168.0.0/16`, exclude import range `192.168.0.0/24` |  | Hub subnet route or transit dynamic route is imported by the hybrid spoke.  
Subnet route or transit dynamic route in the hub is wholly contained in one of the hybrid spoke's include import ranges, but the hub route intersects with one of the spoke's exclude import ranges | Hub subnet route or transit dynamic route `10.0.0.0/17`, include import range `10.0.0.0/16`, exclude import range `10.0.0.0/24` |  | Hub subnet route or transit dynamic route isn't imported by the hybrid spoke.  
Subnet route or transit dynamic route in the hub is wholly contained in one of the hybrid spoke's exclude import ranges (and consequently is contained in one of its include import ranges) | Hub subnet route or transit dynamic route `10.0.0.0/17`, include import range `10.0.0.0/8`, and exclude import range `10.0.0.0/16` |  | Hub subnet route or transit dynamic route isn't imported by the hybrid spoke.  
  
## What's next

  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and Google Cloud CLI commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
