---
url: https://docs.cloud.google.com/vpc/docs/private-services-access/
title: Private services access \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:52.111763+00:00
---

# Private services access  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-services-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private services access

Private services access lets you reach VPC-hosted services—services running on Compute Engine instances within a VPC network—without exposing traffic to the public internet.

To route traffic internally, private services access [creates a private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) between your VPC network and the VPC network of the service producer, who can be Google or a third party. This private connection is established using a VPC Network Peering connection.

Because traffic travels internally within Google's network, instances in your VPC network can reach the service by using their internal IPv4 addresses. While your instances can have external IP addresses, they aren't required for or used by private services access.

## Supported services

The following Google VPC-hosted services support private services access:

  * [AI Platform Training](https://docs.cloud.google.com/ai-platform/training/docs/vpc-peering)
  * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/configure-connectivity)
  * [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking)
  * [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#overview_of_the_service_architecture)
  * [Cloud Build](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview)
  * [Cloud Intrusion Detection System](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids)
  * [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/private-ip) (doesn't support [DNS peering](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#dns-peering))
  * [Cloud TPU](https://docs.cloud.google.com/tpu/docs/shared-vpc-networks)
  * [Converge Enterprise Cloud with IBM Power for Google Cloud](https://console.cloud.google.com/marketplace/product/ibm-sg/ibm-power-cloud-for-gcp)
  * [Filestore](https://docs.cloud.google.com/filestore/docs/networking)
  * [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/vpc)
  * [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking)
  * [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access)
  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip)
  * [Memorystore for Memcached](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection)
  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection)
  * [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/vpc-peering)

**Note:** When you use private services access as a service consumer, you are solely responsible for securing your VPC networks and all resources and data available on them. Google is not responsible for how your data and resources may be accessed or used by the third party that you are connecting with.

## Private services access and VPC Network Peering

In a private connection, the service producer network and your network are connected through VPC Network Peering. For routing between the two networks to work correctly, the two networks must use distinct IP address ranges. To avoid overlaps, you create one or more allocated ranges in your network to use with the private connection.

When you allocate a range in your VPC network, that range can't be used for other resources, such as subnets or destinations of custom static routes.

For information about choosing an allocated range, see [Choose an IP address range for the allocated range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#choose-range).

## Private services access workflow

When you use private services access, resources are deployed in both your VPC network and the service producer's network. The following steps outline the process:

  1. **As a service consumer, you deploy a service instance with private services access**. The details might vary depending on which service you are deploying. The following steps might be performed by you, or might be automated by the service producer as part of service instance deployment:

     1. You allocate an IP address range in your VPC network. This allocated range is reserved exclusively for the service producer.

     2. You create a private connection to the service producer, specifying the allocated range that you created.

     3. You provision a service instance—for example, a Cloud SQL instance—referencing the private connection that you've created.

  2. **The service producer provisions resources for your service instance**.

     1. The service producer creates a project for your service instance. The project is isolated, meaning no other customers share it and the service consumer is billed for only the resources that the service consumer provisions.

     2. Within that project, the service producer creates a VPC network that is dedicated to you.

     3. Within that network, the service producer creates a subnet. The IP address range for this subnet is selected from the allocated range that you provided. The service producer typically chooses a `/29` to `/24` CIDR block. You can't select or modify the service producer's subnet IP address range.

     4. The service instance is assigned an IP address from the new subnet.

  3. **The private connection becomes active**.

     1. The VPC Network Peering connection is established.

     2. Your VPC network imports routes from the service producer's network.

     3. VMs in your network can communicate with the service instance by using its internal IP address. Traffic travels entirely within Google's network and not through the public internet.




You can take the following actions after the initial deployment is created:

  * **Provisioning more resources** : when you provision additional resources for the same service, the service producer places them in existing subnets if there is space. If a subnet is full, a new subnet is created in that region from the allocated range.

  * **Deleting resources** : a subnet in the service producer's network is deleted only when you delete all the service resources within it. For information about deleting resources, see the relevant service producer's documentation.




## Example

The following diagram shows using a private connection to access service instances.

[ ![Resources in a service consumer network can access a Cloud SQL instance
    through private services access.](https://docs.cloud.google.com/static/vpc/images/private-services-access-sql.svg)](https://docs.cloud.google.com/static/vpc/images/private-services-access-sql.svg) Private services access (click to enlarge).

In this example, the service consumer VPC network allocated the `10.240.0.0/16` address range for Google services and established a private connection that uses the allocated range.

  * The private connection is assigned the `10.240.0.0/16` allocated range.

  * Google creates a project and a VPC network for the service consumer's resources. The VPC networks are connected by using VPC Network Peering.

  * The service producer creates a subnet that uses the IP address range `10.240.0.0/24`.

  * The Cloud SQL instance is assigned the IP address `10.240.0.2`.

  * After the subnet is created, the service consumer network imports routes from the service network.

  * In the service consumer VPC network, requests with a destination of `10.240.0.2` are routed to the private connection over to the service producer's network.

  * The service consumer deploys a service instance for a different Google service in `europe-west1`. Because Google is the service producer, the same project and network can be used. However, because the instance is in a different region, a new subnet is required. Google creates a new subnet that uses the IP address range `10.240.10.0/24` and assigns the service instance the IP address `10.240.10.2`.




## Reachability of service instances

Only one service consumer VPC network can create a private connection to a given managed service instance. However, there are ways to make the private connection available to resources that are outside of that VPC network:

  * To make the service instances available from other VPC networks, consider the following options: 
    * Accessing through NCC.
    * Accessing through Shared VPC.
  * To make the service instances available from connected networks, such as on-premises networks, see Accessing through hybrid connectivity.



If none of these options work for your use case, the service producer might offer other ways to connect to the service that are a better fit—for example, through [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#services). For more information, see the documentation for the service.

### Accessing through NCC

For some services that are available through private services access, you can use NCC to make the service reachable by other spokes on a hub by creating a _producer VPC spoke_. For more information, including which services are supported, see [Producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview).

### Accessing through Shared VPC

If you are using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), create the allocated IP range and private connection in the host project. Typically, a network administrator in the host project must do these tasks. After the host project is set up, VM instances in service projects can use the private connection.

### Accessing through hybrid connectivity

In hybrid networking scenarios, an on-premises network is connected to a VPC network either through a [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) connection. By default, on-premises hosts can't reach the service producer's network by using private services access.

In the VPC network, you might have custom static or dynamic routes to correctly direct traffic to your on-premises network. However, the service producer's network doesn't contain those same routes. When you create a private connection, the VPC network and service producer network exchange subnet routes only.

The service producer's network contains a default route (`0.0.0.0/0`) that goes to the internet. If you export a default route to the service producer's network, it is ignored because the service producer network's default route takes precedence. Instead, define and export a custom route with a [more specific destination](https://docs.cloud.google.com/vpc/docs/routes#routeselection).

For more information, see [Configure hybrid connectivity](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#on-prem).

## Service producer network

On the service producer's side of the private connection is a VPC network, where your service resources are provisioned. The service producer's network is created exclusively for you and contains only your resources.

A resource in the service producer network is similar to other resources in your VPC network. For example, it's reachable through internal IP addresses by other resources in your VPC network. You can also create firewall rules in your VPC network to control access to the service producer's network.

For more information about the service producer side, see [Enable private services access](https://docs.cloud.google.com/service-infrastructure/docs/enabling-private-services-access) in the Service Infrastructure documentation. This documentation is for your information only and is not required for you to enable or use private services access.

## Restrict private connections with organization policies

You can use organization policy custom constraints to define restrictions for private connections. For example, configuring custom constraints with the resource type `servicenetworking.googleapis.com/Connection` lets you do the following:

  * Specify which VPC networks can connect with private connections
  * Specify restrictions for the names of allocated ranges that you can use to create private connections



For more information, see [Manage resources by using custom constraints](https://docs.cloud.google.com/vpc/docs/custom-constraints).

## Pricing

For private services access pricing, see [Private services access](https://cloud.google.com/vpc/pricing#psa-pricing) on the VPC pricing page.

## Limitations

The following limitations apply to private services access:

  * Because a private connection is implemented as a VPC Network Peering connection, the behaviors and constraints of peering connections also apply to private connections. For example, because VPC Network Peering isn't transitive, a private connection isn't available to peered VPC networks.

For more information, see [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [VPC Network Peering limitations](https://docs.cloud.google.com/vpc/docs/vpc-peering#limitations), and [Quotas and limits](https://docs.cloud.google.com/vpc/docs/quota).

  * Only one service consumer VPC network can create a private connection that connects to a given managed service instance. However, there are ways to make the private connection available to resources that are outside of that VPC network. For more information, see Reachability of service instances.

  * You can't change the IP address range that's associated with an allocated range. However, you can [modify which allocated ranges are associated with a private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modifying-connection).

  * Using IPv6 address ranges with private services access isn't supported.




## What's next

  * To allocate IP address ranges, create private connections, or share private DNS zones, see [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
