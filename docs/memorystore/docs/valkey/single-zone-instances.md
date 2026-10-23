---
url: https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances/
title: Single-zone instances \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:50.321787+00:00
---

# Single-zone instances  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Single-zone instances Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of single-zone instances for Memorystore for Valkey.

For instructions on provisioning a single-zone instance see [Create a single-zone instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#create_a_single-zone_instance).

By default, Memorystore for Valkey distributes an instance's nodes evenly among available zones. For diagrams that show how nodes are distributed with this setup, see [High availability and replicas](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas).

Alternatively, you can choose to create a single-zone instance. Single-zone instances have lower latency than multi-zone instances because you can place your clients in the same zone as the Valkey nodes and avoid cross-zone communication.

You choose the zone distribution mode (single-zone or multi-zone) during instance creation. After it's created, the zone distribution mode can't be changed.

If you connect to a single-zone instance from a client in the same zone, then you aren't charged for [Consumer Data Processing](https://cloud.google.com/vpc/pricing#psc-consumer-data-processing). For more information, see [Network pricing](https://cloud.google.com/memorystore/docs/valkey/pricing#network-pricing).

Although we recommend provisioning a multi-zone instance with [High Availability](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas), you should use the following recommendations for single-zone instances if they apply to you:

  * If you choose to provision a single-zone instance, you should enable replicas. Replicas reduce shard hotspots and make shards more resilient against single-node failures.

  * If you choose to provision an instance without replicas, you should still use a single-zone instance. For more information, see [When to use a single-zone instance](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#when-to-use-a-single-zone-instance).




## Single-zone instance diagram example

![A diagram that shows
all nodes of an instance placed in a single zone](https://docs.cloud.google.com/static/memorystore/img/valkey-single-zone-1.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
