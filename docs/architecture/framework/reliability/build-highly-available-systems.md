---
url: https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems/
title: Build highly available systems through resource redundancy \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:09.401916+00:00
---

# Build highly available systems through resource redundancy  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Build highly available systems through resource redundancy Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-30 UTC

This principle in the reliability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to plan, build, and manage resource redundancy, which can help you to avoid failures.

This principle is relevant to the _scoping_ [focus area](https://docs.cloud.google.com/architecture/framework/reliability#focus-areas) of reliability.

## Principle overview

After you [decide the level of reliability](https://docs.cloud.google.com/architecture/framework/reliability/set-targets) that you need, you must design your systems to avoid any [single points of failure](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#avoid_single_points_of_failure). Every critical component in the system must be replicated across multiple machines, zones, and [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). For example, a critical database can't be located in only one region, and a metadata server can't be deployed in only one single zone or region. In those examples, if the sole zone or region has an outage, the system has a global outage.

## Recommendations

To build redundant systems, consider the recommendations in the following subsections.

### Identify failure domains and replicate services

Map out your system's [failure domains](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks), from individual VMs to regions, and design for redundancy across the failure domains.

To ensure high availability, distribute and replicate your services and applications across multiple zones and regions. Configure the system for automatic failover to make sure that the services and applications continue to be available in the event of zone or region outages.

For examples of multi-zone and multi-region architectures, see [Design reliable infrastructure for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#deployment_architectures).

### Detect and address issues promptly

Continuously track the status of your failure domains to detect and address issues promptly.

You can monitor the current status of Google Cloud services in all regions by using the [Google Cloud Service Health dashboard](https://status.cloud.google.com/). You can also view incidents relevant to your project by using [Personalized Service Health](https://cloud.google.com/service-health). You can use load balancers to detect resource health and automatically route traffic to healthy backends. For more information, see [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

### Test failover scenarios

Like a fire drill, regularly simulate failures to validate the effectiveness of your replication and failover strategies.

For more information, see [Simulate a zone outage for a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage) and [Simulate a zone failure in GKE regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/simulate-zone-failure).

[ Previous arrow_back  Set realistic targets for reliability  ](https://docs.cloud.google.com/architecture/framework/reliability/set-targets)

[ Next Take advantage of horizontal scalability  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/reliability/horizontal-scalability)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-30 UTC."],[],[]] 
