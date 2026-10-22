---
url: https://docs.cloud.google.com/app-hub/docs/global-regional-applications/
title: Global and regional applications \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:27.059723+00:00
---

# Global and regional applications  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/global-regional-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Global and regional applications Stay organized with collections  Save and categorize content based on your preferences. 

[App Hub is available in supported locations](https://docs.cloud.google.com/app-hub/docs/locations) to help you organize global or regional Google Cloud infrastructure resources in App Hub applications. Location support simplifies management by letting you group application components based on their geographical location and communication methods with other parts of your infrastructure.

When creating an application, you define its location as either _global_ or _regional_. This choice is fundamental in determining which services and workloads can be part of the application. Also, this choice has important implications for data handling, colocation, cost, and compliance. Global and regional applications are defined as follows:

  * **Global applications:** Functionally group services and workloads that are globally distributed or spread across multiple Google Cloud regions. For example, you can include a global Application Load Balancer service and its backend workloads distributed worldwide.

  * **Regional applications:** Functionally group services and workloads that reside entirely within a single Google Cloud region. For example, you can include a regional Application Load Balancer service and its backend workloads, all located in `us-central1`.




To make the best decision for your needs, it's crucial to understand Google Cloud regions and zones, which are designed to provide fault tolerance and high availability. Regions are independent geographic areas, and zones are deployment areas within a region, acting as single failure domains. To learn more about global and regional resources, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [Cloud locations](https://cloud.google.com/about/locations).

## Compare global and regional applications

The following table highlights the key differences and considerations to help you choose between global and regional applications:

| **Global application** | **Regional application**  
---|---|---  
**Recommended use case** | Best for applications with components that are inherently global or distributed across multiple regions. | Recommended when all application components reside within the same Google Cloud region, even if they span multiple projects.  
**Resource extent** | Can contain both global and regional Google Cloud resources from any region. | Can only contain Google Cloud resources from the _same single region_ as the application. You cannot register global components in a regional application.  
**Application metadata** | Stored across multiple regions and accessible from any Google Cloud region.  
[Data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) is not supported. | Stored within the specific region but accessible from any other Google Cloud region.  
[Data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) is not supported.  
**Examples** | Managing a global load-balanced application with backend components in various regions to provide a centralized view of the distributed system. | Managing an application with all services and workloads in `us-central1`.  
  
## Select the best location for your application

Consider the architecture and operational requirements of the business function the application represents when choosing between global and regional locations. The following comparison is based on geography considerations:

  * In general, regional applications offer significant benefits over global applications. If you want to take advantage of lower component latency, alignment with data locality requirements, potential network cost savings, and inherent consistency with region-specific Google Cloud features, opt for _regional_ applications.
  * If your application components are necessarily distributed across multiple regions or rely on global Google Cloud resources, opt for _global_ applications.



You might have Google Cloud resources located in multiple regions that don't form a single, cohesive global function. In that case, it is often best practice to define separate regional applications for components within each region. This approach maximizes the benefits of regionalization for each deployment.

Your Google Cloud resource hierarchy, which defines how you organize folders and projects, is also fundamental. A well-planned hierarchy that aligns with your application management boundaries, whether regional or global, simplifies the grouping and management of services and workloads in applications. For more information, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

### Benefits of regional applications

Global applications offer flexibility for distributed systems. However, choosing a regional location for your App Hub applications can provide significant advantages:

  * **Support data residency and compliance:** App Hub metadata doesn't offer [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency). However, a regional application helps you make sure that the actual data the underlying Google Cloud resources process and store remains within the geographic limits you select. This benefit is often crucial for complying with legal, regulatory, and organizational requirements for data locality.

  * **Reduce latency:** Colocating application components within the same region generally minimizes [network latency between components](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency), potentially improving application performance and user experience.

  * **Meet product feature requirements:** Certain Google Cloud products or features mandate that all interacting components be located in the same region. For example, a Compute Engine instance can only [attach a persistent disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_add_disk) that is in the same region. A regional App Hub application aligns inherently with such architectural constraints.

  * **Optimize cost:** Data transfer _between_ different Google Cloud regions [often incurs networking costs](https://cloud.google.com/vpc/network-pricing), whereas network traffic _within_ the same region is typically priced lower. By creating your application regionally, you can better manage and reduce cross-region network charges.

  * **Align with failure domains:** Google Cloud regions are [designed to be independent failure domains](https://cloud.google.com/about/locations). Deploying your application within a single region and using multiple zones within that region for high availability aligns your application's fault tolerance with Google Cloud's infrastructure resilience model.




## What's next

  * [Review the list of available App Hub locations](https://docs.cloud.google.com/app-hub/docs/locations)
  * [Identify App Hub supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources)
  * [Learn more about geography and regions](https://docs.cloud.google.com/docs/geography-and-regions)
  * [Review Cloud locations](https://cloud.google.com/about/locations)
  * [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
