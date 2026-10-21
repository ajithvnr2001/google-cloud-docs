---
url: https://docs.cloud.google.com/memorystore/docs/cluster/networking/
title: Networking \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:10.027289+00:00
---

# Networking  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Networking Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use networking with [Private Service Connect service connectivity automation](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) for Memorystore for Redis Cluster. The page also describes the following information about networking:

  * [Networking setup guidance](https://docs.cloud.google.com/memorystore/docs/cluster/networking#networking_setup_guidance)
  * [Supported networking architectures](https://docs.cloud.google.com/memorystore/docs/cluster/networking#supported_networking_architectures)
  * [Frequently asked questions](https://docs.cloud.google.com/memorystore/docs/cluster/networking#frequently_asked_questions)

**Note:** Memorystore for Redis Cluster also supports networking for multiple VPCs. For more information about multiple VPC networks, see [About multiple VPC networking](https://docs.cloud.google.com/memorystore/docs/cluster/about-multiple-vpc-networking).

## Networking setup guidance

**Tip:** For a Terraform solution that you can use for a simplified Memorystore for Redis Cluster networking setup, see [ Simplified Google Cloud Networking with Terraform](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions?tab=readme-ov-file#cloudnet-config-solutions-simplified-google-cloud-networking-with-terraform-). 

As a reader of this page, you likely fit into one of two roles. Each role has different tasks that you have to accomplish. However, there might be an overlap between the roles.

Knowing which role you fit into and your role's goals helps you accomplish your cluster creation and networking tasks quickly and efficiently.

You might fit into the following roles:

  * Role 1: _Redis Admin_

    * Your goal is to [create a cluster in Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/create-manage-instances#create_an_instance). You're reading this page to learn if you have the required prerequisites to create a cluster that uses a service connection policy for networking. When you use this networking setup, service connection policies authorize the automatic lifecycle management of Private Service Connect connections.

    * After you know that a service connection policy is established for your network, get the full network name (that has the format of `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`) from your Network Admin so that you can use it to create the cluster.

    * After the service connection policy is associated with your network, service connectivity automation deploys connectivity for the cluster automatically as the cluster is created.

  * Role 2: _Network Admin_

    * Your goal is to find out if a service connection policy is created for the network and if it's located in the region where the Redis Admin wants to deploy a cluster in Memorystore for Redis Cluster.

If the service connection policy isn't created, then [create it](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#create-policy). This policy lets Memorystore automate private connectivity to the Memorystore service.

To create a service connection policy, you must have the [required roles](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#roles). For more information about configuring and managing a service connection policy, see [Configure service connection policies](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies).

**Note** : When you create the service connection policy, use the `gcp-memorystore-redis` service class. For each combination of a network, region, and service class, you can create only _one_ policy.

When creating the service connection policy, you can use the connection limit to ensure enough address space for your clusters. Here's how to estimate this limit.

To determine the connection limit, multiply the number of clusters that you want to create in the region where you're defining the service connection policy by two. So, if you want to create five clusters in the region, then specify 10 for the connection limit.

If you don't know how many clusters you plan to create, then don't specify a connection limit. Also, if the limit is reached, then you can increase it by [ updating the service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy).

    * Your next goal is to provide the network name to the Redis Admin so that they can use it to create the cluster.




### Prerequisites required for using service connection policy networking

As described in [About service connection policies](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies), a service connection policy is unique to your project, network, region, and service class. If you want to use a service connection policy to enable Private Service Connect connections that are deployed automatically, then before you create a cluster, make sure that the following conditions are met:

  * The service connection policy must exist for your project, network, region, and `gcp-memorystore-redis` service class.
  * You must enable the necessary APIs.

**Note:** For more information about how to create service connection policies, see [Configure service connection policies](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies). For more information about how to use these policies to configure Private Service Connect connections as well as the lifecycle of the connections, see [Deploy a managed service instance and configure connectivity](https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies#deploy-service).

#### Communicate networking requirements

If you're a Redis Admin, then ask your Network Admin if a service connection policy exists for the region, network, and `gcp-memorystore-redis` service class where you want to [create your cluster](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#create_an_instance). After your Network Admin creates the policy, ask them for the full network name (that has the format of `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`) so that you can use it to create the cluster.

Send your Network Admin a link to this page so that they can understand the service connection policy prerequisites that they need for you to create the cluster.

**Important:** Make sure that your Network Admin doesn't configure the [service instance scope](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope) in the service connection policy. Instead, the Network Admin must leave the default settings for the policy.

Memorystore for Redis Cluster doesn't support custom service instance scopes. It supports deploying only Private Service Connect endpoints automatically through the authorization of a service connection policy that's in the same Google Cloud project as the cluster.

For more information about deploying Private Service Connect endpoints in Google Cloud projects other than the project that hosts the cluster, see [ Set up multiple VPC networks using user-registered Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-user-registered-psc-connection) and [Set up multiple VPC networks for instances provisioned with automatically registered Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-automatically-registered-psc-connection).

#### Enable APIs

As a Redis Admin, before you can create a cluster in Memorystore for Redis Cluster, you must enable all of the APIs listed in [Before you begin](https://docs.cloud.google.com/memorystore/docs/cluster/create-manage-instances#before_you_begin).

### Shared VPC

In addition to standard [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/overview), Memorystore for Redis Cluster supports [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) networks.

Shared VPC setups have a host project and one or more service projects. The Network Admin defines the service connection policy for Memorystore for Redis Cluster in the host project. Redis Admins use service projects to create clusters in Memorystore for Redis Cluster.

For a quickstart on creating a cluster with Shared VPC, see [Instance provisioning on a Shared VPC network](https://docs.cloud.google.com/memorystore/docs/cluster/instance-provisioning-shared-vpc).

### Reserved network addresses

After you [create a cluster](https://docs.cloud.google.com/memorystore/docs/cluster/create-manage-instances) that uses a service connection policy, Memorystore for Redis Cluster reserves the following network addresses for the cluster:

  * **Discovery endpoint** : the primary network address that your application uses to [connect to your cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance#view_your_clusters_discovery_endpoint).
  * **Internal backend** : the Memorystore for Redis Cluster backend service uses this network address for management and operational purposes.



Memorystore for Redis Cluster uses both network addresses to serve the traffic for your cluster.

## Supported networking architectures

Memorystore for Redis Cluster supports the network architectures described in this section.

### Same network, project, and region client access example

In this example, the client and Memorystore for Redis Cluster endpoint IP addresses are located in the same network, project, and region.

![Shows clients in the consumer project connecting to a Memorystore for Redis Cluster in a producer project through a private service connect intermediary.](https://docs.cloud.google.com/static/memorystore/img/cluster-networking/cluster-network1.svg)

### Same network and project, but multi-region client access example

In this example, the client and Memorystore for Redis Cluster endpoint IP addresses are located in the same network and project, but in multiple regions.

![Shows clients in different regions in the consumer project connecting to a Memorystore for Redis Cluster in a producer project through a private service connect intermediary.](https://docs.cloud.google.com/static/memorystore/img/cluster-networking/cluster-network2.svg)

### Shared VPC client access example

In this example, the clients are located in different Shared VPC projects. Although clients in this example are in the same region, clients from different regions are also supported.

![Shows clients in various Shared VPC consumer projects connecting to a Memorystore for Redis Cluster in a producer project through a private service connect intermediary.](https://docs.cloud.google.com/static/memorystore/img/cluster-networking/cluster-network3.svg)

### On-premises access example

This diagram shows an example of a client connecting to Memorystore for Redis Cluster from an on-premises network using Cloud Interconnect and Cloud Router. Although the Cloud Interconnect and Cloud Router infrastructure is used, the client machines in the on-premises network connect to Redis using the Memorystore for Redis Cluster endpoint IP addresses. For example, in the diagram in this section, clients connect to 10.142.0.10 and 10.142.0.11 directly.

For more information about finding your cluster's discovery endpoint IP address, see [View your cluster's discovery endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance#view_your_clusters_discovery_endpoint).

![Shows clients in an on-premises network connecting to a Memorystore for Redis Cluster in a producer project through Cloud Interconnect and private service connect intermediaries.](https://docs.cloud.google.com/static/memorystore/img/cluster-networking/cluster-network4.svg)

### Multi-VPC network access

If your clients reside in different VPC networks, then you can use Memorystore for Redis Cluster to have your clients access the same cluster. For each consumer VPC network, Memorystore for Redis Cluster creates a separate pair of Private Service Connect endpoints. Your clients in this network are configured to access the cluster through the [discovery endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#discovery_endpoint) in the network.

To connect to Memorystore for Redis Cluster across multiple VPC networks, do one of the following:

  * If the cluster has [automatically registered Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-automatically-registered-psc-connection), then set up connectivity from the VPC networks to the cluster.
  * If the cluster isn't provisioned with automatically registered Private Service Connect connections, then set up multiple VPC networks by using [user-registered VPC connections](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-user-registered-psc-connection).



## Frequently asked questions

This section covers networking FAQs for Memorystore for Redis Cluster.

#### Do you need a service connection policy?

It depends. For network connectivity, you have two options: a [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) or [user-registered Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/cluster/about-multiple-vpc-networking#psc_connection_types). If you choose a multi-VPC setup, then you can either use the second option or both options together.

User-registered Private Service Connect connections enable you to connect multiple VPC networks, if needed. If you don't need multiple VPC networks, then you can also establish connectivity by using a user-registered connection. However, we recommend using a service connection policy because the process is more straightforward.

#### Why must you enable the Network Connectivity and Service Consumer Management APIs?

If you set up networking using a service connection policy, then Memorystore for Redis Cluster uses Private Service Connect service connectivity automation to automate deployment and connectivity in the consumer network. For automation to work, you must enable these APIs. If you don't, then cluster creation operations fail.

#### Which permissions do you need to set up networking in Memorystore for Redis Cluster?

  * If you want to perform the Redis Admin tasks described on this page, then you need the [`redis.admin`](https://docs.cloud.google.com/memorystore/docs/cluster/access-control) role. To see which roles you need for different Memorystore for Redis Cluster permissions, see [Permissions and their roles](https://docs.cloud.google.com/memorystore/docs/cluster/access-control#permissions_and_their_roles).

  * If you want to perform the Network Admin tasks described on this page, then you need the [`compute.networkAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) role.




#### Which ports do you need to set up networking in Memorystore for Redis Cluster?

Your application connects to Memorystore for Redis Cluster by using an IP address and the 6379 port. As part of this connection, it requests the topology of a cluster.

The request's response contains a list of the data nodes in the cluster and their associated ports. For each node, Memorystore for Redis Cluster uses a port in the 11000-to-13047 range. Therefore, in your firewall, you must allow access to both the 6379 port and to all ports in this range.

#### How can you set up connectivity for your on-premises network?

In addition to the guidance on this page, you can learn about setting up on-premises connectivity by using the following links:

  * [Access endpoints from hybrid networks](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises)
  * [On-premises and hybrid access](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments#on-premises-hybrid-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
