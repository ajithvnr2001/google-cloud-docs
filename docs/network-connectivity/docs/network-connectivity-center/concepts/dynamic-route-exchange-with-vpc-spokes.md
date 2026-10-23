---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes/
title: Route exchange with VPC spokes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:04.730716+00:00
---

# Route exchange with VPC spokes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Route exchange with VPC spokes Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of route exchange between hybrid spokes and Virtual Private Cloud (VPC) spokes in Network Connectivity Center (NCC).

Route exchange with VPC spokes lets you connect VPC spokes and hybrid spokes, such as Cloud Interconnect VLAN attachments, HA VPN tunnels, and Router appliance VMs on the same hub, which enables highly scalable any-to-any network connectivity between all such spokes attached to a single hub. Using VPC spokes and hybrid spokes on the same hub lets you connect multiple on-premises networks and Google Cloud VPC networks.

Route exchange with VPC spokes support IPv4 addressing only.

### Workload VPC networks

A _workload VPC network_ is a VPC network that a spoke administrator adds to a hub as a VPC spoke. A workload VPC network can be a standalone VPC network, or it can be a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) network. A workload VPC network can be located in either the same project as the NCC hub or a different project in the same or another organization.

### Routing VPC networks

A _routing VPC network_ is a VPC network that contains at least one [hybrid spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid_spokes) with Cloud Interconnect VLAN attachments, HA VPN tunnels, or Router appliance VMs.

A routing VPC network can also be connected as a [VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#vpc-spokes) on the same hub as its hybrid spokes.

For [Private Service Connect connection propagation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) to work with hybrid spokes, the routing VPC network must also be added as a VPC spoke.

Each routing VPC network—and the Cloud Interconnect VLAN attachments, HA VPN tunnels, or Router appliance VMs that use the routing VPC network—must be located in the same project as the NCC hub.

## Establishing connectivity between hybrid spokes and VPC spokes

You can establish connectivity between hybrid spokes and VPC spokes by adding _workload VPC networks_ to an NCC hub as VPC spokes, then you add Cloud Interconnect VLAN attachments, HA VPN tunnels, or Router appliance VMs to the same hub as hybrid spokes. The Cloud Interconnect VLAN attachments, HA VPN tunnels, or Router appliance VMs in each hybrid spoke are also associated with one or more _routing VPC networks_ , but the routing VPC networks themselves need not be added to the NCC hub as VPC spokes.

To establish connectivity between hybrid spokes and VPC spokes:

  1. Network administrators for the routing VPC networks must first review the Cloud Router path selection and dynamic routing mode:

     * NCC hybrid spokes only support the Cloud Router legacy best path selection mode. For detailed information about Cloud Router path selection, see [Best path selection modes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#best-path-selection-modes) in the Cloud Router documentation.

     * NCC hybrid spokes support both global and regional dynamic routing modes. The dynamic routing mode of a routing VPC network determines in which regions the NCC dynamic routes are programmed in the VPC spokes:

       * If the dynamic routing mode is regional, NCC dynamic routes from its hybrid spokes are only programmed in the same region as each hybrid spoke.

       * If the dynamic routing mode is global, NCC dynamic routes from its hybrid spokes are programmed in all regions.

The VPC spoke only uses the dynamic routing mode when hybrid spokes reside in the same hub.

  2. Hub administrators do the following:

     * [Create a new NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub).

     * [Give access to the NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-give-access) so that spoke administrators can propose VPC spokes that are located in projects other than the hub's project.

  3. Spoke administrators create VPC spokes and hybrid spokes:

     * [Create a VPC spoke proposal](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke#propose_a_spoke) to attach a workload VPC network to the hub.

     * [Create a Router appliance spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-ra-spoke)

     * [Create a Cloud Interconnect VLAN attachment spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vlan-spoke)

     * [Create a VPN spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpn-spoke)

  4. A hub administrator must [review proposed VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes) that are located in projects other than the hub's project.

  5. Spoke administrators or network administrators for the routing VPC networks must configure advertisement of subnet routes in VPC spokes. Either of the following techniques can be used:

     * A spoke administrator for the hybrid spoke can set the `includeImportRanges` field to `["ALL_IPV4_RANGES"]` in the hybrid spoke resource by using the API. For more information, see the [`LinkedRouterApplianceInstances`](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#linkedrouterapplianceinstances), [`LinkedInterconnectAttachments`](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#linkedinterconnectattachments), and [`LinkedVpnTunnels`](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#linkedvpntunnels) types.

     * A spoke administrator for the hybrid spoke can update the hybrid spoke by using the Google Cloud CLI with the `--include-import-ranges=[ALL_IPV4_RANGES]` flag. For more information, see the [`network-connectivity spokes linked-router-appliances update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--include-import-ranges), [`network-connectivity spokes linked-interconnect-attachments update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--include-import-ranges), and [`network-connectivity spokes linked-vpn-tunnels update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpn-tunnels/update#--include-import-ranges) flags.

     * A network administrator for the routing VPC network can [advertise custom address ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) on the Cloud Routers for the hybrid spokes. The custom ranges can be a list of all subnet IPv4 address ranges of the VPC spokes on the hub, or you can use larger CIDRs that contain the subnet IPv4 address ranges of the VPC spokes.




### Route tables

The NCC hub route table lists all learned dynamic routes from on-premises networks and subnet routes that are reachable from the attached spoke networks through the NCC hub. Hub route tables are read-only resources, fully managed by NCC. For detailed information about how to view the hub route table, see [View the hub route table and routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-hub-route-table).

The hub route table is updated with appropriate route entries when the following events occur:

  * VPC spoke creation or deletion
  * Subnet creation or deletion in attached VPC spokes
  * Hybrid spoke creation or deletion
  * BGP route advertisement or withdrawal from attached hybrid spokes



Each VPC spoke also has a VPC network route table. Each VPC network route table lists all routes that are programmed in the VPC network. For steps to view the VPC route table, see [View the VPC route table](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-route-table).

## Example use cases

The following examples show an NCC hub that contains both hybrid spokes and VPC spokes.

### Overlapping NCC dynamic routes

The following NCC hub has a VPC spoke and two hybrid spokes. Both hybrid spokes connect to an on-premises network that advertises both `192.168.0.0/16` and `192.168.44.10/24`. This example shows how NCC programs overlap dynamic routes in a VPC spoke. For simplicity, this example considers hybrid spokes that are in the same region. The next example, How global dynamic routing mode and MED work together, shows hybrid spokes in two regions.

[ ![Overlapping NCC dynamic routes.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/overlapping-dynamic-routes.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/overlapping-dynamic-routes.svg) Overlapping NCC dynamic routes (click to enlarge).

In the preceding diagram, an on-premises network uses both the `192.168.0.0/16` and `192.168.44.10/24` IP address ranges. The on-premises network connects to two routing VPC networks using two pairs of VLAN attachments in the `us-west1` region of each routing VPC network:

  * The `a-west` hybrid spoke contains the Cloud Routers and VLAN attachments that receive `192.168.0.0/16`. This hybrid spoke sends the `192.168.0.0/16` dynamic routes to the hub.

  * The `b-west` hybrid spoke contains the Cloud Routers and VLAN attachments that receive `192.168.44.10/24`. This hybrid spoke sends the `192.168.44.10/24` dynamic routes to the hub.




The VPC spoke imports four NCC dynamic routes from the hub:

  * Two NCC dynamic routes for `192.168.0.0/16`, both with next hops in the `a-west` hybrid spoke.

  * Two NCC dynamic routes for `192.168.44.10/24`, both with next hops in the `b-west` hybrid spoke.




VMs and other resources in the `us-west1` region of the VPC spoke use the NCC dynamic routes as follows:

  * Packets whose destinations fit within `192.168.44.10/24` are sent to the VLAN attachments in the `b-west` hybrid spoke.

  * Packets whose destinations fit within `192.168.0.0/16`, but not in `192.168.44.10/24`, are sent to the VLAN attachments in the `a-west` hybrid spoke.




### How global dynamic routing mode and MED work together

The following NCC hub has a VPC spoke and two hybrid spokes. The two hybrid spokes are in a single routing VPC network. The on-premises IP address range is `192.168.44.10/24`. This example shows how the multi-exit discriminator (MED) value, dynamic routing mode, and Cloud Router best path selection algorithm control the creation of dynamic routes in both the routing VPC network and in VPC spokes.

[ ![Route prioritization by using MED.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/route-prioritization-using-MED.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/route-prioritization-using-MED.svg) Route prioritization by using MED (click to enlarge).

In the preceding diagram, an on-premises network uses the `192.168.44.10/24` IP address range. Four VLAN attachments, two in `us-west1` and two in `us-east1`, connect the on-premises network to a routing VPC network, `routing-vpc-network`. BGP sessions for the two VLAN attachments in each region are managed by Cloud Routers in the same region.

The routing VPC network is configured as follows:

  * The [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes) is global.
  * The [best path selection mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#best-path-selection-modes) is legacy.
  * The two VLAN attachments in `us-west1` are added as a hybrid spoke (`west-hybrid-spoke`) on the NCC hub.
  * The two VLAN attachments in `us-east1` are added as a hybrid spoke (`east-hybrid-spoke`) on the NCC hub.



The on-premises routers advertise the `192.168.44.10/24` IP address range:

  * Using MED `10` to the BGP sessions for the `west-a` and `east-a` VLAN attachments.
  * Using MED `20` to the BGP sessions for the `west-b` and `east-b` VLAN attachments.



In the routing VPC network, each region's Cloud Router dynamic route control plane and VPC control plane work together to create the following local dynamic routes for `192.168.44.10/24` in each region:

  * In the `us-west1` region, two local dynamic routes have next hops in the region and one next hop in the `us-east1` region:

    * The dynamic route with priority `10` uses the `west-a` VLAN attachment next hop.
    * The dynamic route with priority `20` uses the `west-b` VLAN attachment next hop.
    * The dynamic route with priority `275` uses the `east-a` VLAN attachment next hop. The `east-a` next hop has the highest priority (`10`) in the `us-east1` region, and the inter-regional cost between `us-west1` and `us-east1` is `265`.
  * In the `us-central1` region, both of the local dynamic routes have next hops in different regions:

    * The dynamic route with priority `243` uses the `east-a` VLAN attachment next hop. The `east-a` next hop has the highest priority (`10`) in the `us-east1` region, and the inter-regional cost between `us-central1` and `us-east1` is `233`.
    * The dynamic route with priority `248` uses the `west-a` VLAN attachment next hop. The `west-a` next hop has the highest priority (`10`) in the `us-west` region, and the inter-regional cost between `us-central1` and `us-west1` is `238`.
  * In the `us-east1` region, two local dynamic routes have next hops in the region and one next hop in the `us-west1` region:

    * The dynamic route with priority `10` uses the `east-a` VLAN attachment next hop.
    * The dynamic route with priority `20` uses the `east-b` VLAN attachment next hop.
    * The dynamic route with priority `275` uses the `west-a` VLAN attachment next hop. The `west-a` next hop has the highest priority (`10`) in the `us-west1` region, and the inter-regional cost between `us-east1` and `us-west1` is `265`.



A workload VPC network, `workload-vpc-network`, is added to the same NCC hub as a VPC spoke. NCC creates NCC [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) for `192.168.44.10/24` in each region of the workload VPC network to match the local dynamic routes created in each region of the routing VPC network. The dynamic routing mode and best path selection mode of the workload VPC network aren't relevant because the workload VPC network doesn't contain the Cloud Router resources that manage the BGP sessions for the VLAN attachments.

To control the path from the workload VPC network to the on-premises network, adjust the MED values advertised by the on-premises network for the `192.168.44.10/24` prefix. For details about how NCC dynamic routes interact with subnet routes and other types of dynamic routes, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).

## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and Google Cloud CLI commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
