---
url: https://docs.cloud.google.com/managed-spark/docs/networking-private-service-connect/
title: Managed Service for Apache Spark cluster networking with Private Service Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:57.841224+00:00
---

# Managed Service for Apache Spark cluster networking with Private Service Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/networking-private-service-connect/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark cluster networking with Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on configuring network connectivity for Managed Service for Apache Spark clusters when using Private Service Connect. It explains the interaction between Private Service Connect and Virtual Private Cloud peering for different Managed Service for Apache Spark use cases. It also summarizes feature similarities and differences among Private Google Access, Private Service Connect, and Cloud NAT.

## Overview

Managed Service for Apache Spark clusters require network connectivity to Google Cloud APIs and services, such as the Dataproc API, Cloud Storage, and Cloud Logging, and to user resources, such as data sources in other Virtual Private Cloud networks or on-premises environments.

By default, Managed Service for Apache Spark clusters created with image versions `2.2` and later are created with internal IP addresses only. Managed Service for Apache Spark automatically enables [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the regional subnet used by the internal-IP-only cluster to enable connections to Google APIs and services without connecting to the public internet.

To provide more granular network control, you can configure a cluster to use Private Service Connect, which routes traffic to supported Google APIs and services through a private endpoint within your VPC network. This can be beneficial for security and compliance.

## Common private networking options

This section describes Private Google Access, Private Service Connect, and Cloud NAT features and differences.

  * [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) is a one-way path for VMs to reach Google public services without using the internet. It is similar to a special roadway exit from your neighborhood (VPC subnet) that leads directly to the Google services mall, bypassing public roads. Everyone in the neighborhood can use it. Managed Service for Apache Spark automatically enables Private Google Access on the regional subnet used by Managed Service for Apache Spark clusters created with image version `2.2` and later.

  * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) creates a private, two-way endpoint for a service that is located within your VPC network. It is similar to a dedicated private path from your location (VPC network) directly into a service. It has an address at your location (an internal IP address in your VPC network) and only you can use it.

  * [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) allows VMs with private IP addresses to access the internet.




### Features and differences

Feature | Private Google Access (PGA) | Private Service Connect (PSC)  
---|---|---  
How it works | Directs traffic from a VM to a special Google IP address range (`private.googleapis.com`). | Creates a forwarding rule (endpoint) inside your VPC network that represents the Google service.  
IP address | Your VM connects to a Google-owned IP address. | Your VM connects to an internal IP address that you own within your VPC network.  
Direction | Outbound only: Your VM initiates a connection to Google. | Bi-directional: Your VM connects to the service, and the service can initiate return traffic.  
Scope | Enabled or disabled for an entire subnet. | Deployed as a specific endpoint resource.  
Services | Connects only to Google APIs, such as Cloud Storage, BigQuery, or Dataproc API. | Connects to Google APIs, services from other companies, and your own services.  
  
For Managed Service for Apache Spark, Private Google Access is the simpler, traditional method to allow cluster VMs to contact the Managed Service for Apache Spark control plane. Private Service Connect is a more recent and flexible approach that gives you fine-grained control, particularly in complex or multi-tenant networks.

**Why use Private Service Connect?** Even if your Managed Service for Apache Spark cluster has internal-only IP addresses with Private Google Access enabled (the default configuration for `2.2+` image version clusters), Private Service Connect offers the following advantages:

  * Instead of using the Private Google Access shared set of endpoints to connect to Google APIs and services, Private Service Connect lets you create a private endpoint with an internal IP address inside your VPC network that maps directly to a specific Google service.

  * You can create firewall rules that allow traffic only to the Private Service Connect endpoint IP address. For example, you can configure a rule that allows egress traffic from Managed Service for Apache Spark cluster VMs exclusively to the internal IP address of the Private Service Connect endpoint for BigQuery, while denying all other egress traffic. This is a more secure approach than creating broader firewall rules with Private Google Access.

  * Using the Private Service Connect endpoint within your VPC network makes the network path explicit and easier to audit for security and compliance since traffic to a service such as Cloud Storage doesn't share a path with other API traffic.




### Private and public paths

Private Google Access, Private Service Connect, and Cloud NAT allow hosts with [`RFC 1918`](https://www.rfc-editor.org/rfc/rfc1918) addresses to reach Google Cloud services. They also allow Google Cloud resources with private `RFC 1918` addresses to initiate connections to Google Cloud services.

An important distinction to make when assessing different connection options is whether traffic using the connection remains private or travels over the public internet.

  * Private Google Access and Private Service Connect keep traffic within Google's private network. Data does not travel over the public internet to reach Google Cloud services, which is ideal for security and predictable performance.

  * Cloud NAT reaches a Google Cloud service by connecting to a public endpoint for the service. The traffic leaves your VPC network through the NAT gateway and travels over the internet.




### How each option works

Here's a breakdown of each connection mechanism:

Method | Path to service | Destination endpoint | Primary use case  
---|---|---|---  
Private Google Access | Google private network | Special Google IP addresses (`private.googleapis.com`) | Simple, subnet-level access for VMs to reach Google APIs privately.  
Private Service Connect | Google private network | A private IP address endpoint inside your VPC network | Granular, secure access to Google APIs, third-party or your own services.  
Cloud NAT | Public internet | Service public IP address | General-purpose outbound internet access for VMs with private IP addresses.  
  
## Configure Private Service Connect

To use Private Service Connect with your Managed Service for Apache Spark cluster, you must configure the necessary Private Service Connect endpoints and DNS in your VPC network for all Google APIs that Managed Service for Apache Spark depends on. For instructions on setting up your subnet and configuring DNS, see [About accessing Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints).

You can use Private Service Connect with a Managed Service for Apache Spark cluster that has internal-only IP addresses with Private Google Access enabled (the default configuration for `2.2+` image version clusters).

## Enable peering if needed

While Private Service Connect provides private access to many Google services, you may also need to enable [VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), particularly in the following scenarios:

  * Other Virtual Private Cloud networks: Private Service Connect connects to _Google-managed services_ , not directly to other customer VPC networks. If your data sources, custom applications, or other services are located in a different VPC network than your Managed Service for Apache Spark cluster, typically VPC peering is required to enable private communication between these networks.

  * On-premises networks: If your Managed Service for Apache Spark cluster accesses data or services in your on-premises environment, you will need a Cloud VPN or Cloud Interconnect connection to your on-premises network, often combined with VPC peering.

  * Comprehensive internal communication to Google services: While Private Service Connect provides private access to configured Google services, such as Cloud Storage and BigQuery, internal control plane communications or specific Managed Service for Apache Spark features might require VPC peering to a network with broad Google service accessibility to access underlying Google infrastructure or other Google APIs.

Even though a VPC peering sandbox environment succeeds in providing access to necessary backend Google services, cluster connectivity issues can arise later in a production environment when Private Service Connect has not been fully configured.
  * Access to data sources in other VPC networks: If your Managed Service for Apache Spark jobs read from or write to data sources, such as Cloud SQL, self-managed databases, and custom applications, that are located in a different VPC network, you must establish VPC peering between your Managed Service for Apache Spark cluster VPC network and the VPC network containing those data sources. Private Service Connect does not provide inter-VPC network communication between customer-owned networks.

  * Hybrid connectivity: For hybrid cloud deployments where Managed Service for Apache Spark clusters need to interact with resources in an on-premises data center, VPC peering is essential to connect your on-premises network to your Google Cloud VPC network using Cloud VPN or Cloud Interconnect.




## Troubleshoot Private Service Connect

If your Managed Service for Apache Spark cluster with Private Service Connect (without VPC peering) fails to create or has connectivity issues, use the following steps to help troubleshoot and resolve the problem:

  * Confirm required API access:

    * Verify that all necessary Google APIs are enabled in your Google Cloud project.
  * Verify Private Service Connect endpoint configuration:

    * Verify that a Private Service Connect endpoint is correctly configured for all Google APIs that the cluster requires, such as `dataproc.googleapis.com`, `storage.googleapis.com`, `logging.googleapis.com`, `bigquery.googleapis.com`, `compute.googleapis.com`.

    * Use tools such as `dig` or `nslookup` from a VM within the VPC subnet to confirm that the DNS records for required services correctly resolve to the private IP addresses within your VPC network using the Private Service Connect endpoint.

  * Check firewall rules:

    * Verify that firewall rules in your VPC network allow outbound connections from Managed Service for Apache Spark cluster instances to Private Service Connect endpoints.

    * If using Shared VPC, verify that appropriate firewall rules are configured in the host project.

  * Examine Managed Service for Apache Spark cluster logs:

    * Review the cluster creation logs in Logging for any network related errors, such as `connection refused`, `timeout`, or "`unreachable host`. These errors can indicate a missing route or incorrect firewall rule. Examine the serial console logs of cluster instances.
  * Assess the need for VPC peering:

    * Based on workload dependencies, if your Managed Service for Apache Spark cluster requires connectivity to resources that are not Google-managed, such as databases in a separate VPC network and on-premises servers, establish VPC peering.

    * Examine the network requirements of Google Cloud services that your Managed Service for Apache Spark cluster interacts with. Some services may have specific peering requirements even when used with Private Service Connect.




## Follow best practices

  * Comprehensive network architecture planning: Before deploying Managed Service for Apache Spark with Private Service Connect, carefully design your network architecture, considering all implicit and explicit dependencies and data flow paths. This includes identifying all Google APIs that your Managed Service for Apache Spark cluster interacts with during provisioning and operation.

  * Test connectivity: Thoroughly test network connectivity from your Managed Service for Apache Spark cluster to all required services and data sources during the development and staging phases.

  * Use the [Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center/docs): Use Google Cloud Network Intelligence Center tools, such as [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests), to diagnose and troubleshoot network connectivity issues.




## What's next

  * Learn more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * Understand [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  * Explore Managed Service for Apache Spark cluster [networking configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
