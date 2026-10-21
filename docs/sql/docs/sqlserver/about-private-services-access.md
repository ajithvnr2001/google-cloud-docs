---
url: https://docs.cloud.google.com/sql/docs/sqlserver/about-private-services-access/
title: Overview of private services access in Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:21.064364+00:00
---

# Overview of private services access in Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/about-private-services-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Overview of private services access in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/about-private-services-access "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/about-private-services-access "View this page for the PostgreSQL database engine") | SQL Server

This document explains how private services access provides private IP connectivity for Cloud SQL, and covers IP address allocation, network and security considerations, and multi-VPC connectivity.

**Private services access** is implemented as a [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) connection between the [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) and the _service provider_ VPC network where your Cloud SQL instance resides. This private networking connection lets VM instances in your VPC network and the Google Cloud services that you access communicate exclusively using private IP addresses with your Cloud SQL instance. The VM instances don't need internet access or external IP addresses to reach services that are available through private services access.

## IP addresses

To use private services access in a VPC network, one or more IP address ranges need to be available for the VPC (for more information about IP addresses, see [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses)). These ranges must be large enough for Cloud SQL and any other Google Cloud managed services that you plan to use. Cloud SQL and other Google Cloud services each require dedicated IP blocks from the allocated ranges. The minimum size for such blocks is 256 addresses (prefix length `/24`), although the recommended size is 65,536 addresses (prefix length `/16`).

**Tip:** The number of addresses in an IP block is 2n, where n is 32 minus the prefix character length. For example, the number of addresses in a `/20` block is 2(32-20) = 212 = 4,096.

If you're going to create instances in multiple regions or for different database types, you must have at least a `/24` range of IP addresses available for each region or database type. This includes other applications such as [Filestore](https://docs.cloud.google.com/filestore/docs) or [Memorystore](https://docs.cloud.google.com/memorystore/docs).

When you set up private services access, you can select an existing range or allocate a new one. If you let Google Cloud allocate the range for you, as described in the next section, then Google Cloud allocates a range of prefix length `/24` under the name `default-ip-range`.

#### When to use separate CIDR ranges

Since Cloud SQL uses `/24` CIDR ranges as an IP range unit, there are several conditions where separate `/24` ranges are required.

  * **Regional separation** : If you create two Cloud SQL instances in two separate regions, then you must allocate at least two separate /24 CIDR ranges. Each IP range unit can be used only for Cloud SQL instances within a single region.
  * **Enforced network architecture separation** : Instances that you create using the [`--enforce-new-sql-network-architecture`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/create#--enforce-new-sql-network-architecture) flag (or the equivalent API field) can't share the same IP range unit with instances in the same project that use the old network architecture. The instances that you create with the new network architecture require their own dedicated /24 ranges in every region.

**Important:** If you've completed the [network architecture upgrade](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) for an entire project, then any new instances that you create are no longer subject to enforced architecture separation. However, existing instances in the project that are subject to these conditions must remain in their allocated IP ranges.

### Private services access example

In this example, the VPC network allocated the address range `10.240.0.0/16` for Google Cloud services and established a private connection using that range. Each Google Cloud service (for example, Cloud SQL), creates a subnet from the allocated block to provision new resources in a given region, such as Cloud SQL instances.

![Diagram overview of private IP configuration.](https://docs.cloud.google.com/static/sql/images/private-ip.svg)

The diagram illustrates the following aspects of the private services access configuration:

  * The private connection is assigned the `10.240.0.0/16` allocated range. Using this allocation, Google Cloud services can create subnets where new resources are provisioned.
  * On the Google Cloud services side of the private connection, Google Cloud creates a project for the customer. The project is isolated, meaning no other customers share it and the customer is billed for only the resources the customer provisions.
  * Each Google Cloud service creates a subnet in which to provision resources. The subnet's IP address range is typically a `/24` Classless Inter-Domain Routing (CIDR) block that's chosen by the service and comes from the allocated IP address range. You can't modify the service producer's subnet. A service provisions new resources in existing regional subnets that were previously created by that service. If a subnet is full, the service creates a new subnet in the same region.
  * VM instances in the customer's network can access service resources in any region if the service supports it. Some services might not support cross-region communication. View the relevant service's documentation for more information.
  * [Outbound data transfer costs](https://docs.cloud.google.com/vpc/network-pricing#general) for cross-regional traffic, where a VM instance communicates with resources in a different region, still apply.
  * The Cloud SQL instance is assigned the IP address `10.240.0.2`. In the Customer VPC network, requests with a destination of `10.240.0.2` are routed to the private connection over the service producer's network. After the request reaches the service network, the service network contains routes that direct the request to the correct resource.
  * Traffic between VPC networks travels internally within the Google Cloud network, not through the public internet.



## Network considerations

Cloud SQL allocates a `/24` subnet from the private services access IP range for each region. For example, placing SQL Server instances in two regions requires that the allocated IP address ranges include at least two available subnets of size /24.

Connections to a Cloud SQL instance using a private IP address are automatically authorized for [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). This way, all private clients can access the database without going through the Cloud SQL Auth Proxy.

**Note:** You must configure all the Non-RFC 1918 IP address ranges as [authorized networks](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks) of the Cloud SQL for SQL Server instances. Alternatively, you can connect to your instance using the [Cloud SQL Auth Proxy client](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy).

Cloud SQL doesn't learn Non-RFC 1918 subnet routes from your VPC by default. You need to update the network peering to Cloud SQL to export any Non-RFC 1918 routes.

## Security considerations

Traffic over private services access is provided with a certain level of encryption. For more information, see Google Cloud [virtual network encryption and authentication](https://docs.cloud.google.com/security/encryption-in-transit#virtual-network).

The [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy) can be configured to connect using private services access, and provides authentication using IAM credentials and end-to-end encryption using a rotating SSL/TLS certificate.

If your security requirements mandate self-managed SSL/TLS certificates that you manage, see the instructions in [Configuring SSL/TLS](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance).

Creating one VPC network for each instance with a private IP address provides better network isolation than putting all instances in the "default" VPC network.

## Multiple VPC connectivity

Cloud SQL supports private IP addresses through [private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access). When you create a Cloud SQL instance, Cloud SQL creates the instance within its own VPC network, called the Cloud SQL VPC. Enabling private IP requires [setting up a peering connection](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#example) between the Cloud SQL VPC and your VPC network. This allows resources in your VPC network to access the internal IP addresses of your Cloud SQL resources in the Cloud SQL VPC network.

Using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), Cloud SQL implements private services access internally, which allows internal IP addresses to connect across two VPC networks regardless of whether they belong to the same project or organization. However, since VPC Network Peering isn't transitive, it only broadcasts routes between the two VPCs that are directly peered. If you have an additional VPC, it won't be able to access your Cloud SQL resources using the connection set up with your original VPC.

To mitigate this limitation and connect your Cloud SQL instance to multiple VPCs using private IP addresses, you can use the following connection options:

  * Connect using custom advertised routes
  * Connect using an intermediate proxy (SOCKS5)
  * Connect using the Cloud SQL Auth Proxy as a service



For more information about how to connect multiple VPCs, see [Connect your instance to multiple VPC networks](https://docs.cloud.google.com/sql/docs/sqlserver/connect-multiple-vpcs).

## What's next?

  * Learn more about [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).
  * Learn more about [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * Learn more about [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc).
  * Learn more about [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  * Learn more about [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
