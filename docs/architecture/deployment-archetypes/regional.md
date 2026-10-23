---
url: https://docs.cloud.google.com/architecture/deployment-archetypes/regional/
title: Google Cloud regional deployment archetype \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:35.534885+00:00
---

# Google Cloud regional deployment archetype  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deployment-archetypes/regional/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Cloud regional deployment archetype Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-09 UTC

This section of the [Google Cloud deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes) guide describes the regional deployment archetype.

In a cloud architecture that uses the regional deployment archetype, instances of the application run in two or more zones within a single Google Cloud region. All the application instances use a centrally managed, shared repository of configuration files. Application data is replicated synchronously across all the zones in the architecture.

The following diagram shows the cloud topology for a highly available application that runs independently in three zones within a single Google Cloud region:

![Regional deployment archetype.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/regional.svg)

The preceding diagram shows an application with frontend and backend components that run independently in three zones in a Google Cloud region. An external load balancer forwards user requests to one of the frontends. An internal load balancer forwards traffic from the frontends to the backends. The application uses a database that's replicated across the zones. If a zone outage occurs, the database fails over to a replica in another zone.

The topology in the preceding diagram is robust against zone outages, but not against region outages. To be able to recover from region outages, you must have deployed a passive replica of the application in a second (failover) region, as shown in the following diagram:

![Regional deployment archetype with a failover region.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/regional-failover.svg)

When an outage occurs in the primary region, you must promote the database in the failover region, and use [DNS routing policies](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies) to route traffic to the load balancer in the failover region.

To optimize the cost of the failover infrastructure, you can operate the failover region at a lower capacity by deploying fewer resources.

## Use cases

The following sections provide examples of use cases for which the regional deployment archetype is an appropriate choice.

### Highly available application with users within a geographic area

We recommend the regional deployment archetype for applications that need robustness against zone outages but can tolerate some downtime caused by region outages. If any part of the application stack fails, the application continues to run if at least one functioning component with adequate capacity exists in every tier. If a zone outage occurs, the application stack continues to run in the other zones.

### Low latency for application users

If users of an application are within a geographic area, such as a single country, the regional deployment archetype can help improve the user-perceived performance of the application. You can optimize network latency for user requests by deploying the application in the Google Cloud region that's closest to your users.

### Low-latency networking between application components

A single-region architecture might be well suited for applications such as batch computing that need low-latency and high-bandwidth network connections among the compute nodes. All resources are in a single Google Cloud region, so inter-resource network traffic remains within the region. The inter-resource network latency is low, and you don't incur cross-region data transfer costs. Intra-region network costs still apply.

### Compliance with data residency and sovereignty requirements

The regional deployment archetype can help you meet regulatory requirements for [data residency and operational sovereignty](https://cloudsovereignty.withgoogle.com/). For example, a country in Europe might require that all user data be stored and accessed in data centers that are located physically within the country. To help meet this requirement, you can deploy the application to a [Google Cloud region in Europe](https://cloud.google.com/about/locations#europe).

## Design considerations

When you build an architecture that's based on the regional deployment archetype, consider the following design factors.

### Downtime during region outages

When a region outage occurs, the application is down. You can reduce the downtime caused by region outages by maintaining a passive (failover) replica of the infrastructure stack in another Google Cloud region. If an outage occurs in the primary region, you can activate the stack in the failover region and use [DNS routing policies](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies) to route traffic to the load balancer in the failover region.

### Cost of redundant resources

A multi-zone architecture typically has more cloud resources than a single-zone deployment. Consider the cost of these cloud resources when you build your architecture. For applications that need robustness against zone outages, the availability advantage of a multi-zone architecture might justify the higher cost.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

## Reference architecture

For a reference architecture that you can use to design a regional deployment on Compute Engine VMs, see [Regional deployment on Compute Engine](https://docs.cloud.google.com/architecture/regional-deployment-compute-engine).

[ Previous arrow_back  Zonal  ](https://docs.cloud.google.com/architecture/deployment-archetypes/zonal)

[ Next Multi-regional  arrow_forward  ](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
