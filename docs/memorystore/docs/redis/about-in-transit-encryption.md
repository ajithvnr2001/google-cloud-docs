---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption/
title: About in-transit encryption \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:45.124864+00:00
---

# About in-transit encryption  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About in-transit encryption Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are looking for the Memorystore for Redis Cluster documentation, see [About in-transit encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption).

This page gives an overview of in-transit encryption for Memorystore for Redis.

For instructions how to encrypt a connection with in-transit encryption, see [Enabling in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption).

Memorystore for Redis only supports TLS protocol versions 1.2 or higher.

## Introduction

Memorystore for Redis supports encrypting all Redis traffic using the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. When in-transit encryption is enabled Redis clients communicate exclusively across a secure port connection. Redis clients that are not configured for TLS will be blocked. If you choose to enable in-transit encryption you are responsible for ensuring that your Redis client is capable of using the TLS protocol.

**Note:** For Standard Tier instances, replicated data is fully encrypted at the network level based on Google Cloud encryption standards.

## In-transit encryption prerequisites

In order to use in-transit encryption with Memorystore for Redis, you need:

  1. A Redis client that supports TLS or a third-party TLS sidecar
  2. A [Certificate Authority](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption#certificate_authority) installed on the client machine accessing your Redis instance



Native TLS was not supported prior to open source Redis version 6.0. As a result, not every Redis client library supports TLS. If you are using a client that does not support TLS, we recommend using the [Stunnel](https://www.stunnel.org/) third-party plugin that enables TLS for your client. See [Connect to a Redis instance securely by using Stunnel and telnet](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance#connect_to_a_redis_instance_securely_by_using_stunnel_and_telnet) for an example of how to connect to a Redis instance with Stunnel.

## Certificate Authority

A Redis instance that uses in-transit encryption has one or more unique Certificate Authorities (CA) that are used to verify the identity of the server. A CA is a string that you must download and install on the client accessing your Redis instance. A CA is valid for ten years from the date it is created. In order to ensure service continuity, the new CA must be installed on clients of the Redis instance before the previous CA expires.

### Certificate Authority rotation

After you create an instance with in-transit encryption, a CA is valid for 10 years. In addition, five years after you create the instance, Memorystore for Redis generates a new CA and makes it available.

The old CA remains valid until its expiration date, giving you a five-year window to [download](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption#downloading_the_certificate_authority) and [install](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption#installing_a_certificate_authority_on_your_client) the new CA to clients that connect to the Redis instance. After the old CA expires, you can uninstall it from your clients.

**Important** : Because of stricter TLS certificate validation, client applications that use Python 3.13 or later might fail to connect to instances created before July 2025. To resolve this issue, either create a new instance or file a support ticket to request a CA rotation. For more information about filing a ticket, see [ Get support](https://docs.cloud.google.com/memorystore/docs/redis/getting-support). Also, for more information about rotating the CA, see [Managing Certificate Authority rotation](https://docs.cloud.google.com/memorystore/docs/redis/manage-in-transit-encryption#managing_certificate_authority_rotation).

### Server certificate rotation

Server-side certificate rotation occurs every 180 days causing a transient connection drop of a few seconds. You should have retry logic with exponential backoff in place in order to reestablish the connection. Certificate rotation does not cause a failover for Standard Tier instances.

## Connection limits for in-transit encryption

Enabling in-transit encryption on your Redis instance introduces limits on the maximum number of client connections your instance can have. The limit is dependent on your instance size. You should consider increasing the size of your Redis instance if you need more connections than what is supported by your current capacity tier.

Capacity tier | Maximum number of connections for Redis versions 4.0, 5.0, and 6.x1 | Maximum number of connections for Redis version 7.0 and later1  
---|---|---  
M1 (1-4GB)  |  1000  |  65,000   
M2 (5-10GB)  |  2,500  |  65,000   
M3 (11-35GB)  |  15,000  |  65,000   
M4 (36-100GB)  |  30,000  |  65,000   
M5 (101+GB)  |  65,000  |  65,000   
  
1These connection limits are approximate, and depend on the rate and complexity of Redis commands sent per connection.

### Monitoring connections

Since Redis instances with in-transit encryption have specific connection limits, you should [monitor](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances) the `redis.googleapis.com/clients/connected` metric to make sure you don't exceed the connection limit. If the limit is surpassed, the Redis instance rejects newly attempted connections. In this circumstance we recommend [scaling up](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances) your instance to the size that accommodates the required number of connections. If you suspect that idle connections make up a significant number of your connections, you can [proactively terminate these connections](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices#managing_idle_connections) with the `timeout` configuration parameter.

## Performance impact of enabling in-transit encryption

The in-transit encryption feature encrypts and decrypts data, which comes with processing overhead. As a result, enabling in-transit encryption can reduce performance. Also, when using in-transit encryption, each additional connection comes with as associated resource cost. To determine the latency associated with using in-transit encryption, compare application performance by benchmarking application performance with both a Redis instance that has in-transit encryption enabled and a Redis instance that has it disabled.

### Guidelines for improving performance

  * Decrease the number of client connections when possible. Establish and reuse long-running connections rather than creating on-demand short-lived connections.
  * Increase the size of your Memorystore instance (M4 or larger is recommended).
  * Increase the CPU resources of the Memorystore client host machine. Client machines with a higher CPU count yields better performance. If using a Compute Engine VM, we recommend [compute optimized](https://docs.cloud.google.com/compute/docs/machine-types#compute-optimized_machine_type_family) instances.
  * Decrease the payload size associated with application traffic because larger payloads require more round trips.



## In-transit encryption impact on memory usage

Enabling in-transit encryption reserves some of your Redis instance memory for the feature. All other things being equal, with in-transit encryption enabled, the value for the System Memory Usage Ratio metric is higher because of the additional overhead memory used by the feature.

## Redis version 7.0 performance improvements

Using Redis version 7.0 on Memorystore for Redis improves the performance of in-transit encryption. To take advantage of these performance improvements, consider [upgrading your instance](https://docs.cloud.google.com/memorystore/docs/redis/upgrade-redis-version) to use Redis version 7.0. By using this version, Memorystore for Redis doesn't drop connections that you use to rotate server certificates or perform update operations.

## What's next

  * View instructions on [Enabling in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption).
  * Read the [AUTH feature overview](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview).
  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/redis/access-control#in-transit_encryption_permissions) needed in order to perform in-transit encryption management tasks.
  * Learn how to [connect](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance#connect_to_a_redis_instance_securely_by_using_stunnel_and_telnet) to a Redis instance that has in-transit encryption enabled.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
