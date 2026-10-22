---
url: https://docs.cloud.google.com/compute/docs/redis/deployment-options/
title: Deployment Options for Redis on Google Cloud \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:40.185781+00:00
---

# Deployment Options for Redis on Google Cloud  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/redis/deployment-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Deployment Options for Redis on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of [Redis](https://redis.com/) deployments and migrations to Google Cloud, including the options and tradeoffs for deploying Redis on different services, based on your requirements.

Redis is an in-memory data structure store that you can use as a database, cache, message broker, and more. Google Cloud fully supports Redis, including the following:

  * Fully managed options provided by Memorystore and Redis Ltd.

  * Self managed options using the following products:

    * [Compute Engine](https://docs.cloud.google.com/compute/docs)

    * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)

    * [OpenShift](https://cloud.google.com/solutions/redhat#red-hat-openshift-dedicated)




The best way to deploy Redis on Google Cloud depends on your specific needs and requirements. The recommendations provided in this guide are based on general best practices and considerations. It's important to thoroughly analyze your Redis workload and consult official documentation or seek professional advice for specific use cases or requirements.

## Architectures

You can deploy Redis using one of the following architectures:

Architecture | Description | Use case | Deployment options | High availability | Read throughput | Write throughput  
---|---|---|---|---|---|---  
Standard (standalone) | A single Redis node, with no read replicas and no high availability. | Cases where all data fits on one node, write and read throughput can be served by one node, and high availability is not required. | Supported on Memorystore (fully managed) and Redis open source software (OSS) (self-managed). Self-managing requires a more complex setup. Memorystore is a good option to get started quickly. | No | Single node | Single node  
HA and/or read replicas | A single Redis node for write operations, with additional nodes to provide high availability and optionally share the read load, for example, using Sentinel. | Cases where write throughput can still be served by one node, but either read throughput cannot be served by one node, or high availability is required. | Supported on Memorystore (fully managed) and Redis OSS (self managed). Redis Cluster architectures offer automated scaling, high availability, and data sharding, which are ideal for large-scale, distributed applications. To understand the tradeoffs and required maintenance efforts in manual scaling, clustering and sharding, review [ Zero-downtime scaling in Memorystore for Redis Cluster](https://cloud.google.com/blog/products/databases/zero-downtime-scaling-in-memorystore-for-redis-cluster). Self-managing requires a more complex setup. Memorystore is a good option to get started quickly. | Multi-AZ | Multi node | Single node  
Cluster (without proxies) | Several nodes split the data write operations with separate data shards. High availability and read replicas can be optionally added. | Cases where write throughput cannot be served by one node, and high availability or read replication is optionally required. | Multi-AZ | Multi node | Multi node  
Cluster (with proxies) | Several nodes split the data write operations with separate data shards. High availability and read replicas can be optionally added. Proxies are deployed on each primary node. | Cases where write throughput cannot be served by one node, and high availability or read replication is optionally required, and where it is too costly or inconvenient for client applications to be refactored to use the Redis Cluster API, or the use of proxies has other benefits. | Supported by Redis Enterprise Cloud (fully managed) or Redis Enterprise Software (self-managed). Self-managing with Redis OSS requires a more complex setup. Redis Enterprise Cloud is a good option to get started quickly. | Multi-AZ or multi-region (Redis Enterprise only) | Multi node | Single node  
  
## Deployment options

Google Cloud offers the following Redis deployment options:

  * **Fully-managed Memorystore for Redis by Google Cloud** : A fully managed, highly available, and durable Redis service managed by Google that is cost effective and fast to set up, operate, and scale. Memorystore supports both [Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview) and [standalone Redis](https://docs.cloud.google.com/memorystore/docs/redis) with optional high availability.
  * **Self or fully-managed Redis Enterprise by Redis Ltd.** : A highly available and durable Redis cluster licensed by Redis Ltd. and with two management options: managed by Redis Ltd. ("Redis Enterprise Cloud"), or self-managed ("Redis Enterprise Software") with Redis Ltd.'s support. You can procure Redis Enterprise directly from [Redis Ltd.](https://redis.com/redis-enterprise-cloud/overview), or through [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?filter=partner:Redis). Redis Ltd. supports deployments on Compute Engine , Google Kubernetes Engine and OpenShift.
  * **Self-managed Redis Open source software (OSS)** : A self-managed Redis cluster or standalone Redis with optional high availability, deployable on Compute Engine, Google Kubernetes Engine, or OpenShift.

**Note:** On April 20, 2024, [Redis Ltd. announced its adoption of Dual Source-Available Licensing](https://redis.com/blog/redis-adopts-dual-source-available-licensing/). Starting with Redis 7.4, Redis will no longer be distributed under the three-clause Berkeley Software Distribution (BSD). [The Linux Foundation launched the Open Source Valkey Community](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community) \- a Redis Open Source fork.

## Choose a Redis deployment option

This section describes how to choose a Redis deployment option that is best suited for your workload. Figure 1 provides a visual overview of the decision points:

![Redis deployment option decision tree.](https://docs.cloud.google.com/static/compute/docs/redis/decision-tree.png)**Figure 1** : Decision factors and deployment options.

### Choose a Redis management model

You can choose between one of the following management models:

  * **Fully managed deployment**. You offload deployment and management operations to the service provider. Choose this model when you need to focus on building your app and offload management tasks.

  * **Self managed deployment**. You are responsible for deployment and management operations. Choose this model if any of the following are true:

    * You have an existing operational economy of scale, and taking on managing and operating Redis makes economic sense in your organization.

    * You have a strategic preference for IaaS-only dependency.

    * You require advanced optimizations.




### Evaluate deployment options

After you choose your management model, evaluate the deployment options that are available to you.

#### Fully Managed Options

For fully managed deployments, you can use Memorystore or Redis Enterprise Cloud.

##### Memorystore

Choose Memorystore if any of the following are true:

  * You have a preference for consolidating support of managed software with Google Cloud.
  * You have a preference for optimizing for integration with Google Cloud constructs such as Identity and Access Management, APIs, org policies, quota, or Cloud Asset Inventory.
  * You require specific features only available in Memorystore (e.g, scale back in).



For more information about Memorystore, see the [Memorystore product documentation](https://docs.cloud.google.com/memorystore/docs).

###### Deployment options

  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis) (Standalone, HA)
  * [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster) (Cluster, HA)



##### Redis Enterprise Cloud

Choose Redis Enterprise Cloud if any of the following are true:

  * You require specific features only available in Redis Enterprise Cloud (for example, cross-region active-active multi-primary writes with its 99.999% SLA, RedisSearch use case).
  * You require cluster scaling for an application that does not support the Redis Cluster API.



For more information about Redis Enterprise Cloud, see the [Redis Cloud documentation](https://redis.com/cloud).

###### Procurement and billing options

  * [ Redis Enterprise Cloud on Google Cloud](https://redis.io/partners/google/), [ billed by Redis Ltd.](https://redis.io/pricing/)
  * [ Redis Enterprise Cloud on Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/redislabs-public/redis-enterprise), billed by Google



#### Self managed options

For self-managed deployments, you can choose between Redis Enterprise and Redis Open Source Software.

##### Redis Enterprise

Choose self-managed Redis Enterprise if any of the following are true:

  * Your application requires its unique features, such as automatic re-sharding for scaling out, Redis on flash, or Redis Enterprise Operator for Kubernetes.
  * Your operations team does not have the required skill set to handle complex Redis issues internally without qualified third party support.
  * You prefer the enterprise support provided by Redis Ltd., and the associated licensing costs are manageable by your organization.



For more information about Redis Enterprise Software, see the [Redis Enterprise Software documentation](https://redis.io/docs/latest/operate/rs/).

###### Deployment options

  * [ Self-managed Redis Enterprise Software on GKEor OpenShift](https://redis.com/enterprise/redis-enterprise-on-kubernetes/), with optional use of the Redis Enterprise Operator for Kubernetes
  * [Self-managed Redis Enterprise Software on Compute Engine](https://redis.io/docs/latest/operate/rs/)



###### Procurement and billing options

  * [License](https://redis.io/pricing/) and [support](https://redis.com/support/) billed by Redis Inc., while the infrastructure is billed by Google.
  * License and support is procured through [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/redislabs-public/redis-enterprise), while the infrastructure is billed by Google.



##### Redis Open Source Software

Choose self-managed Redis Open Source Software if any of the following are true:

  * You require or have a preference for full customization not otherwise possible.
  * Your operations team has the required skill set to handle complex Redis issues internally without qualified third party support.
  * You want to avoid licensing costs.
  * You have extensive in house Redis and Linux kernel tuning resources, or your use case does not require tuning.



When deploying self-managed Redis Open Source Software, choose a deployment target based on your platform strategy choice. Redis Open Source Software is deployable on Compute Engine, Google Kubernetes Engine, or OpenShift. GKE Autopilot can reduce deployment and management efforts, but may be more limited in ways such as being harder to scale in.

For more information about Redis Open Source Software, see [Redis.io](https://redis.io).

###### Additional resources

  * [ Deploy a Redis cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/upgrading-stateful-workload)



## Feature comparison

The following table summarizes the key differences between all deployment options:

Deployment characteristics | Deployment options  
---|---  
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis) and [Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster) | [Redis Enterprise Cloud](https://docs.redis.com/latest/rc/) | [Redis Enterprise software](https://docs.redis.com/latest/rs/) | Redis open source software  
Managed by | Fully managed by Google | Fully managed by Redis Ltd. | Self managed | Self managed  
Supported by | Google | Redis Ltd. | Redis Ltd. | Self supported  
Billed by | Google | Redis Ltd. or Google | Infrastructure is billed by Google. Redis Ltd. license and support is billed by Redis Ltd. or Google. | Google  
Cost elements | All costs included. Includes: infrastructure, licensing, support, and management costs. For more information, see [Memorystore pricing](https://cloud.google.com/memorystore/docs/redis/pricing). | All costs included. Includes: infrastructure, licensing, support, and management costs. For more information, see [Redis Enterprise Cloud Pricing](https://redis.io/pricing/#cloud). | Software license and support costs are included. Infrastructure usage is billed separately by Google Cloud. Management costs, including deployment, tuning, personnel and downtime are absorbed by the customer. For more information, see [Redis Enterprise Software Pricing](https://redis.io/pricing/#software). | No service or licensing fees. Infrastructure usage billed by Google Cloud. Management costs, including deployment, tuning, personnel and downtime are absorbed by the customer.  
SLA | 

  * **Redis standard:** 99.9% uptime; Less than or equal to 43.2 min/mo downtime
  * **Redis Cluster:** 99.99% uptime with multi-AZ HA; Less than or equal to 4.38 min/mo downtime.

For more information, see the [Memorystore Service Level Agreement](https://docs.cloud.google.com/memorystore/sla). | 

  * **Redis standard:** 99.9% uptime; Less than or equal to 43.2 min/mo downtime
  * **Redis Cluster:** 99.99% uptime with multi-AZ HA; Less than or equal to 4.38 min/mo downtime.
  * **Multi-region active-active HA:** 99.999% uptime; Less than or equal to 26.3 min/mo downtime.

For more information, see the [Redis Cloud Service Level Agreement](https://redis.com/legal/redis-cloud-service-level-agreement/). | Not applicable. You are responsible for uptime. | Not applicable. You are responsible for uptime.  
Free tier | No | Yes | 30 day free trial | Not applicable  
Data tiering | No | Auto tiering | Auto tiering | No  
Multi cloud | No | Yes | Manually | Possible, but involves high effort  
Multiregion active-active | No | [Yes](https://docs.redis.com/latest/rs/databases/active-active/) | Manually | Possible, but involves high effort  
Modules | 

  * [ Vector Search](https://cloud.google.com/blog/products/databases/Memorystore-for-redis-vector-search-and-langchain-integration)
  * Other [Redis modules](https://redis.io/resources/modules/) support varies, depending on licenses

| 

  * [RediSearch](https://github.com/RediSearch/RediSearch)
  * [REST JSON](https://github.com/RedisJSON/RedisJSON)
  * [RedisTimeSeries](https://github.com/RedisTimeSeries/RedisTimeSeries)
  * [RedisBloom](https://github.com/RedisBloom/RedisBloom)
  * [VectorDatabase](https://redis.com/solutions/vector-database/)
  * Other [Redis modules](https://redis.io/resources/modules/)

| 

  * [RediSearch](https://github.com/RediSearch/RediSearch)
  * [REST JSON](https://github.com/RedisJSON/RedisJSON)
  * [RedisTimeSeries](https://github.com/RedisTimeSeries/RedisTimeSeries)
  * [RedisBloom](https://github.com/RedisBloom/RedisBloom)
  * [VectorDatabase](https://redis.com/solutions/vector-database/)
  * Other [Redis modules](https://redis.io/resources/modules/)

| 

  * [ VectorDatabase](https://redis.io/docs/get-started/vector-database/)
  * Other [Redis modules](https://redis.io/resources/modules/) support varies, depending on licenses

  
Compliance | Built-in support for the different compliance regimes. See [ Compliance offerings](https://docs.cloud.google.com/security/compliance/offerings) for more information. | Built-in support for the different compliance regimes. See [Redis Trust Center](https://trust.redis.com/) for more information. | Built-in support for the different compliance regimes. See [Redis Trust Center](https://trust.redis.com/) for more information. | Manual compliance management is required. See [ Compliance offerings](https://docs.cloud.google.com/security/compliance/offerings) for more information.  
Scaling cluster writes | Scales in and out | Scales in and out | Scales out. Scaling in requires manual effort. | Self managed, requires manual effort.  
Auto rebalancing | Yes | Yes | Self managed, requires manual effort | Self managed, requires manual effort  
Adding high availability | Seamless, no redeployment required | Seamless, no redeployment required | No redeployment is required, but requires manual effort | Requires substantial manual effort - redeployment may be required depending on your original architecture  
Adding read replicas | Seamless, no redeployment required | Seamless, no redeployment required | Requires substantial manual effort - redeployment may be required depending on your original architecture | Self managed, requires manual effort  
Moving to a data-sharded Redis Cluster when outgrowing write throughput | Requires redeployment, but tooling is provided to ease effort. Clients need to be refactored to support the Redis Cluster API. | Seamless, no redeployment required | Seamless, no redeployment required | Self managed, requires manual effort  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
