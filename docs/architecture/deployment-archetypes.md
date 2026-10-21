---
url: https://docs.cloud.google.com/architecture/deployment-archetypes/
title: Google Cloud deployment archetypes \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:12.801032+00:00
---

# Google Cloud deployment archetypes  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deployment-archetypes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Cloud deployment archetypes Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-09 UTC

As a cloud architect or decision maker, when you plan to deploy an application in Google Cloud, you need to choose a _deployment archetype_1 that's suitable for your application. This guide describes six deployment archetypes—zonal, regional, multi-regional, global, hybrid, and multicloud—and presents use cases and design considerations for each deployment archetype. The guide also provides a comparative analysis to help you choose the deployment archetypes that meet your requirements for availability, cost, performance, and operational efficiency.

## What is a deployment archetype?

A deployment archetype is an abstract, provider-independent model that you use as the foundation to build application-specific _deployment architectures_ that meet your business and technical requirements. Each deployment archetype specifies a combination of failure domains where an application can run. These failure domains can be one or more [Google Cloud zones or regions](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#regions_and_zones), and they can extend to include your on-premises data centers or failure domains in other cloud providers.

The following diagram shows six applications deployed in Google Cloud. Each application uses a deployment archetype that meets its specific requirements.

![Applications in Google Cloud deployed using different deployment archetypes.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/all-schema.svg)

As the preceding diagram shows, in an architecture that uses the hybrid or multicloud deployment archetype, the cloud topology is based on one of the _basic_ archetypes: zonal, regional, multi-regional, or global. In this sense, the hybrid and multicloud deployment archetypes can be considered as _composite_ deployment archetypes that include one of the basic archetypes.

**Note:** Deployment archetypes are different from [location scopes](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#location_scopes). The location scope of a Google Cloud resource defines its availability boundary. For example, the location scope of a Compute Engine VM is _zonal_. This means that if the Google Cloud zone in which a VM is provisioned has an outage, the availability of the VM is affected. However, by distributing VMs across multiple zones, you can build a highly available architecture that's based on the _regional_ deployment archetype.

Choosing a deployment archetype helps to simplify subsequent decisions regarding the Google Cloud products and features that you should use. For example, for a highly available containerized application, if you choose the regional deployment archetype, then regional Google Kubernetes Engine (GKE) clusters are more appropriate than zonal GKE clusters.

When you choose a deployment archetype for an application, you need to consider tradeoffs between factors like availability, cost, and operational complexity. For example, if an application serves users in multiple countries and needs high availability, you might choose the multi-regional deployment archetype. But for an internal application that's used by employees in a single geographical region, you might prioritize cost over availability and, therefore, choose the regional deployment archetype.

## Overview of the deployment archetypes

The following tabs provide definitions for the deployment archetypes and a summary of the use cases and design considerations for each.

### Zonal

Your application runs within a single Google Cloud zone, as shown in the following diagram:

![Zonal deployment archetype: Application deployed in a single zone.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/zonal-schema.svg)Use cases | 

  * Development and test environments.
  * Applications that don't need high availability.
  * Low-latency networking between application components.
  * Migrating commodity workloads.
  * Applications that use license-restricted software.

  
---|---  
Design considerations | 

  * Downtime during zone outages. For business continuity, you can provision a passive replica of the application in another zone in the same region. If a zone outage occurs, you can restore the application to production by using the passive replica.

  
More information | See the following sections:

  * [ Zonal deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/zonal)
  * [ Comparative analysis of all the deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes/comparison)

  
  
### Regional

Your application runs independently in two or more zones within a single Google Cloud region, as shown in the following diagram:

![Regional deployment archetype: Application deployed across multiple zones in a region.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/regional-schema.svg)Use cases | 

  * Highly available applications that serve users within a geographic area. 
  * Compliance with data residency and sovereignty requirements.

  
---|---  
Design considerations | 

  * Downtime during region outages. For business continuity, you can back up the application and data to another region. If a region outage occurs, you can use the backups in the other region to restore the application to production.
  * Cost and effort to provision and manage redundant resources.

  
More information | See the following sections:

  * [ Regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/regional)
  * [ Comparative analysis of all the deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes/comparison)

  
  
### Multi-regional

Your application runs independently in multiple zones across two or more Google Cloud regions. You can use [DNS routing policies](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies) to route incoming traffic to the regional load balancers. The regional load balancers then distribute the traffic to the zonal replicas of the application, as shown in the following diagram:

![Multi-regional deployment archetype: Application deployed across multiple regions.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/multiregional-schema.svg)Use cases | 

  * Highly available application with geographically dispersed users.
  * Applications that require low end-user latency.
  * Compliance with data residency and sovereignty requirements by using a [geofenced DNS routing policy](https://docs.cloud.google.com/dns/docs/policies-overview#geo-fenced-policy).

  
---|---  
Design considerations | 

  * Cost for cross-region data transfer and data replication.
  * Operational complexity.

  
More information | See the following sections:

  * [ Multiregional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional)
  * [ Comparative analysis of all the deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes/comparison)

  
  
### Global

Your application runs across Google Cloud regions worldwide, either as a globally distributed (location-unaware) stack or as regionally isolated stacks. A global [anycast](https://en.wikipedia.org/wiki/Anycast) load balancer distributes traffic to the region that's nearest to the user. Other components of the application stack can also be global, such as the database, cache, and object store.

The following diagram shows the globally distributed variant of the global deployment archetype. A global anycast load balancer forwards requests to an application stack that's distributed across multiple regions and that uses a globally replicated database.

![Global deployment archetype: Globally distributed stack.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/global-distributed-schema.svg)

The following diagram shows a variant of the global deployment archetype with regionally isolated application stacks. A global anycast load balancer forwards requests to an application stack in one of the regions. All the application stacks use a single, globally replicated database.

![Global deployment archetype: Regionally isolated stacks.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/global-regionally-isolated-schema.svg)Use cases | 

  * Highly available applications that serve globally dispersed users.
  * Opportunity to optimize cost and simplify operations by using global resources instead of multiple instances of regional resources.

  
---|---  
Design considerations | Costs for cross-region data transfer and data replication.   
More information | See the following sections:

  * [ Global deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/global)
  * [ Comparative analysis of all the deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes/comparison)

  
  
### Hybrid

Certain parts of your application are deployed in Google Cloud, and other parts run on-premises, as shown in the following diagram. The topology in Google Cloud can use the zonal, regional, multi-regional, or global deployment archetype.

![Hybrid deployment archetype: Application deployed across Google Cloud and on-premises.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/hybrid-schema.svg)Use cases | 

  * Disaster recovery (DR) site for on-premises workloads.
  * On-premises development for cloud applications.
  * Progressive migration to the cloud for legacy applications.
  * Enhancing on-premises applications with cloud capabilities.

  
---|---  
Design considerations | 

  * Setup effort and operational complexity.
  * Cost of redundant resources.

  
More information | See the following sections:

  * [ Hybrid deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/hybrid)
  * [ Comparative analysis of all the deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes/comparison)

  
  
### Multicloud

Some parts of your application are deployed in Google Cloud, and other parts are deployed in other cloud platforms, as shown in the following diagram. The topology in each cloud platform can use the zonal, regional, multi-regional, or global deployment archetype.

![Multicloud deployment archetype: Application deployed across Google Cloud and other cloud platforms.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/multicloud-schema.svg)Use cases | 

  * Google Cloud as the primary site and another cloud as a DR site.
  * Enhancing applications with advanced Google Cloud capabilities.

  
---|---  
Design considerations | 

  * Setup effort and operational complexity.
  * Cost of redundant resources and cross-cloud network traffic.

  
More information | See the following sections:

  * [ Multicloud deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/multicloud)
  * [ Comparative analysis of all the deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes/comparison)

  
  
## Contributors

Author: [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer

Other contributors: 

  * [Anna Berenberg](https://www.linkedin.com/in/annaberenberg) | Engineering Fellow
  * [Anshu Kak](https://www.linkedin.com/in/anshu-kak-26654a) | Distinguished Engineer
  * [Jeff Welsch](https://www.linkedin.com/in/jeffwelsch) | Director, Product Management
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Sekou Page](https://www.linkedin.com/in/sekoupage) | Outbound Product Manager
  * [Steve McGhee](https://www.linkedin.com/in/stevemcghee) | Reliability Advocate
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking



* * *

  1. Anna Berenberg and Brad Calder, [Deployment Archetypes for Cloud Applications](https://dl.acm.org/doi/10.1145/3498336), ACM Computing Surveys, Volume 55, Issue 3, Article No.: 61, pp 1-48 ↩




[ Next Zonal  arrow_forward  ](https://docs.cloud.google.com/architecture/deployment-archetypes/zonal)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
