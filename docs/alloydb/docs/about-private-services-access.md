---
url: https://docs.cloud.google.com/alloydb/docs/about-private-services-access/
title: Private services access overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:54.833398+00:00
---

# Private services access overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/about-private-services-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Private services access overview Stay organized with collections  Save and categorize content based on your preferences. 

To let clients in your Virtual Private Cloud (VPC) network communicate privately with your AlloyDB for PostgreSQL instances, you can configure [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access). Private services access establishes a private VPC Network Peering connection between your VPC network and the Google-managed network that hosts the internal resources required by your AlloyDB instances.

For a general overview of how network connections work with AlloyDB, see [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview).

## Connectivity between clusters and internal resources

Private services access lets AlloyDB clusters communicate with the internal resources that enable them.

### Instances and internal resources

The AlloyDB clusters and instances that you create in your Google Cloud project rely upon many internal, low-level Google Cloud resources. These include the virtual machine (VM) instances that serve as AlloyDB nodes and load balancers, or the storage volumes that hold your data. All of the resources that power a cluster run within a Google Cloud project that's internal to and managed by Google.

Generally, you don't connect directly to these internal resources. Instead, you manage clusters and instances through the Google Cloud console or Google Cloud CLI. Your applications connect to AlloyDB instances through their private IP addresses to query and modify your data. AlloyDB uses internal APIs to pass your administrative requests or data queries to your cluster's resources as needed.

an AlloyDB instance acts as a logical abstraction of this complex collection of parts. By offering you a private, static IP address and a consistent, PostgreSQL-compatible database interface, AlloyDB can freely update an active instance's internal network routes or relocate its internal resources. This architecture provides optimized throughput and high availability without downtime or disruption.

### How clusters use private services access

The AlloyDB clusters and instances in your project communicate with their internal resources through _private services access_. This establishes a permanent, peered connection between a VPC network in your own project and the separate VPC network used by the Google-managed project hosting the internal resources. Through this connection, the AlloyDB clusters and instances in your project can connect to their internal resources using private IP addresses, just as if they were located within your own project's VPC network.

Configuring private services access with a Google Cloud VPC network involves reserving one or more blocks of contiguous private IP addresses. After Google Cloud establishes a peering connection between your project's VPC network and the internal project's VPC network, AlloyDB applies addresses from your reserved IP blocks to the low-level resources that your instances require. This connection allows private network connectivity among all the working parts of your clusters.

When you create an AlloyDB cluster that uses private services access (rather than [Private Service Connect](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect)), you must specify a VPC network within your project that is configured for private services access. Your project might already have a qualifying VPC network available, especially if your project has already worked with AlloyDB or another Google Cloud product that requires private services access. If your project does not have a VPC network set up for private services access, then you must configure one before creating a cluster with private services access.

You cannot change the private services access configuration of a cluster after AlloyDB has created the cluster.

## Supported private services access configurations

AlloyDB can use private services access configurations in VPC networks that reside in the same project as AlloyDB or that reside in other projects.

### A VPC network in the same project as your cluster

How you configure AlloyDB connectivity using a VPC network that resides in the same Google Cloud project as your AlloyDB cluster depends on whether a private services access configuration already exists in the VPC network:

  * If the VPC network does not already have private services access configured, then [create a private services access configuration](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

  * If the VPC network already has an existing private services access configuration, then make sure the configuration has sufficient IP address space for AlloyDB and [increase the address space](https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase) if necessary.




### A Shared VPC network

To configure AlloyDB connectivity using a VPC network that resides in a Google Cloud project that is different from the one containing your AlloyDB cluster, complete the following steps:

  1. Configure the project where the VPC network resides for [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), with it as the _host project_ and the project where AlloyDB resides as a _service project_.

  2. Make sure the VPC network's private services access configuration has sufficient IP address space for AlloyDB and [increase the address space](https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase) if necessary.

  3. Configure users who can create AlloyDB resources as _Service Project Admins_ with access to the appropriate allocated IP address ranges in the private services access configuration.

  4. When using Google Cloud CLI to create an AlloyDB cluster or instance with a Shared VPC network, make sure that you use the fully qualified path of the VPC network—for example, `projects/cymbal-project/global/networks/shared-vpc-network`.




For more information about Shared VPC, see [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc) and [Provisioning Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc).

## IP address range size considerations

It's important to choose a private services access address range that is wide enough to accommodate the needs of AlloyDB, as well as any other Google Cloud services that require IP addresses from the same address pool. You can adjust the size of this pool at any time.

AlloyDB uses a subnet of size `/24` in each region where you deploy a cluster. While the minimum size is a single `/24` block (256 addresses), the recommended size is a `/16` block (65,536 addresses). This range lets you create clusters and instances in multiple regions, and still leave plenty of IP addresses available for [other Google Cloud services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services).

When you provision new instances in clusters configured with private services access, AlloyDB deploys the resources in newly created or existing regional subnets that were previously created by AlloyDB. If an existing subnet is found to be sufficiently full, AlloyDB creates a new subnet in the same region provided that the allocated IP address range is large enough to create an additional subnet of size `/24`. If the existing IP address space available to AlloyDB is not large enough to create the subnet, then your attempt to create the cluster or instance fails. You must increase the IP address space to resolve the address shortage before retrying to create the cluster or instance. For more information about increasing the IP address space, see [Increase the IP address space available to AlloyDB within your project](https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase). If you no longer need an allocated IP address range after deleting all clusters and instances that use it, see [Remove a private services access allocated range](https://docs.cloud.google.com/alloydb/docs/psa-remove-allocated-range).

## Privately used public IP ranges

AlloyDB doesn't support the use of privately used public IP (PUPI) ranges when using private services access. To connect to AlloyDB from workloads using privately used public IP (PUPI) ranges, you must use [Private Service Connect](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect).

## Limitations

  * Private services access connections are limited to [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) IP ranges.



## What's next

  * [Enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

  * [Learn more about private services access in Google Cloud](https://docs.cloud.google.com/vpc/docs/private-services-access).

  * [Increase the IP address space available to AlloyDB within your project](https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase).

  * [Remove a private services access allocated range](https://docs.cloud.google.com/alloydb/docs/psa-remove-allocated-range).

  * [Deploy AlloyDB with private services access using Terraform](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/blob/main/docs/AlloyDB/alloydbinstance-using-psa-accessed-from-gce.md).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
