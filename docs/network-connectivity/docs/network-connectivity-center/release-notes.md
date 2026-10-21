---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/release-notes/
title: Network Connectivity Center release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:07:40.830274+00:00
---

# Network Connectivity Center release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/resources)



Send feedback 

#  Network Connectivity Center release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Network Connectivity Center and Router appliance. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/networkconnectivitycenter-release-notes.xml) directly. 

## October 12, 2026

Fixed

The technical issue causing incorrect billing for [producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview) has been fixed. Starting today, projects with producer VPC spokes linked to Network Connectivity Center hubs will reflect hourly usage fees. Charges on your future billing invoices are based on [Network Connectivity Center pricing](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/pricing#ncc-pricing).

## October 02, 2026

Feature

Network Connectivity Center supports [site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations) in the following country:

  * Poland



## September 29, 2026

Feature

[Network Connectivity Center (NCC)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) support for [Partner Cross-Cloud Interconnect for Amazon Web Services (AWS)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview) is [Generally Available](https://cloud.google.com/products#product-launch-stages).

Billing for [Partner Cross-Cloud Interconnect for Amazon Web Services (AWS)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview) is going to commence over the next 30 days following General Availability. For the most current billing information, see [Network Connectivity Center pricing](https://cloud.google.com/network-connectivity/pricing).

## September 10, 2026

Feature

Support for [global Google APIs for endpoint propagation through Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview#access-gapi-through-psc) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For information about the new quota for propagated global Google APIs, see [NCC quotas](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-quotas).

## August 31, 2026

Feature

IPv6 dynamic routes support for include and exclude [spoke filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview) for hybrid spokes is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Export filters control which subnets or routes a spoke can send to the hub. Import filters control which subnets or routes can be accepted by a spoke from the hub.

## July 10, 2026

Feature

Include and exclude [spoke filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview) for hybrid spokes are [generally available](https://cloud.google.com/products#product-launch-stages).

You can use export filters to control which subnets or routes a spoke can send to the hub. Import filters control which subnets or routes can be accepted by a spoke from the hub.

## June 09, 2026

Feature

[NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview) is [generally available](https://cloud.google.com/products#product-launch-stages).

NCC Gateway lets you enable security functions, such as third-party Security Service Edge (SSE), for cross-cloud network traffic. You can use [Secure Access Connect](https://docs.cloud.google.com/secure-access-connect/docs/overview) with NCC Gateway to securely connect remote workforces to private applications in Google Cloud, on-premises, or other cloud providers and to public applications, like Palo Alto Networks Prisma Access.

For information about pricing, see [NCC Gateway pricing](https://cloud.google.com/network-connectivity/pricing#ncc-gateway-pricing).

## April 14, 2026

Feature

Network Connectivity Center (NCC) support for [Partner Cross-Cloud Interconnect for Amazon Web Services (AWS)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#partner-cross-cloud-interconnect-spokes) is available in [public preview](https://cloud.google.com/products#product-launch-stages).

## March 25, 2026

Feature

Include and exclude [spoke filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview) for hybrid spokes are available in [public preview](https://cloud.google.com/products#product-launch-stages).

You can use export filters to control which subnets or routes a spoke can send to the hub. Import filters control which subnets or routes can be accepted by a spoke from the hub.

## February 19, 2026

Feature

Producer VPC spokes support for [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/get-started/configure-access/networking) is [generally available](https://cloud.google.com/products#product-launch-stages).

## December 17, 2025

Feature

Support for [privately used public IPv4 addresses](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#privately-used-public-ip-addresses) is [generally available](https://docs.cloud.google.com/products#product-launch-stages) in Network Connectivity Center.

This feature lets you exchange privately used public IPv4 addresses with VPC spokes and producer VPC spokes.

## December 16, 2025

Feature

Network Connectivity Center supports [site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations) in the following countries:

  * Brazil
  * Indonesia
  * South Africa



## August 29, 2025

Feature

Static routes for Network Connectivity Center are available in [GA](https://cloud.google.com/products#product-launch-stages).

You can use static routes to define the next hop along the path that network traffic takes to reach a given destination. For more information about using static routes with Network Connectivity Center, see the [Static routes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/static-routes-overview).

## August 25, 2025

Feature

[IPv4 and IPv6 address range filtering for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update-spoke-ipv4) is available in [GA](https://cloud.google.com/products#product-launch-stages).

This feature lets you change IPv4 and IPv6 address ranges for VPC spokes that are exported to a hub.

## August 18, 2025

Feature

You can allow the exchange of [privately used public IPv4 addresses](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#privately-used-public-ip-addresses) with VPC spokes and producer VPC spokes.

## August 13, 2025

Change

[Site-to-site data transfer locations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations) in the following countries have been added to Network Connectivity Center: 

  * Qatar
  * Switzerland



## June 26, 2025

Feature

Static routes for Network Connectivity Center are available in [public preview](https://cloud.google.com/products#product-launch-stages).

You can use static routes to define the next hop along the path that network traffic takes to reach a given destination. For more information about using static routes with Network Connectivity Center, see the [Static routes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/static-routes-overview).

## June 09, 2025

Issue

Routes that NCC Gateway advertises don't show up in the list of a VPC network's effective routes.

## June 04, 2025

Announcement

[NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview) is available in [public preview](https://cloud.google.com/products#product-launch-stages).

NCC Gateway is a regional product that enables security functions such as third-party Security Service Edge (SSE) for Cross-Cloud Network traffic. You can use [Secure Access Connect](https://docs.cloud.google.com/secure-access-connect/docs/overview) with NCC Gateway to securely connect remote workforces to private applications in Google Cloud, on-premises, or other cloud providers and to public applications, like Palo Alto Networks Prisma Access and Symantec Cloud Secure Web Gateway.

## May 08, 2025

Feature

You can use custom constraints to define your own restrictions on Google Cloud services for Network Connectivity Center resources. To learn about which Network Connectivity Center resources support custom constraints, and some sample use cases, see [Use custom organization policies for Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/org-policy-constraints).

This feature is available in [General Availability](https://cloud.google.com/products#product-launch-stages) for the following resources:

  * **Hubs**
  * **Spokes**



It is available in [Public preview](https://cloud.google.com/products#product-launch-stages) for the **Groups** resource.

## April 29, 2025

Feature

[IPv4 address range filtering for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update-spoke-ipv4) is available in [public preview](https://cloud.google.com/products#product-launch-stages).

This feature lets you change IPv4 address ranges for VPC spokes that are specified to be exported to hub.

## April 07, 2025

Feature

IPv6 subnet exchange is [generally available](https://cloud.google.com/products#product-launch-stages).

You can use export filters to configure a VPC spoke to exchange [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) or both IPv4 and IPv6 subnet ranges. For more information, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).

## March 27, 2025

Change

Site-to-site data transfer locations in the following countries have been added to Network Connectivity Center: 

  * Belgium
  * Canada
  * Chile
  * Finland
  * Israel
  * Mexico
  * Sweden



## March 11, 2025

Feature

VPC spoke updates for IPv6 subnet exchange is available in [public preview](https://cloud.google.com/products#product-launch-stages).

You can update, or propose updates to, an existing VPC spoke to enable or disable the exchange of IPv6 subnet ranges. For information about updating spokes, see [Update whether a VPC spoke exports IPv6 subnet ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update-spoke-ipv6). For information about accepting proposed updates to spokes, see [Review proposed spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes).

## February 27, 2025

Feature

[Producer VPC Spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview) is [generally available](https://cloud.google.com/products#product-launch-stages).

If you have a VPC network that consumes a service offered through private services access, you can use a Network Connectivity Center producer VPC spoke to make the service reachable by other spokes on a hub.

## February 26, 2025

Issue

[Private Service Connect connection propagation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) is asynchronous after spoke creation or deletion. When a VPC spoke is removed from a hub, it can take some time to update propagated Private Service Connect connections. While the Private Service Connect propagation connection update is in progress, traffic from the VM within the VPC network can flow to the backend, even after the VPC spoke is added to a new hub. To avoid this issue, we recommend that before adding the spoke to another hub, make sure that all of the propagation status entries for the VPC network in the previous hub, whether as a source spoke or a target spoke, are deleted.

Feature

[Private Service Connect connection propagation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) is [generally available](https://cloud.google.com/products#product-launch-stages). 

Connection propagation through the Network Connectivity Center hub provides access to Private Service Connect endpoints from other VPC networks.

## January 30, 2025

Feature

[Route exchange with VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes) is [generally available](https://cloud.google.com/products#product-launch-stages). 

This feature lets you connect VPC spokes and hybrid spokes, such as Cloud Interconnect VLAN attachments, HA VPN tunnels, and Router appliance VMs on the same hub.

Note that you are billed for Advanced Data Networking (ADN) for traffic originating from Google Cloud Platform egressing through hybrid spokes.

Issue

See the following known issues for dynamic route exchange:

  * **Routing VPC networks that are also VPC spokes** : A routing VPC network should typically contain hybrid spokes. However, if you do configure a routing VPC network as a VPC spoke, the following limitations apply: 
    * A routing VPC network can also be a VPC spoke only if there are no other routing VPC networks on the hub. A hub supports two or more routing VPC networks only when none of the routing VPC networks are VPC spokes.
    * The site-to-site data transfer setting is not honored for hybrid spokes in a routing VPC network that is also a VPC spoke.
  * **Dynamic route interaction rules** : Within a routing VPC network, for each unique dynamic route destination with a next hop in a hybrid spoke, you must ensure that all other dynamic routes, regardless of priority, whose destinations exactly match or fit within the unique dynamic route destination, have next hop Cloud VPN tunnels or VLAN attachments also in a hybrid spoke. Further, you must ensure that those hybrid spokes use the same site-to-site data transfer setting (either enabled or disabled). 
    * If only some next hops for dynamic routes with a common destination are in hybrid spokes, Network Connectivity Center can't reliably exchange dynamic routes that use that destination with VPC spokes on the hub. Consequently, VPC spokes might not receive those dynamic routes.
    * Network Connectivity Center doesn't perform ECMP among all next hops of hybrid spoke dynamic routes if some hybrid spokes have site-to-site data transfer enabled but other hybrid spokes have site-to-site data transfer disabled. If dynamic routes with a common destination are in hybrid spokes without matching site-to-site data transfer settings, next hops for site-to-site data transfer or for connectivity between VPC spokes and on-premises networks might not be what you expect.
  * **Dynamic route and static route interaction rules** : Within a routing VPC network, for each unique dynamic route destination that has a next hop in a hybrid spoke, you must ensure that no local static routes exist, regardless of priority, whose destinations exactly match or fit within the dynamic route destination. 
    * If a local static route in the routing VPC network has the same destination as a hybrid spoke dynamic route, VPC spokes might lose connectivity to the dynamic route destination.
    * If a local static route in a routing VPC network has a destination that fits within the destination of a hybrid spoke dynamic route, VPC spokes lose connectivity to the static route destination.



## December 19, 2024

Feature

IPv6 subnet exchange is available in [public preview](https://cloud.google.com/products#product-launch-stages).

You can use export filters to configure a VPC spoke to exchange [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) or both IPv4 and IPv6 subnet ranges. For more information, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).

## October 03, 2024

Feature

[Producer VPC Spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview) is now available in [public preview](https://cloud.google.com/products#product-launch-stages).

If you have a VPC network that consumes a service offered through private services access, you can use a Network Connectivity Center producer VPC spoke to make the service reachable by other spokes on a hub.

## August 30, 2024

Feature

[Preset topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#preset-topologies) and [include export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges) are [generally available](https://cloud.google.com/products#product-launch-stages). 

Preset topologies let you specify the connectivity configuration across all VPC spokes. You can choose between mesh or star preset topologies. Include export filters lets you limit connectivity by specifying a list of permitted CIDR ranges, thereby blocking all but the permitted IP address ranges.

## June 27, 2024

Feature

[Route exchange with VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes) is now available in [public preview](https://cloud.google.com/products#product-launch-stages). 

This feature lets you lets you connect VPC spokes and hybrid spokes, such as Cloud Interconnect VLAN attachments, HA VPN tunnels, and Router appliance VMs on the same hub.

## June 20, 2024

Feature

[Include export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges) is now available in [public preview](https://cloud.google.com/products#product-launch-stages). 

This feature lets you limit connectivity by specifying a list of permitted CIDR ranges, thereby blocking all but the permitted IP address ranges.

## June 14, 2024

Feature

[Private Service Connect connection propagation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) is now available in [public preview](https://cloud.google.com/products#product-launch-stages). 

The propagation of Private Service Connect services through the Network Connectivity Center hub enables VPC-hosted services in private VPC networks to be reachable across VPC networks.

## May 29, 2024

Feature

[Preset topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#preset-topologies) are now available in [public preview](https://cloud.google.com/products#product-launch-stages). Network Connectivity Center lets you specify connectivity configuration across all VPC spokes.

## November 16, 2023

Issue

The Advanced Data Networking (ADN) traffic is accounted only for large-sized flows (approximately >20 Kbps) that cross VPC boundaries. Currently, small-sized flows are not accounted.

## November 08, 2023

Announcement

[Connecting VPC networks by using Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) is now [generally available](https://cloud.google.com/products#product-launch-stages).

This feature lets you connect two or more VPC networks, represented as spokes, to a hub in the same or a different project for full mesh connectivity.

## September 19, 2023

Fixed

The issue that [you cannot get the status of a long-running operation for a spoke without the `networkconnectivity.operations.get` IAM permission in the spoke project](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/release-notes#August_08_2023) is now resolved.

The new API and `gcloud` commands are documented on the [Review proposed VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#accept_a_spoke_proposal) page. The previous API methods and `gcloud` commands are now deprecated.

## August 08, 2023

Issue

The [`AcceptSpoke`](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#accept_a_spoke_proposal) and [`RejectSpoke`](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#reject-a-spoke-proposal) API methods and the `network-connectivity spokes accept` and `network-connectivity spokes reject` CLI commands have the following usability issue:

  * As the user, if you do not have the `networkconnectivity.operations.get` IAM permission in a spoke project, you cannot [get the status](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.operations/get) of a long-running operation for that spoke.



The issue is being worked on. The workaround is that the spoke administrator can grant the required permissions to the appropriate hub administrator. For information about granting permissions, see [Give access](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-give-access).

## July 12, 2023

Feature

[Connecting VPC networks by using Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

This feature lets you connect two or more VPC networks, represented as spokes, to a hub in the same or a different project for full mesh connectivity.

## May 31, 2023

Feature

Cross-Cloud Interconnect is now [generally available](https://cloud.google.com/products#product-launch-stages). You can use a Cross-Cloud Interconnect connection to peer your Google Virtual Private Cloud (VPC) network with your network that's hosted by a supported cloud service provider. You can also use Cross-Cloud Interconnect VLAN attachments as part of a site-to-site data transfer strategy.

For example, after you configure a VLAN attachment for your Cross-Cloud Interconnect connection, you can create a Network Connectivity Center spoke to represent the attachment. If the spoke has site-to-site data transfer enabled, you can then transfer data between your remote cloud network and your other external sites. Other external sites can include your on-premises network or your network in other clouds.

For information about the cloud service providers that Cross-Cloud Interconnect supports, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview). For information about site-to-site data transfer, see the [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).

Site-to-site data transfer is supported only in [certain locations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).

## November 09, 2022

Change

The Google Cloud console now lets you do all of the following:

  * See a list of existing hubs
  * Create multiple hubs
  * Edit an existing hub's description and/or labels



Previously, you could complete these actions only by using the Google Cloud CLI or the API.

Also, the Network Connectivity Center [Quotas](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-limits) page has been updated to describe the limit of 60 hubs per project.

For more information about creating and managing hubs, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#working-with-hubs).

## February 23, 2022

Feature

Networking Connectivity Center now supports the use of a third-party network virtual appliance in any Google Cloud region for the following use cases:

  * [Providing site-to-cloud connectivity](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/site-to-cloud)
  * [Providing connectivity or managing traffic between VPC networks](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/firewall-topology)



A third-party network virtual appliance could be an SD-WAN router, a firewall appliance, a load balancer, or another appliance, as long as it uses BGP. After you create a Network Connectivity Center spoke to represent your router appliance instance, it can exchange routes dynamically with Cloud Router.

To view a list of partners whose solutions are integrated with Network Connectivity Center, see [Network Connectivity Center partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).

For more information about Network Connectivity Center, see the [product overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

## October 26, 2021

Fixed

The issue reported on [Sept. 30, 2021,](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/release-notes#September_30_2021) has been resolved. Cloud DNS forwarding services and Private Google Access can now be accessed through Router appliance spokes.

## October 18, 2021

Announcement

Network Connectivity Center is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see the [Network Connectivity Center overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

Fixed

It is now possible to add or remove router appliance instances from an existing spoke, as long as you don't try to add instances that belong to a different VPC network. For details, see [Working with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).

## September 30, 2021

Issue

Cloud DNS forwarding services and Private Google Access cannot be accessed through Router appliance spokes. This issue is being worked on.

## September 29, 2021

Change

Network Connectivity Center includes new limits on the number of underlying resources that can be associated with a spoke. For information about the new limits, see [Network Connectivity Center quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-limits).

Fixed

Previously, if you used a Router appliance spoke to connect more than 1,000 VMs, you might have experienced problems establishing BGP sessions between the router appliance instance and the Cloud Router. This issue has been resolved.

## September 07, 2021

Fixed

Previously, if you used a Router appliance spoke to connect more than 1,000 VMs, you might have experienced problems establishing BGP sessions between the router appliance instance and the Cloud Router. This issue has been resolved.

## September 02, 2021

Announcement

You can now create Router appliance spokes by using the Google Cloud Console. For more information, see [Working with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-ra-spoke).

## August 23, 2021

Change

The Spoke Admin role now includes the following permissions:

  * `networkconnectivity.hubs.get`
  * `networkconnectivity.hubs.list`



For full details about Network Connectivity Center permissions, see [Access control](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control).

## July 20, 2021

Announcement

Network Connectivity Center now supports VPC Service Controls. For details, see [Protecting resources with VPC Service Controls](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#protecting_resources_with).

## July 09, 2021

Change

Network Connectivity Center now includes hard limits on the number of resources that can be linked to an individual spoke. For details, see [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas).

## June 28, 2021

Change

It's no longer possible to add or remove router appliance instances to or from an existing spoke. Instead, you must delete and re-create the spoke to include the router appliance instances that you want the spoke to contain. This issue is being worked on.

## June 11, 2021

Issue

If you use a Router appliance spoke to connect more than 1,000 VMs, you might be unable to establish BGP sessions between the router appliance instance and Cloud Router. The 1,000-VM limit includes any VMs that are accessible through VPC Network Peering.

## May 26, 2021

Feature

The Cloud documentation now includes a [list of partners](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/partners) whose solutions are integrated with Network Connectivity Center.

## May 25, 2021

Change

You can now use the Cloud Console to create hubs and spokes in Network Connectivity Center.

## March 09, 2021

Feature

[Router appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview) for Network Connectivity Center is available in Preview.

## January 25, 2021

Feature

Network Connectivity Center is now available in Preview.

For more information, see the [Network Connectivity Center overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
