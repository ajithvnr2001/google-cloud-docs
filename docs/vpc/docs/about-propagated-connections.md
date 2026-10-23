---
url: https://docs.cloud.google.com/vpc/docs/about-propagated-connections/
title: About propagated connections \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:45.395786+00:00
---

# About propagated connections  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-propagated-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About propagated connections

This page provides an overview of Private Service Connect propagated connections.

With propagated connections, services that are accessible in one consumer [VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#vpc-spokes) through [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) can be privately accessed by other consumer VPC spokes that are connected to the same Network Connectivity Center hub. Propagated connections let consumer VPC spokes access managed services in producer VPC networks as if the two VPC networks were directly connected through endpoints.

Propagated connections provide the following benefits:

  * You can use a common services VPC network to simplify the deployment of Private Service Connect endpoints.
  * You can manage which services are accessible to individual VPC spokes through the NCC hub.



For an overview of propagated connections from the NCC perspective, see [Private Service Connect propagated connections through Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview).

[ ![](https://docs.cloud.google.com/static/vpc/images/private-service-connect-propagated-connections-overview.svg)](https://docs.cloud.google.com/static/vpc/images/private-service-connect-propagated-connections-overview.svg) VPC networks use propagated connections to access published services that are connected to a common services VPC network (click to enlarge). 

For example, in figure 1, the VPC spoke `Common services VPC` contains two endpoints. Two other VPC spokes are attached to the same NCC hub as `Common services VPC`. Because propagated connections are enabled for the hub, there are two propagated connections in `Consumer VPC 2` and two propagated connections in `Consumer VPC 3`. These propagated connections let workloads in `Consumer VPC 2` and `Consumer VPC 3` access managed services in `Producer VPC 1` as if they were directly connected through the endpoints.

No propagated connections are created for `Endpoint 3` because the IP range of that endpoint's subnet is excluded from export and not advertised to other VPC spokes.

## Configuring propagated connections

Propagated connections are managed by [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). You can't directly manage propagated connections by using Private Service Connect.

### Triggering connection propagation

Propagated connections are automatically established when the following actions occur:

  * When a hub administrator [enables connection propagation for a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update_a_hub), NCC creates propagated connections for existing endpoints in the VPC spokes that are connected to the hub.
  * When a hub administrator [adds a VPC spoke to a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke) that has connection propagation enabled, NCC creates propagated connections in the new spoke for existing endpoints in other VPC spokes that are connected to the same NCC hub. If the new spoke has existing endpoints, propagated connections are created for those endpoints in each connected spoke.
  * When a consumer service administrator [creates an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) in a VPC spoke that is attached to a NCC hub with connection propagation enabled, NCC creates propagated connections for that endpoint in other connected VPC spokes.
  * When a producer service administrator [increases a service attachment's propagated connection limit](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#update-propagated-connection-limit), NCC creates propagated connections that were previously blocked by this limit, as long as the new connections don't exceed the new limit.



Propagated connections for published services and regional Google APIs are established asynchronously and might not be immediately available. Propagated connections for global Google APIs ([Preview](https://cloud.google.com/products#product-launch-stages)) are established immediately after the conclusion of the operation that triggered connection propagation.

### Excluding subnets

When you [create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke), you can exclude the IP address ranges of subnets from being exported to the NCC hub. If you exclude a subnet from export, workloads in that subnet can't access propagated connections, and propagated connections aren't created for endpoints in that subnet. For example, in figure 1, workloads in `Consumer VPC 2` and `Consumer VPC 3` can't access the service in `Producer VPC 2`, and workloads in `Subnet 5` can't access the services in `Producer VPC 1`.

### Terminating propagated connections

The following actions indirectly control the deletion of propagated connections:

  * [Deleting the associated endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#delete-endpoint).
  * [Deleting a spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#deleting-a-spoke) that contains a Private Service Connect endpoint.
  * Disabling connection propagation on a NCC hub.



When any of the previous actions happen, propagated connections are terminated. This process is asynchronous and might not happen immediately.

## Specifications

  * The following Private Service Connect endpoint types can be made available through connection propagation: 
    * Endpoints that [access a published service](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints)
    * Endpoints that [access a regional Google API](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints)
    * Endpoints that [access global Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Connection propagation for global Google APIs and connection propagation for published services and regional Google APIs are configured independently. A hub administrator can enable or disable propagation for either type separately on the NCC hub.
  * Connections for endpoints that access published services or regional Google APIs are only propagated if the endpoint has the `Accepted` [connection status](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#connection-statuses).
  * By default, propagated connections are accessible by workloads in the same region and VPC network as the propagated connection.
  * You can configure [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) on an endpoint to make propagated connections for that endpoint available to workloads in any region of the propagated connection's VPC spoke.



## Quotas and limits

The following quotas and limits apply to Private Service Connect connection propagation:

  * **Consumer quotas** : 
    * The [PSC propagated connections per VPC network](https://docs.cloud.google.com/vpc/docs/quota#psc-propagated-connections-per-vpc) quota limits the number of propagated connections for published services and regional Google APIs that can be made available in a consumer VPC network.
    * The [PSC global GAPI routes per route table](https://docs.cloud.google.com/vpc/docs/quota#psc-global-gapi-routes-per-route-table) quota limits the maximum number of Private Service Connect endpoints for global Google APIs that can be propagated to VPC spokes that attach to the same Network Connectivity Center hub. Each endpoint that is propagated counts once towards this maximum, regardless of the number of VPC spokes that the endpoint is propagated to.
  * **Producer quota** : the [PSC ILB consumer forwarding rules per producer VPC network](https://docs.cloud.google.com/vpc/docs/quota#psc-ilb-frs-per-producer-vpc) quota limits the number of endpoints and propagated connections that can connect to a producer VPC network.
  * **Producer connection limit** : each published service (service attachment) has a propagated connection limit, which limits how many propagated connections can be established to the service from a single consumer. For more information about this producer configuration, see [Propagated connections](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagation).



If you can't access a propagated connection, one of these quotas or the connection limit might be affecting your access. For more information, see Troubleshooting.

## Limitations

Propagated connections have the following limitations:

  * If a VPC spoke has connection propagation for Google APIs enabled, deleting an endpoint for global Google APIs can disrupt NCC cross-spoke traffic to other global Google API endpoints in that spoke. For a workaround, see the [known issue](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#delete-issue).
  * Propagated connections don't support endpoints that use IPv6 addresses.
  * Propagated connections aren't created for [Hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid_spokes).
  * Propagated connections aren't created for [Producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview).



## Troubleshooting

If you are a service consumer who can't access a propagated endpoint, ask the NCC hub administrator to help troubleshoot. The hub administrator has the access required to [troubleshoot Private Service Connect connection propagation errors](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshoot-psc-propagation-errors).

## What's next

  * [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * [About accessing published services through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints).
  * [Access published services through endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
