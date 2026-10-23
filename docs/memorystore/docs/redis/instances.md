---
url: https://docs.cloud.google.com/memorystore/docs/redis/instances/
title: Instances \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:16.433651+00:00
---

# Instances  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Instances Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are looking for the Memorystore for Redis Cluster documentation, see [Cluster and shard specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-shard-specification).

This page explains what Memorystore for Redis instances are. It also explains important settings and attributes of Redis instances. To learn how to create Redis instances, see [Creating and Managing Redis Instances](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances).

## What is a Memorystore for Redis instance?

In Memorystore for Redis, an instance refers to an in-memory Redis data store. Memorystore for Redis Instances are also referred to as Redis instances. When you create a new Memorystore for Redis instance, you are creating a new Redis data store.

## Instance IDs

Instances are identified by an Instance ID. You choose the Instance ID when you create an instance.

## Service Tiers

Memorystore for Redis offers two service tiers: [Basic and Standard](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers). The Standard Tier provides a highly available Redis instance with automatic failover.

## Capacity tiers

When you create an instance, you select a size between 1-300 GB. The instance's size puts it in one of five [capacity tiers](https://docs.cloud.google.com/memorystore/docs/redis/pricing#provisioned-capacity), which determine the maximum network performance and price of your instance.

When creating your Redis instance, determine the storage needs of your application and the network throughput you want, and size your instance accordingly.

## Networks

Redis instances can only connect using [VPC networks](https://docs.cloud.google.com/vpc/docs). Redis instances cannot connect using [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).

## Regions and zones

An instance's [_region_ and _zone_](https://docs.cloud.google.com/memorystore/docs/redis/regions) have pricing, performance, and networking implications for your application. Redis instances are available in these regions:

  * Belgium (`europe-west1`)
  * Dammam (`me-central2`)
  * Delhi (`asia-south2`)
  * Doha (`me-central1`)
  * Finland (`europe-north1`)
  * Frankfurt (`europe-west3`)
  * Hong Kong (`asia-east2`)
  * Iowa (`us-central1`)
  * Jakarta (`asia-southeast2`)
  * Las Vegas (`us-west4`)
  * London (`europe-west2`)
  * Los Angeles (`us-west2`)
  * Madrid (`europe-southwest1`)
  * Melbourne (`australia-southeast2`)
  * Milan (`europe-west8`)
  * Montréal (`northamerica-northeast1`)
  * Mumbai (`asia-south1`)
  * Netherlands (`europe-west4`)
  * Northern Virginia (`us-east4`)
  * Oregon (`us-west1`)
  * Osaka (`asia-northeast2`)
  * Paris (`europe-west9`)
  * Salt Lake City (`us-west3`)
  * Santiago (`southamerica-west1`)
  * São Paulo (`southamerica-east1`)
  * Seoul (`asia-northeast3`)
  * Singapore (`asia-southeast1`)
  * South Carolina (`us-east1`)
  * Sydney (`australia-southeast1`)
  * Taiwan (`asia-east1`)
  * Tel Aviv (`me-west1`)
  * Tokyo (`asia-northeast1`)
  * Toronto (`northamerica-northeast2`)
  * Turin (`europe-west12`)
  * Warsaw (`europe-central2`)
  * Zurich (`europe-west6`)



## What's next

  * Get started with Memorystore for Redis using the [Google Cloud console](https://docs.cloud.google.com/memorystore/docs/redis/create-instance-console) or the [Google Cloud CLI](https://docs.cloud.google.com/memorystore/docs/redis/create-instance-gcloud).
  * Learn about the [pricing](https://cloud.google.com/memorystore/pricing) of your Memorystore for Redis instance.
  * Learn how Standard Tier instances provide [high availability](https://docs.cloud.google.com/memorystore/docs/redis/high-availability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
