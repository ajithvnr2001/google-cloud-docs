---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview/
title: Zones in GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:35.258728+00:00
---

# Zones in GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Zones in GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the deployment hierarchy for Google Distributed Cloud (GDC) air-gapped, which includes universes, regions, and zones. To provide high availability for your air-gapped resources and infrastructure, you must understand the locations that host your environment and the strategic boundaries that enforce available configurations for your applications.

This document is for the following audience groups:

  * Infrastructure operators who are responsible for deploying and managing GDC zones and global infrastructure.
  * Platform administrators, such as network and IT administrators, who are responsible for configuring multi-zone services.
  * Application operators who are responsible for developing and managing applications in a GDC universe.



For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Deployment hierarchy overview

A GDC air-gapped deployment follows a hierarchical structure consisting of universes, regions, and zones.

A _universe_ is a high-level grouping of interconnected zones that share network connectivity and a control plane. Even though zones can be geographically distant, a _regional boundary_ is established when distinct zones are physically close enough to have low-latency communication.

A _zone_ is the building block of your GDC air-gapped deployment. Each zone is a self-contained implementation that doesn't require connectivity to Google Cloud at any time. A zone manages its own infrastructure, services, APIs, and tooling through a local control plane.

For example, the following diagram illustrates a GDC multi-zone universe:

![A universe consists of zones that are grouped across regions.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/gdc-universe.png)

This diagram has two regions, each existing within a single universe. Region 1 is highlighted to show three zones that each operate various zonal services, such as virtual machines (VM) and container applications. There are also global services that span all zones and regions in the universe, such as Identity and Access Management (IAM) and load balancing.

For example, you could have a GDC universe that spans across far-reaching geographic regions. Consider Region 1 existing in Virginia, USA with three zones:

  * Zone A, such as `us-virginia1-a`
  * Zone B, such as `us-virginia1-b`
  * Zone C, such as `us-virginia1-c`



Likewise, you could have Region 2 reside in the Netherlands and include zones in Amsterdam:

  * Zone A, such as `eu-ams1-a`
  * Zone B, such as `eu-ams1-b`
  * Zone C, such as `eu-ams1-c`



Zones within a region must be geographically close to each other, but regions can span great distances. For example, a zone might have a fiber distance maximum limit of 50 km to another zone within the same region, but the region can span 100s of km from another region. Contact your infrastructure operator group for more information on your specific latency requirements.

### About zones

A _zone_ contains four layers that can operate in isolation without requiring connectivity to Google Cloud or the public internet:

  * **Hardware** : the foundational equipment fully integrated into the racks of your data center. This layer provides the compute, storage, network, and GPU capacity for your system and integrated workloads.
  * **Infrastructure** : the underlying hardware management system. This layer provides interfaces that enable the software to run without needing hardware specific configurations.
  * **Service Platform** : the framework for building services on GDC. This layer provides consistency among managed services and marketplace services.
  * **Managed and Marketplace services** : the customer-facing cloud services running on GDC. This layer provides a consistent implementation of the data plane for workloads and services.



These components give you the flexibility to adjust your zonal configuration to meet your unique availability and resilience requirements. Understanding this structure gives the foundation for understanding the common air-gapped zone configurations.

## Deployment configurations

The following sections describe common deployment configurations that you can use for GDC air-gapped.

### Single zone configuration

A _single zone_ configuration lets you deploy a universe where one zone acts as the sole region. This configuration is possible because each zone operates independently. You'll typically use this setup for initial deployments or for workloads that don't require high availability or robust disaster recovery.

The main limitation for a single zone universe is that it creates a single point of failure, making your system vulnerable to outages. A single point of failure happens when you deploy resources exclusively to a single zone. [Zonal resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers#resource-types) are impacted as a group when an outage or service disruption occurs in that specific zone.

### Multi-zone configuration

A _multi-zone configuration_ lets you strategically distribute your applications and services across several zones. This setup improves your system's resilience and fault tolerance by providing geographically distributed resources.

This configuration also provides _high availability_ , which lets your application or service remain continuously accessible and operational even if a zone experiences an outage. You achieve high availability through redundancy by deploying and managing resources across multiple zones within a universe. GDC offers a [subset of services](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/multi-zone-services) that provide global capabilities so the resource is managed across multiple zones in a universe by default without manual replication. [Global resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers#resource-types) span multiple zones by default, which makes them available even during a zonal outage.

A key benefit to a multi-zone configuration is that each zone can function as a distinct disaster domain. A _disaster domain_ is a group of resources susceptible to simultaneous failure due to their shared physical location or dependency. By strategically positioning zones far enough apart, your system becomes more resilient against widespread failures.

_Zonal asymmetry_ allows for organization and hardware configurations to be different across zones in a GDC universe. Zonal asymmetry is a [Preview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview) feature starting in version 1.14.4.

## Key capabilities of a multi-zone configuration

Multi-zone configurations let you establish resilient architecture because each zone can function as distinct disaster domains. Distributing resources across these independent disaster domains lets you enhance your air-gapped systems with the key capabilities outlined in the following sections.

### High availability

You can create highly available applications to provide durable services that are able to withstand outages. High availability strategies, such as load balancing and data replication, transform fragile zonal applications into resilient and reliable global services. For more information, see [High availability for your apps](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview).

### Data protection

You can use a multi-zone configuration to keep your data secure and accessible even in the event of an outage using data protection strategies that let you set up data replication to create geographically separated backups. For more information, see [Data protection with multi-zone storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/data-protection).

### Network traffic management

Building a durable network is essential to creating a highly available GDC system. You can configure networking strategies across multiple zones to plan for failover procedures during a potential zonal outage. Balancing your network traffic across zones can also positively impact application performance. For more information, see [Network traffic management for multiple zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/networking).

### Permissions control

You can implement cross-zone roles to apply access control strategies on a global scale, which removes zone-specific permissions management that can be tedious and difficult to manage. Likewise, you can seamlessly manage authentication across zones for your human users and services with global access accounts. For more information, see [Permissions control for a multi-zone universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/permissions).

## Limitations

GDC air-gapped universes have the following limitations:

  * A universe with two zones can't provide an automated recovery strategy, regardless of region configuration, and must be recovered manually. Universes with three or more zones can trigger recovery steps automatically.
  * GDC provides regions only as a grouping concept, and doesn't provide regional services. Regions in a GDC universe are provided to closely align with public Google Cloud architecture, and for future development and planning.



## What's next

  * Learn about the [global and zonal resource types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers) available in a GDC universe.
  * Explore the [High availability guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview) to ensure your application is resilient to local zone failures.
  * Read the [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy) document for more information on how resources are managed hierarchically within a zone.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
