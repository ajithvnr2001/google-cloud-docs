---
url: https://docs.cloud.google.com/memorystore/docs/valkey/operational-guidelines/
title: Operational guidelines \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:15.479808+00:00
---

# Operational guidelines  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/operational-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Operational guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The Memorystore for Valkey [Service Level Agreement (SLA)](https://cloud.google.com/memorystore/sla) excludes outages "caused by factors outside of Google's reasonable control". This page describes some of the user-controlled configurations and workloads that can cause an outage for a Memorystore for Valkey instance to be excluded.

## Introduction

Memorystore strives to give you as much control over how your instance is configured and used as possible. This includes some configurations or workload patterns that increase the risk of instance downtime. If your instance becomes unhealthy and Memorystore determines that it was out of compliance with the operational limits and best practices as described on this page, then the downtime period is not covered by (or does not count against) the Memorystore [SLA](https://cloud.google.com/memorystore/sla).

This list of operational limits and best practices is presented to inform you which configurations and workload patterns present these risks, ways to avoid them, and ways to mitigate the risks when the configuration is required for your business environment.

## Excluded configurations

This section lists configurations that can cause your instance to be excluded from the Memorystore SLA.

### General configuration requirements

If the instance is configured without [high availability](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas) (0 replicas), then the SLA does not apply. Only Memorystore for Valkey instances configured for high availability are covered by the Memorystore SLA.

### Resource constraints

The following resource constraints must be avoided to retain SLA coverage:

  * **CPU overloaded:** If your CPU utilization is consistently high, your instance is not properly sized for your workload or you are using Valkey commands improperly. If CPU resources are overloaded, you may not be covered by the [SLA](https://cloud.google.com/memorystore/sla).

  * **Memory overloaded:** If your memory usage is consistently high, your instance is not properly sized for your workload, and may not be covered by the [SLA](https://cloud.google.com/memorystore/sla).




### The `shared-core-nano` node type

The Memorystore SLA doesn't apply to instances that use the `shared-core-nano` [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type). The node type isn't suitable for most production workloads because it has insufficient performance and is too small for most production use cases.

## Best practices

[Best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices) are guidelines that you can use to receive the best possible experience with Memorystore for Valkey. The [SLA](https://cloud.google.com/memorystore/sla) might not cover downtime events that result from you not following these best practices.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
