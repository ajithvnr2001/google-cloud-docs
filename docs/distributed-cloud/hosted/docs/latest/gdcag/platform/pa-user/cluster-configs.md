---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs/
title: Kubernetes cluster configurations \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:18.996476+00:00
---

# Kubernetes cluster configurations  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Kubernetes cluster configurations Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains the configuration options available for your Kubernetes clusters. You can create Kubernetes clusters that function within a single project, or span across multiple projects, to align with your strategy for managing container workloads in Google Distributed Cloud (GDC) air-gapped. Cluster configurations also offer different permissions-based controls for administrative actions, so GDC can manage your container workload settings or you can manually configure them based on your use case for more flexibility.

This document is for the following audience groups:

  * IT administrators from the platform administrator group who are responsible for creating Kubernetes clusters to host container workloads.

  * Application developers from the application operator group who are responsible for developing container applications in an air-gapped environment.




For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Configuration options

In GDC, there are two cluster configurations that offer different levels of management and flexibility:

  * **Shared cluster** : a multi-project Kubernetes cluster managed by the platform administrator group that offers a full suite of integrated and managed services on the organization level.
  * **Standard cluster** : a single-project, self-service Kubernetes cluster managed by the application operator group that offers greater flexibility for custom workloads that might conflict with the managed services in a shared environment.



The following table describes the differences between the shared and standard Kubernetes clusters:

Feature | Shared clusters | Standard clusters  
---|---|---  
Owner | Platform administrator group | Application operator group  
Cluster administrator | Platform administrator group | Platform administrator group or application operator group  
Tenancy | Multiple projects  | Single project  
Lifecycle Management | Create, Read, Update, Delete, and Upgrade | Create, Read, Update, Delete, and Upgrade  
Monitoring | Prometheus with Grafana Dashboards for Kubernetes | Prometheus with Grafana Dashboards for Kubernetes  
Ingress and egress across projects | Managed by GDC | Configurable  
Backup and restore | Cluster, project, and workload | Cluster, project, and workload  
Kubernetes namespace management | Managed by GDC | Configurable  
Custom resource and controller | Managed by GDC | Configurable  
Logging | Managed by GDC | Managed by GDC  
Audit and Billing | Managed by GDC | Configurable  
Resource type | Zonal only | Zonal only  
Surface support | GDC console, API, and Terraform | GDC console, API, and Terraform  
Managed services | Includes a comprehensive set of protected services that are not configurable. | Includes a minimal set of essential services, providing more service flexibility.  
Marketplace services | Includes integration with marketplace services. | Not available for integration.  
  
For more information, see the following cluster configuration sections.

### Shared cluster

The shared cluster provides a system-managed cluster that includes a set of protected services, such as Istio, Gatekeeper, Managed Harbor Service, and Nginx. The system-managed approach for your cluster provides an opinionated Kubernetes cluster configuration that runs in the `platform` namespace, and can attach to any of your existing projects.

Because the shared cluster can span multiple projects, it is organization-scoped, which means its availability to some audience groups is limited. The platform administrator group primarily creates and manages the shared cluster with very little oversight from application developers.

Cross-project ingress and egress networking traffic is managed by GDC. Networking policies are typically handled using a [project network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview).

The primary use cases for the shared cluster are the following:

  * You need a cluster that offers a full ecosystem of managed capabilities by default with little customization required.
  * You want to manage your container workloads across multiple projects.
  * You have no requirements for migrating workloads from existing cloud environments.



For more information about creating a shared cluster, see [Create a shared cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-user-cluster).

### Standard cluster

The standard cluster provides a configurable Kubernetes cluster that includes a minimal set of services, such as Prometheus and Grafana. Standard clusters include only essential services for necessary Kubernetes container workload functionality, letting you install additional services to customize the cluster for your use case.

The standard cluster is scoped within a project only, which gives application developers that are confined within a project direct control over how it functions. The application operator group primarily creates and manages the standard cluster with very little oversight from platform administrators.

In many cases, application developers control cluster networking using standard Kubernetes networking APIs, instead of relying on GDC-specific networking configurations. However, standard clusters can configure a subset of GDC-specific networking configurations, such as the following:

  * Policies 
    * [Intra-project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#create-standard-cluster-intra)
    * [Cross-project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic#create-standard-cluster-cross)
    * [Organization-external project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/organization-external-traffic#create-standard-cluster-org-external)
  * Load balancing 
    * [Internal load balancing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service#create-internal-load-balancer-standard)
    * [External load balancing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service#create-external-load-balancer-standard)
  * Cloud NAT 
    * [Cloud NAT gateways](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-standard-clusters)



The primary use cases for the standard cluster are the following:

  * You need a cluster that offers minimal services by default, which allows for comprehensive configurations to fit your needs.
  * You want more control over deeper Kubernetes constructs like custom resource definitions or namespaces.
  * You want to manage your container workloads within a single project only.
  * You have existing container workloads on an existing cloud environment you want to migrate into your GDC air-gapped environment.



For more information about creating a standard cluster, see [Create a standard cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster).

## What's next

  * [Deploy a container app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/deploy-container-workloads)
  * [High availability for your apps](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
