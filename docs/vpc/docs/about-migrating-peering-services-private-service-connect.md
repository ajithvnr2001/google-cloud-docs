---
url: https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect/
title: About migrating peering-based services to Private Service Connect \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:59.914773+00:00
---

# About migrating peering-based services to Private Service Connect  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About migrating peering-based services to Private Service Connect

Many managed service producers use [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to offer connectivity to service consumers that are in another Virtual Private Cloud (VPC) network. An alternative solution is to use Private Service Connect.

This document provides an overview of how service producers can [migrate their peering-based services to Private Service Connect](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect) and preserve the IPv4 addresses that are used to access the services. This migration process requires that all resources that are connected to a given subnet must be migrated at the same time.

Each service producer determines whether and when they are going to migrate to Private Service Connect. To learn whether a service producer is migrating from VPC Network Peering to Private Service Connect, check the service documentation or contact the service producer.

## Migrating peering-based services

In this example peering-based service, the client `vm1` sends traffic to the service's load balancer `10.10.10.10` in the producer VPC network. The consumer network has a [peering subnet route](https://docs.cloud.google.com/vpc/docs/routes#types-of-subnet-routes) for the producer subnet because the networks are connected through VPC Network Peering.

[ ![](https://docs.cloud.google.com/static/vpc/images/peering-based-service.svg)](https://docs.cloud.google.com/static/vpc/images/peering-based-service.svg)

**Figure 1.** In a peering-based service, the consumer VPC network and the producer VPC network can access each other through VPC Network Peering (click to enlarge). 

During the migration, the following tasks are completed:

  * The producer deploys the service in a new subnet `producer-subnet-2` in a new VPC network, and publishes the service through Private Service Connect.
  * The producer creates an internal range to reserve the CIDR range of the producer subnet, `10.10.10.0/24`.
  * The producer deletes the original subnet `producer-subnet-1` and all resources in it.
  * A migration subnet `consumer-subnet-2` is created in the consumer VPC network, configured with the same CIDR range as the producer subnet.
  * A Private Service Connect endpoint is created in the migration subnet, configured with the same IP address that was previously used by the producer load balancer forwarding rule.



After the migration is completed, the client `vm1` can still reach the service at `10.10.10.10`, but this IP address is now associated with the Private Service Connect endpoint in the consumer VPC network.

[ ![](https://docs.cloud.google.com/static/vpc/images/migrated-service.svg)](https://docs.cloud.google.com/static/vpc/images/migrated-service.svg)

**Figure 2.** After the migration, clients in the consumer VPC network send requests to the Private Service Connect endpoint, which forwards traffic to the producer VPC network (click to enlarge). 

## Migration tasks

The migration includes tasks that are performed in both the producer and consumer VPC networks. The producer can coordinate with the consumer to perform the migration, or in the case of Google-managed services, the service producer can automate the consumer tasks through a [service agent](https://docs.cloud.google.com/iam/docs/service-agents).

Task | Producer | Consumer  
---|---|---  
**Deploy a Private Service Connect service**  
[ Deploy the service in a new subnet in a new VPC network in the producer project and publish it by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#publish-service) | Performed by producer |   
**Shut down the peering-based service**  
[ Reserve the producer subnet CIDR range by creating an internal range in the producer project](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#create-internal-range) | Performed by producer | Consumer provides the subnet name to use for the migration target  
[ Delete all resources in the producer subnet, and then delete the subnet](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#delete-producer-subnet) | Performed by producer | The consumer can no longer access the service  
**Create a Private Service Connect endpoint in the consumer network**  
[ Create a migration subnet in the consumer network](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#create-consumer-subnet) | If consumer didn't choose the subnet name, the producer provides the subnet name to consumer | Performed by consumer (or by producer through a service agent)  
[Create a Private Service Connect endpoint in the consumer network](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#create-endpoint) | Producer provides service attachment URI to consumer | Performed by consumer (or by producer through a service agent) The consumer can access the service  
[Validate access through the Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#validate-endpoint) |  | Performed by consumer  
**Finalize the migration**  
[Delete the internal range](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#delete-internal-range) | Performed by producer |   
[ Update the consumer's migration subnet to convert it to a regular subnet](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#update-subnet) |  | Performed by consumer (or by producer through a service agent)  
[ If it's not needed for other services, delete the peering connection in the producer and consumer networks](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect#delete-peering) | Performed by producer | Performed by consumer (or by producer through a service agent)  
  
## Considerations

If you are a service producer who wants to migrate your peering-based service to Private Service Connect, consider the following:

  * The Private Service Connect implementation of the service must offer the same features as the peering-based service.
  * The migration process supports preserving IPv4 addresses that access services. Preserving IPv6 addresses isn't supported. However, migrated services can be accessed by IPv6 Private Service Connect endpoints.
  * You must be able to delete all resources in the subnet that contains the service instance during the migration. If multiple service instances use the same subnet, all instances must migrate at the same time.
  * The consumer's Private Service Connect endpoint and the producer's service attachment and forwarding rule must all be in the same region.

To let the endpoint be accessed from any region, you can enable [global access on the endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access).

  * If the service saves state, you must have a method of migrating the state to the new service instances.

  * You can't delete the peering connection until all service instances in the producer VPC network have migrated.

  * The service has a downtime during the migration.

  * Migrating to Private Service Connect has a pricing impact for both producers and consumers. Make sure that your consumers are aware of this change before you migrate them.

  * Private Service Connect translates the source IP address of the client to an IP address in a [NAT subnet](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#psc-subnets). If the service needs IP address information about the client, you must use [PROXY protocol](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol) to get the client IP address, and handle the packets appropriately between the backend VMs and your application.




## Internal ranges for migration

The [internal range](https://docs.cloud.google.com/vpc/docs/internal-ranges) is used to reserve the CIDR range that is used in the producer subnet so that when the producer subnet is deleted, the CIDR range can't be used for another purpose.

When you create an internal range for peer migration, you set the usage to `FOR_MIGRATION` and specify the source and target subnets. The source subnet is the producer subnet, and the target subnet is the new peer migration subnet that will later be created in the consumer network.

Creating the internal range prevents a subnet from being created that matches both the target subnet name, and the CIDR range. However, another subnet can be created in the consumer network that has the same name if it uses a different CIDR range. If that happens, the migration can't proceed until either the consumer subnet with the matching name is deleted, or the internal range is deleted.

## Peer migration subnets

The subnet that is created in the consumer network for migration has the purpose set to `PEER_MIGRATION`. Peer migration subnets can contain only IP addresses and Private Service Connect endpoints.

After the migration is complete and verified, the subnet is updated to become a regular subnet by setting the purpose to `PRIVATE`, and other resources can be created in the subnet. A regular subnet can't be converted back to a peer migration subnet.

Only principals that have the `compute.subnetworks.usePeerMigration` permission can do the following:

  * Create and delete IP address resources in peer migration subnets.
  * Create and delete Private Service Connect endpoints (forwarding rules) in peer migration subnets.



The `compute.subnetworks.usePeerMigration` permission is included in the following roles:

  * [Compute Peer Subnet Migration Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.peerSubnetMigrationAdmin) (`roles/compute.peerSubnetMigrationAdmin`)
  * [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)



Principals with the Compute Peer Subnet Migration Admin role can create and delete IP addresses and Private Service Connect endpoints in a peer migration subnet, but they can't create, update, or delete the migration subnet.

Principals that have the Compute Network Admin role can perform all the tasks necessary for migration, including the preceding tasks and also the following:

  * Create a subnet with the purpose set to `PEER_MIGRATION`.
  * Update the subnet—for example, to expand the CIDR range or enable Private Google Access.
  * Update the subnet purpose to `PRIVATE`.
  * Delete the subnet.



## Pricing

For pricing information, see the following:

  * Service producers: [pricing for publishing a service](https://docs.cloud.google.com/vpc/network-pricing#psc-service-attachment).

  * Service consumers: [pricing for accessing a published service through an endpoint](https://cloud.google.com/vpc/pricing#psc-forwarding-rule-service).




## What's next

  * [Migrate a service subnet from peering to Private Service Connect](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect)
  * [Publish a service through Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
