---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin/
title: Spoke administration overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:42.997534+00:00
---

# Spoke administration overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Spoke administration overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview from the perspective of a Virtual Private Cloud (VPC) spoke administrator.

If the Network Connectivity Center (NCC) hub and VPC spoke are in the same project, VPC spoke administrators must have both of the following Identity and Access Management (IAM) bindings on that project:

  * The [Compute Network Admin role (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin).

  * The [NCC Spoke Admin role (`roles/networkconnectivity.spokeAdmin`)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#networkconnectivity.spokeAdmin).




If the NCC hub and VPC spoke are in different projects, IAM policies must have the following bindings.

  * VPC spoke administrators must have both of the following IAM bindings on the project that contains the VPC network (spoke):

    * The [Compute Network Admin role (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin).
    * The [NCC Spoke Admin (`roles/networkconnectivity.spokeAdmin`)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#networkconnectivity.spokeAdmin).
  * VPC spoke administrators must also have both of the following IAM bindings on the NCC hub or on the project that contains the NCC hub:

    * The [NCC Group User role (`roles/networkconnectivity.groupUser`)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#networkconnectivity.groupUser). You must have the Group User role to add a spoke to a group in star topology.
    * The [NCC Hub & Spoke Viewer role (`roles/networkconnectivity.hubViewer`)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#networkconnectivity.hubViewer).



You can also use custom roles as long as the custom role includes the same permissions as the predefined roles listed earlier.

When a VPC network and the NCC hub are located in different projects, a VPC spoke administrator must create a spoke proposal to request that a VPC network join the hub. A hub administrator reviews the proposal. If the hub administrator accepts the proposal, the VPC network is connected to the hub. A hub administrator can also reject spoke proposals. Spoke administrators can check the status of a VPC spoke proposal at any time.

You can propose updates to an existing VPC spoke to change the set of subnet ranges that are exported to hub route tables.

For more information, see the following sections.

  * [Propose a VPC spoke in a different project](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke)
  * [Check the status of a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status)
  * [View the VPC route table](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-route-table)
  * [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview)
  * [Change exported subnet address ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update-spoke-export-ranges) ([Preview](https://cloud.google.com/products#product-launch-stages))



## Subnet route uniqueness

Similar to VPC Network Peering, Google Cloud prohibits subnet IP address range conflicts among VPC spokes connected to a NCC hub. A subnet IP address range _conflicts_ with another subnet IP address range when one of the following is true:

  * A subnet IP address range in one VPC network _exactly matches_ a subnet IP address range in another VPC network.
  * A subnet IP address range in one VPC network _fits within_ a subnet IP address range in another VPC network.
  * A subnet IP address range in one VPC network _contains_ a subnet IP address range in another VPC network.



VPC spokes can't export conflicting subnet IP address ranges into the same NCC hub. You can use the [`exclude-export-ranges` flag](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create#--exclude-export-ranges) in the Google Cloud CLI or the `excludeExportRanges` field in the API to prevent a subnet IP address range from being shared from a VPC spoke into an NCC hub. For example, suppose you have two VPC networks that you want to connect to the same NCC hub:

  * The first VPC network has a subnet whose primary internal IPv4 address range is 100.64.0.0/16, resulting in a subnet route for 100.64.0.0/16.
  * The second VPC network has a subnet with a secondary internal IPv4 address range of 100.64.0.0/24, resulting in a subnet route for 100.64.0.0/24.



The two subnet routes have conflicting subnet IP address ranges because 100.64.0.0/24 fits within 100.64.0.0/16. You can't connect both networks as VPC spokes to the same NCC hub unless you resolve the conflict. You can use one of the following strategies to resolve the conflict:

  * Either exclude the 100.64.0.0/16 IP address range when you attach the first VPC network to the hub, or exclude the 100.64.0.0/24 IP address range when you attach the second VPC network to the hub.
  * Exclude 100.64.0.0/16 or the whole [RFC 6598](https://tools.ietf.org/html/rfc6598) space, 100.64.0.0/10, when you attach each VPC network.



### Interaction with VPC Network Peering subnet routes

[Peering subnet routes](https://docs.cloud.google.com/vpc/docs/routes#peering-subnet-routes) are those that are exchanged between VPC networks connected using VPC Network Peering. Even though peering subnet routes are never exchanged among VPC spokes connected to an NCC hub, you still need to take peering subnet routes into consideration. From the perspective of each VPC spoke, all local subnet routes, imported peering subnet routes, _and_ imported NCC subnet routes can't conflict.

To illustrate this concept, consider the following configuration:

  * VPC network `net-a` is a VPC spoke connected to an NCC hub.
  * VPC network `net-b` is a VPC spoke connected to the same NCC hub.
  * VPC networks `net-b` and `net-c` are connected to each other using VPC Network Peering.



Suppose that a local subnet IP address range for 100.64.0.0/24 exists in `net-c`. This creates a local subnet route in `net-c` _and_ a peering subnet route in `net-b`. Even though the peering subnet route for the 100.64.0.0/24 IP address range is not exported into the NCC hub, its existence in `net-b` prevents `net-b` from being able to import a NCC route whose destination exactly matches 100.64.0.0/24, fits within 100.64.0.0/24, or contains 100.64.0.0/24. Consequently, no local subnet routes for 100.64.0.0/24, 100.64.0.0/25, or 100.64.0.0/16 can exist in `net-a` _unless_ you configure `net-a` to not export the conflicting range.

## Route tables that show subnet routes

Google Cloud shows NCC subnet routes imported from VPC spokes in two route tables:

  * The [NCC hub route table](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-hub-admin#hub-route-table).
  * The [VPC network route table](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes) for each VPC (spoke) network.



Google Cloud automatically updates the VPC network route table of each VPC spoke and the NCC hub route table when one of the following conditions is met:

  * When you perform [a subnet route lifecycle activity](https://docs.cloud.google.com/vpc/docs/routes#subnet-lifecycle), like adding or deleting a subnet.
  * When VPC spokes are added to or removed from the hub.



In VPC network route tables, each imported route from other VPC spokes appears as a _NCC subnet route_ whose next hop is the NCC hub. These NCC subnet routes have names that begin with the `ncc-subnet-route-` prefix. To see the actual next hop for an imported NCC subnet route, you can [view the NCC hub route table](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-hub-route-table) or you can [view the VPC network route table](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes) of the VPC spoke that exports the subnet route into the NCC hub.

For more information about VPC routes, see [Routes](https://docs.cloud.google.com/vpc/docs/routes) in the VPC documentation.

## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To create a spoke in a project different from the hub, see [Propose a VPC spoke in a different project](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
