---
url: https://docs.cloud.google.com/memorystore/docs/memcached/best-practices/
title: Best practices \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:51.201098+00:00
---

# Best practices  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/best-practices/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page explains best practices to follow when using Memorystore for Memcached.

## Architect your application to handle cache misses

You should follow standard cache-design best practices by designing your cache to handle cache-misses and service unavailability. See the [Service Level Agreement](https://cloud.google.com/memorystore/sla) for information on Memorystore for Memcached's commitment to uptime.

Design your application so that cache misses and temporary service downtime do not stop your application from retrieving data from the underlying database which your Memcached instance supports.

Also, if you experience keyspace unavailability, wait and retry using [exponential backoff](https://wikipedia.org/wiki/Exponential_backoff). Make sure to set a time limit after which your retry strategy ceases.

## Connecting to Memcached nodes

When querying Memcached nodes with commands like `set`, `get`, and `delete`, you should connect to the IP addresses of the nodes directly. It is possible to run these commands on the Auto Discovery endpoint, however this is not recommended because it causes reduced performance for your application.

## Auto-discovery recommended

We recommend that you use the Memorystore for Memcached [Auto Discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview). This service automates cluster IP address management when adding or removing nodes from your cluster. For instructions on setting up auto-discovery for your cluster, see [Using the Auto Discovery Service](https://docs.cloud.google.com/memorystore/docs/memcached/using-auto-discovery).

## Properly configuring the `max-item-size` parameter

This section explains how to best configure the `max-item-size` parameter. For steps on adjusting this configuration parameter, see [Configuring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached). For the full list of available Memcached configuration parameters, see [Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).

#### Supported values and default values

For open source Memcached, the minimum value for `max-item-size` is `1KiB`, the maximum value is `1 GiB`, and the default value is `1 MiB`. For Memorystore for Memcached the minimum value is `512 KiB`, the maximum value is `128 MiB`, and the default value is `1 MiB`. Also, any value to which you set this configuration must be evenly divisible by `512 KiB`.

#### Caching an entry larger than the configured `max-item-size`

When you attempt to cache an entry larger than the configured `max-item-size`, Memcached fails the operation and returns false. If possible, build logic into your application to surface this error from the Memcached OSS client so that you can debug it. Attempting to cache an entry larger than the configured `max-item-size` can cause high latency for your instance.

#### Setting `max-item-size` to maximum value

You can resolve some issues with the `max-item-size` parameter by setting it to the maximum value; however, this is not a good practice, so you should not use this strategy in production. Memcached memory management is based on slabs, and storing items that are larger than the slab leads to inefficient memory allocation.

#### Avoiding `max-item-size` configuration issues

First, figure out what maximum item size is required for your cache. Set `max-item-size` to be slightly larger than the biggest item size, as a safety margin.

Note that the size of values written to your cache may change in your application over time. Also, the cluster can be misconfigured (for example, when migrating from one environment to another). An additional measure you can take is to validate the maximum item size in your application, so that the request is rejected if your application tries to cache items larger than the configured setting.

## How to balance an unbalanced Memcached cluster

#### How unbalanced clusters occur, and associated risks

In some rare circumstances, when you create a Memcached instance nodes can be unevenly distributed across [zones in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). This occurs when a zone is unavailable at that same time that you provision the cluster.

An unbalanced cluster increases the potential for data-loss because nodes are not as evenly distributed as they could be. The cluster does not automatically re-balance when the zone that was down comes back online.

#### How to rebalance your cluster

You can rebalance your cluster by temporarily increasing the number of nodes in your cluster, then scaling down the number of nodes to the original number of nodes. This scaling up and scaling down action allows the Memorystore for Memcached system to re-distribute the nodes evenly across available zones.

The success of this method for rebalancing your cluster depends upon the availability of the zones in question. Google Cloud does not currently list available/unavailable zones, so you can only tell if the zone is online if the nodes are correctly balanced during the scaling operation.

## Cloud Monitoring best practices

In order to track the performance of your cache over time, you should use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to monitor some essential Memorystore for Memcached metrics:

  * Memory usage (`memcache.googleapis.com/node/cache_memory`)
  * CPU usage percent (`memcache.googleapis.com/node/cpu/utilization`)



Tracking these two metrics over time helps you determine how efficiently your cluster is being used, and whether you should consider increasing or decreasing the size of your cluster.

For example, if the metrics indicate that memory usage and cpu usage have grown over time to over 80%, it is possible that the trend may continue. As a result you may increase your instance size early so that your cache has space to store new values as your application's resource requirements increase.

We recommend that you [set an alert](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances#create-stackdriver-alert) for when your memory usage and CPU usage reach 80%.

Alternatively, tracking these metrics over time may indicate that you are not using all of the space and CPU resources you currently have. In this case it would be more cost effective to decrease the size of your cluster.

## What's next

  * Learn more about the [Auto Discovery service](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview).
  * Review the modifiable [Memcached configuration parameters](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
