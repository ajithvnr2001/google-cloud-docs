---
url: https://docs.cloud.google.com/service-directory/docs/sd-td-overview/
title: Service Directory for Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:07.191127+00:00
---

# Service Directory for Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/sd-td-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Service Directory for Cloud Service Mesh Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Deprecated:** Cloud Service Mesh's integration with Service Directory is going to be deprecated. Creating new service binding resources will be disabled.

This document provides an overview of how Cloud Service Mesh and Service Directory work together to give applications in your service mesh access to services listed in the Service Directory registry.

[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) is a service mesh control plane that enables global routing, load balancing, regional failover, and security for heterogeneous deployments. This includes deployments that use sidecars, edge or middle proxies, and proxyless gRPC clients.

Integrating Service Directory and Cloud Service Mesh makes services registered with Service Directory available to Cloud Service Mesh services.

Service Directory makes it easier to access and track your services in a single central registry. This includes Google Cloud services such as GKE, internal passthrough Network Load Balancers, internal Application Load Balancers, and on-premises and multicloud services. When a service producer creates a GKE service or a load balancer, the service or load balancer can automatically be registered with Service Directory through the integrations.

After a service is in Service Directory, you can configure Cloud Service Mesh to enable Cloud Service Mesh clients to access any service registered in Service Directory, such as internal passthrough Network Load Balancers and internal Application Load Balancers.

Using Service Directory's service registry with Cloud Service Mesh makes services in the service registry available to the applications in your mesh and to gateways configured by Cloud Service Mesh.

Registering your Cloud Service Mesh with Service Directory lets you do the following.

  * Make existing services available to Cloud Service Mesh
  * Improve coordination between service producers and consumers
  * Access services in a perimeter using an ingress point
  * Connect services across domains
  * Apply policies when accessing services



For detailed information about these capabilities, see [Use cases for Cloud Service Mesh integration with Service Directory](https://docs.cloud.google.com/service-mesh/docs/service-directory-integration#use_cases).

To integrate your services, you register a service with Service Directory, then bind the service to a Cloud Service Mesh backend service. After a binding is established, Cloud Service Mesh queries Service Directory to obtain information about the registered service and how that service can be reached.

For detailed information about how to set up Cloud Service Mesh with Service Directory, see [Set up Cloud Service Mesh with Service Directory](https://docs.cloud.google.com/service-mesh/docs/service-directory-integration-setup).

## What's next

  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To get a detailed overview of Cloud Service Mesh and Service Directory integration, see [Cloud Service Mesh integration with Service Directory](https://docs.cloud.google.com/service-mesh/docs/service-directory-integration).
  * For instructions about how to set up Cloud Service Mesh with Service Directory, see [Set up Cloud Service Mesh with Service Directory](https://docs.cloud.google.com/service-mesh/docs/service-directory-integration-setup)
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
