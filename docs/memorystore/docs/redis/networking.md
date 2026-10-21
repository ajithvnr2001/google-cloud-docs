---
url: https://docs.cloud.google.com/memorystore/docs/redis/networking/
title: Networking \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:51.433510+00:00
---

# Networking  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Networking Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are looking for the Memorystore for Redis Cluster documentation, see [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking).**Important:** [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection) is a prerequisite that must be completed before creating a Redis instance with a Shared VPC network.

This page gives an overview of networking for Memorystore for Redis.

Memorystore uses VPC peering to connect your VPC network with the internal Google services network. Memorystore for Redis provides different peering architectures and networking features depending on what _connection mode_ you choose when creating an instance.

The option to select a connection mode has been introduced to support advanced networking options in Google Cloud like Shared VPC architectures and better IP management, while ensuring support for Memorystore's existing peering architecture.

Memorystore for Redis supports two connection modes, `DIRECT_PEERING` and `PRIVATE_SERVICE_ACCESS`.

Regardless of the connection mode, Memorystore for Redis always uses internal IP addresses to provision Redis instances.

## Connection modes

Memorystore for Redis provides two connection modes that support different functionalities:

  * Direct peering
  * Private services access



To view the networking connection mode for an existing instance, run the following command, replacing variables with appropriate values:
    
    
    gcloud redis instances describe instance-id --region=region
    

  * The `connectMode` value displays either `DIRECT_PEERING` or `PRIVATE_SERVICE_ACCESS`.



For instructions on how to choose the connect mode during instance creation, see [Creating a Redis instance with a Shared VPC network in a service project](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_with_a_shared_vpc_network_in_a_service_project) or [Creating a Redis instance with a centralized IP address range](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_that_uses_a_centralized_ip_address_range).

#### Direct peering

When using the direct peering mode, Memorystore creates a VPC peering between the customer VPC network and the VPC network in the Google managed project. The peering is created automatically during instance creation and requires no additional steps from the user. Other Google Cloud services do not share the peering. Memorystore for Redis used the direct peering connection mode before the availability of the private services access connection mode.

By default, new instances are created using the direct peering connection mode. Any existing scripts without the connection mode specified use the direct peering mode by default.

If you are creating an instance with the direct peering connection mode, and you want to use the `--reserved-ip-range` gcloud flag to specify an IP address range, see [Creating a Redis instance with a specific IP address range](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_with_a_specific_ip_address_range) for instructions on specifying a range. The minimum required block size is `/29` for instances without read replicas. The minimum required block size is `/28` for instances that have read replicas.

#### Private services access

[Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) is another way to create a peering between your VPC network and the Google services network.

**Important:** If you want to create a Redis instance using the private services access connection mode, you must first [Establish a private services access](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection) connection for your VPC network. Otherwise, you cannot create a Redis instance using the private services access connection mode for that network.

Establishing a private services access connection for a VPC network creates a peering between that VPC network and the Google services network. Once the connection is established, you can [create your instance using the private services access connection mode](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_that_uses_a_centralized_ip_address_range).

Using private services access enables you to use the following capabilities for your Redis instance:

  * Provision a Memorystore for Redis instance in a service project using Shared VPC.
  * Centrally manage IP address ranges across multiple Google services.
  * Connect from external sources to your VPC network over a [VPN tunnel](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) to your VPC network.



One of the added benefits of private service access is that the same network peering is shared across multiple Google services, thereby limiting the number of peerings created by Google services.

The `--reserved-ip-range` gcloud flag serves a different purpose when creating instances with the private services access connection mode than it does when creating instances with the direct peering connection mode. When creating instances with the private services access mode, if there are multiple IP address ranges allocated for private services access, you can use the `--reserved-ip-range` gcloud flag to choose which allocated ranges to use when creating your Redis instance. For instructions on how to do this, see [Creating a Redis instance with a specific IP address range](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_with_a_specific_ip_address_range).

## Choosing a connection mode

The table below outlines the different use cases and connection modes you should use.

Scenario | Supported connection mode  
---|---  
Provision a Redis instance with a Shared VPC network | Private services access only  
Access a Redis instance from on-premise networks using VPN | Private services access only  
Use centralized IP range management for multiple Google services | Private services access only |   
Provision a Redis instance using a dedicated VPC network | Private services access (recommended) or direct peering  
  
## Switching connection modes of existing instances

You cannot switch the connection mode of an existing instance. To switch the connection mode you have to recreate the instance using the new connection mode. This results in a change in the IP address of the instance.

For example, if you have an existing instance that was created before the private services access connection mode was available, the connection mode property for that instance is set to direct peering. If you recreate the instance using private service access connection mode, the IP address of the instance changes.

Also, Memorystore for Redis supports having Redis instances using private services access, and instances using direct peering, in the same project and in the same network.

## On-premises access with private services access

You can connect from a client in an on-premises network if the on-premises network is connected to the VPC network to which your Memorystore for Redis instance is connected. To permit connections from an on-premises network, do the following:

  1. Ensure your Shared VPC network is connected to your on-premises network using a one of the following options 
     * [ Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
     * a VLAN attachment for [ Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview) or [ Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview). 
  2. Ensure the BGP sessions on the Cloud Routers managing your Cloud VPN tunnels and Cloud Interconnect attachments (VLANs) have received specific prefixes (destinations) from your on-premises network. Default routes (destination `0.0.0.0/0`) cannot be imported into the Memorystore for Redis VPC network because that network has its own local default route. [Local routes for a destination are always used](https://docs.cloud.google.com/vpc/docs/routes#routeselection), even when the Memorystore for Redis peering is configured to import custom routes from your VPC network. 
  3. [ Identify the peering](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing-connections) produced by the private services connection. The peering used by Memorystore for Redis is named `servicenetworking-googleapis-com`.
  4. [ Update the peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peer-connection) connection to exchange custom routes by setting both `--import-custom-routes` and `--export-custom-routes` flag 
  5. [ Identify the allocated range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing_allocated_ip_address_ranges) used by the private services connection.
  6. [ Create a Cloud Router custom advertised route](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) for the allocated range on the Cloud Routers managing BGP sessions for your Cloud VPN tunnels or Cloud Interconnect attachments (VLANs). 

**Note:** The peering used for older installation of Memorystore for Redis uses the peering name of the format `redis-peer-[peer project number]`. For older installations, use this peering to exchange custom routes by setting both `--import-custom-routes` and `--export-custom-routes` flag.**Note:** Once you enable the peering `redis-peer-[peer project number]` to exchange custom routes, the custom routes will not be accepted by the peer Google Managed Project. Please contact Google Cloud Support to help you enable custom routes exchange for Google Managed Project.

## Communicating networking requirements

Usually the networking team and/or network admin for your organization is responsible for setting up a private services access connection. This allows the networking team to ensure that no IP addresses or ranges used for other Google Cloud resources overlap, which can cause connectivity issues.

We recommend that you contact the network\security team in your organization to set up the private service connection for you, especially if you encounter an error during the setup process. When reaching out to your networking team, send them the following information:
    
    
    The Memorystore for Redis instance cannot be created due to the following
    error:
    
    "Google private services access is not enabled. Enable privates service access
    and try again."
    
    Before an instance can be created, a private service access connection needs to
    be established for network <project name: network>. Please refer to the
    following Memorystore documentation links for more information on how to create
    this connection:
    
    * [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking).
    * [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection).
    * [Verifying a private services access connection](https://docs.cloud.google.com/memorystore/docs/redis/verifying-connection).
    

## Networking requirements for read replica enabled instances

To use the read replicas feature for Memorystore for Redis your instance must have a CIDR IP address range of `/28` or greater. Larger range sizes like `/27` and `/26` are valid. Smaller ranges like `/29` are not supported for this feature.

## Required permissions to establish a private services access connection

In order to manage a private services access connection, the user should have the following IAM roles. If you do not have the required permissions you can get insufficient-permissions errors. For a list of common networking errors, see [Networking error scenarios](https://docs.cloud.google.com/memorystore/docs/redis/troubleshooting#networking_error_scenarios).

#### UI permissions

##### Permissions required to list local and host project networks in the UI:

  * `compute.networks.list`
    * Needed in both the local and host projects.



##### Permission required to check the private services access connection in the UI:

  * `compute.networks.list`
    * Needed in both the local and host projects.



##### Permission required to create a private services access connection in the UI:

  * `serviceusage.services.enable`
    * Needed to enable the Service Networking API.
  * `compute.addresses.create`
  * `compute.addresses.list`
  * `servicenetworking.services.addPeering`



#### gcloud permissions

##### gcloud permissions required to check the private services access connection

  * `compute.networks.list`
    * Needed in both the local and host projects.



##### gcloud permissions required to create a private services access connection

  * `serviceusage.services.enable`
    * Needed to enable the Service Networking API.
  * `compute.addresses.create`
  * `compute.addresses.list`
  * `servicenetworking.services.addPeering`



## Supported networks and client IP ranges

Memorystore for Redis supports RFC 1918 private IP addresses and some non-RFC 1918 private IP addresses.

  * [Valid ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) provides a list of acceptable ranges for Memorystore for Redis. However, Memorystore for Redis does not support the privately used public IP (PUPI) addresses listed in the valid ranges table linked here.
  * [Restricted ranges](https://docs.cloud.google.com/vpc/docs/subnets#restricted-ranges) gives a list of IP address ranges that cannot be used to create Memorystore for Redis instances.
  * If a Memorystore instance uses the private services access connection mode, clients from PUPI ranges cannot connect to the Memorystore instance.



Memorystore also supports [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc) except [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy), on-premise access, and [Shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
