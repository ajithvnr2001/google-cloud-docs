---
url: https://docs.cloud.google.com/memorystore/docs/memcached/about-auto-discovery/
title: About the Auto Discovery service \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:14.615923+00:00
---

# About the Auto Discovery service  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/about-auto-discovery/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  About the Auto Discovery service Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Auto Discovery service for Memorystore for Memcached. To learn how to access and connect to the Auto Discovery service, see [Using the Auto Discovery Service](https://docs.cloud.google.com/memorystore/docs/memcached/using-auto-discovery).

The Auto Discovery service is a programmatic way for clients to automatically adapt to the addition and removal of node IP addresses that happens when you [scale](https://docs.cloud.google.com/memorystore/docs/memcached/scaling-instances) your Memcached instance.

If you don't use the Auto Discovery service, you must manually manage the node IP address list in your memcached client during scaling. Manually managing the node IP address list adds additional overhead because you must ensure that the clients are updated as the instance scales up and down. The Auto Discovery helps to automate this work for you.

You should use the Auto Discovery endpoint for its intended purpose, and not to run Memcached commands such as `get`, `set`, and `delete`.

## Overview of Auto Discovery service architecture

Memorystore for Memcached exposes the Auto Discovery service using a _discovery endpoint_. The discovery endpoint is a dedicated IP address for your instance that returns a current list of nodes in your Memcached instance. Every Memorystore for Memcached instance has a unique discovery endpoint. Once the instance is created, the IP address of the discovery endpoint does not change.

To get the instance's Auto Discovery information, you query the discovery endpoint. The discovery endpoint returns the following information:

Field | Description | Datatype | Example  
---|---|---|---  
Configuration version ID | ID that increments for each node list change | Integer | `9`  
Node List | Returns a list of current nodes and their IP addresses. | String | `node1-ip|node1-ip|node1-port node2-ip|node2-ip|node2-port`  
  
Memorystore for Memcached directly exposes the discovery endpoint, however auto discovery must also be available in your client libraries. There are two ways to have auto discovery in your clients:

  1. Use a client library that supports auto discovery.

     * [Golang](https://github.com/google/gomemcache) memcached client fork.
  2. Manually add auto discovery logic to your client library.




## Auto Discovery service behavior

The Auto Discovery service is eventually consistent. There can be a delay (on the order of seconds) while the Auto Discovery node list catches up to the current cluster configuration after a scaling operation.

Eventual consistency, in addition to the distributed nature of the service, can produce the following behavior for clients. The client logic should be designed to account for this behavior:

  * Same client on two separate queries to the Auto Discovery service can receive two different Auto Discovery responses from the service (while the service is inconsistent). However, one of the responses has a higher `Configuration version ID` which clients can use to handle the responses.

  * Two clients can receive two different Auto Discovery responses from the service (while the service is inconsistent), but they don't have a way to find which one is latest as clients don't talk to each other. While in this state, the instance can return cache misses. In this scenario, clients have to wait for the Auto Discovery service to become consistent.




## What's next

  * Learn how to [Use the Auto Discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/using-auto-discovery).
  * Review the available [Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
