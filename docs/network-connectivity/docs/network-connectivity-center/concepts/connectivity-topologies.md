---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies/
title: Preset connectivity topologies \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:58.585963+00:00
---

# Preset connectivity topologies  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Preset connectivity topologies Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Network Connectivity Center (NCC) hub, you can choose one of the following preset _topologies_. The mesh topology is the default.

  * Mesh topology
  * Star topology 
  * Hybrid inspection topology 



After you create a hub with a preset topology, you can't change the topology.

## Spoke groups

Depending on the topology, a hub supports one or more _spoke groups_. The types of spokes that can be in each spoke group also depend on the hub topology. For all topologies, the following characteristics apply:

  * Each spoke group is a routing domain with its own route table. The spoke group's route table is updated automatically as spokes are added to or removed from the spoke group.
  * Each spoke added to a hub can only belong to one spoke group.
  * NCC automatically accepts spokes that are added from the same project as the hub.
  * NCC offers both automatic acceptance and spoke proposal review options when adding VPC spokes that are in different projects from the hub. For more information, see [VPC spokes in a different project from a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-spokes-different-project).



For steps to configure topologies and spoke groups, see [Configure a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub).

## Mesh topology

With mesh topology, all spokes on the hub belong to a single spoke group.

If you create a hub without explicitly specifying a topology, the hub topology defaults to mesh. When you add two or more [workload VPC networks](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#workload-vpc) to the hub as VPC spokes, each VPC spoke exports its subnet routes according to the configured export include and export exclude filters. For more information about subnet route exchange among VPC spokes, see [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview).

Mesh topology also supports high scale network connectivity between VPC spokes and hybrid spokes. Spoke administrators or network administrators for a routing VPC network that contains hybrid spokes must configure the advertisement of subnet routes received from VPC spokes. For more information, see [Establishing connectivity between hybrid spokes and VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#connectivity-between-hybrid-and-vpc-spokes).

The following diagram shows a hub that uses the mesh topology and has three VPC spokes.

[ ![NCC mesh topology connectivity.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/ncc-mesh-topology.png)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/ncc-mesh-topology.png) NCC mesh topology connectivity (click to enlarge).

### Supported spoke types

Mesh topology supports the following spoke types in its single spoke group:

  * [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview)
  * [producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview)
  * [hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid_spokes)
  * [NCC Gateway spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview)



The [`gcloud network-connectivity hubs groups list --hub` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/list) only returns the single default spoke group when using mesh topology.

## Star topology

The star topology has two spoke groups that provide network segmentation using separate route tables for each spoke group. The following route table rules apply to each spoke group:

  * The _center_ spoke group permits routes in its route table that let resources in spokes of the center group communicate with resources in spokes of either the center group or edge group.
  * The _edge_ spoke group only permits routes in its route table that let resources in spokes of the edge group communicate with resources in spokes of the center group. NCC prohibits routes in the edge spoke group route table that would provide connectivity among different spokes in the edge group.



Subject to the spoke group route table rules, spoke administrators or network administrators can do the following.

  * Use [export include](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges) and [export exclude filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#exclude-export-ranges) to control which subnet ranges a VPC spoke exports to the route table of the spoke group that the VPC spoke belongs to.

  * Control which VPC spoke subnet ranges are exported on the BGP sessions of Cloud Routers in hybrid spokes. For more information, see [Establishing connectivity between hybrid spokes and VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#connectivity-between-hybrid-and-vpc-spokes).




The following diagram shows star topology connectivity among four VPC spokes. The `center-vpc-a` and `center-vpc-b` VPC spokes are members of the center spoke group, and the `edge-vpc-c` and `edge-vpc-d` VPC spokes are members of the edge spoke group.

[ ![NCC star topology connectivity.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/ncc-star-topology-1.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/ncc-star-topology-1.svg) NCC star topology connectivity (click to enlarge).

### Supported spoke types

Star topology supports VPC spokes, producer VPC spokes, hybrid spokes, and NCC Gateway. The following table shows the spoke groups that are supported according to the spoke type:

Spoke | Can be in the center spoke group | Can be in the edge spoke group  
---|---|---  
VPC spoke |  |   
Producer VPC spoke |  |   
Hybrid spoke with site-to-site data transfer _disabled_ |  |   
Hybrid spoke with site-to-site data transfer _enabled_ |  |   
NCC Gateway spoke  |  |   
  
The [`gcloud network-connectivity hubs groups list --hub` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/list) returns the _center_ and _edge_ groups when using star topology.

#### Hybrid spoke compatibility with star topology

A hub configured to use the star topology enforces the following limitations on its hybrid spokes:

  * Hybrid spokes with site-to-site data transfer enabled must be in the center spoke group.
  * Hybrid spokes without site-to-site data transfer enabled can be in either the center spoke group or the edge spoke group.



For detailed information about how to configure the mesh or star topology for your VPC spokes, see [Configure a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub).

## Hybrid inspection topology

The hybrid inspection topology has the following four spoke groups that provide network segmentation and packet inspection capabilities:

  * The _prod_ spoke group is designed for production workloads.
  * The _non-prod_ spoke group is designed for non-production workloads.
  * The _services_ spoke group is designed for services that are essential to both production and non-production workloads.
  * The _gateways_ spoke group supports NCC Gateway spokes that serve as security checkpoints.



The following rules apply to the route table for each spoke group:

  * The prod spoke group permits routes in its route table that let resources in spokes of the prod group communicate with resources in spokes of the prod group, the services group, or the gateway group. NCC prohibits routes in the prod spoke group route table that would provide connectivity to spokes in the non-prod group.

  * The non-prod spoke group permits routes in its route table that let resources in spokes of the non-prod group communicate with resources in spokes of the non-prod group, the services group, or the gateway group. NCC prohibits routes in the non-prod spoke group route table that would provide connectivity to spokes in the prod group.

  * The services spoke group permits routes in its route table that let resources in spokes of the services group communicate with resources in spokes of any spoke group.

  * The gateways spoke group permits routes in its route table that let each NCC Gateway spoke communicate with resources in spokes of any spoke group.




Subject to the spoke group route table rules, spoke administrators or network administrators can do the following:

  * Use [export include and export exclude filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) to control which subnet ranges a VPC spoke exports to the route table of the spoke group that the VPC spoke belongs to.

  * Create custom route advertisements on the BGP sessions of Cloud Routers that manage hybrid connections in NCC Gateway spokes. These custom route advertisements can include VPC spoke subnet ranges. For more information, see [Add hybrid connections to NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments).

  * Control which VPC spoke subnet ranges are exported on the BGP sessions of Cloud Routers in hybrid spokes. For more information, see [Establishing connectivity between hybrid spokes and VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#connectivity-between-hybrid-and-vpc-spokes).




### Security Service Edge availability

Security Service Edge (SSE) packet inspection is available only for traffic that is routed between an NCC Gateway spoke in the gateways spoke group and a spoke in the prod group, the non-prod group, or the services group.

**Note:** SSE packet inspection isn't available for traffic that is routed using Cloud Interconnect VLAN attachments, HA VPN tunnels, or Router appliances in a hybrid spoke because hybrid spokes must be a member of the prod group, the non-prod group, or the services group.

The following table summarizes whether routing is permitted, and whether SSE packet inspection is available, for traffic routed between spokes in different spoke groups.

| Destination resource spoke  
---|---  
Source resource spoke | in the **prod** group | in the **non-prod** group | in the **services** group | in the **gateways** group  
in the **prod** group | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection  
in the **non-prod** group | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection  
in the **services** group | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection  
in the **gateways** group | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection | routing  
SSE inspection  
  
### Supported spoke types

Hybrid inspection topology supports VPC spokes, producer VPC spokes, hybrid spokes, and NCC Gateway spokes. The following table shows the spoke groups that are supported according to the spoke type.

Spoke | Can be in the prod spoke group | Can be in the non-prod spoke group | Can be in the services spoke group | Can be in the gateways spoke group  
---|---|---|---|---  
VPC spoke |  |  |  |   
Producer VPC spoke |  |  |  |   
Hybrid spoke with site-to-site data transfer _disabled_ |  |  |  |   
Hybrid spoke with site-to-site data transfer _enabled_ |  |  |  |   
NCC Gateway spoke |  |  |  |   
  
The [`gcloud network-connectivity hubs groups list --hub` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/list) returns the prod, non-prod, services, and gateway groups when using hybrid inspection topology.

## What's next

  * To learn about NCC, see [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).
  * To find solutions for common issues, see [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).
  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
