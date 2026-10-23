---
url: https://docs.cloud.google.com/memorystore/docs/memcached/networking/
title: Networking \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:12.263969+00:00
---

# Networking  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/networking/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Networking Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of networking for Memorystore for Memcached. For a list of common networking errors, see [Networking error scenarios](https://docs.cloud.google.com/memorystore/docs/memcached/troubleshoot-issues#networking_error_scenarios).

## Private services access

Memorystore for Memcached uses [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) to create a network peering between your project and an internal network for some Google Cloud services like Cloud SQL, Memorystore for Redis, and Memorystore for Memcached.

**This means that you must first[establish a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection) for a network before you can create a Memcached instance using that network.**

Using a private services access connection offers you the benefit of centralized, customizable IP address ranges for the aforementioned services. For instructions on selecting a specific IP range allocation, see [Creating a Memcached instance that uses a specific IP address range](https://docs.cloud.google.com/memorystore/docs/memcached/create-manage-instances#creating_a_memcached_instance_that_uses_a_specific_ip_address_range).

**Important:** Once a private services connection is established for any of these services on a network, it is established for all other services on that network that use the private services access networking architecture.

## On-premises access with private services access

You can connect from a client in an on-premises network if the on-premises network is connected to the VPC network to which your Memorystore for Memcached instance is connected. To permit connections from an on-premises network, do the following:

  1. Ensure your Shared VPC network is connected to your on-premises network using a one of the following options 
     * [ Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
     * an interconnect attachment (VLAN) for [ Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview) or [ Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview). 
  2. [ Identify the peering](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing-connections) produced by the private services connection. The peering used by Memorystore for Memcached is named `servicenetworking-googleapis-com`.
  3. [ Update the peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peer-connection) connection to exchange custom routes by setting both `--import-custom-routes` and `--export-custom-routes` flag 
  4. [ Identify the allocated range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing_allocated_ip_address_ranges) used by the private services connection.
  5. [ Create a Cloud Router custom advertised route](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) for the allocated range on the Cloud Routers managing BGP sessions for your Cloud VPN tunnels or Cloud Interconnect attachments (VLANs). 



## Communicating networking requirements

Usually the networking team and/or network admin for your organization is responsible for setting up a private services access connection. This allows the networking team to ensure that no IP addresses or ranges used for other Google Cloud resources overlap, which can cause connectivity issues.

We recommend that you contact the network\security team in your organization to set up the private service connection for you, especially if you encounter an error during the setup process. When reaching out to your networking team, send them the following information:
    
    
    The Memorystore for Memcached instance cannot be created due to the following
    error:
    
    "Google private services access is not enabled. Enable privates service access
    and try again."
    
    Before an instance can be created, a private service access connection needs to
    be established for network <project name: network>. Please refer to the
    following Memorystore documentation links for more information on how to create
    this connection:
    
    * [Networking](https://docs.cloud.google.com/memorystore/docs/memcached/networking).
    * [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).
    * [Verifying a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/verifying-connection).
    

## IP addresses

Each Memorystore for Memcached instance has a [discovery endpoint](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview), and each node in the instance has its own IP address. You can view these IP addresses in the Google Cloud console, or by using [`gcloud memcache instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/describe).

IP addresses for nodes and for the discovery endpoint do not change.

## Supported networks and client IP ranges

###### The following network or instances with RFC 1918 IP addresses are supported:

  * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc) except [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy)
  * [Shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * on-premise systems
  * Compute Engine VM instances except for 172.17.0.0/16 because this IP range is reserved for internal components
  * We recommend using a private services access range with a block size of at least `/24` to support Memorystore for Memcached and other services. However, the minimum block size needed to support Memorystore for Memcached is `/26`.



## What's next

  * [Establish a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).
  * [Create a Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/creating-managing-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
