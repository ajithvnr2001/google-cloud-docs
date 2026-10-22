---
url: https://docs.cloud.google.com/architecture/deployment-archetypes/zonal/
title: Google Cloud zonal deployment archetype \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:02.959614+00:00
---

# Google Cloud zonal deployment archetype  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deployment-archetypes/zonal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Cloud zonal deployment archetype Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-09 UTC

This section of the [Google Cloud deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes) guide describes the zonal deployment archetype.

In a cloud architecture that uses the basic zonal deployment archetype, the application runs in a single Google Cloud zone, as shown in the following diagram:

![Zonal deployment archetype.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/zonal.svg)

To be able to recover from zone outages, you can use a dual-zone architecture where a passive replica of the application stack is provisioned in a second (failover) zone, as shown in the following diagram:

![Zonal deployment archetype with a failover zone.](https://docs.cloud.google.com/static/architecture/images/deployment-archetypes/zonal-failover.svg)

If an outage occurs in the primary zone, you can promote the standby database to be the primary (write) database and update the load balancer to send traffic to the frontend in the failover zone.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

## Use cases

The following are examples of use cases for which the zonal deployment archetype is an appropriate choice:

  * **Cloud development and test environments** : You can use the zonal deployment archetype to build a low-cost environment for development and testing.
  * **Applications that don't need high availability** : The zonal deployment archetype might be sufficient for applications that can tolerate downtime.
  * **Low-latency networking between application components** : A single-zone architecture might be well suited for applications such as batch computing that need low-latency and high-bandwidth network connections among the compute nodes.
  * **Migration of commodity workloads** : The zonal deployment archetype provides a cloud migration path for commodity on-premises applications for which you have no control over the code or that can't support architectures beyond a basic active-passive topology.
  * **License-restricted software** : The zonal deployment archetype might be well suited for license-restricted systems where running more than one instance at a time is either too expensive or isn't permitted.



## Design considerations

When you build an architecture that's based on the zonal deployment archetype, consider the potential downtime during zone and region outages.

### Zone outages

If the application runs in a single zone with no failover zone, then when a zone outage occurs, the application can't serve requests. To prevent this situation, you must maintain a passive replica of the infrastructure stack in another (failover) zone in the same region. If an outage occurs in the primary zone, you can promote the database in the failover zone to be the primary database, and ensure that incoming traffic is routed to the frontend in the failover zone. After Google resolves the outage, you can choose to either _fail back_ to the primary zone or make it the new failover zone.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

### Region outages

If a region outage occurs, you must wait for Google to resolve the outage and then verify that the application works as expected. If you need robustness against region outages, consider using the multi-regional deployment archetype.

## Reference architecture

For a reference architecture that you can use to design a zonal deployment on Compute Engine VMs, see [Single-zone deployment on Compute Engine](https://docs.cloud.google.com/architecture/single-zone-deployment-compute-engine).

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/architecture/deployment-archetypes)

[ Next Regional  arrow_forward  ](https://docs.cloud.google.com/architecture/deployment-archetypes/regional)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
