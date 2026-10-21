---
url: https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/assessment/
title: Define the scope of your migration to Redis Enterprise Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:35.973005+00:00
---

# Define the scope of your migration to Redis Enterprise Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/assessment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Define the scope of your migration to Redis Enterprise Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-01-29 UTC

By: Gilbert Lau, Principal Cloud Architect, [Redis](https://redis.io/)

This document describes how you define the scope of your migration to deploy [RIOT Live Migration to migrate to Redis Enterprise Cloud](https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud) in a production environment. Database architects, DevOps and SRE teams, or Network administrators can use this architecture to offer near-zero downtime migrations to their teams. This document assumes that you're familiar with using the Google Cloud CLI and Compute Engine.

To define the scope of your migration, you complete the following steps:

  1. Assess the source environment.
  2. Build an inventory of your source instances.
  3. Identify and document the migration scope and affordable downtime.
  4. Assess your deployment and administration process.



## Assess the source environment

To assess your source environment, you determine the requirements and dependencies of the resources that you want to migrate from Redis OSS, AWS ElastiCache, and Azure Cache for Redis to a fully-managed Redis Enterprise Cloud instance in Google Cloud.

The assessment phase consists of the following tasks:

  1. Build a comprehensive inventory of Redis-compatible workloads.
  2. Perform data sizing and Redis Cluster sizing: 
     * If you're using AWS ElastiCache, you can extract your database metrics by using the Redis tool [ECstats](https://github.com/Redislabs-Solution-Architects/ecstats2).
     * If you're using Azure Cache for Redis, you can extract raw usage data for your Redis instances by using the [acrp2acre](https://github.com/Redislabs-Solution-Architects/acrp2acre) tool.
  3. Review networking requirements such as [VPC peering](https://docs.redis.com/latest/rc/security/vpc-peering/) or [Private service connect](https://docs.redis.com/latest/rc/security/private-service-connect/).
  4. Calculate the total cost of ownership (TCO) of the target environment by visiting the [Redis Enterprise Cloud Pricing page](https://redis.com/cloud/pricing/).
  5. Decide on the order and priority of the workloads that you want to migrate. Create different [subscriptions](https://docs.redis.com/latest/rc/subscriptions/#flexible-plans) to consolidate databases with similar purposes such as development or test, staging, and production.



## Build an inventory of your source instances

To define the scope of your migration, you create an inventory of your source instances from Redis OSS, AWS ElastiCache, and Azure Cache for Redis. The goal of this step is to collect information about each database, such as memory limit, IOPS, and durability requirements.

  * Generic properties at the [subscription level](https://docs.redis.com/latest/rc/subscriptions/#flexible-plans): 
    * The region of your subscription
    * Active-Active geo distribution
    * Auto-tiering (receive lower total cost of ownership if memory limit is over 250GB or more)
  * Configurations for each database: 
    * Memory limit and throughput (operations per second)
    * High availability
    * Durability requirements
    * [Advanced capabilities](https://docs.redis.com/latest/rc/databases/create-database/#flexible-and-annual-module-options) such as search, JSON, time series, and probabilistic for each database
    * Connection information including port, user, and other [security options](https://docs.redis.com/latest/rc/databases/create-database/#security-section)
  * Requirements and constraints: 
    * Recovery point objective (RPO) and recovery time objective (RTO)
    * Service level agreements (SLAs)
    * Regulatory and compliance requirements (see the [Redis Customer Trust Center](https://redis.com/company/compliance-and-privacy/))
    * Authentication and security requirements



## Identify and document the migration scope and affordable downtime

To have a successful migration, you need to have a migration scope in place. To scope your migration, you document essential information that influences your migration strategy and tooling. By this stage of the assessment, you can answer the following questions:

  * Are your databases larger than 250GB? If so, you will receive a lower total cost of ownership if [auto-tiering](https://docs.redis.com/latest/rs/databases/auto-tiering/) is enabled.
  * Where are the databases located (regions and zones) and what is their proximity to applications?
  * How often does the data change?



Many components of this effort are already described in the preceding section "Build an inventory of your source instances." However, there are other aspects that you need to consider in this step, like documenting the scalability, durability, and security requirements and constraints that need to be upheld. We recommend that you review the [Redis Trust Center](https://trust.redis.com/) for industry and compliance certifications, and discuss them with your business owners and legal team if necessary.

You should also define a thorough migration scope. You can use the output from tools like [ECstats](https://github.com/Redislabs-Solution-Architects/ecstats2) and [acrp2acre](https://github.com/Redislabs-Solution-Architects/acrp2acre) to define the sizing requirements for your Redis Enterprise Cloud instances in Google Cloud. Review the attributes of each database instance, such as scalability, and security requirements. If the database size is greater than 250 GB, we recommend that you use auto-tiering. We also recommend that you group databases with similar characteristics and security profiles into a single [subscription](https://docs.redis.com/latest/rc/subscriptions/#flexible-plans). Doing so will help ensure that your database migration doesn't affect your existing SLA and business operations.

## Assess your deployment and administration process

To ensure that there aren't any unnecessary interruptions to your production environment, we recommend that you assess the operational and deployment processes of your database. The assessment should help you to determine how your databases need to be adapted to facilitate a successful migration.

  * Assess how you define and enforce [security policies](https://docs.redis.com/latest/rc/databases/create-database/#security-section) for your database instance to control access to your database.
  * Assess your [monitoring and alerting requirements](https://docs.redis.com/latest/rc/databases/create-database/#alerts-section) by defining notification emails sent to your account and the conditions that trigger them.
  * Collect and visualize your Redis Cloud metrics by using the Redis [Prometheus and Grafana integration](https://docs.redis.com/latest/rc/cloud-integrations/prometheus-integration/).



## What's next

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
