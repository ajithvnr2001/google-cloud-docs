---
url: https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/
title: Use RIOT Live Migration to migrate to Redis Enterprise Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:50:46.622896+00:00
---

# Use RIOT Live Migration to migrate to Redis Enterprise Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Use RIOT Live Migration to migrate to Redis Enterprise Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-01-29 UTC

By: Gilbert Lau, Principal Cloud Architect, [Redis](https://redis.io/)

This document describes an architecture to migrate from Redis compatible sources like Redis Open Source (Redis OSS), AWS ElastiCache, and Azure Cache for Redis to fully managed Redis Enterprise Cloud in Google Cloud using the [Redis Input and Output Tool (RIOT)](https://developer.redis.com/riot/) Live Migration service. This document is intended for database architects, database administrators, and database engineers who want to migrate from Redis-compatible sources to fully managed Redis Enterprise Cloud.

Redis Enterprise Cloud is a fully managed, enterprise-grade Redis solution that can help support your mission-critical applications. Compared to Redis-compatible sources, it provides enhanced scalability, availability, security, and operational efficiency. By using RIOT—a free, command-line utility—you can migrate your data from Redis to Redis Enterprise Cloud without any service interruption or downtime.

## Architecture

The following diagram shows the migration architecture:

![Redis-compatible sources are migrated through RIOT to Redis Enterprise Cloud.](https://docs.cloud.google.com/static/architecture/images/riot-live-migration-redis-enterprise-cloud-architecture.svg)

In the diagram, RIOT Live Migration Service is used to migrate Redis-compatible sources to Redis Enterprise Cloud.

The architecture contains the following components:

  * **Source** : Redis-compatible sources like Redis OSS, AWS ElastiCache, and Azure Redis.
  * **Target** : Redis Enterprise Cloud running in a Redis managed VPC.
  * **Migration Service** : RIOT running on [Compute Engine virtual machines (VMs)](https://docs.cloud.google.com/compute).



## Products used

This reference architecture uses the following Google Cloud and third-party products:

  * [ Compute Engine](https://cloud.google.com/compute): A secure and customizable compute service that lets you create and run VMs on Google's infrastructure.
  * [ RIOT Live Migration](https://developer.redis.com/riot/): A free, command-line utility that's designed to help you get data in and out of Redis.
  * [ Redis Enterprise Cloud on Google Cloud](https://console.cloud.google.com/marketplace/product/redis-marketplace-isaas/redis-enterprise-cloud-flexible-plan): A fully managed, enterprise-grade Redis solution that can help support your mission-critical applications. 



## Use case

Redis offers sub-millisecond latency, advanced data structure support, resiliency, and open source portability. However, it can be difficult to scale self-managed Redis-compatible sources to meet the demanding workloads of enterprises while maintaining ultra-low latencies. When you outgrow your self-managed Redis cluster deployment, you might struggle to scale. It's time-consuming and error-prone to architect a highly available solution and manage replication. Scaling also presents logistic challenges and costs associated with hardware management, patching, and upgrades.

To help you solve these challenges, Redis Enterprise Cloud fully integrates with Google Cloud to provide a real time database service to run, scale, and manage Redis. Redis Enterprise Cloud offers an open source core, full enterprise grade functionality and security, market-leading performance, [scalability](https://redis.com/redis-enterprise/technology/linear-scaling-redis-enterprise/), and [availability](https://redis.com/redis-enterprise/technology/highly-available-redis/) that business-critical applications require. Redis Enterprise Cloud offers sub-millisecond latency, single digit seconds failover, and five-nines uptime.

## Design alternatives

RIOT provides a flexible migration solution in and out of Redis. The following sections present potential design alternatives for this architecture. The alternatives either incur downtime or require that the target database is in a Redis [Flexible (or Annual) subscription](https://docs.redis.com/latest/rc/subscriptions/create-flexible-subscription/).

### RDB snapshots

[Redis Database (RDB) snapshot](https://redis.io/docs/management/persistence/) is one way that you can persist your data in Redis on durable storage. It performs point-in-time snapshots of your dataset, and it's commonly used to back up data in Redis. As an alternative to using RIOT to perform your migration, you can use RDB snapshot to migrate from a Redis OSS instance to Redis Enterprise. However, unlike RIOT, RDB snapshot doesn't support live migration and will incur downtime.

### Sync using Active-Passive

You can use the Redis OSS `ReplicaOf` command to configure a Redis instance as a replica of another Redis server. The command is used in the context of Redis replication, which lets you create copies of your data in different Redis instances. Like RIOT, the `ReplicaOf` command supports live migration and incurs zero downtime, but the command is built in to Redis OSS, so you don't need to install any tools.

Redis Enterprise's [Active-Passive ](https://redis.com/redis-enterprise/technology/active-passive-geo-distribution/)Geo Distribution uses the `ReplicaOf` command to scale a Redis deployment in multiple geographical locations. If the target database is in a [Flexible (or Annual) subscription](https://docs.redis.com/latest/rc/subscriptions/create-flexible-subscription/), the command can also be used to migrate data from a Redis database to Redis Enterprise Cloud subscriptions. However, the command doesn't work if the target is a Fixed subscription, and it doesn't work between flexible subscriptions from different Redis Cloud accounts.

## Design considerations

The following guidelines can help you to develop an architecture that meets your organization's requirements for reliability, cost, and performance.

### Reliability

The migration in this architecture is a one-way migration from a source Redis OSS instance to a target Redis Enterprise instance. After you complete a cutover from the source Redis OSS to the target Redis Enterprise cluster, the source isn't kept up to date with changes to the target cluster. Therefore, if you implement this architecture in a production environment, you can't switch your applications to up-to-date source instances in a fallback.

### Cost optimization

When you migrate Redis OSS instances to Redis Enterprise, we recommend that you group your target Redis Enterprise databases into [subscriptions](https://docs.redis.com/latest/rc/subscriptions/create-flexible-subscription/) so that you can lower the total cost of ownership by using multi-tenancy. For example, if you have a group of databases that are designed for development and testing, you can group them in a single subscription because they share common characteristics and network requirements. Similarly, a group of databases for production can be hosted on a different subscription.

### Performance

RIOT Live Migration supports near-zero downtime. During the migration from the source Redis OSS instance, your applications can still access the source Redis OSS instance without any impact. During the migration process, after the initial load of data from Redis OSS, RIOT Live Migration continues to migrate changes from Rediss OSS as they occur.

After the initial key-value pairs data is migrated, you perform the cutover from the source Redis OSS instance to the target Redis Enterprise instance. As part of the cutover process, you suspend client writes to the source Redis OSS instance. You then wait for RIOT to process any remaining changes from the source Redis OSS instance to the target Redis Enterprise instance.

## Deployment

To deploy this architecture, see [Deploy RIOT Live Migration to migrate from Redis Open Source to Redis Enterprise Cloud](https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/deployment).

## What's Next?

  * Read [Google Cloud data migration content](https://docs.cloud.google.com/solutions/database-migration).
  * For more in-depth documentation and best practices, review [RIOT documentation](https://developer.redis.com/riot/).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Saurabh Kumar](https://www.linkedin.com/in/saurabh-kumar-48556a19) | ISV Partner Engineer
  * [Gilbert Lau](https://www.linkedin.com/in/gilau) | Principal Cloud Architect, Redis



Other contributors: 

  * [Chris Mague](https://www.linkedin.com/in/chris-mague-35b1624) | Customer Engineer, Data Management
  * [Gabe Weiss](https://www.linkedin.com/in/weissgabriel) | Developer Advocacy Manager
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-01-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-01-29 UTC."],[],[]] 
