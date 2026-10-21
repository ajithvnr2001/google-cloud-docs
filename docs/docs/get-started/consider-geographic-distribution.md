---
url: https://docs.cloud.google.com/docs/get-started/consider-geographic-distribution/
title: Consider geographic distribution \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:27.466376+00:00
---

# Consider geographic distribution  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/get-started/consider-geographic-distribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Consider geographic distribution Stay organized with collections  Save and categorize content based on your preferences. 

Before you create resources, consider how you plan to distribute resources geographically to meet your company's unique requirements. Administrators and architects in your organization usually make decisions about geography, and make their decisions available to people who deploy resources. For example, your company might have an [Infrastructure as Code (IaC)](https://docs.cloud.google.com/docs/terraform/iac-overview) process that automatically assigns geographies as you deploy resources.

This document provides an overview on how geography impacts your workloads.

## Distribute resources to help ensure availability

You can geographically distribute resources to meet your unique requirements, as in the following examples:

  * Latency: Ensure you have resources in zones near your users.
  * Availability: Create redundant resources in multiple regions in case of a region failure.



## Regions and zones

When you create resources, you might select the following geographic categories:

  * _Regions_ are independent geographic areas that contain zones. For example, `asia-east1` (Taiwan).

  * _Zones_ are areas that are isolated from each other within a region. For example, zone `a` in the `asia-east1` (Taiwan) region is named `asia-east1-a`.




Consider a zone as a single failure domain within a region. To deploy fault-tolerant applications with high availability and help protect against unexpected failures, you might deploy your applications across multiple zones in a region. For more information, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

Each resource has its own location dynamics. For example, see the following details about Compute Engine and Cloud Storage:

  * [Compute Engine regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones)
  * [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/bucket-locations)



### Select geographies based on resource interactions

As you create your resource distribution plan, consider resource communication across zones and regions. Resource interaction capabilities are determined by the following resource types:

  * _Global resources_ can be accessed by any other resource, across regions and zones. Examples include disk images, disk snapshots, and networks.

  * _Regional resources_ are redundantly deployed across multiple zones within a region. Regional resources can be accessed only by resources that are located in the same region. Examples include App Engine applications and [regional managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#types_of_managed_instance_groups).

  * _Multi-regional_ services are redundantly distributed within and across regions. These services optimize availability, performance, and resource efficiency. For a list of services that have one or more multi-regional locations, see [Products available by location](https://cloud.google.com/about/locations#regional-products).

  * _Zonal resources_ can be accessed only by resources that are located in the same zone. An example of a zonal resource is a Compute Engine virtual machine (VM) instance.




For example, consider the following resources:

  * Globally: a network that can be accessed by all resources.
  * In each region: IP addresses that provide external access to resources only within a single region.
  * In each zone: disks that can connect to VMs that are in the same zone.



![A global network can contain region-specific resources such as IP addresses and zone-specific resources such as VMs and disks](https://docs.cloud.google.com/static/docs/images/overview/regions-zones.svg)

[ Previous arrow_back  Resource planning overview  ](https://docs.cloud.google.com/docs/get-started/resource-planning-overview)

[ Next Organize resources  arrow_forward  ](https://docs.cloud.google.com/docs/get-started/organize-resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
