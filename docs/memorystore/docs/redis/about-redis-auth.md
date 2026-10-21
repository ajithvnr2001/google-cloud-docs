---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-redis-auth/
title: About Redis AUTH \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:53.028918+00:00
---

# About Redis AUTH  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-redis-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About Redis AUTH Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of [AUTH](https://redis.io/commands/auth) on Memorystore for Redis.

For instructions on managing AUTH for your Redis instance, see [Managing Redis AUTH](https://docs.cloud.google.com/memorystore/docs/redis/managing-auth).

## AUTH behavior

Using AUTH is optional for Memorystore for Redis.

A connecting client starts by sending the [AUTH](https://redis.io/commands/auth) command followed by the Redis instance's AUTH string. Every AUTH string is a [Universally Unique Identifier (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier). Each Redis instance with AUTH enabled has a unique AUTH string.

If you enable the AUTH feature on your Memorystore for Redis instance, then incoming client connections must authenticate to connect. After a client authenticates with an AUTH string, it remains authenticated for the lifetime of that connection, even if you change the AUTH string.

For Memorystore for Redis, the AUTH string is automatically generated after AUTH is enabled on the instance. The AUTH string is a randomly generated string of 36 characters that is exclusive to each Memorystore instance. The AUTH string is uniquely generated each time that AUTH is enabled. Therefore, the AUTH string can be changed if necessary by toggling AUTH from off to on.

Like every command, if [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption) is not enabled, there is no guarantee that the command is encrypted in-transit end to end. This is because there is no guarantee that the client traffic is meeting the [VPC network level based encryption on Google Cloud encryption standards](https://docs.cloud.google.com/docs/security/encryption-in-transit#virtual-network).

### AUTH impact on client connections

This section explains how changing the AUTH status of a Memorystore for Redis instance affects the client connections on that instance. An instance can have the following types of client connections:

  * **Established connection** : a client connects to an instance, but isn't authenticated against the instance.
  * **Authenticated connection** : a client connects to an instance and authenticates against the instance.



#### Behavior

The following table lists the actions for changing the AUTH status of each version of an instance and how those actions impact the client connections on the instance.

**Important** : The exact behavior that you experience might differ depending on the specific tools or client libraries that you use to connect to your instance.Action | Versions 3.2 - 5.0 | Versions 6.x - 7.2  
---|---|---  
Enabling | If you enable AUTH, then Memorystore for Redis rejects the commands, regardless of whether the connections are established. | Commands from established connections continue to work. However, if the client doesn't provide the correct password upon reconnection, then the commands fail.  
Disabling | Commands from established connections continue to work. However, even if the client provides the correct password upon reconnection, the reconnection fails.  
Rotating (disabling and re-enabling) | Commands from established and authenticated connections continue to work. However, if the client doesn't provide the correct password upon reconnection, then the commands fail.  
  
#### Troubleshoot

The following table lists the error messages associated with changing the AUTH status of an instance, their applicable versions, their explanations, and how to troubleshoot them.

Error | Applicable versions | Description | Troubleshoot  
---|---|---|---  
`NOAUTH Authentication required.` | All | A client isn't authenticated against the instance, but AUTH is enabled. | Update your client configuration to authenticate with the correct password.  
`ERR invalid password.` | 3.2 - 5.0 | A client uses the AUTH command, but provides an incorrect password.  | Update your client configuration to provide the correct password.  
`ERR Client sent AUTH, but no password is set.` | 3.2 - 5.0 | A client attempts to authenticate against an instance, but AUTH is disabled. | Disable authentication in your client configuration, or enable AUTH on the instance.  
`WRONGPASS invalid username-password pair or user is disabled. ` | 6.x - 7.2 | A client uses the AUTH command, but provides an incorrect username or password. | Update your client configuration to provide the correct username and password.  
`ERR AUTH <password> called without any password configured for the default user. Are you sure your configuration is correct?` | 6.x - 7.2 | A client attempts to authenticate against an instance, but AUTH is disabled. | Disable authentication in your client configuration, or enable AUTH on the instance.  
  
## Security and privacy

AUTH helps you ensure that known entities in your organization do not unintentionally access and modify your Redis instance. AUTH does not provide security during data transportation. Also, AUTH does not protect your instance against any malicious entities that have access to your VPC network.

Make sure to limit access to your VPC network to known users and clients. See [Redis security](https://redis.io/topics/security) for additional details.

## Using AUTH with read replica enabled instances

If AUTH is enabled on an instance that also has [read replicas](https://docs.cloud.google.com/memorystore/docs/redis/read-replicas) enabled, any connection to the Redis instance requires initial authentication using the AUTH string.

## What's next

  * Perform common tasks associated with [Redis AUTH](https://docs.cloud.google.com/memorystore/docs/redis/managing-auth)
  * See the [permissions](https://docs.cloud.google.com/memorystore/docs/redis/access-control#redis_authentication_permissions) required to perform Redis AUTH tasks.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
