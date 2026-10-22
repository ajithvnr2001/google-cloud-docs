---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview/
title: Private Service Connect connection propagation through NCC \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:04.734931+00:00
---

# Private Service Connect connection propagation through NCC  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Private Service Connect connection propagation through NCC Stay organized with collections  Save and categorize content based on your preferences. 

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) lets _consumers_ access _managed services_ privately from inside their Virtual Private Cloud (VPC) network. Similarly, it lets managed service _producers_ host these services in their own separate VPC networks and projects and offer a private connection to their consumers. Private Service Connect connections aren't transitive between VPC spokes. The propagation of Private Service Connect services through the Network Connectivity Center (NCC) hub enables these services to be reachable by any other spoke VPC in the same hub through the route table.

NCC also supports the following capabilities:

  * Regional endpoint propagation. For more information about regional endpoints, see [About accessing regional endpoints through Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).
  * VPC Flow Logs for propagated Private Service Connect connections to internal passthrough Network Load Balancer. For detailed information about this capability, see the [VM-to-VM flows through Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-traffic-flows#psc-flows) section in the VPC Flow Logs documentation.



The NCC Private Service Connect connection propagation feature benefits the following use cases:

  * You can use a common services VPC network to create multiple Private Service Connect consumer endpoints. By adding a single common services VPC network to the NCC hub, all Private Service Connect consumer endpoints in the VPC network become transitively accessible to other VPC spokes through the NCC hub. This connectivity eliminates the need to individually manage each Private Service Connect endpoint in each VPC network.

  * You can access managed services in a VPC spoke network from on-premises networks that are reachable by hybrid spokes.




When you connect a VPC spoke to a hub that has propagated connections enabled, NCC creates propagated connections in that spoke for any endpoints that are attached to the same hub, unless the endpoint's subnet is excluded from being exported. After a VPC network is added to a NCC hub as a VPC spoke, new Private Service Connect endpoints are also propagated, unless the endpoint's subnet is excluded from export.

To set up a hub with a Private Service Connect propagated connection enabled, the hub administrator must [create a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub) with Private Service Connect propagation or update the propagation setting by using the `--export-psc` flag. Then the hub administrator must add the VPC networks as spokes to the hub. The spoke owner can use the `--exclude-export-ranges` and `--include-export-ranges` flags to exclude specific Private Service Connect allocated subnets from the NCC routing so that specified subnets can't be reached from other VPC networks, thus keeping them private to the local VPC network.

**Note:** Connections are propagated asynchronously and could take up to 24 hours to propagate.

For information about Private Service Connect propagated connections, see [About propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections).

For information about the `--exclude-export-ranges` and `--include-export-ranges` flags, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).

For detailed information about setting up a hub for a Private Service Connect propagated connection, see [Configure a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub).

## Connection propagation limit

For details about propagated connection limits, see [Propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit).

## Considerations

Consider the following before you enable a Private Service Connect propagated connection:

  * A Private Service Connect propagated connection works only with VPC spokes.

  * Private Service Connect IPv6 propagated connections across VPC spokes aren't supported.

  * If you need to make propagated Private Service Connect connections available to on-premises networks connected to hybrid spokes:

    * Your NCC hub must have only one [routing VPC network](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#routing-vpc) that contains all of its hybrid spokes.

    * The hub's single routing VPC network must also be a VPC spoke.

If a hub has two or more routing VPC networks, none of the routing VPC networks can also be VPC spokes. Consequently, hubs with two or more routing VPC networks can't make propagated Private Service Connect connections available to on-premises networks.

  * For Private Service Connect propagation to work with hybrid spokes, the routing VPC network must also be added as a VPC spoke.

  * Private Service Connect endpoints using privately used public IP address ranges aren't propagated to the NCC hub.

  * If a subnet in a VPC spoke is configured with Private NAT to access the NCC hub, the traffic from the subnet to the propagated Private Service Connect service is dropped. If the Private NAT gateway is configured with `--nat-all-subnet-ip-ranges`, then Private Service Connect propagation through NCC doesn't work for all subnets in this spoke VPC. To get it to work from non-overlapping subnets of this VPC spoke, use `--nat-custom-subnet-ip-ranges` for the Private NAT gateway. Don't use NAT to route traffic from non-overlapping subnets to the NCC hub.

  * The propagation status might be inaccurate if you create, delete, and re-create the Private Service Connect endpoint within a short timeframe. However, after some time, the propagation status becomes accurate and reflects the actual state of the propagated connection. This could take up to 15 minutes.

  * Private Service Connect connection propagation is asynchronous after spoke creation or deletion. When a VPC spoke is removed from a hub, it can take some time to update propagated Private Service Connect connections. While the Private Service Connect propagation connection update is in progress, traffic from the VM within the VPC network can flow to the backend, even after the VPC spoke is added to a new hub. To avoid traffic flow to the backend, before adding the spoke to another hub, make sure that all of the propagation status entries for the VPC network in the previous hub, whether as a source spoke or a target spoke, are deleted.




## Private Service Connect connection propagation status

NCC lets you view the status of the Private Service Connect connection propagation within a NCC hub. You can view a summary of statuses or drill down on specific errors to view error details.

The following table lists the propagation status codes and what they mean.

Code | Message  
---|---  
**Ready** | The propagated Private Service Connect connection is ready.   
**Propagating** | The Private Service Connect connection propagation is pending. This is a transient state.   
**Error, producer propagated connection limit exceeded** | The propagated Private Service Connect connection propagation failed because the VPC network or the project of the target spoke has exceeded the propagation connection limit set by the producer. To address this issue, see your producer's documentation or contact their support team.   
**Error, producer NAT IP space exhausted** | The Private Service Connect connection propagation failed because the NAT IP subnet space is exhausted. It is equivalent to the `Needs attention` status of the PSC connection. For details, see [Connection statuses](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#connection-statuses) in the Private Service Connect documentation.   
**Error, producer quota exceeded** | The Private Service Connect connection propagation failed because the `PSC_ILB_CONSUMER_FORWARDING_RULES_PER_PRODUCER_NETWORK` quota in the producer VPC network is exceeded.   
**Error, consumer quota exceeded** | The Private Service Connect connection propagation failed because the `PSC_PROPAGATED_CONNECTIONS_PER_VPC_NETWORK` quota in the consumer VPC network is exceeded.   
  
For information about how to view Private Service Connect connection propagation statuses, see [View the Private Service Connect connection propagation status](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#view-psc-propagation-status). For Private Service Connect connection propagation troubleshooting information, see [Troubleshoot Private Service Connect connection propagation errors](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshoot-psc-propagation-errors).

## Access global Google APIs through Private Service Connect endpoints

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

VPC spokes can export [global Google APIs through Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) for propagation to other spokes in the hub. You can enable this feature on Google APIs through Private Service Connect endpoints by using the `--export-psc-global-google-apis` flag on the hub to allow Google API access across spokes. You can also exclude Private Service Connect Google API endpoints from propagation by adding their `/32` IP address to the exclude filter.

The tasks to configure the propagation of global Google APIs through Private Service Connect endpoints to other spokes include the following:

  1. Create an NCC hub by using the `gcloud network-connectivity hubs create` command.
  2. Create a VPC network and attach it to the NCC hub by using the `gcloud network-connectivity spokes linked-vpc-network create` command.
  3. Create a Private Service Connect global IP address on the VPC network by using the `gcloud compute addresses create` command.
  4. Create a global Google API endpoint by using the `gcloud compute forwarding-rules create` command.
  5. Update the hub to enable the propagation of Private Service Connect global Google API endpoints to other spokes with the `gcloud beta network-connectivity hubs update` command

When you enable the propagation option, any Private Service Connect global Google API endpoint in any VPC spoke that is not in an excluded range is propagated to every VPC spoke of the NCC hub. Other VPC spokes that are directly connected to the hub can access Google API services by sending traffic to the IP address of a Private Service Connect global Google API endpoint being propagated.


**Caution:** If a VPC spoke has connection propagation for global Google APIs enabled, deleting an endpoint for global Google APIs can disrupt traffic to other global Google API endpoints in that spoke. For a workaround, see the [Known issues](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#delete-issue) section on the [Configure Private Service Connect APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) page.

For detailed information about Private Service Connect propagated connections, see [About propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections).

## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and Google Cloud CLI commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
