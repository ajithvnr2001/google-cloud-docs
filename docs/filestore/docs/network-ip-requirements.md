---
url: https://docs.cloud.google.com/filestore/docs/network-ip-requirements/
title: Network configuration and IP resource requirements \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:50:59.995468+00:00
---

# Network configuration and IP resource requirements  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/network-ip-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Network configuration and IP resource requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses network configuration and IP resource requirements for Filestore.

## Connectivity support

Filestore connects to your Virtual Private Cloud (VPC) network using either [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) or [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-services-connect). The following chart shows which connection method supports specific scenarios:

Scenario | VPC Network Peering | Private services access | Private Service Connect  
---|---|---|---  
Set up connectivity for Filestore Basic instances. | Yes | Yes | No  
Set up connectivity for Filestore Zonal and Regional instances. | Yes | Yes | Yes  
Create an instance with a standalone VPC network. | Yes | Yes | Yes  
Create an instance on a Shared VPC network from the host project. | Yes | Yes | Yes  
Create an instance on a Shared VPC network from a service project. | No | Yes | Yes  
Create an instance on using Google Cloud console. | Yes | Yes | Yes  
Create an instance on using Google Cloud CLI, Filestore API. | Yes | Yes | Yes  
Use centralized IP range management for multiple Google services. | No | Yes | Yes  
Access an instance from on-premises networks using Cloud VPN or Cloud Interconnect. | Yes | Yes | Yes  
Specify a manually selected IP address for Filestore instances. | No | No | Yes  
  
Filestore supports the following connectivity scenarios:

  * Most any Compute Engine VM or Google Kubernetes Engine (GKE) cluster can access any Filestore instance that's on the same VPC network. All internal IP addresses in the selected VPC network can connect to the Filestore instance unless access is restricted using IP-based access control.

    * Clients with an IP address in the `172.17.0.0/16` range can't connect to Filestore instances. For more information, see [Known issues](https://docs.cloud.google.com/filestore/docs/known-issues#clients_cant_have_an_ip_address_from_the_172170016_range).

**Note:** This limitation doesn't apply when using Private Service Connect. For more information, see [Create a Filestore instance with Private Service Connect](https://docs.cloud.google.com/filestore/docs/configure-psc).
  * You can connect Filestore instances to clients in remote networks using Cloud VPN or Cloud Interconnect, including clients from another project or your on-premises clients.

  * You can connect non-[RFC 1918](https://tools.ietf.org/html/rfc1918) clients to Filestore. In this case, you must explicitly grant them access to the Filestore instance using [IP-based access control](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control).




Filestore doesn't support [transitive peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#transit-network). For example, if VPC network N1 is peered to Filestore's internal network, and another VPC network, N2, is peered to N1, N2 won't have connectivity to the Filestore instance. Only clients on N1 can access the Filestore instance.

## Firewall rules

You may need to create firewall rules in the following scenarios:

  * To enable NFS file locking, you may need to open up the ports used by the `statd` and `nlockmgr` daemons. For more information, see [Configuring firewall rules](https://docs.cloud.google.com/filestore/docs/configuring-firewall).
  * In the Shared VPC scenario, NFS access is not restricted to the service project by default. You can set firewall rules or use [IP-based access control](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control) to restrict access, but these solutions don't specifically enforce project boundaries.



## Legacy network support

You can't use a legacy network with Filestore instances. If necessary, create a new VPC network to use by following the instructions at [Creating a new VPC network with custom subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network).

## IP resource requirements

Each Filestore instance must have an IP address range associated with it. Both [RFC 1918](https://tools.ietf.org/html/rfc1918) and non-RFC 1918 IP address ranges ([GA](https://cloud.google.com/products#product-launch-stages)) are supported.

During instance creation, Filestore can either manually provide a specific IP address range for your instance or let Filestore automatically allocate an IP address range and assign IP addresses from that range to the instance. When you create an instance with Private Service Connect through Google Cloud CLI or Filestore API, you can manually provide a specific IPv4 or IPv6 address.

After you create the instance, you can't change the assigned IP addresses. If you want to introduce changes, delete and recreate the instance with a new IP address range.

For more information, see [Configure a reserved IP address range](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_a_reserved_ip_address_range).

## What's next

  * [Acquire the Identity and Access Management (IAM) roles and permissions](https://docs.cloud.google.com/filestore/docs/iam) needed to use Filestore.
  * Try one of the Filestore quickstarts: 
    * Using the [Google Cloud console](https://docs.cloud.google.com/filestore/docs/quickstart-console)
    * Using the [Google Cloud CLI](https://docs.cloud.google.com/filestore/docs/quickstart-gcloud)
  * Learn more about [VPC networks and subnets](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).
  * Troubleshoot [common Filestore networking issues](https://docs.cloud.google.com/filestore/docs/troubleshooting).
  * [Create a Filestore instance on a Shared VPC network in service projects](https://docs.cloud.google.com/filestore/docs/shared-vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
