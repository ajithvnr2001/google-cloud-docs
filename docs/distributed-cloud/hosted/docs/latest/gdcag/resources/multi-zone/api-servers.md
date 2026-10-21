---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers/
title: Global and zonal resources \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:35.163609+00:00
---

# Global and zonal resources  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Global and zonal resources Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the differences between global and zonal resources, and how they operate in a multi-zone universe. Google Distributed Cloud (GDC) air-gapped provides different deployment areas for your resources so you can implement high availability strategies for your workloads and services. You must understand the multi-zone architecture and how resources span those zones to effectively plan for highly available applications.

This document is for the following audience groups:

  * Platform administrators, such as IT administrators, who are responsible for developing disaster recovery workflows.
  * Application operators, such as application developers, who are responsible for developing and maintaining applications in a GDC universe.



For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Resource types in GDC

GDC air-gapped operates as a multi-zone universe. This operating model uses two resource types:

  * **Zonal resource** : operates within a single zone independently. A zonal outage can affect a zonal resource because the resource doesn't function outside the zone. You deploy a zonal resource to the zonal management API server, also known as the _management API server_.
  * **Global resource** : operates with redundancy across multiple zones for fault tolerance, and is accessible by any resource in any zone. You deploy a global resource to the global management API server, also known as the _global API server_.



Zonal and global resources are managed differently by the GDC system with the use of distinct management API servers. An API server provides a single endpoint for creating, managing, and deleting API resources with a strongly consistent storage backend. GDC provides interfaces so you can effectively manage your resources in the various API servers within your universe.

There is always only one global API server for your universe. Likewise, there is a zonal management API server for each zone that you operate. Even if you operate in a single zone environment, there is one global API server and a zonal management API server for the single zone.

![A universe manages a global API server that spans all zones, and zonal API servers dedicated for each zone.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/mz-api-servers.png)

This diagram illustrates a three zone GDC universe. Each zone has an independent zonal management API server, which manages the zonal resources that live within the scope of that zone. The universe also provides a global API server, which manages the global resources, such as projects, that span all zones.

You must have an understanding of GDC's global resource management architecture to appropriately [deploy your resources for high availability](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview). While some resources can be deployed both globally or operate in a single zone independently, there are others that are global or zonal only. Refer to the appropriate documentation of a resource type for more information.

## Interfaces for resource management

GDC provides multiple surfaces that each provide mechanisms to appropriately deploy your zonal or global resource to a designated API server:

  * **GDC console**: a console interface that gives access to your resources across your universe.
  * **gdcloud CLI**: a dedicated CLI tool for GDC air-gapped, which gives zonal and global configurations and flags to manage all resource types.
  * **Management APIs**: management plane APIs that give you total control over fine-tuning your resource types zonally and globally.
  * **Terraform**: an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure zonally and globally.

**Note:** The GDC console is based on the underlying GDC APIs. However, there might be some gaps in functionality between the GDC console and the API and the gdcloud CLI.

You can choose the surface to manage your resources based on your needs and preferences. For more information about how to use each surface to manage your resources in a multi-zone universe, see [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones).

### GDC console

The GDC console for a given organization is accessible from every zone within the same universe. Therefore, you can use the GDC console to manage all global and zonal resources within an organization.

The GDC console provides several ways to view and manage your resources based on their deployment location:

  * **Navigate using a fully qualified domain name (FQDN):** use the global FQDN to automatically resolve to the most appropriate zonal console endpoint. If the global FQDN fails to resolve in a disruption, you can use the zonal FQDN to navigate to a specific console endpoint in a target zone.
  * **Manage zonal resource creation:** use the zone picker on select resource creation pages to determine where to create a zonal resource. The zone picker isn't visible when you create a global resource.
  * **View existing resources across zones:** view zonal resources by zone in the GDC console. You can use the zone picker to select from which zone to view the list of resources.
  * **Be aware of zonal connectivity status:** monitor your zone's connectivity status by reviewing notifications in the GDC console. Notifications could alert you of a zonal outage that might block you from modifying resources in that zone.



For more information about how to use the GDC console to create and manage your resources, see the corresponding resource documentation.

### gdcloud CLI

The gdcloud CLI provides the following ways to interact with the zonal or global API server to manage your resources:

  * **Configure a zonal or global console URL** : sign in to the zonal or global console URL using the CLI.
  * **Define a zonal command flag** : use a zonal CLI flag for specific zone actions.



The global URL is what is configured by default when [initializing the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install#init-default-config). You can [update your gdcloud CLI configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-manage-configurations) to set zonal URLs and sign in to them to complete zone-specific tasks.

Likewise, the gdcloud CLI offers a `--zone` flag that you can set for many resource management tasks across command groups. When signed in to the global URL configuration, your CLI actions on global resources are applied to all zones for which they are in scope.

For more information about the gdcloud CLI, see the [gdcloud CLI overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview).

### Management APIs

GDC air-gapped offers two levels of management plane APIs to create and manage both global and zonal resources: global APIs and zonal APIs.

Both global and zonal APIs are Kubernetes declarative APIs served at different endpoints, and GDC resources are represented as Kubernetes custom resources in the API servers. In every organization, a zonal management API server provides the zonal API for administrators and developers to manage zonal resources, and a global management API server provides the global API to manage global resources.

For more information about APIs in GDC, see the [APIs overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/apis-overview).

### Terraform

GDC air-gapped offers a seamless way to deploy and manage all your resource types using [Terraform](https://developer.hashicorp.com/terraform). You use the [Kubernetes Provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) plugin to call the available zonal and global management APIs using industry standard Terraform lifecycle management.

For more information, see the [Terraform overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/terraform).

## What's next

  * Read the [Zones in GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview) to learn more about the composition of a GDC universe.
  * Explore the [High availability guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview) to ensure your application is resilient to local zone failures.
  * Visit the [gdcloud CLI reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) for a comprehensive list of gdcloud CLI commands that are available.
  * Visit the [API reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service-api-overview) for a comprehensive list of zonal and global APIs that are available.
  * To configure Terraform, see the [Terraform documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/configure-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
