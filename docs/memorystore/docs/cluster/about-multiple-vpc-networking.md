---
url: https://docs.cloud.google.com/memorystore/docs/cluster/about-multiple-vpc-networking/
title: About multiple VPC networking \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:10.078826+00:00
---

# About multiple VPC networking  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/about-multiple-vpc-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  About multiple VPC networking Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of multiple VPC networking for Memorystore for Redis Cluster. In situations where you only need one VPC network, we recommend (but don't require) using a service connection policy to provision your network, as explained in [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

Setting up networking for multiple VPC networks requires Memorystore users to configure and register up Private Service Connect connections.

**Important** : To use multiple VPC networking with Memorystore for Redis Cluster, your cluster must run a maintenance version of at least `REDISCLUSTER_20251210_02_00`. If your cluster runs an older maintenance version, then you must perform a self-service update before you can add or use multiple connections. For more information about updating your cluster to a newer maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/self-service-maintenance).

For a tutorial on setting up multiple VPCs using only user-registered connections, see [Provision a new instance to use multiple VPC networks](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-user-registered-psc-connection).

For a tutorial on setting up multiple VPCs for instances provisioned with automatically registered connections, see [Configure an existing instance to use multiple VPC networks](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-automatically-registered-psc-connection).

## Private Service Connect connections

This section explains essential information about Private Service Connect connections for Memorystore.

### Private Service Connect connection basics

For Memorystore, a Private Service Connect connection consists of two fundamental items:

  * An IP address
  * An established connection between a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) and a Memorystore instance's service attachment



### Private Service Connect connection types

When using Memorystore for Redis Cluster, Private Service Connect connections fall into two categories: automatically registered and user-registered. A Memorystore for Redis Cluster instance is compatible with both types.

  * **User-registered Private Service Connect connections** : self-created and self-registered connections. For Memorystore, user-registered connections are needed for multiple VPC networking setups.

Self-managing these connections has the benefit of giving you control over the subnets, IP addresses, and forwarding rules used to create them. For these connections, you're responsible for their lifecycle (including creating, registering, and deleting them).

  * **Automatically registered Private Service Connect connections** : connections created and registered by [Private Service Connect service connectivity automation](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) for your Memorystore instance. When you create or delete a Memorystore instance, your service connection policy manages the lifecycle of the associated connection by creating, registering, or deleting the connection automatically.

If you already have a Memorystore instance that you've been using, and you want to connect additional VPC networks, you probably have automatically registered connections. If you want to keep these connections because your existing application uses them, you can keep them and only add user-registered connections for new VPCs.




### Application connection requirements

To connect your application using a multiple VPC networking setup, Memorystore has networking requirements that you must meet.

Each VPC network that you connect to your cluster in Memorystore for Redis Cluster must have two Private Service Connect connections. These connections can be either user-registered or registered automatically. One connection is the discovery connection that your client uses to establish a connection to the cluster. The other connection is reserved for internal usage by the Memorystore for Redis Cluster backend.

**Important:** Don't configure your Redis client to connect to this reserved, internal endpoint. Unlike the discovery endpoint, the internal endpoint doesn't accept connections on port `6379`. Attempting to use this endpoint for either initial cluster discovery or standard client connections results in a connection timeout.

For more information about connecting your client to a cluster that uses user-registered connections, see [Set up a client connection](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-user-registered-psc-connection#step_5_set_up_a_client_connection).

For more information about connecting your client to a cluster that uses automatically registered connections, see [Set up a client connection](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-automatically-registered-psc-connection#step_3_set_up_a_client_connection).

For more information about setting up connections to services through Private Service Connect endpoints, see [About accessing published services through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints).

## Limitations

  * You can have between 1 and 20 VPC networks connected to a single Memorystore instance, and no more than 40 Private Service Connect connections in total
  * To delete a Memorystore instance connected with user-registered Private Service Connect connections, you must [delete](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-user-registered-psc-connection#delete_your_psc_connections) and [deregister](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-user-registered-psc-connection#deregister_your_private_service_connect_endpoints) the connections first.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
