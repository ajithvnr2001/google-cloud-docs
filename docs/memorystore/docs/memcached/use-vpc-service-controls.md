---
url: https://docs.cloud.google.com/memorystore/docs/memcached/use-vpc-service-controls/
title: Use VPC Service Controls with Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:44.394164+00:00
---

# Use VPC Service Controls with Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/use-vpc-service-controls/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Use VPC Service Controls with Memorystore for Memcached Stay organized with collections  Save and categorize content based on your preferences. 

You can protect your Memorystore for Memcached instances using VPC Service Controls.

VPC Service Controls protect against data exfiltration and provide an extra layer of security for your instances. For more information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Once the Memorystore for Memcached API is protected by your service perimeter, Memorystore for Memcached API requests coming from clients outside of the perimeter must have the proper access level rules.

## Protecting your Memcached instances using VPC Service Controls

  1. [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  2. Add the Memorystore for Memcached API to your service perimeter. For instructions on adding a service to your service perimeter, see [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).




## Configuration requirements

If you use both Shared VPC and VPC Service Controls, you must have the host project that provides the network and the service project that contains the Memcached instance inside the same perimeter in order for Memcached requests to succeed. Otherwise, requests between the service project instance and the host project network are be blocked by the VPC Service Controls service perimeter.

At any time, separating the host project and service project with a perimeter can cause a Memcached instance failure, in addition to blocked requests.

## Limitations of VPC Service Controls for Memcached instances

For a list of VPC Service Controls limitations for Memorystore, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_memstore-memcache)

## What's next

  * Learn more about Auto Discovery with the [Auto Discovery service overview](https://docs.cloud.google.com/memorystore/docs/memcached/auto-discovery-overview).
  * View the available [Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
