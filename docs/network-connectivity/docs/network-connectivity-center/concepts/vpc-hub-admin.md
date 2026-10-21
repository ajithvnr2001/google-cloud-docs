---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-hub-admin/
title: Hub administration overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:04.603660+00:00
---

# Hub administration overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-hub-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Hub administration overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the [Network Connectivity Center (NCC) hub administrator role (`roles/networkconnectivity.hubAdmin`)](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#networkconnectivity-roles). An Identity and Access Management (IAM) principal who has the hub administrator role can do the following:

  * [Create a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub) and create Virtual Private Cloud (VPC) spokes for VPC networks that are in the same project as the hub.
  * [Give access to spoke administrators](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-give-access) so they can create VPC spoke proposals for VPC networks located in different projects.
  * [Review, accept, and reject VPC spoke proposals](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes) or [set up _auto-accept_ for spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#manage_auto-accept_for_spoke_groups).
  * [View hub route tables](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-hub-route-table).



Custom roles can also be used if they at least include the same permissions of the NCC hub administrator role.

## How VPC spokes join a hub

If a VPC network and an NCC hub are located in the same project, creating a VPC spoke for the VPC network immediately establishes connectivity to the hub without any additional steps.

If a VPC network and an NCC hub are located in different projects, the process for creating a VPC spoke is as follows:

  1. A hub administrator establishes IAM policy bindings that let spoke administrators in other projects create VPC _spoke proposals_. Note: Hub administrators can change IAM policy bindings at any time. For example, a hub administrator might revoke access later, preventing a spoke administrator from creating additional spoke proposals. This is true when auto-accept for spokes is not enabled.
  2. During hub creation, the hub administrator chooses the connectivity topology between the default mesh topology and star topology.
  3. A spoke administrator [proposes a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke). If the spoke proposal is for a hub that is configured to use the star topology, the spoke administrator assigns the spoke to either the _center_ or the _edge_ group. For mesh topology, all spokes belong to the single default group.
  4. A hub administrator reviews each spoke proposal, and then accepts or rejects the proposal. The following describes how hub connectivity works following accepting or rejecting a proposal: 
     * A spoke becomes active only after a hub administrator accepts the spoke proposal. NCC only provides network connectivity to active spokes.
     * A hub administrator can reject a previously accepted VPC spoke, making the spoke inactive. When a previously active VPC spoke becomes inactive, NCC does not provide network connectivity to the spoke.



## How spoke update proposals work

When a VPC or a producer VPC spoke exists in a project different from the hub, a hub administrator must accept or reject update proposals unless auto-accept for spokes is enabled. These spoke updates can be changes to the include or exclude IPv4 subnet ranges ([Preview](https://cloud.google.com/products#product-launch-stages)).

For more information about updating spokes, see [Update a spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update-spoke).

### Auto-accept projects

A hub administrator can enable auto-accept for spoke groups in a hub. When enabled, VPC spokes located in the auto-accept projects list are added or updated immediately after the VPC spoke creation or update proposal. Manual review and approval from a hub administrator is skipped.

## The hub route table

The hub route table shows subnet routes imported from the VPC spokes. When a new VPC spoke is created, all _local_ subnet routes from the VPC network are exported to the hub _unless_ the spoke administrator uses the [`exclude-export-ranges` flag](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create#--exclude-export-ranges) in the Google Cloud CLI or the `excludeExportRanges` field in the API. For more information, see [subnet route uniqueness](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#subnet-uniqueness).

When you create a new VPC spoke, the following occurs:

  * A spoke _belongs_ to exactly one group.
  * Each group has a corresponding route table.
  * Spokes are _associated_ with that route table.
  * Spoke subnets are _propagated_ to one or more route tables.



Because there is only one default group in a mesh topology connectivity, the subnet routes are propagated to a single hub route table. Spokes connected to a hub that supports star topology belong to one of two different groups, namely, _center_ and _edge_. So, two hub route tables are generated, one associated with each spoke group. Spokes in the center group have their subnet routes _propagated_ to the center and edge route tables. Spokes in the edge group have their subnet routes _propagated_ to the center route table.

For detailed information about connectivity topologies, see [Preset connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).

Google Cloud automatically updates the VPC network route table of each VPC spoke and the NCC hub route table when any of the following occur:

  * You perform [a subnet lifecycle activity](https://docs.cloud.google.com/vpc/docs/routes#subnet-lifecycle), such as adding or deleting a subnet.
  * You add or remove VPC spokes from the hub.



For more information, see [Route tables that show subnet routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#vpc-route-table) and [Routes](https://docs.cloud.google.com/vpc/docs/routes) in the VPC documentation.

## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis). Note: For a Terraform solution that simplifies the setup of NCC hubs and various types of spokes, see the [Terraform examples for NCC](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/tree/main/execution/02-networking/NCC).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
