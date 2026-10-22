---
url: https://docs.cloud.google.com/memorystore/docs/redis/faq/
title: Memorystore for Redis FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:25.532893+00:00
---

# Memorystore for Redis FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/redis/resources)



Send feedback 

#  Memorystore for Redis FAQ Stay organized with collections  Save and categorize content based on your preferences. 

How long does a failover take for a Standard Tier Redis instance?
    A failover normally takes around 30 seconds to complete.
What is the difference between Basic Tier and Standard Tier for Memorystore for Redis?
    

A Standard Tier instance provides High Availability (HA) with a replica. In cases of routine maintenance, scaling, or an instance failure, the primary cache fails over to the replica, preserving your data. A Basic Tier instance is a standalone cache that is used for applications that can withstand a cold restart/full data flush. For more information, see [Redis Tier Capabilities](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers).

To help protect your data and provide a baseline level of persistence, RDB snapshots for Standard Tier instances are enabled by default when you create a Memorystore for Redis instance using the Google Cloud console.

Is scale out cluster available on Memorystore for Redis?
    No. Memorystore for Redis Basic and Standard Tier both use a single primary node to store all Redis data. Standard Tier provides a replica node to back up your data for High Availability.
Can I use a client library that isn’t listed on the [ Client Libraries](https://docs.cloud.google.com/memorystore/docs/redis/libraries) page?
    Yes. Memorystore for Redis is compatible with any client library for Redis. See the [ Redis sample app for Compute Engine ](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gce) and the[ Redis sample app for Kubernetes](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gke) for examples of different client library setups.
Can I use a shared VPC?
    Yes, Shared VPC is supported for Memorystore for Redis. For more details, see [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking).
Can I connect to a Redis instance using the App Engine standard environment?
    Yes, but first you need to [connect the App Engine standard environment to your VPC network](https://docs.cloud.google.com/appengine/docs/standard/python/connecting-vpc).
Can I connect to a Redis instance using Cloud Run functions?
    Yes, but first you need to [connect Cloud Run functions to your VPC network](https://docs.cloud.google.com/functions/docs/connecting-vpc).
Does Memorystore for Redis use open source Redis, also known as OSS Redis?
    Yes. Memorystore for Redis uses open source Redis.
What version of Redis is currently supported?
    For a list of supported Redis versions, see [Current versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions#current_versions).
`gcloud redis` isn’t working on the command line. Why?
    You may have an older version of `gcloud` installed. Try running `gcloud components update`.
To avoid drawing additional memory from the system, does Memorystore for Redis reuse the space that's freed up after you create keys?
    The memory allocators can reuse free chunks of memory. If you free 2 GB of your 5-GB data set, and you create more keys, then you see the resident set size (RSS) stay steady and not increase as you add up to 2 GB of additional keys. The allocators reuse the 2 GB of memory that you freed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
