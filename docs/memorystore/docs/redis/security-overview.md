---
url: https://docs.cloud.google.com/memorystore/docs/redis/security-overview/
title: Security overview \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:53.143319+00:00
---

# Security overview  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/security-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Security overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the security provided for your Memorystore for Redis instance.

A Memorystore for Redis instance isn't publicly accessible. Access to the instance is limited only to the clients that can [establish a private services access connection](https://docs.cloud.google.com/memorystore/docs/redis/establish-connection). For instructions on setting up connectivity, see [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking).

Management of Memorystore for Redis instances is secured using Identity and Access Management (IAM) role-based access control. For more information, see [Access control with IAM](https://docs.cloud.google.com/memorystore/docs/redis/access-control).

## Encryption

All network data to and from Memorystore for Redis is encrypted in transit at the network level according to Google Cloud's default [protection](https://docs.cloud.google.com/docs/security/encryption-in-transit) for any VM to VM traffic.

Memorystore for Redis doesn't encrypt data in memory and it doesn't use disks during replication.

## Security best practices

We recommend that you access your Memorystore for Redis instance by using trusted clients inside of the trusted environments. Don't expose the instance to the internet directly, or, in general, to an environment where untrusted clients can access the instance's TCP port or UNIX socket directly.

For example, if a web application uses an instance as a database, cache, or messaging system, then the clients inside of the frontend (the web side) of the application query the instance to generate pages or to perform operations that the user requests. In this case, the web application mediates access between the instance and the untrusted clients. These clients are the user browsers that access the web application.

We recommend that you mediate untrusted access to the instance by using a layer that does the following:

  * Implements access control lists (ACLs)
  * Validates user inputs
  * Decides which operations to perform against the instance



For more information about security from Redis' point of view, see [Redis security](https://redis.io/docs/latest/operate/oss_and_stack/management/security/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
