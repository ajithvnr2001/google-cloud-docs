---
url: https://docs.cloud.google.com/memorystore/docs/memcached/provisioning/
title: Provisioning Memcached instances \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:48.337975+00:00
---

# Provisioning Memcached instances  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/provisioning/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Provisioning Memcached instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for initially sizing and configuring your instance.

For instance creation instructions, see [Creating and managing Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/creating-managing-instances).

For details on Memcached instance settings, see [Instance and node properties](https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties).

#### Number of nodes

You should choose an appropriate number of nodes for the level of fail-proofing you want. The greater the number of nodes, the less data lost should an individual node fail. We recommend that you use 3 nodes for small instances, 10 nodes for medium sized instances, and 20 nodes for large instances. 20 nodes is the maximum number of nodes you can provision for a single instance.

#### Instance and node size

In order to choose your initial instance size, you should first estimate how much data your application will require. Estimate the average key size and the number of keys you expect your application to write. This number can change, but estimating the size of your data is a good start for choosing instance size. Then, divide the total instance size by the number of nodes you want to provision.

**Important:** Memory per node is constrained by the number of vCPUs that the node has. You can provision up to 8 GB of memory for every vCPU, and must provision at least 0.9GB for every vCPU. See [Instance and node properties](https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties#instance_settings) for more details.

#### Number of vCPUs/cores

Your vCPU allocation depends on your preference for price vs. speed. More vCPUs provide more processing power, up to a point. 4 vCPUs per node are sufficient for most use cases.

The number of vCPUs you choose impacts the amount of memory per node you must provision. See the note in Instance and node size for more details.

#### Network options

Memorystore for Memcached uses VPC networking by default and is compatible with Shared VPC, should you or your organization wish to use Shared VPC. You must establish a private services access for a network before you can create a Memcached instance with that network. See [Networking](https://docs.cloud.google.com/memorystore/docs/memcached/networking) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
