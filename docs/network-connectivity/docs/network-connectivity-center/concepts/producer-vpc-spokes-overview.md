---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview/
title: Producer VPC spokes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:04.067123+00:00
---

# Producer VPC spokes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Producer VPC spokes Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of producer Virtual Private Cloud (VPC) spokes in Network Connectivity Center (NCC). 

## Introduction

Some service providers offer managed services by using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access). Private services access uses a [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering) connection between a producer VPC network and your VPC network. NCC supports adding select producer VPC networks to a hub when you add your VPC network to the hub as a VPC spoke. Producer VPC networks that are added to a hub are called _producer VPC spokes_.

Services in a producer VPC spoke remain accessible to clients in your VPC network to which the producer VPC network is peered. Additionally, services in a producer VPC spoke are accessible by other VPC spokes on the hub, subject to spoke group and export filters.

Producer VPC spokes support the following services:

  * [Google services offered by private services access](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services)

  * [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/get-started/configure-access/networking)




## How it works

When you create a producer VPC spoke, you provide the following:

  * The existing VPC spoke of your consumer network that is peered with the producer network.
  * The name of the peering connection.



Then, NCC uses that information to identify the VPC network of the service producer and add a corresponding producer VPC spoke to a hub in your project.

After the producer VPC spoke is part of the hub, its subnet routes are exported and the other spokes on that hub can access its services.

### Example configuration

The example configuration in the following diagram includes:

  * A _Service producer network_ that is a producer VPC spoke on the hub.
  * A _Peered consumer network_ that is a VPC spoke on the hub.
  * Additional networks, _Network 3_ and _Network 4_ , that are also VPC spokes on the hub.



All of the networks attached to the hub as VPC spokes can access the services in the producer network:

  * The peered consumer network continues to access services by using the subnet routes exported from the service producer network through the existing VPC Network Peering connection.
  * Network 3 and Network 4 have the same access to services in the producer network through NCC. The subnet routes from the service producer network are exported to the hub and advertised to the VPC spokes associated with Networks 3 and 4.

[ ![NCC producer VPC spoke.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/producer-vpc-spokes.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/producer-vpc-spokes.svg) NCC producer VPC spoke (click to enlarge).

## Supported services

For a list of supported services, see [Supported services for producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-supported-services).

## Considerations

The following sections describe considerations for using producer VPC spokes.

### Shared properties with VPC spokes

Producer VPC spokes are a type of VPC spoke, which means they inherit most of the properties of VPC spokes described in the [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). For example, both spoke types do the following:

  * Connect a VPC network to an NCC hub.
  * Export subnet routes to the NCC hub, which advertises those routes to other VPC spokes and [routing VPC networks](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#routing-vpc). This includes any new subnets added to the producer VPC spoke, which means that other spokes can access newly provisioned services from a producer VPC spoke.
  * Import dynamic routes from the NCC hub routing table, providing connectivity to hybrid spokes. The hub [topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#preset-topologies) must also support dynamic route exchange.
  * Limit which subnets are exported by using [export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).
  * Use the same [NCC quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas), including:

    * Number of active VPC spokes per hub
    * Number of subnet routes per hub route table

If adding a producer VPC spoke could result in the hub exceeding the limit of either of the preceding quotas, NCC prohibits you from adding the producer VPC spoke. To reduce the usage of the _number of subnet routes per hub route table_ quota, you can use export filters to limit which of the subnets in the producer VPC spoke are exported.




The [limitations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#limitations) of VPC spokes also apply to producer VPC spokes.

### Properties unique to producer VPC spokes

Producer VPC spokes have the following unique properties and requirements:

Property | Description  
---|---  
Dependencies |  Creating a producer VPC spoke requires that you have the following existing resources and connections:

  * A VPC network that consumes a supported service from a producer network through VPC Network Peering.
  * The consumer VPC network is a VPC spoke on the hub.

  
Creation steps |  When you create a producer VPC spoke, you don't enter the service producer network directly. Instead, you enter:

  * The VPC spoke of your consumer network that is peered with the producer network.
  * The name of the peering connection.

If your hub is configured for star topology, the producer VPC spoke and its corresponding VPC spoke must belong to the same group.  
Resource locations |  A producer VPC spoke and its backing VPC network are in different projects:

  * The service producer's VPC network is in a producer-owned project that you don't have access to.
  * The producer VPC spoke resource is created in your project, and this is always the same project as the VPC spoke of your peered consumer network.

  
Connectivity exceptions |  Creating a producer VPC spoke does _not_ establish connectivity through NCC between the following resources:

  * The producer VPC spoke and other producer VPC spokes.
  * The producer VPC spoke and the VPC spoke of its peered consumer network that you entered at creation time. Instead, these two networks remain connected through their existing VPC Network Peering connection.

  
Private Service Connect connection propagation |  Private Service Connect connection propagation isn't supported on producer VPC spokes.  
Internal passthrough Network Load Balancer exceptions |  Static routes in a producer VPC don't resolve to an internal passthrough Network Load Balancer in a NCC peer; the load balancer must be in the same VPC or a legacy peer. [`PER_SESSION` connection tracking mode](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#tracking-mode) isn't supported.  
  
### Avoid overlap with allocated IP ranges

If you want to create a producer VPC spoke for a supported service offered through private services access, consider the following:

  * NCC does not check for overlaps with allocated IP ranges. Ensure that the IP address ranges of the VPC spokes on your hub don't overlap with an allocated IP range configured for private services access.
  * If your VPC spokes overlap with allocated IP ranges, private services access might not be able to create new resources when needed and you'll get an error. To resolve this, expand or modify the allocated IP range.



For more information, see [Allocated IP address ranges for services](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range).

## What's next

  * [Create a producer VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/create-producer-vpc-spoke)
  * [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting)
  * [Get details about API and `gcloud` commands](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
