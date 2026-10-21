---
url: https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional/
title: Google Cloud multi-regional deployment archetype \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:25.408403+00:00
---

# Google Cloud multi-regional deployment archetype  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Cloud multi-regional deployment archetype Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-09 UTC

This section of the [Google Cloud deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes) guide describes the multi-regional deployment archetype.

In a cloud architecture that uses the multi-regional deployment archetype, the application runs in two or more [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). Application data is replicated across all the regions in the architecture. To help ensure fast and synchronous replication of data, the regions are typically within a continent.

The following diagram shows the cloud topology for an application that runs in two Google Cloud regions:

![Multi-regional deployment archetype.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/multiregional.svg)

The preceding diagram shows two isolated multi-tier application stacks that run independently in two Google Cloud regions. In each region, the application runs in three zones. The databases in the two regions are replicated. If the workload has a low recovery point objective (RPO) or if it requires strong cross-region consistency of data, then the database replication needs to be synchronous. Otherwise, the databases can be replicated asynchronously. User requests are routed to regional load balancers by using [DNS routing policies](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies). If an outage occurs in any one of the two regions, DNS routes user requests to the load balancer in the other region.

## Use cases

The following sections provide examples of use cases for which the multi-regional deployment archetype is an appropriate choice.

### High availability for geographically dispersed users

We recommend a multi-regional deployment for applications that are business-critical and where high availability and robustness against region outages are essential. If a region becomes unavailable for any reason (even a large-scale disruption caused by a natural disaster), users of the application don't experience any downtime. Traffic is routed to the application in the other available regions. If data is replicated synchronously, the recovery time objective (RTO) is near zero.

### Low latency for application users

If your users are within a specific geographical area, such as a continent, you can use a multi-regional deployment to achieve an optimal balance between availability and performance. When one of the regions has an outage, the global load balancer sends requests that originate in that region to another region. Users don't perceive significant performance impact because the regions are within a geographical area.

### Compliance with data residency and sovereignty requirements

The multi-regional deployment archetype can help you meet regulatory requirements for [data residency and operational sovereignty](https://cloudsovereignty.withgoogle.com/). For example, a country in Europe might require that all user data be stored and accessed in data centers that are located physically within the country. You can deploy the application to [Google Cloud regions in Europe](https://cloud.google.com/about/locations#europe) and use DNS with a [geofenced routing policy](https://docs.cloud.google.com/dns/docs/policies-overview#geo-fenced-policy) to route traffic to the appropriate region.

## Design considerations

When you provision and manage redundant resources across locations, the volume of cross-location network traffic can be high. You also store and replicate data across multiple regions. When you build an architecture that uses the multi-regional deployment archetype, consider the potentially higher cost of cloud resources and network traffic, and the complexity of operating the deployment. For business-critical applications, the availability advantage of a multi-region architecture might outweigh the increased cost and operational complexity.

## Reference architecture

For a reference architecture that you can use to design a multi-regional deployment on Compute Engine VMs, see [Multi-regional deployment on Compute Engine](https://docs.cloud.google.com/architecture/multiregional-vms).

[ Previous arrow_back  Regional  ](https://docs.cloud.google.com/architecture/deployment-archetypes/regional)

[ Next Global  arrow_forward  ](https://docs.cloud.google.com/architecture/deployment-archetypes/global)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
