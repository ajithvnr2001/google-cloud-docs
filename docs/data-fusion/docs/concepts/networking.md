---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/networking/
title: Introduction to Cloud Data Fusion networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:01.311887+00:00
---

# Introduction to Cloud Data Fusion networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Introduction to Cloud Data Fusion networking Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Data Fusion lets you connect to your data sources from public or private instances across pipeline design and execution environments.

**Note:** This guidance applies to Cloud Data Fusion versions higher than 6.4.

## Before you begin

Networking in Cloud Data Fusion requires a basic understanding of the following:

#### Tenant project

Cloud Data Fusion creates a tenant project that holds the resources and services needed to manage pipelines on your behalf, such as when it runs pipelines on the Managed Service for Apache Spark clusters that reside in your customer project.   
  
The tenant project isn't exposed to you directly, but when you create a private instance, you use the project's name to set up VPC peering. Each private instance in the tenant project has its own VPC network and subnet.   
  
The project can have multiple Cloud Data Fusion instances. You manage the resources and services it holds when you access an instance in the Cloud Data Fusion UI or Google Cloud CLI.   
For more information, see the Service Infrastructure documentation about [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant). 

#### Customer project

The customer creates and owns this project. By default, Cloud Data Fusion creates an ephemeral Managed Service for Apache Spark cluster in this project to run your pipelines.

#### Cloud Data Fusion instance

A Cloud Data Fusion instance is a unique deployment of Cloud Data Fusion, where you design and execute pipelines. You can create multiple instances in a single project and specify the Google Cloud region in which to create the Cloud Data Fusion instances. Based on your requirements and cost constraints, you can create an instance that uses the [Developer, Basic, or Enterprise](https://docs.cloud.google.com/data-fusion/pricing) edition of Cloud Data Fusion. Each instance contains a unique, independent Cloud Data Fusion deployment that contains a set of services that handle pipeline lifecycle management, orchestration, coordination, and metadata management. These services run using long-running resources in a [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant). 

## Network diagram

The following diagrams show the connections when you build data pipelines that extract, transform, blend, aggregate, and load data from various on-premises and cloud data sources.

See the diagrams for [controlling egress in a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/egress-control) and [connecting to a public source](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-public-source).

## Pipeline design and execution

Cloud Data Fusion provides separation of design and execution environments, which lets you design a pipeline once, and then execute it in multiple environments. The design environment resides in the tenant project, while the execution environment is in one or more customer projects.

Example: You design your pipeline using Cloud Data Fusion services, such as Wrangler and Preview. Those services run in the tenant project, where access to data is controlled by the Google-managed [Cloud Data Fusion Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) role. You then execute the pipeline in your customer project so that it uses your Managed Service for Apache Spark cluster. In the customer project, the default Compute Engine service account controls access to data. You can configure your project to use a custom service account.

For more information about configuring service accounts, see [Cloud Data Fusion service accounts](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts).

### Design environment

When you create a Cloud Data Fusion instance in your customer project, Cloud Data Fusion automatically creates a separate, Google-managed tenant project to run the services required to manage the lifecycle of pipelines and metadata, the Cloud Data Fusion UI, and design-time tools like Preview and Wrangler.

#### DNS resolution in Cloud Data Fusion

To resolve domain names in your design-time environment when you wrangle and preview the data that you're transferring into Google Cloud, use DNS Peering (available starting in Cloud Data Fusion 6.7.0). It lets you use domain or hostnames for sources and sinks, which you don't need to reconfigure as often as IP addresses.

DNS resolution is recommended in your design-time environment in Cloud Data Fusion, when you test connections and preview pipelines that use domain names of on-premises or other servers (such as databases or FTP servers), in a private VPC network.

For more information, see [DNS Peering](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) and [Cloud DNS Forwarding](https://cloud.google.com/blog/products/networking/announcing-cloud-dns-forwarding-unifying-hybrid-cloud-naming).

### Execution environment

After you verify and deploy your pipeline in an instance, you either execute the pipeline manually, or it executes on a time schedule or a pipeline state trigger.

Whether the execution environment is provisioned and managed by Cloud Data Fusion or the customer, the environment exists in your customer project.

**Note:** As an execution environment and a managed service, Managed Service for Apache Spark has its own network and firewall requirements.

## Public instances (default)

The easiest way to provision a Cloud Data Fusion instance is to create a public instance. It serves well as a starting point and provides access to external endpoints on the public internet.

A public instance in Cloud Data Fusion uses the default VPC network in your project.

**Note:** Both design and execution environments have external IP addresses that are kept behind a firewall to control access.

The default VPC network has the following:

  * Autogenerated subnets for each region
  * Routing tables
  * Firewall rules to ensure communication among your computing resources



### Networking across regions

When you create a new project, a benefit of the default VPC network is that it autopopulates one subnet per region using a predefined IP address range, expressed as a CIDR block. The IP address ranges start with `10.128.0.0/20`, `10.132.0.0/20`, across the Google Cloud global regions.

To ensure that your computing resources connect to each other across regions, the default VPC network sets the default local routes to each subnet. By setting up the default route to the internet (`0.0.0.0/0`), you gain access to the internet and capture any unrouted network traffic.

### Firewall rules

The default VPC network provides a set of firewall rules:

Default | Description  
---|---  
Default allow `icmp` | Enable `icmp` protocol for source `0.0.0.0/0`  
Default allow internal | Enable `tcp:0-65535`; `udp:0-65535`; `icmp` for source `10.128.0.0/9`, which covers min `10.128.0.1` to max `10.255.255.254` IP addresses  
Default allow `rdp` | Enable `tcp:3389` for source `0.0.0.0/0`  
Default allow `ssh` | Enable `tcp:22` for source `0.0.0.0/0`  
  
These default VPC network settings minimize the prerequisites for setting up cloud services, including Cloud Data Fusion. Due to concerns about network security, organizations often don't let you use the default VPC network for business operations. Without the default VPC network, you cannot create a Cloud Data Fusion public instance. Instead, [create a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip).

The default VPC network does not grant open access to resources. Instead, Identity and Access Management (IAM) controls access:

  * A validated identity is required to sign in to Google Cloud.
  * After you've logged in, you need explicit permission (for example, the Viewer role) to view Google Cloud services.



## Private instances

Some organizations require that all of their production systems be isolated from public IP addresses. A Cloud Data Fusion private instance meets that requirement in all kinds of VPC network settings.

### Private Service Connect in Cloud Data Fusion

Cloud Data Fusion instances might need to connect to resources located on-premises, on Google Cloud, or on other cloud providers. When using Cloud Data Fusion with internal IP addresses, connections to external resources are established over the VPC network in your Google Cloud project. Traffic over the network doesn't go through the public internet. When Cloud Data Fusion is provided access to your VPC using VPC network peering, there are limitations, which become apparent when you use large-scale networks.

With Private Service Connect interfaces, Cloud Data Fusion connects to your VPC without the use of VPC network peering. The [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) is a type of [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) that provides a way for Cloud Data Fusion to initiate private and secure connections to consumer VPC networks. This not only provides the flexibility and ease of access (like VPC network peering), but also provides the explicit authorization and consumer-side control that Private Service Connect offers. For more information, see [Create a private instance with Private Service Connect](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect).

## Access to data in design and execution environments

In a public instance, network communication happens over the open internet, which is not recommended for critical environments. To securely access your data sources, always execute your pipelines from a private instance in your execution environment.

## Access to sources

When accessing data sources, public and private instances:

  * make outgoing calls to Google Cloud APIs using Private Google Access
  * communicate with an execution (Managed Service for Apache Spark) environment through VPC peering



The following table compares public and private instances during design and execution for various data sources:

Data sources | Public Cloud Data Fusion instance  
(design-time) | Public Cloud Data Fusion Managed Service for Apache Spark  
(execution) | Private Cloud Data Fusion instance  
(design-time) | Private Cloud Data Fusion Managed Service for Apache Spark  
(execution)  
---|---|---|---|---  
Google Cloud source  
(after you grant permissions and set firewall rules) |  |  |  |   
On-premises source  
(after you set up VPN/Interconnect, grant permissions, and set firewall rules) |  |  |  |   
Public internet source  
(after you grant permissions and set firewall rules) |  |  |  |   
  
## What's next

  * [Access control in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/access-control)
  * [Service accounts in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts)
  * [Creating a public instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance)
  * [Creating a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
