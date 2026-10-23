---
url: https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect/
title: Overview of Private Service Connect in Cloud SQL \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:44.678141+00:00
---

# Overview of Private Service Connect in Cloud SQL  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Overview of Private Service Connect in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect "View this page for the SQL Server database engine")

This document describes concepts associated with Private Service Connect. You can use Private Service Connect for the following:

  * Provide private network connectivity to a Cloud SQL instance from multiple Virtual Private Cloud (VPC) networks that belong to different groups, teams, projects, or organizations.
  * Provide network connectivity to either a Cloud SQL primary instance or any of its read replicas.



Private Service Connect is the default private connectivity method for Cloud SQL instances in new projects.

## Private Service Connect endpoint

You can use [_Private Service Connect endpoints_](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) to access Cloud SQL instances privately from your consumer VPC networks. These endpoints are internal IP addresses that are associated with a forwarding rule that references a service attachment of a Cloud SQL instance.

You can either have Cloud SQL create the endpoint for you automatically, or you can create the endpoint manually.

### Create an endpoint automatically

To have Cloud SQL create an endpoint automatically, do the following:

  1. Create a service connection policy in your VPC networks.
  2. Create a [Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-cloud-sql-instance-psc-enabled-2) with Private Service Connect enabled for the instance and configure the instance to create an endpoint automatically. While creating the instance, specify auto-connection parameters such as VPC networks and projects.

Cloud SQL locates the service connection policy in these networks and creates a Private Service Connect endpoint that points to the service attachment of the instance.

After you create the instance and Cloud SQL creates the endpoint, the clients in the corresponding VPC networks can connect to the instance from the endpoint, either through an IP address or a DNS record.




### Create an endpoint manually

To create an endpoint manually, do the following:

  1. Create a [Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-cloud-sql-instance-psc-enabled) with Private Service Connect enabled for the instance.
  2. Get the [service attachment](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#get-service-attachment) URI that you need to create the endpoint manually.
  3. Reserve an internal IP address in your VPC network for the endpoint and [create an endpoint](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-psc-endpoint) with that address.

After you create the instance and Cloud SQL creates the endpoint, the clients in the corresponding VPC networks can connect to the instance from the endpoint, either through an IP address or a DNS record.


**Note:** You need the [`compute.networkAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) role to create a Private Service Connect endpoint. This role grants full control over the VPC network that initiates a connection to a Cloud SQL instance. You must create this endpoint in each VPC network where database access is needed. To access the endpoint from any region in that network, you must [configure global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) for the endpoint.

## Service connection policy

A [_service connection policy_](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) lets you authorize a specified service class to create a Private Service Connect connection between VPC networks. As a result, you can provision Private Service Connect endpoints automatically.

You can create a maximum of one policy for each service class, region, and VPC network combination. A policy dictates service connectivity automation for that specific combination. When you configure a policy, you select a subnet. The subnet is used to allocate IP addresses for the endpoints that you create through the policy. If multiple service connection policies share the same region, then you can reuse the same subnet for all of the policies.

For example, if you want to use service connectivity automation with two services in three different regions, then create six policies. You can use a minimum of three subnets: one for each region.

After you create a service connection policy, you can only update the policy's subnets and connection limit. If you need to update other fields, then do the following:

  1. Remove all connections that use the policy.
  2. Delete the policy.
  3. Create a new policy.

**Note:** If you choose to create an endpoint automatically, then you can have Cloud SQL create or update a service connection policy for you when you create your Cloud SQL instance. To have Cloud SQL create or update a service connection policy, you need additional IAM permissions. For more information, see [Create a service connection policy automatically](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-service-connection-policy-automatically).

## Service attachment

When you create a [Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance) and configure the instance to use Private Service Connect, Cloud SQL creates a service attachment for the instance automatically. A [_service attachment_](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments) is an attachment point that VPC networks use to access the instance.

You create a Private Service Connect endpoint that the VPC network uses to connect to the service attachment. This enables the network to access the instance.

Each Cloud SQL instance has one service attachment to which the Private Service Connect endpoint can connect through the VPC network. If there are multiple networks, then each network has its own endpoint.

## DNS names and records

For instances with Private Service Connect enabled, we recommend that you connect using a DNS name, because different networks can connect to the same instance and Private Service Connect endpoints in each network might have different IP addresses. Additionally, the Cloud SQL Auth Proxy requires DNS names to connect to these instances. See [Configure DNS in Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-dns).

You can use [DNS automation](https://docs.cloud.google.com/sql/docs/postgres/configure-dns#dns-auto) to automatically provision and manage DNS records for your Cloud SQL instances in your authorized consumer VPC networks.

## Allowed Private Service Connect projects

To connect to Cloud SQL instances that have Private Service Connect enabled, you must add at least one project to its allowlist.

This allowlist controls connections from Private Service Connect endpoints:

  * If a project is in the list of allowed projects, you can successfully create a Private Service Connect endpoint in that project and connect to your Cloud SQL instance.
  * If a project is not in the list of allowed projects, you can still attempt to create a new endpoint. However, the connection will be blocked and the new endpoint will stay in a `PENDING` state until you add that project to the allowlist.



### Project removal and reconciliation

If you remove a project from the list of allowed projects:

  * For all Cloud SQL instance creations, clones, and Private Service Connect enablements in August 2026 and after, connection reconciliation behavior is enabled by default and cannot be disabled. When you remove a project from the list of allowed projects, all existing Private Service Connect connections from the removed project are immediately closed (reconciled). This means applications using Private Service Connect endpoints in those removed projects cannot continue connecting using those endpoints.
  * For instances created before August 2026, when you remove a project from the list of allowed projects, applications using Private Service Connect endpoints in those removed projects continue to connect until you manually remove those endpoints.



## Private Service Connect endpoint propagation

By default, Private Service Connect connections aren't transitive from peered VPC networks. You must create a Private Service Connect endpoint in each VPC network that needs to connect to your Cloud SQL instance. For example, if you have three VPC networks that have to connect to your instance, then you must create three Private Service Connect endpoints — one endpoint for each VPC network.

However, by propagating Private Service Connect endpoints through the [Network Connectivity Center hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview), these endpoints can be reachable by any other [spoke VPC network](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) in the same hub. The hub provides a centralized connectivity management model to interconnect spoke VPC networks to Private Service Connect endpoints.

The connection propagation feature in NCC benefits the following use case for Private Service Connect deployments:

You can use a common services VPC network to create multiple Private Service Connect endpoints. By adding a single common services VPC network to the NCC hub, all Private Service Connect endpoints in the VPC network become accessible transitively to other spoke VPC networks through the hub. This connectivity eliminates the need to manage each Private Service Connect endpoint in each VPC network individually.

To learn how to use the NCC hub to propagate Private Service Connect endpoints to spoke VPC networks, see the [NCC—Private Service Connect propagation codelab](https://codelabs.developers.google.com/ncc-psc-propagation#0).

## Private Service Connect backend

You can use [_Private Service Connect backends_](https://docs.cloud.google.com/vpc/docs/private-service-connect#backends) as an alternative to [_Private Service Connect endpoints_](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints), to access Cloud SQL instances. For ease of use, we recommend connecting to your Cloud SQL instances using Private Service Connect endpoints. For additional control and visibility, you can connect using Private Service Connect backends.

To use Private Service Connect backends, you must set up the following resources for each serving port on which you want to access a given Cloud SQL instance:

  * [Private Service Connect Network Endpoint Group (NEG)](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#neg-published-service), which must reference the service attachment and a serving port of the Cloud SQL instance.
  * [Internal Proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) (consisting of Backend Service, Target TCP Proxy, and Forwarding Rule) with its backend being the Private Service Connect NEG.

The supported serving ports for PostgreSQL are as follows: 
  * TCP port 5432 for direct connections to PostgreSQL database server.
  * TCP port 6432 for direct connections to PgBouncer server when using [Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling#ports-psql).
  * TCP port 3307 for connections through [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy). 



## Private Service Connect outbound connections

You can attach a Private Service Connect interface to your existing Cloud SQL Private Service Connect-enabled instances using a [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments) to allow your Cloud SQL instance to make outbound connections to your network. To connect to your network's Private Service Connect interface, you either need a new or existing network attachment within your Google Cloud project.

You can use outbound connectivity to migrate data from an external server within your network, use PostgreSQL extensions that require an outbound connection to your Cloud SQL instance, or do a [homogeneous migration](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations) using Database Migration Service.

### Limitations

If you configure outbound connectivity on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery), then after either a replica switchover or a replica failover operation, when the DR replica is promoted to the primary instance, outbound connectivity continues to work on the new primary that's created. If you don't configure outbound connectivity on the DR replica, then in order for the service to continue to work after either a replica switchover or replica failover operation, you need to enable Private Service Connect outbound connectivity on the new primary instance.

When using a Private Service Connect interface with a network attachment to create outbound connections to your network from your Cloud SQL instance, note the following limitations:

  * Enabling or disabling Private Service Connect outbound connectivity requires downtime. You can expect this operation to take about 8 minutes to complete with an approximate downtime of 3 minutes.
  * If you're using a hostname or DNS for your outbound connection, then the DNS name must be publicly resolvable and resolved to an RFC-1918 IP range.
  * IPv6 addresses aren't supported.
  * Public IP addresses aren't supported.
  * If the outbound connectivity IP address conflicts with the `eth0` IP or the Private Service Connect forwarding rule, then the IP address might not connect correctly. For more information, see [Private Service Connect overview](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint).
  * You can't enable Private Service Connect outbound connectivity when you create the Cloud SQL instance. To enable outbound connectivity, you must edit your instance settings after creation.
  * If your instance is configured for [both private service access and Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access-and-private-service-connect), then you can't enable Private Service Connect outbound connectivity for your instance. 
  * Private Service Connect outbound connectivity cannot be enabled on [read pool](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools) instances.



For more information on how to setup outbound connectivity for your Cloud SQL instance, see [Configure outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#configure-psc-outbound).

## What's next

  * Learn more about [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip).
  * Learn more about [configuring an instance for Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
