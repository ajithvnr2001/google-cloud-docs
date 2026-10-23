---
url: https://docs.cloud.google.com/architecture/deployment-archetypes/global/
title: Google Cloud global deployment archetype \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:32.555708+00:00
---

# Google Cloud global deployment archetype  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deployment-archetypes/global/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Cloud global deployment archetype Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-09 UTC

This section of the [Google Cloud deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes) guide describes the global deployment archetype.

In an architecture that's based on the global deployment archetype, the application runs in multiple [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) across the globe. You can deploy the application either as a distributed location-unaware stack or as multiple regionally isolated stacks. In either case, a global [anycast](https://en.wikipedia.org/wiki/Anycast) load balancer distributes traffic to the appropriate region. The application writes data to, and reads from, a synchronously replicated database that's available in all the regions, like [Spanner with multi-region configuration](https://docs.cloud.google.com/spanner/docs/instance-configurations#multi-region-configurations). Other components of the application stack can also be global, such as the cache and object store.

The following diagram shows the distributed location-unaware variant of the global deployment archetype:

![Global deployment archetype with a globally distributed application stack.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/global-distributed.svg)

The preceding diagram shows a location-unaware application stack, with frontend and backend instances (typically microservices) that are distributed across multiple zones in three Google Cloud regions. A global anycast load balancer distributes incoming traffic to an appropriate frontend instance. This distribution is based on the availability and capacity of the instances and their geographical proximity to the source of the traffic. Cross-region internal load balancers distribute traffic from the frontend instances to appropriate backend instances based on their availability and capacity. The application uses a database that is synchronously replicated and available across regions.

The following diagram shows a variant of the global deployment archetype with regionally isolated application stacks:

![Global deployment archetype with regionally isolated application stacks.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/global-regionally-isolated.svg)

The preceding diagram shows regionally isolated application stacks that run in multiple zones in two Google Cloud regions. This topology is similar to the [multi-regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional), but it uses a global anycast load balancer instead of DNS routing. The global load balancer distributes incoming traffic to a frontend in the region that's nearest to the user. Both the application stacks write data to, and read from, a database that is synchronously replicated and available across both the regions. If an outage occurs in any one of the two regions, the global load balancer sends user requests to a frontend in the other region.

## Use cases

The following sections provide examples of use cases for which the global deployment archetype is an appropriate choice.

### Highly available application for a global audience

We recommend the global deployment archetype for applications that serve users across the world and, therefore, need high availability and robustness against outages in multiple regions.

### Opportunity to optimize cost and simplify operations

With the global deployment archetype, you can use highly available global resources like a global load balancer and a global database. Compared to a multi-regional deployment, a global deployment can help lower costs and simplify operations because you provision and manage fewer resources.

## Design considerations

When you build an architecture that's based on the global deployment archetype, consider the following design factors.

### Storage, replication, and networking costs

In a globally distributed architecture, the volume of cross-location network traffic can be high compared to a regional deployment. You might also store and replicate more data. When you build an architecture that's based on the global deployment archetype, consider the potentially higher cost for data storage and networking. For business-critical applications, the availability advantage of a globally distributed architecture might outweigh the higher networking and storage costs.

### Managing changes to global resources

The opportunity to use highly available global resources can help you to optimize cost and simplify operations. However, to help ensure that the global resources don't become single points of failure (SPOF), you must carefully [manage configuration changes to global resources](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#careful_management_of_changes_to_global_resources).

## Reference architecture

For a reference architecture that you can use to design a global deployment, see [Global deployment with Compute Engine and Spanner](https://docs.cloud.google.com/architecture/global-deployment-compute-engine-spanner).

[ Previous arrow_back  Multi-regional  ](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional)

[ Next Hybrid  arrow_forward  ](https://docs.cloud.google.com/architecture/deployment-archetypes/hybrid)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
