---
url: https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview/
title: Memorystore for Memcached overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:50.040487+00:00
---

# Memorystore for Memcached overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Memorystore for Memcached overview Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces the Memorystore for Memcached service, including use cases, key concepts, and the advantages of using Memcached.

Memorystore for Memcached is a highly scalable, fully managed Memcached service for the Google Cloud. The service is built on open source Memcached and is binary and ASCII protocol compliant. This service can be accessed using standard OSS Memcached client libraries across all languages, making it easy to lift and shift existing applications with little to no code changes.

High-performance, scalable web applications often use a distributed, in-memory data store to achieve low latency and high performance. Memcached is a popular distributed in-memory key-value store used for building such applications. Some of the common Memcached use cases include caching of reference data, database query caching, and, in some cases, use as a session store.

To learn more about Memcached, see the Open Source Software (OSS) Memcached [about page](https://memcached.org/about).

Memorystore also makes it very easy to deploy a Memcached service. You deploy Memorystore and Google manages the service for you, so that you can focus on your application. Memorystore gives you all the benefits of Memcached without the overhead of installing and managing it.

## Key concepts

Memorystore for Memcached enables creating a fully-managed Memcached cluster. Before using the service, it is important to understand some key concepts and terms.

  * **Memcached Instance** represents one instance of a Memcached cluster. An instance can be comprised of a single node or a collection of nodes. All nodes in an instance must have the same memory per node, and the same number of vCPUs. Keys written to your instance are divided across all nodes in your cluster, and are not replicated.

  * **Memcached Node** is the fundamental unit of a Memcached instance. Before creating a cluster it is important to determine the number of nodes, the memory per node, and the number of vCPUs per node that will be used to create the Memcached cluster. The configuration of the node and the number of nodes depends on the size of the dataset, tolerance for key loss, and workload characteristics. Each node has an IP address and port. You can [get the list of IP addresses of all the nodes manually](https://docs.cloud.google.com/memorystore/docs/memcached/creating-managing-instances#viewing_instance_information), or by using the [Auto Discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview).

  * **Location** allows you to specify the [region](https://docs.cloud.google.com/docs/geography-and-regions) in which you deploy your instance, and how the nodes are distributed across the zones within the region.

When creating a Memorystore instance first choose the region in which to deploy the instance. The choice of region is an important consideration. You should deploy the instance in the same region where the application accessing the Memorystore instance is deployed. Accessing a Memorystore instance from a Google Cloud resource in a different region is not supported.

All Memorystore nodes are distributed within the region you designate. Within the region, you have the option to automatically distribute the nodes across all zones or select the specific zones where the nodes should be located. We recommend that you distribute the nodes automatically to allow Memorystore to distribute nodes optimally in available zones. You should avoid provisioning all nodes in a single zone, to improve your application's fault tolerance.

  * **Authorized VPC Network** designates which Google [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) your instance uses. This network is set during instance creation, and cannot be altered later. A [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection must be established on a VPC network in order for it to work with Memorystore for Memcached. Only resources and users who have access to the network can access the instance.

  * **Private services access** connection must be [established](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection) for the authorized VPC network that the Memcached instance uses before you can create the Memcached instance. We recommend that you [contact your networking/security team](https://docs.cloud.google.com/memorystore/docs/redis/networking#communicating_networking_requirements) to setup the connection before creating the instance. A private services access connection enables creating instances using internal IP addresses and provides administrators control over the internal IP address range used by Memorystore instances. For more details, see [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking).

  * **Configurations** allow setting Memcached specific configurations during instance creation, and also permit changing the configurations during runtime. For a list of supported configurations, see [Memcache configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).

  * **Auto Discovery service** provides a programmatic way for Memcached clients to discover all the nodes in the cluster. Clients can periodically query the discovery endpoint to get the list of node IP addresses. The list is typically used to distribute the keys across all the nodes using consistent hashing. Using the Auto Discovery service is particularly useful for environments that periodically scale the number of nodes in an instance. To learn more, see [Auto discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview).




The following table outlines the different features and capabilities available Memorystore for Memcached:

Features and Capabilities | Description  
---|---  
Memcached versions | The service currently supports versions 1.5.16 and 1.6.15. For more information, see [Supported versions](https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions).  
Instance sizing | An instance can have a maximum of 20 nodes. All nodes have the same configuration. A node can have a minimum of 1 vCPU and a maximum of 32 vCPUs. The minimum memory per node is 1 GB and the maximum memory supported per node is 256 GB. Memory can be specified in 1 GB increments. The maximum size of an instance is 5 TB.  
Instance scaling | You can horizontally scale your instance by increasing or decreasing the number of nodes. Vertically scaling your nodes requires recreating the instance.  
Memcached configurations | You can configure the instance for your specific workload. For a list of configurations, see [Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).  
Security and access control | 

  * Access to an instance is restricted to clients connected to your project's VPC Network. If the instance is using a Shared VPC network all clients in the Shared VPC network can access the instance. 
  * Instance level authentication is not available. 
  * Admin operations are controlled using the Identity and Access Management roles listed on the [Access control](https://docs.cloud.google.com/memorystore/docs/memcached/access-control) page. 

  
Platform support |  Memorystore for Memcached can be accessed from the following platforms.  
  
Supported platforms:   


  * Compute Engine 
  * Google Kubernetes Engine 
  * Cloud Run (Requires [Serverless VPC Access](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#connecting_to_your_vpc_network)). 
  * Cloud Run functions (Requires [Serverless VPC Access](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#connecting_to_your_vpc_network)). 
  * App Engine flexible environment. 
  * App Engine standard environment (Requires [Serverless VPC Access](https://docs.cloud.google.com/appengine/docs/standard/python/connecting-vpc#creating_a_connector)). 

  
Client Libraries | All standard Memcached client libraries across all languages are supported.  
Auto Discovery service |  Enables programmatic discovery of nodes in an instance. Auto discovery support is currently available in the following clients:   


  * Go

  
You can also modify any existing Memcached clients to add auto discovery support. For more details see [Auto Discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview).   
  
The Auto Discovery service is also compatible with most clients supporting AWS Elasticache auto discovery.   
Monitoring  |  Memorystore for Memcached provides metrics and dashboards in the Google Cloud console to monitor the instance. For more details see [Monitoring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).   
  
## What's next

  * [Create a Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/creating-managing-instances).
  * Set up Memorystore for Memcached [Networking](https://docs.cloud.google.com/memorystore/docs/memcached/networking).
  * [Establish a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
